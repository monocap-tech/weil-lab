import WeilDefect.MasterRecon.V10B47b
import WeilDefect.MasterRecon.V10B46c
import WeilDefect.MasterRecon.V10B43a

/-! V10B47c: actual recovered polynomial trial pairings on the unit
interval. Physical support-coordinate and kernel identification remain
separate. Trials here use integer numerators, not the divided bank. -/
namespace WeilDefect.MasterRecon.V10B47c
open MeasureTheory Set Polynomial
open scoped BigOperators Matrix
open WeilDefect.MasterRecon.V10B33a
open WeilDefect.MasterRecon.V10B45a
open WeilDefect.MasterRecon.V10B46a
open WeilDefect.MasterRecon.V10B46b
open WeilDefect.MasterRecon.V10B46c
open WeilDefect.MasterRecon.V10B47b
open WeilDefect.MasterRecon.V10B39b
open WeilDefect.MasterRecon.V10B40a
open WeilDefect.MasterRecon.V10B43a

noncomputable def trial (col : Fin 16) (x : ℝ) :=
  ∑ j ∈ Finset.range 160, (v col j:ℝ)*legendre j x

noncomputable def load (x : ℝ) :=
  deflate legendre (fun j => 2*(j:ℝ)+1) 14 f x/(31*I 15)

theorem legendre_cont (j : ℕ) : Continuous (legendre j) := by
  unfold legendre
  exact continuous_const.mul (shiftedLegendre j).differentiable_aeval.continuous

theorem orth_all (i j : ℕ) :
    (∫ x in (0:ℝ)..1, legendre i x*legendre j x) =
      if i=j then (2*(j:ℝ)+1)⁻¹ else 0 := by
  by_cases h : i=j
  · subst i
    simpa [one_div] using legendre_diagonal j
  · rw [if_neg h]
    exact legendre_orthogonal i j h

theorem trial_pair_sum (g : ℝ → ℝ) (hg : Continuous g) (col : Fin 16) :
    (∫ x in (0:ℝ)..1, g x*trial col x) =
      ∑ j ∈ Finset.range 160, (v col j:ℝ)*
        (∫ x in (0:ℝ)..1, g x*legendre j x) := by
  have he : (fun x : ℝ => g x*trial col x) =
      fun x => ∑ j ∈ Finset.range 160, (v col j:ℝ)*(g x*legendre j x) := by
    funext x
    unfold trial
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [he,intervalIntegral.integral_finsetSum]
  · simp only [intervalIntegral.integral_const_mul]
  · intro j _
    exact (continuous_const.mul (hg.mul (legendre_cont j))).intervalIntegrable 0 1

theorem low_row (i : ℕ) (hi : i<15) (col : Fin 16) :
    (2*(i:ℝ)+1)*(∫ x in (0:ℝ)..1, legendre i x*trial col x) =
      (v col i:ℝ) := by
  rw [trial_pair_sum _ (legendre_cont i)]
  simp only [orth_all]
  rw [Finset.sum_eq_single i]
  · simp only [if_pos rfl]
    have hd : (2*(i:ℝ)+1)≠0 := by positivity
    field_simp [hd]
  · intro j _ hj
    simp [Ne.symm hj]
  · exact fun h => False.elim (h (Finset.mem_range.mpr (by omega)))

theorem load_cont : Continuous load := by
  unfold load deflate project
  have hf : Continuous f := by unfold f; fun_prop
  have ho : Continuous (oddPart f) := oddPart_continuous f hf
  have hL : ∀ j, Continuous (legendre j) := legendre_cont
  have hp : Continuous (fun x => ∑ j ∈ Finset.range 14,
      (2*(j:ℝ)+1)*(∫ t in (0:ℝ)..1, oddPart f t*legendre j t)*legendre j x) := by
    fun_prop
  exact (ho.sub hp).div_const _

theorem load_pair (j : ℕ) :
    31*(∫ x in (0:ℝ)..1, load x*legendre j x) =
      if j<14 then 0 else ((1-(-1:ℝ)^j)/2)*(I j/I 15) := by
  have hf : Continuous f := by unfold f; fun_prop
  have he : (fun x : ℝ => load x*legendre j x) =
      fun x => (deflate legendre (fun i => 2*(i:ℝ)+1) 14 f x*legendre j x)/(31*I 15) := by
    funext x
    unfold load
    ring
  rw [he,intervalIntegral.integral_div,deflated_pair legendre
    (fun i => 2*(i:ℝ)+1) legendre_cont (fun i => by positivity)
    orth_all legendre_reflect 14 j f hf]
  change 31*((if j<14 then 0 else ((1-(-1:ℝ)^j)/2)*I j)/(31*I 15)) = _
  split_ifs <;> field_simp [(I_pos 15).ne'] <;> ring

theorem load_pair_low (j : ℕ) (hj : j<16) :
    31*(∫ x in (0:ℝ)..1, load x*legendre j x) =
      if j=15 then 1 else 0 := by
  rw [load_pair]
  by_cases h : j<14
  · simp [h,show j≠15 by omega]
  · have h' : j=14 ∨ j=15 := by omega
    rcases h' with rfl | rfl
    · norm_num
    · norm_num [div_self (I_pos 15).ne']

theorem load_pair_even (k : ℕ) :
    31*(∫ x in (0:ℝ)..1, load x*legendre (16+2*k) x)=0 := by
  rw [load_pair,if_neg (by omega)]
  rw [pow_add,pow_mul]
  norm_num

theorem load_pair_odd (k : ℕ) :
    31*(∫ x in (0:ℝ)..1, load x*legendre (17+2*k) x)=I (17+2*k)/I 15 := by
  rw [load_pair,if_neg (by omega)]
  rw [pow_add,pow_mul]
  norm_num

theorem paired_blocks (g : ℕ → ℝ) (hz : ∀ k, g (16+2*k)=0) (n : ℕ) :
    (∑ j ∈ Finset.range (16+2*n), g j) =
      (∑ j ∈ Finset.range 16, g j)+∑ k ∈ Finset.range n, g (17+2*k) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [show 16+2*(n+1)=(16+2*n)+1+1 by omega,
      Finset.sum_range_succ,Finset.sum_range_succ,hz,add_zero,ih,Finset.sum_range_succ]
    rw [show 16+2*n+1=17+2*n by omega]
    ring

theorem high_row (col : Fin 16) :
    31*(∫ x in (0:ℝ)..1, load x*trial col x) =
      (v col 15:ℝ)+highCorrection col := by
  rw [trial_pair_sum _ load_cont,Finset.mul_sum]
  let g : ℕ → ℝ := fun j => (v col j:ℝ)*
      (31*(∫ x in (0:ℝ)..1, load x*legendre j x))
  have he : (∑ j ∈ Finset.range 160, 31*((v col j:ℝ)*
      (∫ x in (0:ℝ)..1, load x*legendre j x))) =
      ∑ j ∈ Finset.range 160, g j := by
    apply Finset.sum_congr rfl
    intro j _
    dsimp [g]
    ring
  rw [he]
  have hb := paired_blocks g (fun k => by dsimp [g]; rw [load_pair_even,mul_zero]) 72
  change (∑ j ∈ Finset.range 160, g j) = _ at hb
  rw [hb]
  have hlow : (∑ j ∈ Finset.range 16, g j) = (v col 15:ℝ) := by
    rw [Finset.sum_eq_single 15]
    · simp [g,load_pair_low 15 (by omega)]
    · intro j hj hne
      simp [g,load_pair_low j (Finset.mem_range.mp hj),hne]
    · norm_num
  have hhigh : (∑ k ∈ Finset.range 72, g (17+2*k)) = highCorrection col := by
    unfold highCorrection
    apply Finset.sum_congr rfl
    intro k _
    dsimp [g]
    rw [load_pair_odd]
  rw [hlow,hhigh]

noncomputable def unitMatrix : Matrix (Fin 16) (Fin 16) ℂ :=
  fun i j => if i.val=15 then
    ((31*(∫ x in (0:ℝ)..1, load x*trial j x):ℝ):ℂ)
    else (((2*(i.val:ℝ)+1)*(∫ x in (0:ℝ)..1, legendre i.val x*trial j x):ℝ):ℂ)

theorem unitMatrix_surjective : Function.Surjective unitMatrix.mulVec := by
  apply row_identity_surjective
  intro i j
  unfold unitMatrix base
  by_cases hi : i.val=15
  · simp only [hi,if_true,high_row]
    push_cast <;> rfl
  · simp only [hi,if_false,add_zero]
    rw [low_row _ (by omega)] <;> push_cast <;> rfl

end WeilDefect.MasterRecon.V10B47c

#print axioms WeilDefect.MasterRecon.V10B47c.legendre_cont
#print axioms WeilDefect.MasterRecon.V10B47c.orth_all
#print axioms WeilDefect.MasterRecon.V10B47c.trial_pair_sum
#print axioms WeilDefect.MasterRecon.V10B47c.low_row
#print axioms WeilDefect.MasterRecon.V10B47c.load_cont
#print axioms WeilDefect.MasterRecon.V10B47c.load_pair
#print axioms WeilDefect.MasterRecon.V10B47c.load_pair_low
#print axioms WeilDefect.MasterRecon.V10B47c.load_pair_even
#print axioms WeilDefect.MasterRecon.V10B47c.load_pair_odd
#print axioms WeilDefect.MasterRecon.V10B47c.paired_blocks
#print axioms WeilDefect.MasterRecon.V10B47c.high_row
#print axioms WeilDefect.MasterRecon.V10B47c.unitMatrix_surjective
