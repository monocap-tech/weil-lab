import WeilDefect.Arithmetic.ActualZetaIV106E10IntegratedCoercivity
import WeilDefect.Arithmetic.ActualZetaIV106E17AExplicitShift
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Analysis.Complex.RealDeriv

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap FourierTransform
open scoped SchwartzMap LineDeriv FourierTransform InnerProduct ComplexConjugate BigOperators

def neutralIV106W02PCellMap :
    NeutralLogHilbertCarrier (11/10:ℝ) →L[ℂ] (Fin 665 → ℂ) :=
  ContinuousLinearMap.pi fun i =>
    neutralIV106C3PhysicalRow (11/10:ℝ) (neutralIV106C3CellColumn (11/10:ℝ) 665 i)

theorem neutralIV106W02PCellMeans (q : NeutralLogHilbertCarrier (11/10:ℝ)) (v : 𝓢(ℝ,ℂ))
    (hv : neutralLogPhysical q.val = v.toLp 2 volume)
    (hq : neutralIV106W02PCellMap q = 0) :
    ∀ j < 665, (∫ t in neutralIV106D6Endpoint j..neutralIV106D6Endpoint (j+1), v t) = 0 := by
  intro j hj
  let i : Fin 665 := ⟨j,hj⟩
  have hm := congrFun hq i
  change neutralIV106C3PhysicalRow (11/10:ℝ) (neutralIV106C3CellColumn (11/10:ℝ) 665 i) q = 0 at hm
  rw [neutralIV106C3PhysicalRow_eq, neutralIV106C3Cell_pair] at hm
  rw [hv] at hm
  have he : (∫ t in neutralIV106C3Cell (11/10:ℝ) 665 i, (v.toLp 2 volume) t) =
      ∫ t in neutralIV106C3Cell (11/10:ℝ) 665 i, v t := by
    apply setIntegral_congr_ae (show MeasurableSet (neutralIV106C3Cell (11/10:ℝ) 665 i)
      from measurableSet_Icc)
    filter_upwards [v.coeFn_toLp 2 volume] with t ht _
    exact ht
  rw [he] at hm
  have hc : neutralIV106C3Cell (11/10:ℝ) 665 i =
      Set.Icc (neutralIV106D6Endpoint j) (neutralIV106D6Endpoint (j+1)) := by
    unfold neutralIV106C3Cell neutralIV106D6Endpoint
    dsimp [i]
    push_cast
    norm_num
  rw [hc] at hm
  apply neutralIV106D5Closed_cell _ _ _ _ hm
  exact sub_nonneg.mp (by rw [neutralIV106D6Endpoint_width]; norm_num)

theorem neutralIV106W02PCellPrimitive (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106W02PCellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    ∃ v V : 𝓢(ℝ,ℂ), neutralLogPhysical q.val = v.toLp 2 volume ∧
      ∂_{(1:ℝ)} V = v ∧
      ‖V.toLp 2 volume‖^2 ≤ (11/3325:ℝ)^2/6 * ‖v.toLp 2 volume‖^2 := by
  rcases hd with ⟨v,hv,hphys⟩
  have hm := neutralIV106W02PCellMeans q v hphys hq
  have hends := neutralIV106D3Endpoint v neutralIV106D6Endpoint 665 hm
  have htotal := hends 665 (by omega)
  rw [neutralIV106D6Endpoint_zero, neutralIV106D6Endpoint_last] at htotal
  obtain ⟨V,hV,hder,hout⟩ := neutralIV106D3Schwartz_primitive v
    (-(11/10:ℝ)) (11/10:ℝ) (by norm_num) hv htotal
  have hlocal (j : ℕ) (hj : j < 665) (x : ℝ)
      (_ : x ∈ Set.Icc (neutralIV106D6Endpoint j) (neutralIV106D6Endpoint (j+1))) :
      V x = ∫ t in neutralIV106D6Endpoint j..x, v t := by
    have he := intervalIntegral.integral_add_adjacent_intervals
      (v.continuous.intervalIntegrable (μ := volume) (neutralIV106D6Endpoint 0) (neutralIV106D6Endpoint j))
      (v.continuous.intervalIntegrable (μ := volume) (neutralIV106D6Endpoint j) x)
    rw [hends j (Nat.le_of_lt hj), zero_add, neutralIV106D6Endpoint_zero] at he
    rw [hV x, he]
  have hmass := neutralIV106D5Partition_energy v V v.continuous V.continuous
    neutralIV106D6Endpoint 665 (11/3325:ℝ) (by norm_num)
    (fun j _ => neutralIV106D6Endpoint_width j) hm hlocal
  rw [neutralIV106D6Endpoint_zero, neutralIV106D6Endpoint_last,
    neutralIV106D6Window_mass V _ _ (by norm_num) hout,
    neutralIV106D6Window_mass v _ _ (by norm_num) hv] at hmass
  exact ⟨v,V,hphys,hder,hmass⟩

theorem neutralIV106W02PCellReciprocal (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106W02PCellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    Integrable (fun ξ : ℝ => ‖(𝓕 (neutralLogPhysical q.val) : RealComplexL2) ξ‖^2 / ξ^2) ∧
    (∫ ξ : ℝ, ‖(𝓕 (neutralLogPhysical q.val) : RealComplexL2) ξ‖^2 / ξ^2) ≤
      (2*Real.pi^2/3)*(11/3325:ℝ)^2*‖neutralLogPhysical q.val‖^2 := by
  obtain ⟨v,V,hphys,hder,hmass⟩ := neutralIV106W02PCellPrimitive q hq hd
  rw [hphys]
  exact ⟨neutralIV106D6Reciprocal_integrable V v hder,
    neutralIV106D2Reciprocal_bound V v (11/3325:ℝ) hder hmass⟩

theorem neutralIV106W02PCellGamma (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106W02PCellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (Real.log 118+1/2-(118^2*Real.pi^2/3+25/12)*(11/3325)^2)*
      ‖neutralLogPhysical q.val‖^2 ≤ neutralIV106E10Gamma q := by
  obtain ⟨hr,hj⟩ := neutralIV106W02PCellReciprocal q hq hd
  obtain ⟨hf,hm⟩ := neutralIV106E10Mass q
  have he := neutralIV106D1Energy_receiver
    (fun ξ => compactWindowArchimedeanSymbol (2*Real.pi*ξ)*neutralIV106E10Density q ξ)
    (neutralIV106E10Density q) (fun ξ => neutralIV106E10Density q ξ / ξ^2)
    (Real.log 118+1/2) (118^2/2+25/(8*Real.pi^2))
    (‖neutralLogPhysical q.val‖^2) ((2*Real.pi^2/3)*(11/3325)^2)
    (neutralIV106E10Gamma_integrable q) hf hr (by positivity) hm hj
    (by
      have hz : ∀ᵐ ξ : ℝ ∂volume, ξ ≠ 0 := by
        simpa using (measure_singleton (0:ℝ) : volume ({0}:Set ℝ) = 0)
      filter_upwards [hz] with ξ hξ
      have hp := mul_le_mul_of_nonneg_right (neutralIV106E10Point ξ hξ)
        (show 0 ≤ neutralIV106E10Density q ξ from sq_nonneg _)
      convert hp using 1 <;> ring)
  change _ ≤ neutralIV106E10Gamma q at he
  have hc : (118^2/2+25/(8*Real.pi^2))*((2*Real.pi^2/3)*(11/3325)^2) =
      (118^2*Real.pi^2/3+25/12)*(11/3325)^2 := by
    field_simp [Real.pi_pos.ne']
    <;> ring
  rwa [hc] at he

theorem neutralIV106W02PPrimitiveEndpoints (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106W02PCellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    ∃ v V : 𝓢(ℝ,ℂ), neutralLogPhysical q.val = v.toLp 2 volume ∧
      ∂_{(1:ℝ)} V = v ∧
      (∀ x, V x = ∫ t in -(11/10:ℝ)..x, v t) ∧
      V (11/10:ℝ) = 0 ∧
      ‖V.toLp 2 volume‖^2 ≤ (11/3325:ℝ)^2/6 * ‖v.toLp 2 volume‖^2 := by
  rcases hd with ⟨v,hv,hphys⟩
  have hm := neutralIV106W02PCellMeans q v hphys hq
  have hends := neutralIV106D3Endpoint v neutralIV106D6Endpoint 665 hm
  have htotal := hends 665 (by omega)
  rw [neutralIV106D6Endpoint_zero, neutralIV106D6Endpoint_last] at htotal
  obtain ⟨V,hV,hder,hout⟩ := neutralIV106D3Schwartz_primitive v
    (-(11/10:ℝ)) (11/10:ℝ) (by norm_num) hv htotal
  have hlocal (j : ℕ) (hj : j < 665) (x : ℝ)
      (_ : x ∈ Set.Icc (neutralIV106D6Endpoint j) (neutralIV106D6Endpoint (j+1))) :
      V x = ∫ t in neutralIV106D6Endpoint j..x, v t := by
    have he := intervalIntegral.integral_add_adjacent_intervals
      (v.continuous.intervalIntegrable (μ := volume) (neutralIV106D6Endpoint 0) (neutralIV106D6Endpoint j))
      (v.continuous.intervalIntegrable (μ := volume) (neutralIV106D6Endpoint j) x)
    rw [hends j (Nat.le_of_lt hj), zero_add, neutralIV106D6Endpoint_zero] at he
    rw [hV x, he]
  have hmass := neutralIV106D5Partition_energy v V v.continuous V.continuous
    neutralIV106D6Endpoint 665 (11/3325:ℝ) (by norm_num)
    (fun j _ => neutralIV106D6Endpoint_width j) hm hlocal
  rw [neutralIV106D6Endpoint_zero, neutralIV106D6Endpoint_last,
    neutralIV106D6Window_mass V _ _ (by norm_num) hout,
    neutralIV106D6Window_mass v _ _ (by norm_num) hv] at hmass
  exact ⟨v,V,hphys,hder,hV,(hV (11/10:ℝ)).trans htotal,hmass⟩

/-- A coarse global exponential-column bound, independent of the cells. -/
theorem neutralIV106W02PExpBound (s x : ℝ)
    (hs : s = -(1/2) ∨ s = 1/2) (hx : x ∈ Set.Icc (-(11/10:ℝ)) (11/10)) :
    Real.exp (s*x) ≤ 2 := by
  have hh : s*x ≤ (11/20:ℝ) := by
    rcases hs with rfl | rfl <;> nlinarith [hx.1,hx.2]
  have he := Real.abs_exp_sub_one_sub_id_le (x := (11/20:ℝ)) (by norm_num)
  have h := (abs_le.mp he).2
  have h2 : Real.exp (11/20:ℝ) ≤ 2 := by linarith
  exact (Real.exp_le_exp.mpr hh).trans h2

theorem neutralIV106W02PColumnNorm (s : ℝ) (hs : s = -(1/2) ∨ s = 1/2) :
    ‖neutralMomentColumnL2 (11/10:ℝ) s‖^2 ≤ (44/5:ℝ) := by
  let f := neutralMomentColumnL2 (11/10:ℝ) s
  have hi : Integrable (fun x : ℝ => ‖f x‖^2) :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable f)).mp (Lp.memLp f)
  have hc : Integrable ((Set.Icc (-(11/10:ℝ)) (11/10)).indicator
      (fun _ : ℝ => (4:ℝ))) := by
    exact (continuous_const.integrableOn_Icc).integrable_indicator measurableSet_Icc
  have he : (f : ℝ → ℂ) =ᵐ[volume] neutralMomentColumn (11/10:ℝ) s :=
    (neutralMomentColumn_memLp (11/10:ℝ) s).coeFn_toLp
  have hb := integral_mono_ae hi hc (by
    filter_upwards [he] with x hx
    rw [hx]
    by_cases hxw : x ∈ Set.Icc (-(11/10:ℝ)) (11/10)
    · simp only [neutralMomentColumn, Set.indicator_of_mem hxw, Complex.norm_real,
        Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
      exact pow_le_pow_left₀ (Real.exp_pos _).le (neutralIV106W02PExpBound s x hs hxw) 2
    · simp [neutralMomentColumn,hxw])
  rw [integral_indicator measurableSet_Icc, integral_Icc_eq_integral_Ioc,
    ← intervalIntegral.integral_of_le (by norm_num : -(11/10:ℝ) ≤ 11/10),
    intervalIntegral.integral_const] at hb
  change ‖f‖^2 ≤ _
  rw [neutralPhysicalL2_norm_sq]
  norm_num [smul_eq_mul] at hb ⊢
  exact hb

/-- Literal physical moment on a Schwartz representative. -/
theorem neutralIV106W02PSchwartzMoment (s : ℝ) (v : 𝓢(ℝ,ℂ)) :
    sourceWindowMoment (11/10:ℝ) s (v.toLp 2 volume) =
      ∫ x in -(11/10:ℝ)..11/10, (Real.exp (s*x):ℂ)*v x := by
  unfold sourceWindowMoment
  rw [intervalIntegral.integral_of_le (by norm_num : -(11/10:ℝ) ≤ 11/10),
    ← integral_Icc_eq_integral_Ioc]
  apply setIntegral_congr_ae measurableSet_Icc
  filter_upwards [v.coeFn_toLp 2 volume] with x hx _
  rw [hx]
  ring

/-- Integration by parts retains the actual two signed exponential moments. -/
theorem neutralIV106W02PPrimitiveMoment (s : ℝ) (v V : 𝓢(ℝ,ℂ))
    (hV : ∀ x, V x = ∫ t in -(11/10:ℝ)..x, v t)
    (hend : V (11/10:ℝ) = 0) :
    sourceWindowMoment (11/10:ℝ) s (v.toLp 2 volume) =
      -(s:ℂ)*sourceWindowMoment (11/10:ℝ) s (V.toLp 2 volume) := by
  let u : ℝ → ℂ := fun x => (Real.exp (s*x):ℂ)
  let u' : ℝ → ℂ := fun x => (s:ℂ)*u x
  have hu : Continuous u := by unfold u; fun_prop
  have hu' : Continuous u' := by unfold u' u; fun_prop
  have hdu (x : ℝ) : HasDerivAt u (u' x) x := by
    dsimp [u,u']
    convert (((hasDerivAt_id x).const_mul s).exp.ofReal_comp) using 1 <;>
      simp [Function.id_def, mul_comm]
  have hdV (x : ℝ) : HasDerivAt (fun t => V t) (v x) x := by
    rw [show (fun t => V t) = (fun t => ∫ y in -(11/10:ℝ)..t, v y) from funext hV]
    exact (v.continuous.integral_hasStrictDerivAt (-(11/10:ℝ)) x).hasDerivAt
  have hleft : V (-(11/10:ℝ)) = 0 := by rw [hV,intervalIntegral.integral_same]
  have h := intervalIntegral.integral_mul_deriv_eq_deriv_mul_of_hasDerivAt
    (a := -(11/10:ℝ)) (b := (11/10:ℝ))
    hu.continuousOn V.continuous.continuousOn
    (fun x _ => hdu x) (fun x _ => hdV x)
    (hu'.intervalIntegrable _ _) (v.continuous.intervalIntegrable _ _)
  rw [hend,hleft,mul_zero,mul_zero,sub_self,zero_sub] at h
  rw [neutralIV106W02PSchwartzMoment,neutralIV106W02PSchwartzMoment]
  change (∫ x in -(11/10:ℝ)..11/10, u x*v x) = -(s:ℂ)*(∫ x in -(11/10:ℝ)..11/10,u x*V x)
  rw [h]
  dsimp only [u']
  simp_rw [mul_assoc]
  rw [intervalIntegral.integral_const_mul]
  ring

/-- Physical moment error is controlled by the already bounded primitive. -/
theorem neutralIV106W02PPrimitiveMomentBound
    (s : ℝ) (hs : s = -(1/2) ∨ s = 1/2) (v V : 𝓢(ℝ,ℂ))
    (hV : ∀ x, V x = ∫ t in -(11/10:ℝ)..x, v t)
    (hend : V (11/10:ℝ) = 0)
    (hmass : ‖V.toLp 2 volume‖^2 ≤ (11/3325:ℝ)^2/6*‖v.toLp 2 volume‖^2) :
    ‖sourceWindowMoment (11/10:ℝ) s (v.toLp 2 volume)‖^2 ≤
      (1331/331668750:ℝ)*‖v.toLp 2 volume‖^2 := by
  have hc := neutralIV106W02PColumnNorm s hs
  have hb : ‖sourceWindowMoment (11/10:ℝ) s (V.toLp 2 volume)‖^2 ≤
      (44/5:ℝ)*‖V.toLp 2 volume‖^2 := by
    rw [← neutralMomentColumnL2_inner]
    calc
      _ ≤ (‖neutralMomentColumnL2 (11/10:ℝ) s‖*‖V.toLp 2 volume‖)^2 :=
        pow_le_pow_left₀ (norm_nonneg _) (norm_inner_le_norm _ _) 2
      _ = ‖neutralMomentColumnL2 (11/10:ℝ) s‖^2*‖V.toLp 2 volume‖^2 := by ring
      _ ≤ _ := mul_le_mul_of_nonneg_right hc (sq_nonneg _)
  have hn : ‖(-(s:ℂ))‖ = (1/2:ℝ) := by
    rcases hs with rfl | rfl <;> norm_num [Complex.norm_real]
  rw [neutralIV106W02PPrimitiveMoment s v V hV hend,norm_mul,hn]
  nlinarith only [hb,hmass]

/-- Signed pole loss from cell means on the supported core; no approximation premise. -/
theorem neutralIV106W02PPoleLoss
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02PCellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    -(1331/165834375:ℝ)*‖neutralLogPhysical q.val‖^2 ≤
      2*(conj (sourceWindowMoment (11/10) (-(1/2)) (neutralLogPhysical q.val)) *
      sourceWindowMoment (11/10) (1/2) (neutralLogPhysical q.val)).re := by
  obtain ⟨v,V,hphys,hder,hV,hend,hmass⟩ := neutralIV106W02PPrimitiveEndpoints q hq hd
  have hm := neutralIV106W02PPrimitiveMomentBound (-(1/2)) (Or.inl rfl) v V hV hend hmass
  have hn := neutralIV106W02PPrimitiveMomentBound (1/2) (Or.inr rfl) v V hV hend hmass
  rw [hphys]
  let u := sourceWindowMoment (11/10:ℝ) (-(1/2)) (v.toLp 2 volume)
  let w := sourceWindowMoment (11/10:ℝ) (1/2) (v.toLp 2 volume)
  change ‖u‖^2 ≤ _ at hm
  change ‖w‖^2 ≤ _ at hn
  change _ ≤ 2*(conj u*w).re
  have h := Complex.abs_re_le_norm (conj u*w)
  rw [norm_mul,Complex.norm_conj] at h
  nlinarith only [neg_le_abs (conj u*w).re, h, hm, hn,
    sq_nonneg (‖u‖-‖w‖)]

theorem neutralIV106W02PEnergyDecomposition
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) :
    (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re =
    neutralIV106E10Gamma q - neutralIV106E10Prime q +
      2*(conj (sourceWindowMoment (11/10) (-(1/2)) (neutralLogPhysical q.val)) *
      sourceWindowMoment (11/10) (1/2) (neutralLogPhysical q.val)).re := by
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re]
  unfold neutralActualZetaCanonicalNativeQuadratic
  change (∫ ξ, rightLimitCompactWeilSymbolMathlib (11/10) ξ * neutralIV106E10Density q ξ) + _ = _
  unfold neutralIV106E10Gamma neutralIV106E10Prime
  rw [← integral_sub (neutralIV106E10Gamma_integrable q) (neutralIV106E10Prime_integrable q)]
  congr 1
  apply integral_congr_ae
  filter_upwards [] with ξ
  simp only [Pi.sub_apply, rightLimitCompactWeilSymbolMathlib, rightLimitCompactWeilSymbol]
  ring

theorem neutralIV106W02PCoreMass 
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02PCellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (1327460357/1326675000:ℝ)*‖neutralLogPhysical q.val‖^2 ≤
      (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  have hg := neutralIV106W02PCellGamma q hq hd
  have hb := mul_le_mul_of_nonneg_right neutralIV106E1Budget
    (sq_nonneg ‖neutralLogPhysical q.val‖)
  have hp' := neutralIV106E10Prime_bound q hd
  have hh := neutralIV106W02PPoleLoss q hq hd
  rw [neutralIV106W02PEnergyDecomposition]
  linarith only [hg,hb,hp',hh]

theorem neutralIV106W02PGammaShift
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) :
    ‖q‖^2 ≤ neutralIV106E10Gamma q + 12*‖neutralLogPhysical q.val‖^2 := by
  let f := neutralLogHilbertToCanonical q
  have hf := neutralIV106E10Gamma_integrable q
  have hm := neutralIV106E10Mass q
  have hw : Integrable (fun ξ => logarithmicFourierWeight ξ * neutralIV106E10Density q ξ) :=
    f.property.2
  have hi := integral_mono hw (hf.add (hm.1.const_mul 12)) (fun ξ => by
    have h := mul_le_mul_of_nonneg_right (neutralIV106E17AGamma_shift ξ)
      (show 0 ≤ neutralIV106E10Density q ξ from sq_nonneg _)
    simpa only [Pi.add_apply,add_mul] using h)
  change (∫ ξ, logarithmicFourierWeight ξ * neutralIV106E10Density q ξ) ≤
    ∫ ξ, compactWindowArchimedeanSymbol (2*Real.pi*ξ)*neutralIV106E10Density q ξ +
      12*neutralIV106E10Density q ξ at hi
  rw [integral_add hf (hm.1.const_mul 12), integral_const_mul, hm.2] at hi
  have hn : ‖q‖^2 = ∫ ξ, logarithmicFourierWeight ξ * neutralIV106E10Density q ξ := by
    rw [neutralLogHilbertCarrier_norm_sq]
    rfl
  rw [← hn] at hi
  exact hi

theorem neutralIV106W02PCoreLog17 
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02PCellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  have hm := neutralIV106W02PCoreMass q hq hd
  have hg := neutralIV106W02PGammaShift q
  have hP := neutralIV106E10Prime_bound q hd
  have hH := neutralIV106W02PPoleLoss q hq hd
  rw [neutralIV106W02PEnergyDecomposition] at hm ⊢
  linarith only [hm,hg,hP,hH,sq_nonneg ‖neutralLogPhysical q.val‖]

theorem neutralIV106W02PClosedLog17 
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02PCellMap q = 0) :
    (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  let S : Set (NeutralLogHilbertCarrier (11/10:ℝ)) :=
    {x | (1/17:ℝ)*‖x‖^2 ≤ (inner ℂ x (neutralActualZetaLogWeilFormOperator (11/10) x)).re}
  have hleft : Continuous (fun x : NeutralLogHilbertCarrier (11/10:ℝ) =>
      (1/17:ℝ)*‖x‖^2) := continuous_const.mul (continuous_norm.pow 2)
  have hright : Continuous (fun x : NeutralLogHilbertCarrier (11/10:ℝ) =>
      (inner ℂ x (neutralActualZetaLogWeilFormOperator (11/10) x)).re) :=
    Complex.continuous_re.comp
      (continuous_id.inner (neutralActualZetaLogWeilFormOperator (11/10)).continuous)
  have hc : IsClosed S := isClosed_le hleft hright
  have hs : (neutralIV106C3Core (11/10:ℝ) : Set (NeutralLogHilbertCarrier (11/10:ℝ))) ∩
      {x | neutralIV106W02PCellMap x = 0} ⊆ S := by
    intro x hx
    exact neutralIV106W02PCoreLog17 x hx.2 hx.1
  have h := closure_minimal hs hc
  rw [neutralIV106C3Core_kernel_closure (11/10:ℝ) (by norm_num) 665 neutralIV106W02PCellMap] at h
  exact h hq

#print axioms neutralIV106W02PCellMeans
#print axioms neutralIV106W02PCellPrimitive
#print axioms neutralIV106W02PCellReciprocal
#print axioms neutralIV106W02PCellGamma
#print axioms neutralIV106W02PPrimitiveEndpoints
#print axioms neutralIV106W02PExpBound
#print axioms neutralIV106W02PColumnNorm
#print axioms neutralIV106W02PSchwartzMoment
#print axioms neutralIV106W02PPrimitiveMoment
#print axioms neutralIV106W02PPrimitiveMomentBound
#print axioms neutralIV106W02PPoleLoss
#print axioms neutralIV106W02PEnergyDecomposition
#print axioms neutralIV106W02PCoreMass
#print axioms neutralIV106W02PGammaShift
#print axioms neutralIV106W02PCoreLog17
#print axioms neutralIV106W02PClosedLog17
end
end WeilDefect
