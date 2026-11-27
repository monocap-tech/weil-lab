/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
Convolution transport adapted from Zeta23/ExplicitFormula.lean,
mirror revision 77f832c86fbb3e5336b949dae0fdcae26baea87c,
blob 11119489556113fd419d7b6fb45ccbaa2e493e2a. Native RECON Mellin dictionary is new.
-/
import WeilDefect.MasterRecon.V07A
import Mathlib.Analysis.Fourier.Convolution
import Mathlib.Analysis.Calculus.ContDiff.Convolution
import Mathlib.Analysis.Fourier.Inversion

namespace WeilDefect.MasterRecon.V10B8a

open MeasureTheory Complex Filter Set
open scoped Real FourierTransform Convolution ComplexConjugate
noncomputable section

def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ :=
  ∫ u : ℝ, f u * Complex.exp (Complex.I*z*(u:ℂ))

def tilde (g : ℝ → ℂ) : ℝ → ℂ := fun u => conj (g (-u))

def weilTest (f g : ℝ → ℂ) : ℝ → ℂ :=
  f ⋆[ContinuousLinearMap.mul ℝ ℂ] tilde g

theorem cintegral_const_mul (c : ℂ) (f : ℝ → ℂ) : ∫ x, c * f x = c * ∫ x, f x :=
  integral_const_mul c f

theorem cintegral_mul_const (c : ℂ) (f : ℝ → ℂ) : ∫ x, f x * c = (∫ x, f x) * c :=
  integral_mul_const c f

theorem cintegral_conj (f : ℝ → ℂ) : ∫ x, conj (f x) = conj (∫ x, f x) := integral_conj

theorem continuous_tilde {g : ℝ → ℂ} (hg : Continuous g) : Continuous (tilde g) :=
  Complex.continuous_conj.comp (hg.comp continuous_neg)

theorem hasCompactSupport_tilde {g : ℝ → ℂ} (hgs : HasCompactSupport g) :
    HasCompactSupport (tilde g) :=
  (hgs.comp_homeomorph (Homeomorph.neg ℝ)).comp_left (g := fun w : ℂ => conj w) (map_zero _)

theorem support_tilde_subset (g : ℝ → ℂ) : Function.support (tilde g) ⊆ -tsupport g := by
  intro u hu
  simp only [Function.mem_support, tilde, ne_eq, map_eq_zero] at hu
  exact subset_tsupport _ (by simpa [Function.mem_support] using hu)

theorem tsupport_tilde_subset {g : ℝ → ℂ} {L : ℝ} (hgs : tsupport g ⊆ Icc (-(L / 2)) (L / 2)) :
    tsupport (tilde g) ⊆ Icc (-(L / 2)) (L / 2) := by
  refine closure_minimal ((support_tilde_subset g).trans ?_) isClosed_Icc
  intro u hu
  have := hgs hu
  simp only [mem_Icc] at this ⊢
  constructor <;> linarith [this.1, this.2]

theorem paperFT_tilde (g : ℝ → ℂ) (z : ℂ) :
    paperFT (tilde g) z = conj (paperFT g (conj z)) := by
  unfold paperFT tilde
  rw [← cintegral_conj, ← integral_neg_eq_self]
  congr 1; ext u
  simp only [map_mul, ← Complex.exp_conj, conj_conj, Complex.conj_I, Complex.conj_ofReal,
    Complex.ofReal_neg, neg_neg]
  ring_nf

/-- App. A: `h_{f⋆g̃}(z) = h_f(z) · conj(h_g(conj z))` for all complex z. -/
theorem paperFT_weilTest {f g : ℝ → ℂ} (hf : Continuous f) (hg : Continuous g)
    (hfs : HasCompactSupport f) (hgs : HasCompactSupport g) (z : ℂ) :
    paperFT (weilTest f g) z = paperFT f z * conj (paperFT g (conj z)) := by
  rw [← paperFT_tilde]
  have hgt : Continuous (tilde g) := continuous_tilde hg
  have hgts : HasCompactSupport (tilde g) := hasCompactSupport_tilde hgs
  -- the integrand on ℝ × ℝ : (x,t) ↦ f(t) g̃(x−t) e^{izx}, continuous with compact support
  have hFc : Continuous (Function.uncurry fun (x t : ℝ) => f t * tilde g (x - t) * cexp (I * z * x)) := by
    change Continuous fun p : ℝ × ℝ => f p.2 * tilde g (p.1 - p.2) * cexp (I * z * p.1)
    fun_prop
  have hFs : HasCompactSupport
      (Function.uncurry fun (x t : ℝ) => f t * tilde g (x - t) * cexp (I * z * x)) := by
    refine HasCompactSupport.intro ((hgts.isCompact.add hfs.isCompact).prod hfs.isCompact) ?_
    rintro ⟨x, t⟩ hxt
    change f t * tilde g (x - t) * cexp (I * z * x) = 0
    rw [mem_prod, not_and_or] at hxt
    rcases hxt with hx | ht
    · by_cases ht : t ∈ tsupport f
      · have hx' : x - t ∉ tsupport (tilde g) := fun h => hx ⟨x - t, h, t, ht, by ring⟩
        rw [image_eq_zero_of_notMem_tsupport hx']; simp
      · rw [image_eq_zero_of_notMem_tsupport ht]; simp
    · rw [image_eq_zero_of_notMem_tsupport ht]; simp
  have hFi : Integrable (Function.uncurry fun (x t : ℝ) => f t * tilde g (x - t) * cexp (I * z * x))
      (volume.prod volume) := hFc.integrable_of_hasCompactSupport hFs
  -- translation v = x − t in the inner integral
  have hshift : ∀ t : ℝ, ∫ x : ℝ, tilde g (x - t) * cexp (I * z * x)
      = cexp (I * z * t) * ∫ v : ℝ, tilde g v * cexp (I * z * v) := by
    intro t
    rw [← cintegral_const_mul,
      ← integral_sub_right_eq_self (fun v : ℝ => cexp (I * z * t) * (tilde g v * cexp (I * z * v))) t]
    congr 1; ext x
    simp only [Complex.ofReal_sub]
    rw [mul_left_comm, ← Complex.exp_add]
    congr 2; ring
  calc paperFT (weilTest f g) z
      = ∫ x : ℝ, (∫ t : ℝ, f t * tilde g (x - t)) * cexp (I * z * x) := by
        simp only [paperFT, weilTest, convolution_def, ContinuousLinearMap.mul_apply']
    _ = ∫ x : ℝ, ∫ t : ℝ, f t * tilde g (x - t) * cexp (I * z * x) := by
        congr 1; ext x; rw [← cintegral_mul_const]
    _ = ∫ t : ℝ, ∫ x : ℝ, f t * tilde g (x - t) * cexp (I * z * x) := integral_integral_swap hFi
    _ = ∫ t : ℝ, f t * cexp (I * z * t) * ∫ v : ℝ, tilde g v * cexp (I * z * v) := by
        congr 1; ext t
        rw [show (fun x : ℝ => f t * tilde g (x - t) * cexp (I * z * x))
            = fun x => f t * (tilde g (x - t) * cexp (I * z * x)) from funext fun _ => mul_assoc _ _ _,
          cintegral_const_mul, hshift t]
        ring
    _ = paperFT f z * paperFT (tilde g) z := by
        simp only [paperFT]; rw [← cintegral_mul_const]

theorem weilTest_contDiff {f g : ℝ → ℂ} (hf : ContDiff ℝ 2 f) (hg : Continuous g)
    (hfs : HasCompactSupport f) :
    ContDiff ℝ 2 (weilTest f g) := by
  have := hfs.contDiff_convolution_left (n := 2) (L := ContinuousLinearMap.mul ℝ ℂ) (μ := volume)
    hf (continuous_tilde hg).locallyIntegrable
  simpa [weilTest] using this

theorem weilTest_hasCompactSupport {f g : ℝ → ℂ}
    (hfs : HasCompactSupport f) (hgs : HasCompactSupport g) :
    HasCompactSupport (weilTest f g) :=
  hfs.convolution _ (hasCompactSupport_tilde hgs)

/-- App. A: `supp k ⊆ [−L, L]` when `supp f, supp g ⊆ [−L/2, L/2]`. -/
theorem tsupport_weilTest_subset {f g : ℝ → ℂ} {L : ℝ}
    (hfs : tsupport f ⊆ Icc (-(L / 2)) (L / 2)) (hgs : tsupport g ⊆ Icc (-(L / 2)) (L / 2)) :
    tsupport (weilTest f g) ⊆ Icc (-L) L := by
  refine closure_minimal ?_ isClosed_Icc
  refine (support_convolution_subset _).trans ?_
  rintro x ⟨a, ha, b, hb, rfl⟩
  have ha' := hfs (subset_tsupport _ ha)
  have hb' := tsupport_tilde_subset hgs (subset_tsupport _ hb)
  simp only [mem_Icc] at ha' hb' ⊢
  constructor <;> linarith [ha'.1, ha'.2, hb'.1, hb'.2]


theorem paperFT_mellin (f : ℝ → ℂ) (z : ℂ) :
    paperFT f z = V07A.mellin f (I*z) := by
  unfold paperFT V07A.mellin
  apply integral_congr_ae
  filter_upwards with x
  exact mul_comm _ _

theorem mellin_congr_ae (f g : ℝ → ℂ) (h : f =ᵐ[volume] g) (z : ℂ) :
    V07A.mellin f z = V07A.mellin g z := by
  unfold V07A.mellin
  apply integral_congr_ae
  filter_upwards [h] with x hx
  rw [hx]

theorem autocorr_support {f : ℝ → ℂ} {t : ℝ}
    (hf : tsupport f ⊆ Icc (-t) t) :
    tsupport (weilTest f f) ⊆ Icc (-(2*t)) (2*t) := by
  apply tsupport_weilTest_subset
  · simpa only [mul_div_cancel_left₀ _ (by norm_num : (2:ℝ) ≠ 0)] using hf
  · simpa only [mul_div_cancel_left₀ _ (by norm_num : (2:ℝ) ≠ 0)] using hf

end
end WeilDefect.MasterRecon.V10B8a

#print axioms WeilDefect.MasterRecon.V10B8a.cintegral_const_mul
#print axioms WeilDefect.MasterRecon.V10B8a.cintegral_mul_const
#print axioms WeilDefect.MasterRecon.V10B8a.cintegral_conj
#print axioms WeilDefect.MasterRecon.V10B8a.continuous_tilde
#print axioms WeilDefect.MasterRecon.V10B8a.hasCompactSupport_tilde
#print axioms WeilDefect.MasterRecon.V10B8a.support_tilde_subset
#print axioms WeilDefect.MasterRecon.V10B8a.tsupport_tilde_subset
#print axioms WeilDefect.MasterRecon.V10B8a.paperFT_tilde
#print axioms WeilDefect.MasterRecon.V10B8a.paperFT_weilTest
#print axioms WeilDefect.MasterRecon.V10B8a.weilTest_contDiff
#print axioms WeilDefect.MasterRecon.V10B8a.weilTest_hasCompactSupport
#print axioms WeilDefect.MasterRecon.V10B8a.tsupport_weilTest_subset
#print axioms WeilDefect.MasterRecon.V10B8a.paperFT_mellin
#print axioms WeilDefect.MasterRecon.V10B8a.mellin_congr_ae
#print axioms WeilDefect.MasterRecon.V10B8a.autocorr_support
