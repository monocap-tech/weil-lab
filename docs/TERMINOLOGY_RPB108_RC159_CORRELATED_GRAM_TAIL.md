# RC159 terminology additions

Definitions are additive; historical wording remains unchanged.

**Conditioned common-eta source tail.** After the RC158 source transform, each of the seven source tails beyond degree 16382 is eta_n times a polynomial a_j+sum_{k>=1} b_kj x_n^k, where eta_n=(2n+1)/(n(n+1)D_n) and x_n=(16384*16385)/(n(n+1)) lies in (0,1]. The signed source transform is applied to each coefficient before any absolute value is taken.

**Shared leading tail Gram.** If the eta tail has D-energy at most T, its leading constant coefficient vector a gives the rank-one Gram upper T aa^T. This preserves leading correlations between the seven sources rather than charging seven separate diagonal energies.

**Higher-moment tail remainder budget.** For r_j=sum_{k>=1}|b_kj|, the remainder column energies are at most T r_j^2, and their joint Gram is bounded by 7T diag(r_j^2). Signed Young's inequality combines this remainder with the leading feature using a rational parameter tau.

**Correlated source-Gram upper.** The unchanged finite-prefix upper plus (1+tau)T aa^T+(1+1/tau)7T diag(r_j^2). The lower remains the certified finite-prefix lower. This is a source Gram enclosure and does not by itself certify inverse-response precision.
