# RPB108 — NF25: original directional source Gram and correlated response bounds

Date: 2026-10-09. Aperture a=53/50. Independent Phase Geometry continues
NF24 at `b7fa4461ab4cca2ebc9383ae4b9407c03a580826`.
Coupled CC64 was read at `0d3def3c12acdb97d027cc75b1a400919b202f74`;
no Coupled or paused branch is modified.

NF25 rigorously encloses the **complete original physical directional
three-source Gram** for each of NF24's two frozen rational compensated
polynomials. Every arch, prime and signed-pole cross term is included.
It then rigorously rejects both the coarse sufficient response test and
the optimal two-mode correlated sufficient test for those fixed targets.
This is a failure of these upper estimators to prove positivity, not a
negative Weil vector or a lower bound on the actual inverse response.

Terminology is defined additively in
[the NF25 registry](../docs/TERMINOLOGY_RPB108_DIRECTIONAL_SOURCE_CORRELATION_NF25.md).
Historical definitions are unchanged.

## 1. The certified original object

In each parity let E be the original retained E112 space, F its physical
orthogonal complement, p the authenticated NF24 target, and phi1,phi2
its original two measured high modes. Define

\[
r=P_F L_a p,\qquad G_j=P_F L_a\phi_j,
\qquad \operatorname{Gram}(r,G_1,G_2)=
\begin{pmatrix}P&z^*\\z&D\end{pmatrix}.
\]

Here P=||r||_2^2, z_j=<G_j,r>, and D_jk=<G_j,G_k>.
The high modes are e112,e114 even and e113,e115 odd. The retained
space has 56 modes in each parity. The original finite energy q=Q(p,p)
is positive and is carried unchanged from NF24. This is one complete
three-source Gram per fixed direction; it is not the full 58-source Gram
or the collective retained residual matrix.

The following are **strict rationally certified brackets**, including all
physical approximation errors. The correlation credit means
zbar* V^-1 zbar, defined below.

| Quantity divided by q | Even | Odd |
| --- | ---: | ---: |
| Original residual source square P/q | (0.3499, 0.3502) | (0.28027, 0.28030) |
| Correlation credit / q | (0.00152, 0.00155) | (0.000185, 0.000188) |
| Optimal two-mode response majorant / q | **(1.683, 1.685)** | **(1.3530, 1.3532)** |

The coarse majorant P/(kappa q) is approximately 1.691 even and 1.354
odd; its exact rational intervals also lie strictly above one.
The independent NF24 numerical residual-square diagnostics lie inside
the new certified residual-square brackets. Numerical quadrature is not
used as a proof input.

## 2. Exact endpoint and cell moment construction

The archimedean source of every polynomial is reconstructed as

\[
L_{arch}p(x)=c p(x)-\tfrac12 p(x)\log(a^2-x^2)
 +S_p(x)-\int_{-a}^a r(|x-y|)p(y)\,dy,
\qquad c=-\gamma-\log(2\pi).
\]

S_p is the exact removable-singularity polynomial. For a monomial,

\[
S_{x^m}=H_m x^m-
\sum_{\substack{1\le j<m\\j\text{ odd}}}
\frac{a^{j+1}}{j+1}x^{m-1-j}.
\]

NF22's rational N=320 construction replaces only the regular kernel.
Endpoint Taylor coefficients of p and exact beta integrals produce its
polynomial convolution. The endpoint logarithm remains explicit.

The six prime powers 2,3,4,5,7,8 contribute their original twelve oriented
translations. Rational outward log and square-root enclosures order all
thirteen original cells and certify active translation membership. Prime
sources are polynomials on each cell. The original signed-pole source
uses independently bounded Rodrigues first moments and degree-40
cosh/sinh expansions.

Each reconstructed source consists of a global polynomial, a polynomial
times log(a^2-x^2), and a cellwise prime polynomial. Products are integrated
using exact polynomial moments, exact global log and log-square moments,
and exact cell endpoint-log antiderivatives. At x=+/-a their removable
log coefficients vanish algebraically; their continuous limits are used.
There is no sampling estimate for an endpoint singularity.

All arithmetic is outward on the rational grid 10^-280. Normalized
Legendre square roots are enclosed using integer square roots. Constants
use rational atanh logarithms with paid series tails, Machin pi, and the
harmonic Euler-gamma formula with 100 Bernoulli corrections through B200
and the next B202 remainder. The stable cell-log primitive uses an exact
polynomial recurrence to avoid a repeated cubic-time summation.

Retained source coordinates are subtracted at fixed rational interval
midpoints. Their small projection errors are paid in physical norm after
integration, rather than amplified by coefficient dependence in a giant
polynomial expression.

## 3. Paid physical errors

The authenticated p has norm below 1001/1000; each phi_j has norm one.
Let m_i be these norm bounds. NF22 gives

\[
\eta_{arch}=2a\epsilon,\qquad
\epsilon=\frac{4(106/125)^{320}}{1-106/125}.
\]

The regular-kernel replacement error is at most eta_arch ||p||_2,
without a polynomial-degree factor. Let
R40=2(a/2)^41/41!. Cauchy-Schwarz and the bounded pole moments give the
conservative pole-source error 8 m_i R40. The Rodrigues moment tail and
all rounding errors are already enclosed in the moment Gram.

With delta_i bounding the midpoint retained-projection error, use

\[
\eta_i=m_i(\eta_{arch}+8R40)+\delta_i.
\]

If hats denote the reconstructed sources, every true Gram entry is
within

\[
\eta_i\|\widehat f_j\|_2+
\eta_j\|\widehat f_i\|_2+\eta_i\eta_j
\]

of its reconstructed entry. Rational square-root upper bounds on the
reconstructed diagonal entries make this ledger fully explicit. The
machine certificate records every eta and all nine entrywise payments.

## 4. Original correlated response test

Use the unchanged original native two-mode form C2 and the measured
coordinates u_j=Q(p,phi_j). The latter are retained explicitly even though
the compensation makes them tiny. With kappa=207/1000, set

\[
V=D-\kappa C_2,\qquad \bar z=z-\kappa u.
\]

The certificate verifies V positive definite, the measured high-tail
Gram H=D-C2^2 positive definite, and the joint three-source Gram positive
definite. CC64's original high-floor argument yields

\[
T\le U_{corr}=
\frac{P-\bar z^*V^{-1}\bar z}{\kappa}
\le \frac P\kappa,
\]

where T is the actual full original high inverse response. Correlation
credit is strictly positive, and the correlated enclosure is strictly
smaller than the coarse one. Nevertheless Ucorr/q>1 in both parities.
Thus neither sufficient inequality Ucorr<q closes these directions.
This does **not** imply T>=q, a negative direction, or failure of the
original whole-domain form.

As an independent evaluation, the validator freezes rational Y with
denominator 10^80 near V^-1 zbar, pays the combined physical source
error, and computes

\[
2u^*Y-Y^*C_2Y+
\frac{\|r-GY\|_2^2}{\kappa}.
\]

CC64's optimality/sharpness refers to completions compatible with its
measured two-mode data and high floor. It explains why changing Y within
this estimator cannot repair the certified deficit. It does not assert
nonimplication from all additional original Weil identities.

## 5. Validation and reproducibility

The strengthened full replay passes twelve independent unsquared native
pairings: each of the three reconstructed sources against each of its
two original high modes in both parities. After paid errors they overlap
the independently produced original native intervals for u and C2.
The replay reproduces all first-run Gram intervals exactly.

Additional construction checks compare the generic convolution against
both independent NF22 polynomial sources, the cell-log primitives against
independent full log moments through degree 12, and fixed-grid log
intervals against independent Fraction atanh enclosures. The certificate
checks positive determinants, strict estimator rejection, strict positive
correlation credit and every displayed decimal bracket.

Artifacts:

- [Rational physical moment producer](../scripts/certify_native_correlated_sources_nf25_106.py).
- [Paid original response validator](../scripts/validate_native_correlated_response_nf25_106.py).
- [Reconstructed rational moment Gram and twelve native checks](data/RPB108_NF25_DIRECTIONAL_SOURCE_MOMENTS_20261009.json).
- [Complete original Gram, error ledger and response certificate](data/RPB108_NF25_DIRECTIONAL_SOURCE_CORRELATION_CERTIFICATE_20261009.json).
- [Unchanged NF24 target ledger](data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json).

The three unchanged native archives are native112_N720_K620.json.gz,
native_boundary_columns_112_113.json.gz, and native_boundary_114_115.json.gz.
Both programs authenticate their decompressed SHA-256 digests and the
exact target bytes before use. Existing NF17 and NF22 dependency scripts
remain unchanged. With these archives in INPUT_DIR, replay:

```bash
python scripts/certify_native_correlated_sources_nf25_106.py \
  notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json \
  INPUT_DIR/native112_N720_K620.json.gz \
  INPUT_DIR/native_boundary_columns_112_113.json.gz \
  INPUT_DIR/native_boundary_114_115.json.gz --output moments.json
python scripts/validate_native_correlated_response_nf25_106.py \
  notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json moments.json \
  INPUT_DIR/native112_N720_K620.json.gz \
  INPUT_DIR/native_boundary_columns_112_113.json.gz \
  INPUT_DIR/native_boundary_114_115.json.gz --output certificate.json
```

## 6. NF26 frontier and claim boundary

The missing quantity is no longer the directional complete-source Gram.
The two measured sources and a global 0.207 floor give insufficient
correlation credit for these fixed near-critical directions. NF26 should
obtain additional original high-form information: more measured high
response or a justified stronger bound on the source-relevant high
subspace, with every omitted contribution controlled.

A full collective residual Gram, actual inverse-response control and
whole-domain Schur sign at 1.06 remain open. The highest internally
certified whole-domain aperture remains 1.05. RH, F4 and Lean closure are
not claimed. Coupled's investigation and both paused branches remain
untouched.
