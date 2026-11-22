# Weil-Lab — UOI050: Exact prime-density cancellation and smooth-head tail decay

**Date:** 2026-11-21 (PT)  
**Status:** Read-only mathematical investigation. Conditional on the specified physical prime-form normalization, UOI045 Gamma coercivity on the completed family, and the stated 8-adic collar geometry. No Lean compilation, native-source bridge, CI submission, full prime operator compactness, global Weil positivity, or RH proof.

## 0. Sources and fixed inputs

Carry forward the UOI048 three local neutralities on every collar: `int h = int exp(x/2) h = int exp(-x/2) h = 0`, together with the stated original weighted prime shifts `Lambda(n)/sqrt(n)` and Gamma coercivity `Gamma(v) >= g ||v||_2^2`, `g >= 1099/1000` (to be independently verified in the exact local Gamma realization). The UOI049 working 8-adic collar model has centers `c_k=c_0+k log 8` and width `|I_k| <= delta*8^(-k)`, `delta=1/1000`. Each `I_k` lies within `c_k + [-delta,delta]`.

External classical input: there are constants `A,c>0` such that for `u>=2`, `|psi(u)-u| <= A*u*exp(-c*sqrt(log u))`, where `psi(u)=sum_(n<=u) Lambda(n)`. See https://kskedlaya.org/ant/chapter-8.html and https://openmaths.org/courses/NT-ZETA/NT-ZETA-12.html . The constants in this report are **not numerically certified**.

## 1. Exact discrepancy identity (no RH)

For a fixed `h in C_c^1(R)` supported in `[a,b]` (the finite head), define the oriented prime field

`(T h)(y) = sum_{n>=2} Lambda(n)/sqrt(n) * h(y-log n)`.

For `y>b+log 2`, put `F_y(u)=u^(-1/2) h(y-log u)`, whose support lies in `u>1`. Stieltjes summation gives

`T h(y) = integral_1^infty F_y(u) d psi(u)`.

Since `u=e^(y-x)` gives

`integral_1^infty F_y(u) du = exp(y/2) * integral_a^b h(x) exp(-x/2) dx = 0`, 

we obtain exactly, with `E(u)=psi(u)-u`,

`T h(y) = integral_1^infty F_y(u) d E(u) = - integral_1^infty E(u) F_y'(u) du`.

Derivative: `F_y'(u) = -u^(-3/2) [h'(y-log u) + h(y-log u)/2]`.

This uses the **complete genuine von Mangoldt sum**, not an averaged prime replacement. The subtraction of `du` is an exact algebraic decomposition with an identically zero continuous-density pairing.

## 2. Classical unconditional pointwise bound

Let `D(h) = integral_a^b exp(-x/2) |h'(x) + h(x)/2| dx`.

If `y-b >= log 2` and the classical PNT error applies throughout the integration interval, then

`|T h(y)| <= A exp(y/2) exp(-c sqrt(y-b)) D(h)`.

Indeed `|E(u)| <= A u exp(-c sqrt(log u))`, `log u=y-x>=y-b`, and the substitution `du=u dx` yields the bound with `u^(1/2)=exp((y-x)/2)`.

**Important — genuine derivative-loss obstruction:** `D(h)` is not bounded uniformly by `Gamma(h)^(1/2)` on an infinite-dimensional log-energy head space. Indeed choose `phi in C_c^infty(I_0)` nonzero and define `h_Q = Q^(-3) D_x (D_x^2-1/4)[phi(x) exp(i Q x)]`. All three exponential moments vanish exactly by integration by parts, `||h_Q||_2` stays bounded above and below, and `D(h_Q) asymp Q` as `Q -> infinity`. In contrast, under the standard digamma upper asymptotic, `Gamma(h_Q) = O(log Q)`. Thus `D(h_Q)/sqrt(Gamma(h_Q))` diverges at least on the order of `Q/sqrt(log Q)`. The discrepancy estimate cannot be made Gamma-uniform by substituting the Gamma norm for `D(h)`. This is an analytic counterexample to that proposed *proof step*, not a counterexample to compactness of the prime operator.

## 3. Square-summable remote collar fields for each fixed smooth head

Assume `I_k subset [c_0+k log 8-delta, c_0+k log 8+delta]`, `|I_k| <= delta 8^(-k)`. Fix a head bound `b` and choose `K_0` large enough that for all `k>=K_0` and `y in I_k`, `y-b >= (log 8) k/2` and `y-b>=log 2`. Set `a_*=c sqrt(log 8/2)>0`.

The previous pointwise bound gives

`||1_(I_k) T h||_2 <= C_h exp(-a_* sqrt(k))`,

where one admissible (non-numerical) constant is

`C_h = A D(h) sqrt(delta) exp((c_0+delta)/2)`.

The crucial exact geometric cancellation is

`|I_k| * exp(c_0+k log 8 + delta) <= delta * exp(c_0+delta)`,

which neutralizes the growing `exp(y/2)` factor after taking L2 over the shrinking collar.

Hence for `K>=K_0`,

`||1_(union_(k>=K) I_k) T h||_2 <= C_h [ sum_(k>=K) exp(-2a_* sqrt(k)) ]^(1/2)`.

By monotone comparison to an integral,

`sum_(k>=K) exp(-2a_* sqrt(k)) <= exp(-2a_*sqrt K) * (1+sqrt(K)/a_*+1/(2a_*^2))`.

Thus the tail field norm is `O_h(K^(1/4) exp(-a_* sqrt K))`.

## 4. Consequence for original mixed prime form on the smooth head

Assume the exact original mixed prime polarization for separated supports is `P(h,t)=C_P <T h,t>_(L2)` for the project normalization factor `C_P` (known only after source-convention audit). Also assume UOI045 provides `Gamma(t)>=g||t||_2^2` uniformly for the completed tail, with `g>0`.

Then every fixed smooth three-moment-neutral `h` satisfies

`sup_{t!=0, supp t subset union_(k>=K) I_k} |P(h,t)|/sqrt(Gamma(t)) <= |C_P| g^(-1/2) C_h exp(-a_*sqrt K) sqrt(1+sqrt K/a_*+1/(2a_*^2))`.

This is a **remote-tail decay estimate for each fixed smooth h**, and is valid uniformly in the number of tail collars under the displayed assumptions.

On any **fixed finite-dimensional smooth head subspace** `E`, `D(h) <= C_E sqrt(Gamma(h))` by equivalence of norms; the same decay is uniform for `h in E`.

This is a compactness-like result for finite-dimensional smooth head models, **not** full compactness of the prime core–tail operator from the completed infinite-dimensional head.

## 5. Why the UOI049 resonance is compatible

The UOI049 resonance uses an M-dependent L2-normalized head packet of width `ell_M=delta*8^(-M)`, then translates it by `M log 8` into collar M, picking the genuine `n=8^M` prime power. The head packet changes with M; its derivative seminorm `D(h_M)` is of size `ell_M^(-1/2)`, namely `~8^(M/2)` up to fixed factors, even though its Gamma norm grows only on the order of `sqrt(M)`.

Therefore the constant `C_{h_M}` in the PNT discrepancy bound grows rapidly with M. The fixed-head estimate does not contradict the UOI049 conditional lower bound `beta_M >= c_0 8^(-M/2)/(1+M)`, nor does it prove a Gamma-normalized small bound for `beta_M`.

## 6. Unresolved operator-theoretic gate

To conclude compactness, one would need **uniform** control, such as:

`lim_(K->infty) sup_(Gamma(h)<=1; head h) sup_(Gamma(t)<=1; tail t>=K) |P(h,t)|=0`.

A falsifiable sufficient square-function target is

`R_(M,K)^2 := sup_(Gamma(h)=1; supp h in head<M) sum_(k>=K) ||1_(I_k) T h||_2^2`.

If `R_(M,K)<infty` and `R_(M,K)->0` as `K->infty`, then with the retained coercivity and polarization assumptions,

`sup_(Gamma(h)=Gamma(t)=1; supp t in collars >=K) |P(h,t)| <= |C_P|*g^(-1/2)*R_(M,K) ->0`.

This would prove compactness of the fixed-head-to-tail operator by finite-block compactness and uniform finite-tail approximation. It is deliberately *sufficient*, not claimed necessary: the tail Gamma-dual norm could be small even when the stronger `L2` square-function estimate fails. A natural route is a uniform prime discrepancy inequality that controls the derivative-dependent estimate using *only* the original Gamma/logarithmic norm, potentially via a scale-resolved almost-orthogonality argument. Its existence is not established here. The a priori global boundedness of this mixed prime form on the complete Gamma head/tail product also remains an independent prerequisite.

Afterwards still needed: a certified infinite-tail positivity margin `tau_M>0` and `beta_M` small enough to satisfy `(beta_M + kappa_M)^2 < alpha_M*tau_M` at a common cutoff (for M=10 the recorded head margin is `14/25`). No numerical comparison is claimed from this theorem.

## 7. Proof/certification obligations

1. Audit exact source-to-native mixed prime polarization and its complex-conjugate and factor-2 conventions.
2. Reprove `Gamma(t)>=g||t||_2^2` for the entire completed infinite tail, with the exact UOI045 lower constant and closure/domain identifications.
3. Establish the exact collar placement and widths for the original nested family; 8-adic centers and width control remain listed assumptions until matched to source.
4. Formalize finite Stieltjes sums, the neutral main-term identity, integration by parts, and the classical PNT error as an explicitly imported analytic lemma.
5. Distinguish fixed smooth head / fixed finite-dimensional head from uniform infinite-dimensional Gamma-normalized head estimates.
6. Only after a uniform operator bound, address compactness, `beta_M`, and compatible positive tail margins; retain strict axioms/source receipts for any Lean certification.

**Reproducibility:** `UOI050_discrepancy_checker.py` and `UOI050_discrepancy_receipt.json` verify exact elementary identities and collar scaling. They do **not** verify the PNT error theorem, gamma carrier, prime form convention, or completed-space operator bound.
