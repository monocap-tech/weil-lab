# RPB108 — RC242: original actions on residual-shaped trials

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC241: `7ab2888f9c9e7fd76468ccb66d3387c24d641b69`. Branch: research/rpb108-route-consolidation.

RC242 certifies the complete original Weil actions on the two exact residual-shaped polynomials R0 and R1 prepared in RC241. Their finite output is retained through degree 128, and all omitted output and model faults are paid in D energy. This supplies new original-action data for trials aimed at the source-fit obstruction found in RC241.

The rational augmentation actions on these inputs and their enriched inverse responses are not evaluated in this pass. The actual response sources remain N0 P0 and N0 P1. There are eight certified original-action inputs, six certified augmented-action inputs, and the previous three-trial response enclosures remain unchanged. Full signed positivity, original whole-space positivity, Stage I, RH, F4 and Lean remain open.

## Exact residual inputs and stable physical bounds

Each input is the exact rational polynomial recorded by RC241,

\[
R_p(x)=\sum_{n=0}^{64}a_{p,n}P_n(x/B),
\qquad a_{p,n}=0\text{ for }n\not\equiv p\pmod2.
\]

The coefficients were rounded to the 10^-60 grid when selecting the trial. They now define the exact input: uncertainty in its origin as a proposed residual is not added to the action error of this exact polynomial. RC241 separately records the small difference from the unrounded retained-center residual.

Orthogonality gives exact physical norm squared sum_n m_n a_n^2 and actual D-energy intervals sum_n m_n(H_n+s)a_n^2, with m_n=2B/(2n+1). Direct polynomial integration independently verifies the physical norm.

The monomial representation of a degree-64 Legendre expansion can have large cancelling coefficients. To control moving prime supports, use the input bounds

\[
\|R\|_\infty\le\sum_n|a_n|,
\qquad
\|R'\|_\infty\le B^{-1}\sum_n|a_n|n(n+1)/2.
\]

The validator checks Laplace's polynomial identity through every input degree 0–64. For t in [-1,1], its integral representation has integrand (t+i sqrt(1-t^2) cos(theta))^n of modulus at most one, proving |P_n(t)|<=1. The positive Legendre expansion

\[
P_n'(t)=\sum_{k<n,\ n-k\text{ odd}}(2k+1)P_k(t)
\]

is also checked exactly at every such degree; its coefficients sum to n(n+1)/2. These proofs justify the stable physical input bounds. No sampled supremum is used.

## Complete original action

Use the unchanged direct identity

\[
N_0=I+D^{-1}(h-rI-K_{\rm reg}+K_{\rm prime}+K_{\rm pole}),
\quad r=789/125.
\]

The entire regular convolution is computed by the generic polynomial beta-integral construction, with physical reflection enforcing the input parity. Exact Legendre projection separates its degree-128 retained output from its full remaining polynomial output. Direct integration checks the first eight coefficients. Low-degree control inputs replay the RC237 convolution formula.

For the prime action, sum every active translation pair before taking norms. The active set remains 2,3,4,5,7,8,9, each with both orientations, on fifteen physical support segments. Select rational model translations and coefficients on the 10^-16 grid to make the higher-degree exact integrations practical. The error radii use the maximum distance from each selected value to either endpoint of its pinned actual interval, explicitly paying this extra parameter rounding. Moving supports pay the proved input supremum and derivative bounds, while coefficient errors pay the exact physical input norm. Thus full-output prime uncertainty remains certified despite the much larger input degree.

Exact segment monomial integrals are cached and then paired with the Legendre polynomial coefficients. Checked reflection allows mirrored segment moments to be combined and opposite-parity moments to be set to zero. Direct segment integration independently checks the low output coefficients. Each segment's squared norm is replayed in affine coordinates. This rearranges exact rational polynomial integration and preserves all cross-prime terms. The full prime physical norm minus the retained degree-128 norm bounds its complete omitted output.

The certificate records a SHA256 of the exact segment endpoints and polynomial coefficients. The digest uses sign bytes and length-prefixed big-endian numerator/denominator bytes; it avoids decimal serialization of very large exact fractions. Rounded lower/upper physical output energies are recorded separately.

Both signed pole terms use the moment of the full residual input against the degree-40 cosh/sinh Taylor polynomial and its complete error bound. The exact residual parity fixes the pole sign. Finite original output coefficients pay the actual s interval, endpoint log2 enclosure and rational rounding.

## Combined endpoint tail

For output degree n above the input degree, the full input's endpoint coefficient is

\[
c_n=(2n+1)\sum_{d=0}^{64}
\frac{a_d}{(n-d)(n+d+1)}
\]

on the input parity. Squaring this combined coefficient retains all cross-input terms. The validator sums the resulting D-energy tail exactly, with upward rounding, from degrees 129 through 256.

Beyond degree 256, apply the RC238 elementary summand bound to each input Legendre column and combine the complete tail norms by the triangle inequality:

\[
E_{h,>256}\le
\left[\sum_d|a_d|
\sqrt{\frac{3B}{(H_{\rm first}+s_{\rm lower})(256-d)^2}}\right]^2.
\]

Here first is the first same-parity degree above 256. The underlying inequality 2B(2n+1)/[(n-d)^2(n+d+1)^2]<=6B/(n-d)^3 holds whenever n>d; all used tail degrees meet that condition. The explicit combined tail and this remaining tail together pay the entire endpoint output outside degree 128.

Regular, prime and pole omitted output is likewise paid with the first omitted D weight. The complete original action error adds the finite-rounding, endpoint-tail, regular-tail, prime-tail, regular-kernel, prime-arithmetic and pole-Taylor fault norms before squaring. Opposite parity makes the two-input error Gram diagonal; no same-parity error independence is inferred.

## Original form pairings and output norms

The exact input degree is at most 64, while the action retains through degree 128. Hence every omitted projected output is orthogonal to the input polynomial. The sharp original form interval pairs the input with retained output coefficient intervals in actual D energy and adds only the regular-kernel, prime-arithmetic and pole-Taylor model faults. It does not needlessly charge orthogonal omitted outputs to that pairing.

Complete original output D-energy intervals, in contrast, do pay the full action error using forward/reverse triangle inequalities. The certificate records both forms and output norms, as well as the relative squared action error. These remain statements about R0 and R1, not a positive full original operator.

| Certified quantity | R0 (even) | R1 (odd) |
|---|---:|---:|
| Complete original squared D error upper, rounded upward | 0.000088843 | 0.000085108 |
| Squared error divided by input D energy, rounded upward | 0.005523918 | 0.005018610 |
| Original test form lower, rounded downward | 0.004170908 | 0.004139699 |
| Original test form upper, rounded upward | 0.004170915 | 0.004139707 |

Both original form lower endpoints are strictly positive. Exact rational comparison of each lower endpoint to its input D-energy upper bound gives

\[
\langle z,N_0z\rangle_D\ge\frac{61}{250}\|z\|_D^2,
\qquad z\in\operatorname{span}\{R_0,R_1\}.
\]

The coefficient 61/250=0.244 is rounded conservatively below the smaller ratio. Opposite parity makes both the D cross term and the actual original form cross term vanish, so this inequality covers every complex combination of the two inputs. This is actual original-form positivity on a two-dimensional residual trial span; it is not a full original auxiliary-norm certificate or Stage I closure.

## Verification and remaining step

The validator checks 161 pinned input/helper blobs. Exact replay reverses pinned read order, mirrored-segment moment accumulation and endpoint tail summation, requiring equality with the stored certificate. Independent exact controls cover Legendre bounds, generic convolution, low-degree prime projection and affine segment norms.

Publication adds this note, the validator and the certificate to RC241 while preserving existing repository blobs. The previously certified original-action inverse-response upper bounds remain 23.389542374 even and 29.021020187 odd when rounded upward. The canonical eight-source metric-inverse width remains the separate 485647/1000000.

Next: certify the actual rational augmentation actions on R0 and R1, then evaluate the enriched residual-shaped response space with all cross terms and complete faults paid. That step must confront the fixed-trial obstruction proved in RC241. Completion still requires the full signed form on the 248-dimensional even and 391-dimensional odd parameter spaces, or an equivalent uniform proof.
