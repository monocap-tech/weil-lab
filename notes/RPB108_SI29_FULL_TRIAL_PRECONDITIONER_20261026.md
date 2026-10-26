# Original full-trial physical preconditioner (October 26, 2026)

W-ODD-NEG remains OPEN. This is original-operator inverse/preconditioner information for the SAME 470 original generators and 14 actual continuous SI29 features, conditional on the inherited Fourier/form-domain and coercivity hypotheses. It does not assemble or invert the original Astar matrix.

## GitHub custody and input

Base is draft PR #334, e8e3b6c9ca39ffcef13175a58be3d17d3c7fafa0. Focused negative-cluster run 40404177269 passed; its negative bound remains on the UNALIGNED physical residual only. No negative-action invariance under adding J is used.

Reuse original full-J physical projection from builder ab41a96861c9e5d0623807e40d53482985d143bc, successful Actions 40385192745, artifact 12679609974. Archive SHA256 243d40e1fc7d7ce349a0c16c809f06eea0593cd91635d6966241e4f5f478cf33; JSON SHA256 c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60. The workflow independently verifies run/source/artifact/archive/JSON custody before native calculation. Runtime: Python 3.12, python-flint 0.8.0, 4096 bits.

## Complete trial coordinates

Rebuild H=J*J from all 470 original physical generators using rigorous closed-form integrals. Construct a candidate exact dyadic D by midpoint Cholesky with rounding after EVERY candidate operation and midpoint of the triangular inverse. Candidate arithmetic does not certify anything. Verify D* H D against the ORIGINAL ball matrix by complete row-sum enclosure.

With exact real X=H^-1 J*F and accepted exact dyadic C, set

    Z = [J D, (F-J X) C].

Recompute H, J*F and F*F, and certify the entire 484x484 physical Gram, including all 470x14 cross terms, by complete row sums:

    (99/100) I <= Z*Z <= (101/100) I.

Native balls enclosing X define one exact real projection, not arbitrary independent entries. The calculation may lose correlations but is outward. Positivity of the full Gram proves that the coordinate map is injective; it spans the entire unchanged original augmented trial. Its exact dyadic J-transform is fingerprinted in the artifact and deterministically regenerated from the source and pinned runtime during replay. The certificate does not store an unchecked rounded Gram or use it as an Astar matrix.

## Uniform original energy bound

Enclose the FULL 484x484 physical derivative Gram and the entire endpoint row. Independent degree-255 entire Taylor derivative Grams check all first-cluster generators, the pole and all 14 actual continuous features, with explicit product-tail payments. This independently checks the Laurent/regularized-Si derivative formulas.

Let d be the outward trace bound for Zprime*Zprime and e the outward squared norm bound for Z(B). For every unit coefficient vector, variation squared is at most V=8e+4B d. One physical integration by parts, including BOTH endpoint jumps, gives |Fourier(Zy)(xi)|^2 <= V/(36 xi^2), using 2pi>6. This is a full-family operator bound through trace and endpoint-vector Cauchy, not a sum of separate diagonal positivity claims.

For R=2^k, ln R < (7/10)k. The original Ao majorants (36 below frequency 1, 17+ln|xi| above) and Parseval give

    Z* Astar Z <= Z* Ao Z
               <= [(101/100) max(36,17+7k/10)
                    + V (18+7k/10)/(18*2^k)] I.

The last term includes both signs of the infinite frequency tail. The ln2 bound is checked by the first five positive terms of exp(7/10)>2. All final optimization, outward endpoint extraction, log-split arithmetic, integer upper rounding and condition-number composition use exact Fractions. A separate standard-library checker replays those compositions.

Inherited Astar >= (33621/10^9) I implies

    Z* Astar Z >= (3328479/10^11) I.

The native output supplies the resulting explicit upper and inverse condition bound. No Astar entries are replaced by derivative entries: derivative data only prove a Loewner upper. The inverse inherits the reciprocal scalar enclosure; its entries and response are still uncomputed.

## What this changes and what remains

A future original Astar trial solve can target an explicitly certified physical preconditioner for the entire 484-dimensional space, rather than the catastrophically conditioned raw source coordinates. The accepted physical projection is reused; no new source direction or frequency quadrature is added. This also prevents interpreting the tiny raw Hermite residual scale as an unavoidable energy inversion singularity.

Actual Astar entries/projection, matched forcing, energy-projected negative action, the complete signed Schur/response, infinite operator transfer, and independent original analytic/domain review remain OPEN. The negative bound from PR #334 is not transported to these coordinates or the energy projection. W-ODD-NEG, even-sector obligations, CC27, Weil and RH remain OPEN. CI establishes only the declared enclosure/replay checks. This branch is draft/unmerged.
