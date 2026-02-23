import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['loan_status'].isin(['Fully Paid', 'Charged Off'])].copy()
    df['is_default'] = df['loan_status'].apply(
        lambda x: 1 if x == 'Charged Off' else 0
    )

    if df['int_rate'].dtype == 'object':
        df['int_rate'] = df['int_rate'].str.strip(' %').astype(float)

    if df['revol_util'].dtype == 'object':
        df['revol_util'] = df['revol_util'].str.strip(' %').astype(float)
    num_cols = [
        'loan_amnt', 'int_rate', 'installment', 'annual_inc', 'dti',
        'fico_range_low', 'revol_util', 'total_acc', 'open_acc', 'pub_rec'
    ]

    for col in num_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    if 'term' in df.columns:
        df['term_months'] = df['term'].str.extract(r'(\d+)').astype(float)
    # One-hot encoding
    cat_cols = ['grade', 'home_ownership', 'verification_status', 'purpose']
    df_encoded = pd.get_dummies(df, columns=cat_cols, dummy_na=False)

    # Select columns except loan_status
    drop_cols = ['loan_status']
    df_encoded = df_encoded.drop(columns=[c for c in drop_cols if c in df_encoded.columns])

    return df_encoded