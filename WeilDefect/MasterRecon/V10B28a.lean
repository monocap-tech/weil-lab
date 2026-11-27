import WeilDefect.MasterRecon.V10B27b

/-! V10B28a: reflection and assembly of the restricted scalar action.
Each one-sided integral is split on disjoint Ioc pieces. Integrability
of the pieces and the already-staged scalar cancellation are explicit. -/
namespace WeilDefect.MasterRecon.V10B28a

open MeasureTheory Set
open V10B24b (zeroExtend physicalTerm b h)

def reflect (L : ℝ) (p : ℝ → ℂ) (x : ℝ) : ℂ := p (L-x)

theorem reflect_zero (L : ℝ) (p : ℝ → ℂ) (x : ℝ) :
    zeroExtend L (reflect L p) (L-x) = zeroExtend L p x := by
  have hm : L-x ∈ Icc 0 L ↔ x ∈ Icc 0 L := by
    simp only [mem_Icc]
    constructor <;> intro hh <;> constructor <;> linarith [hh.1,hh.2]
  by_cases hx : x ∈ Icc 0 L
  · unfold zeroExtend reflect
    rw [indicator_of_mem (hm.mpr hx),indicator_of_mem hx,show L-(L-x)=x by ring]
  · unfold zeroExtend
    rw [indicator_of_notMem (fun h => hx (hm.mp h)),indicator_of_notMem hx]

theorem reflect_shift (L : ℝ) (p : ℝ → ℂ) (x r : ℝ) :
    zeroExtend L (reflect L p) ((L-x)-r) = zeroExtend L p (x+r) := by
  rw [show L-x-r=L-(x+r) by ring,reflect_zero]

theorem reflect_inside (L x : ℝ) (hx : x ∈ Ioo 0 L) :
    L-x ∈ Ioo 0 L := ⟨by linarith [hx.2],by linarith [hx.1]⟩

noncomputable def diffTerm (L : ℝ) (p : ℝ → ℂ) (x r : ℝ) : ℂ :=
  ((1/(2*r):ℝ):ℂ)*(p x-zeroExtend L p (x-r))

noncomputable def regTerm (L : ℝ) (p : ℝ → ℂ) (x r : ℝ) : ℂ :=
  (h r:ℂ)*zeroExtend L p (x-r)

noncomputable def singular (p : ℝ → ℂ) (x : ℝ) : ℂ :=
  ∫ r in Ioc (0:ℝ) x, ((1/(2*r):ℝ):ℂ)*(p x-p (x-r))

noncomputable def regular (p : ℝ → ℂ) (x : ℝ) : ℂ :=
  ∫ r in Ioc (0:ℝ) x, (h r:ℂ)*p (x-r)

theorem partition (L x : ℝ) (hx : x ∈ Ioo 0 L) :
    Ioc (0:ℝ) x ∪ Ioc x L = Ioc 0 L := by
  ext r
  simp only [mem_union,mem_Ioc]
  constructor
  · rintro (hr|hr)
    · exact ⟨hr.1,hr.2.trans hx.2.le⟩
    · exact ⟨hx.1.trans hr.1,hr.2⟩
  · intro hr
    by_cases h : r ≤ x
    · exact Or.inl ⟨hr.1,h⟩
    · exact Or.inr ⟨lt_of_not_ge h,hr.2⟩

theorem partition_disjoint (L x : ℝ) : Disjoint (Ioc (0:ℝ) x) (Ioc x L) := by
  apply Set.disjoint_left.mpr
  intro r h₁ h₂
  exact (not_lt_of_ge h₁.2) h₂.1

theorem diff_integral (L x : ℝ) (p : ℝ → ℂ) (hx : x ∈ Ioo 0 L)
    (hi : IntegrableOn (diffTerm L p x) (Ioc 0 L)) :
    (∫ r in Ioc (0:ℝ) L, diffTerm L p x r) =
      singular p x+((Real.log L-Real.log x:ℝ):ℂ)*p x/2 := by
  have h₁ : Ioc (0:ℝ) x ⊆ Ioc 0 L := fun r hr => ⟨hr.1,hr.2.trans hx.2.le⟩
  have h₂ : Ioc x L ⊆ Ioc 0 L := fun r hr => ⟨hx.1.trans hr.1,hr.2⟩
  rw [← partition L x hx,setIntegral_union (partition_disjoint L x) measurableSet_Ioc
    (hi.mono_set h₁) (hi.mono_set h₂)]
  congr 1
  · unfold singular
    apply setIntegral_congr_fun measurableSet_Ioc
    intro r hr
    unfold diffTerm
    rw [V10B27b.left_difference_inside L x r p hx hr]
  · exact V10B27b.left_log_piece L x p hx

theorem reg_integral (L x : ℝ) (p : ℝ → ℂ) (hx : x ∈ Ioo 0 L)
    (hi : IntegrableOn (regTerm L p x) (Ioc 0 L)) :
    (∫ r in Ioc (0:ℝ) L, regTerm L p x r) = regular p x := by
  have h₁ : Ioc (0:ℝ) x ⊆ Ioc 0 L := fun r hr => ⟨hr.1,hr.2.trans hx.2.le⟩
  have h₂ : Ioc x L ⊆ Ioc 0 L := fun r hr => ⟨hx.1.trans hr.1,hr.2⟩
  rw [← partition L x hx,setIntegral_union (partition_disjoint L x) measurableSet_Ioc
    (hi.mono_set h₁) (hi.mono_set h₂)]
  have he : (∫ r in Ioc x L, regTerm L p x r) = 0 := by
    rw [← integral_zero (α := ℝ) (E := ℂ) (μ := volume.restrict (Ioc x L))]
    apply setIntegral_congr_fun measurableSet_Ioc
    intro r hr
    unfold regTerm
    rw [V10B24b.outside_shift_left L p x r hx hr.1,mul_zero]
  rw [he,add_zero]
  unfold regular
  apply setIntegral_congr_fun measurableSet_Ioc
  intro r hr
  unfold regTerm zeroExtend
  rw [indicator_of_mem (show x-r ∈ Icc 0 L from ⟨by linarith [hr.2],by linarith [hr.1,hx.2]⟩)]

theorem restricted_near (L x r : ℝ) (p : ℝ → ℂ) (hx : x ∈ Ioo 0 L)
    (hr : 0 < r) :
    physicalTerm L p x r =
      ((b r-1/r:ℝ):ℂ)*p x + diffTerm L p x r +
        diffTerm L (reflect L p) (L-x) r - regTerm L p x r -
        regTerm L (reflect L p) (L-x) r := by
  rw [V10B24b.restricted_split L p x r hx hr]
  unfold diffTerm regTerm
  rw [reflect_shift]
  simp only [reflect,show L-(L-x)=x by ring]
  ring

noncomputable def model (L : ℝ) (p : ℝ → ℂ) (x : ℝ) : ℂ :=
  ((-Real.log (2*L)+Real.log L-(Real.log x+Real.log (L-x))/2:ℝ):ℂ)*p x+
    singular p x+singular (reflect L p) (L-x)-
    regular p x-regular (reflect L p) (L-x)

theorem restricted_action (L x : ℝ) (p : ℝ → ℂ) (hx : x ∈ Ioo 0 L)
    (hd₁ : IntegrableOn (diffTerm L p x) (Ioc 0 L))
    (hd₂ : IntegrableOn (diffTerm L (reflect L p) (L-x)) (Ioc 0 L))
    (hr₁ : IntegrableOn (regTerm L p x) (Ioc 0 L))
    (hr₂ : IntegrableOn (regTerm L (reflect L p) (L-x)) (Ioc 0 L))
    (hconstant : (∫ r in Ioc (0:ℝ) L, b r-1/r)+(∫ r in Ioi L, b r) = -Real.log (2*L)) :
    (∫ r in Ioi (0:ℝ), physicalTerm L p x r) = model L p x := by
  have hL := hx.1.trans hx.2
  let A := fun r : ℝ => ((b r-1/r:ℝ):ℂ)*p x
  let B := fun r : ℝ => (b r:ℂ)*p x
  have ha : IntegrableOn A (Ioc 0 L) :=
    (Complex.ofRealCLM.integrable_comp (V10B26b.near_integrable L)).mul_const _
  have hb : IntegrableOn B (Ioi L) :=
    (Complex.ofRealCLM.integrable_comp (V10B26b.far_integrable L hL)).mul_const _
  have hn : IntegrableOn (physicalTerm L p x) (Ioc 0 L) := by
    apply ((((ha.add hd₁).add hd₂).sub hr₁).sub hr₂).congr
    rw [ae_restrict_iff' measurableSet_Ioc]
    exact Eventually.of_forall fun r hr => (restricted_near L x r p hx hr.1).symm
  have hf : IntegrableOn (physicalTerm L p x) (Ioi L) := by
    apply hb.congr
    rw [ae_restrict_iff' measurableSet_Ioi]
    exact Eventually.of_forall fun r hr => (V10B24b.far_action L p x r hx hr.le).symm
  have hu : Ioc (0:ℝ) L ∪ Ioi L = Ioi 0 := by
    ext r
    simp only [mem_union,mem_Ioc,mem_Ioi]
    constructor
    · rintro (hr|hr)
      · exact hr.1
      · exact hL.trans hr
    · intro hr
      by_cases hh : r ≤ L
      · exact Or.inl ⟨hr,hh⟩
      · exact Or.inr (lt_of_not_ge hh)
  have hj : Disjoint (Ioc (0:ℝ) L) (Ioi L) := by
    apply Set.disjoint_left.mpr
    intro r hr hs
    exact (not_lt_of_ge hr.2) hs
  rw [← hu,setIntegral_union hj measurableSet_Ioi hn hf]
  have he : (∫ r in Ioc (0:ℝ) L, physicalTerm L p x r) =
      ∫ r in Ioc (0:ℝ) L, A r+diffTerm L p x r+
        diffTerm L (reflect L p) (L-x) r-regTerm L p x r-
        regTerm L (reflect L p) (L-x) r := by
    apply setIntegral_congr_fun measurableSet_Ioc
    exact fun r hr => restricted_near L x r p hx hr.1
  have he' : (∫ r in Ioi L, physicalTerm L p x r) = ∫ r in Ioi L, B r := by
    apply setIntegral_congr_fun measurableSet_Ioi
    exact fun r hr => V10B24b.far_action L p x r hx hr.le
  rw [he,he',integral_sub (((ha.add hd₁).add hd₂).sub hr₁) hr₂,
    integral_sub ((ha.add hd₁).add hd₂) hr₁,integral_add (ha.add hd₁) hd₂,
    integral_add ha hd₁,diff_integral L x p hx hd₁,
    diff_integral L (L-x) (reflect L p) (reflect_inside L x hx) hd₂,
    reg_integral L x p hx hr₁,
    reg_integral L (L-x) (reflect L p) (reflect_inside L x hx) hr₂]
  unfold A B
  rw [integral_mul_const,integral_mul_const,integral_complex_ofReal,integral_complex_ofReal]
  unfold model reflect
  rw [show L-(L-x)=x by ring]
  push_cast
  have hc := congrArg Complex.ofReal hconstant
  push_cast at hc
  linear_combination p x*hc

end WeilDefect.MasterRecon.V10B28a

#print axioms WeilDefect.MasterRecon.V10B28a.reflect_zero
#print axioms WeilDefect.MasterRecon.V10B28a.reflect_shift
#print axioms WeilDefect.MasterRecon.V10B28a.reflect_inside
#print axioms WeilDefect.MasterRecon.V10B28a.partition
#print axioms WeilDefect.MasterRecon.V10B28a.partition_disjoint
#print axioms WeilDefect.MasterRecon.V10B28a.diff_integral
#print axioms WeilDefect.MasterRecon.V10B28a.reg_integral
#print axioms WeilDefect.MasterRecon.V10B28a.restricted_near
#print axioms WeilDefect.MasterRecon.V10B28a.restricted_action
