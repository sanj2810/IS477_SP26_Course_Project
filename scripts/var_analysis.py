import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

Path("results/figures").mkdir(parents=True, exist_ok=True)
Path("results/tables").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/processed/cleaned_inflation_data.csv", index_col=0, parse_dates=True)

vars_for_var = ['CPIAUCSL', 'FEDFUNDS', 'M2SL', 'UNRATE', 'AWHAETP', 'DCOILWTICO', 'INDPRO']
data = df[vars_for_var].pct_change().dropna() * 100

model = VAR(data)
var_model = model.fit(3)

with open("results/tables/var_model_summary.txt", "w") as f:
    f.write(str(var_model.summary()))

irf = var_model.irf(10)
fig = irf.plot(orth=False, figsize=(12, 8))
plt.suptitle('Impulse Response Functions')
plt.tight_layout()
plt.savefig("results/figures/impulse_responses.png", dpi=300)
plt.close()

fevd = var_model.fevd(10)
fevd.plot(figsize=(12, 6))
plt.suptitle('Forecast Error Variance Decomposition')
plt.tight_layout()
plt.savefig("results/figures/variance_decomposition.png", dpi=300)
plt.close()

print("\ndone")