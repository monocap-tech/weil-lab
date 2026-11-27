import WeilDefect.MasterRecon.V10B20b

/-! V10B20c: evaluate the mixed-log rational series using harmonic
partial sums and the native Basel theorem. -/
namespace WeilDefect.MasterRecon.V10B20c

open Filter MeasureTheory
open scoped BigOperators Topology
open V10B20b (H H₂)

noncomputable def recip (j : ℕ) : ℝ := 1/((j:ℝ)+1)

theorem harmonic_gap_finite (n N : ℕ) :
    (∑ j ∈ Finset.range N, (recip j-recip (j+n))) =
      H n-∑ j ∈ Finset.range n, recip (N+j) := by
  have h₁ := Finset.sum_range_add recip n N
  have h₂ := Finset.sum_range_add recip N n
  rw [Nat.add_comm n N] at h₁
  have he : (∑ j ∈ Finset.range N, recip (n+j)) =
      ∑ j ∈ Finset.range N, recip (j+n) := by
    apply Finset.sum_congr rfl
    intro j _
    rw [Nat.add_comm]
  rw [he] at h₁
  rw [Finset.sum_sub_distrib]
  change _ = (∑ j ∈ Finset.range n, recip j) - _
  linarith only [h₁,h₂]

theorem recip_tendsto : Tendsto recip atTop (𝓝 0) :=
  tendsto_one_div_add_atTop_nhds_zero_nat

theorem harmonic_gap (n : ℕ) :
    HasSum (fun j : ℕ => recip j-recip (j+n)) (H n) := by
  have hp (j : ℕ) : 0 ≤ recip j-recip (j+n) := by
    unfold recip
    push_cast
    apply sub_nonneg.mpr
    apply one_div_le_one_div_of_le (by positivity)
    linarith [Nat.cast_nonneg (α := ℝ) n]
  rw [hasSum_iff_tendsto_nat_of_nonneg hp]
  simp_rw [harmonic_gap_finite]
  have ht (j : ℕ) : Tendsto (fun N : ℕ => recip (N+j)) atTop (𝓝 0) := by
    apply recip_tendsto.comp
    apply tendsto_atTop.2
    intro b
    filter_upwards [eventually_ge_atTop b] with N hN
    omega
  have h := tendsto_finset_sum (Finset.range n) (fun j _ => ht j)
  simpa using tendsto_const_nhds.sub h

theorem basel_shift (n : ℕ) :
    HasSum (fun j : ℕ => 1/((j:ℝ)+(n:ℝ)+1)^2) (Real.pi^2/6-H₂ n) := by
  have h : HasSum (fun j : ℕ => 1/((j:ℝ)+1)^2) (Real.pi^2/6) := by
    simpa using (hasSum_nat_add_iff' 1).mpr hasSum_zeta_two
  simpa [H₂,Nat.cast_add] using (hasSum_nat_add_iff' n).mpr h

theorem mixed_series_exact (n : ℕ) (hn : 0 < n) :
    HasSum (fun j : ℕ => 1/(((j:ℝ)+1)*((n:ℝ)+(j:ℝ)+1)^2))
      (H n/(n:ℝ)^2-(Real.pi^2/6-H₂ n)/(n:ℝ)) := by
  have h₁ := (harmonic_gap n).mul_left (1/(n:ℝ)^2)
  have h₂ := (basel_shift n).mul_left (1/(n:ℝ))
  have h := h₁.sub h₂
  have he (j : ℕ) : 1/(((j:ℝ)+1)*((n:ℝ)+(j:ℝ)+1)^2) =
      (1/(n:ℝ)^2)*(recip j-recip (j+n))-
        (1/(n:ℝ))*(1/((j:ℝ)+(n:ℝ)+1)^2) := by
    unfold recip
    push_cast
    convert V10B20b.mixed_partial_fraction (n:ℝ) ((j:ℝ)+1) (by exact_mod_cast hn) (by positivity) using 1 <;> ring_nf
  convert h using 1
  · funext j
    exact he j
  · ring

theorem mixed_log_exact (k : ℕ) :
    (∫ x in Set.Ioo (0:ℝ) 1, x^k*Real.log x*Real.log (1-x)) =
      H (k+1)/((k:ℝ)+1)^2-(Real.pi^2/6-H₂ (k+1))/((k:ℝ)+1) := by
  rw [V10B20b.mixed_series_integral]
  have h := (mixed_series_exact (k+1) (by omega)).tsum_eq
  simpa [Nat.cast_add,add_assoc,add_comm,add_left_comm] using h

end WeilDefect.MasterRecon.V10B20c

#print axioms WeilDefect.MasterRecon.V10B20c.harmonic_gap_finite
#print axioms WeilDefect.MasterRecon.V10B20c.recip_tendsto
#print axioms WeilDefect.MasterRecon.V10B20c.harmonic_gap
#print axioms WeilDefect.MasterRecon.V10B20c.basel_shift
#print axioms WeilDefect.MasterRecon.V10B20c.mixed_series_exact
#print axioms WeilDefect.MasterRecon.V10B20c.mixed_log_exact
