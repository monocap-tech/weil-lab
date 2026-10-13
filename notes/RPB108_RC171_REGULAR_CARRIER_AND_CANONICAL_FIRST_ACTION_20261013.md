# RPB108 — RC171: regular carrier and canonical first action

Aperture 11/10. Parent RC170: `2fb1048057f4e0fc60c235f1ecfef42f3cea6fbe`.
Only `research/rpb108-route-consolidation` is written. Historical checkpoints and Lean remain unchanged.

RC171 realizes the first regular action in the finite Legendre carrier. It pays D^-1 R P0 through even degree 256 with full D-energy error below 0.000179349. Combining this polynomial with the exact existing endpoint response gives the first actual canonical action D^-1 L P0 at the same displayed error. This is a source/action result; it is not a canonical inverse or an original Weil response.

| Component | Outward norm or energy upper |
|---|---:|
| Projected regular D-action norm error | 0.000125207 |
| Full omitted D-action squared energy | 1.648926e-8 |
| Complete regular D-action norm error | 0.000179349 |
| Complete canonical first-action norm error | 0.000179349 |

The projected error and the actual omitted tail occupy orthogonal D coefficient supports. Their squared bounds are added before taking the final root. Exact endpoints appear in the certificate. The approximation uses 129 even coefficients, not a truncation that assumes the remote action vanishes.

## Exact finite Poisson–Legendre projection

RC170's rational nodes and positive weights are reconstructed and their joint SHA-256 digest is checked. Put u=x/B, c=2 pi_kernel B/t, h=1/c and z=1+i h. The kernel pi is the rational center of RC170's actual pi enclosure; its effect on the action is separately paid.

Define elementary complex moments

\[
Q_n(z)=\frac12\int_{-1}^1\frac{P_n(u)}{z-u}\,du.
\]

Integration gives Q0=(1/4)log(1+4c^2)-(i/2)atan(2c) and Q1=z Q0-1. The Legendre three-term recurrence, together with integral P_n=0 for n>=1, gives

\[
Q_{n+1}=\frac{(2n+1)zQ_n-nQ_{n-1}}{n+1}.
\]

The Poisson constant-source profile is [atan(c(1-u))+atan(c(1+u))]/pi_kernel. Its zeroth Legendre coefficient is [-4 Im Q0-2h Re Q0]/pi_kernel. For positive even n its coefficient is

\[
-\frac2{\pi_{kernel}}\operatorname{Im}(Q_{n+1}-Q_{n-1}).
\]

To verify the last formula directly, integrate P_n once as (P_(n+1)-P_(n-1))/(2n+1); its endpoint values vanish. Partial fractions give integral P_n/[1+c^2(1-u)^2]=-2h Im Q_n. Reflection supplies the opposite-endpoint sign. No sampled quadrature of the boundary layer is used.

The 2,198 nodes with c>=1/4 use this recurrence through Q257. Directed 360-digit arithmetic and explicit logarithm/arctangent series remainders enclose the potentially cancelling moments. The arithmetic width of each final coefficient is checked to be below 10^-30 before selecting a rational center.

For the 1,898 far nodes with c<1/4, both arctangent arguments have absolute value below 1/2. A 32-term alternating series produces a degree-62 even polynomial and full uniform remainder at most 2(2c)^65/(65 pi_kernel) per node. Signed polynomial moments are combined across nodes before projection. The exact conversion factor from u^j to P_n is (2n+1)j!/[(j-n)!!(j+n+1)!!], for j>=n with matching parity. This avoids ill-conditioned forward moment recurrences at remote nodes while retaining the entire action-error payment.

The small replacement of actual pi by pi_kernel costs at most 4 times its radius divided by pi_lower in Poisson operator norm, per weighted term. This follows by differentiating the physical kernel with respect to pi: the absolute derivative is at most 2k/pi, and its full-space L1 norm is bounded uniformly over the enclosed pi interval. That error, the far-node remainder and RC170's full operator error are all included.

## Actual regular-action tail

Write k=F^-1 log(1+e/abs(xi)). The positive Poisson integral makes k even and nonnegative. RC118's multiplier identity and Plancherel give ||k||_2^2=2 I2, with I2=e pi^2/3. For f=R P0,

\[
f'(x)=k(B+x)-k(B-x),\qquad \|f'\|_2^2\le2I_2.
\]

The last bound uses positivity to drop the negative cross term and evenness to bound the two restricted kernel energies by the whole kernel energy. Differentiating the positive kernel integral at positive distance d and using 1-exp(-et)<=et gives |k'(d)|<=2e/d. Consequently |(B^2-x^2) f''(x)|<=4eB.

For the physical Legendre differential operator A=-d/dx((B^2-x^2)d/dx),

\[
\|Af\|_2\le\sqrt{8B^2I_2}+4eB\sqrt{2B}=:K_A.
\]

These estimates imply f' is in L2 and Af is in L2. The boundary flux vanishes because the positive kernel bound grows at most logarithmically as d tends to zero, so integration against the Legendre equation has no unpaid boundary term. Equivalently, the weighted differential operator's natural weak domain gives the same coefficient identity.

Thus the actual coefficients satisfy sum_n [n(n+1)]^2 m_n |f_n|^2 <= K_A^2. Since f is even and D_n=H_n+s increases with n, the entire D^-1 tail after degree 256 obeys

\[
\sum_{n\ge258,\ n\ even}\frac{m_n|f_n|^2}{D_n}
\le\frac{K_A^2}{[258\cdot259]^2(H_{258}+s_{lower})}.
\]

This bound concerns the actual regular action, not just the quadrature polynomial. Finite coefficient and D-constant errors are paid independently on the retained support. A rational lower square root is used when dividing the physical error by sqrt(s_lower).

## Canonical first action and metric pairing

RC126's exact endpoint identity is C P0=((1-log2)/s)P0+f0+psi0. With r=789/125 and L=D+h+R-rI, it gives

\[
D^{-1}LP_0=\left[1+\frac{1-\log2-r}{s}\right]P_0+f_0+\psi_0+D^{-1}RP_0.
\]

RC171 therefore supplies a concrete finite-plus-analytic trial: the new regular polynomial, the existing exact f0 and infinite psi0, and a rational center for the constant correction. Its constant and full regular errors are paid. The analytic f0/psi0 definitions retain the actual s; any later numerical realization must keep their existing coefficient/tail contracts.

The zeroth regular coefficient also gives <P0,L P0>=2B[s+1-log2-r+(R P0)_0]. RC171 records an actual interval for this single canonical metric pairing, with RC170 operator error and all representation errors included. Its lower exceeds the inherited embedding floor on this direction. This does not improve the full-space canonical floor or establish a positive original Weil direction.

Remaining work: extend the regular carrier action to the required source family or execute an inverse correction whose subsequent endpoint and regular actions have paid full errors. The seven-source reference inverse certificate is preserved. Full canonical iteration, Stage I tolerance/closure, original augmented responses, whole-aperture positivity, Global/F4, RH and Lean remain open.

## Reproduction

Run `python scripts/validate_rpb108_rc171_regular_legendre_projection.py --output certificates/rpb108_rc171_regular_legendre_projection.json` with RC170, RC169, RC121 and RC129 certificate paths in that order. Repeat with `--replay` to reverse all 4,096 Poisson nodes, including the signed far-moment accumulation, and compare the complete rational certificate. The validator checks dependency hashes, the original node digest, all coefficient intervals, positive-tail contracts and final norm bounds. Historical files are unchanged.
