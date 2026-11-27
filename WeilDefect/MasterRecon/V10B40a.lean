import WeilDefect.MasterRecon.V10B39b
import WeilDefect.MasterRecon.V10B39c

/-! V10B40a: direct finite low-mode deflation. The projection bound
is applied only to the removed modes. No infinite expansion is needed. -/
namespace WeilDefect.MasterRecon.V10B40a
open MeasureTheory Set
open scoped BigOperators
open WeilDefect.MasterRecon.V10B39b
open WeilDefect.MasterRecon.V10B39c

noncomputable def oddPart (f : ℝ → ℝ) (x : ℝ) :=
  (f x-f (1-x))/2

noncomputable def deflate (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (n : ℕ) (f : ℝ → ℝ) (x : ℝ) :=
  oddPart f x-project p d n (oddPart f) x

theorem oddPart_continuous (f : ℝ → ℝ) (hf : Continuous f) :
    Continuous (oddPart f) := by
  unfold oddPart
  fun_prop

theorem deflation_error (p : ℕ → ℝ → ℝ) (d b : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, 0 ≤ d j)
    (hb : ∀ j, 0 ≤ b j)
    (hpb : ∀ j x, x ∈ Icc (0:ℝ) 1 → |p j x| ≤ b j)
    (n : ℕ) (f g : ℝ → ℝ) (hf : Continuous f) (hg : Continuous g)
    (ε : ℝ) (hε : 0 ≤ ε)
    (he : ∀ x ∈ Icc (0:ℝ) 1, |f x-g x| ≤ ε)
    (x : ℝ) (hx : x ∈ Icc (0:ℝ) 1) :
    |deflate p d n f x-deflate p d n g x| ≤
      ε*(1+∑ j ∈ Finset.range n, d j*(b j)^2) := by
  have hfo := oddPart_continuous f hf
  have hgo := oddPart_continuous g hg
  have ho : ∀ t ∈ Icc (0:ℝ) 1, |oddPart f t-oddPart g t| ≤ ε :=
    fun t ht => reflected_error f g ε t ht he
  have h := project_bound p d b hp hd hb hpb n
    (fun t => oddPart f t-oddPart g t) (hfo.sub hgo) ε hε ho x hx
  rw [← project_sub p d hp n (oddPart f) (oddPart g) hfo hgo x] at h
  unfold deflate
  calc
    _ = |(oddPart f x-oddPart g x)-
        (project p d n (oddPart f) x-project p d n (oddPart g) x)| := by
      congr 1
      ring
    _ ≤ |oddPart f x-oddPart g x|+
        |project p d n (oddPart f) x-project p d n (oddPart g) x| := by
      simpa only [sub_eq_add_neg,abs_neg] using
        abs_add_le (oddPart f x-oddPart g x)
          (-(project p d n (oddPart f) x-project p d n (oddPart g) x))
    _ ≤ ε+ε*(∑ j ∈ Finset.range n, d j*(b j)^2) := add_le_add (ho x hx) h
    _ = _ := by ring

theorem denominator_transport (u v A D : ℝ) (hA : 0<A) (hD : 0<D) :
    |u/A-v/D| ≤ |u-v|/A + |v/D| *|A-D|/A := by
  have he : u/A-v/D = (u-v)/A + (v/D)*(D-A)/A := by
    field_simp [hA.ne',hD.ne'] <;> ring
  rw [he]
  calc
    _ ≤ |(u-v)/A|+|(v/D)*(D-A)/A| := abs_add_le _ _
    _ = _ := by rw [abs_div,abs_div,abs_mul,abs_of_pos hA,abs_sub_comm D A]

theorem coefficient_compare (p : ℕ → ℝ → ℝ) (b : ℕ → ℝ)
    (s : Finset ℕ) (a c : ℕ → ℝ) (x : ℝ)
    (hb : ∀ j ∈ s, |p j x| ≤ b j) :
    |(∑ j ∈ s, a j*p j x)-(∑ j ∈ s, c j*p j x)| ≤
      ∑ j ∈ s, |a j-c j| *b j := by
  rw [← Finset.sum_sub_distrib]
  calc
    _ ≤ ∑ j ∈ s, |a j*p j x-c j*p j x| := by
      simpa only [Real.norm_eq_abs] using
        norm_sum_le s (fun j => a j*p j x-c j*p j x)
    _ ≤ _ := by
      apply Finset.sum_le_sum
      intro j hj
      rw [← sub_mul,abs_mul]
      exact mul_le_mul_of_nonneg_left (hb j hj) (abs_nonneg _)

end WeilDefect.MasterRecon.V10B40a

#print axioms WeilDefect.MasterRecon.V10B40a.oddPart_continuous
#print axioms WeilDefect.MasterRecon.V10B40a.deflation_error
#print axioms WeilDefect.MasterRecon.V10B40a.denominator_transport
#print axioms WeilDefect.MasterRecon.V10B40a.coefficient_compare
