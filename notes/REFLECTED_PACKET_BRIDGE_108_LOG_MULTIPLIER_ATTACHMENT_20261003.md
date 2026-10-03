# RPB-108 — actual normalized multiplier-plus-pole attachment

Continues from `a28a1cc6fabf0f50c0c205558a8932e66ea75b2e` on `research/reflected-packet-bridge`.
Threshold bookkeeping remains closed. This is a concrete form construction;
it does not assert that the retained WD-T38 source identity has already been
identified with this form.

## Concrete carrier and terminology

Let (w(ξ)=\log(e+|ξ|)). The already certified
`NeutralLogHilbertCarrier a` is the closed supported subspace in weighted
Fourier L2 coordinates. Its physical reconstruction is `neutralLogPhysical`;
its squared Hilbert norm equals the physical logarithmic Fourier energy.
The exact canonical supported form domain was identified in the preceding
carrier checkpoint.

Write (m_a) for `rightLimitCompactWeilSymbolMathlib a`.
The retained normalized comparison is
`lowerC*w ≤ m_a+shift ≤ upperC*w`, with `0 ≤ lowerC`.
The symbol continuity premise and these comparison bounds are explicit
retained inputs. They are not proved here or replaced by a new representation
premise.

Here a **form operator** means a bounded Riesz realization in the logarithmic
Hilbert norm. It does not mean the unbounded physical spectral operator is
defined on every form vector.

## Actual construction

The new module `NeutralLogMultiplierSourceAttachment.lean` constructs
pointwise multiplication by the actual ratio (m_a/w) on weighted Fourier
L2. The retained comparison proves the ratio bound
`|m_a/w| ≤ |upperC|+|shift|`.

If (j_a) is inclusion of the closed supported weighted subspace, the concrete
multiplier form operator is (j_a^* M_{m_a/w} j_a).
Its mixed pairing is exactly the physical integral
`∫ conj(FT f) * m_a * FT g`. The factor (w) from the weighted inner product
cancels the denominator. Absolute signed energy and mixed integrability
are proved, so this integral is genuinely convergent.

Adding the preceding certified two-column pole operator produces
`neutralLogWeilFormOperator`. Its mixed identity is exactly multiplier plus
the Hermitian compact-moment cross terms. Its diagonal is the actual real
signed multiplier integral plus
`2*Re(conj(M_- f)*M_+ f)`.
This is the concrete expression used by `sourceDomainQuadratic` and the
existing diagonal/polarization bridges. No new `hrep`, source-equality,
positivity-of-pole, or spectral-domain field is assumed.

The retained normalized shifted comparison is also attached to every actual
form vector: the integral of `(m_a+shift)*|FT f|²` lies between
`lowerC*‖f‖log²` and `upperC*‖f‖log²`.
The constant shift contributes physical L2 energy, not logarithmic energy.
This does not certify every retained EXT5 estimate or Gaussian coercivity.

## Witness standing and next cursor

**Proved:** complete supported logarithmic carrier; actual moment and pole
attachment; actual bounded normalized multiplier construction; genuine
absolute/signed/mixed integrability; full same-domain mixed and real diagonal
identities; transfer of the retained normalized comparison to actual form
energy.

**Retained inputs:** normalized symbol continuity and lower/upper shifted
comparison. Actual-zeta sampling and effective background endpoint attachment
remain written/retained, rather than certified by this module.

**Still unattached:** the current WD-T38 carrier's logarithmic-energy custody,
its identification with the native completed source vector, and its retained
quadratic/null witness as this specific actual multiplier-plus-pole form.
The new concrete operator does not establish that identification merely by
existing. The previously certified source-witness independence audit remains
load-bearing.

**Central cancellation:** open for every compact Schwartz test supported in
`(-a,a)`. No enlarged cancellation follows solely from the construction.

**Spectral L2:** genuinely unproved from WD-T38, and unassumed throughout.
One-log form energy is not silently upgraded to squared-multiplier L2.
Bounded multiplication by `m_a/w` in weighted coordinates does not prove
`MemLp (neutralWeilSpectralProduct carrier a) 2`.

The weak regularity route is already available: as soon as actual enlarged
central cancellation is proved, immediately consume
`neutralExteriorIntegralGrowthResidual_realizes_of_central` and its
inner-collar regularity/boundary-removal assembly. No exterior, digamma, or
boundary work is reopened here.

Next: attach the actual WD-T38 source vector and null identity to this
specific form, then use the existing same-domain polarization bridge and
derive enlarged central cancellation. F-4 logarithmic Gaussian coercivity
has not started. WD-T40/RH standing is unchanged.

## Validation

Certified validation head: `696acc4ce502fb7b48b803b4568d6115ff60d7f0`.
Run: `37126512016`; job: `111212760495`.
Whole-root `lake build WeilDefect`: 9,025 jobs succeeded.
Ten axiom audits contain only `propext`, `Classical.choice`, and `Quot.sound`.
The unfinished/project-axiom declaration gate passed.
New module blob: `170c31cc3c09cd63c0aeb372f800043ad8a3cc4a`.
Root import blob: `a2fcf2016fe70c71657041c1c185088a528b0c8c`.
The validation-only workflow is excluded from research promotion.
