# Weil-Lab NF429 — Original cell-6 Chebyshev quadratic-moment router

**2026-10-31 PT.** Canonical W-ODD-NEG OPEN; NF404 full physical centered scalar OPEN; RH OPEN. Stack this source-exact/mathematical integration pass on NF428 draft PR #436. Unchanged actual original NF370 fourth supported trial u4, NF407 242 selected plus four critical source, NF406 seven original signed prime-power seams, NF404 dyadic center, NF424 analytic transfer, NF427 degree1499 *series* cutoff, and NF428 certified first 256 z coefficients plus 1500 signed principal p-moments. No merge to main.

## Previous cursor / current circle / next

- **Previous NF428 accepted in Actions #41248984553:** Source-correlated original cell-6 z Chebyshev series coefficient intervals a0..a255, each width <1e-25, all 1500 original signed p moments m0..m1499 width <1e-25. Remaining 1244 coefficients unavailable. Original pz/z² never integrated.
- **NF429 new mathematical interface:** The **entire quadratic polynomial integration operator** on the true original cell 6 reduces to 2999 raw Chebyshev dx moments, with no x quadrature and no new original signed-prime-source calculation. Give a source-knot-authenticated native Arb evaluator, rational polynomial identity tests, optional full response/moment interval contraction that **refuses** to calculate the signed scalar if any of the 1500 source response coefficient intervals is absent.
- **Next:** Certify original z coefficients n256..1499 in bounded correlated blocks, permanently attach all 1500 interval JSON (and current NF428 artifact JSON); invoke NF429 full signed contraction with original NF428 signed p moments; then cells 3, 7, five others and whole NF410/NF404 signed acceptance.

## Exact quadratic reduction

Keep true original physical cell

J6 = (log 7 - B, log 8 - B), B=11/10.

Use only the inherited NF425/427 fixed analytic cell-6 branch, with t=(x-C)/H, C=91/100 and H=7/100. **The fixed branch outside J6 is not the physical operator.**

Let original true z on J6 admit the degree-1499 series partial sum P(t)=sum_{n=0}^{1499}a_n T_n(t), with NF427 strict uniform tail |z-P|<eps=2*10^-45. NF428 certified signed original m_n=int_{J6}p(x)T_n(t(x))dx for n=0..1499, where p=q+r is the actual original signed principal with v=u4(B)<0, W=sum_{n in 2,3,4,5,7}Lambda(n)/sqrt(n)>0 and p(x)=v*[W+(1/2)log(B/(B-x))]<0 on J6.

Define true irrational-endpoint **raw** moments

J_n = int_{J6} T_n(t(x)) dx, 0<=n<=2998.

The complete original quadratic gram is not an independent numerical integration:

int_{J6}T_i(t)T_j(t)dx = (J_{i+j}+J_{|i-j|})/2,

by the exact Chebyshev identity T_i*T_j=(T_(i+j)+T_|i-j|)/2. Consequently

int_{J6}P(x)^2 dx = (1/2) sum_{i,j=0}^{1499} a_i*a_j*(J_{i+j}+J_{|i-j|}),

int_{J6} p(x)P(x) dx = sum_{n=0}^{1499} a_n*m_n.

This requires only **2999** one-index raw moment intervals (plus the already measured 1500 signed principal moments), rather than a separate 1500x1500 table of numerically integrated Gram entries. The contraction is inherently source-correlated because the same single original-source evaluated a-vector enters both terms; each interval coefficient covers all 242+4 source generators and complete prime/pole/endpoint branches before integration.

Every raw J_n is computed directly by exact endpoint antiderivatives:

J_0 = x_R-x_L,
J_1 = H*(t_R^2-t_L^2)/2,
J_n = H*[T_(n+1)(t)/(2(n+1))-T_(n-1)(t)/(2(n-1))]_(t_L)^(t_R), n>=2.

For numerical outward enclosures, the true irrational physical endpoints are evaluated in native 2048-bit Arb as log7-B, log8-B; T_n(tL/R) uses cos(n*acos(tL/R)), avoiding unstable direct recurrence. NF406 exact rational knot certificates are independently checked. No interpolation grid, Gauss rule, physical t-source recomputation, fabricated rational endpoint, or proxy signed function is introduced.

The native script separately checks Chebyshev product-to-sum by exact Fraction polynomial multiplication and integration on rational control endpoints, including an independent nontrivial signed polynomial squared-integration test. It must produce 2999 interval J_n enclosures, each width <1e-40. A native PASS certifies precisely the raw moment vector, not any missing a coefficient or actual z².

## Exact full-input error and acceptance contract

Provided ALL 1500 original a_n source interval balls, and the NF428 1500 signed p-moment intervals, use exact rational interval arithmetic for the bilinear and quadratic contractions. In the algorithm b_k is assembled by coefficient-space products T_i T_j, exploiting symmetric i<j and accounting for T0/diagonal factors correctly.

The *analytical* NF427 truncation charge is eps=2e-45, distinct from interval widths of a_n, m_n and J_n, which are propagated inside the contraction. Since |T_n|<=1 on the actual cell,

Pmax = sum_{n=0}^{1499} max(|a_n.lower|,|a_n.upper|),

|int p(z-P)| <= eps * int |p| = eps*(-m_0), taking upper outward p-moment uncertainty, since the actual original p is strictly negative on J6,

|int(z²-P²)| <= |J6|*(2 eps Pmax+eps²).

Thus the interval cells E6,pz and E6,z2 are then genuine **true original cell6** intervals; its original non-principal signed contribution to NF410 is 4E6,pz+2E6,z2. The global NF410 also requires every other cell and exact E_p; this script does not call a one-cell result the full NF404 scalar.

The optional contraction loader checks every coefficient interval index from 0 through 1499 is present exactly once, matching NF407 source/NF406 seam digests, original prime branches, NF404 center, and width <1e-25. It verifies the signed p moment parent source/seam SHA and all 1500 moment widths. If inputs are absent, current NF429 emits ONLY the raw 2999 moment vector and explicit false scalar/acceptance flags.

## Verification / standing

- Native verifier: scripts/local_replay/nf429_original_cell6_chebyshev_square_router_native.py.
- Focused workflow: .github/workflows/nf429-original-cell6-chebyshev-square-router.yml.
- Source parents: original NF406 exact knots and NF407 242+4 source in notes/data/provisional, NF427 analytic series cutoff, NF428 source-correlated 256 coefficient interval and 1500 signed p moment artifacts.
- This is a mathematical identity plus native raw moment computation. **Numeric PASS and generated JSON interval custody are not claimed until the focused CI run confirms.**
- **No complete response coefficient vector is supplied** by this pass. NF429 must not claim a completed true cell6 z² or pz integral, whole NF410/NF404 signed scalar, original fourth J242 complement upper, W-ODD-NEG, even/whole Weil or RH.

**Disposition:** New quadratic integration obligation becomes an exact moment-contraction problem with a finite native original-cell endpoint receipt. The 1244 missing original source-correlated z modes remain the current numerical blocker. No source swaps, no source-proxy interpolation, no main merge.


## Focused original-native verification receipt (post-submission)

**Accepted exact product-algebra and native true-cell raw moments:** [Actions #41249833015](https://github.com/monocap-tech/weil-lab/actions/runs/41249833015) **SUCCESS** on committed Git head c1b3c26191870dfc7db1e1cfbf5b05cce7f9d731. The independent exact-Fraction polynomial-product and nontrivial signed square identity tests PASS. With the original NF406 irrational log7/log8 endpoints and NF407 source-identity preflight, 2048-bit Arb produced **all 2999** actual J0..J2998 dx raw Chebyshev moment intervals, strictly width <1e-40 each. The workflow also independently asserts true_original_cell6_integral_evaluated=false, NF404 signed scalar undecided and W-ODD-NEG/RH OPEN.

Source-native JSON Actions artifact: **#13061000795**, name NF429-original-cell6-2999-raw-Chebyshev-moments, ZIP digest **sha256:eab0d4968217d62d3f1b6fbf4e2077f6a82d89ad85c45d3ddf6e550abc1cb529**; retention expires **2027-01-29**. Generated interval JSON **is not yet independently committed permanently**, although the exact source, script and CI receipt are on the NF429 draft branch.

**NF429 post-CI accepted:** exact Chebyshev quadratic product/contraction identity on original J6, genuine 2999 outward native raw dx Chebyshev moments, fail-closed full-input integral router. **NF429 NOT accepted:** all 1500 z coefficients (only original first 256), actual signed complete cell6 pz/z² or NF410/NF404 signed scalar, fourth exterior bound, W-ODD-NEG, even/whole Weil, RH. The 1244 missing z coefficients are not interpolated, guessed, or set to zero.
