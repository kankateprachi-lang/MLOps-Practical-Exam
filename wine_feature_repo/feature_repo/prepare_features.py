from pathlib import Path

import pandas as pd


<<<<<<< HEAD
def main() -> None:
    source = Path("../../data/raw/wine_raw.csv")
    output = Path("data/wine_features.parquet")

    df = pd.read_csv(source)
    df.insert(0, "sample_id", range(len(df)))
    df["event_timestamp"] = pd.date_range(start="2026-01-01", periods=len(df), freq="min")
    df["created_timestamp"] = df["event_timestamp"]

    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output, index=False)
    print(f"Saved {len(df)} feature rows to {output}")
=======
FEATURE_REPO = Path(__file__).resolve().parent
PROJECT_ROOT = FEATURE_REPO.parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "wine_raw.csv"
FEATURE_DATA_PATH = FEATURE_REPO / "data" / "wine_features.parquet"
FEATURE_COLUMNS = ["alcohol", "malic_acid", "ash"]


def main() -> None:
    if not RAW_DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Wine data not found at {RAW_DATA_PATH}. Run `python src/collect.py` first."
        )

    df = pd.read_csv(RAW_DATA_PATH)
    required_columns = set(FEATURE_COLUMNS + ["target"])
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Wine data is missing columns: {', '.join(sorted(missing_columns))}")

    df.insert(0, "sample_id", range(len(df)))
    for column in FEATURE_COLUMNS:
        df[column] = df[column].astype("float32")
    df["target"] = df["target"].astype("int64")
    df["event_timestamp"] = pd.date_range(
        start="2026-01-01", periods=len(df), freq="min", tz="UTC"
    )
    df["created_timestamp"] = df["event_timestamp"]

    FEATURE_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(FEATURE_DATA_PATH, index=False)
    print(f"Saved {len(df)} feature rows to {FEATURE_DATA_PATH.relative_to(PROJECT_ROOT)}")
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3


if __name__ == "__main__":
    main()
