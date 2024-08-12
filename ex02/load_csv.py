
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load data"""
    try:
        df = pd.read_csv(path)
    except Exception:
        print("Error path is bad")
        return
    return df
