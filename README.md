# US Inflation Causal Analysis (2010-2024)

## Contributors
- Sangeetha Jayaraman (sj66)

## Summary

This project investigates what causes US inflation between 2010 and 2024. I integrated two datasets (FRED and World Bank) containing 15 macroeconomic variables to test whether inflation is driven more by Federal Reserve policy, labor market conditions, or commodity price shocks. Using correlation analysis, Granger causality tests, and Vector Autoregression modeling, I found that producer prices (PPIACO) show the strongest causal relationship with inflation (p<0.001), followed by M2 money supply (p=0.0004) and average hourly earnings (p=0.0059). Traditional variables like Federal Funds Rate, oil prices, and unemployment do not show statistically significant Granger causality. The VAR model confirms inflation persistence with a very strong autoregressive coefficient (0.997), indicating that inflation in one period heavily predicts inflation in the next period. These findings suggest that upstream inflation (producer prices) is the primary causal driver of consumer price inflation, while the nominal policy rate and oil prices have weaker direct predictive power than expected.

## Data Profile

### FRED Data
- **Source:** Federal Reserve Economic Data (https://fred.stlouisfed.org/)
- **Time Period:** January 2010 - December 2024 (180 months, 3963 observations in raw data)
- **Variables:** 15 macroeconomic indicators including CPI, Federal Funds Rate, unemployment, wages, oil prices, money supply, industrial production, capacity utilization, producer prices, real GDP, and GDP deflator
- **Location in repo:** `data/raw/fred_data.csv`
- **Legal:** Public domain - no restrictions

### World Bank Data
- **Source:** World Bank Open Data (https://data.worldbank.org/)
- **Variables:** Commodity price indices (WTI oil, food, metals - annual, interpolated to monthly)
- **Location in repo:** `data/raw/world_bank_commodities.csv`
- **Legal:** CC BY 4.0 - attribution required

**How they relate:** FRED provides US inflation and monetary policy data; World Bank provides global commodity prices. Combined, they allow testing of demand-side (Fed policy, wages) vs supply-side (oil, commodities) inflation drivers.

## Data Quality

**Completeness:** 100% - 180 consecutive monthly observations from Jan 2010 to Dec 2024
**Missing values:** 1 value after integration (interpolated during merge)
**Outliers:** 0 extreme outliers (>5 standard deviations)
**Temporal coverage:** Full alignment of all 15 variables

**Summary Statistics:**
- **CPIAUCSL (CPI):** Mean=265.17, Std=32.49, Min=220.64, Max=319.09
- **FEDFUNDS:** Mean=1.89%, Std=1.63%, Min=0.08%, Max=5.33%
- **UNRATE:** Mean=5.51%, Std=1.98%, Min=3.50%, Max=14.70%
- **M2SL:** Mean=13,366B, Std=3,748B, Min=8,807B, Max=21,110B
- **DCOILWTICO:** Mean=59.26$/bbl, Std=28.94, Min=-37.63, Max=145.31
- **AWHAETP:** Mean=24.16$/hr, Std=4.36, Min=16.76, Max=34.88
- **PPIACO:** Mean=177.43, Std=28.33, Min=139.3, Max=280.0

## Data Cleaning

**Alignment:** World Bank annual data interpolated to monthly using cubic spline to match FRED monthly frequency.

**Missing Value Imputation:** 1 missing value filled using linear interpolation after merging datasets.

**Data Alignment:** All 15 variables successfully aligned to monthly frequency, verified no gaps in date index.

**Validation:** Post-cleaning confirmed 100% temporal coverage with effectively zero missing values (<0.1%).

## Findings

### Granger Causality Test Results

Shows which variables have statistically significant predictive power for inflation:

**Significant Predictors (p < 0.05):**
1. **PPIACO (Producer Price Index):** F=28.04, p<0.001 
   - Producer prices are the strongest predictor of consumer inflation
   - Suggests upstream inflation passes through to consumer prices

2. **M2SL (M2 Money Supply):** F=7.92, p=0.0004 
   - Broader money supply predicts inflation changes
   - Supports demand-side inflation channel

3. **AWHAETP (Average Hourly Earnings):** F=5.15, p=0.0059 
   - Wage growth predicts inflation
   - Wage-price spiral effects visible

**Non-Significant Predictors (p > 0.05):**
- FEDFUNDS (Federal Funds Rate): F=1.77, p=0.17 
- DCOILWTICO (Oil Prices): F=1.15, p=0.32 
- INDPRO (Industrial Production): F=1.12, p=0.33 
- UNRATE (Unemployment Rate): F=0.76, p=0.47 

**Interpretation:** Surprisingly, the Federal Funds Rate and oil prices do not show statistically significant Granger causality with inflation in this 2010-2024 sample, despite strong correlations. Producer prices dominate as the causal driver.

### Correlation Analysis - Top Relationships with CPI

From the correlation matrix:
- **M2 Money Supply:** r=0.94 
- **Core CPI & PCE:** r=1.00 
- **Commodity Prices (PMAT.WTI, PMAT.FOOD, PMAT.METAL):** r=0.81-0.88 
- **Federal Funds Rate:** r=0.83 
- **Producer Prices (PPIACO):** r=0.89 
- **Unemployment Rate:** r=-0.63 

### Time Series Observations

From the time-series visualization:
- **CPI Trend:** Steady increase 2010-2021, acceleration 2021-2024, reflecting inflation surge
- **Monetary Policy:** Fed Funds Rate held near-zero 2010-2015 and 2020-2022; rapid tightening cycle 2022-2023 to 5.33%
- **Labor Market:** Unemployment high in 2010-2011 (~9%), normalized to ~3.5% by 2019, spiked to 14.7% in April 2020, recovered to 4% by 2024
- **Commodity Prices:** Oil highly volatile; visible shocks in April 2020 (negative prices during pandemic), and 2022 (supply disruptions)
- **Money Supply:** M2 expanded dramatically from ~8.8T (2010) to ~21T (2022), providing liquidity that fueled post-pandemic inflation
- **Producer Prices:** Sharp increase post-2021, tracking CPI closely with higher amplitude, confirming upstream inflation pressure

### VAR Model Results

**Model Specification:**
- Variables: CPIAUCSL, FEDFUNDS, M2SL, UNRATE, AWHAETP, DCOILWTICO, INDPRO (7 variables)
- Lag Order: 3 months
- Observations: 3,958 (after differencing)
- Model Fit: AIC=-44.17, BIC=-43.93

**Key Coefficient (Equation for CPIAUCSL):**
- **Constant:** 0.000167 (t=2.579, p=0.010)
- **L1.CPIAUCSL:** 0.9966 (t=58.73, p<0.001) 
  - Last month's inflation rate is the strongest predictor of current inflation
  - Explains inflation inertia
- **L1.FEDFUNDS:** -0.000331 (t=-3.841, p<0.0001) 
  - Higher Fed Funds Rate associated with lower inflation (lag effect)
- **L1.M2SL:** 0.001655 (t=0.189, p=0.85) 
  - Money supply effect absorbed in other specifications

**Interpretation:** The VAR results confirm that inflation is highly persistent (0.997 autoregressive coefficient means 99.7% carryover from previous month). The Federal Funds Rate shows negative correlation with inflation, consistent with monetary tightening reducing inflation. The model captures complex dynamic interactions between variables.

## Future Work

**Limitations:**
- Full sample masks structural changes (pandemic regimes differ from normal periods)
- Granger causality tests past relationships, may not predict future changes
- Limited supply-side variables (only commodities taken)
- No forward-looking variables (expectations, yield curve, surveys)
- No fiscal policy variables (government spending, deficits)
- Assumes linear relationships; nonlinearities likely exist

## Challenges

1. Federal Funds Rate and oil prices, despite strong correlations, showed no statistically significant Granger causality. This suggests that while they move with inflation, they may not be predictive drivers. 

2. Merging 15 FRED variables with World Bank annual data needed a solid amount of pre processing. 

3. Major events were visible in time series (unemployment spike, Fed emergency measures, supply disruptions). VAR assumes stable relationships but these events throws a stone in the model this. Would need separate analysis.

## Reproducing Results

**Setup:**
```bash
pip install -r requirements.txt
$env:FRED_API_KEY = "personalkey"
```

**Run full workflow:**
```bash
python scripts/fetchingdata.py
python scripts/worldbankdata.py
python scripts/cleaning.py
python scripts/exploratory_analysis.py
python scripts/granger_causality.py
python scripts/var_analysis.py
```

**Outputs:**
- Data: `data/processed/cleaned_inflation_data.csv`
- Figures: `results/figures/` (time_series_trends.png, correlation_heatmap.png, impulse_responses.png, variance_decomposition.png)
- Tables: `results/tables/` (summary_statistics.csv, granger_results.csv, var_model_summary.txt)

All results reproducible from data acquisition through analysis.

## References

- Federal Reserve Bank of St. Louis. (2024). Federal Reserve Economic Data (FRED). https://fred.stlouisfed.org/
- World Bank. (2024). World Bank Open Data. https://data.worldbank.org/

## Licenses

**Code:** MIT License

**Data:** 
- FRED: Public domain
- World Bank: CC BY 4.0

**Python packages:** See requirements.txt (pandas, numpy, matplotlib, seaborn, statsmodels, scikit-learn, fredapi, wbdata, scipy)