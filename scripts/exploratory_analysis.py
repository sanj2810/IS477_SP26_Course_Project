import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

Path("results/figures").mkdir(parents=True, exist_ok=True)
Path("results/tables").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/processed/cleaned_inflation_data.csv", index_col=0, parse_dates=True)

fig, axes = plt.subplots(5, 3, figsize=(16, 12))
axes = axes.flatten()

cols = list(df.columns)
for idx in range(len(cols)):
    if idx < len(axes):
        axes[idx].plot(df.index, df[cols[idx]], color='steelblue')
        axes[idx].set_title(cols[idx], fontsize=10)
        axes[idx].grid(True, alpha=0.3)

plt.suptitle("All Variables Over Time", fontsize=14)
plt.tight_layout()
plt.savefig("results/figures/time_series_trends.png", dpi=300)
plt.close()

corr = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, cbar_kws={"shrink": 0.8})
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("results/figures/correlation_heatmap.png", dpi=300)
plt.close()

df.describe().T.to_csv("results/tables/summary_statistics.csv")
print("\n yay")