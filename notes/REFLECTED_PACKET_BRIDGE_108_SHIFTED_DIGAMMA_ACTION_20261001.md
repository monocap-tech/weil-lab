# RPB-108 — actual shifted digamma action and physical finite split

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `3d0347e1738b2d8abc776a0eb0a5af57e22c11e3`.

## Actual normalized tail

The new symbol is Re ψ(1/4+N+iπξ) - log π, complex-cast at
the fixed t=2πξ normalization. The proved finite digamma recurrence
identifies it exactly with the original archimedean symbol plus the
positive finite reciprocal symbol. This is the actual function, not a
replacement tail satisfying an assumed representation.

For each fixed N, temperate growth follows from the retained actual
full Weil-symbol growth premise, the proved prime growth, and the proved
finite Gauss growth. The original growth premise remains retained.
There is no additional shifted-tail premise and no uniform-in-N bound.

## Actual operator split

The existing distributional Fourier multiplier acts on every Schwartz
test through its transposed Schwartz map. Lawful additivity follows from
the two proved growth statements. The prior finite physical attachment
then gives exactly

    archimedean action = shifted digamma action - finite Gauss convolution pairing.

Combining the prior full prime attachment gives exactly

    whole core = shifted digamma action - finite Gauss convolution pairing
                 - actual finite prime pairing.

Both physical pairings genuinely converge by prior global L1 results.
The signs are inherited from the actual recurrence and full Weil symbol.
This is an equality for every finite N and every Schwartz test.

## Remaining obligations

The unidentified action is now the actual shifted digamma tail. A lawful
estimate and weak/operator limit on support-separated tests remain open.
Fixed-N temperate growth and pointwise off-diagonal kernel convergence
do not justify a whole-line singular Gauss integral or operator limit.
Local/contact contributions must be controlled before any limit claim.

Whole archimedean source attachment, central cancellation, boundary
reconstruction and actual source-domain/quadratic/polarization/normalized
estimate witnesses remain open. Threshold bookkeeping is closed;
logarithmic coercivity has not started. Canonical Weil, main and WD-T40
mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,967 build jobs passed. All four audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `b5539d09ef9c7661d5d512a1f24f4affc3333856`,
run `36962858435`, job `110700132811`, source blob
`3a769eee13cff80100c34b154e153d1bfe2d2d7f`.

Validation-only workflow/cache
changes are excluded from research promotion. Prior notes are immutable.
