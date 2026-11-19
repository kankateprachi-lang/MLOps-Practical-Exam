# Wine Classification MLOps Pipeline

<<<<<<< HEAD
An end-to-end local MLOps pipeline for classifying the scikit-learn Wine dataset using Git, DVC, Feast, and MLflow.

## Setup
=======
Aim 1 builds a tracked Wine classification project with Git, DVC, Feast, and
MLflow. Commands below are run from the repository root unless noted otherwise.

## Environment

Use Python 3.10 or newer, then install the project dependencies:
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3

```bash
python -m venv .venv
source .venv/bin/activate
<<<<<<< HEAD
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
=======
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Collect and version the data

```bash
python src/collect.py
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3
dvc init
mkdir -p ~/dvc-remote-storage
dvc remote add -d myremote ~/dvc-remote-storage
dvc add data/raw/wine_raw.csv
<<<<<<< HEAD
dvc push
```
=======
git add .gitignore .dvc data/raw/wine_raw.csv.dvc data/raw/.gitignore
dvc push
```

The local DVC remote is machine-specific; choose a writable storage path on
your machine. Commit the generated DVC metadata with your Git changes.

## Register Feast features

Prepare the Parquet source and apply the feature definitions:

```bash
python wine_feature_repo/feature_repo/prepare_features.py
cd wine_feature_repo/feature_repo
feast apply
feast materialize-incremental 2026-11-19T23:59:59
cd ../..
```

Replace the materialization end time with the current UTC time when running
later. The example feature timestamps are generated from 2026-01-01.

## Train and track the model

```bash
python src/train.py
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Training reads the DVC-managed raw CSV, evaluates a stratified holdout split,
and logs parameters, metrics, and the model artifact to MLflow. The Feast repo
is registered and materialized independently; the baseline trainer does not
yet use Feast as its feature retrieval source.

## GitHub

Commit the source and Feast definitions after reviewing the generated DVC
metadata. Push only to the GitHub remote configured for this repository; do
not replace an existing remote with a placeholder URL.
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3
