# Wine Classification MLOps Pipeline

An end-to-end Wine classification baseline using Git, DVC, Feast, and MLflow.
Run the commands below from the repository root. Python dependencies are listed
in `requirements.txt`.

## 1. Set up the environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows Git Bash: source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

If this is a new repository, initialize Git and make the initial commit:

```bash
git init
git add .gitignore README.md requirements.txt src/ wine_feature_repo/
git commit -m "chore: initialize wine classification pipeline"
```

## 2. Collect and version the data

```bash
python src/collect.py
dvc init
mkdir -p ~/dvc-remote-storage
dvc remote add --local -d myremote ~/dvc-remote-storage
dvc add data/raw/wine_raw.csv
git add data/raw/wine_raw.csv.dvc data/raw/.gitignore .dvc/config
git commit -m "data: track raw wine dataset with DVC"
dvc push
```

The DVC remote path above is local to your machine and is stored in
`.dvc/config.local`, not committed. Replace it with a shared remote if your team
needs to push or pull the data. The generated CSV itself is intentionally
ignored by Git and stored through DVC.

## 3. Prepare and register Feast features

The feature repository is at `wine_feature_repo/feature_repo`. Prepare its
Parquet source and run Feast commands from that directory:

```bash
python wine_feature_repo/feature_repo/prepare_features.py
cd wine_feature_repo/feature_repo
feast apply
feast materialize-incremental "$(date -u +'%Y-%m-%dT%H:%M:%S')"
cd ../..
```

The Feast entity uses a stable integer `sample_id`, and each row receives UTC
event and creation timestamps. The feature view includes alcohol, malic acid,
ash, and the Wine class label.

## 4. Train and track the model

```bash
python src/train.py
```

Training reads the DVC-managed CSV, makes a stratified train/test split, and
logs the Random Forest parameters, accuracy, macro F1, and model artifact to a
local SQLite-backed MLflow tracking store (`mlflow.db`).

## 5. Push the project

```bash
git add src/ wine_feature_repo/ README.md requirements.txt .gitignore
git commit -m "feat: complete wine classification MLOps pipeline"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repository>.git
git push -u origin main
```

Replace the GitHub URL with your repository's URL. Keep credentials and
machine-specific DVC remote configuration out of the committed source.
