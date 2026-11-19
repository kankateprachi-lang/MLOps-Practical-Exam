import pandas as pd
from sklearn.datasets import load_wine


def main() -> None:
    wine = load_wine(as_frame=True)
    df = wine.frame
    df.to_csv("data/raw/wine_raw.csv", index=False)
    print(f"Saved {len(df)} rows to data/raw/wine_raw.csv")


if __name__ == "__main__":
    main()
