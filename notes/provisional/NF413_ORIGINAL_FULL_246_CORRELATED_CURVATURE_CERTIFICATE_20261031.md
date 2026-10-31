# NF413 — Full original 246-source physical curvature Gram (certified)

2026-10-31 PT. Canonical W-ODD-NEG; unchanged NF370 fourth u4, 242 original selected and four original critical source functions, B=11/10, seven signed prime powers and original NF404 pole shear retained.

## Previous / current / next

Previous NF412: analytic small-t symmetric arch I0 error bound was correct, but four-critical-only curvature plus NF374 exterior w4 curvature was NOT a true u4 curvature certificate. The exact 242+4 source triangle was valid but far too loose (upper order 10^144). Prior invalid interpretation remains explicitly superseded in draft PR #408.

Current NF413: 4096-bit Arb FULL original 246-source analytic physical Gram, with 242 selected polynomial-sine/cosine source generators, all four original critical source shapes, all 32 source critical sine frequencies, and odd sinh pole; every selected–selected, selected–critical and critical–critical physical cross survives before norm evaluation. The exact native coefficients are merged at shared physical basis keys before transcendental interval evaluations. All native 4096-bit source coefficient radii are paid at derivative order TWO.

Focused original GitHub Actions #41225707791 SUCCESS. Durable original-source certificate is notes/data/provisional/NF413_original_full_246_source_curvature_native.json, source SHA-pinned. Independent source endpoint and derivative are verified against NF411 original native receipt, not an invented source.

**Accepted physical source result:**

- Midpoint original full source ||u4_mid''||_L2(-B,B)^2 approximately 17768.07940443482530; complete interval given in attached Arb receipt.
- True original supported u4 curvature satisfies ||u4''||_L2(-B,B) < 256 (integer outward bound; coefficient uncertainty explicitly included).
- This is the SAME u4 on which NF404 and NF407 operate, not a four-critical or selected-only substitution. No physical x quadrature.

## Source correlation and analytic Gram

Write original true midpoint source, after exact dyadic physical coefficient consolidation,

u4(x) = sum_(f,k) a_(f,k)*x^k*phi_k(2*pi*f*x) + b*sinh(x/2),
phi_k = sin when k even, cos when k odd.

All 242 selected physical monomial trig source generators and all 4 critical expansions with 32 sine frequencies are included. Both u4(B) and u4'(B) from this formula overlap the independent NF411 4096-bit original endpoint Arb values.

For even k,
 (x^k sin wx)'' = k(k-1)x^(k-2)sin(wx) + 2kw x^(k-1)cos(wx) - w^2 x^k sin(wx).
For odd k,
 (x^k cos wx)'' = k(k-1)x^(k-2)cos(wx) - 2kw x^(k-1)sin(wx) - w^2 x^k cos(wx).
For pole: (sinh(x/2))'' = sinh(x/2)/4.

Each derivative basis is odd. For f rational, define C_(2m)(f)=int_-B^B x^(2m)cos(2*pi*f*x)dx and S_(2m+1)(f)=int_-B^B x^(2m+1)sin(2*pi*f*x)dx. Their analytic recurrence, with omega=2*pi*f, is:

 C_0(f)=2sin(omega B)/omega,
 S_(2m+1)(f)= -2 B^(2m+1)cos(omega B)/omega + (2m+1) C_(2m)(f)/omega,
 C_(2m+2)(f)=2 B^(2m+2)sin(omega B)/omega - (2m+2) S_(2m+1)(f)/omega.

At f=0, C_(2m)(0)=2 B^(2m+1)/(2m+1), S_(2m+1)(0)=0. Original source terms are multiplied by complete product-to-sum signed sine/cosine formulas before summing.

Each source-pole cross is integrated using the exact finite recurrence for int_-B^B x^m exp((1/2+2*pi*i*f)*x)dx, extracting real or imaginary part as appropriate. The pure pole squared power is sinh(B)-B.

This is the entire physical signed quadratic beta^T G^(2) beta, including all original 246 source directions. It has 273 distinct nonzero physical second-derivative basis terms after exact source consolidation. The native second-derivative coefficient error S2 uses an independent rational weighted generator derivative bound; its full L2 charge is <(3/2)S2.

The full Gram is independent of the original outer x quadrature / original arch physical t quadrature and establishes a true operator-input source curvature bound.

## Original arch t=0 error is now certified

For 0<h<=1/2, write D_t u(x)=u(x)-[u(x+t/2)+u(x-t/2)]/2. For 0<t<min(h,2(B-x)) on positive physical support,

 ||D_t u||_{L2(0,B)} <= (t^2/8) ||u''||_{L2(-B,B)}.

The physical arch kernel K(t)=exp(-t/4)/(1-exp(-t))<2/t, so Minkowski gives

 ||int_0^min(h,2(B-x)) K(t) D_t u(x)dt||_L2(0,B)
   <= h^2/8 * ||u''||_L2(-B,B).

For the TRUE original supported u4 and h=10^-10, substitute M=256:
 positive-half error <3.2e-19,
 whole odd physical error <4.8e-19 using sqrt(2)<3/2.

This is below 9e-17/8. The original NF409 0<t<1e-10 omitted kernel contribution now has an independent certified L2 upper. For h=10^-12 or 10^-14 the same theorem yields 1e-4 / 1e-8 times this charge, respectively. NO unverified Gauss-mesh agreement used.

## What remains OPEN

NF413 certifies only the small-t I0 error, not any final z enclosure. The larger t>=h arch integrals I0 and I1 remain unvalidated; original continuous z(x) Taylor coefficients and remainders on cells 6,3,7 and remaining five remain UNMEASURED. True signed original z/p cross and complete scalar E_true remain UNDECIDED against NF404 C≈1.0950537731e-21. The fourth J242-perp lowband, original domain, infinite inverse, W-ODD-NEG, even/whole Weil and RH remain OPEN.

**Next NF414:** source-correlation-preserving interval/Taylor integration of the true original continuous arch t>=h and signed prime translations, prioritize original cells 6,3,7, then all remaining cells; combine NF410 exact principal moments and decide NF404 entire centered scalar only from a fully certified interval.

No source modifications, signed cell additions, historical replacement, main merge or theorem promotion.

Source script: scripts/local_replay/nf413_original_full_246_curvature_gram_native.py.
CI workflow: .github/workflows/nf413-full-original-246-curvature.yml.
Actual verification: https://github.com/monocap-tech/weil-lab/actions/runs/41225707791.
