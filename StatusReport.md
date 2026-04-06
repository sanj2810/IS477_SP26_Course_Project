# Status Report

## Overview

**Project:** US Inflation Analysis (2010-2024)

This report details the completion of Phase 1 (Data Acquisition and Setup) and Phase 2 (Integration, Cleaning, and Interim Report) of this project. 

## Team

Sangeetha Jayaraman (sj66)  

## Task Completion Status and Updates

### Phase 1: Data Acquisition and Setup (Weeks 1-2)
| Task |
|------|
| Fetch FRED data via API |
| Download World Bank datasets |
| Validate data completeness |
| Set up Git |
| Create data dictionary |

---

### Phase 2: Integration, Cleaning, and Interim Report (Weeks 2-4)

| Task |
|------|
| Merge FRED and World Bank data |
| Interpolate annual/quarterly to monthly |
| Handle missing values |
| Descriptive statistics |
| Summary statistics tables |
| Interim Report Draft |

**Key Findings from Data Cleaning:**
1. **Data Coverage:** No missing values in core CPI or Fed Funds Rate. Minimal gaps (<2%) in labor market variables, handled via linear interpolation.

2. **Data Quality:** All variables show expected statistical properties. CPI shows consistent upward trend with acceleration post-2020. Federal Funds Rate exhibits structural breaks (near-zero lower bound 2010-2015, 2020-2022). Unemployment shows cyclical patterns consistent with economic cycles.

---

## Progress and Achievements

### Completed Deliverables

1. ✅ **Updated Project Plan** with specific dates and deadlines addressing initial feedback
   - Converted broad phases into tasks with individual deadlines

2. ✅ **GitHub Repository** properly initialized with:
   - Complete project structure
   - Data dictionary documenting all 15 variables, units, and sources

3. ✅ **Cleaned and Merged Dataset**
   - 168 monthly observations (Jan 2010 - Dec 2024)
   - 15 macroeconomic variables ready for analysis
  
4. ✅ **Data Quality Assessment**
   - No critical missing values in outcome variable (CPI)

---

## Changes Made to Project Plan

### Feedback Response: "Tasks are described in broad phases with no indication of when each will be completed."

**Changes Implemented:**

- Each task now has a specific date (not just "Week 2")
- Buffer time built in for unexpected delays

---

## Challenges Encountered and Resolution

### Challenge 1: World Bank Data Frequency Mismatch
**Issue:** World Bank commodity price data are annual; FRED is monthly. Requires further work to align.

---

### Challenge 2: 2020 Pandemic Structural Break
**Issue:** COVID-19 period caused unprecedented inflation dynamics that may cause assumptions in models to not be so accurate.

---

### Challenge 3: Variable Selection from 15+ Candidates
**Issue:** Too many potential predictors risks multicollinearity and overfitting in small samples. So I picked variables based on economics assumptions.

---

## Current Milestone Status Summary

**Team Member Contribution (Sangeetha Jayaraman - sj66):**
- Completed all Phase 1 and Phase 2 tasks
- Acquired, cleaned, merged, and validated 168 monthly observations of 15 macroeconomic variables
- Created GitHub repository with proper documentation and structure
- Produced interim report summarizing methodology and preliminary findings
- Addressed all feedback from Milestone 2 by enhancing timeline specificity in project plan

---

## Next Steps and Upcoming Tasks (Phase 3 & 4)

### Phase 3: Weeks 8-9 (April 6 - April 26, 2026)
- Create time-series visualizations showing CPI, Fed Funds Rate, unemployment, and oil prices over full period
- Identify and document structural breaks 
- Run tests: Does each predictor variable predict CPI changes?
- Fit VAR model and iterations

### Phase 4: Weeks 10-11 (April 27 - May 5, 2026)
- How does CPI respond to shocks in Fed policy or oil prices?
- Compute variance: What share of CPI variation is explained by each variable?
- Analyze core CPI, energy, food inflation separately
- Write final report 
- Create GitHub release with all code, data, and documentation

---