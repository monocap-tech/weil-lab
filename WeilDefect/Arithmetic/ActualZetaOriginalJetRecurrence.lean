import Mathlib

namespace WeilDefect
noncomputable section
open Finset Filter
open scoped ENNReal NNReal

/-! NF590: analytic identity of a finite polynomial/exponential jet
recurrence. The recurrence is the one used in NF587's direct interval
replay. All orders are covered, not only the first 400. -/

def neutralNF590ExpJet (z : ℂ) : ℕ → ℂ
  | 0 => 1
  | n+1 => neutralNF590ExpJet z n * z / (n+1:ℂ)

theorem neutralNF590ExpJet_eq (z : ℂ) (n : ℕ) :
    neutralNF590ExpJet z n = z^n/(n.factorial:ℂ) := by
  induction n with
  | zero => simp [neutralNF590ExpJet]
  | succ n ih =>
    rw [neutralNF590ExpJet,ih,pow_succ,Nat.factorial_succ,Nat.cast_mul,Nat.cast_succ]
    have h : (n.factorial:ℂ) ≠ 0 := by exact_mod_cast n.factorial_ne_zero
    have hn : (n:ℂ)+1 ≠ 0 := by exact_mod_cast Nat.succ_ne_zero n
    field_simp

theorem neutralNF590ExpJet_hasSum (z w : ℂ) :
    HasSum (fun n : ℕ => neutralNF590ExpJet z n*w^n) (Complex.exp (z*w)) := by
  have h := NormedSpace.expSeries_div_hasSum_exp (z*w)
  rw [← Complex.exp_eq_exp_ℂ] at h
  convert h using 1
  funext n
  rw [neutralNF590ExpJet_eq,mul_pow]
  ring

def neutralNF590ShiftedJet (z : ℂ) (m n : ℕ) : ℂ :=
  if m ≤ n then neutralNF590ExpJet z (n-m) else 0

theorem neutralNF590ShiftedJet_hasSum (z w : ℂ) (m : ℕ) :
    HasSum (fun n : ℕ => neutralNF590ShiftedJet z m n*w^n)
      (w^m*Complex.exp (z*w)) := by
  let f := fun n : ℕ => neutralNF590ShiftedJet z m n*w^n
  have htail : HasSum (fun n : ℕ => f (n+m)) (w^m*Complex.exp (z*w)) := by
    convert (neutralNF590ExpJet_hasSum z w).mul_left (w^m) using 1
    funext n
    dsimp [f,neutralNF590ShiftedJet]
    rw [if_pos (by omega : m ≤ n+m),Nat.add_sub_cancel,pow_add]
    ring
  have hhead : (∑ n ∈ range m, f n) = 0 := by
    apply sum_eq_zero
    intro n hn
    simp [f,neutralNF590ShiftedJet,not_le_of_gt (mem_range.mp hn)]
  have h := (hasSum_nat_add_iff m).mp htail
  simpa only [hhead,add_zero] using h

def neutralNF590PolyTerm (B D : ℂ) (k m : ℕ) : ℂ :=
  (k.choose m:ℂ)*B^(k-m)*D^m

def neutralNF590ModeJet (B D λ : ℂ) (k n : ℕ) : ℂ :=
  ∑ m ∈ range (k+1),
    neutralNF590PolyTerm B D k m * neutralNF590ShiftedJet λ m n

/-- This is the exact finite summation in the interval recurrence:
the zero terms with m>n can be omitted. -/
theorem neutralNF590ModeJet_truncate (B D λ : ℂ) (k n : ℕ) :
    neutralNF590ModeJet B D λ k n =
      ∑ m ∈ range (min k n+1),
        neutralNF590PolyTerm B D k m * neutralNF590ExpJet λ (n-m) := by
  unfold neutralNF590ModeJet
  rw [← sum_subset (s₁ := range (min k n+1)) (s₂ := range (k+1))
    (range_subset_range.mpr (by omega : min k n+1 ≤ k+1))]
  · apply sum_congr rfl
    intro m hm
    have hh : m ≤ n := by have := mem_range.mp hm; omega
    simp [neutralNF590ShiftedJet,hh]
  · intro m hm hnot
    have hk := mem_range.mp hm
    have hh : ¬ m ≤ n := by
      intro h
      apply hnot
      exact mem_range.mpr (by omega)
    simp [neutralNF590ShiftedJet,hh]

theorem neutralNF590ModeJet_hasSum (B D λ w : ℂ) (k : ℕ) :
    HasSum (fun n : ℕ => neutralNF590ModeJet B D λ k n*w^n)
      ((B+D*w)^k*Complex.exp (λ*w)) := by
  have h : HasSum (fun n : ℕ => ∑ m ∈ range (k+1),
      neutralNF590PolyTerm B D k m * (neutralNF590ShiftedJet λ m n*w^n))
      (∑ m ∈ range (k+1),
        neutralNF590PolyTerm B D k m * (w^m*Complex.exp (λ*w))) :=
    hasSum_sum fun m _ => (neutralNF590ShiftedJet_hasSum λ w m).mul_left _
  convert h using 1
  · funext n
    unfold neutralNF590ModeJet
    rw [sum_mul]
    apply sum_congr rfl
    intro m _
    ring
  · rw [add_comm B (D*w), add_pow, sum_mul]
    apply sum_congr rfl
    intro m _
    unfold neutralNF590PolyTerm
    rw [mul_pow]
    ring

/-- A completely independent real-series uniqueness interface: equality
on real samples near zero identifies coefficients, without trusting an
external numerical routine or needing a complex interval computation. -/
theorem neutralNF590RealSeries_unique (u v : ℕ → ℝ) (f : ℝ → ℝ)
    (hu : ∀ w : ℝ, HasSum (fun n => u n*w^n) (f w))
    (hv : ∀ w : ℝ, HasSum (fun n => v n*w^n) (f w)) : u = v := by
  have make (c : ℕ → ℝ) (hc : ∀ w : ℝ, HasSum (fun n => c n*w^n) (f w)) :
      HasFPowerSeriesAt f (FormalMultilinearSeries.ofScalars ℝ c) 0 := by
    let p := FormalMultilinearSeries.ofScalars ℝ c
    have hs : Summable c := by simpa using (hc 1).summable
    have ht : Tendsto (fun n => ‖p n‖ * ((1:ℝ≥0):ℝ)^n) atTop (nhds 0) := by
      simpa [p,FormalMultilinearSeries.ofScalars_norm] using hs.tendsto_atTop_zero.norm
    have hr : (1:ℝ≥0∞) ≤ p.radius := by
      exact p.le_radius_of_tendsto (r := 1) ht
    refine ⟨1,hr,by norm_num,?_⟩
    intro w _
    simpa [p,FormalMultilinearSeries.ofScalars_apply_eq,smul_eq_mul] using hc w
  have h := (make u hu).eq_formalMultilinearSeries (make v hv)
  exact (FormalMultilinearSeries.ofScalars_series_eq_iff ℝ ℝ v).mp h

end
end WeilDefect
