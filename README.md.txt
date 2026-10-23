# Customer Churn Analysis

**Question:** Which customers are most likely to leave, and why?

## Tools
Python (Pandas), MySQL, Power BI (DAX)

## Dataset
IBM Telco Customer Churn dataset (7,043 customers, 33 columns). Source: Kaggle.

## Process
1. Cleaned data in Python: fixed Total Charges data type (11 blank values), checked duplicates, created tenure groups.
2. Analyzed churn by contract, tenure, payment method and churn reason using MySQL queries.
3. Built an interactive Power BI dashboard with KPI cards, charts and slicers.

## Key findings
- Overall churn rate: 26.5%
- Month-to-month customers churn at 42.7%, vs 2.8% for two-year contracts.
- Customers in their first year churn most (47.4%).
- Electronic check users churn at about 45%, vs 15-19% for other payment methods.
- Top reasons: attitude of support staff and competitor offers.

## Dashboard
![Dashboard](images/dashboard.png)

## Files
- `churn_analysis.py`: data cleaning and exploration
- `queries.sql`: SQL analysis
- `churn_dashboard.pbix`: Power BI dashboard