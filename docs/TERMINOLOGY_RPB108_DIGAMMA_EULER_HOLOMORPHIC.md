# RPB-108 terminology: independent holomorphic Euler candidate

`neutralDigammaEulerTerm n z` means the actual rational function
`1/(n+1)-1/(z+n)`. `neutralDigammaEulerSeries z` means its complex tsum
minus the Euler–Mascheroni constant. These are candidate definitions;
their names do not assert equality with actual complex digamma.

The right half-plane means `{z : ℂ | 0 < z.re}`. A bounded separated
region in this pass means `{z | a < z.re ∧ ‖z-1‖ < R}`, where 0<a≤1.
The independent majorant is `(R/a)/(n+1)^2` on such a region.
Holomorphy is complex differentiability throughout this open domain.
Actual digamma identification and residual cancellation remain separate.
