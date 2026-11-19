<<<<<<< HEAD
import pandas as pd
from sklearn.datasets import load_wine


def main() -> None:
    wine = load_wine(as_frame=True)
    df = wine.frame
    df.to_csv("data/raw/wine_raw.csv", index=False)
    print(f"Saved {len(df)} rows to data/raw/wine_raw.csv")
=======
from pathlib import Path

from sklearn.datasets import load_wine


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "wine_raw.csv"


def main() -> None:
    RAW_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    wine = load_wine(as_frame=True)
    wine.frame.to_csv(RAW_DATA_PATH, index=False)
    print(f"Saved {len(wine.frame)} rows to {RAW_DATA_PATH.relative_to(PROJECT_ROOT)}")
>>>>>>> 8f5f889b7bbef22de8eca763dfb87e89aef517b3


if __name__ == "__main__":
    main()
