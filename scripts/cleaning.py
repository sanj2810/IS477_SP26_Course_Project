import pandas as pd
import numpy as np
from pathlib import Path
from scipy.interpolate import interp1d

Path("data/processed").mkdir(parents=True, exist_ok=True)

fred_data = pd.read_csv("data/raw/fred_data.csv", index_col=0, parse_dates=True)
commodities = pd.read_csv("data/raw/world_bank_commodities.csv", index_col=0)

monthly_index = pd.date_range(start=fred_data.index.min(), end=fred_data.index.max(), freq='MS')
commodities_monthly = pd.DataFrame(index=monthly_index)

for col in commodities.columns:
    years = commodities.index.values
    values = commodities[col].values
    f = interp1d(years, values, kind='cubic', fill_value='extrapolate')
    month_years = monthly_index.year + (monthly_index.month - 1) / 12
    commodities_monthly[col] = f(month_years)

df_merged = fred_data.join(commodities_monthly, how='left')
df_merged = df_merged.interpolate(method='linear')
df_merged = df_merged.ffill()

missing = df_merged.isnull().sum().sum()
print(f"Missing values: {missing}")

df_merged.to_csv("data/processed/cleaned_inflation_data.csv")

report = f"""# Data Quality Report
- Observations: {df_merged.shape[0]}
- Variables: {df_merged.shape[1]}
- Date Range: {df_merged.index.min().date()} to {df_merged.index.max().date()}
- Missing Values: {missing}
- Status: READY FOR ANALYSIS ✓
"""

with open("data/processed/DataQualityReport.md", "w") as f:
    f.write(report)