# RPB-108 — WD-T38 witness attachment audit

Recovered live research head: `a212c087ae269a27e17f7b715531caaa95b37088`.
Cursor: RPB-108 / WD-T40 F-4 — WITNESS ATTACHMENT.
This is a source-custody and dependency audit, not a new Lean theorem certificate.

## Determination

No actual source witness has been attached in this pass. The historical
WD-T38 statement retains the required carrier/source identification as a
mathematical hypothesis, but the live Lean constructor does not carry its
concrete identifications. Naming the constructed form or adding another
constructor consuming its identity would not supply the missing witness.

The six audited source files were checked by Git blob hash against the live
research tree `ba6e6eb5e0a0813754b914d8031d32923818426c`.
The repository search found no application of
`wd_t38_attained_unit_gain_neutral_morphology` outside its definition and
no source witness instance connecting it to the concrete Fourier carrier.

## Witness custody

| Obligation | Retained mathematical data | Live Lean data and result |
| --- | --- | --- |
| Actual carrier in logarithmic form domain | docs/NEUTRAL_DEFECT_MORPHOLOGY.md §2 and composite hypothesis 8 require source membership | NeutralPhysicalFourierCarrier has L2 and support, but no log-energy field. WD-T38 takes hlog_int for an independent density. No density identification is returned. NOT ATTACHED. |
| Actual source quadratic identity | Same compact-window form/operator realization is retained in hypothesis 8 | WD-T38 takes scalar hQ for independent Q, symbol and density. No source sesquilinear form or all-vector diagonal identity on the concrete domain is returned. NOT ATTACHED. |
| Endpoint null identity | Physical null and endpoint restriction null are retained | physicalNull and endpointInteriorNull are proved/retained for abstract operators. No equality to the concrete multiplier-plus-pole action is supplied. ABSTRACT NULL ONLY. |
| Mixed identity | Same-domain polarization is already certified | sourceDomainWeilForm_eq_of_sourceQuadratic needs the source diagonal for every vector in that same domain. Zero of one carrier diagonal is insufficient. CONDITIONAL BRIDGE ONLY. |
| Normalized shifted comparison | WD-T38 takes pointwise comparisons and scalar form comparison | No symbol = rightLimitCompactWeilSymbolMathlib identification or source-coordinate transport is returned. Existing normalized comparison bridges consume such identified inputs. NOT ATTACHED. |
| Enlarged central cancellation | Strict persistence is the contradiction hypothesis in WD-T40 | Endpoint nullity concerns (-c,c). Cancellation on (-a,a), a > c, is not an endpoint consequence; persistenceGoal is deliberately unresolved. NOT PROVED. |
| Global spectral L2 product | Not part of WD-T38 form-domain membership | No squared-symbol energy hypothesis or derivation is present. NOT ESTABLISHED; not assumed in this pass. |
| Locally integrable actual defect | Sufficient for certified 592eaf7 boundary removal | Actual function/pairing representation is not supplied by the abstract null interface. NOT CONSTRUCTED. |
| Whole compact weak realization | Existing theorem consumes regularity plus enlarged cancellation | Neither required actual witness is available. NOT INVOKED. |

## Exact missing identifications

In `WeilDefect/Morphology/Neutral.lean`, the constructor
`wd_t38_attained_unit_gain_neutral_morphology` accepts:

- `hlog_int` for `logarithmicFourierWeight * density`;
- `hlower` and `hupper` for an arbitrary `symbol`;
- `hQ` for an arbitrary scalar `Q` and `pole`;
- `hendpointExt` for abstract bounded operators and restrictions.

It does not accept or return equations identifying these with the exact
physical carrier, Fourier normalization, concrete source quadratic, or compact
test action. Its output `NeutralArithmeticMorphology` records the resulting
numerical order inequalities, not the input integrability witnesses or those
missing equations. `nullExtensionVector` links the abstract extended vector
to `extend k`; the concrete Fourier carrier separately links its interface
vector to its L2 representative. Neither link identifies the source form.

The lawful next source reconstruction must preserve the original retained
hypothesis and expose its actual domain, carrier inclusion, source form and
identification with the endpoint realization. It must then identify its
diagonal with the normalized multiplier-plus-pole diagonal on every vector
where the source formula is valid. Existing polarization applies on this
retained domain. Containment in the canonical logarithmic domain does not
authorize extending a source identity to every member of the larger domain.

The WD-T35/38 scalar order theorem also uses a nonnegative pole premise.
The full complex Hermitian pole cross term need not be nonnegative. That
premise cannot be transferred to the full complex canonical domain without
a lawful parity restriction or a separately proved bound/shift.

## Endpoint versus enlarged nullity

The retained endpoint equation is
`P_[-c,c] W_endpoint kExt = 0`. After actual source attachment this can
supply compact-test cancellation in the endpoint interior.

It does not give
`frozenWeilCompactAction carrier a hSymbol u hu = 0` for every compact
test in `(-a,a)` when `c < a`. WD-T38's `persistenceGoal` deliberately
has no proof. WD-T40 excludes precisely the strict enlarged null equation,
so deriving it unconditionally from endpoint nullity would reverse the
logical role of the contradiction hypothesis.

For WD-T40 assembly, enlarged cancellation must be obtained by translating
a retained strict-persistence assumption through the same source/observation
identification. The historical WD-T38 hypothesis list alone does not assert
that strict persistence occurs. At the endpoint, retain the already certified
threshold conversion; do not replace the strict source operator by the
right-limit operator without that conversion.

## Spectral regularity route: stopped

Logarithmic form energy controls one logarithmic weight. Spectral-product
L2 membership controls the square of the symbol, hence roughly two
logarithmic weights at high frequency. The scalar retained estimates do
not close this gap.

For a simple frequency-only illustration, on xi >= e take
rho(xi) = 1 / (xi * log(xi)^3), zero elsewhere. Its mass and
one-logarithm weighted mass converge, whereas its two-logarithm weighted
mass diverges, by the substitution s = log(xi). This is not a compactly
supported physical null-mode counterexample. It demonstrates why the
weight comparison itself cannot upgrade form energy to spectral L2.
Additional consequences of a correctly attached null equation remain to be
investigated; non-derivability for that fully identified particular mode is
not proved by this audit.

Thus spectral membership is NOT genuinely derived from WD-T38 in the
current branch. The stronger route is stopped, rather than promoted by
adding membership as a new hypothesis.

## Weakest regularity route to investigate

Keep the target of 592eaf7: a locally integrable representative of the actual
compact source defect, with equality on all compact Schwartz tests. A
pointwise exponential bound or global spectral L2 output is unnecessary.

If enlarged distributional cancellation is attached under strict persistence,
the actual source action is zero on the enlarged central open set. Away from
the physical support [-c,c], the already certified gap-kernel, finite-prime
and pole ingredients offer local function representatives. Choose c < b < a
and seek an open-cover gluing argument: central zero on (-a,a), local
off-support representation on the outside of [-b,b], with overlap. This
would address the former boundary points ±a through neighborhoods disjoint
from the carrier support, without a form-to-operator-domain upgrade.

This is the selected investigation route, not a proved gluing theorem or a
claimed regularity witness. It should reuse the existing exterior results,
keep the target prime cutoff fixed, and prove compact-test equality during
localization. It must not identify the zero-continued candidate globally
before that equality is proved.

## Next work and standing

1. Reconstruct the concrete source-identification data omitted by the WD-T38
   Lean adapter, beginning with the actual source domain and carrier inclusion.
2. Apply the already certified diagonal/polarization and normalized comparison
   bridges on the lawful same domain.
3. Translate endpoint nullity on the endpoint window; separately translate
   strict persistence on the enlarged window when assembling the contradiction.
4. Seek local defect regularity using the existing off-support representation.
5. Consume 592eaf7 immediately when regularity and enlarged cancellation are
   both actual attached witnesses.
6. Only then mark source attachment closed and enter logarithmic Gaussian
   coercivity.

No additional conditional representation module, spectral membership
assumption, or new axiom was added. No theorem build was required for this
documentation-only audit. The latest source certificate remains a212c087:
8,987 jobs and five standard-axiom endpoint audits.

Threshold bookkeeping: CLOSED.
Actual source-domain/quadratic/polarization/normalized attachment: OPEN.
Actual enlarged central cancellation: OPEN / needs correctly identified
strict-persistence input for the contradiction.
Actual regularity and whole compact realization: OPEN.
F-4 logarithmic Gaussian coercivity: NOT STARTED.
