# RC194 terminology

**Signed q185 endpoint-output moments** are the exact rational numbers mu_k=sum_m q185_m [m(m+1)/lambda]^k, for k=0..24 and lambda=256*257. Their signs are retained. They describe the endpoint action on the exact finite RC185 polynomial, not on the actual RC184 residual.

**Retained analytic q185 endpoint tail** means the coefficient rule eta_n sum_{k=0}^{24} mu_k [lambda/n(n+1)]^k at every even n>=4096. It is combined with RC185's endpoint prefix through degree4094. The omitted geometric remainder has its own complete D-norm bound.

**Refined q185 canonical action** keeps the exact q185 identity, finite endpoint prefix, negative-r polynomial, and regular polynomial from RC185, and adds the retained analytic endpoint tail. Its error is an absolute D-norm bound on Mq185; it is not an inverse-response width or a new approximation to the actual residual.
