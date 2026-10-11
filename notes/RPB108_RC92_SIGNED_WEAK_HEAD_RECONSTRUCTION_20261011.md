# RPB108 RC92 — Signed weak-head reconstruction

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC91, commit `79c6f6081aba812c5169335cc4e9664ff32937b2`.

RC92 certifies positivity of the original Weil form on both fixed two-dimensional RC63 weak spans. This is a signed result on actual native Riesz vectors, including the two within-parity cross entries. It resolves the signs that RC63 and RC91 left open, without evaluating the complete 1,250-feature head or performing new integrations.

The existing RC91 projected coupling upper remains too large to certify either corrected weak Schur block. Failure of this sufficient enclosure does not establish a negative actual Schur block or a lower bound on actual coupling. Full head positivity, weak-mode coverage, strong-block control and weak/strong cross-block control remain open.

## Matching the 64-mode trial, source and error certificates

Let R denote the actual native Riesz vectors, V the fixed RC67 physical 64-mode polynomial trials and E=R−V. The canonical metric operator L satisfies LR=q. The original Weil form is Q(u,v)=<Lu,v>+<Ku,v>, with the complete bounded physical remainder K, including archimedean, prime and signed pole terms.

RC68 already encloses H_ij=<V_i,q_j+K_nom V_j>. With J_ij=<q_i,V_j> and the RC67 nominal trial metric G_T, the symmetric trial Weil center is

    Q_T,nom = sym(G_T + H − J^T).

The directed RC68 source-pairing radii pay every rounding and integration error. The actual trial metric and K approximation allowances add (δ_G+δ_K)||V_i||||V_j||. The signed pole, all exact prime translations and the archimedean remainder are already inside H. No unsigned reconstruction of these source contributions is made here.

Crucially, the trials and source pairings are both 64-dimensional. RC92 does not attach RC81's 64-mode Riesz-error estimates to RC61's different 32-mode trial head.

## Original-source cancellation

For real vectors the exact bilinear identity is

    Q(R_i,R_j) = Q(V_i,V_j)
                 + <q_i+KV_i,E_j> + <E_i,q_j+KV_j>
                 + <KE_i,E_j> − <LE_i,E_j>.

This follows from LE=q−LV. The negative canonical error term is retained. On a diagonal it lies in [−E_c,ii,0]; on a cross entry its magnitude is at most sqrt(E_c,ii E_c,jj). The physical quadratic error is bounded by k_parity sqrt(E_p,ii E_p,jj).

For each weak vector, RC68's complete nominal source Gram gives U_ii and its physical trial Gram gives T_ii. Hence the actual trial-source norm is at most sqrt(U_ii)+δ_K sqrt(T_ii). The two linear terms are bounded separately using the matching RC81 physical Riesz-error Gram. All square roots are rounded upward on a rational 10^40 grid. All final signed endpoints are rounded outward on that grid.

These bounds give exactly three independent signed entries for each parity, six total. Opposite parity entries vanish by the inherited symmetry. The validator records each center and each metric/source, linear, physical quadratic and canonical error allowance.

## Results

The following are actual canonical Rayleigh enclosures for the four fixed directions. Positive lower endpoints use the actual canonical norm upper ρ times the native physical Gram; upper endpoints use the RC67 actual canonical Gram lower. They are not normalized by a single surrogate norm.

| Direction | Actual Rayleigh lower | Actual Rayleigh upper | RC63 interval-width reduction |
| --- | ---: | ---: | ---: |
| even weak_0 | 9.70286251e-18 | 2.75054728e-17 | 1.164836e+07 |
| even weak_1 | 1.65553487e-13 | 2.85110609e-13 | 2270.382 |
| odd weak_0 | 7.48151474e-16 | 1.02205044e-15 | 1175348 |
| odd weak_1 | 4.73268479e-12 | 8.06331495e-12 | 79.25216 |

Positive diagonals alone would not prove positivity of each two-mode span. RC92 constructs a full Loewner lower from the six signed entry intervals. If B is the interval midpoint, r its symmetric halfwidth matrix and d a fixed positive rational scaling, the lower is

    B − diag(sum_j r_ij d_j/d_i).

After the diagonal congruence diag(d), this is the usual symmetric row-radius bound. The fixed scales are (100,1) in the even block and (80,1) in the odd block. They balance the very different head magnitudes while paying every cross-entry uncertainty. Exact Sylvester tests show both 2×2 lower matrices are positive definite.

A separate exact rational bisection proves Q_W ≥ h_W M_W,upper, therefore Q_W ≥ h_W M_W,actual. The certified full-span canonical floors are:

- even: `4910867569/1099511627776000000000000000` (approximately 4.466408035e-18).
- odd: `362799697111/549755813888000000000000000` (approximately 6.599288047e-16).

These are floors only on the specified two-dimensional spans. They are not floors for the complete 22-, 38- or 1,250-feature head.

## What the coupling comparison settles

Subtracting the unchanged RC91 rank-1250 Schur-penalty upper from these weak-head lowers does not produce a positive lower block in either parity. All four available diagonal Schur lower bounds remain negative. The coupling is small in absolute canonical terms, but the head is also extraordinarily weak. Thus RC91's small-coupling observation alone cannot close the matrix Schur argument.

The rank-1250 penalty remains justified by actual projection nesting: the rank-38 source covariance upper bounds the rank-1250 covariance. The inherited complement floor 247/2500 is applied only to the rank-1250 complement. No rank-38 complement floor is asserted, and the two projection covariances are not identified.

RC92 proves actual weak-head positivity. It does not prove actual corrected-block negativity. To discriminate further, the next useful step is a coupling enclosure tailored to these four combinations, retaining cancellations before the global source attachment and row rounding. Computing or bounding signed source/error correlations on these small spans may reduce the conservative penalty. An actual coupling lower would also be informative, but is not supplied here.

A successful weak-block Schur result would still require a theorem identifying all potentially dangerous modes in the complete sufficient head, a positive corrected strong block and its weak/strong inverse allowance. The four RC63 vectors are not assumed exhaustive. Global first-contact exclusion remains an independent alternative.

## Reproducibility and scope

The new validator consumes RC91, RC63, RC67, RC59, RC68, RC81 and RC66 in that order. It records SHA-256 digests and checks the relevant source/trial/native/precision crosslinks. Every accepted inequality uses exact Fraction arithmetic and upward rational square roots; no floating-point eigenvalue is evidence.

Independent replay contracts every bilinear matrix by a column-first formula rather than matrix multiplication, rechecks all six signed allowances, and verifies the weighted row-radius identity after diagonal congruence. Generation and replay agree exactly. The exact positive-definiteness tests and canonical lower-floor inequalities pass.

Deliverables:

- `scripts/validate_rpb108_rc92_signed_weak_head_reconstruction.py`
- `certificates/rpb108_rc92_signed_weak_head_reconstruction.json`
- `notes/RPB108_RC92_SIGNED_WEAK_HEAD_RECONSTRUCTION_20261011.md`

No Lean files or other research fronts are changed. No complete-head positivity, RH or Global/F4 claim is made.
