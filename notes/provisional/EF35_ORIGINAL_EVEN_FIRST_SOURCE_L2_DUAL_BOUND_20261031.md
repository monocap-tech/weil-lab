# EF35 — Original first even-source global energy-dual upper and projected-source acceptance threshold

**2026-10-31. Canonical W-EVEN-FORM OPEN.** Parent EF34 [draft PR #433](https://github.com/monocap-tech/weil-lab/pull/433), final source [Actions #41245337303](https://github.com/monocap-tech/weil-lab/actions/runs/41245337303) SUCCESS. EF33 original full signed 471-bell floor >21/5 and restricted original first-source/bell-kernel Schur S2>1/500 retained. EF34 proved true original signed nonzero source-to-unobserved gap pairing after bell shorting, with analytic pseudolocality/form-core conditions still independently auditable. Its exact missing quantity eta>0 had NO numeric upper.

## 1. Entire original signed first-source gradient lies in physical L2, with explicit cap

Original source `e(x)=1_{[-B,B]}(x) cos(2*pi*c0*x)`, B=11/10, c0=37/64, genuine original seven-prime multiplier

`m_prime(xi)=-2 sum_{n=2,3,4,5,7,8,9} w_n cos(2*pi*xi*ln n)`, original w_n=(ln p)/sqrt(n), plus original quarter-digamma symbol

`a_arch(xi)=Re psi(1/4+i*pi*xi)-ln pi`,

and genuine original positive even pole `2|<cosh(x/2),f>|²`. For first-source mixed functional the genuine physical signed gradient on I is

`g_e=P_I[(a_arch+m_prime)(D)e] + 2u cosh(x/2)`, `u=<cosh(x/2),e>`.

The full Fourier multiplier is unbounded (log growth), so naively bounding it by a global L-infinity norm would be WRONG. Instead EF35 gives a **source-specific strong L2 bound**, proving the first original cutoff cosine e belongs to the strong unbounded multiplier domain. It is a new analytic attachment supporting the inherited EF18/EF34 source gradient premise, not an operator-domain theorem for all original test functions.

### Original quarter-digamma symbol bound on all real frequency

Use exact digamma identity

`a_arch(xi)=-C+sum_{k>=0} y²/[(k+1/4)((k+1/4)²+y²)]`, `y=pi|xi|`,

with `C=gamma+3ln2+pi/2+ln pi`. The source SI06 rational constant `CONST_UP<6` bounds `C` above and `C>0`. The k=0 term <=4. For `0<=y<1`, the remaining sum <=sum_{k>=1}k^-3<3/2. For `y>=1`, set `N=floor(y)>=1`: up to N use `1/k`, yielding <=1+log y; for k>N use y²/k³ and integral comparison `y²/(2N²)<2`. Therefore **for every real xi**,

`|a_arch(xi)| <= 7+log(1+pi|xi|) <=7+log(1+4|xi|)`.

This is a complete ORIGINAL signed arch symbol envelope, not truncation of the digamma series.

### Exact source Fourier envelope and physical gradient norm

Original e Fourier transform, with physical e^{-2*pi*i*xi*x} convention, is

`ehat(xi)=sin(2*pi*B*(xi-c0))/(2*pi*(xi-c0)) + sin(2*pi*B*(xi+c0))/(2*pi*(xi+c0))`.

On |xi|<=2, the arch symbol has absolute value <10 because log9<3, and `||e||²<=2B=11/5`. On |xi|>=2, original c0<3/5, pi>3, giving `|ehat(xi)|<10/(21|xi|)`. Also `|a_arch|<9+log|xi|` because log5<2. The exact positive integral formula

`int_2^infty (9+log t)^2/t² dt = [(9+log2)^2+2(9+log2)+2]/2`

and log2<1 give full two-sided tail <12200/441. Combining low and high:

`||a_arch(D)e||² < 100*(11/5)+12200/441 = 109220/441 <256`.

Hence **entire original arch first-source gradient norm is <16**, with all frequencies included. Every transcendental log inequality above is checked by exact positive rational exponential partial sums in the validator; the functional analytic Fourier/Plancherel steps are stated as mathematical deductions, not masqueraded as executable integration.

For all seven original arithmetic prime powers, SI06 certified `TWOC=2 sum_n w_n<70751/10000<71/10`. Since `||e||²<11/5<9/4`, the **original full prime first-source gradient** norm is <11, without dropping channels.

EF32's genuine original pole source interval gives `2u²<1/2`. An elementary full-I bound `cosh(B/2)<=1/(1-B²/8)=800/679<6/5` (by even-power series dominance) and `sqrt(2B)<3/2` gives the original even pole first-source gradient norm `||2u cosh(x/2)||<2`.

Thus the true original physical signed first-source gradient obeys

`||g_e||_{L2(I)} < 16+11+2=29`,

with no source projection, no float SVD, and no unbounded-operator substitution.

## 2. Actual EF34 residual energy dual now has a FINITE original quantitative upper

Original SI10 even cofinite `F=V469^perp` has the genuine complete signed q_even floor `q_even(v,v) > mu||v||²`, `mu=17/25000`, including the nonnegative genuine pole. Let `b(v)=q_even(e,v)=<g_e,v>`.

The energy-dual Cauchy estimate gives

`||b|F||²_{q_even,*} <=||g_e||²/mu < 29²/(17/25000)=21025000/17 <1.237e6`.

Schur-transitivity and the q_even-orthogonal direct sum `F=span{f_*} ⊕_q F1` imply the **original** EF34 residual

`eta=||b_res|F1||²_{q_even,*} <=||b|F||²_{q_even,*} < 21025000/17.`

EF34 supplies `eta>0` (conditionally attached by original noncanceling arithmetic jump); EF35 now gives an ACTUAL finite upper on the entire true original energy-dual response:

`0<eta<21025000/17`  **(not a decision-quality interval).**

The upper is much larger than the EF33 `S2>1/500`; it neither proves `eta<S2` nor `eta>S2`. This is a quantitative source-enclosure success plus explicitly unsuccessful **sign acceptance**. It does not numerically evaluate eta.

## 3. New exact source-projection acceptance criterion avoiding kernel conditioning

Since `F=V469^perp` in the actual physical L2 space,

`||P_F g_e|| = inf_{v in V469} ||g_e-v||.`

By the same cofinite energy floor,

`eta <= ||b|F||²_{q_even,*} <=||P_F g_e||²/mu`.

Therefore an explicit, rigorous sufficient original-form EF36 entry condition is:

**Find ANY explicit native original 469-source linear combination v such that**

`||g_e-v||²_{L2(I)} < mu/500 = 17/12500000 ≈ 1.36e-6`.

Then `eta<1/500<S2`, establishing strict positivity of the original **first-source fully cofinite** Schur without requiring the ill-conditioned EF31 bell-kernel orientation. Since g_e includes the TRUE pole and all seven signed prime powers and complete original arch multiplier, any attempted approximation must include all these parts, and must be an original whole physical L2 norm with certified tails.

This sufficient gate is stringent: `||g_e-v||<sqrt(17/12500000)≈0.0011662`. **EF35 has not supplied v**. Other methods, especially a direct q-energy Riesz approximation, may certify eta more efficiently; this gate is sufficient, not necessary and does not establish a method impossibility.

## 4. Research status, scope and independent audit

The native script validates source coefficients, full original pole interval, SI06 fixed lower/cofinite constants, exact rational analytic envelope constants and the derived inequalities. It does not numerically integrate the full original cofinite resolvent, compute `P_F g_e`, prove the global pseudolocality theorem, or validate original test-core density for every vector. The first-source strong L2 spectral bound materially reduces but does not discharge those general analytic audit duties.

**Accepted (source + mathematical derivation, independent review open):** original first-source full signed gradient in strong L2, `||g_e||<29`; original full cofinite energy-dual and EF34 eta strictly <21025000/17; the exact source-approximation sufficient acceptance threshold 17/12500000.

**Still OPEN:** whether the genuine original `eta<=S2`, all 469 exceptional columns and entire Schur, whole supported even form, paused odd, whole Weil/RH. The numerical gap is huge: do not claim a positive or negative first-source full-cofinite Schur from the global gradient cap.

**EF36 bold:** build the source-projected original L2 gradient residual with strict physical/source-domain certification, or derive a sharper original energy-dual enclosure that pays all correlations and improves the 10^6-to-10^-3 numerical gap. No automatic new frontier; original even obligation remains canonical. No `main` merge.
