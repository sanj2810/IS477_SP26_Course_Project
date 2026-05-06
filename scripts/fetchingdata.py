import pandas as pd
from fredapi import Fred
import os
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

FRED_API_KEY = os.getenv("90798f61eafd481fa95ce62890f84ec3")

FRED_SERIES = {
    "CPIAUCSL": "Consumer Price Index",
    "CPILFESL": "Core CPI",
    "PCEPI": "PCE Price Index",
    "FEDFUNDS": "Federal Funds Rate",
    "M1SL": "M1 Money Supply",
    "M2SL": "M2 Money Supply",
    "UNRATE": "Unemployment Rate",
    "CIVPART": "Labor Force Participation",
    "AWHAETP": "Average Hourly Earnings",
    "INDPRO": "Industrial Production",
    "UTILIZATION": "Capacity Utilization",
    "DCOILWTICO": "Oil Prices (WTI)",
    "PPIACO": "Producer Price Index",
    "A191RL1Q225SBEA": "Real GDP",
    "A191RLSI1Q225SBEA": "GDP Price Deflator",
}

print("Fetching FRED data...")
fred = Fred(api_key=FRED_API_KEY)
data_dict = {}

for series_id, description in FRED_SERIES.items():
    try:
        print(f"Fetching {series_id}...", end=" ")
        series = fred.get_series(series_id, observation_start="2010-01-01", observation_end="2024-12-31")
        data_dict[series_id] = series
        print("✓")
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        continue

df = pd.DataFrame(data_dict)
df.index.name = "Date"

print(f"\nData acquired: {df.shape[0]} observations, {df.shape[1]} variables")
print(f"Date range: {df.index.min().date()} to {df.index.max().date()}")

df.to_csv("data/raw/fred_data.csv")