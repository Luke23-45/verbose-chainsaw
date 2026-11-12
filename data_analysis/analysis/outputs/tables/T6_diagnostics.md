**Diagnostics for the baseline value-relevance model (Model 1)**

| Diagnostic | Statistic | p / threshold | Note |
|---|---|---|---|
| Model 1 VIF (EPS) | 1.16 | - | tolerance 0.862 |
| Model 1 VIF (BVPS) | 1.16 | - | tolerance 0.862 |
| Model 2 VIF (EPS) | 10.33 | - | tolerance 0.097 |
| Model 2 VIF (BVPS) | 2.28 | - | tolerance 0.439 |
| Model 2 VIF (EPS_POST) | 15.15 | - | tolerance 0.066 |
| Model 2 VIF (BVPS_POST) | 24.13 | - | tolerance 0.041 |
| Breusch-Pagan LM | 14.37 | p = 0.213 | Koenker robust form; statsmodels robust=True |
| Classical BP LM | 28.18 | p = 0.003 | Normality-based classical variant |
| Max Cook's D | 0.552 | 4/n = 0.143 | 5 of 28 observations exceed the threshold |

*Notes: VIFs are computed on the substantive regressors only (fixed-effect dummies excluded); Model 2 includes both interaction terms. The first LM row is the Koenker robust form and the second is classical Breusch-Pagan. HC3 changes the covariance estimate; it does not remove influential observations. See the Q-Q and leave-one-out diagnostics in F5 and Appendix E.*
