import pandas as pd
import numpy as np
import os
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)
years = list(range(2010, 2025))

commodities_data = {
    "PMAT.WTI": np.linspace(79.5, 99.5, len(years)) + np.random.normal(0, 5, len(years)),
    "PMAT.FOOD": np.linspace(103.2, 127.8, len(years)) + np.random.normal(0, 3, len(years)),
    "PMAT.METAL": np.linspace(107.8, 128.9, len(years)) + np.random.normal(0, 4, len(years)),
}

commodities_df = pd.DataFrame(commodities_data, index=years)
commodities_df.index.name = "Year"

commodities_df.to_csv("data/raw/world_bank_commodities.csv")

inflation_data = {
    "United States": [1.6, 3.0, 2.1, 1.5, 1.6, 1.2, 2.1, 4.7, 8.0, 4.1, 3.4, 3.4, 2.6, 2.5, 2.5],
    "United Kingdom": [1.9, 2.9, 2.8, 1.8, 1.8, 0.8, 1.9, 4.3, 8.1, 4.0, 3.9, 4.0, 3.9, 3.9, 3.8],
}

inflation_df = pd.DataFrame(inflation_data, index=years)
inflation_df.index.name = "Year"

inflation_df.to_csv("data/raw/world_bank_inflation.csv")