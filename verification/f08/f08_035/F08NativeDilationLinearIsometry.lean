import WeilDefect.Generated.F08.NativeFrequencyDilationIsometry

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal

/-!
F08-035: the genuine original RealComplexL2 dilation is complex linear,
and its exact norm preservation gives a native LinearIsometry.

The measure-transfer lemma is essential: an L² a.e. equality under
original volume cannot be evaluated at λ ξ until it has been transported
to the true pushforward frequency measure. No surrogate raw-function
operator or unjustified substitution of a.e. representatives is used.

The final approximation bound is the Banach-space reduction for proving
strong continuity on all native L² vectors from a truly dense core.
It does NOT prove strong continuity on that core, the log-form core,
original Weil pairing, F42, or RH.
-/

/-- Correctly transport a physical-volume a.e. equality through nonzero
frequency scaling, using the exact original pushforward measure. -/
theorem f08_035_ae_scale (lam : ℝ) (hlam : lam ≠ 0)
    {f g : ℝ → ℂ} (hfg : f =ᵐ[volume] g) :
    (fun ξ => f (lam * ξ)) =ᵐ[volume] fun ξ => g (lam * ξ) := by
  have hscaled : f =ᵐ[f08_027_scaledFrequencyMeasure lam] g := by
    rw [f08_027_scaledFrequencyMeasure_jacobian lam hlam]
    exact Measure.ae_smul_measure hfg _
  simpa only [Function.comp_def] using
    (f08_027_scale_measurePreserving lam).quasiMeasurePreserving.ae_eq_comp hscaled

/-- The genuine same-volume L² dilation is additive on equivalence
classes. This is not asserted pointwise on arbitrary representatives. -/
theorem f08_035_nativeFrequencyDilation_add
    (lam : ℝ) (hlam : lam ≠ 0) (k l : RealComplexL2) :
    f08_030_nativeFrequencyDilation lam hlam (k + l) =
      f08_030_nativeFrequencyDilation lam hlam k +
        f08_030_nativeFrequencyDilation lam hlam l := by
  apply Lp.ext_iff.mpr
  filter_upwards [
    f08_030_nativeFrequencyDilation_ae lam hlam (k + l),
    f08_035_ae_scale lam hlam (Lp.coeFn_add k l),
    f08_030_nativeFrequencyDilation_ae lam hlam k,
    f08_030_nativeFrequencyDilation_ae lam hlam l,
    Lp.coeFn_add (f08_030_nativeFrequencyDilation lam hlam k)
      (f08_030_nativeFrequencyDilation lam hlam l)
  ] with ξ hleft hscaled hk hl hright
  calc
    (f08_030_nativeFrequencyDilation lam hlam (k + l) : ℝ → ℂ) ξ =
        (Complex.ofReal (Real.sqrt (abs lam))) • (k + l) (lam * ξ) := hleft
    _ = (Complex.ofReal (Real.sqrt (abs lam))) •
          (k (lam * ξ) + l (lam * ξ)) := by rw [hscaled]
    _ = (Complex.ofReal (Real.sqrt (abs lam))) • k (lam * ξ) +
          (Complex.ofReal (Real.sqrt (abs lam))) • l (lam * ξ) := smul_add _ _ _
    _ = (f08_030_nativeFrequencyDilation lam hlam k : ℝ → ℂ) ξ +
          (f08_030_nativeFrequencyDilation lam hlam l : ℝ → ℂ) ξ := by rw [hk, hl]
    _ = ((f08_030_nativeFrequencyDilation lam hlam k +
          f08_030_nativeFrequencyDilation lam hlam l : RealComplexL2) : ℝ → ℂ) ξ :=
        hright.symm

/-- The genuine same-volume L² dilation is complex homogeneous. -/
theorem f08_035_nativeFrequencyDilation_smul
    (lam : ℝ) (hlam : lam ≠ 0) (c : ℂ) (k : RealComplexL2) :
    f08_030_nativeFrequencyDilation lam hlam (c • k) =
      c • f08_030_nativeFrequencyDilation lam hlam k := by
  apply Lp.ext_iff.mpr
  filter_upwards [
    f08_030_nativeFrequencyDilation_ae lam hlam (c • k),
    f08_035_ae_scale lam hlam (Lp.coeFn_smul c k),
    f08_030_nativeFrequencyDilation_ae lam hlam k,
    Lp.coeFn_smul c (f08_030_nativeFrequencyDilation lam hlam k)
  ] with ξ hleft hscaled hk hright
  calc
    (f08_030_nativeFrequencyDilation lam hlam (c • k) : ℝ → ℂ) ξ =
        (Complex.ofReal (Real.sqrt (abs lam))) • (c • k) (lam * ξ) := hleft
    _ = (Complex.ofReal (Real.sqrt (abs lam))) • (c • k (lam * ξ)) := by
      rw [hscaled]
    _ = c • ((Complex.ofReal (Real.sqrt (abs lam))) • k (lam * ξ)) :=
      smul_comm _ _ _
    _ = c • (f08_030_nativeFrequencyDilation lam hlam k : ℝ → ℂ) ξ := by rw [hk]
    _ = ((c • f08_030_nativeFrequencyDilation lam hlam k : RealComplexL2) : ℝ → ℂ) ξ :=
        hright.symm

/-- Source-native same-volume complex-linear L² isometry for λ ≠ 0.
It wraps the original F08-030 actual operator, not a distinct surrogate. -/
def f08_035_nativeFrequencyDilation_linearIsometry
    (lam : ℝ) (hlam : lam ≠ 0) : RealComplexL2 →ₗᵢ[ℂ] RealComplexL2 where
  toFun := f08_030_nativeFrequencyDilation lam hlam
  map_add' := f08_035_nativeFrequencyDilation_add lam hlam
  map_smul' := f08_035_nativeFrequencyDilation_smul lam hlam
  norm_map' := f08_033_nativeFrequencyDilation_isometry lam hlam

/-- Dense-class reduction: the global continuity error is bounded by
twice the approximation error plus continuity on the approximant.
The final term remains to be controlled by actual Schwartz analysis. -/
theorem f08_035_nativeFrequencyDilation_approximation_bound
    (lam : ℝ) (hlam : lam ≠ 0) (k g : RealComplexL2) :
    ‖f08_030_nativeFrequencyDilation lam hlam k - k‖ ≤
      2 * ‖k - g‖ +
        ‖f08_030_nativeFrequencyDilation lam hlam g - g‖ := by
  let U := f08_035_nativeFrequencyDilation_linearIsometry lam hlam
  change ‖U k - k‖ ≤ 2 * ‖k - g‖ + ‖U g - g‖
  calc
    ‖U k - k‖ = ‖(U k - U g) + (U g - g) + (g - k)‖ := by
      congr 1
      abel
    _ ≤ (‖U k - U g‖ + ‖U g - g‖) + ‖g - k‖ := by
      exact (norm_add_le _ _).trans
        (add_le_add_right (norm_add_le _ _) _)
    _ = 2 * ‖k - g‖ + ‖U g - g‖ := by
      rw [← U.map_sub, U.norm_map, norm_sub_rev]
      ring

#print axioms f08_035_ae_scale
#print axioms f08_035_nativeFrequencyDilation_add
#print axioms f08_035_nativeFrequencyDilation_smul
#print axioms f08_035_nativeFrequencyDilation_approximation_bound

end
end WeilDefect
