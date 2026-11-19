<<<<<<< HEAD
=======
from pathlib import Path

>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


<<<<<<< HEAD
def main() -> None:
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("wine-classification")

    df = pd.read_csv("data/raw/wine_raw.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

=======
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "wine_raw.csv"


def main() -> None:
    if not RAW_DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Wine data not found at {RAW_DATA_PATH}. Run `python src/collect.py` first."
        )

    df = pd.read_csv(RAW_DATA_PATH)
    if "target" not in df.columns:
        raise ValueError(f"Expected a 'target' column in {RAW_DATA_PATH}")

    X = df.drop(columns="target")
    y = df["target"]
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

<<<<<<< HEAD
=======
    mlflow.set_tracking_uri(f"sqlite:///{(PROJECT_ROOT / 'mlflow.db').as_posix()}")
    mlflow.set_experiment("wine-classification")
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3
    with mlflow.start_run(run_name="rf_baseline"):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

<<<<<<< HEAD
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="macro")

        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)
        mlflow.log_param("test_size", 0.2)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_macro", f1)
        mlflow.sklearn.log_model(
            model,
            artifact_path="model",
            skops_trusted_types=["sklearn.tree._tree.Tree"],
        )

        print(f"Logged model with Accuracy: {acc:.4f} and F1: {f1:.4f}")
=======
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1_macro = f1_score(y_test, predictions, average="macro")

        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_macro", f1_macro)
        mlflow.sklearn.log_model(
            model,
            name="model",
            skops_trusted_types=["sklearn.tree._tree.Tree"],
        )
        print(f"Logged model with Accuracy: {accuracy:.4f} and F1: {f1_macro:.4f}")
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3


if __name__ == "__main__":
    main()
