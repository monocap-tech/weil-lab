# RPB108 RC104 — Eight low modes and the strong floor after six-mode isolation

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC103, commit `a164eaaacce8f0b41949fa64e5765e9dd65f9965`.
Aperture B=1.10. Actual sufficient canonical head H has rank 1250.

RC104 certifies a four-dimensional low-Rayleigh span in each parity, using existing signed original source and metric data. Each span necessarily intersects the remaining strong space after removal of the three certified weak vectors in that parity. This bounds the possible strong floor for both the exact effective head and the scalar-floor effective head, without approximating the actual canonical projection.

The original operator has at least eight discrete eigenvalues below the reported small positive ceiling. This is not a proof of eight nonpositive modes. The known positive corrected span remains six-dimensional and the nonpositive spectral-dimension upper remains 1244.

## Fixed rational test spans

RC104 fixes four rational native coefficient vectors in each parity. They lie in the unchanged 22-feature native Riesz span and hence in the sufficient head H1250. Candidate selection used a floating generalized eigensolve of the signed nominal trial form against the actual native metric lower. Each candidate was rescaled to maximum coefficient magnitude one and rounded to a denominator dividing 10^12.

The search is not proof or acceptance. The production validator embeds the fixed rational vectors and has no numerical eigensolver dependency. It certifies the resulting entire subspace, with all original source and metric error allowances, using exact Fractions. No asserted eigenvector property of a candidate is used.

For the fixed coefficient matrix W_4, contract RC67's actual canonical native Gram lower:

    M_lower = W_4* M_native,lower W_4.

Exact positive pivots prove M_lower>0, and therefore actual dimension four. The vectors need not contain the three known weak vectors and need not be orthogonal to them. Dimension intersection will replace numerical projection.

## Matching signed original head reconstruction

All nominal quantities use RC67's matching 64-mode Riesz trials V and the same RC68 original source construction. With nominal trial metric G_0, physical Legendre mass M_phys, exact native target coefficient matrix C, and nominal trial/source pairing H_0, the signed trial Weil center is

    Q_0 = sym(V* G_0 V + H_0 - (C* M_phys V)*).

This is the RC97 signed reconstruction identity; all 4-by-4 contractions are performed on the original signed center. Pairing radii and the nominal metric/operator approximation allowance are paid separately.

RC81's raw nominal Legendre residual intervals are first contracted onto the four exact physical targets. After common row inflation with unit scales and nu=1/65536,

    Ep = rho^2 [(1+nu) E_nom,upper
                  +(1+1/nu) delta_L^2 T_trial],
    rho=252/257.

This supplies a common actual physical Riesz error upper. Source norms use RC68's raw signed Gram contracted on each candidate, plus its actual operator approximation allowance, rather than a broad preinflated diagonal estimate.

For each original head entry, the additional allowances are

    trial pairing radius + (delta_K+delta_G) sqrt(T_ii T_jj),
    sqrt(Ep_ii) source_norm_j + sqrt(Ep_jj) source_norm_i,
    kappa sqrt(Ep_ii Ep_jj).

Canonical diagonal correction lies between -Ep_ii/rho and zero; off-diagonal correction is bounded absolutely by sqrt(Ep_ii Ep_jj)/rho. Directed rational endpoint rounding gives ten signed entry enclosures in each parity. Unit-scale weighted row inflation then gives a common original head upper Q_upper.

The certificate verifies the exact inequality

    Q_actual <= Q_upper <= eta M_lower <= eta M_actual.

The scalar eta is a sufficient entire-subspace Rayleigh ceiling. It is not merely a maximum of four individual tests; all mixed combinations are covered. No new source integrations are required.

## Exact ceilings and spectral meaning

| Parity | Exact whole-span canonical Rayleigh upper eta | Approximate display |
| --- | --- | ---: |
| Even | 110385385239/4294967296000000 | 2.57011002952e-5 |
| Odd | 1671169795457/8589934592000000 | 1.94549769566e-4 |

Each four-dimensional span has every original canonical Rayleigh quotient at most its eta. RC77 compactness gives A_Q=I+compact with essential spectrum at 1. The selfadjoint minmax principle therefore certifies at least four discrete eigenvalues in each parity at or below eta, counting multiplicity. At least eight original eigenvalues are at or below the common ceiling eta_odd<1.

These eigenvalues may all be positive. The result counts low spectrum; it does not classify it as negative or null. In particular, the certified six-dimensional positive span is not asserted to consist of exact eigenvectors, and the two additional low directions below are not asserted to be eigenvectors.

## The actual strong-floor restriction

Let W be the known three-dimensional canonical weak span in one parity and S=H orthogonal W. Restrict the canonical orthogonality functionals <W_j, .> to the four-dimensional test span X. There are at most three independent constraints, so

    dim(X intersect S)>=4-3=1.

A nonzero actual strong vector therefore exists with original Rayleigh quotient at most eta. This argument uses actual canonical orthogonality and dimension, without estimating a projection matrix or substituting the physical metric for the canonical one.

For E=H orthogonal complement define, as in RC103,

    D=P_E A_Q P_E,    B=P_H A_Q P_E,
    F=A_H-B D^(-1)B*,
    T_alpha=A_H-alpha^(-1)B B*,    alpha=247/2500.

Since D is positive, F<=A_H and T_alpha<=A_H. If either effective head has a positive canonical lower beta on S, evaluating it on the actual low strong vector proves

    beta_even <= eta_even,
    beta_odd <= eta_odd.

A single floor used for both parity blocks satisfies beta<=eta_even. The argument supplies upper restrictions on possible floors, not positive lower bounds. It proves at least one low strong direction per parity, independently of the known positive six-dimensional compression.

RC97's much smaller strong-floor ceiling concerned removal of only two weak vectors per parity. Its three-dimensional test span could then guarantee an intersection. That same argument cannot be carried unchanged to removal of three vectors. RC104 supplies the required fourth dimension for the current six-mode decomposition.

Consequently RC103's hypothetical targets beta=1 and beta=10^-3 are impossible as floors of the current remaining effective strong blocks. The smaller targets in that table are not ruled out by these ceilings, but none is thereby certified.

## Consequences for the uniform inverse budget

RC103 allocates epsilon_n^2 V<=beta L/8, with V=(g/alpha^2)G and epsilon_n the certified uniform Chebyshev residual. Even at the largest allowed parity-specific floor, the first passing degrees are:

| Parity | Optimistic floor used only as an upper limit | Residual degree n | Inverse polynomial degree |
| --- | ---: | ---: | ---: |
| Even | eta_even | 35 | 34 |
| Odd | eta_odd | 26 | 25 |

RC104 checks the full exact matrix inequality at these degrees and its failure at the immediately preceding degree. Smaller degrees have larger uniform epsilon_n, so they cannot meet this same matrix allowance at any beta<=eta. A shared beta may impose a larger odd degree, and a smaller actual strong floor imposes further work.

This is a lower restriction on that particular uniform certificate with the inherited G and L. It is not a lower bound on the actual difficulty of inversion, on the degree needed by a posterior residual solver, or on the work needed by a different proof. RC103's 52/43 residual degrees for hypothetical beta=10^-9 remain valid conditional budgets.

## Verification and remaining work

The twelve direct inputs are RC103, RC102, RC101, RC100, RC95, RC63, RC67, RC59, RC68, RC81, RC66 and RC77. Byte SHA-256 digests and predecessor/source/trial crosslinks are checked. The sufficient head, aperture, original operator and native trials are unchanged.

Generation contracts signed matrices directly. Independent replay reorders the source/residual contractions, uses column-first head/metric contractions and the positive-binomial Chebyshev identity. It rebuilds the exact rank, original Rayleigh ceilings, strong-floor exclusions and uniform-budget boundary tests, and requires equality with the saved certificate. The exploratory candidate file is an intermediate artifact, not an extra repository deliverable.

The test now establishes that the remaining strong space contains additional low-energy directions. The next obligation is a positive lower certificate on that space, or a spectral/structural exclusion theorem that controls its potentially nonpositive part. The six lifted-response certificate is separately open. No strong lower, negative/null mode, complete nonpositive-mode coverage, whole-aperture positivity, Global/F4 or RH claim is made. This is an internal exact-rational certificate with analytic minmax and intersection lemmas, not a Lean formalization.

- `scripts/validate_rpb108_rc104_eight_mode_strong_floor_ceiling.py`
- `certificates/rpb108_rc104_eight_mode_strong_floor_ceiling.json`
- `notes/RPB108_RC104_EIGHT_LOW_MODES_AND_SIX_MODE_STRONG_FLOOR_CEILING_20261011.md`
