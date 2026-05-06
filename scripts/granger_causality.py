import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

Path("results/tables").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/processed/cleaned_inflation_data.csv", index_col=0, parse_dates=True)
df['inflation'] = df['CPIAUCSL'].pct_change(12) * 100
test_vars = ['FEDFUNDS', 'M2SL', 'UNRATE', 'AWHAETP', 'DCOILWTICO', 'PPIACO', 'INDPRO']

results = []
lag_order = 3

for var in test_vars:
    try:
        data = df[['inflation', var]].dropna()
        if len(data) < lag_order + 10:
            continue
            
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=['inflation', var])
        
        gc = grangercausalitytests(data_scaled.values, lag_order, verbose=False)
        p_value = gc[lag_order-1][0]['ssr_ftest'][1]
        f_stat = gc[lag_order-1][0]['ssr_ftest'][0]
        
        results.append({
            'Variable': var,
            'F_Statistic': f_stat,
            'P_Value': p_value,
            'Significant': 'Yes' if p_value < 0.05 else 'No'
        })
        
        print(f"{var}: p={p_value:.4f} {'✓' if p_value < 0.05 else ''}")
    except:
        continue

results_df = pd.DataFrame(results).sort_values('P_Value')
results_df.to_csv("results/tables/granger_results.csv", index=False)
print("\nPhew, worked")
print(results_df.to_string(index=False))
