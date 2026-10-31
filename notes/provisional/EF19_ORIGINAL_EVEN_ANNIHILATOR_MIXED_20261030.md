# EF19 — Exact exceptional-space annihilator, original signed mixed cofinite test, and quantitative stopping line

**Date:** 2026-10-30. **Active obligation:** `W-EVEN-FORM` (OPEN). Parent EF18 [draft PR #394](https://github.com/monocap-tech/weil-lab/pull/394), **source-scoped original signed arithmetic jump** and manifest passed [Actions #41153873998](https://github.com/monocap-tech/weil-lab/actions/runs/41153873998). Parent EF18 still retains an independent archimedean pseudolocality and original form-domain audit obligation. The true original even/odd/full Weil form and RH remain open.

## 1. Why the EF18 jump cannot be treated as a Schur bound

EF18's actual original signed physical source gradient `g=P_I m(D)e` for `e(x)=1_I(x) cos(2 pi (37/64)x)` has a nonzero arithmetic support-translation jump

`J=(ln2/sqrt2)cos(407 pi/320)<-1/4`

at `x0=11/10-ln2`. The fully original 7-prime edge isolation is certified, and the archimedean log-symbol is pseudolocal near that point.

The trace jump functional is **NOT bounded on L²**: an L² function can have the same nonzero point jump while being supported on a shrinking interval, with `||h_delta||_{L²}=O(sqrt(delta))`. Therefore `|J|>1/4` alone implies **no** uniform numerical lower bound on `||Q_V g||_{L²}`, on its original signed energy-dual norm, or on the true signed inverse Schur correction `<b,C0^-1 b>`. Any proposal to do so from the jump size alone is a method STOP.

The question is how to construct a genuine **F=V469^perp** test without computing or inverting a catastrophically conditioned 469D Gram.

## 2. Genuine original 469-source annihilator: constructive finite-to-infinite trial

EF15's exact b9 original seven-prime protected cover gives 107 distinct positive rational centers `c_j` and degrees `p_j>=1`, with `sum_j p_j=469`. In the open physical interval `I=(-11/10,11/10)`, the native even sources are

`u^e_{j,k}(x)=(2 pi x)^k/k! cos(2 pi c_j x+k pi/2)`, `0<=k<p_j`.

Define the **real, monic, even constant-coefficient differential annihilator**

`P(D)=prod_{j=1}^{107} (D²+(2 pi c_j)²)^{p_j}`, of order `2 sum p_j=938`.

Each source `u^e_{j,k}` is annihilated on the open interval by its j-th factor, because
`(D²+omega²)^p [x^k exp(i omega x)] = exp(i omega x)(D²+2i omega D)^p x^k =0` for `k<p`. The other factors commute. Hence `P(D)u^e_{j,k}=0` pointwise in I for *every* generator. This is not a numerical Gram-orthogonality heuristic.

For any real even `Phi∈C_c^infty(I)`, set `f=P(D)Phi`. Then

`<f,u^e_{j,k}>_{L²(I)}=<Phi,P(D)u^e_{j,k}>_{L²(I)}=0`

by exact integration by parts without boundary terms. Thus **f is a genuine, exactly orthogonal original even complement test**: `f∈F=V469^perp`. Moreover f is smooth and compactly supported in I, and therefore belongs to the original signed log-order Fourier multiplier form domain, in fact to its strong multiplier domain.

This replaces the explicit 469D Gram inverse in the **construction** of a cofinite test. It does not yet make the cofinite Riesz inverse affordable.

## 3. Turn the actual original arithmetic jump into a nonzero mixed trial

Write `x0=B-ln2`. The true original pole-free signed physical source gradient `g=P_I m(D)e` has jump `J` at `x0` and the opposite jump `-J` at `-x0`, by original parity. All other arithmetic shifted endpoints are strictly separated from these by the authentic rational logarithmic enclosures. The logarithmic archimedean pseudodifferential term is smooth in sufficiently small neighborhoods of ±x0 by pseudolocality. Thus on each side of these isolated jumps g is smooth.

For `0<epsilon<1/100`, introduce

`theta(t)= t^937 exp(1-1/(1-t²))/937!` for `|t|<1`, and `theta(t)=0` outside `[-1,1]`.

This real smooth bump has `theta^(k)(0)=0` for `k<937` and `theta^(937)(0)=1`. Let

`phi_epsilon(x)=epsilon^937 theta((x-x0)/epsilon)`,
`Phi_epsilon(x)=[phi_epsilon(x)+phi_epsilon(-x)]/2`, and
`f_epsilon=P(D)Phi_epsilon∈F`.

The supports are interior, disjoint and avoid other original prime-power translated edges, for epsilon in the stated small range (certified rational interval separation). Because `P(D)` is monic of order 938, the distribution `P(D)g` contains the leading point singularities `J delta_x0^(937)` and `-J delta_-x0^(937)`; all lower delta derivatives vanish when paired with `Phi_epsilon` because its lower-order central jets vanish. The smooth remainder pairing is `O(epsilon^938)` since the detector amplitude scales as `epsilon^937` and its support length as epsilon. Consequently

`q0(e,f_epsilon)=<g,P(D)Phi_epsilon> -> -J > 1/4` as epsilon->0.

In particular, **there exists** a sufficiently small, finite epsilon in this explicit source-defined family with

`q0(e,f_epsilon) > 1/8`.

This is a **genuine original signed exceptional-to-infinite mixed pairing with an exact cofinite trial**, not a surrogate upper cap or an abstract Schur model. The value 1/8 is an **existential unnormalized bound**; no explicit epsilon or certified finite physical quadrature has yet been supplied. The exact rational validator checks the authentic original source/phase/translated-edge isolation, the 469-source/938-order algebra and delta-jet coefficient. The full analytic pseudolocality/domain argument is in this note and still requires independent audit.

## 4. Schur interpretation and explicit remaining numerical gate

Let `b_e(w)=q0(e,w)` on F and `C0=q0|_F>=mu I`, `mu=17/25000` under inherited original SI10 closed-form hypotheses. For any **explicit** `f_epsilon∈F`, positivity and Cauchy-Schwarz give the *true original* inverse-coupling variational bound

`<b_e,C0^-1 b_e> >= |q0(e,f_epsilon)|² / q0(f_epsilon,f_epsilon)`.

When the existential bound above holds, its numerator is `>1/64`. But **NO numerical Schur certificate has been obtained**, because the original signed positive denominator `q0(f_epsilon,f_epsilon)` is uncomputed and f_epsilon has very high differential order.

### Proven normalization METHOD STOP: the narrow bump worsens the real Schur bound

Because `P(D)` is **monic and even order 938**, and the bump `Phi_epsilon` scales as `epsilon^937 theta((x-x0)/epsilon)`, the leading derivative `D^938 Phi_epsilon` has L²-squared norm proportional to `epsilon^(-1)`, with a strictly positive coefficient `c=(1/2)||theta^(938)||²_{L²(R)}>0` from the two reflected, disjoint lobes. The next-highest order in `P(D)` is **936**, with squared norm scaling `epsilon^(+3)`: all lower derivative coefficients are fixed, even if individually enormous. Consequently,

`||f_epsilon||²_{L²(I)} = c/epsilon (1+o(1))`.

By the genuinely original SI10/EF15 complement floor, conditional on its closed-form analytic proof,

`q0(f_epsilon,f_epsilon) >= mu ||f_epsilon||² >= (mu*c)/(2 epsilon)` for small enough epsilon.

Yet the ORIGINAL signed mixed numerator tends to the finite value `-J`. Therefore the precise true original cofinite **variational Schur lower obtained from THIS test family** satisfies

`0 <= |q0(e,f_epsilon)|²/q0(f_epsilon,f_epsilon) = O(epsilon) -> 0`.

This is an actual **localized-annihilator method-class STOP**: shrinking epsilon to expose the jump more cleanly makes the normalized inverse-correction certificate **worse**, not better. A raw unnormalized `>1/8` is not a useful positive lower on the inverse Schur energy (it can be altered by rescaling f). The original strict nonzero mixed operator remains correct; it is not numerically resolved by this narrow-bump limit.

The exact-rational validator separately checks the formal derivative scaling exponents `-1` and `+3`. Neither these exponents nor a green workflow substitutes for a certified finite physical `q0(e,f)` and `q0(f,f)` at an explicit epsilon.

**Next EF20 acceptance:** either (a) exhibit an explicitly fixed epsilon and a **certified original full signed mixed numerator and full signed positive denominator** for this exact F trial, or (b) replace order-938 annihilation by a verified lower-order/source-conditioned finite nullspace construction with both actual mixed and energy-bound measurements; then apply the original cofinite variational inequality. Do not derive a false `||B0||` floor solely from point jump magnitude, do not restart conservative-cap dominance and do not assume the 469-dimensional source Gram is well-conditioned.

**Current scope:** 469-source source-annihilator algebra and original jump coefficient are exact-rational checkable; arch pseudolocality, original unbounded form attachment and finite-epsilon quantitative certificate remain independently AUDIT/OPEN. W-EVEN-FORM, paused W-ODD-NEG, W-WHOLE-FORM and RH OPEN.
