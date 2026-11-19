from pathlib import Path

from sklearn.datasets import load_wine


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT_DIR / "data" / "raw" / "wine_raw.csv"


def main() -> None:
    wine = load_wine(as_frame=True)
    df = wine.frame
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} rows to {OUTPUT_PATH.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    main()
