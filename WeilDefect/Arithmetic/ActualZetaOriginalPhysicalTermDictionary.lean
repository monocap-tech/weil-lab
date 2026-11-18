import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentRecurrence
import WeilDefect.Arithmetic.ActualZetaOriginalNF407NormalizedComplexSource

namespace WeilDefect
noncomputable section
open MeasureTheory intervalIntegral

/-! NF607: literal generator dictionaries for the actual physical
H,V matrix, using complex exponential polynomials. These are exact
function identities, not samples, approximations, or new generators. -/

structure NF607Term where
  coeff : ℂ
  degree : ℕ
  exponent : ℂ

def NF607Term.eval (t : NF607Term) (x : ℝ) : ℂ :=
  t.coeff * ((x:ℂ)^t.degree * Complex.exp (t.exponent*(x:ℂ)))

def neutralNF607SinTerm (w : ℂ) (n : ℕ) (sign : Bool) : NF607Term :=
  if sign then ⟨1/(2*Complex.I),n,Complex.I*w⟩
  else ⟨-1/(2*Complex.I),n,-Complex.I*w⟩

def neutralNF607CosTerm (w : ℂ) (n : ℕ) (sign : Bool) : NF607Term :=
  if sign then ⟨1/2,n,Complex.I*w⟩
  else ⟨1/2,n,-Complex.I*w⟩

def neutralNF607SinhTerm (sign : Bool) : NF607Term :=
  if sign then ⟨1/2,0,1/2⟩ else ⟨-1/2,0,-1/2⟩

theorem neutralNF607SinTerm_sum (w : ℂ) (n : ℕ) (x : ℝ) :
    (neutralNF607SinTerm w n true).eval x +
      (neutralNF607SinTerm w n false).eval x =
      (x:ℂ)^n * Complex.sin (w*(x:ℂ)) := by
  simp only [neutralNF607SinTerm,if_true,if_false,Bool.false_eq_true,NF607Term.eval,
    Complex.sin]
  have h : -Complex.I*w*(x:ℂ) = -(w*(x:ℂ))*Complex.I := by ring
  have h' : Complex.I*w*(x:ℂ) = w*(x:ℂ)*Complex.I := by ring
  rw [h,h']
  ring

theorem neutralNF607CosTerm_sum (w : ℂ) (n : ℕ) (x : ℝ) :
    (neutralNF607CosTerm w n true).eval x +
      (neutralNF607CosTerm w n false).eval x =
      (x:ℂ)^n * Complex.cos (w*(x:ℂ)) := by
  simp only [neutralNF607CosTerm,if_true,if_false,Bool.false_eq_true,NF607Term.eval,
    Complex.cos]
  have h : -Complex.I*w*(x:ℂ) = -(w*(x:ℂ))*Complex.I := by ring
  have h' : Complex.I*w*(x:ℂ) = w*(x:ℂ)*Complex.I := by ring
  rw [h,h']
  ring

theorem neutralNF607SinhTerm_sum (x : ℝ) :
    (neutralNF607SinhTerm true).eval x +
      (neutralNF607SinhTerm false).eval x =
      Complex.sinh ((x:ℂ)/2) := by
  simp only [neutralNF607SinhTerm,if_true,if_false,Bool.false_eq_true,NF607Term.eval,
    pow_zero,one_mul,Complex.sinh]
  rw [show (1/2:ℂ)*(x:ℂ)=(x:ℂ)/2 by ring,
    show (-1/2:ℂ)*(x:ℂ) = -((x:ℂ)/2) by ring]
  ring

def neutralNF607SelectedTerm (j : Fin 242) (s : Bool) : NF607Term :=
  if hj : j.val<241 then
    let node := nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩
    let w : ℂ := 2*(Real.pi:ℂ)*(node.1:ℂ)
    if Even node.2 then neutralNF607SinTerm w node.2 s
    else neutralNF607CosTerm w node.2 s
  else neutralNF607SinhTerm s

theorem neutralNF607SelectedTerm_sum (j : Fin 242) (x : ℝ) :
    (neutralNF607SelectedTerm j true).eval x+
      (neutralNF607SelectedTerm j false).eval x =
      (nf545OriginalSelectedRealGenerator j x:ℂ) := by
  rw [← neutralNF588SelectedComplex_ofReal]
  unfold neutralNF607SelectedTerm neutralNF588SelectedComplex
  by_cases hj : j.val<241
  · simp only [dif_pos hj]
    split_ifs
    · exact neutralNF607SinTerm_sum _ _ _
    · exact neutralNF607CosTerm_sum _ _ _
  · simp only [dif_neg hj]
    exact neutralNF607SinhTerm_sum x

def neutralNF607CriticalTerm (j : Fin 4) (k : Fin 33) (s : Bool) : NF607Term :=
  if hk : k.val<32 then
    let t := neutralNF607SinTerm
      (2*(Real.pi:ℂ)*(neutralNF587CriticalFrequencies[k.val]! : ℂ)) 0 s
    {t with coeff := ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℂ)*t.coeff}
  else
    let t := neutralNF607SinhTerm s
    {t with coeff := (neutralNF587CriticalPoles[j.val]! : ℂ)*t.coeff}

/-- Integral of a single product, used for every selected-selected
and selected-critical term pair. -/
theorem neutralNF607Term_product (a b : ℝ) (t u : NF607Term) :
    (∫ x in a..b, t.eval x*u.eval x) =
    t.coeff*u.coeff*neutralNF606ExpMoment a b (t.exponent+u.exponent)
      (t.degree+u.degree) := by
  have he : (fun x : ℝ => t.eval x*u.eval x) =
    (fun x : ℝ => (t.coeff*u.coeff)*
      (((x:ℂ)^t.degree*Complex.exp (t.exponent*(x:ℂ)))*
       ((x:ℂ)^u.degree*Complex.exp (u.exponent*(x:ℂ))))) := by
    funext x
    unfold NF607Term.eval
    ring
  rw [he,intervalIntegral.integral_const_mul,neutralNF606ExpMoment_product]

end
end WeilDefect
