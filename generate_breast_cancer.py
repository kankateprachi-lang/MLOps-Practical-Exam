from pathlib import Path

import pandas as pd
from sklearn.datasets import load_breast_cancer


data = load_breast_cancer(as_frame=True)
df = data.frame.copy()
df["diagnosis"] = df["target"].map(
    {
        0: "malignant",
        1: "benign",
    }
)

output_path = Path("data/raw/breast_cancer.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("Wisconsin Breast Cancer dataset generated")
print("Dataset shape:", df.shape)
print("Saved to:", output_path)
print(df.head())
