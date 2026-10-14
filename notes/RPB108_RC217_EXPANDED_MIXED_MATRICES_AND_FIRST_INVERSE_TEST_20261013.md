# RC217 — expanded mixed matrices and first inverse test

Parent: RC216 `58119a94295f3bfe1b1f4cf5197d1049f08c4aa5`.

RC217 assembles compatible full source, canonical mixed, and nominal action-Gram entry enclosures for ten trial vectors: the eight existing RC203 trials, the native difference delta = z_b6 − v10, and native t10. All 20 new mixed/action rows are supplied. Pairings are summed through degree **65534**, and all signed infinite tails are paid. The existing eight-trial nominal action block reproduces RC203 exactly.

## Source identity and carrier compatibility

Every native t10 finite center and generator radius through degree 16382 is reconstructed, and the full historical RC135 hash is reproduced. The full native difference hash is also reproduced. These are the unchanged historical native sources, not new finite approximations.

The difference action is RC214's complete carrier; the t10 action is RC216's refined carrier. On the native z source, the compatible represented action is the old v action plus the difference action. The old RC211 z action and old RC212 t10 action are not assigned the new error radii.

For each new source/action row, both orientations are enclosed independently and their self-adjoint canonical intervals are intersected. Nominal action pairings pay signed tail products on both sides; actual-action error payments are recorded separately. This avoids confusing an action approximation Gram with the actual operator Gram.

## Eight-source frame

The inverse response is reported in the conditioned order [P0, P2, f0, psi0, w14, v10, delta, t10]. An explicit invertible matrix maps this to RC213's original native-plus-P2 source frame. The source span is unchanged by this coordinate transformation. RC213's rigorous source Gram floor and upper bound are transported by exact congruence. Independence of all ten trial vectors is not assumed.

## First inverse enclosure — not accepted

The first trial uses a source-span variational lower bound and a spectral-chord upper bound. For a I <= M <= 2 I, with the inherited metric a = 32125/230953, the chord is

    M^-1 <= ((a+2) I − M)/(2a).

The variational lower bound follows from Q(f) >= 2 Re<f,u> − <u,Mu> for the selected source-span trial u. All Gram uncertainty is transported with exact Loewner bounds and rational PSD checks.

Neither this entrywise variational/chord approach nor its combinations improve the broad global spectral fallback. The selected valid inverse enclosure has relative width **12.263225**, exceeding the half-Gram threshold **0.5**. Its lower and upper bounds, gate matrix, and evaluated candidates are stored in the certificate.

This is **not** a lower bound on the true inverse uncertainty or evidence that the actual inverse gate is impossible. It is a failed precision test of this first conservative enclosure. The main new result is the compatible expanded matrix assembly; no inverse-width improvement is claimed. The next refinement must combine the residual and shared action errors before payment, rather than reuse this broad entrywise enclosure.

## Validation and retained results

Normal execution and full reversed-order replay agree exactly. All 79 immutable certificate/helper pins match the live parent tree; a wrong input pin is rejected before reconstruction. Publication is add-only.

The RC216 correlated eight-source action-error gate remains passed at **0.420465**, with margin **0.079535**. The accepted RC210 six-source inverse width stays **0.436100**. That six-source result is not directly comparable to the expanded eight-source width because the source family has changed.

The finite eight-response residual Gram and its ten-trial coupled error transport remain unassembled. Expanded inverse acceptance, source-range/augmentation obligations, odd coverage, Stage I, RH, F4, and Lean closure remain open.

Next cursor: RC218 — assemble the ten-trial/eight-response residual and coupled error transport, then refine the expanded inverse enclosure.
