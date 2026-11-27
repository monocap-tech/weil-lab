import WeilDefect.Arithmetic.ActualZetaIV106E18JCellClosure
import WeilDefect.Arithmetic.ActualZetaIV106E18K1PolynomialMoments

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap ComplexConjugate

/-- Exact agreement with the already staged clipped polynomial, not a new trial. -/
theorem neutralIV106E18K2Poly_eq (h t : ℝ) :
    neutralIV106E18IPoly h t = neutralIV106E18K1Poly h t := by
  unfold neutralIV106E18IPoly neutralIV106E18K1Poly
    neutralIV106E18K1B3 neutralIV106E18K1B1
  ring

/-- Physical affine Jacobian and the exact exponential scale. This identity
retains arbitrary rates, including those needed for the Gauss-series rows. -/
theorem neutralIV106E18K2Affine (l h s : ℝ) (hh : 0 < h) :
    (∫ x in l..l+h, neutralIV106E18ITrial l h x * (Real.exp (s*x) : ℂ)) =
      Complex.ofReal (h*Real.exp (s*l)) *
        Complex.ofReal (∫ t in (0:ℝ)..1, Real.exp ((s*h)*t)*neutralIV106E18K1Poly h t) := by
  let F : ℝ → ℂ := fun x => neutralIV106E18ITrial l h x * (Real.exp (s*x) : ℂ)
  have hchange :
      (∫ x in l..l+h, F x) = h • (∫ t in (0:ℝ)..1, F (h*t+l)) := by
    have he := intervalIntegral.smul_integral_comp_mul_add F
      (a := (0:ℝ)) (b := 1) h l
    simpa [add_comm] using he.symm
  have he : (∫ t in (0:ℝ)..1, F (h*t+l)) =
      ∫ t in (0:ℝ)..1, (Real.exp (s*l) : ℂ) *
        ((Real.exp ((s*h)*t)*neutralIV106E18K1Poly h t : ℝ) : ℂ) := by
    apply intervalIntegral.integral_congr
    intro t ht
    rw [uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)] at ht
    have hx : h*t+l ∈ Set.Icc l (l+h) := by
      constructor
      · nlinarith [mul_nonneg hh.le ht.1]
      · nlinarith [mul_nonneg hh.le (sub_nonneg.mpr ht.2)]
    have ha : (h*t+l-l)/h = t := by field_simp [hh.ne'] <;> ring
    dsimp [F]
    rw [neutralIV106E18ITrial_inside l h hh _ hx, ha, neutralIV106E18K2Poly_eq]
    rw [show s*(h*t+l) = s*l+(s*h)*t by ring, Real.exp_add]
    push_cast
    ring
  change (∫ x in l..l+h, F x) = _
  rw [hchange, he, intervalIntegral.integral_const_mul, intervalIntegral.integral_ofReal]
  rw [Complex.real_smul, Complex.ofReal_mul]
  ring

/-- The whole physical trial has the literal cell integral as its window moment.
No approximate moment correction is used for the trial itself. -/
theorem neutralIV106E18K2Window_moment (a l h s : ℝ) (hh : 0 < h)
    (hwin : Set.Icc l (l+h) ⊆ Set.Icc (-a) a) :
    sourceWindowMoment a s ((neutralIV106E18JTrial_memLp l h hh).toLp _) =
      Complex.ofReal (h*Real.exp (s*l)) *
        Complex.ofReal (∫ t in (0:ℝ)..1, Real.exp ((s*h)*t)*neutralIV106E18K1Poly h t) := by
  let f := neutralIV106E18ITrial l h
  let F : ℝ → ℂ := fun x => f x * (Real.exp (s*x) : ℂ)
  have he : sourceWindowMoment a s ((neutralIV106E18JTrial_memLp l h hh).toLp _) =
      ∫ x in Set.Icc (-a) a, F x := by
    change (∫ x in Set.Icc (-a) a,
      (neutralIV106E18JTrial_memLp l h hh).toLp _ x * (Real.exp (s*x) : ℂ)) = _
    apply integral_congr_ae
    filter_upwards [ae_restrict_of_ae
      (neutralIV106E18JTrial_memLp l h hh).coeFn_toLp] with x hx
    rw [hx]
  rw [he]
  have hzero : ∀ x ∉ Set.Icc l (l+h), F x = 0 := by
    intro x hx
    simp [F,f,neutralIV106E18ITrial_outside l h hh x hx]
  rw [setIntegral_eq_integral_of_forall_compl_eq_zero
    (fun x hx => hzero x (fun hmem => hx (hwin hmem))),
    ← setIntegral_eq_integral_of_forall_compl_eq_zero hzero,
    integral_Icc_eq_integral_Ioc, ← intervalIntegral.integral_of_le (by linarith : l ≤ l+h)]
  exact neutralIV106E18K2Affine l h s hh

theorem neutralIV106E18K2Moment_zero (a l h s : ℝ) (hh : 0 < h)
    (hwin : Set.Icc l (l+h) ⊆ Set.Icc (-a) a)
    (hs : s = 0 ∨ s = 1/2 ∨ s = -(1/2)) :
    sourceWindowMoment a s ((neutralIV106E18JTrial_memLp l h hh).toLp _) = 0 := by
  rw [neutralIV106E18K2Window_moment a l h s hh hwin,
    neutralIV106E18K1Zero h (s*h) (by
      rcases hs with rfl | rfl | rfl
      · left; ring
      · right; left; ring
      · right; right; ring)]
  simp

theorem neutralIV106E18K2Both_moments (a l h : ℝ) (hh : 0 < h)
    (hwin : Set.Icc l (l+h) ⊆ Set.Icc (-a) a) :
    neutralIV106E18HMoments a ((neutralIV106E18JTrial_memLp l h hh).toLp _) = 0 := by
  apply (neutralIV106E18HMoments_zero _ _).mpr
  exact ⟨neutralIV106E18K2Moment_zero a l h _ hh hwin (Or.inr (Or.inr rfl)),
    neutralIV106E18K2Moment_zero a l h _ hh hwin (Or.inr (Or.inl rfl))⟩

/-- Both pole moments are now discharged by the polynomial itself.
The finite buffered geometry is the remaining literal premise. -/
theorem neutralIV106E18K2Trial_response (k : ℕ) (hk : 0 < k) (i : Fin k)
    (l h ε : ℝ) (hh : 0 < h) (hε : 0 < ε)
    (hwin : closedBall (l+h/2) (h/2+ε) ⊆ Set.Icc (-(11/10:ℝ)) (11/10))
    {δ : ℝ} (hδ : 0 < δ)
    (hgap : ∀ x ∈ Set.Icc (4393/4000:ℝ) (4399/4000),
      ∀ y ∈ closedBall (l+h/2) (h/2+ε), δ ≤ |x-y|)
    (hshift : ∀ n ∈ rightLimitPrimePowerFinset (11/10:ℝ),
      ∀ x ∈ closedBall (l+h/2) (h/2+ε),
      x-Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000) ∧
      x+Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000)) :
    inner ℂ (neutralIV105CResponse k hk i)
      ((neutralIV106E18JTrial_memLp l h hh).toLp _) =
    ∫ x, conj (neutralIV100Carrier k hk i x) *
      (∫ y, neutralIV106E18ITrial l h y *
        ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  apply neutralIV106E18JTrial_response k hk i l h ε hh hε hwin hδ hgap hshift
  apply neutralIV106E18K2Both_moments _ l h hh
  intro x hx
  apply hwin
  rw [mem_closedBall,Real.dist_eq,abs_le]
  constructor <;> linarith [hx.1,hx.2]

#print axioms neutralIV106E18K2Poly_eq
#print axioms neutralIV106E18K2Affine
#print axioms neutralIV106E18K2Window_moment
#print axioms neutralIV106E18K2Moment_zero
#print axioms neutralIV106E18K2Both_moments
#print axioms neutralIV106E18K2Trial_response
end
end WeilDefect
