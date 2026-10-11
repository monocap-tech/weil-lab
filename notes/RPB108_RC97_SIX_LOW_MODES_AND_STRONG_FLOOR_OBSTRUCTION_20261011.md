# RPB108 RC97 — Six low modes and a strong-floor obstruction

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC96, commit `325c6728d369f4c2de5cb5cfda53004ece09e6d4`.
Aperture B=1.10. All head projections and metrics are the actual canonical ones.

RC97 proves that removing the four known weak vectors does not leave a strong complement with the old low-eight floor 1/2900000. There is an additional low strong direction in each parity. The proof uses three-dimensional signed Rayleigh bounds and a dimension argument; it neither approximates canonical orthogonality nor evaluates a dense enlarged head.

The original Weil operator has at least six eigenvalues, counted with multiplicity, at or below 2.508112034e-7. This is a low-spectrum statement, not an assertion that any of these eigenvalues is zero or negative. The four known corrected modes remain certified positive from RC94/95. Complete weak coverage, a positive corrected strong floor, and the weak/strong cross allowance remain open.

## Exact results

For each parity use the three fixed RC63 native combinations, ordered weak_0, weak_1, positive_control. Their actual Riesz vectors lie in the complete rank-1250 head. RC97 constructs an original Weil bilinear upper Q_upper and an actual canonical Gram lower M_lower. Exact rational arithmetic proves M_lower>0 and

    Q_actual <= Q_upper <= eta M_lower <= eta M_actual.

Thus every vector in this actual three-dimensional subspace has canonical Rayleigh value at most eta.

| Quantity | Even | Odd |
| --- | ---: | ---: |
| Certified eta | 1637343470131/1099511627776000000000 | 2154451831659/8589934592000000000 |
| Decimal display | 1.4891552111e-9 | 2.5081120334e-7 |
| Test-subspace dimension | 3 | 3 |
| Known weak dimension | 2 | 2 |
| Dimension remaining in the canonical strong complement, at least | 1 | 1 |

Both eta values are strictly smaller than 1/2900000, approximately 3.4482758621e-7. The even ceiling is therefore also an upper limit on any uniform corrected strong floor after removing only the four known weak vectors.

The tables are explanatory. Determinants, pivots, interval domination and generalized Rayleigh bounds are checked using Fraction arithmetic. No floating eigenvalue is evidence for acceptance.

## 1. Reconstruct the matching signed trial head

RC67 supplies the 64-mode native Riesz trials V, the nominal canonical metric G, the physical mass matrix D, and the mass-relative canonical metric error delta_G. RC68 supplies the complete nominal source pairings

    H_ij = <V_i, q_j + K_nom V_j>_physical.

Let X denote the physical mass-weighted polynomial inputs and J=X*V. The signed original trial head center is

    Q_trial,nom = sym(V* G V + H − J*).

Subtracting J* retains the original source cancellation. RC97 applies the fixed three-vector contractions before attaching scalar direction errors. It uses matching RC67 trials throughout; no 32-mode trial head is combined with a 64-mode residual.

The center and pairing halfwidths are symmetrized with their paid error bounds. For contracted trial Gram T, nominal source Gram U, physical Riesz-error upper Ep, and canonical Riesz-error upper Ec, set

    s_i = sqrt(U_ii) + delta_K sqrt(T_ii).

The actual entry allowance consists of:

- the contracted source-pairing interval radius;
- (delta_K+delta_G) sqrt(T_ii T_jj);
- sqrt(Ep_ii) s_j + sqrt(Ep_jj) s_i;
- kappa_parity sqrt(Ep_ii Ep_jj);
- sqrt(Ec_ii Ec_jj) for off-diagonal canonical error.

The canonical diagonal error has the original cancellation sign: -Ec_ii <= correction <= 0. It is subtracted in the diagonal lower and does not enlarge the diagonal upper. All square roots are rational outward ceilings. Final entries are rounded outward on a 1e-40 grid.

This is the same signed attachment identity used in RC92, now on three vectors per parity. The broad RC81 error uppers suffice for the low-subspace upper theorem. RC93's later targeted weak-error sharpening is unnecessary here. No new source integration is performed.

## 2. From signed entry bounds to an entire-subspace upper

Let midpoint and radius be the contracted symmetric entry enclosure. Choose exact interval-balancing scales (100,1,1) for even and (80,1,1) for odd, and add to each midpoint diagonal

    row_i = sum_j radius_ij scale_j/scale_i.

Weighted symmetric diagonal dominance proves that the resulting Q_upper dominates every matrix in the signed entry enclosure. This is a Loewner upper, so it controls all linear combinations, not only the three displayed vectors.

Contract RC67's actual native canonical Gram lower onto the same three inputs. Exact positive pivots establish that the three actual vectors are independent. A 40-step rational upper bisection, after scaling Q_upper by 1e9, certifies eta M_lower−Q_upper is positive semidefinite. The last exact PSD test is the certificate; bisection merely finds a usable rational value.

The positive-control label is inherited from RC63's individual direction sign checks. It does not mean the entire three-dimensional corrected block is positive. RC97 certifies an upper on that space and does not evaluate its coupling covariance.

## 3. Canonical strong directions exist by dimension

Let W_p be the two known weak vectors in parity p, and U_p the three-dimensional test span. They satisfy W_p subset U_p subset H_p. Define S_p=H_p intersect W_p-perp in the actual canonical metric.

The linear map from U_p to W_p*, sending u to its two canonical pairings with W_p, has rank at most two. Its kernel is U_p intersect S_p and therefore has dimension at least one. Any nonzero vector in this kernel inherits the entire-subspace Rayleigh upper eta_p.

This proves the existence of an actual canonical strong direction with original Weil Rayleigh at most eta_p. It does not require an approximate metric inverse or the numerical construction of that direction. Coefficient-space Euclidean orthogonality is never substituted for canonical orthogonality.

For the complete corrected head T=A−Gamma/alpha, Gamma is positive semidefinite. Hence T<=A, and the same strong direction has corrected Rayleigh at most eta_p. If a proposed theorem claims

    T_SS >= beta I_canonical,

then beta<=eta_p for each parity. In particular any common beta is at most 1.4891552111e-9. A strong floor of 1/2900000 on this four-mode complement is rigorously ruled out.

This is a true upper bound for the original and corrected strong Rayleigh values, not merely failure of a convenient source upper estimate. It says nothing about their sign: beta could be smaller and positive, or no positive strong floor may exist. That remains to be determined.

## 4. Six low eigenvalues, not six dangerous eigenvalues

Parity makes U_even and U_odd orthogonal and eliminates mixed Weil entries. Their direct sum U has dimension six. Every nonzero vector in U has Rayleigh at most

    eta_max = eta_odd = 2154451831659/8589934592000000000 < 1.

RC77 establishes compactness of the canonical embedding i. Since the physical original remainder K is bounded and self-adjoint, A_Q=I+i* K i has compact self-adjoint remainder and essential spectrum at 1. The min-max principle then gives at least six eigenvalues of A_Q at or below eta_max, counted with multiplicity. More directly, if its spectral projection on (-infinity,eta_max] had dimension below six, U would contain a nonzero vector orthogonal to that projection. Its spectral measure would be supported strictly above eta_max, contradicting the Rayleigh bound. Compactness makes this projection finite dimensional.

There are at least three such low eigenvalues within each parity at its own eta_p ceiling. The trial vectors themselves are not claimed to be eigenvectors, and RC97 does not identify the corresponding spectral subspaces.

The old eight-feature floor remains valid on its original subspace. RC97 does not contradict it: the new six-dimensional test span is a different subspace with higher-degree native content.

## 5. Consequence for the strategy

The known weak span was selected to contain four exceptionally small directions, not every direction below the old floor. RC97 now supplies a rigorous reason to distinguish those goals. A coverage theorem using the old low-eight floor as its strong threshold must enlarge the isolated subspace by at least one additional independent direction in each parity. Alternatively it may retain four weak vectors and prove a substantially smaller strong floor, paying the correspondingly tighter RC96 cross budget.

Neither option requires dense evaluation of every original head entry. The next useful test is the corrected three-mode block: determine whether the existing positive controls and their combinations remain positive after actual coupling is paid. If so, their isolation could improve a later strong-floor theorem. If not, the result would guide a better decomposition or the first-contact route. Six modes are not presumed sufficient; further low modes may exist.

The six-dimensional span's uncorrected upper theorem alone does not certify it as a replacement weak block for Schur completion. In particular RC94/95 source-tail bounds cover the original four inputs, not these two extra directions. A new source certificate is needed before extending the corrected weak positivity claim.

## Verification and deliverables

Inputs in order: RC96, RC63, RC67, RC59, RC68, RC81, RC66 and RC77. SHA-256 digests, matching trial/source/residual crosslinks, trial dimensions, fixed roles, parity support and the inherited compactness flag are checked.

Generation uses exact matrix contractions. Independent algebra replay uses column-first bilinear contractions and the weighted diagonal congruence check, then rechecks all signed allowances, actual metric independence and both generalized ceilings. It must reproduce the JSON exactly. This is an algebra replay of inherited source enclosures, not a fresh replay of their integrations or a Lean formalization.

- `scripts/validate_rpb108_rc97_additional_low_mode_coverage.py`
- `certificates/rpb108_rc97_additional_low_mode_coverage.json`
- `notes/RPB108_RC97_SIX_LOW_MODES_AND_STRONG_FLOOR_OBSTRUCTION_20261011.md`

No other branch or research front is modified. Full positivity, RH and Global/F4 remain open.
