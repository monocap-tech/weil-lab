# RPB108 — NF37: arbitrary correction functionals along the NF36 high polynomials

2026-10-09 UTC. Phase Geometry parent is NF36,
`2265e4ede44e3e993fbd2eef4f6d86a7aa2ee9cd`. Coupled CC79 was read only
at `dd93e5cc7d003d44cdc240c5710f4c253dc1346f`. Only the Phase Geometry
branch receives this additive checkpoint. Definitions precede use in the
[NF37 terminology entry](../docs/TERMINOLOGY_RPB108_FREE_CORRECTION_FUNCTIONAL_NF37.md).

## Result

NF37 extends NF36's scalar-strength obstruction to **every real
three-coordinate correction functional using the same fixed high
polynomial** in each parity. All three joined columns may change
independently along that polynomial. A single exact rational witness
in each parity has a strictly negative floor value for every such
functional. No search over the functional is needed.

| Certified quantity | Even | Odd |
| --- | --- | --- |
| Universal witness floor upper bound, all real functionals | < -1.0941e-22 | < -7.5691e-21 |
| Loewner ceiling condensed margin | (-1.13364e-22, -1.09169e-22) | (-7.58021e-21, -7.56878e-21) |
| Universal witness floor at selected rational functional | (-1.13301e-22, -1.09208e-22) | (-7.58007e-21, -7.56892e-21) |
| NF35 original mixed witness floor at that functional | (1.43210e-22, 1.56105e-22) | (2.12382e-18, 2.12388e-18) |
| Universal witness original native energy there | (4.37166e-21, 4.37194e-21) | (9.66043e-19, 9.66044e-19) |

Every displayed interval strictly encloses the exact rational endpoints.
At each selected rational functional, all three floor diagonals and the
native energy matrix are positive. The joined floor matrix still has a
negative determinant and a certified negative mixed witness. The old
NF35 witness has become positive: the obstruction has moved to a
different retained combination. Repairing that old witness alone does
not certify the complete joined restriction.

The checkpoint adds no jointly certified retained direction. The prior
four-direction restriction with all original F and the separate
two-direction restriction with all F remain valid. A floor obstruction
is not a negative original Weil form and does not exclude sharper actual
inverse-response estimates.

## Exact enlargement of the correction family

Let M=(v,t,u34) be NF35's ordered joined family and let z be the exact
NF36 high polynomial of the same parity. For any real three-vector
lambda, define

\[
M_\lambda=M-z\lambda^T.
\]

The three columns are v-lambda0 z, t-lambda1 z and u34-lambda2 z.
Since z lies in the original high space F, retained components remain
(x,w,u32). NF36's family lambda=(0,0,tau) is included. The enlargement
allows an arbitrary coordinate functional but still uses one high
polynomial. It does not allow three independent high directions or
change the direction of z.

NF36 already certified all signed native responses beta, qz and all
complete projected source responses zeta, gamma_z. Define

\[
U=Q-\Gamma/\kappa,\qquad
e=\beta-\zeta/\kappa,\qquad
d=q_z-\gamma_z/\kappa,\qquad \kappa=207/1000.
\]

Then the full updated floor matrix is

\[
U_\lambda=U-e\lambda^T-\lambda e^T+d\lambda\lambda^T.
\]

All physical source-error payments are retained in these rational
intervals. No new source approximation or quadrature is introduced.
The original N320 regular kernel, exact endpoint logarithms, degree40
pole approximation with paid tail, thirteen translation cells, and
500-digit outward polynomial/log/log-square moments are inherited from
NF36's hash-authenticated complete original source certificates.

## A ceiling for all functionals

The correction floor diagonal d has a strictly negative upper bound in
both parities. For the true quantities within their outward enclosures,
completion of squares gives

\[
V=U-\frac{ee^T}{d},\qquad
U_\lambda=V+d(\lambda-e/d)(\lambda-e/d)^T\preceq V.
\]

This is a bound for every real lambda. The rational enclosure of V has
a positive leading pair, negative condensed margin and negative
determinant in each parity. A rational witness h is selected from the
midpoint leading-pair elimination, rounded downward at denominator
10^100. Its sign is then checked against the outward ceiling matrix.
The certificate stores the exact h; approximate displays are

| Coordinate | Even | Odd |
| --- | ---: | ---: |
| h0 | -6256117.952757238 | 1284205.5756936457 |
| h1 | -16722366.60520742 | 2776604.9806897077 |
| h2 | 1 | 1 |

The midpoint selection is not a sign proof.

## Independent universal witness bound

The stronger, separately computed rejection bound uses this fixed h
directly. Let a=h^T U h, b=h^T e and x=lambda^T h. Then

\[
h^TU_\lambda h=a-2bx+dx^2.
\]

Write aU for an upper endpoint of a, bU for an upper bound on |b| and
m=-d_upper>0. For every real x,

\[
a-2bx+dx^2
\le a_U+2b_U|x|-mx^2
=a_U+\frac{b_U^2}{m}-m\left(|x|-\frac{b_U}{m}\right)^2.
\]

The exact rational constant aU+bU^2/m is strictly negative in each
parity and gives the universal bounds in the result table. This proof
does not rely on a sampled functional, a midpoint maximizer, or
independence of the uncertain source entries. It is valid for the true
correlated data enclosed by the certificates.

## Selected rational diagnostic and the moved obstruction

The coordinate midpoints of e/d select a rational lambda, rounded
downward at denominator 10^100. The native energy and complete source
Gram are updated separately, preserving every signed entry and its
error enclosure. The full matrix sign, original native positivity,
universal witness value and old NF35 witness value are all verified.
Approximate functional coordinates are

| Coordinate | Even | Odd |
| --- | ---: | ---: |
| lambda0 | -1.278756233588135e-7 | -9.194937521318763e-9 |
| lambda1 | 6.909288969947297e-9 | 2.4188029177790287e-8 |
| lambda2 | -0.17035069816162007 | -0.0028679317144652866 |

The exact real optimum would depend on the true data e/d, whereas these
are frozen rational candidates. Their diagnostic signs are separately
certified. The universal bound requires neither this selection nor
native positivity for every possible functional.

## Validation and reproduction

The independent validator passes both parity certificates. It replays
NF36's authenticated rational selection, physical source-error payments,
native pairings, source-square and covariance payments, candidate signs
and scalar-family bounds. NF37's checks reconstruct the ceiling,
compare its condensed margin with a separately ordered LDL calculation,
and verify the universal scalar envelope by an exact square identity.
They also check every selected native/source entry, the full joined
sign, positive native energies, and the opposite signs of the old and
new mixed witnesses.

Six exact free-functional controls cross positive/null/negative at two
scales. Both the original and ceiling diagonals stay positive; the
optimal functional realizes the ceiling exactly. The null control has
an exact kernel. Completion-square identities and fixed-witness
quadratics are checked at rational functionals, and the universal upper
bound is checked algebraically. Three full-physical-mass shifts retain
their exact positive ground levels. These are matrix controls, not
actual Weil counterexamples.

With the inherited repository inputs staged, run:

```sh
python3 scripts/certify_native_free_correction_functional_nf37_106.py --parity even --output notes/data/RPB108_NF37_EVEN_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json
python3 scripts/certify_native_free_correction_functional_nf37_106.py --parity odd --output notes/data/RPB108_NF37_ODD_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json
python3 scripts/validate_native_free_correction_functional_nf37_106.py --output notes/data/RPB108_NF37_FREE_CORRECTION_FUNCTIONAL_VALIDATION_20261009.json
```

## Next frontier and preserved boundary

NF38 must introduce a different high polynomial, independent high
directions, or a sharper inverse-response estimate. Changing the scalar
strength or the three-coordinate functional of either NF36 polynomial
cannot pass this scalar-floor criterion. The new universal witnesses
identify the remaining combinations that any broader correction must
address; fixing only NF35's old witness is insufficient.

The full remaining shared source Gram, its collective mixed covariance,
the full retained infinite-high sign, and whole-domain positivity at
53/50=1.06 remain open. Highest internally certified whole-domain
aperture remains 21/20=1.05. RH, F4, full transport and Lean closure are
unclaimed. Historical wording and paused branches remain unchanged.
