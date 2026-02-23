import pandas as pd
import numpy as np
import os

def load_data(filepath) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found {filepath}")
    
    df = pd.read_csv(filepath,low_memory=False) if 'LendingClub' in filepath else pd.read_csv(filepath)
    return df