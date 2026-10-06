# RPB108: global lane recovery, contact dichotomy, and F4 entry audit

Date: 2026-10-06 (America/Los_Angeles).
Pinned live recovery: d7ce2da16b3162edd31216587a42e63a53897733.
Requested checkpoint: 66001e26df619feb80dfe8144b761dad1e9cc33c; not restored.
Publication rebase: 0f6add60ad0a58e5c3e1ec09da44d766b390940b. Its aperture-only source/native repair and cursor were recovered and preserved.
Scope: GLOBAL ENDPOINT / RETAINED ATTACHMENT -> F4. No aperture computations.

## Definitions and scope

Here D_a is the actual supported logarithmic Hilbert domain, Q_a the full actual native Hermitian form, A_a its logarithmic Riesz operator, and K_a=ker A_a. On one dilation carrier write A(t), reserving a different name B_hist(t) for the historical monotone closed coefficient submodules. These are different objects.

P_0,N_0 are the complete actual positive/negative analyses. A finite actual coordinate projection gives R=Pi_s N_0. The effective background covariance is G_s=A+R*R, with effective positive synthesis S and compensator C_s=-S^{-1}R*. The finite response is D_s=I-R G_s^{-1}R*. All adjoints and inverses use the specified Hilbert metrics.

"Global domination" below means ||N_0 h||<=||P_0 h|| for every finite support window and every h in its actual domain. It is not a single uniform strictly positive constant across all windows, and not domination of only the unselected background.

"F4" has two uses that must remain separate. Historical RPB-67 F-4 is Gaussian-window logarithmic coercivity -> exponential Fourier weight, downstream of a support-gap upper pairing. The present global lane seeks the actual attachment and endpoint theorem needed to use that stack. Completing a conditional WD-T40 no-persistence theorem is not excluding first contact.

## Exact recovered interfaces

| Object or gate | Current custody | Remaining obligation |
| --- | --- | --- |
| Actual full native null h | Conditional on an actual nonnegative null window; canonical domain and complete samples attached | Exclude the window, or supply an independent lawful negative input if constructing it |
| Effective background G_s | Coercive for a finite selection separating K_a; coercive nearby | It is not null on h: G_s h=R*Rh and its quadratic is ||Rh||^2>0 |
| Fresh S,C_s,h packet | Actual construction; unit gain and physical adjoint on the same endpoint vector | Historical coefficient carrier/right-limit sequence and arithmetic fields are not inferred |
| Historical P,C,k packet | Generic Lean output; recovered scan found no actual constructor application | Actual realization map, prescribed selected rows/metric, and source identities |
| Full-native central cancellation | Holds on the endpoint interior for an actual full null h | Does not hold on a strict enlargement for the same nonzero h |
| Enlarged frozen-action cancellation | Explicit hcentral argument in NeutralInnerCollarRegularity.lean | Same-vector action/form dictionary plus an independent enlarged equation; inclusion is insufficient |
| All-window unit domination | Certified only on the fixed-aperture frontier | Global nonnegative-contact exclusion, as reduced below |
| Historical F-4 Gaussian lower bound | Standalone analytic theorem already in ACTUAL_MOVING_GAUSSIAN_COERCIVITY | Matching actual residual upper bound and exponential-weight deduction; lower bound alone does not complete F-4 |

Lean NeutralDefectMorphology additionally retains StrictMono phi, NeutralCriticalBranch, nonzero coefficient membership in rightLimit B_hist c, aLim=C uLim, unitGain, physicalAdjoint, physicalNull, named arithmetic integrability/identity fields, and extend k identified with the null-extension vector. Its constructor returns an unresolved persistenceGoal; it does not prove that goal.

The fresh LOCAL_FINITE_SOURCE_MATRIX sequence approaches contact from below. Neither its normalization nor its strong coefficient limits proves membership in an actual historical monotone B_hist(t), especially with the historical right-approach convention.

## Dependency graph

~~~mermaid
flowchart TD
  A["Actual source and native identities"] --> B["Nonnegative contact kernel"]
  P["Certified initial positivity"] --> E["Negative input implies first contact"]
  E --> B
  B --> C["Finite selection and effective realization"]
  C --> D["Local response and exact null reconstruction"]
  H["Historical packet and carrier compatibility"] --> T["Attached WD-T38 morphology"]
  C --> T
  B --> N["Independent contact exclusion"]
  N --> G["All-window domination"]
  B --> O["No same-vector enlarged full nullity"]
  T --> X["Enlarged central cancellation gate"]
  X --> U["Support-gap upper pairing"]
  L["Actual Gaussian lower bound"] --> F["F-4 exponential Fourier weight"]
  U --> F
~~~

N, H and X are unproved obligation nodes. Edges into them locate the required inputs or investigation; they are not claims that those obligations follow. In particular the edge into X is a required gate, not a proved implication from T. For an actual nonzero full-null vector, O obstructs X whenever the frozen action is identified with the enlarged full native equation. G cannot supply a nonzero kernel witness: the theorem below excludes such witnesses under G.

## New structural reduction: exhaustive global contact dichotomy

Fix a certified coercive starting window a0=91/100 (any certified starting interval suffices). The accumulated actual results imply exactly one of:

1. Q_a is strictly coercive in its logarithmic domain for every a>0; consequently full-negative unit domination holds at every window.
2. There is a finite first-contact c>a0, Q_c>=0 with K_c nonzero; every b>c admits a lawful actual negative vector.

Proof. If any negative vector exists, support inclusion puts one in a window larger than a0. The recovered norm-continuous I+compact constructor gives a nonnegative attained contact c. TRANSLATION_NULL_EXTENSION_OBSTRUCTION constructs a negative vector at every strict enlargement, not just at selected decimals.

If no negative vector exists, all Q_a are nonnegative. A nonzero null h at a would have the same physical vector and zero diagonal at b>a. Nonnegativity at b gives full mixed nullity by Hermitian Cauchy-Schwarz. Strict-margin translation rigidity contradicts that nullity. Thus every K_a is zero. A_a=I+compact and nonnegative, with zero kernel, is strictly coercive at that fixed window. Windows below a0 inherit the certified logarithmic lower bound by physical inclusion. This proves exhaustiveness and mutual exclusion.

Equivalently,
  [for all a, Q_a>=0]
  iff [for all a, Q_a>=0 implies K_a={0}],
given the recovered initial coercivity, continuity, Fredholm attainment and strict-margin obstruction. The reverse implication uses first contact from any hypothetical negative vector. Constants may depend on a.

This is a reduction, not a proof of either alternative. It identifies the smallest global theorem: exclude a nonzero full kernel at a nonnegative actual window. An endpoint-specific arithmetic constraint or sufficient global derivative invariance would do so. No new aperture certificate is required by the reduction.

## Retained attachment: exact compatibility obstruction

The actual construction cannot identify a prescribed historical packet by equations alone. For the prescribed rows, the smallest fixed-window inverse gate is
  ker A intersect ker R_hist={0}.
At a nonnegative Fredholm window this is equivalent to G_hist being coercive. A finite existential selection proves this gate for that selection only. The rational two-dimensional control below rejects its replacement by a blind prescribed selection.

Even this inverse gate does not attach the historical coefficient carrier. A concrete sufficient coordinate-compatibility theorem would supply Hilbert unitary identifications T of physical form carriers, U_+ of positive coefficient carriers, U_- of selected coefficient carriers with:
  T P_hist = S U_+,
  U_+ C_hist = C_s U_-,
  T k_hist = h,
and agreement of the physical L2 inclusion/zero extension and the selected actual source rows. These equations transport adjoints and unit gain because the identifications preserve the metrics. An arbitrary bounded isomorphism cannot be used to transport adjoints without the corresponding metric correction.

This is a sufficient precise comparison target, not a claim that unitary comparison is necessary for every possible realization. A direct same-domain mixed-form/synthesis identity is another lawful route. The remaining sequence theorem must independently attach the retained B_hist, right-limit membership and critical branch. Named density must equal the actual Fourier density and the scalar arithmetic form must agree on the common domain. No map or retained sequence was recovered that supplies these witnesses.

A fresh packet can replace the historical packet only in an additively stated actual morphology theorem whose sequence and coefficient-carrier hypotheses are proved. The existing local fresh sequence is not that theorem. Its fixed-window operator equations are already valid and need not be reopened.

## Endpoint attacks and their exact stopping points

1. Strict response monotonicity does not exclude zero. For t>0 take H=M=C, P_0=1, N_0=t, A=1-t^2, R=t, G=1, S=1, C_s=-t. Then D_s=1-t^2 is strictly decreasing, is positive initially and vanishes at t=1. At contact h=1,u=-1 give C_s u=S*h=1 and C_s*C_s u=u. Null reconstruction gives h=-G^{-1}R*u=1. All fixed-window effective identities and the sign/nullity reduction hold. This is an algebraic control, not an actual-zeta or nested-physical-domain counterexample. It falsifies exclusion from the finite algebra and Loewner order alone; actual translation rigidity is itself consistent with crossing.

2. Finite nullity plus derivative commutation does not put a derivative in D_a. Existing regularity gives H^s for s<1/2 and finite logarithmic weights, not global H^{1+epsilon}. The minimal sufficient regularity theorem is: every h in K_a has its global zero-extension derivative in D_a. This makes differentiation preserve the finite-dimensional kernel, and the recovered Fourier-polynomial independence excludes it. No such regularity theorem is proved here. Interior smoothness without global endpoint control is insufficient.

3. Supported-L2 domain promotion consumes the exact full interior equation. It supplies logarithmic membership and full mixed nullity, but does not enlarge the interval where the equation vanishes.

4. The single inverse-boundary moment remains noninjective on the general carrier. No inference from its zero value to h=0 is used.

5. A residual-Gram enclosure is a sign certificate only after actual selected rows, actual trial/source residual and a valid coercivity constant are supplied. Its existence as an algebraic mechanism is not an arithmetic sign input.

## Same-vector transport: obstruction sharpened to the typed central gate

Suppose a nonzero physical L2 h is supported in [-c,c], c<a, and the actual frozen compact action with cutoff a and its actual pole vanishes against every compact smooth test in (-a,a). Under the actual action/distribution dictionary this is precisely
  m_a(D)h+p_h=0 on (-a,a).
L2_NULL_DOMAIN_PROMOTION puts h in D_a and K_a. Strict-margin translation rigidity, applied to the unchanged support [-c,c], then contradicts h!=0.

Thus a nonzero actual realization cannot satisfy the enlarged hcentral field consumed by neutralExteriorIntegralGrowthResidual_realizes_of_central. Domain promotion removes the possible escape that h merely lacks prior logarithmic membership. This is an analytic deduction from the recovered actual dictionary; it is not a new Lean instantiation of that dictionary.

The unchanged vector is the global physical h. Physical support inclusion changes its Hilbert Riesz representation and source-domain setting; raw complete samples remain the same. Changing effective positive coefficient coordinates by the local unitary preserves the endpoint physical vector, but supplies no larger-window equation. Dilation U_t changes h physically and cannot discharge same-vector persistence.

For full null h at c, in a larger window a the scalar Q_a(h,h) remains zero while A_a h!=0. Effective background energy remains ||Rh||^2 when the selection is fixed; it is positive, not null. Central endpoint cancellation, enlarged cancellation, and selected-background cancellation therefore remain different assertions.

This obstruction blocks the proposed actual-contact -> same-vector enlarged-null -> support-gap F4 path. It does not invalidate conditional WD-T40, whose conclusion is exactly that enlarged persistence is impossible, and does not exclude contact itself.

## Shortest remaining route

Global lane: prove actual nonnegative-contact kernel exclusion. The structural dichotomy then gives global domination immediately. Historical attachment remains a separate named-witness claim; no nonzero attained endpoint would survive global exclusion.

Historical F-4 lane: the actual Gaussian lower estimate already exists. Closing its exponential-weight conclusion requires an actual upper pairing with exponential frequency decay. For a hypothetical strict-margin null extension the existing support-gap machinery is the conditional route; for a genuine endpoint residual, the upper estimate is independent and presently absent. Do not import the strict-gap upper bound for a residual with nonzero collar flux.

A sufficient new endpoint theorem could bound the genuine endpoint action on the moving Gaussian exponentially in R; paired with the existing lower estimate it would yield exponential moving Fourier mass. One must still prove the exponential-weight reconstruction and both frequency tails (or a lawful reflection argument), rather than declare strip holomorphy from a one-sided moving estimate. No such endpoint upper bound is obtained by this recovery.

## Validation and custody

This pass is analytic and documentation/control code only. No Lean module, workflow, external input or historical certificate is changed. No Lean compiler is installed in this execution workspace; no new Lean build or axiom audit is claimed. The reported prior certificates retain their own scope.

The accompanying exact-rational control checks the response crossing, endpoint signs and reconstruction, and the prescribed-selection coercivity failure; a deliberately false no-contact assertion and a blind-selection assertion are rejected. These are controls of failed implications, not arithmetic examples or RH evidence.

Every primary source below was read at the pinned recovery SHA:
- notes/REFLECTED_PACKET_BRIDGE_67_20260929.md (F-1 through F-6);
- docs/WEIL_DEFECT_MANUSCRIPT.md (WD-T40 conditional no-persistence scope);
- WeilDefect/Morphology/Neutral.lean and notes/LEAN_WD_T17_CERT_20260924.md;
- WeilDefect/Morphology/NeutralInnerCollarRegularity.lean and NeutralGaussianAssembly.lean;
- ACTUAL_FIRST_CONTACT_CONSTRUCTOR_20261004;
- FINITE_SELECTION_EFFECTIVE_POSITIVE_REALIZATION_20261006;
- LOCAL_FINITE_SOURCE_MATRIX_20261006 and FINITE_SOURCE_LOEWNER_20261006;
- DERIVATIVE_CHAIN_REGULARITY_CEILING_20261006 and L2_NULL_DOMAIN_PROMOTION_20261006;
- TRANSLATION_NULL_EXTENSION_OBSTRUCTION_20261004;
- ACTUAL_MOVING_GAUSSIAN_COERCIVITY_20261004;
- RETAINED_UNIT_GAIN_CUSTODY_20261004 and RETAINED_SOURCE_RECOVERY_20261003;
- INVERSE_MOMENT_OBSERVABILITY_AUDIT_20261005.

F4, global endpoint exclusion, historical retained attachment and FULL TRANSPORT CLOSED remain unclaimed. The lane cursor is the actual nonnegative-contact exclusion theorem or an independent genuine-residual Gaussian upper bound, not another aperture decimal.
