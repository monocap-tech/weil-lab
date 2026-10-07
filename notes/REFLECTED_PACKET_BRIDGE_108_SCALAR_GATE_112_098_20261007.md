# RPB108: quantify the 96-vector gap and preflight 112 vectors at 49/50

The current 96-vector scalar Schur route cannot be repaired by ordinary frequency-cut optimization with the saved positive-region method. A stronger rational witness requires c>0.93317516, while the deeper prime estimate leaves that method's output ceiling below 0.854202. Separately, the 112-vector complement is now certified at 247/250=0.988. This is a preflight for a new construction, not whole-domain positivity. The certified whole-domain frontier remains 973/1000; F4 remains open.

## Stronger sign bracket on the unchanged 96-vector Gram

The complete audited Gram, native block and source are reused without changes. A decimal midpoint search at c=93/100 supplies a rational candidate; search arithmetic is not proof evidence. Exact rational quadratic enclosures, independently recomputed from 4656 triangular terms, certify

\[
v^*(Q-(100/93)R_{\rm actual})v<-9\times10^{-30}
\]

even after allowing the complete source perturbation in the direction favorable to positivity. The resulting necessary scalar complement bound is greater than 0.93317516. No actual negative Weil-form value is claimed.

At the hypothetical c=47/50, the corrected finite matrix Q-(50/47)R_surrogate-[(50/47)delta+10^-33]I has all 96 positive outward pivots at 160 digits. Two exact runs match byte for byte. An independently formed, widened 80-digit matrix with row-factor elimination also passes all 96 pivots and a negative-pivot control. The hypothetical complement is not proved; these checks establish a sufficient finite coupling target only.

## Deeper prime majorant and the method ceiling

Two fresh depth-ten constructions match byte for byte and improve the actual prime operator majorant from 1.899882 to 1.899459. The independent finer-log audit checks 2337 weight cells, 3101 refined cells, 2910 translated cut events and all 31010 signed transitions. Omitted-cut and smaller-majorant controls are rejected. This is an operator upper estimate; no actual operator lower norm is claimed.

For the 96-moment positive-region method, every admissible cutoff T satisfies (2a pi T)^2<96*97. A rational Machin enclosure proves T<157/10. Each monotone band lower estimate, with the fixed depth-ten prime loss, is at most log(157/10)-1.899459, before subtracting its nonnegative mass and pole penalties. A finer independent Machin/log audit places that ceiling below 0.854202, far below the necessary 0.93317516. The ceiling concerns this lower-bound method, not the actual complement. More precision, more bands within that region, or rounding cannot close this gap.

## 112-vector construction preflight

Projecting away degrees 0 through 111 gives a different complement subspace. With the same aperture and prime powers 2,3,4,5,7, depth-six Bessel damping at cutoffs 16,17,18 proves

\[
c_{112}\ge247/250=0.988,
\]

with unrounded lower estimate approximately 0.9886124780930549. Two fresh complete preflight runs match byte for byte. The independent audit verifies all 144 retained degree-mass terms, all three infinite tails, all four pointwise band regions and finer endpoint logarithms; two invalid positive regions are rejected.

The degree-111 native diagonal truncation budget fails the required threshold at orders 300/300 and passes at orders 360/360, with width approximately 3.422639e-49. Remainder ceilings 51 and 49/10 remain valid at this aperture. This verifies the highest diagonal budget only. A complete 112-row native construction, finite sign, fresh 112-column source-error budget, all eleven source panels per column, complete residual Gram and corrected coupling sign remain pending.

The 96-vector conditional c=0.94 result cannot be transferred to the new subspace: its finite block and residual Gram have changed. The larger complement makes 112 vectors a concrete next construction target, without certifying its final sign in advance.

## Custody and reproduction

The accompanying custody manifest binds all scripts, outputs, unchanged arithmetic dependencies and the compressed/decoded depth-ten prime certificate. Restore the prime archive with `scripts/restore_native_prime7_scalar_gate_098_archive.py`; the prior complete 96-vector Gram restore remains unchanged. Run the stronger-obstruction constructor and validator, conditional constructor and widened validator, scalar-method ceiling constructor and validator, and 112-vector preflight constructor and validator. The latter's degree-111 width audit uses direct binomial endpoint integration independently of the constructor's correlation routine.

No whole-domain positivity at 49/50, global endpoint exclusion, F4, full transport, Lean formalization or RH closure is claimed. Historical aperture certificates and concurrent global work are preserved.
