# Wine Classification MLOps Pipeline

An end-to-end local MLOps pipeline for classifying the scikit-learn Wine dataset using Git, DVC, Feast, and MLflow.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run

```bash
python src/collect.py
cd wine_feature_repo/feature_repo
python prepare_features.py
feast apply
feast materialize-incremental "$(date -u +'%Y-%m-%dT%H:%M:%S')"
cd ../..
python src/train.py
```

Open the MLflow UI:

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

## DVC

```bash
dvc init
mkdir -p ~/dvc-remote-storage
dvc remote add -d myremote ~/dvc-remote-storage
dvc add data/raw/wine_raw.csv
dvc push
```
