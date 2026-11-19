from pathlib import Path

import pandas as pd


FEATURE_REPO = Path(__file__).resolve().parent
ROOT_DIR = FEATURE_REPO.parents[1]
INPUT_PATH = ROOT_DIR / "data" / "raw" / "wine_raw.csv"
OUTPUT_PATH = FEATURE_REPO / "data" / "wine_features.parquet"
FLOAT_FEATURES = ["alcohol", "malic_acid", "ash"]


def main() -> None:
    if not INPUT_PATH.is_file():
        raise FileNotFoundError(
            f"Wine data not found at {INPUT_PATH}. Run `python src/collect.py` first."
        )

    df = pd.read_csv(INPUT_PATH)
    df.insert(0, "sample_id", range(len(df)))
    df[FLOAT_FEATURES] = df[FLOAT_FEATURES].astype("float32")

    event_timestamps = pd.date_range(
        start="2026-01-01", periods=len(df), freq="min", tz="UTC"
    )
    df["event_timestamp"] = event_timestamps
    df["created_timestamp"] = event_timestamps

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} feature rows to {OUTPUT_PATH.relative_to(FEATURE_REPO)}")


if __name__ == "__main__":
    main()
