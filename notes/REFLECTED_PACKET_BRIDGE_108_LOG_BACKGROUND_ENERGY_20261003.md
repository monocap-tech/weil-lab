# RPB-108 — actual background logarithmic energy estimate

Continues from `8b332c1a212212a5c809812d50a99cfc1a256861`.
This pass certifies an actual lower energy estimate with a physical L2
correction, as needed before completing the retained background source model.
It does not assert strict coercivity, current WD-T38 source attachment, or
F-4 logarithmic Gaussian coercivity.

## Constants and domain

Write `f_phys=neutralLogPhysical f.val` for physical reconstruction of a
vector of the already complete supported logarithmic Hilbert carrier.
Its form norm is the actual one-log Fourier energy.

The actual pole error constant is
`K_a = ‖neutralMomentColumnL2 a (-1/2)‖² +
‖neutralMomentColumnL2 a (1/2)‖²`.
These are the two previously constructed compact exponential L2 columns.
The constant is nonnegative and finite by that concrete construction.
It is not an identification of WD-T38's independent scalar poleC.

Here the logarithmic lower estimate, also called a Garding estimate, means
the explicit inequality below with a physical L2 correction. It does not
mean positivity in the logarithmic norm.

## Actual pole and exact physical shift

For every physical L2 vector, the compact moment squared is bounded by the
column norm squared times the physical vector norm squared. This is ordinary
L2 Cauchy-Schwarz through the certified column pairing.

The actual Hermitian pole obeys
`|2*Re(conj(M_- f_phys)*M_+ f_phys)| ≤ K_a*‖f_phys‖₂²`.
Both signs are controlled. No nonnegativity of the complex cross-pole is
assumed.

The retained normalized symbol shift is attached exactly:
`∫(m_a+shift)*|FT f_phys|² =
∫m_a*|FT f_phys|² + shift*‖f_phys‖₂²`.
Genuine signed integrability is consumed from the preceding module.
The mass equality uses ordinary L2 Plancherel in the pinned normalized
Fourier convention. It does not require m_a*FT f_phys in L2.

## Certified lower estimates

Combining the retained shifted lower comparison with the actual pole bound
gives, for every vector on this same domain,

`lowerC*‖f‖log² ≤ Q_full[f] + (shift+K_a)*‖f_phys‖₂²`.

The concrete finite selected addition is nonnegative, so the same bound holds
for the explicit background expression:

`lowerC*‖f‖log² ≤ Q_B[f] + (shift+K_a)*‖f_phys‖₂²`.

Here Q_full and Q_B are real parts of the pairings with the actual operators
already constructed, with their certified physical quadratic expressions.
No new representation-equality or background-positivity field is added.
The coefficient shift+K_a need not be nonnegative; the stated signed correction
is the exact one supplied by the proof.

The normalized symbol continuity and comparison are still explicit retained
inputs. This module does not prove their actual source instance. In particular,
the interface only assumes lowerC>=0, not lowerC>0, and this bound alone does
not prove equivalence with a strictly positive background norm.

## Witness standing and next cursor

**Proved:** actual physical L2 mass formula; compact moment squared bounds;
nonnegative concrete pole constant; two-sided absolute control of the actual
Hermitian pole; exact physical L2 shift; actual full/background logarithmic
lower estimates with physical L2 correction.

**Retained/written:** actual-zeta source and packet assignment, global
sampling, native Green/core explicit-formula transport, and the strict
effective background realization. Equality of that realization with this
specific concrete expression and its current source vector is still OPEN.

Next: attach the retained native Green-core/source identity to the concrete
same-domain background. Once strict background positivity is identified,
the actual energy estimate can support absorption of the physical L2 error
and lawful completion in the background norm. The retained native identity
must be proved, not replaced by an assumed representation field.

Current-carrier logarithmic-energy custody and WD-T38 source/quadratic/null
identification remain OPEN, as does fixed physical enlarged central
cancellation for every compact Schwartz test in (-a,a).

**Spectral L2:** not derived from WD-T38 and unassumed. Ordinary L2 Plancherel,
finite compact column bounds, and one-log form energy do not provide
squared-multiplier spectral membership.

Immediately consume the existing inner-collar/locally-integrable defect,
boundary-removal and whole compact weak realization once actual enlarged
central cancellation is available. Exterior/digamma/boundary work remains
closed. Threshold bookkeeping CLOSED; F-4 NOT STARTED; WD-T40/RH unchanged.

## Validation

Certified validation head: `517eb90dae857977e26e89560f027d817ac78abe`.
Run: `37131988362`; job: `111228747667`.
Whole-root `lake build WeilDefect`: 9,028 jobs succeeded.
Seven axiom audits contain only `propext`, `Classical.choice`, and `Quot.sound`.
The unfinished/project-axiom declaration gate passed.
New module blob: `77112d87bad6633ce59690df69a212399bf45e63`.
Root import blob: `886b83d752fbd32f56881bdcadf805594fe2f933`.
The validation-only workflow is excluded from research promotion.
