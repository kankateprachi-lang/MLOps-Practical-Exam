from pathlib import Path

import pandas as pd


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


if __name__ == "__main__":
    main()
