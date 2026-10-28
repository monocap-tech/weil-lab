# Weil-Lab — NF371: finite-direction strong domain and boundary-jet feasibility gate

**Date:** 2026-10-28. **Standing:** LOCAL ANALYTIC PREFLIGHT ONLY. `W-ODD-NEG` OPEN; infinite signed exterior residual **NOT** certified; all original operator-realization assumptions retained. No GitHub commit, no RH transfer. Original J242, four PR348 critical functions, NF369 exact dyadic Y0, and NF370 exact T,d remain unchanged.

## 1. Source and scope

Read `NF370_DYADIC_WHOLE_EXTERIOR_RESIDUAL_GATE.md`, `NF370_ORIGINAL_SOURCE_SHEAR_AND_SMOOTH_SIGNED_FORCING.md`, `NF367_QUOTIENT_FORM_ENERGY_TRANSFER.md`, and native producer `verify_rpb108_nf369_critical_quotient_schur.py` from the live draft PR #356 head `f929a4a3a3811b7fcc2411d6d2df6117c7e94750`. The mathematical basis is the original SI29 selected generators `x^k sin(2 pi c x)` for even k, `x^k cos(2 pi c x)` for odd k, plus supported `sinh(x/2)`; the original four f_i use 32 sine frequencies `c_n=5n/11` and a shared supported sinh. These source functions are smooth on the closed interval `[-B,B]`, `B=11/10`, but their zero extensions need not be continuous at its endpoints.

The historical reconciliation changed custody, not any original hypothesis. This note is a **new conditional finite-source analytic reduction**, not a numerical original-operator test.

## 2. Fixed matched four trials and strong representative

Write `f=p+E`, with `p=P_J f` and `E=Q f` as four-column maps. Let `Y0` be the previously fixed dyadic four-by-four NF369 trial, and let `t_i=T e_i` be the exact NF370 dyadic directions. Define

    u_i = p t_i - E Y0 t_i = f t_i - E (I+Y0)t_i.

Because J242 and f are finite spans of the original supported piecewise-C2 generators, **each particular u_i is piecewise C2 and in W^{1,1}(-B,B)**. Extend it by zero to R. By integration by parts its Fourier transform is O(1/|xi|). Under the inherited original complete Fourier multiplier realization, `a_o(xi)<=17+log|xi|` for `|xi|>=1`, `|kminus|<=17`, and `a_o` is bounded on `|xi|<=1`. Thus `a_o hat(u_i)` and `m hat(u_i)` belong to L2(R), and `u_i` belongs to the *strong compressed-operator domain* of the original form realization. In particular

    h_i := Q W u_i = Q P_I F^{-1}[m hat(u_i)] in L2(I),

since the bounded odd pole `-2|s><s|` is annihilated by Q (s lies in J242). Therefore the full exterior residual functional has the **finite-trial** strong representative `h_i`:

    R(t_i)(v) = <h_i,v> for v in J242^perp ∩ D(c).

The claim is conditional on the original compressed multiplier operator being identified with the inherited closed form. It **does not** settle the general original-domain audit and does not provide an upper bound for `||h_i||`.

## 3. Explicit endpoint-jet Fourier bound

Every `u_i` is odd. Set `k=2 pi xi`. Two integrations by parts on `[0,B]` show, for `xi!=0`,

    |hat(u_i)(xi)| <= |u_i(B)|/(pi |xi|)
            + (|u_i'(B)| + int_0^B |u_i''(x)|dx)/(2 pi^2 |xi|^2).

This is a true boundary-jet bound and does not infer endpoint data from weak-form smallness. Set

    alpha_i = |u_i(B)|/pi,
    beta_i  = (|u_i'(B)| + int_0^B |u_i''|)/(2 pi^2),
    L = 17+log Lambda,  Lambda>=1.

For the full signed multiplier `m`, the inherited `|m(xi)|<=17+log|xi|` at `|xi|>=1` gives

    ||1_{|xi|>Lambda} m hat(u_i)||_2 <= alpha_i sqrt(J2) + beta_i sqrt(J4),
    J2 = 2/Lambda * (L^2+2L+2),
    J4 = 2/Lambda^3 * (L^2/3+2L/9+2/27).

The formulas are exact calculus identities; numerical evaluation requires outward enclosures of pi, log Lambda, and the boundary-jet quantities. If `u_i(B)=0` the leading tail disappears and the sufficient envelope improves from essentially `Lambda^-1/2 log Lambda` to `Lambda^-3/2 log Lambda`. The original f_i sine parts individually have zero boundary trace because `2 pi (5n/11)(11/10)=pi n`; this does **not** establish that the matched u_i has zero boundary trace after subtraction of E(I+Y0).

## 4. Fully matched whole-infinite sufficient test

Let `H_i(Lambda;j_i)` be the physical L2 norm of

    P_I F^{-1}[1_{|xi|<=Lambda} m hat(u_i)] - j_i,

with an *explicitly specified selected-space trial* `j_i` in J242. Q-contraction and physical support, without commuting Q through a frequency cutoff, give

    ||h_i|| <= H_i(Lambda;j_i) + alpha_i sqrt(J2) + beta_i sqrt(J4).

With `mu0=49/50000` and the NF370 `d_i`, this implies the exact full four-direction acceptance criterion

    SUM_i (H_i + alpha_i sqrt(J2) + beta_i sqrt(J4))^2/(mu0*d_i) <= 1.

This criterion can be certified by four physical low-band residuals and four explicit high tails; it does **not** require computing C^{-1} or treating a finite Galerkin probe as an infinite upper.

## 5. No silent transfer from NF367 form smallness to boundary traces

NF367's very small `a(Ez,Ez)` and physical L2 quotient do **not** bound `E(B)` or `E'(B)`. In the relevant logarithmic-energy topology, point trace is not a continuous functional: a smooth interior-supported near-boundary pulse of unit endpoint value and width epsilon has L2 norm O(sqrt(epsilon)) and logarithmic-energy squared O(epsilon log(1/epsilon)) while its endpoint stays 1. Consequently the endpoint jet of the *actual* finite matched u_i must be extracted from its actual coefficients, never inferred from `tr(S)<2^-604` or `a(E,E)<2^-600`.

## 6. Preliminary method-feasibility numbers (NONCERTIFYING display)

For the strict fourth NF370 individual strong-norm budget, `sqrt(mu0*d4/4) ~= 3.4648e-13`. With cutoff Lambda=2^24, elementary real numerical evaluation yields

    alpha sqrt(J2) = 0.0038080968 * |u_4(B)|,
    beta sqrt(J4)  = 2.0447807e-11 * (|u_4'(B)|+int_0^B|u_4''|).

Thus **this specific boundary-jet envelope at this cutoff**, even with a perfect low-band selected subtraction, cannot pass the individual sufficient gate unless both

    |u_4(B)| <= 9.10e-11,
    |u_4'(B)|+int_0^B|u_4''| <= 0.01695

hold (both together may still fail; the full sum matters). Those are *necessary for this chosen conservative sufficient test*, NOT necessary for actual residual positivity. No values of the two quantities were measured here; it is unknown whether either fails. The low-band H4 is also uncomputed. Larger cutoffs or sharper exact Fourier/moment cancellations may be required.

## 7. NF371 stopping point and next artifact

**Result:** Conditional finite-source strong-residual existence and a whole-frequency, source-matched, independently checkable upper **formula**. **Not achieved:** actual directional upper; endpoint jet numbers; selected low-band trial; complete signed four-plane positivity; remaining 238 modes.

**Immediate executable gate:** Recover the exact 242-by-4 physical projection X and the exact fixed 4-by-4 Y0, compute the four coefficient combinations u_i, and evaluate outward-rational/Arb intervals for `u_i(B)` and `u_i'(B)` before integrating any new low-frequency cells. First test direction 4, the smallest supplied diagonal budget. If the endpoint envelope fails, STOP this generic tail method and test explicit Fourier moment cancellation; do not start another precision/source-count campaign. Only after a viable tail envelope and an explicit selected-space low-band trial exist should expensive full-frequency integration begin.

**Jurisdiction:** `NF371 FINITE-SOURCE-STRONG-DOMAIN = CONDITIONAL ANALYTIC`, `NF371 RESIDUAL UPPER = OPEN`, `W-ODD-NEG = OPEN`, original-domain general audit OPEN, RH OPEN. No GitHub transfer authorized by this local NF request.
