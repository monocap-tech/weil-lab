import WeilDefect.Arithmetic.ActualZetaOriginalJetRecurrence
import WeilDefect.Arithmetic.ActualZetaOriginalNF407NormalizedComplexSource

namespace WeilDefect
noncomputable section
open Finset

/-! NF590: the exact real coefficient recurrence of the UNGROUPED
original NF407 source. NF587 groups equal oscillator nodes only
to reduce interval work. The source is the same linear combination. -/

def neutralNF590OscillatorJet (f : ℝ) (k n : ℕ) : ℝ :=
  let ω := 2*Real.pi*f
  let α : ℂ := if Even k then -Complex.I else 1
  (α*Complex.exp (Complex.I*(ω:ℂ)*(11/10))*
    neutralNF590ModeJet (11/10) (-1/500)
      (-(Complex.I*(ω:ℂ))/500) k n).re

theorem neutralNF590OscillatorJet_hasSum (f : ℝ) (k : ℕ) (w : ℝ) :
    HasSum (fun n : ℕ => neutralNF590OscillatorJet f k n*w^n)
      ((11/10-w/500)^k*
        (if Even k then Real.sin (2*Real.pi*f*(11/10-w/500))
        else Real.cos (2*Real.pi*f*(11/10-w/500)))) := by
  let ω := 2*Real.pi*f
  let α : ℂ := if Even k then -Complex.I else 1
  let B : ℂ := 11/10
  let D : ℂ := -1/500
  let lam : ℂ := -(Complex.I*(ω:ℂ))/500
  have h := (neutralNF590ModeJet_hasSum B D lam (w:ℂ) k).mul_left
    (α*Complex.exp (Complex.I*(ω:ℂ)*B))
  have hr := Complex.reCLM.hasSum h
  convert hr using 1
  · funext n
    change neutralNF590OscillatorJet f k n*w^n =
      (α*Complex.exp (Complex.I*(ω:ℂ)*B)*
        (neutralNF590ModeJet B D lam k n*(w:ℂ)^n)).re
    rw [← mul_assoc, ← Complex.ofReal_pow]
    simp [neutralNF590OscillatorJet,ω,α,B,D,lam,Complex.mul_re,mul_comm]
  · let x : ℝ := 11/10-w/500
    have hx : B+D*(w:ℂ) = (x:ℂ) := by
      dsimp [B,D,x]
      push_cast
      ring
    have hphase : Complex.I*(ω:ℂ)*B+lam*(w:ℂ) = Complex.I*((ω*x:ℝ):ℂ) := by
      dsimp [B,lam,x]
      push_cast
      ring
    change x^k*(if Even k then Real.sin (ω*x) else Real.cos (ω*x)) =
      (α*Complex.exp (Complex.I*(ω:ℂ)*B)*
        ((B+D*(w:ℂ))^k*Complex.exp (lam*(w:ℂ)))).re
    rw [hx]
    have he : α*Complex.exp (Complex.I*(ω:ℂ)*B)*
        ((x:ℂ)^k*Complex.exp (lam*(w:ℂ))) =
        (x:ℂ)^k*α*Complex.exp (Complex.I*((ω*x:ℝ):ℂ)) := by
      rw [← hphase,Complex.exp_add]
      ring
    rw [he,← Complex.ofReal_pow]
    by_cases hk : Even k
    · simp [α,hk,Complex.mul_re,Complex.mul_im,Complex.exp_re,Complex.exp_im]
    · simp [α,hk,Complex.mul_re,Complex.mul_im,Complex.exp_re,Complex.exp_im]

/-- The true sinh mode is the difference of two real exponential
recurrences, not an oscillatory approximation to the pole. -/
def neutralNF590PoleJet (n : ℕ) : ℝ :=
  ((Complex.exp (11/20)*neutralNF590ExpJet (-1/1000) n -
    Complex.exp (-11/20)*neutralNF590ExpJet (1/1000) n).re)/2

theorem neutralNF590PoleJet_hasSum (w : ℝ) :
    HasSum (fun n : ℕ => neutralNF590PoleJet n*w^n)
      (Real.sinh ((11/10-w/500)/2)) := by
  have hp := (neutralNF590ExpJet_hasSum (-1/1000) (w:ℂ)).mul_left
    (Complex.exp (11/20))
  have hn := (neutralNF590ExpJet_hasSum (1/1000) (w:ℂ)).mul_left
    (Complex.exp (-11/20))
  have h := (Complex.reCLM.hasSum (hp.sub hn)).mul_left (1/2:ℝ)
  convert h using 1
  · funext n
    unfold neutralNF590PoleJet
    simp only [ContinuousLinearMap.coe_sub,Complex.reCLM_apply,
      ← mul_assoc,← Complex.ofReal_pow,Complex.sub_re,Complex.mul_re,
      Complex.ofReal_re,Complex.ofReal_im,mul_zero,sub_zero]
    ring
  · change Real.sinh ((11/10-w/500)/2) =
      (1/2:ℝ)*(Complex.exp (11/20)*Complex.exp ((-1/1000:ℂ)*(w:ℂ)) -
        Complex.exp (-11/20)*Complex.exp ((1/1000:ℂ)*(w:ℂ))).re
    rw [← Complex.exp_add,← Complex.exp_add]
    have hp' : (11/20:ℂ)+(-1/1000:ℂ)*(w:ℂ) =
        (((11/10-w/500)/2:ℝ):ℂ) := by push_cast; ring
    have hn' : (-11/20:ℂ)+(1/1000:ℂ)*(w:ℂ) =
        ((-((11/10-w/500)/2):ℝ):ℂ) := by push_cast; ring
    rw [hp',hn',← Complex.ofReal_exp,← Complex.ofReal_exp,
      Complex.sub_re,Complex.ofReal_re,Complex.ofReal_re,Real.sinh_eq]
    ring

def neutralNF590SelectedJet (j : Fin 242) (n : ℕ) : ℝ :=
  if hj : j.val < 241 then
    let node := nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩
    neutralNF590OscillatorJet (node.1:ℝ) node.2 n
  else neutralNF590PoleJet n

def neutralNF590CriticalJet (j : Fin 4) (n : ℕ) : ℝ :=
  (∑ k : Fin 32, ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ)*
    neutralNF590OscillatorJet (neutralNF587CriticalFrequencies[k.val]! : ℝ) 0 n) +
      (neutralNF587CriticalPoles[j.val]! : ℝ)*neutralNF590PoleJet n

def neutralNF590SourceJet (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (n : ℕ) : ℝ :=
  (∑ j : Fin 242, a j*neutralNF590SelectedJet j n) +
    ∑ j : Fin 4, b j*neutralNF590CriticalJet j n

theorem neutralNF590SelectedJet_hasSum (j : Fin 242) (w : ℝ) :
    HasSum (fun n : ℕ => neutralNF590SelectedJet j n*w^n)
      (nf545OriginalSelectedRealGenerator j (11/10-w/500)) := by
  unfold neutralNF590SelectedJet nf545OriginalSelectedRealGenerator
  by_cases hj : j.val < 241
  · simp only [dif_pos hj]
    exact neutralNF590OscillatorJet_hasSum _ _ w
  · simp only [dif_neg hj]
    exact neutralNF590PoleJet_hasSum w

theorem neutralNF590CriticalJet_hasSum (j : Fin 4) (w : ℝ) :
    HasSum (fun n : ℕ => neutralNF590CriticalJet j n*w^n)
      (neutralNF587CriticalGenerator j (11/10-w/500)) := by
  have ho (k : Fin 32) := (neutralNF590OscillatorJet_hasSum
    (neutralNF587CriticalFrequencies[k.val]! : ℝ) 0 w).mul_left
      ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ)
  have hs := hasSum_sum (s := univ) (fun k _ => ho k)
  have hp := (neutralNF590PoleJet_hasSum w).mul_left
    (neutralNF587CriticalPoles[j.val]! : ℝ)
  convert hs.add hp using 1
  · funext n
    unfold neutralNF590CriticalJet
    rw [add_mul,sum_mul]
    simp_rw [mul_assoc]
  · simp [neutralNF587CriticalGenerator]

theorem neutralNF590SourceJet_hasSum (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (w : ℝ) :
    HasSum (fun n : ℕ => neutralNF590SourceJet a b n*w^n)
      (neutralNF587Source a b (11/10-w/500)) := by
  have ha := hasSum_sum (s := univ) (fun j : Fin 242 => fun _ =>
    (neutralNF590SelectedJet_hasSum j w).mul_left (a j))
  have hb := hasSum_sum (s := univ) (fun j : Fin 4 => fun _ =>
    (neutralNF590CriticalJet_hasSum j w).mul_left (b j))
  convert ha.add hb using 1
  · funext n
    unfold neutralNF590SourceJet
    rw [add_mul,sum_mul,sum_mul]
    simp_rw [mul_assoc]
  · rfl

/-- Canonical Cauchy coefficient equals the exact finite recurrence,
for every coefficient choice and every n. No cutoff or disc bound
is needed for coefficient identity. -/
theorem neutralNF590SourceJet_eq_canonical (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    neutralNF590SourceJet a b =
      neutralNF588NormalizedCoefficient (neutralNF588NormalizedSource a b) := by
  apply neutralNF590RealSeries_unique _ _
    (fun w => neutralNF587Source a b (11/10-w/500))
  · exact neutralNF590SourceJet_hasSum a b
  · intro w
    simpa only [neutralNF588NormalizedSource_ofReal,Complex.ofReal_re] using
      neutralNF588NormalizedCoefficient_value (neutralNF588NormalizedSource a b)
        (neutralNF588NormalizedSource_differentiable a b) w

end
end WeilDefect
