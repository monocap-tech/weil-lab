# RPB108 RC84 — direct complete nominal response residual

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `4e68e48d27e8c9a6e3a0982e1dc8300351da3b05` (RC83).

## Result

RC84 evaluates the complete physical covariance of
`r_nom = F_nom - L_nom Z`, where `F_nom = q + K_nom V64` is the unchanged
RC68 nominal source and `Z` is the unchanged RC83 64-mode canonical trial
response. All signed base, prime, pole and mixed correlations are retained.
It then pays the canonical-operator approximation uncertainty and transports
the residual through the actual canonical adjoint.

The resulting canonical response-error upper matrix improves RC83's
upper matrix in whole Loewner order. Across the 22 input columns,
the squared-error diagonal upper bounds improve by factors
6.770483–265.559012.
These compare upper bounds; they do not measure actual error reductions.

Generation and independent replay: **PASS**.

This remains a result for the nominal source in the actual canonical metric.
The actual original source uncertainty has not been attached to this new
response, and its rank-38 complementary projection has not been evaluated.
RC82's actual rank-38 source factor `2061/4096 = 0.503173828125` remains the
retained bound. The scalar source budget remains open.

## Source and response interface

| Object | Size | Status |
|---|---:|---|
| Native source inputs | 22 | Original inputs 0–21 |
| Original source Riesz trials `V64` | 64 × 22 | Unchanged from RC67 |
| Canonical response `Z` | 64 × 22 | Unchanged from RC83 |
| Actual Riesz projection head | Rank 38 | Unchanged from RC70 |

`L_actual` denotes the canonical strong physical source operator on the
polynomial trial vectors, characterized by
`i* L_actual Z = Z`. `L_nom` is its recentered order-192 approximation from
RC81. It is distinct from `K_nom`, the signed Weil remainder operator in
the original source.

The RC68 source builder returns `q_native + K_arch,nom V64`, before prime
and pole additions. The RC81 operator builder applied to `Z` returns
`P_j - L_nom Z_j`, with an auxiliary physical Legendre target `P_j`.
RC84 adds those expressions and removes `P_j`. This preserves the native
source target and yields the base residual

`q_native + K_arch,nom V64 - L_nom Z`.

No congruence of `Z` or replacement of the original source trials is made.
The existing prime source and signed pole source are then added unchanged.

## Direct covariance construction

Write the residual as `b + p + o`, where `b` is the base residual just
constructed, `p` is the paired prime source, and `o` is the signed pole
source. RC84 computes

`Gram(b) + Gram(p) + Gram(o) + [b,p] + [b,o] + [p,o]`,

where each bracket denotes the symmetrized physical cross Gram.

The 132 same-parity upper-triangular base Gram entries and the 132
symmetrized base–prime entries are regenerated. Prime interactions use
all fourteen signed translations over fifteen support segments. The 22
base exponential moments are regenerated for the signed pole interaction.
The unchanged prime Gram, pole Gram, trial exponential moments and prime
exponential moments are reused from the hash-attached RC68 certificate.
The base–pole and prime–pole interactions are combined with their original
parity sign before enclosing the complete residual entries. The 121
mixed-parity upper-triangular entries are exactly zero.

Every component and complete covariance entry is enclosed outward at
`10^-20`. Midpoints form a symmetric matrix. Its row-sum interval-radius
diagonal is added to obtain the physical residual upper matrix `U_res`.
Exact rational positive-semidefinite checks verify `U_res`. The certificate
records every entry enclosure and row allowance; cancellations retain their
signs rather than being replaced by independent operator norms.

## Actual canonical-operator transport

For the polynomial response, RC81 supplies

`||(L_actual - L_nom) Z a||_phys <= delta_L ||Z a||_phys`,

with

`delta_L = 2 radius(c56) + (4/3) (192+64) 42^193 / 193!`.

The nominal source itself stays fixed in this step. Let `T_Z = Z' D64 Z`
be the exact rational physical response Gram and `t = 1/65536`. Then

`Gram_phys(F_nom - L_actual Z)`
`<= (1+t) U_res + (1+1/t) delta_L^2 T_Z`.

The right-hand side is rounded upward in Loewner order at `10^-24`, with
every rounding row allowance recorded. Independent replay reconstructs
`T_Z` entry by entry rather than using the matrix-product route.

Using the polynomial operator-domain identity,

`i* F_nom - Z = i* (F_nom - L_actual Z)`.

Since `||i*||^2 <= rho = 252/257`, the published canonical response-error
upper matrix is `E_direct = rho B_actual`, where `B_actual` is the paid
physical residual matrix. Exact rational checks certify both
`E_direct >= 0` and `E_RC83 - E_direct >= 0`.

This construction replaces RC83's generic variational source-norm
subtraction by direct physical covariance of a residual. Its final
adjoint transport still uses the global embedding bound `rho`.

## Whole-input error bounds

The table compares the indicated canonical error upper matrices to the
RC67 original 22-input canonical Gram lower matrix. Each displayed factor
passes an exact rational parity-block Loewner check.

| Parity | RC83 response-error factor | RC84 direct response-error factor |
|---|---:|---:|
| even | 2383/1024 = 2.3271484375 | 909/2048 = 0.4438476562 |
| odd | 5495/2048 = 2.6831054688 | 821/2048 = 0.4008789062 |

These are unprojected nominal-source response-error upper bounds. They are
not rank-38 projected-source factors and do not certify a scalar Schur
budget, a positivity extension, or an actual failure.

## Independent replay and provenance

Generation evaluates the full nine-term base covariance using separate
left and right logarithmic moments. Replay uses the six-term reflection
reduction for same-parity residuals. Mixed base–prime replay similarly
uses reflected logarithmic moments. Pole-moment replay uses an independent
reflected exponential formula and a polynomial coefficient tail bound;
generation uses the Gram-controlled tail bound. Both moment paths include
explicit exponential truncation errors.

Replay checks every regenerated value inside its saved rational enclosure,
reconstructs physical response transport independently, repeats all exact
positive-semidefinite and relative-Gram checks, and requires equality with
the saved JSON certificate. All seven direct dependency SHA-256 hashes
are recorded. The RC83 and RC68 links to the source, response, native
conversion, precision, prime and archimedean certificates are checked.

Repository replay command:

```bash
python scripts/validate_rpb108_rc84_direct_nominal_response_residual.py --replay certificates/rpb108_rc84_direct_nominal_response_residual.json
```

## Remaining attachment

The next interface is the explicit response together with `E_direct`.
To bound the actual original source after the rank-38 complementary
projection, one must still bound the complementary component of `Z` and
attach the difference between the actual source and `F_nom`. Those are
separate from the canonical strong-operator correction paid here.

No new actual rank-38 projected-source bound, original-source attachment,
enlarged source covariance, scalar source-budget closure, actual rank-38
failure proof, Weil floor, complement floor, whole-aperture positivity,
RH, F4 or Lean result is asserted.
