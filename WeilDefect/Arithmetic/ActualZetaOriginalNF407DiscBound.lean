import WeilDefect.Arithmetic.ActualZetaOriginalComplexDiscMajorants
import WeilDefect.Arithmetic.ActualZetaOriginalNF407NormalizedComplexSource

namespace WeilDefect
noncomputable section
open Finset

/-! NF589: sum the elementary complex majorants over the literal
NF407 source, not a proxy polynomial. Separate the rational table
bounds from the transcendental analytic proof. -/

def neutralNF589ModeMajorant : ℝ := (2:ℝ)^13*3^283

theorem neutralNF589ModeMajorant_pos : 0 < neutralNF589ModeMajorant := by
  unfold neutralNF589ModeMajorant
  positivity

theorem neutralNF589Pole_le_mode : (3:ℝ) ≤ neutralNF589ModeMajorant := by
  unfold neutralNF589ModeMajorant
  calc
    (3:ℝ) = 1*3^1 := by norm_num
    _ ≤ 2^13*3^283 := mul_le_mul (by positivity) 
      (pow_le_pow_right₀ (by norm_num) (by decide)) (by norm_num) (by positivity)

theorem neutralNF589Disc_arithmetic :
    (400:ℝ)*10^143*neutralNF589ModeMajorant ≤ (10:ℝ)^400 := by
  have h3 : (3:ℝ)^283 ≤ 10^142 := calc
    _ ≤ (3:ℝ)^284 := pow_le_pow_right₀ (by norm_num) (by decide)
    _ = ((3:ℝ)^2)^142 := by rw [← pow_mul]; norm_num
    _ ≤ (10:ℝ)^142 := pow_le_pow_left₀ (by positivity) (by norm_num) _
  have h2 : (2:ℝ)^13 ≤ 10^4 := by norm_num
  unfold neutralNF589ModeMajorant
  calc
    _ = 400*10^143*2^13*3^283 := by ring
    _ ≤ (10:ℝ)^3*10^143*10^4*10^142 := by
      gcongr <;> norm_num
    _ = (10:ℝ)^292 := by
      rw [← pow_add,← pow_add,← pow_add]
      norm_num
    _ ≤ _ := pow_le_pow_right₀ (by norm_num) (by decide)

/-- This predicate concerns only finite rational data and the original
primitive coefficient intervals. No analytic enclosure is assumed. -/
def neutralNF589SourceScalarBounds (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) : Prop :=
  (∀ j, |a j| ≤ (10:ℝ)^143) ∧
  (∀ j, |b j| ≤ (10:ℝ)^143) ∧
  (∀ i : Fin 241,
    0 ≤ (nf545OriginalOscillatorNodeAt i).1 ∧
      (nf545OriginalOscillatorNodeAt i).1 ≤ 883 ∧
      (nf545OriginalOscillatorNodeAt i).2 ≤ 13) ∧
  (∀ k : Fin 32, 0 ≤ neutralNF587CriticalFrequencies[k.val]! ∧
      neutralNF587CriticalFrequencies[k.val]! ≤ 883) ∧
  (∀ j : Fin 4, ∀ k : Fin 32, |(neutralNF587CriticalSines[j.val]!)[k.val]!| ≤ 1) ∧
  (∀ j : Fin 4, |neutralNF587CriticalPoles[j.val]!| ≤ 1)

theorem neutralNF589SourceDisc_of_scalarBounds
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (h : neutralNF589SourceScalarBounds a b)
    (w : ℂ) (hw : ‖w‖ ≤ 20) :
    ‖neutralNF588NormalizedSource a b w‖ ≤ (10:ℝ)^400 := by
  let x := (11/10:ℂ)-w/500
  have hx : ‖x‖ ≤ 2 := (neutralNF589NormalizedGeometry w hw).1
  have hy : |x.im| ≤ 1/25 := (neutralNF589NormalizedGeometry w hw).2
  let Q := neutralNF589ModeMajorant
  have hQ : 0 < Q := neutralNF589ModeMajorant_pos
  obtain ⟨ha,hb,hn,hf,hc,hp⟩ := h
  have hsel (j : Fin 242) : ‖neutralNF588SelectedComplex j x‖ ≤ Q := by
    unfold neutralNF588SelectedComplex
    by_cases hj : j.val < 241
    · rw [dif_pos hj]
      let i : Fin 241 := ⟨j.val,hj⟩
      exact neutralNF589Oscillator_norm x ((nf545OriginalOscillatorNodeAt i).1:ℝ)
        (nf545OriginalOscillatorNodeAt i).2 hx hy (by exact_mod_cast (hn i).1)
        (by exact_mod_cast (hn i).2.1) (hn i).2.2
    · rw [dif_neg hj]
      exact (neutralNF589Pole_norm x hx).trans neutralNF589Pole_le_mode
  have hcrit (j : Fin 4) : ‖neutralNF588CriticalComplex j x‖ ≤ 33*Q := by
    unfold neutralNF588CriticalComplex
    have hterm (k : Fin 32) :
        ‖((neutralNF587CriticalSines[j.val]!)[k.val]! : ℂ) *
        Complex.sin (2*(Real.pi:ℂ)*(neutralNF587CriticalFrequencies[k.val]! : ℂ)*x)‖ ≤ Q := by
      have htrig := neutralNF589Oscillator_norm x
        (neutralNF587CriticalFrequencies[k.val]! : ℝ) 0 hx hy
        (by exact_mod_cast (hf k).1) (by exact_mod_cast (hf k).2) (by decide)
      simp only [pow_zero,even_zero,if_true,one_mul] at htrig
      have htrig' : ‖Complex.sin (2*(Real.pi:ℂ)*
          (neutralNF587CriticalFrequencies[k.val]! : ℂ)*x)‖ ≤ Q := by
        simpa only [Complex.ofReal_ratCast] using htrig
      have hcoef : ‖((neutralNF587CriticalSines[j.val]!)[k.val]! : ℂ)‖ ≤ 1 := by
        rw [← Complex.ofReal_ratCast,Complex.norm_real,Real.norm_eq_abs]
        exact_mod_cast hc j k
      rw [norm_mul]
      exact (mul_le_mul hcoef htrig' (norm_nonneg _) (by norm_num)).trans_eq (one_mul _)
    have hs : ‖∑ k : Fin 32, ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℂ) *
        Complex.sin (2*(Real.pi:ℂ)*(neutralNF587CriticalFrequencies[k.val]! : ℂ)*x)‖ ≤ 32*Q := by
      apply (norm_sum_le _ _).trans
      calc
        _ ≤ ∑ _k : Fin 32, Q := sum_le_sum (fun k _ => hterm k)
        _ = _ := by simp
    have hpol : ‖(neutralNF587CriticalPoles[j.val]! : ℂ)*Complex.sinh (x/2)‖ ≤ Q := by
      have hcoef : ‖(neutralNF587CriticalPoles[j.val]! : ℂ)‖ ≤ 1 := by
        rw [← Complex.ofReal_ratCast,Complex.norm_real,Real.norm_eq_abs]
        exact_mod_cast hp j
      rw [norm_mul]
      exact (mul_le_mul hcoef ((neutralNF589Pole_norm x hx).trans neutralNF589Pole_le_mode)
        (norm_nonneg _) (by norm_num)).trans_eq (one_mul _)
    exact (norm_add_le _ _).trans (by linarith)
  have hA : ‖∑ j : Fin 242, (a j:ℂ)*neutralNF588SelectedComplex j x‖ ≤
      242*((10:ℝ)^143*Q) := by
    apply (norm_sum_le _ _).trans
    calc
      _ ≤ ∑ _j : Fin 242, (10:ℝ)^143*Q := by
        apply sum_le_sum
        intro j _
        rw [norm_mul,Complex.norm_real,Real.norm_eq_abs]
        exact mul_le_mul (ha j) (hsel j) (norm_nonneg _) (by positivity)
      _ = _ := by simp
  have hB : ‖∑ j : Fin 4, (b j:ℂ)*neutralNF588CriticalComplex j x‖ ≤
      4*((10:ℝ)^143*(33*Q)) := by
    apply (norm_sum_le _ _).trans
    calc
      _ ≤ ∑ _j : Fin 4, (10:ℝ)^143*(33*Q) := by
        apply sum_le_sum
        intro j _
        rw [norm_mul,Complex.norm_real,Real.norm_eq_abs]
        exact mul_le_mul (hb j) (hcrit j) (norm_nonneg _) (by positivity)
      _ = _ := by simp
  change ‖neutralNF588SourceComplex a b x‖ ≤ _
  unfold neutralNF588SourceComplex
  calc
    _ ≤ _ := norm_add_le _ _
    _ ≤ 242*((10:ℝ)^143*Q)+4*((10:ℝ)^143*(33*Q)) := add_le_add hA hB
    _ = 374*((10:ℝ)^143*Q) := by ring
    _ ≤ 400*10^143*Q := by nlinarith [show 0 ≤ (10:ℝ)^143*Q by positivity]
    _ ≤ _ := neutralNF589Disc_arithmetic

end
end WeilDefect
