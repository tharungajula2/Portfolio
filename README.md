# Analytics & Quantitative Projects

Applied machine learning and quantitative modelling on financial, banking and time-series data. Each project is a Jupyter notebook taken end to end, from raw data through to validated results.

**Portfolio:** [tharungajula.vercel.app](https://tharungajula.vercel.app) · **Credit risk system:** [retail-credit-risk](https://github.com/tharungajula2/retail-credit-risk)

---

## Featured work

### Bank Customer Churn, Neural Network
Customer attrition on a 10,000-customer retail banking dataset, built in Keras across five model variants: SGD, Adam, dropout, hyperparameter tuning, and SMOTE for class imbalance.

Churn recall improved from 0.48 to 0.75 after SMOTE. Precision fell from 0.79 to 0.51 and accuracy from 0.87 to 0.80, while ROC-AUC held near 0.85 across all five variants.

The point is not that SMOTE improved the model. It is that the metric worth optimising depends on the cost of the decision. For retention outreach, missing a churner costs more than contacting a non-churner, so recall wins and the precision cost is accepted deliberately.

**Techniques:** Keras, class imbalance handling, SMOTE, optimiser comparison, dropout regularisation, ROC-AUC and recall-focused evaluation.

---

### Antidiabetic Drug Prescription Forecasting
Monthly prescription volumes over 204 observations from July 1991 to June 2008, split 168 training and 36 test, evaluated through rolling 12-month forecasts.

STL decomposition and ADF stationarity testing, followed by regular and seasonal differencing, then model selection across 625 candidate SARIMA structures.

| Model | MAPE |
|---|---|
| Naive seasonal baseline | 12.69% |
| SARIMA(2,1,3)(1,1,3)₁₂ | **7.90%** |

The discipline transfers directly to loss forecasting, provisioning workflows and collections volume planning.

**Techniques:** STL decomposition, ADF testing, differencing, SARIMA grid search, rolling forecast validation, baseline comparison.

---

### NIFTY 100 Portfolio Optimisation
Modern Portfolio Theory applied to NIFTY 100 constituents. Adjusted close prices from Yahoo Finance over a three-year lookback, reduced to 82 usable stocks after download failures and missing-value handling, giving a 609 × 82 return matrix.

Log returns, annualised mean returns and a covariance matrix, then 10,000 randomly generated weight vectors used to trace the efficient frontier and select on return over volatility. Equal weight across the 82 stocks returns 9.6% at 4.77% variance, used as the comparison baseline.

This is MPT implemented honestly. It is not an institutional portfolio construction engine: there is no factor model, no sector neutrality, no transaction cost model and no rebalancing backtest.

**Techniques:** log returns, covariance estimation, Monte Carlo weight generation, Sharpe ratio selection, efficient frontier construction.

---

### Reference notes
Written technical references built alongside the modelling work, covering regression analysis, machine learning methods, a Python data analytics reference, regulatory foundations, and a quantitative modelling workflow reference.

These exist because being able to explain the work matters as much as producing it.

---

## The credit risk system lives elsewhere

The retail credit risk work outgrew this repository and has its own home:

**[github.com/tharungajula2/retail-credit-risk](https://github.com/tharungajula2/retail-credit-risk)**

An end-to-end system on 466,285 loans from the public LendingClub dataset. PD scorecard with WoE and IV binning, two-stage LGD across 50,968 defaults, EAD, Expected Loss, IFRS 9 and Ind AS 109 ECL staging with SICR criteria and lifetime PD term structures, Basel III Advanced IRB capital, and a full validation and monitoring suite.

---

## Also in this repository

Earlier work kept for completeness rather than featured: employee attrition classification, socio-economic household classification, Twitter sentiment analysis, and a CartPole reinforcement learning comparison. These were built while learning the respective methods.

---

## Data

Every dataset used here is public. Sources include Kaggle, Yahoo Finance and published open datasets. No proprietary, client or employer data appears anywhere in this repository.

---

## Stack

Python, pandas, NumPy, scikit-learn, statsmodels, Keras, imbalanced-learn, XGBoost, yfinance, matplotlib, seaborn, Jupyter.

---

## Contact

Tharun Gajula · Bengaluru, India
[tharun.gajula.2@gmail.com](mailto:tharun.gajula.2@gmail.com) · [LinkedIn](https://linkedin.com/in/tharungajula) · [Portfolio](https://tharungajula.vercel.app)
