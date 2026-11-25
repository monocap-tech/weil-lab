import WeilDefect.Arithmetic.ActualZetaIV094OriginalDiagonalSignedTailGate
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Order.Filter.Finite
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate Topology

def neutralIV095FiniteDiagonal (M N : ℕ) (s : 𝓢(ℝ,ℂ)) : ℝ :=
  (neutralIV086PhysicalWeilFinite M N
    (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume))).re

def neutralIV095DiagonalTail (M N : ℕ) (s : 𝓢(ℝ,ℂ)) : ℝ :=
  neutralNF598SmoothWeil s - neutralIV095FiniteDiagonal M N s

def neutralIV095TailProfile (N : ℕ) (s : 𝓢(ℝ,ℂ)) (r : ℝ) : ℝ :=
  (1 / (2 * Real.pi)) *
    (Zeta23.EF.gammaBracket r - neutralIV071GammaFinite N r) *
    ‖neutralWindowEvaluation (11/10:ℝ) (r : ℂ) (s.toLp 2 volume)‖^2

/-- The literal diagonal remainder is exactly an integrable nonnegative
weighted square, with the original paper normalization. -/
theorem neutralIV095DiagonalTail_data (M N : ℕ) (s : 𝓢(ℝ,ℂ))
    (hs : neutralNF735InOriginalCollars s)
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ)) :
    Integrable (neutralIV095TailProfile N s) ∧
      neutralIV095DiagonalTail M N s = ∫ r : ℝ, neutralIV095TailProfile N s r := by
  let k := neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume)
  have hw := neutralIV009OriginalCollars_supported_window s hs
  have hk : ContDiff ℝ 2 k :=
    neutralWindowCorrelation_contDiff_of_ae_smoothSecond _ _ _ (fun x => s x)
      (s.smooth 2) (neutralIV008SchwartzWindow_hasCompactSupport _ s hw)
      (neutralIV006Schwartz_window_ae _ s hw)
  have hL : 0 ≤ 2*(11/10:ℝ) := by norm_num
  have hsup : ∀ u, k u ≠ 0 → |u| ≤ 2*(11/10:ℝ) :=
    neutralIV087WindowCorrelation_support_abs _ _ _
  have hi := neutralIV090GammaProduct_integrable_compactC2 k hk hL hsup
  have hf := neutralIV078Finite_spectral_integrable N k
    (neutralIV082Fourier_integrable_compactC2 k hk hL hsup)
  have he : Integrable (neutralIV090GammaErrorIntegrand N k) := by
    apply (hi.sub hf).congr
    filter_upwards [] with r
    simp only [neutralIV090GammaErrorIntegrand, Complex.ofReal_sub, Pi.sub_apply]
    ring
  have hp (r : ℝ) : (1 / (2 * Real.pi)) *
      (neutralIV090GammaErrorIntegrand N k r).re = neutralIV095TailProfile N s r := by
    unfold neutralIV090GammaErrorIntegrand neutralIV095TailProfile
    dsimp only [k]
    rw [neutralIV094WindowDiagonal_paperFT]
    simp only [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im, zero_mul, sub_zero]
    ring
  have hI : Integrable (neutralIV095TailProfile N s) := by
    apply (he.re.const_mul (1 / (2 * Real.pi))).congr
    filter_upwards [] with r
    exact hp r
  refine ⟨hI, ?_⟩
  have hd := congrArg Complex.re (neutralIV090WeilError_eq_integral M N k hk hL hsup hM)
  have hc : ((1 / (2 * Real.pi) : ℝ) : ℂ) = (1 / (2 * Real.pi) : ℂ) := by
    push_cast <;> rfl
  rw [← hc] at hd
  simp only [Complex.sub_re, Complex.mul_re, Complex.ofReal_re,
    Complex.ofReal_im, zero_mul, sub_zero] at hd
  have hr := integral_re he
  change (∫ r : ℝ, (neutralIV090GammaErrorIntegrand N k r).re) =
    (∫ r : ℝ, neutralIV090GammaErrorIntegrand N k r).re at hr
  change (Zeta23.EF.literatureRHS k).re - (neutralIV086PhysicalWeilFinite M N k).re = _
  rw [hd, ← hr, ← integral_const_mul]
  exact integral_congr_ae (Filter.Eventually.of_forall hp)

/-- Finite Cauchy--Schwarz applied to the actual window evaluations,
with the nonnegative omitted Gamma weight retained. -/
theorem neutralIV095TailProfile_sum_le {n : ℕ} (N : ℕ)
    (s : Fin n → 𝓢(ℝ,ℂ)) (u : Fin n → ℂ) (r : ℝ) :
    neutralIV095TailProfile N (neutralIV009PhysicalSchwartzSum s u) r ≤
      (∑ i : Fin n, ‖u i‖^2) * ∑ i : Fin n, neutralIV095TailProfile N (s i) r := by
  let F (i : Fin n) := neutralWindowEvaluation (11/10:ℝ) (r : ℂ) ((s i).toLp 2 volume)
  let w : ℝ := (1 / (2 * Real.pi)) *
    (Zeta23.EF.gammaBracket r - neutralIV071GammaFinite N r)
  have hw : 0 ≤ w := mul_nonneg (by positivity) (neutralIV089GammaRemainder_bound N r).1
  have h₁ : ‖∑ i : Fin n, u i * F i‖ ≤ ∑ i : Fin n, ‖u i‖ * ‖F i‖ := by
    simpa only [norm_mul] using norm_sum_le (Finset.univ : Finset (Fin n)) (fun i => u i * F i)
  have h₂ := (pow_le_pow_left₀ (norm_nonneg _) h₁ 2).trans
    (Finset.sum_mul_sq_le_sq_mul_sq (Finset.univ : Finset (Fin n)) (fun i => ‖u i‖) (fun i => ‖F i‖))
  unfold neutralIV095TailProfile
  rw [neutralIV009WindowEvaluation_finiteLinear]
  change w * ‖∑ i : Fin n, u i * F i‖^2 ≤
    (∑ i : Fin n, ‖u i‖^2) * ∑ i : Fin n, w * ‖F i‖^2
  rw [← Finset.mul_sum]
  calc
    _ ≤ w * ((∑ i : Fin n, ‖u i‖^2) * ∑ i : Fin n, ‖F i‖^2) :=
      mul_le_mul_of_nonneg_left h₂ hw
    _ = _ := by ring

/-- A uniform error on actual physical sums is bounded by the trace of
the original diagonal tails times the squared coefficient norm. -/
theorem neutralIV095DiagonalTail_sum_le {n : ℕ} (M N : ℕ)
    (s : Fin n → 𝓢(ℝ,ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i, neutralNF735InOriginalCollars (s i))
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ)) :
    neutralIV095DiagonalTail M N (neutralIV009PhysicalSchwartzSum s u) ≤
      (∑ i : Fin n, ‖u i‖^2) * ∑ i : Fin n, neutralIV095DiagonalTail M N (s i) := by
  have hS : neutralNF735InOriginalCollars (neutralIV009PhysicalSchwartzSum s u) :=
    neutralNF738OriginalCollars_finset_linear Finset.univ s u (fun i _ => hs i)
  obtain ⟨hI, hE⟩ := neutralIV095DiagonalTail_data M N _ hS hM
  have hentry (i : Fin n) := neutralIV095DiagonalTail_data M N (s i) (hs i) hM
  let A : ℝ := ∑ i : Fin n, ‖u i‖^2
  have hsum : Integrable (fun r : ℝ => ∑ i : Fin n, neutralIV095TailProfile N (s i) r) :=
    integrable_finsetSum Finset.univ (fun i _ => (hentry i).1)
  rw [hE]
  calc
    _ ≤ ∫ r : ℝ, A * ∑ i : Fin n, neutralIV095TailProfile N (s i) r :=
      integral_mono hI (hsum.const_mul A) (neutralIV095TailProfile_sum_le N s u)
    _ = A * ∑ i : Fin n, neutralIV095DiagonalTail M N (s i) := by
      rw [integral_const_mul, integral_finsetSum Finset.univ (fun i _ => (hentry i).1)]
      congr 1
      apply Finset.sum_congr rfl
      intro i _
      exact (hentry i).2.symm

/-- All diagonal tail traces tend to zero for the same fixed arithmetic
cutoff, by genuine physical convergence, not an assumed matrix limit. -/
theorem neutralIV095DiagonalTailTrace_eventual {n : ℕ} (M : ℕ)
    (s : Fin n → 𝓢(ℝ,ℂ)) (hs : ∀ i, neutralNF735InOriginalCollars (s i))
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ)) (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, (∑ i : Fin n, neutralIV095DiagonalTail M N (s i)) ≤ ε := by
  let δ : ℝ := ε / ((n : ℝ)+1)
  have hδ : 0 < δ := by dsimp [δ]; positivity
  have hEach (i : Fin n) : ∀ᶠ N : ℕ in atTop, neutralIV095DiagonalTail M N (s i) < δ := by
    let k := neutralWindowCorrelation (11/10:ℝ) ((s i).toLp 2 volume) ((s i).toLp 2 volume)
    have hk := neutralIV087OriginalMixedCorrelation_contDiff (11/10:ℝ) s
      (fun j => neutralIV009OriginalCollars_supported_window (s j) (hs j)) i i
    have ht := neutralIV086PhysicalWeilFinite_tendsto_original M k hk
      (show 0 ≤ 2*(11/10:ℝ) by norm_num)
      (neutralIV087WindowCorrelation_support_abs (11/10:ℝ) _ _) hM
    have htr : Tendsto (fun N : ℕ => neutralIV095FiniteDiagonal M N (s i)) atTop
        (𝓝 (neutralNF598SmoothWeil (s i))) :=
      Complex.continuous_re.continuousAt.tendsto.comp ht
    have hd := (tendsto_const_nhds.sub htr :
      Tendsto (fun N : ℕ => neutralNF598SmoothWeil (s i) -
        neutralIV095FiniteDiagonal M N (s i)) atTop
        (𝓝 (neutralNF598SmoothWeil (s i) - neutralNF598SmoothWeil (s i))))
    rw [sub_self] at hd
    exact hd.eventually (Iio_mem_nhds hδ)
  filter_upwards [Filter.eventually_all.mpr hEach] with N hN
  calc
    _ ≤ ∑ _i : Fin n, δ := Finset.sum_le_sum (fun i _ => (hN i).le)
    _ = (n : ℝ) * δ := by simp
    _ ≤ ε := by
      dsimp [δ]
      have hden : 0 < (n : ℝ)+1 := by positivity
      rw [← mul_div_assoc]
      apply (div_le_iff₀ hden).mpr
      nlinarith only [hε]

/-- A single cutoff works on the ENTIRE source-native finite collar
span when its actual physical mass controls the coefficient norm.
The mass comparison is explicit; dependent generators are not assumed
to have a positive coefficient-space lower bound. -/
theorem neutralIV095OriginalCollarSpan_uniform_finite_margin {n : ℕ}
    (M : ℕ) (s : Fin n → 𝓢(ℝ,ℂ))
    (hs : ∀ i, neutralNF735InOriginalCollars (s i))
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ))
    (C : ℝ) (hC : 0 < C)
    (hmass : ∀ u : Fin n → ℂ, (∑ i : Fin n, ‖u i‖^2) ≤
      C * ‖(neutralIV009PhysicalSchwartzSum s u).toLp 2 volume‖^2) :
    ∃ N₀ : ℕ, ∀ N ≥ N₀, ∀ u : Fin n → ℂ,
      (1/5:ℝ) * ‖(neutralIV009PhysicalSchwartzSum s u).toLp 2 volume‖^2 ≤
        neutralIV095FiniteDiagonal M N (neutralIV009PhysicalSchwartzSum s u) := by
  let ε : ℝ := 1 / (5*C)
  have hε : 0 < ε := by dsimp [ε]; positivity
  obtain ⟨N₀, hN₀⟩ := eventually_atTop.mp (neutralIV095DiagonalTailTrace_eventual M s hs hM ε hε)
  refine ⟨N₀, ?_⟩
  intro N hN u
  let S := neutralIV009PhysicalSchwartzSum s u
  have hS : neutralNF735InOriginalCollars S :=
    neutralNF738OriginalCollars_finset_linear Finset.univ s u (fun i _ => hs i)
  have hfull := neutralNF600SmoothCollarLower S hS
  have hsum := neutralIV095DiagonalTail_sum_le M N s u hs hM
  have hA : 0 ≤ ∑ i : Fin n, ‖u i‖^2 := Finset.sum_nonneg (fun i _ => sq_nonneg _)
  have herr : neutralIV095DiagonalTail M N S ≤ (1/5:ℝ)*‖S.toLp 2 volume‖^2 := by
    calc
      _ ≤ (∑ i : Fin n, ‖u i‖^2) * ∑ i : Fin n, neutralIV095DiagonalTail M N (s i) := hsum
      _ ≤ (∑ i : Fin n, ‖u i‖^2) * ε := mul_le_mul_of_nonneg_left (hN₀ N hN) hA
      _ ≤ (C * ‖S.toLp 2 volume‖^2) * ε := mul_le_mul_of_nonneg_right (hmass u) hε.le
      _ = _ := by dsimp [ε]; field_simp [ne_of_gt hC] <;> ring
  change neutralNF598SmoothWeil S - neutralIV095FiniteDiagonal M N S ≤ _ at herr
  change (1/5:ℝ) * ‖S.toLp 2 volume‖^2 ≤ neutralIV095FiniteDiagonal M N S
  linarith

#print axioms neutralIV095DiagonalTail_data
#print axioms neutralIV095TailProfile_sum_le
#print axioms neutralIV095DiagonalTail_sum_le
#print axioms neutralIV095DiagonalTailTrace_eventual
#print axioms neutralIV095OriginalCollarSpan_uniform_finite_margin

end
end WeilDefect
