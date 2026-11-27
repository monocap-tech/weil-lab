import WeilDefect.MasterRecon.V10B39b

/-! V10B39c: a finite projection error receiver. The approximant must
be literally reproduced; no convergence or completeness is assumed. -/
namespace WeilDefect.MasterRecon.V10B39c
open MeasureTheory Set
open scoped BigOperators
open WeilDefect.MasterRecon.V10B39b

theorem finite_projection_error (p : ℕ → ℝ → ℝ) (d b : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, 0 ≤ d j)
    (hb : ∀ j, 0 ≤ b j)
    (hpb : ∀ j x, x ∈ Icc (0:ℝ) 1 → |p j x| ≤ b j)
    (n : ℕ) (f g : ℝ → ℝ) (hf : Continuous f) (hg : Continuous g)
    (ε : ℝ) (hε : 0 ≤ ε)
    (he : ∀ x ∈ Icc (0:ℝ) 1, |f x-g x| ≤ ε)
    (hrepro : ∀ x ∈ Icc (0:ℝ) 1, project p d n g x = g x)
    (x : ℝ) (hx : x ∈ Icc (0:ℝ) 1) :
    |f x-project p d n f x| ≤
      ε*(1+∑ j ∈ Finset.range n, d j*(b j)^2) := by
  have h := project_bound p d b hp hd hb hpb n (fun t => f t-g t)
    (hf.sub hg) ε hε he x hx
  rw [← project_sub p d hp n f g hf hg x,hrepro x hx] at h
  calc
    _ = |(f x-g x)-(project p d n f x-g x)| := by ring_nf
    _ ≤ |f x-g x|+|project p d n f x-g x| := by simpa only [sub_eq_add_neg,abs_neg] using abs_add_le (f x-g x) (-(project p d n f x-g x))
    _ ≤ ε+ε*(∑ j ∈ Finset.range n, d j*(b j)^2) :=
      add_le_add (he x hx) h
    _ = _ := by ring

theorem reflected_error (f g : ℝ → ℝ) (ε x : ℝ)
    (hx : x ∈ Icc (0:ℝ) 1)
    (he : ∀ t ∈ Icc (0:ℝ) 1, |f t-g t| ≤ ε) :
    |(f x-f (1-x))/2-(g x-g (1-x))/2| ≤ ε := by
  have hx' : 1-x ∈ Icc (0:ℝ) 1 := ⟨by linarith [hx.2],by linarith [hx.1]⟩
  have h : |(f x-g x)-(f (1-x)-g (1-x))| ≤
      |f x-g x|+|f (1-x)-g (1-x)| := by
    simpa only [sub_eq_add_neg,abs_neg] using abs_add_le (f x-g x) (-(f (1-x)-g (1-x)))
  have hh := add_le_add (he x hx) (he (1-x) hx')
  calc
    _ = |((f x-g x)-(f (1-x)-g (1-x)))/2| := by ring_nf
    _ = |(f x-g x)-(f (1-x)-g (1-x))|/2 := by rw [abs_div]; norm_num
    _ ≤ ε := by linarith

theorem normalized_transfer (u v w D E F : ℝ)
    (hD : 0<D) (h₁ : |u-v| ≤ D*E) (h₂ : |v-w| ≤ D*F) :
    |u/D-w/D| ≤ E+F := by
  rw [← sub_div,abs_div,abs_of_pos hD]
  apply (div_le_iff₀ hD).mpr
  calc
    _ ≤ |u-v|+|v-w| := abs_sub_le u v w
    _ ≤ D*E+D*F := add_le_add h₁ h₂
    _ = _ := by ring

end WeilDefect.MasterRecon.V10B39c

#print axioms WeilDefect.MasterRecon.V10B39c.finite_projection_error
#print axioms WeilDefect.MasterRecon.V10B39c.reflected_error
#print axioms WeilDefect.MasterRecon.V10B39c.normalized_transfer
