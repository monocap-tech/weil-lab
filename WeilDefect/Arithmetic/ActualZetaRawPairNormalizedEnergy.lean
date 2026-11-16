import WeilDefect.Arithmetic.ActualZetaRawSamplesToFullSourceGraph
import WeilDefect.Arithmetic.ActualZetaHilbertSourceGraph

namespace WeilDefect
noncomputable section
open InnerProductSpace

/-!
NF537: genuine complete-divisor P/N normalization, for arbitrary ℓ²
raw sample families. This is HILBERT ALGEBRA, not a Green-identity
assumption or a RH/positivity assertion. Every coordinate remains in
the existing NeutralActualZetaGreenCoefficients space.
-/

/-- Exact normalized signed two-source energy equals the real Hilbert
cross term of the two original raw zero sample families.

The FIRST sqrt(2) comes from the raw P/N pair, and the SECOND is the
existing actual full-divisor normalization that pays the double count.
Neither factor may be suppressed. -/
theorem neutralActualZetaRawPair_normalizedPN_energy
    (A B : NeutralActualZetaGreenCoefficients) :
    ‖neutralActualZetaSourceNormalization •
      (neutralActualZetaSourceNormalization • (A + B))‖ ^ 2 -
    ‖neutralActualZetaSourceNormalization •
      (neutralActualZetaSourceNormalization • (A - B))‖ ^ 2 =
    (inner ℂ A B).re := by
  let c := neutralActualZetaSourceNormalization
  have hsmul (v : NeutralActualZetaGreenCoefficients) :
      ‖c • (c • v)‖ ^ 2 = (‖c‖ ^ 2) ^ 2 * ‖v‖ ^ 2 := by
    simp only [norm_smul]
    ring
  change ‖c • (c • (A + B))‖ ^ 2 -
    ‖c • (c • (A - B))‖ ^ 2 = (inner ℂ A B).re
  rw [hsmul, hsmul]
  have hc : ‖c‖ ^ 2 = (1 / 2 : ℝ) :=
    neutralActualZetaSourceNormalization_norm_sq
  rw [hc, norm_add_sq (𝕜 := ℂ) A B,
      norm_sub_sq (𝕜 := ℂ) A B]
  ring

end
end WeilDefect
