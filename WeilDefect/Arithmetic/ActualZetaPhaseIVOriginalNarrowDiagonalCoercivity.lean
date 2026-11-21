import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalNarrowSignedGamma
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope
import WeilDefect.Arithmetic.ActualZetaOriginalCollarPoleBound
import WeilDefect.Arithmetic.ActualZetaOriginalCollarLiteralArch
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-!
IV017 part two: actual ORIGINAL zeta physical window (11/10),
narrow source pole estimate, true Gamma Fourier attachment and
conditional only on the already IV016 certified-prime-free support
geometry, a FULL NEW DIAGONAL signed quantitative lower bound.

This is a genuine ORIGINAL signed literatureRHS, not a surrogate
Gram form. The lower bound constant is 19/20, using
 (483/500) mass from true Gamma/digamma high/low symbol and
 (2/125) mass penalty from the TWO original pole residues.
The actual von-Mangoldt diagonal contributes ZERO by the
original physical 0.002-width support geometry.

A kernel check of this module depends on IV009–IV016 imports.
All declarations remain candidates pending pinned Lean acceptance.
-/

/-- Under ORIGINAL [-11/10,11/10] support, the TRUE half-axis
Mellin/pole moment is bounded by twice the physical L¹ norm.
This is the actual exponential window evaluation, not a
fictional rank-one or diagonal-square replacement. -/
theorem neutralIV017OriginalWindowMoment_bound
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0)
    (v : ℝ) (hv : |v| ≤ 1/2) :
    ‖sourceWindowMoment (11/10:ℝ) v (t.toLp 2 volume)‖ ≤
      2 * ‖t.toLp 1 volume‖ := by
  have h := neutralWindowEvaluation_imaginary
    (11/10:ℝ) (-v) (t.toLp 2 volume)
  rw [neg_neg] at h
  rw [← h]
  rw [neutralNF573WindowEvaluation_eq_raw_of_ae _ _ _
    (neutralIV006Schwartz_window_ae (11/10:ℝ) t ht)]
  unfold neutralRawTransform
  let f := fun x : ℝ =>
    t x * Complex.exp (Complex.I*(Complex.I*((-v:ℝ):ℂ))*(x:ℂ))
  have hf (x : ℝ) : ‖f x‖ ≤ 2*‖t x‖ := by
    by_cases hx : x∈Set.Icc (-(11/10:ℝ)) (11/10:ℝ)
    · have hxnorm : |x| ≤ (11/10:ℝ) := abs_le.mpr hx
      have htx : v*x ≤ 11/20 := by
        calc
          _ ≤ |v*x| := le_abs_self _
          _ = |v| * |x| := abs_mul _ _
          _ ≤ (1/2:ℝ)*(11/10) :=
            mul_le_mul hv hxnorm (abs_nonneg _) (by norm_num)
          _ = _ := by norm_num
      have he :
          Complex.I*(Complex.I*((-v:ℝ):ℂ))*(x:ℂ) =
            ((v*x:ℝ):ℂ) := by
        calc
          _ = (Complex.I*Complex.I)*((-v:ℝ):ℂ)*(x:ℂ) := by ring
          _ = _ := by rw [Complex.I_mul_I]; push_cast; ring
      have hexp : Real.exp (v*x) ≤ 2 :=
        (Real.exp_le_exp.mpr htx).trans
          (by
            have h := neutralNF585Exp_half_le_two
            rw [neutralNF578B,
              show (11/10:ℝ)/2 = 11/20 by norm_num] at h
            exact h)
      dsimp [f]
      rw [he,norm_mul,Complex.norm_exp,Complex.ofReal_re]
      exact (mul_le_mul_of_nonneg_left hexp
        (norm_nonneg _)).trans_eq (mul_comm _ _)
    · simp [f, ht x hx]
  have hi : Integrable (fun x : ℝ => 2*‖t x‖) :=
    t.integrable.norm.const_mul 2
  have hfi : Integrable (fun x => ‖f x‖) := by
    apply hi.mono' (by dsimp [f]; fun_prop)
    filter_upwards [] with x
    rw [Real.norm_eq_abs,abs_of_nonneg (norm_nonneg _)]
    exact hf x
  change ‖∫ x,f x‖ ≤ _
  calc
    _ ≤ ∫ x,‖f x‖ := norm_integral_le_integral_norm _
    _ ≤ ∫ x,2*‖t x‖ := integral_mono hfi hi hf
    _ = _ := by rw [integral_const_mul,SchwartzMap.norm_toLp_one]

/-- The TWO true source pole moments of an original supported
physical Schwartz test cost at most 8 times its actual squared
L¹ norm (not one pole and not a positive artificial square). -/
theorem neutralIV017OriginalPole_norm_le_eightL1_sq
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0) :
    ‖neutralIV011OriginalMixedPole (11/10:ℝ) t t‖ ≤
      8 * ‖t.toLp 1 volume‖^2 := by
  let A := sourceWindowMoment (11/10:ℝ) (1/2) (t.toLp 2 volume)
  let B := sourceWindowMoment (11/10:ℝ) (-(1/2)) (t.toLp 2 volume)
  have hA : ‖A‖ ≤ 2 * ‖t.toLp 1 volume‖ :=
    neutralIV017OriginalWindowMoment_bound t ht (1/2) (by norm_num)
  have hB : ‖B‖ ≤ 2 * ‖t.toLp 1 volume‖ :=
    neutralIV017OriginalWindowMoment_bound t ht (-(1/2)) (by norm_num)
  have hAB :
      ‖A‖*‖B‖ ≤ (2*‖t.toLp 1 volume‖)*
          (2*‖t.toLp 1 volume‖) :=
    mul_le_mul hA hB (norm_nonneg _) (by positivity)
  have hBA :
      ‖B‖*‖A‖ ≤ (2*‖t.toLp 1 volume‖)*
          (2*‖t.toLp 1 volume‖) :=
    mul_le_mul hB hA (norm_nonneg _) (by positivity)
  have hp := neutralIV012OriginalMixedPole_norm_le_momentBudget
    (11/10:ℝ) t t
  unfold neutralIV012OriginalPoleMomentBudget at hp
  change ‖neutralIV011OriginalMixedPole (11/10:ℝ) t t‖ ≤
    ‖B‖*‖A‖ + ‖A‖*‖B‖ at hp
  nlinarith only [hp,hAB,hBA]

/-- Exact resulting signed REAL pole lower bound at width 1/500:
both genuine original half-pole moments together are bounded by
2/125 of the physical L² mass. -/
theorem neutralIV017NarrowPole_real_lower
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/1000:ℝ))
        ((1/5:ℝ)+(1/1000:ℝ)) → t x = 0) :
    -(2/125:ℝ) * neutralNF600Mass t ≤
      (neutralIV011OriginalMixedPole (11/10:ℝ) t t).re := by
  have hsmall := neutralIV017Narrow_support_from_bump t ht
  have htwide : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0 :=
    neutralIV015Bump_supported_largeWindow
      (11/10:ℝ) (1/5:ℝ) (1/1000:ℝ)
      (by norm_num) t ht
  have hL1 := neutralIV017NarrowL1_sq_le t hsmall
  have hp := neutralIV017OriginalPole_norm_le_eightL1_sq
    t htwide
  have hb :
      ‖neutralIV011OriginalMixedPole (11/10:ℝ) t t‖ ≤
      (2/125:ℝ) * neutralNF600Mass t := by
    linarith only [hp,hL1]
  have hre :=
    (Complex.abs_re_le_norm
      (neutralIV011OriginalMixedPole (11/10:ℝ) t t)).trans hb
  exact (abs_le.mp hre).1

/-- Original correlation spectral Fourier equality generalized from
NF600's OLD two-collar support to ANY authentic Schwartz input
fitting in the SAME actual [-11/10,11/10] physical window.
This step is needed to evaluate the new bump's diagonal without
silently applying an old-collar-only Gamma theorem outside its
support hypotheses. -/
theorem neutralIV017OriginalWindowCorrelation_spectral
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0)
    (ξ : ℝ) :
    Zeta23.paperFT
      (neutralWindowCorrelation (11/10:ℝ)
        (t.toLp 2 volume) (t.toLp 2 volume))
      ((-2*Real.pi*ξ:ℝ):ℂ) =
      (neutralNF600Density t ξ:ℂ) := by
  have h := neutralNF573WindowEvaluation_eq_raw_of_ae
    (11/10:ℝ) (t.toLp 2 volume) (fun x => t x)
    (neutralIV006Schwartz_window_ae (11/10:ℝ) t ht)
    ((-2*Real.pi*ξ:ℝ):ℂ)
  rw [← neutralRawTransform_eq_paperFT,
    neutralWindowCorrelation_rawTransform,
    Complex.conj_ofReal,h,← neutralRawTransform_fourier]
  rw [← SchwartzMap.fourier_coe]
  unfold neutralNF600Density
  simpa only [Complex.ofReal_pow] using
    Complex.conj_mul' ((𝓕 t) ξ)

/-- FULL ORIGINAL Gamma/digamma diagonal at the new physical
source equals the exact SIGNED real-frequency Plancherel integral,
not IV012's absolute Gamma envelope. The 1/(2π) factor and
original true full gammaBracket are carried through unchanged. -/
theorem neutralIV017OriginalWindowArch_real_eq_spectral
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0) :
    (neutralIV011OriginalMixedArch (11/10:ℝ) t t).re =
      neutralNF600Arch t := by
  let F : ℝ → ℂ := fun r =>
    Zeta23.paperFT
      (neutralWindowCorrelation (11/10:ℝ)
        (t.toLp 2 volume) (t.toLp 2 volume))
      (r:ℂ)*(Zeta23.EF.gammaBracket r:ℂ)
  have h := Measure.integral_comp_mul_left F (-2*Real.pi)
  have habs : |(-2*Real.pi)⁻¹|=1/(2*Real.pi) := by
    rw [show -2*Real.pi=-(2*Real.pi) by ring,
      inv_neg,abs_neg,
      abs_of_pos (inv_pos.mpr (by positivity))]
    simp only [one_div]
  rw [habs,Complex.real_smul] at h
  have hc : (1/(2*Real.pi):ℂ)=
      ((1/(2*Real.pi):ℝ):ℂ) := by push_cast; rfl
  change ((1/(2*Real.pi):ℂ)*∫ r,F r).re = _
  rw [hc,← h]
  have he :
      (fun ξ : ℝ => F ((-2*Real.pi)*ξ)) =
        fun ξ =>
          ((Zeta23.EF.gammaBracket (-2*Real.pi*ξ)*
            neutralNF600Density t ξ:ℝ):ℂ) := by
    funext ξ
    dsimp only [F]
    rw [neutralIV017OriginalWindowCorrelation_spectral t ht ξ,
      Complex.ofReal_mul,mul_comm]
  rw [he]
  unfold neutralNF600Arch
  first
  | rw [integral_ofReal] <;> rfl
  | norm_cast <;> rfl
  | have hi := neutralNF600Arch_integrable t
    have hc := Complex.ofRealCLM.integral_comp_comm hi
    simpa using congrArg Complex.re hc
  | have hi := neutralNF600Arch_integrable t
    rw [← Complex.integral_re
      (Complex.continuous_ofReal.comp
        (by fun_prop) |>.aestronglyMeasurable)]

/-- MAJOR new original signed arithmetic result TARGET:
Every complex Schwartz input confined to the genuine narrow
physical interval [0.199,0.201] has signed original zeta
diagonal >= 19/20 of its actual physical squared L² mass.

The proof incorporates all original terms:
 * TRUE prime side zero by IV016 source physical self-nonoverlap;
 * TRUE two-pole residue lower >= -2/125 mass;
 * TRUE signed digamma integral lower >= 483/500 mass.

This is not the old NF600 collar coercivity applied incorrectly
outside the collars. It derives an independent quantitative
narrow-window lower from actual original source estimates.

A successful Lean kernel proof would establish NEW-DIRECTION
diagonal nonnegativity for this narrow class. It still would
NOT establish the mixed old/new Schur bound or global Weil
positivity; the IV017 proof remains a compiler CANDIDATE. -/
theorem neutralIV017NarrowOriginalDiagonal_coercive
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/1000:ℝ))
        ((1/5:ℝ)+(1/1000:ℝ)) → t x = 0) :
    (19/20:ℝ) * neutralNF600Mass t ≤
      (neutralIV010Diagonal (11/10:ℝ) t).re := by
  have hsmall := neutralIV017Narrow_support_from_bump t ht
  have htwide : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0 :=
    neutralIV015Bump_supported_largeWindow
      (11/10:ℝ) (1/5:ℝ) (1/1000:ℝ)
      (by norm_num) t ht
  have hprime :=
    (neutralIV016FrozenSmallBump_selfPrime_zero t ht).1
  have hpole := neutralIV017NarrowPole_real_lower t ht
  have hgamma := neutralIV017NarrowGamma_coercive t hsmall
  have heq :=
    neutralIV017OriginalWindowArch_real_eq_spectral t htwide
  have hsplit := neutralIV011OriginalMixed_arithmeticSplit
    (11/10:ℝ) t t
  change neutralIV010Diagonal (11/10:ℝ) t =
    neutralIV011OriginalMixedPole (11/10:ℝ) t t -
      neutralIV011OriginalMixedPrime (11/10:ℝ) t t +
      neutralIV011OriginalMixedArch (11/10:ℝ) t t at hsplit
  rw [hprime] at hsplit
  simp only [sub_zero] at hsplit
  have hre := congrArg Complex.re hsplit
  simp only [Complex.add_re] at hre
  rw [heq] at hre
  linarith only [hre,hpole,hgamma]

/-- For the specific PHYSICAL nonzero bump constructed by
the IV015 Mathlib bump theorem, the original new diagonal is
nonnegative WITHOUT a separately postulated diagonal sign.
The whole new mixed Schur bound against old two-collar input
still needs an independent original pole/Gamma estimate. -/
theorem neutralIV017ExistsNonzeroNewSource_diagonalNonnegative :
    ∃ t : 𝓢(ℝ,ℂ),
      t (1/5:ℝ) = 1 ∧
      ¬ neutralNF735InOriginalCollars t ∧
      0 ≤ (neutralIV010Diagonal (11/10:ℝ) t).re := by
  obtain ⟨t,htc,htlocal⟩ :=
    neutralIV015ExistsComplexSchwartzBump
      (1/5:ℝ) (1/1000:ℝ) (by norm_num)
  have hnon : ¬ neutralNF735InOriginalCollars t := by
    intro hOld
    have hz := hOld (1/5:ℝ)
      neutralIV015FrozenConcrete_centerOutside
    rw [htc] at hz
    exact one_ne_zero hz
  have hdiag := neutralIV017NarrowOriginalDiagonal_coercive t htlocal
  have hm : 0 ≤ neutralNF600Mass t := by
    unfold neutralNF600Mass
    positivity
  refine ⟨t,htc,hnon,?_⟩
  linarith only [hdiag,hm]

/-- NEW ORIGINAL SUPPORT-EXTENSION GATE with BOTH diagonal
nonnegativity assumptions DISCHARGED from their physical sources.
The accepted old NF738 collar 2/5 coercivity supplies A>=0;
the new IV017 narrow-source 19/20 bound supplies D>=0.

Only the original mixed pole/Gamma cross-SCHUR estimate remains
a REAL analytic premise. It is deliberately not implied by the
positive new diagonal or a synthetic matrix. The coefficients,
unchanged signed zeta EF and full true finite physical Schwartz
combination are preserved. -/
theorem neutralIV017OneNewSource_nonnegative_of_singleResidualBound
    {n : ℕ}
    (s : Fin n → 𝓢(ℝ,ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i))
    (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/1000:ℝ))
        ((1/5:ℝ)+(1/1000:ℝ)) → t x = 0)
    (hResidual :
      (neutralIV010Mixed (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV010Mixed (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
        (neutralIV007OriginalMixedEnergy (11/10:ℝ) s u).re *
          ((19/20:ℝ) * neutralNF600Mass t))
    (v : ℂ) :
    0 ≤ (neutralIV010Diagonal (11/10:ℝ)
      (neutralIV009PhysicalSchwartzSum s u + v • t)).re := by
  have hswide :
      ∀ i : Fin n, ∀ x : ℝ,
        x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
          s i x = 0 := by
    intro i
    exact neutralIV009OriginalCollars_supported_window (s i) (hs i)
  have htwide :
      ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        t x = 0 :=
    neutralIV015Bump_supported_largeWindow
      (11/10:ℝ) (1/5:ℝ) (1/1000:ℝ)
      (by norm_num) t ht
  have hOldBound :=
    neutralIV009OriginalCollars_mixedEnergy_lower s u hs
  have hOld :
      0 ≤ (neutralIV007OriginalMixedEnergy
        (11/10:ℝ) s u).re := by
    have hnon :
        0 ≤ (2/5:ℝ) *
          ‖(neutralIV009PhysicalSchwartzSum s u).toLp 2 volume‖^2 := by
      positivity
    linarith
  have hdiag := neutralIV017NarrowOriginalDiagonal_coercive t ht
  have hmass : 0 ≤ neutralNF600Mass t := by
    unfold neutralNF600Mass
    positivity
  have hNew :
      0 ≤ (neutralIV010Diagonal (11/10:ℝ) t).re := by
    linarith
  have hCross :
      (neutralIV010Mixed (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV010Mixed (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
        (neutralIV007OriginalMixedEnergy
          (11/10:ℝ) s u).re *
          (neutralIV010Diagonal (11/10:ℝ) t).re := by
    calc
      _ ≤ (neutralIV007OriginalMixedEnergy
            (11/10:ℝ) s u).re *
          ((19/20:ℝ) * neutralNF600Mass t) := hResidual
      _ ≤ _ := mul_le_mul_of_nonneg_left hdiag hOld
  exact neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
    (11/10:ℝ) (11/10:ℝ) (le_refl _) s u hswide
    t htwide hOld hNew hCross v

#print axioms neutralIV016FrozenSmallBump_selfPrime_zero
#print axioms neutralIV012OriginalMixedPole_norm_le_momentBudget
#print axioms neutralNF573WindowEvaluation_eq_raw_of_ae
#print axioms neutralIV017NarrowGamma_coercive
#print axioms neutralIV017OriginalWindowMoment_bound
#print axioms neutralIV017OriginalPole_norm_le_eightL1_sq
#print axioms neutralIV017NarrowPole_real_lower
#print axioms neutralIV017OriginalWindowCorrelation_spectral
#print axioms neutralIV017OriginalWindowArch_real_eq_spectral
#print axioms neutralIV017NarrowOriginalDiagonal_coercive
#print axioms neutralIV017ExistsNonzeroNewSource_diagonalNonnegative
#print axioms neutralIV017OneNewSource_nonnegative_of_singleResidualBound

end
end WeilDefect
