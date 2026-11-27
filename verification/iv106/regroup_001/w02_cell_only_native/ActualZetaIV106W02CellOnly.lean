import WeilDefect.Arithmetic.ActualZetaIV106E10IntegratedCoercivity
import WeilDefect.Arithmetic.ActualZetaIV106E17AExplicitShift

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap FourierTransform
open scoped SchwartzMap LineDeriv FourierTransform InnerProduct ComplexConjugate BigOperators

def neutralIV106W02CellMap :
    NeutralLogHilbertCarrier (11/10:ℝ) →L[ℂ] (Fin 665 → ℂ) :=
  ContinuousLinearMap.pi fun i =>
    neutralIV106C3PhysicalRow (11/10:ℝ) (neutralIV106C3CellColumn (11/10:ℝ) 665 i)

theorem neutralIV106W02CellMeans (q : NeutralLogHilbertCarrier (11/10:ℝ)) (v : 𝓢(ℝ,ℂ))
    (hv : neutralLogPhysical q.val = v.toLp 2 volume)
    (hq : neutralIV106W02CellMap q = 0) :
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

theorem neutralIV106W02CellPrimitive (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106W02CellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    ∃ v V : 𝓢(ℝ,ℂ), neutralLogPhysical q.val = v.toLp 2 volume ∧
      ∂_{(1:ℝ)} V = v ∧
      ‖V.toLp 2 volume‖^2 ≤ (11/3325:ℝ)^2/6 * ‖v.toLp 2 volume‖^2 := by
  rcases hd with ⟨v,hv,hphys⟩
  have hm := neutralIV106W02CellMeans q v hphys hq
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

theorem neutralIV106W02CellReciprocal (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106W02CellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    Integrable (fun ξ : ℝ => ‖(𝓕 (neutralLogPhysical q.val) : RealComplexL2) ξ‖^2 / ξ^2) ∧
    (∫ ξ : ℝ, ‖(𝓕 (neutralLogPhysical q.val) : RealComplexL2) ξ‖^2 / ξ^2) ≤
      (2*Real.pi^2/3)*(11/3325:ℝ)^2*‖neutralLogPhysical q.val‖^2 := by
  obtain ⟨v,V,hphys,hder,hmass⟩ := neutralIV106W02CellPrimitive q hq hd
  rw [hphys]
  exact ⟨neutralIV106D6Reciprocal_integrable V v hder,
    neutralIV106D2Reciprocal_bound V v (11/3325:ℝ) hder hmass⟩

theorem neutralIV106W02CellGamma (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106W02CellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (Real.log 118+1/2-(118^2*Real.pi^2/3+25/12)*(11/3325)^2)*
      ‖neutralLogPhysical q.val‖^2 ≤ neutralIV106E10Gamma q := by
  obtain ⟨hr,hj⟩ := neutralIV106W02CellReciprocal q hq hd
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

theorem neutralIV106W02CellAnnihilation
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02CellMap q = 0)
    (a : Fin 665 → ℂ) :
    inner ℂ (∑ j, a j • neutralIV106C3CellColumn (11/10:ℝ) 665 j)
      (neutralLogPhysical q.val) = 0 := by
  classical
  have hz (j : Fin 665) :
      inner ℂ (neutralIV106C3CellColumn (11/10:ℝ) 665 j)
        (neutralLogPhysical q.val) = 0 := by
    have h := congrFun hq j
    change neutralIV106C3PhysicalRow (11/10:ℝ)
      (neutralIV106C3CellColumn (11/10:ℝ) 665 j) q = 0 at h
    rwa [neutralIV106C3PhysicalRow_eq] at h
  simp only [sum_inner, inner_smul_left, hz, mul_zero, Finset.sum_const_zero]

theorem neutralIV106W02MomentBound
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02CellMap q = 0)
    (s : ℝ) (a : Fin 665 → ℂ)
    (ha : ‖neutralMomentColumnL2 (11/10:ℝ) s -
      ∑ j, a j • neutralIV106C3CellColumn (11/10:ℝ) 665 j‖^2 ≤ (1331/663337500:ℝ)) :
    ‖sourceWindowMoment (11/10:ℝ) s (neutralLogPhysical q.val)‖^2 ≤
      (1331/663337500:ℝ)*‖neutralLogPhysical q.val‖^2 := by
  let d := neutralMomentColumnL2 (11/10:ℝ) s -
    ∑ j, a j • neutralIV106C3CellColumn (11/10:ℝ) 665 j
  have he : inner ℂ d (neutralLogPhysical q.val) =
      sourceWindowMoment (11/10:ℝ) s (neutralLogPhysical q.val) := by
    dsimp only [d]
    rw [inner_sub_left, neutralIV106W02CellAnnihilation q hq a,
      sub_zero, neutralMomentColumnL2_inner]
  rw [← he]
  calc
    _ ≤ (‖d‖*‖neutralLogPhysical q.val‖)^2 :=
      pow_le_pow_left₀ (norm_nonneg _) (norm_inner_le_norm _ _) 2
    _ = ‖d‖^2*‖neutralLogPhysical q.val‖^2 := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_right ha (sq_nonneg _)

/-- The geometric premise is explicit, not an admitted theorem. -/
def neutralIV106W02PoleApprox : Prop :=
  ∀ s : ℝ, s = -(1/2) ∨ s = 1/2 →
    ∃ a : Fin 665 → ℂ, ‖neutralMomentColumnL2 (11/10:ℝ) s -
      ∑ j, a j • neutralIV106C3CellColumn (11/10:ℝ) 665 j‖^2 ≤ (1331/663337500:ℝ)

theorem neutralIV106W02PoleLoss (hp : neutralIV106W02PoleApprox)
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02CellMap q = 0) :
    -(1331/331668750:ℝ)*‖neutralLogPhysical q.val‖^2 ≤
      2*(conj (sourceWindowMoment (11/10) (-(1/2)) (neutralLogPhysical q.val)) *
      sourceWindowMoment (11/10) (1/2) (neutralLogPhysical q.val)).re := by
  obtain ⟨a,ha⟩ := hp (-(1/2)) (Or.inl rfl)
  obtain ⟨b,hb⟩ := hp (1/2) (Or.inr rfl)
  have hm := neutralIV106W02MomentBound q hq _ a ha
  have hn := neutralIV106W02MomentBound q hq _ b hb
  let u := sourceWindowMoment (11/10) (-(1/2)) (neutralLogPhysical q.val)
  let v := sourceWindowMoment (11/10) (1/2) (neutralLogPhysical q.val)
  change ‖u‖^2 ≤ _ at hm
  change ‖v‖^2 ≤ _ at hn
  change _ ≤ 2*(conj u*v).re
  have h := Complex.abs_re_le_norm (conj u*v)
  rw [norm_mul] at h
  have hconj : ‖conj u‖ = ‖u‖ := Complex.norm_conj u
  rw [hconj] at h
  nlinarith only [neg_le_abs (conj u*v).re, h, hm, hn,
    sq_nonneg (‖u‖-‖v‖)]

theorem neutralIV106W02EnergyDecomposition
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

theorem neutralIV106W02CoreMass (hp : neutralIV106W02PoleApprox)
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02CellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (1327465681/1326675000:ℝ)*‖neutralLogPhysical q.val‖^2 ≤
      (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  have hg := neutralIV106W02CellGamma q hq hd
  have hb := mul_le_mul_of_nonneg_right neutralIV106E1Budget
    (sq_nonneg ‖neutralLogPhysical q.val‖)
  have hp' := neutralIV106E10Prime_bound q hd
  have hh := neutralIV106W02PoleLoss hp q hq
  rw [neutralIV106W02EnergyDecomposition]
  linarith only [hg,hb,hp',hh]

theorem neutralIV106W02GammaShift
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

theorem neutralIV106W02CoreLog17 (hp : neutralIV106W02PoleApprox)
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02CellMap q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re := by
  have hm := neutralIV106W02CoreMass hp q hq hd
  have hg := neutralIV106W02GammaShift q
  have hP := neutralIV106E10Prime_bound q hd
  have hH := neutralIV106W02PoleLoss hp q hq
  rw [neutralIV106W02EnergyDecomposition] at hm ⊢
  linarith only [hm,hg,hP,hH,sq_nonneg ‖neutralLogPhysical q.val‖]

theorem neutralIV106W02ClosedLog17 (hp : neutralIV106W02PoleApprox)
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (hq : neutralIV106W02CellMap q = 0) :
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
      {x | neutralIV106W02CellMap x = 0} ⊆ S := by
    intro x hx
    exact neutralIV106W02CoreLog17 hp x hx.2 hx.1
  have h := closure_minimal hs hc
  rw [neutralIV106C3Core_kernel_closure (11/10:ℝ) (by norm_num) 665 neutralIV106W02CellMap] at h
  exact h hq

#print axioms neutralIV106W02CellMeans
#print axioms neutralIV106W02CellPrimitive
#print axioms neutralIV106W02CellReciprocal
#print axioms neutralIV106W02CellGamma
#print axioms neutralIV106W02CellAnnihilation
#print axioms neutralIV106W02MomentBound
#print axioms neutralIV106W02PoleLoss
#print axioms neutralIV106W02EnergyDecomposition
#print axioms neutralIV106W02CoreMass
#print axioms neutralIV106W02GammaShift
#print axioms neutralIV106W02CoreLog17
#print axioms neutralIV106W02ClosedLog17
end
end WeilDefect
