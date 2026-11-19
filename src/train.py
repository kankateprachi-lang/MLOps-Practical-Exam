from pathlib import Path

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "raw" / "wine_raw.csv"


def main() -> None:
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Wine data not found at {DATA_PATH}. Run `python src/collect.py` first."
        )

    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    mlflow.set_tracking_uri((ROOT_DIR / "mlflow.db").as_uri().replace("file:///", "sqlite:///"))
    mlflow.set_experiment("wine-classification")

    with mlflow.start_run(run_name="rf_baseline"):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1_macro = f1_score(y_test, predictions, average="macro")

        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_macro", f1_macro)
        mlflow.sklearn.log_model(model, artifact_path="model")

        print(f"Logged model with Accuracy: {accuracy:.4f} and F1: {f1_macro:.4f}")


if __name__ == "__main__":
    main()
