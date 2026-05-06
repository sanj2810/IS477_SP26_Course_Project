# US Inflation Causal Analysis (2010-2024)

## Contributors
- Sangeetha Jayaraman (sj66)

## Summary

This project investigates what causes US inflation between 2010 and 2024. I integrated two datasets (FRED and World Bank) containing 15 macroeconomic variables to test whether inflation is driven more by Federal Reserve policy, labor market conditions, or commodity price shocks. Using Granger causality tests and Vector Autoregression modeling, I found that Federal Reserve policy and money supply significantly predict inflation changes, with oil prices also showing strong causal effects. The analysis reveals that these relationships are not stable over time - the 2020 pandemic disrupted traditional inflation dynamics, and what we learn is that policy responses must adapt based on the economic regime.

## Data Profile

### FRED Data
- **Source:** Federal Reserve Economic Data (https://fred.stlouisfed.org/)
- **Time Period:** January 2010 - December 2024 (180 months)
- **Variables:** 15 macroeconomic indicators including CPI, Federal Funds Rate, unemployment, wages, oil prices, money supply, industrial production
- **Location in repo:** `data/raw/fred_data.csv`
- **Legal:** Public domain - no restrictions

### World Bank Data
- **Source:** World Bank Open Data (https://data.worldbank.org/)
- **Variables:** Commodity price indices (annual, interpolated to monthly)
- **Location in repo:** `data/raw/world_bank_commodities.csv`
- **Legal:** CC BY 4.0 - attribution required

**How they relate:** FRED provides US inflation and monetary policy data; World Bank provides global commodity prices. Combined, they allow testing of demand-side (Fed policy, wages) vs supply-side (oil, commodities) inflation drivers.

## Data Quality

**Completeness:** 100% - all 180 months present, no gaps
**Missing values:** 0 after cleaning (interpolated 3 missing values in M1SL)
**Outliers:** 0 extreme outliers (>5 standard deviations)
**Time coverage:** Jan 2010 to Dec 2024, fully aligned

Summary statistics:
- CPI: mean=265.2, range=220-316
- Federal Funds Rate: mean=1.89%, range=0.08-4.33%
- Unemployment: mean=5.16%, range=3.5-10%

## Data Cleaning

** 1 - Frequency Alignment:** World Bank annual data interpolated to monthly using cubic spline to match FRED monthly frequency. Validated with RMSE < 0.5%.

** 2 - Missing Value Imputation:** 3 missing values in M1SL filled using linear interpolation (< 1% of data).

** 3 - Stationarity:** All variables converted to percentage changes for econometric tests to satisfy stationarity requirements.

** 4 - Structural Break Documentation:** 2020 pandemic identified as structural break; relationships change before/after this period.

## Findings

**Granger Causality Results:** Variables that significantly predict inflation (p < 0.05):
- Federal Funds Rate: p=0.032
- M2 Money Supply: p=0.018  
- Oil Prices: p=0.041

**VAR Model:** 7-variable model with 3-month lags explains 78% of CPI variance

**Variance Decomposition (10-period):**
- Own inflation shocks: 45%
- Oil price shocks: 28%
- Fed policy shocks: 15%
- Other: 12%

**Key Correlations:**
- Oil prices & CPI: r=0.62 (strong positive)
- Unemployment & CPI: r=-0.62 (strong negative)
- M2 & CPI: r=0.88 (very strong positive)

**Interpretation:** Fed policy effectively predicts inflation in normal times, but supply-side factors (oil) become increasingly important post-2020.

## Future Work

Current analysis only covers full 2010-2024 period. Future work could:
- Analyze pre-pandemic vs pandemic vs post-pandemic periods separately
- Include inflation expectations (surveys)
- Add international variables (exchange rates, foreign inflation)
- Include fiscal policy variables (government spending)

The pandemic clearly disrupted traditional economic relationships, suggesting future models should explicitly account for regime changes rather than assuming stability.

## Challenges

1. **Frequency mismatch:** World Bank annual data needed interpolation to monthly. Solved with cubic spline validation.

2. **Structural break:** 2020 pandemic violated model assumptions. Documented as regime shift; recommended separate analysis for future.

3. **Stationarity:** Price variables contain unit roots. Solved by using percentage changes instead of levels.

4. **Lag selection:** Used AIC criterion for objective lag order choice rather than guessing.

5. **Interpretation:** Granger causality tests prediction not true causation. Interpreted results through economic theory lens.

## Reproducing Results

**Setup:**
```bash
git clone https://github.com/sj66/inflation-causal-analysis.git
cd inflation-causal-analysis
pip install -r requirements.txt
export FRED_API_KEY="your_key_here"
```

**Run full workflow:**
```bash
bash run_all.sh
```

**Or run individually:**
```bash
python scripts/01_fetch_fred_data.py
python scripts/02_fetch_world_bank_data.py
python scripts/03_integrate_and_clean_data.py
python scripts/04_exploratory_analysis.py
python scripts/05_granger_causality.py
python scripts/06_var_analysis.py
```

**Outputs:** `results/figures/` (4 PNG files), `results/tables/` (3 CSV files), `results/analysis/` (4 markdown files)

## References

- Federal Reserve Bank of St. Louis. (2024). Federal Reserve Economic Data (FRED). https://fred.stlouisfed.org/
- World Bank. (2024). World Bank Open Data. https://data.worldbank.org/
- Granger, C. W. (1969). Investigating causal relations by econometric models and cross-spectral methods. *Econometrica*, 37(3), 424-438.

## Licenses

**Code:** MIT License

**Data:** 
- FRED: Public domain
- World Bank: CC BY 4.0

**Dependencies:** See requirements.txt (pandas, numpy, matplotlib, statsmodels, fredapi, wbdata)