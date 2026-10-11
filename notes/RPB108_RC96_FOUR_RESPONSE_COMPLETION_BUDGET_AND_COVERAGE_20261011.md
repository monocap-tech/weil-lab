# RPB108 RC96 — Four-response completion budget and the coverage gap

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC95, commit `50e2eb279439d000ed4d8e32fa3cc2a90682c2f2`.
Aperture B=1.10. Complete sufficient Riesz head rank 1250.

RC96 translates the certified four-mode positivity into an exact correlated completion test. The weak/strong cross penalty can be controlled by a Gram matrix of four corrected response vectors, without evaluating every entry of a 1246-dimensional strong block. A structural lower bound for that strong block is still needed.

There is also a modest unconditional index consequence: the original operator's nonpositive spectral subspace has dimension at most 1246. This follows from positivity on the sum of the known weak span and the certified infinite complement. It is not a four-mode index theorem. Abstract finite-rank examples saturate 1246 while preserving the stated positive subspace, parity and compactness. Arithmetic structure must supply any much sharper coverage result.

No new original-source integration, strong-block floor, actual corrected-response covariance or whole-aperture positivity certificate is claimed.

## 1. Exact inherited objects

Let H be the actual canonical polynomial Riesz head of rank 1250, E its canonical orthogonal complement, and W the four-dimensional span of the fixed RC63 weak vectors. Let A_Q be the original Weil operator and alpha=247/2500 its certified E-compression floor. Set

    A = P_H A_Q P_H,
    Gamma = P_H A_Q P_E A_Q P_H,
    T = A − Gamma/alpha.

RC94 and RC95 give a positive bilinear lower L for T on W. In the fixed two-vector basis of each parity,

    L_even = Q_even,lower − G_even,RC95/alpha,
    L_odd  = Q_odd,lower  − G_odd,RC94/alpha.

RC96 reconstructs both equalities exactly from the predecessor certificates and checks their determinants. Mixed parity entries vanish. W has canonical dimension four because the certified positive bilinear form on its four generators excludes dependence.

Write S=H intersect W-perp, using the actual canonical inner product. Then dim S=1246. Let B=T_WW, C=T_WS and D=T_SS, as bilinear matrices in chosen bases. B>=L is already proved. D and C are not certified.

## 2. Conditional completion theorem

Suppose a new theorem proves

    D >= beta M_S,  beta>0,

where M_S is the actual canonical Gram in a strong basis. Suppose U is a rigorous upper for

    C M_S^(-1) C*.

Then D^(-1)<=beta^(-1) M_S^(-1), and

    B − C D^(-1) C* >= L − U/beta.

Consequently beta L−U>0 proves T>0. Together with the inherited E-floor, this proves original Weil positivity at the aperture. A weaker, easily checked sufficient condition is

    trace(L^(-1) U) < beta.

Indeed L^(-1/2) U L^(-1/2) is positive semidefinite, so its largest eigenvalue is at most its trace. The trace test loses some information; the matrix test retains the full correlation.

If D is available directly, a sharper test bounds C D^(-1) C* itself. The beta method is a sufficient strategy, not a necessary condition for positivity.

The corrected cross block is C=A_WS−Gamma_WS/alpha. Controlling the cross entries of A alone is insufficient. Nor does an uncorrected strong-head floor imply D>0 without paying the strong coupling covariance.

## 3. Four corrected responses replace the large cross table

Let the map W_0 send four coefficient coordinates to the actual weak vectors. Its canonical Gram is M_W=W_0* W_0. Define

    R = T W_0,
    B = W_0* T W_0,
    G_R = R* R.

All responses R lie in H. The canonical weak projection is

    P_W = W_0 M_W^(-1) W_0*.

Therefore the exact strong-response Gram is

    U_actual = R* P_S R
             = G_R − B M_W^(-1) B
             = C M_S^(-1) C*.

The last equality follows by expanding P_S in any strong basis. This identity is independent of that basis. It requires four response vectors and their Gram, rather than a table of 4 by 1246 cross entries. Parity reduces the matrix to two 2 by 2 blocks.

The response itself has the operator formula

    R_j = P_H A_Q w_j − alpha^(-1) P_H A_Q P_E A_Q w_j.

Thus it involves the full corrected operator, including the complement-mediated term. A rigorous enclosure may be developed through source-tail methods, projected operator applications, or a structural response theorem. RC96 proves the reduction, not that this response computation is cheap or already available. Applying P_H still requires rigorous control of the actual head projection.

Enclosing G_R and the weak capture must preserve signs and uncertainty. One cannot substitute L for B in B M_W^(-1) B merely because B>=L: squaring does not preserve that Loewner comparison in general. Likewise, Euclidean orthogonality of native coefficient vectors does not define P_W.

The validator checks this projection identity on a rational example with a nonidentity metric diag(2,3,7). Replay computes the same residual directly from the strong response components. This is an algebra check, not an original canonical-Gram certificate.

## 4. The numerical cross budget is anisotropic

For either inherited block write

    L = [[a,b],[b,d]], p=d−b²/a >0, r=b/a.

For a corrected cross column c=(c0,c1), exact inversion gives

    c* L^(-1) c = c0²/a + (c1−r c0)²/p.

In a canonical orthonormal strong basis, summing this expression over all strong columns gives trace(L^(-1) C C*). With a general strong metric, use the corresponding metric contraction. The trace must be less than beta; both parities together contribute to the full trace. Alternatively certify each parity matrix beta L_parity−U_parity>0 separately.

| Quantity | Even | Odd |
| --- | ---: | ---: |
| a | 3.549809923e-18 | 3.431976057e-16 |
| p | 6.710932180e-14 | 8.722417363e-15 |
| r=b/a | -60.10238845 | 31.81015397 |
| axis c1=0: maximum c0² / beta | 2.980339195e-18 | 8.408761787e-18 |
| axis c0=0: maximum c1² / beta | 6.710932180e-14 | 8.722417363e-15 |

Axis thresholds concern a single column with the other coordinate zero, in a unit canonical strong coordinate, with strict inequality required. They are not measured actual cross terms. Along c1=r c0, the second inverse term vanishes and c0²<beta a is sufficient for that single column. This explains why retaining cross correlation matters even after the weak diagonal blocks have been certified.

Every number used for acceptance is an exact rational in the JSON certificate. The table is display only. The validator independently checks the adjugate inverse, an LDL triangular congruence, a passing half-matrix budget, and the zero-margin boundary U=beta L.

## 5. What coverage follows without a new theorem?

The compression of A_Q to W plus E is positive. To see this, its E-block is at least alpha I and its Schur complement on W is at least the certified L>0. Since W is finite dimensional and the cross operator is bounded, completion of the square also gives a positive coercive floor on W plus E, although RC96 does not calculate that floor.

This subspace has codimension 1246. Any nonpositive spectral subspace N of A_Q intersects it only at zero: a nonzero vector in the intersection would have both nonpositive and strictly positive quadratic value. Orthogonal projection of N onto the 1246-dimensional remaining space is therefore injective, giving

    dim spectral_subspace(A_Q; (-infinity,0]) <= 1246.

This includes null modes. RC77's compactness places these modes in discrete spectrum; the codimension argument supplies the bound. It does not identify the modes, prove they lie in W, or exclude any remaining zero or negative eigenvalue. Positivity of W is evidence against danger within W, not evidence that W contains every exceptional mode.

## 6. Exact abstract obstructions: coverage and cross are separate

The validator constructs two types of rational head matrices for each inherited L.

First, diag(L,-1) retains the positive weak block and has zero weak/strong cross. Its extra strong direction has quadratic value -1. More generally, combine the two weak blocks with -I on all 1246 remaining head coordinates. Add alpha on one exterior coordinate and identity on the infinite tail, with zero head/exterior cross. This saturates the index bound while keeping the known corrected weak block positive.

Second, put c=L e0=(a,b) and strong diagonal a>0. The matrix

    [[L,c],[c*,a]]

is positive semidefinite with null vector (1,0,-1). Doubling c gives quadratic value -2a on the same vector, despite both diagonal blocks being strictly positive. Halving c pays only one quarter of the rank-one weak inverse budget and gives a positive completion. All these statements are checked exactly.

These examples can be embedded into the abstract compact-embedding framework. On l2 take i to be diagonal with entries 1/(n+1). It is compact, injective and has dense range. For any specified finite modified block of A_Q, define K on that finite support by

    K = i^(-1) (A_Q−I) i^(-1),

and set it to zero outside. K is bounded, self-adjoint and finite rank, and A_Q=I+i* K i. Coordinate polynomial spaces can supply the finite sufficient head in this abstract model. Assign modifications within parity blocks; reflection then commutes with all operators. The exterior floor is alpha and the coupling covariance is zero.

Scope is deliberately limited: these are logical countermodels to an implication from positive corrected weak blocks, parity, a positive infinite complement and compactness. They do not preserve the original arithmetic source formulas, physical norm estimates, all inherited entry intervals or the actual Fourier embedding. They are not counterexamples to the original Weil positivity problem. Those additional structures may be precisely what proves a sharper coverage theorem.

## 7. Next theorem-facing obligation

The decisive next target is a corrected strong-floor or coverage theorem on S, together with a rigorous upper for the four-response Gram. RC96 provides the acceptance formula for that result. Another improvement to the already-positive four-mode block is useful only if it helps pay this remaining interaction.

A structural strong floor could avoid evaluating a dense strong matrix. If such a floor fails, a spectral exclusion theorem may enlarge W by only the truly exceptional modes. Global/F4 first-contact exclusion remains an independent alternative; no separate aperture-1.10 certificate has become logically mandatory.

## Verification

Inputs: RC95 and RC94; their byte SHA-256 digests and predecessor crosslink are checked. This validator inherits their signed source calculations rather than replaying those integrations again.

Generation uses exact Fraction inversion and rational witness tests. Independent algebra replay uses adjugate inversion, triangular congruence and direct metric strong components. The JSON must match exactly. No floating eigenvalue, quadrature, new Lean proof, dense original head, actual response Gram, strong floor, RH or F4 claim is made.

Deliverables:

- `scripts/validate_rpb108_rc96_weak_strong_completion_budget.py`
- `certificates/rpb108_rc96_weak_strong_completion_budget.json`
- `notes/RPB108_RC96_FOUR_RESPONSE_COMPLETION_BUDGET_AND_COVERAGE_20261011.md`
