import Mathlib

namespace WeilDefect

open Filter Set
open scoped Topology

/--
The real-line exponential mode with complex frequency λ.
This is exactly x ↦ exp(x λ).
-/
def realExpMode (λ : ℂ) (x : ℝ) : ℂ :=
  Complex.exp ((x : ℂ) * λ)

/-- The complex exponential mode never vanishes. -/
theorem realExpMode_ne_zero (λ : ℂ) (x : ℝ) :
    realExpMode λ x ≠ 0 := by
  simp [realExpMode]

/--
One real derivative of a complex exponential mode multiplies it by its
complex frequency.
-/
theorem hasDerivAt_realExpMode (λ : ℂ) (x : ℝ) :
    HasDerivAt (realExpMode λ) (λ * realExpMode λ x) x := by
  have h :=
    hasDerivAt_exp_smul_const' (𝕂 := ℝ) (𝔸 := ℂ) λ x
  simpa [realExpMode, ← Complex.exp_eq_exp_ℂ, smul_eq_mul, mul_comm] using h

/--
The k-th real derivative of x ↦ exp(x λ) is λ^k exp(x λ).
-/
theorem iteratedDeriv_realExpMode (k : ℕ) (λ : ℂ) :
    iteratedDeriv k (realExpMode λ) =
      fun x : ℝ => λ ^ k * realExpMode λ x := by
  induction k with
  | zero =>
      simp
  | succ k ih =>
      rw [iteratedDeriv_succ, ih]
      funext x
      have h :=
        (hasDerivAt_realExpMode λ x).const_mul (λ ^ k)
      simpa [pow_succ, mul_assoc, mul_left_comm, mul_comm] using h.deriv

/--
Each scalar multiple of a real exponential mode is smooth, hence has every
finite iterated derivative required by the Vandermonde argument.
-/
theorem contDiffAt_const_mul_realExpMode
    (k : ℕ) (c λ : ℂ) (x : ℝ) :
    ContDiffAt ℝ k (fun y : ℝ => c * realExpMode λ y) x := by
  fun_prop

/--
Derivative formula for a finite exponential sum.
-/
theorem iteratedDeriv_finite_exp_sum
    {n : ℕ} (k : ℕ) (c λ : Fin n → ℂ) (x : ℝ) :
    iteratedDeriv k
        (fun y : ℝ => ∑ i : Fin n, c i * realExpMode (λ i) y) x
      =
        ∑ i : Fin n, c i * (λ i) ^ k * realExpMode (λ i) x := by
  rw [iteratedDeriv_fun_sum]
  · apply Finset.sum_congr rfl
    intro i hi
    rw [iteratedDeriv_const_mul_field]
    rw [iteratedDeriv_realExpMode]
    simp only [Pi.zero_apply]
    ring
  · intro i hi
    exact contDiffAt_const_mul_realExpMode k (c i) (λ i) x

/--
WD-T24 / ZW1-T5: finite distinct-frequency exponential independence on a
nonempty real interval.

If λ₁,...,λₙ are distinct complex frequencies and a finite exponential sum
vanishes throughout a nonempty real interval, then every coefficient is zero.
-/
theorem wd_t24_finite_distinct_frequency_exponential_independence
    {n : ℕ}
    (λ c : Fin n → ℂ)
    (hλ : Function.Injective λ)
    (a b : ℝ)
    (hab : a < b)
    (hzero :
      Set.EqOn
        (fun x : ℝ => ∑ i : Fin n, c i * realExpMode (λ i) x)
        0
        (Set.Ioo a b)) :
    c = 0 := by
  let x0 : ℝ := (a + b) / 2
  have hx0 : x0 ∈ Set.Ioo a b := by
    dsimp [x0]
    constructor <;> linarith

  let F : ℝ → ℂ :=
    fun x => ∑ i : Fin n, c i * realExpMode (λ i) x

  have hFzero : F =ᶠ[𝓝 x0] (0 : ℝ → ℂ) := by
    filter_upwards [isOpen_Ioo.mem_nhds hx0] with x hx
    simpa [F] using hzero hx

  let v : Fin n → ℂ :=
    fun i => c i * realExpMode (λ i) x0

  have hmom :
      ∀ k : Fin n,
        (∑ i : Fin n, v i * (λ i) ^ (k : ℕ)) = 0 := by
    intro k
    have hderiv :
        iteratedDeriv (k : ℕ) F x0 = 0 := by
      have h :=
        Filter.EventuallyEq.iteratedDeriv_eq (k : ℕ) hFzero
      simpa using h
    have hformula :=
      iteratedDeriv_finite_exp_sum (n := n) (k : ℕ) c λ x0
    rw [show F =
        (fun x : ℝ => ∑ i : Fin n, c i * realExpMode (λ i) x) by rfl] at hderiv
    rw [hformula] at hderiv
    simpa [v, mul_assoc, mul_left_comm, mul_comm] using hderiv

  have hv : v = 0 :=
    Matrix.eq_zero_of_forall_pow_sum_mul_pow_eq_zero hλ hmom

  funext i
  have hvi : v i = 0 := by
    simpa [hv]
  dsimp [v] at hvi
  exact (mul_eq_zero.mp hvi).resolve_right (realExpMode_ne_zero (λ i) x0)

end WeilDefect
