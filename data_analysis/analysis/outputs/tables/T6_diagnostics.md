**Diagnostics for the baseline value-relevance model (Model 1)**

| Diagnostic | Statistic | p / threshold | Note |
|---|---|---|---|
| VIF (EPS) | 1.16 | - | tolerance 0.862 |
| VIF (BVPS) | 1.16 | - | tolerance 0.862 |
| Breusch-Pagan LM | 14.37 | p = 0.213 | Cook-Weisberg test for heteroskedasticity |
| Max Cook's D | 0.552 | 4/n = 0.143 | 5 of 28 observations exceed the threshold |

*Notes: VIF computed on the substantive regressors only (fixed-effect dummies excluded). HC3 robust inference is the designated answer to heteroskedasticity; the Breusch-Pagan test is reported for disclosure. Residual normality: see the Q-Q panel of F5; Cook's-distance influence is examined there per observation.*
