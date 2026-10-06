# RPB-108: complete residual Gram and depth-six estimator obstruction at 23/25

The aperture is a=23/25. Q is the certified native restriction on the 84
physical orthonormal Legendre vectors of degrees 0–83. R is the complete
residual Gram surrogate after all 84 retained projection components are
removed. The source-map approximation bound is eta, and its actual Gram
operator error bound is delta=eta(2M+eta), where M bounds the surrogate
residual source map norm. The scalar c=626973/1000000 is the certified
complete-complement lower bound; beta=1/c. The sufficient scalar Schur
estimator is Q-beta R, with delta used to transfer R to the actual residual
Gram. Definitions are retained in `docs/TERMINOLOGY_RPB108_GRAM_STAGE_092.md`.

The complete residual Gram export and its repeat are byte identical,
SHA-256 `1cc913aa44fffdd21a85084aab5cf543d72089f91fcbafd21cb8b6c7c95bed54`.
It retains all nine panels, all mixed terms and all 84 projection components.
Its maximum residual entry width is approximately 3.041949685829048e-114;
M is approximately 5.498299532627936, and delta approximately
1.634358599206149e-35. All 7,056 native/source pairings pass and the complete
contraction checkpoint and independent pairing audit repeat exactly.

The export runs the unchanged constructor through complete residual
assembly and observes its result at the first sign call. Its caller and
matrix identity checks pass. No earlier numerical operation is changed;
all original checkpoint bindings remain intact. The export explicitly
leaves corrected sign pending and supplies no whole-domain positivity.

The separate 160-digit depth-six positive-pivot check fails. A 120-digit
Decimal LDL search then generates a rational candidate vector on grid
10^-40. Decimal arithmetic contributes no proof evidence: the stored vector
is checked by outward 160-digit interval arithmetic against the pinned
complete Gram, native, source and complement certificates.

For that rational vector, the actual scalar estimator has Rayleigh upper
bound approximately -6.229045910393781e-21 after the Gram approximation
allowance is included. The same vector's native Rayleigh lower bound is
approximately +3.485188273002293e-19. A coordinate direction with a positive
upper value is rejected as a negative-estimator control. The obstruction
certificate repeats byte for byte.

An independent validator uses exact rational signed endpoint sums, without
an interval class or a candidate search. It checks 14,112 quadratic terms,
recomputes delta and its trace/norm budget, verifies positive native energy,
and obtains a negative estimator upper bound at least as strong as the
stored outward bound. The validator and its repeat are byte identical.

This direction forces the scalar complement bound needed by this sufficient
estimator above approximately 0.6381788324992956, whereas the available bound
is 0.626973. This is a proved failure of the present scalar sufficient
estimate. It is not an actual negative witness for the full native form,
nor a proof that the actual complement cannot have a stronger lower bound.
The next aperture frontier is a stronger certified complement or a revised
retained-space/coupling estimate at 23/25.

The native finite restriction, source approximation and complete residual
Gram are accepted at this aperture. Whole-domain positivity remains
certified through 91/100 only. F4, full transport, global endpoint exclusion
and historical attachment remain open. Separate global-lane results are
preserved. Lean and workflows are unchanged.

## Custody

- `notes/data/RPB108_PRIME5_GRAM84_092_CERTIFICATE_20261006.json`
- `notes/data/RPB108_PRIME5_DEPTH6_OBSTRUCTION_092_CERTIFICATE_20261006.json`
- `notes/data/RPB108_PRIME5_DEPTH6_OBSTRUCTION_092_VALIDATION_20261006.json`
- `scripts/certify_native_prime5_depth6_obstruction_092.py`
- `scripts/validate_native_prime5_depth6_obstruction_092.py`

The preceding complete panel checkpoint and pairing audit remain unchanged
in `REFLECTED_PACKET_BRIDGE_108_COMPLETE_PANELS_092_20261006.md`.
