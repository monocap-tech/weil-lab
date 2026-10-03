# RPB-108 — actual compact moments and pole source attachment
Date: 2026-10-03
Parent: 69c836c8e0203349f7abb01263a834fcf87976c4

## Concrete witness

The physical inclusion J_a is the already constructed inverse-weight/Fourier reconstruction restricted to the complete supported logarithmic Hilbert carrier.

A moment column e_(a,s) is the actual function exp(s x) on [-a,a], zero outside. Compactness proves its genuine L2 membership. Its L2 inner product with f is exactly the retained sourceWindowMoment a s f. The moment therefore becomes an actual continuous linear functional, constructed from this column rather than assumed to be a representation.

The form-space source column is J_a* e_(a,s). The adjoint identity proves its analysis coefficient on every form vector is the same compact-window moment of that vector's physical reconstruction. This is an actual same-domain source attachment with no spectral-domain hypothesis.

## Concrete Hermitian pole operator

Let b_- and b_+ be these source columns for s=-1/2 and s=1/2. Define

    K_a = rankOne(b_-,b_+) + rankOne(b_+,b_-).

For every f,g in the complete logarithmic carrier, the certified mixed identity is

    <f,K_a g> = conj(M_- f) M_+ g + conj(M_+ f) M_- g,

where M_s f is the retained sourceWindowMoment of the actual physical reconstruction. Its diagonal is

    <f,K_a f> = 2 Re(conj(M_- f) M_+ f).

These are precisely the pole terms in sourceDomainWeilForm and sourceDomainQuadratic. This attaches the actual pole component, not an arbitrary source form. The general complex pole is Hermitian and may have either sign; no nonnegative pole scalar or equality of the two moments is imposed. This does not identify WD-T38's independently supplied nonnegative pole scalar with this physical diagonal.

## Scope of the source witness

PROVED after validation: actual compact exponential columns in L2; continuity and exact integral realization of retained moments; their actual adjoint columns on the complete logarithmic form domain; concrete pole operator and same-domain mixed/diagonal attachment.

No source identity is added as a hypothesis. No physical carrier, null vector or compensator is substituted.

STILL WRITTEN / RETAINED: actual-zeta global upper sampling and the effective background endpoint reconstruction, including the full source diagonal extension, from b382eec and 6645b05.

OPEN: actual normalized multiplier attachment on the complete carrier; identify current WD-T38 P,C,k and h with this realization; attach full source quadratic/null law; obtain actual enlarged central cancellation. The pole component alone proves none of these.

Current-carrier spectral L2 remains unproved and unassumed. This construction uses compact L2 moment columns and form-space adjoints, not a logarithmic-energy-to-spectral-L2 upgrade. The existing certified inner-collar assembly still supplies regularity and consumes boundary removal as soon as actual enlarged central cancellation is attached.

Thresholds CLOSED; F-4 NOT STARTED; WD-T40/RH unchanged.

## Validation

Whole-root validation succeeded (9,024 jobs). Six public-declaration axiom audits each use only propext, Classical.choice and Quot.sound. The unfinished-declaration gate passed.

Validation commit: 0f4dffa9533a3a6e0dca505874754271703e2ddb
Validation tree: 9ce9762aa1ce08f279a8fb10c5f3271eef184d4d
Run: https://github.com/monocap-tech/weil-lab/actions/runs/37124525533
Job: 111207034718
Source blob: 331ad94a02336a124eb6c17e3ee94480694a8c5c
Root blob: d4ff7bcebb9962313da0518f717abb82a59dd45e

Separate promotion changes the two certified code files, this new note and four current status documents. All other Lean/manifests agree with the validation tree. Research workflow and historical notes remain unchanged.
