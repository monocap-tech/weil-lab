import WeilDefect.MasterRecon.V10B40a

/-! V10B43a: exact pairings for the canonical constraint section.
This does not establish rank of the optimized frozen trial bank. -/
namespace WeilDefect.MasterRecon.V10B43a
open MeasureTheory Set
open scoped BigOperators
open WeilDefect.MasterRecon.V10B39b
open WeilDefect.MasterRecon.V10B40a

theorem projection_pair (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, d j ≠ 0)
    (ho : ∀ i j, (∫ t in (0:ℝ)..1, p i t*p j t)=
      if i=j then (d j)⁻¹ else 0)
    (n j : ℕ) (f : ℝ → ℝ) :
    (∫ t in (0:ℝ)..1, project p d n f t*p j t) =
      if j<n then (∫ t in (0:ℝ)..1, f t*p j t) else 0 := by
  let a : ℕ → ℝ := fun i => d i*(∫ t in (0:ℝ)..1, f t*p i t)
  change (∫ t in (0:ℝ)..1, (∑ i ∈ Finset.range n, a i*p i t)*p j t) = _
  by_cases hj : j<n
  · rw [if_pos hj,finite_pair p d hp hd ho n j (Finset.mem_range.mpr hj) a]
    dsimp [a]
    field_simp [hd j]
  · rw [if_neg hj]
    have he : (fun t : ℝ => (∑ i ∈ Finset.range n, a i*p i t)*p j t) =
      fun t => ∑ i ∈ Finset.range n, a i*(p i t*p j t) := by
      funext t
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro i _
      ring
    rw [he,intervalIntegral.integral_finsetSum]
    · apply Finset.sum_eq_zero
      intro i hi
      have hij : i ≠ j := by
        intro h
        exact hj (h ▸ Finset.mem_range.mp hi)
      rw [intervalIntegral.integral_const_mul,ho,if_neg hij,mul_zero]
    · intro i _
      exact (continuous_const.mul ((hp i).mul (hp j))).intervalIntegrable 0 1

theorem odd_pair (p f : ℝ → ℝ) (s : ℝ) (hp : Continuous p) (hf : Continuous f)
    (hr : ∀ x, p (1-x)=s*p x) :
    (∫ t in (0:ℝ)..1, oddPart f t*p t) =
      ((1-s)/2)*(∫ t in (0:ℝ)..1, f t*p t) := by
  let g : ℝ → ℝ := fun x => f x*p (1-x)
  have href : (∫ t in (0:ℝ)..1, g (1-t)) = ∫ t in (0:ℝ)..1, g t := by
    simpa using intervalIntegral.integral_comp_sub_left (a := (0:ℝ)) (b := 1) g 1
  have hleft : (fun t : ℝ => g (1-t)) = fun t => f (1-t)*p t := by
    funext t
    simp only [g,show 1-(1-t)=t by ring]
  have hright : g = fun t => s*(f t*p t) := by
    funext t
    dsimp [g]
    rw [hr]
    ring
  rw [hleft,hright,intervalIntegral.integral_const_mul] at href
  have he : (fun t : ℝ => oddPart f t*p t) =
      fun t => (f t*p t-f (1-t)*p t)/2 := by
    funext t
    unfold oddPart
    ring
  have hc : Continuous (fun t : ℝ => f (1-t)*p t) := by fun_prop
  rw [he,intervalIntegral.integral_div,intervalIntegral.integral_sub
    ((hf.mul hp).intervalIntegrable 0 1) (hc.intervalIntegrable 0 1),href]
  ring

theorem deflated_pair (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, d j ≠ 0)
    (ho : ∀ i j, (∫ t in (0:ℝ)..1, p i t*p j t)=
      if i=j then (d j)⁻¹ else 0)
    (hr : ∀ j x, p j (1-x)=(-1:ℝ)^j*p j x)
    (n j : ℕ) (f : ℝ → ℝ) (hf : Continuous f) :
    (∫ t in (0:ℝ)..1, deflate p d n f t*p j t) =
      if j<n then 0 else ((1-(-1:ℝ)^j)/2)*(∫ t in (0:ℝ)..1, f t*p j t) := by
  have hc : Continuous (project p d n (oddPart f)) := by
    unfold project
    fun_prop
  have he : (fun t : ℝ => deflate p d n f t*p j t) =
      fun t => oddPart f t*p j t-project p d n (oddPart f) t*p j t := by
    funext t
    unfold deflate
    ring
  rw [he,intervalIntegral.integral_sub
    (((oddPart_continuous f hf).mul (hp j)).intervalIntegrable 0 1)
    ((hc.mul (hp j)).intervalIntegrable 0 1),
    projection_pair p d hp hd ho n j (oddPart f)]
  by_cases hj : j<n
  · simp [hj]
  · rw [if_neg hj,if_neg hj,sub_zero]
    exact odd_pair (p j) f ((-1:ℝ)^j) (hp j) hf (hr j)

/-- The actual normalized deflated load, when its leading coefficient is
nonzero, has exactly the same first sixteen pairings as the degree-15
Legendre polynomial. No truncation error or infinite expansion is used. -/
theorem normalized_pairings (p : ℕ → ℝ → ℝ)
    (hp : ∀ j, Continuous (p j))
    (ho : ∀ i j, (∫ t in (0:ℝ)..1, p i t*p j t)=
      if i=j then (2*(j:ℝ)+1)⁻¹ else 0)
    (hr : ∀ j x, p j (1-x)=(-1:ℝ)^j*p j x)
    (f : ℝ → ℝ) (hf : Continuous f)
    (hA : (31:ℝ)*(∫ t in (0:ℝ)..1, f t*p 15 t) ≠ 0)
    (j : ℕ) (hj : j<16) :
    (∫ t in (0:ℝ)..1,
      (deflate p (fun i => 2*(i:ℝ)+1) 14 f t /
        ((31:ℝ)*(∫ x in (0:ℝ)..1, f x*p 15 x)))*p j t) =
      if j=15 then 1/31 else 0 := by
  let A : ℝ := 31*(∫ t in (0:ℝ)..1, f t*p 15 t)
  have he : (fun t : ℝ => (deflate p (fun i => 2*(i:ℝ)+1) 14 f t/A)*p j t) =
      fun t => (deflate p (fun i => 2*(i:ℝ)+1) 14 f t*p j t)/A := by
    funext t
    ring
  change (∫ t in (0:ℝ)..1,
    (deflate p (fun i => 2*(i:ℝ)+1) 14 f t/A)*p j t) = _
  rw [he,intervalIntegral.integral_div,
    deflated_pair p (fun i => 2*(i:ℝ)+1) hp (fun i => by positivity)
      ho hr 14 j f hf]
  by_cases hl : j<14
  · simp [hl,show j≠15 by omega]
  · have hj' : j=14 ∨ j=15 := by omega
    rcases hj' with rfl | rfl
    · norm_num
    · norm_num
      dsimp [A]
      have hi : (∫ t in (0:ℝ)..1, f t*p 15 t) ≠ 0 := by
        intro h
        apply hA
        rw [h,mul_zero]
      field_simp [hi]

end WeilDefect.MasterRecon.V10B43a

#print axioms WeilDefect.MasterRecon.V10B43a.projection_pair
#print axioms WeilDefect.MasterRecon.V10B43a.odd_pair
#print axioms WeilDefect.MasterRecon.V10B43a.deflated_pair
#print axioms WeilDefect.MasterRecon.V10B43a.normalized_pairings
