import WeilDefect.MasterRecon.V10B5d

/-! V10B5e: attach the actual right-half strip-zero index and
analytic multiplicity to V09D's literal finite-sum counting function.
The numerical logarithmic bound for that count is still an explicit
arithmetic input; no RH or reflection assumption is used here. -/
namespace WeilDefect.MasterRecon.V10B5e

open Set MeasureTheory
open scoped ENNReal BigOperators

open V10A (Index displacement ordinate multiplicity)

theorem strip_unit_window_finite (n : ℤ) :
    (V09D.stripWindow (n : ℝ) ((n : ℝ)+1)).Finite := by
  let K := (Icc (0:ℝ) 1 ×ˢ Icc (n : ℝ) ((n : ℝ)+1))
  let e : ℝ × ℝ → ℂ := fun p => (p.1 : ℂ) + (p.2 : ℂ)*Complex.I
  have hk : IsCompact K := isCompact_Icc.prod isCompact_Icc
  have he : Continuous e := by dsimp [e]; fun_prop
  apply ((hk.image he).inter_riemannZetaZeros_finite).subset
  intro ρ hρ
  rcases hρ with ⟨⟨hz,hr₀,hr₁⟩,hy₀,hy₁⟩
  refine ⟨?_,hz⟩
  refine ⟨(ρ.re,ρ.im), ⟨⟨hr₀.le,hr₁.le⟩,⟨hy₀.le,hy₁⟩⟩, ?_⟩
  apply Complex.ext <;> simp [e, Complex.add_re, Complex.add_im, Complex.mul_re, Complex.mul_im]

theorem literal_count_finset (n : ℤ) :
    V09D.count (n : ℝ) ((n : ℝ)+1) =
      ∑ ρ ∈ (strip_unit_window_finite n).toFinset, V09D.mult ρ := by
  unfold V09D.count
  exact finsum_mem_eq_finite_toFinset_sum V09D.mult (strip_unit_window_finite n)

theorem index_in_window (i : Index) (n : ℤ)
    (h : V10B5a.cell (ordinate i) = n) :
    (i : ℂ) ∈ V09D.stripWindow (n : ℝ) ((n : ℝ)+1) := by
  have hy := V10B5a.cell_mem (ordinate i)
  rw [h] at hy
  exact ⟨i.property.1,hy.1,hy.2⟩

theorem finite_index_count_le (S : Finset Index) (n : ℤ) :
    (∑ i ∈ S.filter (fun i => V10B5a.cell (ordinate i) = n),
      (multiplicity i : ℝ)) ≤ (V09D.count (n : ℝ) ((n : ℝ)+1) : ℝ) := by
  classical
  let U := S.filter (fun i => V10B5a.cell (ordinate i) = n)
  let e : Index ↪ ℂ := ⟨Subtype.val, Subtype.val_injective⟩
  let W := (strip_unit_window_finite n).toFinset
  have hsub : U.map e ⊆ W := by
    intro ρ hρ
    obtain ⟨i,hi,rfl⟩ := Finset.mem_map.mp hρ
    exact (Set.Finite.mem_toFinset _).mpr
      (index_in_window i n (Finset.mem_filter.mp hi).2)
  have hnat : (∑ i ∈ U, multiplicity i) ≤ V09D.count (n : ℝ) ((n : ℝ)+1) := by
    rw [literal_count_finset]
    calc
      _ = ∑ ρ ∈ U.map e, V09D.mult ρ := by
        rw [Finset.sum_map]
        rfl
      _ ≤ ∑ ρ ∈ W, V09D.mult ρ :=
        Finset.sum_le_sum_of_subset_of_nonneg hsub (fun _ _ _ => Nat.zero_le _)
  exact_mod_cast hnat

theorem strip_displacement (i : Index) :
    displacement i ∈ Icc (-(1/2):ℝ) (1/2) :=
  abs_le.mp (V10A.displacement_bound i)

theorem reflected_strip_displacement (i : Index) :
    -displacement i ∈ Icc (-(1/2):ℝ) (1/2) := by
  have h := strip_displacement i
  exact ⟨by linarith [h.2],by linarith [h.1]⟩

theorem zeroth_moment (f : ℝ → ℂ) : V10B4f.momentInput f 0 = f := by
  funext x
  simp [V10B4f.momentInput]

theorem right_sample_identity (t : ℝ) (g : V08I.logCarrier t) (i : Index) :
    V10B5c.angularMoment t g 0 (displacement i) (ordinate i) =
      V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ) ((i : ℂ)-1/2) := by
  rw [V10B5c.angularMoment, zeroth_moment, V10A.right_exponent]

theorem left_sample_identity (t : ℝ) (g : V08I.logCarrier t) (i : Index) :
    V10B5c.angularMoment t g 0 (-displacement i) (ordinate i) =
      V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ)
        (V10A.reflect (i : ℂ)-1/2) := by
  rw [V10B5c.angularMoment, zeroth_moment, Complex.ofReal_neg, V10A.left_exponent]

/-- Both members of each representative orbit satisfy the same
uniform Bessel upper bound, conditional only on the literal count
estimate and the upstream analytical proofs. -/
theorem bounded_arithmetic_samples (t : ℝ) (ht : 0 ≤ t) (A : ℝ)
    (hA : 0 ≤ A)
    (hcount : ∀ n : ℤ, (V09D.count (n : ℝ) ((n : ℝ)+1) : ℝ) ≤
      A * Real.log (|(n : ℝ)|+3)) :
    ∃ B : ℝ, 0 ≤ B ∧ ∀ g : V08I.logCarrier t,
      (∑' i : Index, ENNReal.ofReal ((multiplicity i : ℝ) *
        ‖V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ)
          ((i : ℂ)-1/2)‖^2)) ≤ ENNReal.ofReal (B*‖g‖^2) ∧
      (∑' i : Index, ENNReal.ofReal ((multiplicity i : ℝ) *
        ‖V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ)
          (V10A.reflect (i : ℂ)-1/2)‖^2)) ≤ ENNReal.ofReal (B*‖g‖^2) := by
  obtain ⟨C,hC,h⟩ := V10B5d.bounded_strip_sampling t ht
  refine ⟨4*A*C,by positivity,?_⟩
  intro g
  have hc (S : Finset Index) (n : ℤ) :
      (∑ i ∈ S.filter (fun i => V10B5a.cell (ordinate i) = n),
        (multiplicity i : ℝ)) ≤ A * Real.log (|(n : ℝ)|+3) :=
    (finite_index_count_le S n).trans (hcount n)
  have hr := h displacement ordinate (fun i => (multiplicity i : ℝ))
    A hA strip_displacement (fun i => by positivity) hc g
  have hl := h (fun i => -displacement i) ordinate (fun i => (multiplicity i : ℝ))
    A hA reflected_strip_displacement (fun i => by positivity) hc g
  have he : 4*(A*(C*‖g‖^2)) = (4*A*C)*‖g‖^2 := by ring
  exact ⟨by simpa only [right_sample_identity,he] using hr,
    by simpa only [left_sample_identity,he] using hl⟩

end WeilDefect.MasterRecon.V10B5e

#print axioms WeilDefect.MasterRecon.V10B5e.strip_unit_window_finite
#print axioms WeilDefect.MasterRecon.V10B5e.literal_count_finset
#print axioms WeilDefect.MasterRecon.V10B5e.index_in_window
#print axioms WeilDefect.MasterRecon.V10B5e.finite_index_count_le
#print axioms WeilDefect.MasterRecon.V10B5e.strip_displacement
#print axioms WeilDefect.MasterRecon.V10B5e.reflected_strip_displacement
#print axioms WeilDefect.MasterRecon.V10B5e.zeroth_moment
#print axioms WeilDefect.MasterRecon.V10B5e.right_sample_identity
#print axioms WeilDefect.MasterRecon.V10B5e.left_sample_identity
#print axioms WeilDefect.MasterRecon.V10B5e.bounded_arithmetic_samples
