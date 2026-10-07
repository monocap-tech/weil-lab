# RPB108: logarithmic collar concentration sharpens the actual gain criterion

Date: 2026-10-06 (America/Los_Angeles). Source `99301c708c5660792150bd8d9c5b94b67f85aa69`.
Definitions: [exterior collar gain registry](../docs/TERMINOLOGY_RPB108_COLLAR_GAIN.md).
Global/F4 lane. No aperture computation or actual null existence assertion.

## Actual endpoint statements

Fix a hypothetical nonnegative actual contact c and a full-null vector h. Use a fixed finite separating actual selection with effective covariance uniformly coercive near c: g_t(v,v)>=beta E_1(v), beta>0. Choose b>c with no new prime threshold in (2c,2b], retaining all equality terms at c. The full physical residual q_h is locally L2 by the established domain promotion and is zero on (-c,c).

For 0<s<min(b-c,exp(-2)), the enlarged residual's effective inverse energy satisfies the new estimate
\[
\boxed{e_s(h)\le\frac{10}{\beta\log(1/s)}M_s(h).}
\tag{1}
\]
Combining this with the quadratic gain theorem and the derivative collar estimate gives the exact criterion
\[
\boxed{h\in H^1(\mathbb R)
\ \Longleftrightarrow\ M_s(h)=O(s^2\log(1/s))
\ \Longleftrightarrow\ M_s(h)=o(s^2).}
\tag{2}
\]
In addition, existing actual logarithmic bootstrap implies, for every fixed N>=0,
\[
M_s(h)=o((\log(1/s))^{-N}),\qquad
e_s(h)=o((\log(1/s))^{-N}).
\tag{3}
\]
These are conditional analytic actual-null conclusions, with constants uniform on the fixed kernel for physical mass one. They do not supply the s^2 log(1/s) bound in (2), and do not exclude contact.

## Small-set concentration in the canonical logarithmic domain

Let v be any whole-line vector with E_1(v)<infinity, not necessarily null. For a measurable set Omega of measure 2s, split Fourier(v) at N_s=s^(-1/2). Cauchy-Schwarz on [-N_s,N_s] gives
\[
\|v_{lo}\|_\infty^2\le2N_s\|v\|_2^2,
\quad \|1_\Omega v_{lo}\|_2^2\le4sN_s\|v\|_2^2.
\]
The high-frequency mass is at most E_1(v)/log N_s, since w>=log N_s there. As w>=1, ||v||_2^2<=E_1(v). The squared triangle inequality therefore gives
\[
\|1_\Omega v\|_2^2
\le\left(8\sqrt{s}+\frac4{L_s}\right)E_1(v)
\le\frac{10}{L_s}E_1(v),\qquad L_s\ge2.
\tag{4}
\]
For the last bound, L exp(-L/2)<=2/e for L>=2, so 8 L exp(-L/2)<=16/e<6. The elementary series gives e>8/3. No support indicator boundedness on H1 or boundary trace is used.

More generally, for each integer p>=1 the same split gives
\[
\|1_\Omega v\|_2^2
\le\left(8\sqrt{s}+\frac{2^{p+1}}{L_s^p}\right)E_p(v)
\le\frac{C_p}{L_s^p}E_p(v),
\quad C_p=8(2p)^p+2^{p+1}.
\tag{5}
\]
Indeed sup_(L>=2) L^p exp(-L/2)<=(2p)^p. These are finite-p estimates; no uniform limit in p is claimed.

## Effective residual estimate and equivalence

The frozen actual cutoff agrees with the native cutoff for t=c+s in this small interval. Domain promotion eliminates endpoint distributions. Thus for v in D_t the full mixed residual is the ordinary pairing
\[
Q_t(v,Ih)=\int_{\Omega_s}\overline{v(x)}q_h(x)dx
\]
up to the repository's equivalent conjugate-slot convention. Its squared dual g_t norm is exactly e_s(h), by COMPENSATOR_RESIDUAL. Cauchy-Schwarz, (4) and g_t>=beta E_1 yield (1) by taking the supremum over g_t-unit tests. This estimates the full residual, not the core and pole separately.

If M_s=O(s^2 L_s), then (1) gives e_s=O(s^2). QUADRATIC_GAIN_REGULARITY proves that h is globally H1. Conversely for globally H1 null h, supported-L2 promotion gives h' in K_c; q_h'=q_(h') is locally L2, q_h is locally H1 across both boundaries, and its endpoint traces are zero. The already audited collar Poincare estimate gives
\[
M_s(h)\le\frac{s^2}{2}\|q_{h'}\|_{L^2(\Omega_s)}^2=o(s^2).
\tag{6}
\]
Finally o(s^2) implies O(s^2 L_s). This proves (2). Only the converse takes traces, after global H1 and derivative promotion have been proved; no trace of a general logarithmic null vector is assumed.

## Every finite logarithmic order localizes the full residual

The actual bootstrap proves h in X_k for all finite integers k, with fixed-window bounds ||h||_(X_k)<=L_(c,k)||h||_2. Since |m_c|<=(1+C_c)w, the global core m_c(D)h has every finite logarithmic Fourier weight. The pole is only locally L2, so do not assign the full q_h a global L2 norm.

Instead choose chi smooth and compact, equal to one on [-b,b]. Multiplication by chi preserves every E_p space. To check it explicitly, e+|xi|<=(e+|eta|)(e+|xi-eta|), and w>=1 imply
\[
w(\xi)^{p/2}\le2^{p/2}w(\eta)^{p/2}w(\xi-\eta)^{p/2}.
\]
Fourier convolution and Young's L1-L2 bound then give
\[
\|\chi f\|_{E_p}\le2^{p/2}\|w^{p/2}\widehat\chi\|_1\|f\|_{E_p}.
\tag{7}
\]
Here ||f||_(E_p) denotes sqrt(E_p(f)). The weighted cutoff transform is integrable since chi is smooth compact. The localized pole chi p_h is smooth compact with moment bounds proportional to ||h||_2. Consequently E_p(chi q_h)<infinity for every finite p, bounded on the actual fixed kernel by a constant times physical mass.

Apply (5) to chi q_h, which agrees with q_h on both collars. For any N choose an integer p>N; then M_s=O(L_s^-p)=o(L_s^-N). Equation (1) proves the gain statement in (3). This extracts a physical collar rate from the previously spectral logarithmic bootstrap. The constants grow with p; optimizing p as a function of s is not justified by these fixed-p statements.

## The inverse logarithm is sharp on the general carrier

Take v_s=s^(-1/2)1_(c,c+s), a physical-mass-one logarithmic carrier vector. It lies wholly in one collar, so ||1_Omega_s v_s||_2^2=1. With f=1_(0,1), scaling gives
\[
E_1(v_s)=\int\log(e+|\eta|/s)|\widehat f(\eta)|^2d\eta=L_s+O(1).
\tag{8}
\]
The upper difference is bounded by integral w |Fourier f|^2. The lower difference is bounded below by integral log|eta| |Fourier f|^2, a finite real constant: Fourier f is bounded near zero and O(1/|eta|) at infinity. Thus (8) uses only integrable logarithmic moments and mass one.

No general one-logarithm carrier bound can improve (4) to o(1/L_s) times E_1 uniformly. These indicators are not actual null vectors. Higher-p estimates for an actual residual are lawful because its entire finite-log bootstrap has been proved, not because the one-log concentration constant can be improved.

Superlogarithmic decay remains too weak for (2). For example the scalar rate e_s=s^(1/2) tends to zero faster than every fixed inverse logarithmic power, while e_s/s^2=s^(-3/2) diverges. This is a rate control, not an actual residual or null construction. It rejects the inference from (3) to quadratic gain or H1.

## Concrete actual arithmetic target

For x>0 sufficiently small, the exact right exterior residual is
\[
q_h(c+x)=-\int_{-c}^c
\frac{e^{-(c+x-y)/2}}{1-e^{-2(c+x-y)}}h(y)dy
-\sum_{\log n\le2c}\frac{\Lambda(n)}{\sqrt n}h(c+x-\log n)
+M_-(h)e^{(c+x)/2}+M_+(h)e^{-(c+x)/2}.
\tag{9}
\]
The second prime shift is outside the support and is zero. The left collar has the symmetric archimedean distance kernel, the opposite prime shift h(-c-x+log n), and the same physical pole formula evaluated at -c-x. Equality-threshold terms remain. Both expressions are L2 collar identities, not endpoint traces.

The smallest sufficient endpoint theorem isolated here is: for every h in a hypothetical actual nonnegative kernel, the **combined** residual (9) and its left counterpart have
\[
\int_0^s(|q_h(c+x)|^2+|q_h(-c-x)|^2)dx
\le C_h s^2\log(1/s)
\quad(0<s<s_h).
\tag{10}
\]
This theorem is unproved. It would put the entire finite kernel in global H1 by (2), and automatic derivative invariance would exclude it. An estimate for only one averaged inverse moment does not establish (10), nor does a bound on only the archimedean summand while discarding the prescribed primes and signed pole.

The failed implication is now explicit: every finite logarithmic collar estimate (3) -> the polynomial-scale cancellation (10). It belongs to **endpoint exclusion**. No retained packet is attached by that implication and no enlarged full mixed-null equation is obtained. The unchanged h is used throughout; neither dilation nor a changed inverse-residual trial is used.

## Validation and custody

Pinned source blobs and repeat rational controls: notes/data/RPB108_COLLAR_GAIN_20261006.json. Controls audit the e-series ceiling used for 10, finite-p integer concentration budgets and the compatible rough/superlog scalar rate. They do not certify the Fourier/domain proof or (10), and compute no actual arithmetic null mode. No Lean/compiler/workflow changes or new axiom/CI claim. Historical wording preserved; whole-domain aperture remains 23/25, independent 93/100 corrected sign pending. F4 and FULL TRANSPORT CLOSED remain open.
