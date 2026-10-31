# EF37 — Correlation-preserving original prime-pole physical response and complete arch cutoff

**2026-10-31. Active original W-EVEN-FORM OPEN.** Parent EF36 [draft PR #437](https://github.com/monocap-tech/weil-lab/pull/437) final original source CI [Actions #41249267411](https://github.com/monocap-tech/weil-lab/actions/runs/41249267411) SUCCESS. The genuine 107 original SI10 frequency clusters / 469 protected even sources, seven signed prime-power arithmetic channels, full quarter-digamma and genuine positive even pole are unchanged. EF33's positive original 471-bell span and exact restricted source/kernel 2D Schur >1/500, EF34's nonzero unseen coupling eta (conditional physical analytic attachment), EF36's source-row-reduced global gradient <379/40 and energy-dual eta upper <17955125/136, are retained with their source types.

## 1. The ORIGINAL jointly signed physical response, not seven independent norms

First original protected even source: e(x)=1_{[-B,B]}cos(omega x), B=11/10, omega=2*pi*(37/64). Remove the genuine protected arch source row exactly (EF26/EF29/EF36), so the true first source cofinite projected response obeys

P_F g_e = P_F h, where h(x)=g_prime(x)+2u cosh(x/2)+h_arch,cut(x),
u=<e,cosh(x/2)>.

The original arithmetic term on the actual physical interval is

g_prime(x)=-sum_{n=2,3,4,5,7,8,9} w_n [1_I(x+ln n)cos(omega(x+ln n))+1_I(x-ln n)cos(omega(x-ln n))],

where the weights are the authentic original w_n=ln(p)/sqrt(n) for n=p^k. On the positive half x in [0,B], the seven genuine cutoff transitions are at |B-ln n|, in the strictly ordered n-sequence 3,4,2,5,7,8,9. Thus the true original signed g_prime is, on each of EIGHT exact physical cells,

g_prime(x)=P_j cos(omega x)+Q_j sin(omega x),

with source-complete P_j,Q_j computed from all active genuine original signed translated cutoff channels, at native 10^340 directed outward intervals (EF24/EF29 original exact SI06 logs/pi/sqrt/trig). The positive even pole adds the actual source-pinned k cosh(x/2), k=2u, with its original EF32 outward interval (u<0). No source or even-pole term is omitted.

For a cell [a,b], exact elementary antiderivatives give

int_a^b (P cos omega x+Q sin omega x)^2 dx =
(P²+Q²)(b-a)/2
+(P²-Q²)(sin(2omega b)-sin(2omega a))/(4omega)
+P Q(cos(2omega a)-cos(2omega b))/(2omega).

The genuine signed prime-pole cross terms use exact primitives

int cos(omega x)cosh(x/2)dx =
((1/2)sinh(x/2)cos(omega x)+omega cosh(x/2)sin(omega x))/(omega²+1/4),

int sin(omega x)cosh(x/2)dx =
((1/2)sinh(x/2)sin(omega x)-omega cosh(x/2)cos(omega x))/(omega²+1/4).

The pole norm uses the exact full physical integral int_-B^B cosh²(x/2)dx=B+sinh B. The first source, prime shifts and pole are real and even, so the whole original squared norm is exactly twice the sum of signed positive-half cell integrals, plus the pole squared norm. All complete correlations among n2,n3,n4,n5,n7,n8,n9 AND their genuine pole cross terms are preserved, not bounded separately by a triangle inequality. The native acceptance bound is

**||g_prime+2u cosh(x/2)||²_{L2(I)}<7/10**, hence its physical L2 norm is <17/20.

This is a genuine original-object correlation-specific reduction. It does NOT yet project the 469-dimensional V469 source row space or compute the remaining full inverse response.

## 2. Complete original quarter-digamma physical cutoff norm, now below 3/5

The original archimedean cutoff component, precisely as derived and exported in EF26/EF29/EF36, is

h_arch,cut(x) = sum_{m>=0} 2 Re[e^(i omega B)/(lambda_m-i omega)]e^(-lambda_m B)cosh(lambda_m x),
lambda_m=2m+1/2.

The directed physical source verifier bounds the absolute L2 norm contribution of every m=0,...,99 by a true source sign-sensitive coefficient interval and **an outward bound on the exact physical Laplace cosh norm**:

||e^(-lambda B)cosh(lambda x)||²
=B e^(-2lambda B)+(1-e^(-4lambda B))/(4lambda)
<=B e^(-2lambda B)+1/(4lambda).

No false truncation is imposed: the omitted infinite m>=100 tail is bounded by sum(lambda_m^-3/2 +2sqrt(B)e^(-lambda_m B)/lambda_m), whose monotone algebraic integral bound is

sum_{m>=100} lambda_m^-3/2 <=1/sqrt(397/2)<71/1000,

with an independent total exponential tail <1/10000 using native EF29 outward exp. The first 100 native upward squared-root terms certify absolute summed mode upper <528/1000. Together the entire infinite arch cutoff has

**||h_arch,cut||_{L2(I)}<3/5**.

The arch/primes/pole CROSS with this remaining cutoff component is **not** evaluated here; its complete norm is paid via a genuine full infinite (L^2) bound rather than being dropped.

## 3. Resulting original projected response upper, with exact limit on its scope

Combining the fully correlated original prime+pole response with the complete original arch cutoff gives

||g_e-a_arch(37/64)e||_{L2(I)}
<=||g_prime+2u cosh(x/2)||+||h_arch,cut||
<17/20+3/5 = **29/20=1.45**.

Because e itself is an exact authentic original protected SI10 even source,

**||P_F g_e||_{L2(I)}<29/20**.

Original complete signed even SI10 cofinite coercivity mu>17/25000 implies the full first-source energy-dual response and EF34 residual satisfy the new genuine original upper

**eta < (29/20)^2/(17/25000) =105125/34≈3091.912.**

The signed prime-pole cancellation is the critical new piece; EF36 used a six-plus-1.6 separate triangle budget for those responses, whereas this pass analytically integrates their whole signed combined norm.

This substantially improves EF36's eta upper ~132023. It is not decision quality: EF33 restricted source/kernel Schur lower S2>0.002, EF34 eta>0 with original analytic premises, and no proof eta<=S2 or eta>=S2 follows.

This bound is BEFORE true 469D source projection: EF37 still does not construct an original source combination v satisfying EF35's L2 square projection sufficient gate 17/12500000; it does not compute delta, eta, first-source full Schur, the other 468 exceptional columns or full original even-sector sign.

## 4. Verification and next active research entry

Native source script: `scripts/validate_rpb108_ef37_original_even_correlated_prime_pole.py`. Dedicated CI: `.github/workflows/ef37-original-even-correlated-prime-pole.yml`. It carries source-pinned 340-digit outward intervals, exact seven cutoff ordering and flags, signed pole cross primitives and the entire arch half-integer infinite tail. Verification is source arithmetic/regression; independent original Fourier normalization, physical EF26 digamma cutoff identity and form/core audit remain separate.

**EF38:** move from this improved unprojected signed bound to a genuine **correlation-preserving original source-projected L2 distance or direct cofinite energy-dual computation**, including physical seven-shift/arch/pole cross terms and continuous remainder. Source projection must be against all original 469 modes. No another global triangle estimate should be promoted unless it demonstrably narrows that interface. W-EVEN-FORM remains OPEN; W-ODD-NEG paused/OPEN; whole Weil and RH OPEN. No `main` merge.
