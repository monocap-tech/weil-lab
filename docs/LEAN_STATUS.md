# Lean Status Ledger

This file records formal verification separately from mathematical standing and P4 audit status.

## Status labels

- **LEAN-NOT-ATTEMPTED** — not yet entered into the formalization queue.
- **LEAN-IN-PROGRESS** — a Lean declaration or infrastructure exists but has not yet passed the pinned CI build.
- **LEAN-CERTIFIED** — kernel-checked under the pinned toolchain with no project \`sorry\`, \`admit\`, or \`axiom\`.
- **LEAN-CERTIFIED-FROM-IMPORTED-PREMISE** — Lean verifies the downstream deduction from an explicit external premise, but not the external theorem itself.
- **LEAN-BLOCKED** — direct formalization is exhausted for the current pass and an exact missing formal dependency is recorded.
- **SCOPE-ONLY** — jurisdiction rule rather than a theorem.

## Declaration map

| Stable ID | Lean declaration | Status |
| --- | --- | --- |
| WD-T09 | WeilDefect.WDT09.wd_t09_full_quadratic_factorization + WeilDefect.WDT09.wd_t09_shared_defect_factorization + WeilDefect.WDT09.wd_t09_full_nonnegative_iff_joint_budget + WeilDefect.WDT09.wd_t09_separate_contractions_not_joint + WeilDefect.WDT09.wd_t09_shared_screening_budget | LEAN-CERTIFIED |
| WD-T08 | WeilDefect.WDT08.selected_adjoint_comp_injective + WeilDefect.WDT08.wd_t08_selected_negative_rank_le_finrank + WeilDefect.WDT08.wd_t08_background_null_finrank_lower + WeilDefect.WDT08.wd_t08_selected_negative_on_background_null + WeilDefect.WDT08.wd_t08_full_negative_rank_background_reduction + WeilDefect.WDT08.wd_t08_finite_selected_sector_index_cap | LEAN-CERTIFIED |
| WD-T07 | WeilDefect.wd_t07_selected_full_identity + WeilDefect.wd_t07_selected_negative_implies_full + WeilDefect.WDT07.wd_t07_full_le_selected + WeilDefect.WDT07.wd_t07_negative_rank_custody + WeilDefect.WDT07.wd_t07_full_negative_without_selected_negative + WeilDefect.WDT07.wd_t07_selected_background_monotonicity_and_custody | LEAN-CERTIFIED |
| WD-T06 | WeilDefect.WDT06.wd_t06_truncated_inner_identity + WeilDefect.WDT06.wd_t06_quadratic_mono + WeilDefect.WDT06.wd_t06_defect_mono + WeilDefect.WDT06.wd_t06_defect_le_full + WeilDefect.WDT06.wd_t06_defect_strong_tendsto + WeilDefect.WDT06.wd_t06_quadratic_tendsto + WeilDefect.WDT06.wd_t06_negative_rank_antitone + WeilDefect.WDT06.wd_t06_monotone_positive_screening | LEAN-CERTIFIED |
| WD-T05 | WeilDefect.wd_t05_rank_one_covariance + WeilDefect.WDT05.wd_t05_defect_rank_one + WeilDefect.WDT05.wd_t05_signed_factor_iff_vector + WeilDefect.WDT05.wd_t05_covariance_iff_unit_vector + WeilDefect.WDT05.wd_t05_physical_nonnegative_iff_unit_vector + WeilDefect.WDT05.wd_t05_analysis_nonnegative_iff_unit_vector + WeilDefect.WDT05.wd_t05_rank_one_specialization | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T04 | WeilDefect.WDT04.wd_t04_range_defect_no_exact_screening + WeilDefect.WDT04.wd_t04_range_defect_negative + WeilDefect.WDT04.wd_t04_over_budget_negative + WeilDefect.WDT04.wd_t04_strict_screened_lower_bound + WeilDefect.WDT04.wd_t04_attained_critical_neutral + WeilDefect.WDT04.wd_t04_nonattained_critical_positive + WeilDefect.WDT04.wd_t04_critical_approximate_neutral + WeilDefect.WDT04.wd_t04_complete_reduced_taxonomy | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T03 | WeilDefect.WDT03.wd_t03_kernel_decomposition + WeilDefect.WDT03.wd_t03_analysis_graph_iff + WeilDefect.WDT03.wd_t03_graph_signature + WeilDefect.WDT03.wd_t03_defect_factorization | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T02 | WeilDefect.WDT02.wd_t02_contractive_screening_equivalence + WeilDefect.WDT02.wd_t02_unique_reduced_solution | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T01 | WeilDefect.WDT01.wd_t01_defect_inner_identity + WeilDefect.WDT01.wd_t01_nonnegative_iff + WeilDefect.WDT01.wd_t01_negative_rank_iff | LEAN-CERTIFIED |
| WD-T33 | WeilDefect.wd_t33_adaptive_cocancellation | LEAN-CERTIFIED |
| WD-T30 | WeilDefect.wd_t30_two_mode_kernel_combination + WeilDefect.wd_t30_zero_functional_preserves_every_mode | LEAN-CERTIFIED |
| WD-X01 | WeilDefect.wd_x01_partial_sum + WeilDefect.wd_x01_finite_defect_negative + WeilDefect.wd_x01_finite_defect_formula + WeilDefect.wd_x01_defect_tendsto_zero | LEAN-CERTIFIED |
| WD-T26 | \`WeilDefect.wd_t26_finite_pair_zero_moment\` | LEAN-IN-PROGRESS |
| WD-X03 | \`WeilDefect.wd_x03_individual_not_compositional\` | LEAN-IN-PROGRESS |
| WD-X04 | \`WeilDefect.wd_x04_shorted_covariance_identity\` | LEAN-IN-PROGRESS |
| WD-X07 | WeilDefect.wd_x07_response_identity + WeilDefect.wd_x07_real_response_formula + WeilDefect.wd_x07_scaled_response_tendsto_neg_one | LEAN-CERTIFIED |

The statuses above become LEAN-CERTIFIED only after the pinned CI build succeeds.

## Current formalization cursor

\[
\boxed{
\texttt{LEAN-H1-P0 / INFRASTRUCTURE AND VERTICAL PILOT}.
}
\]


## First certificate evidence

The first stable-ID certifications were built at Lean commit:

\[
\boxed{
\texttt{c125114e2dd39fa3907f8690ca39d9c899468caf}.
}
\]

GitHub Actions run:

\[
\boxed{
\texttt{35949414095}.
}
\]

The run completed successfully with all of:

- pinned dependency resolution;
- mathlib cache fetch;
- Lake build;
- unfinished/project-axiom rejection.

Thus WD-X03 and WD-X04 satisfy the repository's LEAN-CERTIFIED rule.

WD-T26 and WD-X07 remain LEAN-IN-PROGRESS because their current declarations certify only algebraic cores, not yet the complete stable theorem/example statements.

## Current formalization cursor

\[
\boxed{
\texttt{LEAN-H1-P1 / ALGEBRAIC AND FINITE-DIMENSIONAL CORE}.
}
\]


## WD-X01 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-X01: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.wd_x01_weight_sq_telescope;
- WeilDefect.wd_x01_partial_sum;
- WeilDefect.wd_x01_finite_defect_negative;
- WeilDefect.wd_x01_finite_defect_formula;
- WeilDefect.wd_x01_defect_tendsto_zero.

The dedicated theorem CI checked only:

\[
\texttt{WeilDefect/Examples/SpectralScreening.lean}.
\]

Certificate run:

\[
\boxed{
\texttt{35952789867}
}
\]

at repository head:

\[
\boxed{
\texttt{6ef0dffba1a8732d554b15ee906c64fe60bc63c7}.
}
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- Lean compilation of the WD-X01 target;
- repository unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-X07 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-X07: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.wd_x07_response_identity;
- WeilDefect.wd_x07_real_response_formula;
- WeilDefect.wd_x07_scaled_response_tendsto_neg_one.

The certificate proves the exact two-point rational identity and an explicit
sharpness witness with nonzero inverse-square leading coefficient.

The current theorem file blob

\[
\texttt{83196783b21e40eee21ca74c12b3b8094c2af391}
\]

is identical to the blob checked successfully by GitHub Actions run

\[
\boxed{
\texttt{35951096357}.
}
\]

That run checked repository commit

\[
\texttt{e9f158d3c8fb5b85494d08931d62cddfc8d4a534}
\]

under the pinned Lean 4.34.0 / mathlib v4.34.0 environment and passed the
unfinished-proof/project-axiom gate.

A later dedicated WD-X07 rerun was also launched for redundant single-target
confirmation; certification does not depend on it because the exact current
Lean source blob is already kernel-checked.

No other stable theorem ID is promoted by this certificate.


## WD-T30 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T30: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.wd_t30_two_mode_selected_preserving;
- WeilDefect.wd_t30_both_zero_selected_preserving;
- WeilDefect.wd_t30_two_mode_kernel_combination;
- WeilDefect.wd_t30_zero_functional_preserves_every_mode.

The stable theorem is represented at the functional level:

given a complex-linear selected-response functional \(C\) and two multiplier
modes \(\psi_1,\psi_2\) whose selected responses are not both zero, Lean
constructs a nontrivial coefficient pair \((\beta_1,\beta_2)\) with

\[
C(\beta_1\psi_1+\beta_2\psi_2)=0.
\]

The identically-zero functional branch is also formalized: every mode is
selected-preserving.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Arithmetic.Scalarization}
\]

through Lake.

Certificate run:

\[
\boxed{
\texttt{35953990661}
}
\]

at repository head:

\[
\boxed{
\texttt{6836f64a22544a2bd51daeb97d97bf824d339def}.
}
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T33 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T33: LEAN-CERTIFIED}.
}
\]

Formal declaration:

- WeilDefect.wd_t33_adaptive_cocancellation.

The certificate formalizes the exact cutoffwise algebraic implication:

\[
N+F=P+A,
\qquad
N=A
\quad\Longrightarrow\quad
P=F.
\]

This is the complete algebraic content of the audited WD-T33 co-adaptation theorem.
The analytic interpretation of \(N,F,P,A\) belongs to the surrounding explicit-formula
setup and is not assumed by the Lean proof.

The current theorem file blob

\[
\texttt{d01f92d725b9ad412130424b74bea9efadcda1e1}
\]

is identical to the blob included in successful full-library GitHub Actions run

\[
\boxed{
\texttt{35951096357}.
}
\]

That run checked commit

\[
\texttt{e9f158d3c8fb5b85494d08931d62cddfc8d4a534}
\]

with:

- pinned dependency resolution;
- mathlib cache retrieval;
- full Lake build;
- unfinished-proof/project-axiom rejection.

A later dedicated WD-T33-only CI run was also launched; certification does not depend
on it because the exact current source blob was already kernel-checked in the successful
full-library run.

No other stable theorem ID is promoted by this certificate.


## WD-T01 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T01: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.WDT01.wd_t01_coeff_identity;
- WeilDefect.WDT01.wd_t01_defect_inner_identity;
- WeilDefect.WDT01.wd_t01_nonnegative_iff;
- WeilDefect.WDT01.negativeWitness_injective_of_zero;
- WeilDefect.WDT01.wd_t01_physical_to_analysis_rank;
- WeilDefect.WDT01.wd_t01_analysis_to_physical_rank;
- WeilDefect.WDT01.wd_t01_negative_rank_iff.

The formal negative-index statement is encoded dimension-by-dimension.

For each \(n\), Lean proves equivalence between:

1. an \(n\)-direction negative witness in the physical carrier; and
2. an \(n\)-direction negative witness in the closed analysis carrier.

The bridge theorem proves such a unit-sphere negative witness is injective whenever
the quadratic form vanishes at zero. Therefore these witnesses are genuine
\(n\)-dimensional negative directions, and equality for every finite \(n\) is the
formal finite-rank-spectrum version of equality of the supremum negative indices.

The certificate also proves:

\[
[E^*h,E^*h]_J
=
\langle Dh,h\rangle,
\]

in the project coefficient/operator encoding, and

\[
\mathcal A\text{ nonnegative}
\iff
D\text{ nonnegative}.
\]

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.DefectIndex}.
\]

Certificate run:

\[
\boxed{
\texttt{35959085940}
}
\]

at repository head:

\[
\boxed{
\texttt{79218489b0a3cdeacc5ed7abe44565ee45fffca5}.
}
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T02 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T02: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
\]

Formal declarations:

- WeilDefect.WDT02.physicalNonnegative_iff_covarianceLe;
- WeilDefect.WDT02.covarianceLe_iff_signed_contractive_factorization;
- WeilDefect.WDT02.reduced_neg_iff;
- WeilDefect.WDT02.signed_reduced_exists_unique;
- WeilDefect.WDT02.wd_t02_contractive_screening_equivalence;
- WeilDefect.WDT02.wd_t02_unique_reduced_solution.

The imported theorem is represented explicitly by the proposition-valued structure

\[
\texttt{WeilDefect.WDT02.DouglasUnitData}.
\]

It supplies exactly the Douglas unit-majorization input:

- covariance majorization iff contractive factorization;
- existence and uniqueness of the reduced exact factor.

It is passed as a theorem premise. It is not declared as a project axiom.

Lean then verifies the full Horizon-1 convention transfer:

\[
\mathcal A\text{ nonnegative}
\iff
D\succeq0
\iff
S_-S_-^*\preceq S_+S_+^*
\iff
\exists X,\ \|X\|\le1,\ S_-=-S_+X,
\]

where covariance order is encoded by its quadratic-form inequality.

Lean also verifies that the Douglas reduced solution transfers through the
project sign convention and is unique among exact signed solutions whose range
is orthogonal to \(\ker S_+\).

The Douglas source theorem itself has not been reconstructed in Lean.
Accordingly this theorem must not be reported as a native LEAN-CERTIFIED result.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.Douglas}.
\]

Certificate run:

\[
\boxed{
\texttt{35960549233}
}
\]

at repository head:

\[
\boxed{
\texttt{5dca4d98b7062e3676399b34dfc89b383bfe1662}.
}
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T03 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T03: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
\]

Formal declarations include:

- WeilDefect.WDT03.signed_reduced_of_range;
- WeilDefect.WDT03.wd_t03_kernel_decomposition;
- WeilDefect.WDT03.wd_t03_analysis_graph_iff;
- WeilDefect.WDT03.wd_t03_graph_signature;
- WeilDefect.WDT03.wd_t03_defect_factorization;
- WeilDefect.WDT03.wd_t03_reduced_graph_normal_form.

The imported theorem is isolated in the explicit proposition-valued interface
WeilDefect.WDT03.DouglasRangeData. It supplies only the Douglas
range-inclusion step giving the unique reduced exact factor.

Once the reduced signed solution X is supplied, Lean verifies internally the
orthogonal kernel decomposition, graph characterization, graph signature
identity, and defect factorization.

The coefficient direct-sum inner form is represented explicitly as

\[
\langle(a,v),(x,u)\rangle_\oplus
=
\langle a,x\rangle+\langle v,u\rangle,
\]

so the formalization does not confuse Lean's ordinary product Banach norm with
the Hilbert direct-sum norm.

Dedicated theorem CI built WeilDefect.Screening.GraphNormalForm.

Certificate run:

\[
\boxed{\texttt{35962199281}}
\]

at repository head:

\[
\boxed{\texttt{570dcb25de1e728bb2b135363e0b0d1ae735b5e5}}.
\]

The run passed the single-module Lake build and unfinished-proof/project-axiom
gate. The Douglas source theorem itself remains unformalized.

No other stable theorem ID is promoted by this run.


## WD-T04 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T04: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
\]

Formal declarations:

- WeilDefect.WDT04.wd_t04_range_defect_no_exact_screening;
- WeilDefect.WDT04.wd_t04_range_defect_negative;
- WeilDefect.WDT04.wd_t04_over_budget_negative;
- WeilDefect.WDT04.wd_t04_strict_screened_lower_bound;
- WeilDefect.WDT04.wd_t04_attained_critical_neutral;
- WeilDefect.WDT04.wd_t04_nonattained_critical_positive;
- WeilDefect.WDT04.wd_t04_critical_approximate_neutral;
- WeilDefect.WDT04.wd_t04_complete_reduced_taxonomy.

The certificate formalizes the five-way abstract screening morphology:
range defect, over-budget negative defect, strict positive screening, attained
critical neutrality, and non-attained approximate neutrality.

The range-defect negative-direction implication consumes the explicit
WeilDefect.WDT02.DouglasUnitData theorem premise.  Douglas is not introduced as
a project axiom and is not reconstructed by this certificate.  The
over-budget, strict-screening, attained-critical, and non-attained-critical
branches are checked internally once the reduced factor is given.

In particular, the non-attained critical branch does not assume operator-norm
attainment.  Lean derives arbitrarily small graph defect from the definition of
the operator norm while proving every nonzero graph vector remains strictly
positive when no nonzero adjoint vector attains norm one.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.Taxonomy}.
\]

Certificate run:

\[
\boxed{\texttt{35965367830}}
\]

at repository head:

\[
\boxed{\texttt{fe4ab88bbed7e5a6b1091587569ccb7713522960}}.
\]

The certified theorem source blob is:

\[
\texttt{f86f72692fb4465827e4ec9f374a5a3c64f3d22a}.
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T05 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T05: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
\]

Formal declarations:

- WeilDefect.wd_t05_rank_one_covariance;
- WeilDefect.wd_t05_rank_one_covariance_apply;
- WeilDefect.WDT05.rankOneNegative;
- WeilDefect.WDT05.wd_t05_defect_rank_one;
- WeilDefect.WDT05.wd_t05_signed_factor_iff_vector;
- WeilDefect.WDT05.wd_t05_covariance_iff_unit_vector;
- WeilDefect.WDT05.wd_t05_physical_nonnegative_iff_unit_vector;
- WeilDefect.WDT05.wd_t05_analysis_nonnegative_iff_unit_vector;
- WeilDefect.WDT05.wd_t05_rank_one_specialization.

Lean verifies natively that the one-dimensional synthesis map
\(\alpha\mapsto\alpha g\) has covariance \(g\otimes g\), hence

\[
D=S_+S_+^*-g\otimes g.
\]

It also verifies internally that a signed contractive map
\(X:\mathbb C\to K_+\) is equivalent to a single coefficient vector
\(c=X(1)\) with \(\|c\|\le1\), and reconstructs the converse factor from
\(c\) by \(\operatorname{toSpanSingleton}(c)\).

The covariance-majorization/positivity-to-factorization step is supplied by
the explicit proposition-valued Douglas premise

\[
\texttt{WeilDefect.WDT02.DouglasUnitData}.
\]

Therefore the complete stable theorem is reported as
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE rather than native LEAN-CERTIFIED.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.RankOne}.
\]

Certificate run:

\[
\boxed{\texttt{35966956166}}
\]

at repository head:

\[
\boxed{\texttt{ef3853ef4a3892662fa59761685dfe68b1f82844}}.
\]

The certified theorem source blob is:

\[
\texttt{2c37aaf3546b49cbab8be2c58ee954fd6989a965}.
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T06 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T06: LEAN-CERTIFIED}.
}
\]

Formal declarations include:

- WeilDefect.WDT06.ProjectionChainData;
- WeilDefect.WDT06.projection_inner_self;
- WeilDefect.WDT06.projection_norm_mono;
- WeilDefect.WDT06.wd_t06_truncated_inner_identity;
- WeilDefect.WDT06.wd_t06_quadratic_mono;
- WeilDefect.WDT06.wd_t06_quadratic_le_full;
- WeilDefect.WDT06.wd_t06_defect_mono;
- WeilDefect.WDT06.wd_t06_defect_le_full;
- WeilDefect.WDT06.wd_t06_defect_strong_tendsto;
- WeilDefect.WDT06.wd_t06_quadratic_tendsto;
- WeilDefect.WDT06.wd_t06_negative_rank_antitone;
- WeilDefect.WDT06.wd_t06_monotone_positive_screening.

The projection-chain interface records exactly the operator properties consumed by
the proof: self-adjointness, idempotence, nesting, contractivity, and strong
convergence to the identity.

Lean then verifies internally that

\[
D_N=S_+P_NS_+^*-S_-S_-^*
\]

has quadratic form

\[
\|P_NS_+^*h\|^2-\|S_-^*h\|^2,
\]

that the projected positive norms are nondecreasing under the nested
contractive projections, and hence

\[
D_N\preceq D_{N+1}\preceq D.
\]

It also proves strong pointwise operator convergence

\[
D_Nh\to Dh,
\]

and pointwise convergence of the corresponding quadratic forms.

Negative-index monotonicity is certified in the same dimension-by-dimension
form used by WD-T01: every \(k\)-dimensional negative witness for
\(D_{N+1}\) is already a \(k\)-dimensional negative witness for \(D_N\).
Thus the attainable finite negative-rank spectrum is nonincreasing under
positive-channel restoration.

No imported theorem premise is used by WD-T06.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.MonotoneScreening}.
\]

Certificate run:

\[
\boxed{\texttt{35967932548}}
\]

at repository head:

\[
\boxed{\texttt{6024cce8bf4f152ca21a545b93cb467e7cdadb31}}.
\]

The certified theorem source blob is:

\[
\texttt{b4424d28e14466275f593e58683170d9e952b134}.
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T07 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T07: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.wd_t07_selected_full_identity;
- WeilDefect.wd_t07_selected_negative_implies_full;
- WeilDefect.WDT07.wd_t07_full_le_selected;
- WeilDefect.WDT07.wd_t07_negative_rank_custody;
- WeilDefect.WDT07.wd_t07_converse_failure;
- WeilDefect.WDT07.wd_t07_full_negative_without_selected_negative;
- WeilDefect.WDT07.wd_t07_selected_background_monotonicity_and_custody.

Lean verifies the exact quadratic identity

\[
q_{\rm full}(h)
=
q_M(h)-\|S_B^*h\|^2,
\]

and therefore the pointwise form order

\[
q_{\rm full}(h)\le q_M(h).
\]

It certifies the negative-index custody statement in finite-rank-spectrum form:
for every \(k\), any \(k\)-dimensional negative witness for the selected
quadratic form remains a \(k\)-dimensional negative witness for the full
quadratic form after arbitrary negative-background aggregation.

The converse is disproved internally by an explicit one-dimensional complex
example: selected positive and negative synthesis maps are zero while the
background synthesis is the identity.  At \(h=1\), the selected quadratic
value is zero but the full quadratic value is strictly negative.  Thus full
aggregate negativity does not identify the selected sector as the owner of the
defect.

No imported theorem premise is used by WD-T07.

The first dedicated attempt exposed only a simplifier gap for the adjoint of
the identity map; this was repaired explicitly using mathlib's
`ContinuousLinearMap.adjoint_id`.  No theorem statement changed.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.BackgroundCustody}.
\]

Certificate run:

\[
\boxed{\texttt{35968741697}}
\]

at repository head:

\[
\boxed{\texttt{48f20dfa63e5b36bd5786a0fc9fe23db9e63e21a}}.
\]

The certified theorem source blob is:

\[
\texttt{8a0acaef36c3c10df5f0ec6d7a692db1b420f32a}.
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T08 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T08: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.WDT08.selected_adjoint_comp_injective;
- WeilDefect.WDT08.wd_t08_selected_negative_rank_le_finrank;
- WeilDefect.WDT08.backgroundNullCoords;
- WeilDefect.WDT08.wd_t08_background_null_finrank_lower;
- WeilDefect.WDT08.wd_t08_selected_negative_on_background_null;
- WeilDefect.WDT08.wd_t08_full_negative_rank_background_reduction;
- WeilDefect.WDT08.wd_t08_finite_selected_sector_index_cap.

For the selected sector, Lean proves that any k-dimensional negative witness
forces the composed adjoint map

\[
S_M^*\circ T : \mathbb C^k \to M
\]

to be injective.  Finite-dimensional rank comparison therefore gives

\[
k\le \dim M.
\]

This is the finite-rank-spectrum form of

\[
\operatorname{ind}_{-}(D_M)\le \dim M.
\]

For the background correction, given any k-dimensional full negative witness
T, Lean forms the canonical coordinate kernel

\[
\ker(S_B^*\circ T).
\]

Rank-nullity and the finite-dimensional range bound give

\[
k-\dim B
\le
\dim\ker(S_B^*\circ T).
\]

On this kernel the background term vanishes identically, so the full and
selected quadratic forms agree, and Lean proves the selected form is strictly
negative on the unit sphere of that kernel.  This is exactly the
finite-dimensional kernel-slice argument underlying

\[
\operatorname{ind}_{-}(D_{\rm full})
\le
\operatorname{ind}_{-}(D_M)+\dim B.
\]

The stable theorem is therefore certified in the same finite-negative-rank /
negative-subspace encoding used by the earlier index certificates.

No imported theorem premise is used by WD-T08.

The first dedicated build exposed only a normalization-through-kernel
simplification issue.  The repair replaced automation by the explicit fact
that a scalar multiple of a kernel vector remains in the kernel; no theorem
statement or mathematical hypothesis changed.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.FiniteIndexCap}.
\]

Certificate run:

\[
\boxed{\texttt{36007743473}}
\]

at repository head:

\[
\boxed{\texttt{c2b318997f2aaa9ca756ae66f9149ba9ac34956a}}.
\]

The certified theorem source blob is:

\[
\texttt{9c61af90ab1374f65df446c558790a8b7f4dff27}.
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T09 certificate evidence

Stable ID:

\[
\boxed{
\text{WD-T09: LEAN-CERTIFIED}.
}
\]

Formal declarations:

- WeilDefect.WDT09.sharedDefect;
- WeilDefect.WDT09.JointBudget;
- WeilDefect.WDT09.FullNonnegative;
- WeilDefect.WDT09.adjoint_of_signed_factor;
- WeilDefect.WDT09.wd_t09_full_quadratic_factorization;
- WeilDefect.WDT09.wd_t09_shared_defect_factorization;
- WeilDefect.WDT09.wd_t09_full_nonnegative_iff_joint_budget;
- WeilDefect.WDT09.wd_t09_separate_contractions_not_joint;
- WeilDefect.WDT09.wd_t09_shared_screening_budget.

The certificate is stated on the reduced positive carrier, encoded by

\[
\ker S_+=0,
\]

which is the abstract theorem's \((\ker S_+)^\perp\) target treated as its
own Hilbert carrier.

Under exact signed screening factorizations

\[
S_M=-S_+X_M,
\qquad
S_B=-S_+X_B,
\]

Lean verifies the operator identity

\[
D_{\rm full}
=
S_+
\left(
I-X_MX_M^*-X_BX_B^*
\right)
S_+^*.
\]

It also proves natively that full nonnegativity is equivalent to the shared
quadratic budget

\[
\|X_M^*a\|^2+\|X_B^*a\|^2
\le
\|a\|^2
\qquad
\forall a.
\]

For the reverse implication from full physical nonnegativity to the global
coefficient-space budget, Lean uses

\[
\overline{\operatorname{Ran}S_+^*}
=
(\ker S_+)^\perp
=
K_+,
\]

and closure of the budget inequality. Thus no Douglas factorization theorem
premise is consumed by the WD-T09 certificate.

The file imports the Douglas module only to reuse the IsContraction definition
in the explicit separate-versus-joint counterexample. It does not consume
DouglasUnitData or any imported theorem premise.

Lean also certifies that separate unit bounds are insufficient: with both
screening maps equal to the identity on \(\mathbb C\), each individual map
has norm one, while the joint budget fails at \(a=1\).

The first WD-T09 build exposed only local elaboration issues: theorem
visibility, rewrite order, closed-set construction, and final scalar
arithmetic. These were repaired without changing the theorem statement or
mathematical hypotheses.

Dedicated theorem CI built:

\[
\texttt{WeilDefect.Screening.BackgroundCustody}.
\]

Certificate run:

\[
\boxed{\texttt{36019357419}}
\]

at repository head:

\[
\boxed{\texttt{f08c8f8a5639e1cf9d23b6381ca852c6c2e1007a}}.
\]

The certified theorem source blob is:

\[
\texttt{eec7e8db876cf2504bc3cca349b68bb60d93a626}.
\]

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T09-containing module;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.
