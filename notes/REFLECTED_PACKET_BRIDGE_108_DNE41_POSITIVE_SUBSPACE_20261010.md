# RPB108 — DNE41 preserves the old spans and certifies maximal positive comparison subspaces

Parent: DNE40, `4cc32239ede79980bceac75226add04e167c659e`, on `research/rpb108-direct-null-exclusion`.
Terminology: `docs/TERMINOLOGY_RPB108_DNE41_POSITIVE_SUBSPACE.md`, registered before certification.

DNE41 uses the existing complete 36-column source packet in each parity and the unchanged original infinite F112 floor 289/500. It certifies 34 positive retained directions even and 35 odd, containing both DNE40 positive spans and the whole infinite high space. Original retained positivity advances 62 -> 69 directions. The other 43 retained dimensions and whole a=53/50 positivity remain open. No source integration is repeated.

## Exact embedding and containment

Let H=(289/500)N36-G36 be DNE40's sufficient original-source uniform-floor comparison. Its positive coordinate prefix has dimension n=29 even and n=33 odd. Write H in blocks A,B0,C relative to that prefix. Midpoint linear solves propose a rational approximation J to A^{-1}B0 at grid 1e-40. A numerical eigensystem of C-B0*J proposes rational vectors at grid 1e-20.

The extension map is R=(-J;I). The positive embedding is B=(E_n,R W_positive), where E_n consists of the unchanged first n coordinate columns. The negative comparison embedding is D=R W_negative. All products defining these embeddings are exact rational products. No mixed entry is discarded and no approximate orthogonality is assumed.

Rational congruences certify B*H B positive and -D*H D positive by outward interval evaluation and strictly positive Gershgorin margins. Floating-point solves and eigenvalues choose candidates only. The first n columns of B equal E_n exactly, proving containment of DNE40's positive span. Every original native/source correlation and all inherited physical payments remain in the compressed matrices.

## Dimension and maximality

| Quantity | Even | Odd |
|---|---:|---:|
| Original joint packet dimension | 36 | 36 |
| Preserved DNE40 positive prefix | 29 | 33 |
| New positive extension directions | 5 | 2 |
| Certified positive retained rank | 34 | 35 |
| Certified negative comparison rank | 2 | 1 |
| Certified uniform-comparison inertia (+,-,0) | (34,2,0) | (35,1,0) |

The independent verifier checks exact full rank of (B,D), the original packet's complete retained-coordinate rank 36, and every prefix identity column. Therefore the new retained ranks are actual ranks, not counts of approximate eigenvectors.

The positive and negative comparison dimensions total 36 in each parity. Sylvester inertia bounds therefore certify maximality of the positive dimension for this fixed H. No basis change alone can make the same full 36-column uniform comparison positive. This says nothing negative about the true original Schur matrix: its inverse response may be strictly smaller than G36/(289/500). The negative certificates are comparison controls, not original Weil negative vectors or null vectors.

## Original physical guard

Exact physical columns are reconstructed as rational combinations of the unchanged original packet and their exact masses are recomputed in the orthonormal physical Legendre basis, including the high polynomial components. Native normalization is never treated as physical normalization.

For the positive compressed comparison, a rational congruence U with U*B*H B U >= m I gives d=m/||U||_F^2. Original high square completion yields Schur coefficient floor d/kappa, kappa=289/500. With M the sum of exact physical column masses and T the outward upper trace of B*G36 B, the physical gap is at least min{(d/kappa)/(4(M+T/kappa^2)),kappa/2}.

The even physical gap is approximately 2.931837502e-39 and the odd gap approximately 6.939708182e-34. The common enlarged-span physical guard is 1e-39. DNE39 and DNE40 guards retain their scopes on their earlier smaller spans. The new positive span contains all 62 previously certified retained directions plus the entire infinite F112 space.

## Audit and next obligation

The independent audit passes **9,871 new exact rational checks**. It authenticates the DNE40 source/comparison inputs and its passing source validation by hash, checks all compressed interval matrices and rational congruences, proves positive and negative ranks and exact containment, reconstructs physical coefficients and masses, and verifies the paid physical gap. Source-integral and high-floor audits are reused rather than rerun. Actual inverse evaluation, whole-aperture positivity, RH and Lean remain open.

The next comparison obligation is concentrated on three directions within the computed packet: two even and one odd. Closing those directions requires additional original information, such as a stronger high bound or a paid directional response estimate. Forty retained dimensions lie outside the computed packet; together these account for the remaining 43 uncovered dimensions. This decomposition does not assert that any remaining original direction is negative. Further source integration can extend the packet, but cannot fix its existing uniform-comparison negative inertia by itself.

## Reproduction

Run `certify_dne41_positive_subspace.py PARITY --output CERTIFICATE.json` in each parity with the authenticated DNE40 inputs at their recorded paths. Then run `validate_dne41_positive_subspace.py EVEN_CERTIFICATE ODD_CERTIFICATE --output VALIDATION.json`. Require PASS before publication. Both scripts pass syntax compilation. The producer and verifier use an explicitly ordered exact rational interval calculation for the source trace; the final audit verifies its outward bound and physical payment.
