# Breast Cancer Practical 3 — Member 2

This project demonstrates data version control with DVC using scikit-learn's Wisconsin Breast Cancer dataset. Git tracks the source code and DVC metadata; a local DVC remote stores the dataset content.

## Set up and generate the dataset

Run these commands from this project directory in PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python generate_breast_cancer.py
```

The generated CSV is `data/raw/breast_cancer.csv`. DVC tracks its content, so the CSV itself is excluded from Git.

## Initialize Git and DVC

```powershell
git init
git branch -M main
dvc init
dvc add data/raw/breast_cancer.csv
git add .
git commit -m "Track Breast Cancer dataset using DVC"
```

## Configure and use a local DVC remote

The remote below is a folder beside this project. It is local to this machine and is not shared with collaborators.

```powershell
New-Item -ItemType Directory -Force ..\breast-cancer-dvc-remote
dvc remote add -d myremote ..\breast-cancer-dvc-remote
git add .dvc\config
git commit -m "Configure local DVC remote"
dvc push
dvc status
```

## Push Git metadata to GitHub

Create a separate GitHub repository for this project, then replace the URL below with its clone URL:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/breast-cancer-practical-3-member-2.git
git push -u origin main
```

The GitHub repository contains code and DVC metadata, not the contents of the local DVC remote. To share the data, configure a shared remote instead.
