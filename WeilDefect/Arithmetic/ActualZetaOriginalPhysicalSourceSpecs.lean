import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEntryAssembly
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramPilotAssembly

namespace WeilDefect
noncomputable section

/-! NF624: the executable rational term specs are exactly the
historical source dictionary, including every original degree,
critical rational coefficient, and the genuine final pole. -/

def neutralNF624OscSpec (f : ℚ) (n : ℕ) (s : Bool) : NF622TermSpec :=
  if n%2=0 then
    ⟨neutralNF616OscKey f s,n,0,-neutralNF616Signed s (1/2)⟩
  else
    ⟨neutralNF616OscKey f s,n,1/2,0⟩

def neutralNF624PoleSpec (s : Bool) : NF622TermSpec :=
  ⟨neutralNF616PoleKey s,0,neutralNF616Signed s (1/2),0⟩

def NF622TermSpec.scale (t : NF622TermSpec) (c : ℚ) : NF622TermSpec :=
  ⟨t.key,t.degree,c*t.coeffRe,c*t.coeffIm⟩

theorem NF622TermSpec.scale_term (t : NF622TermSpec) (c : ℚ) :
    (t.scale c).term = {t.term with coeff := (c:ℂ)*t.term.coeff} := by
  unfold scale term coeff
  push_cast
  congr 1
  ring

theorem neutralNF624OscSpec_term (f : ℚ) (n : ℕ) (s : Bool) :
    (neutralNF624OscSpec f n s).term =
      if Even n then neutralNF607SinTerm (2*(Real.pi:ℂ)*(f:ℂ)) n s
      else neutralNF607CosTerm (2*(Real.pi:ℂ)*(f:ℂ)) n s := by
  have hs (s : Bool) :
      (neutralNF607SinTerm (2*(Real.pi:ℂ)*(f:ℂ)) n s).exponent =
        (neutralNF616OscKey f s).value := neutralNF616Osc_sin f n s
  have hc (s : Bool) :
      (neutralNF607CosTerm (2*(Real.pi:ℂ)*(f:ℂ)) n s).exponent =
        (neutralNF616OscKey f s).value := neutralNF616Osc_cos f n s
  by_cases he : Even n
  · have hn : n%2=0 := by rcases he with ⟨k,hk⟩; omega
    rw [if_pos he,neutralNF624OscSpec,if_pos hn]
    cases s <;>
      simp [NF622TermSpec.term,NF622TermSpec.coeff,neutralNF607SinTerm,
        neutralNF616Signed,neutralNF619SinCoeff,← hs] <;> ring
  · have hn : n%2≠0 := by
      intro h
      apply he
      exact ⟨n/2,by omega⟩
    rw [if_neg he,neutralNF624OscSpec,if_neg hn]
    cases s <;>
      simp [NF622TermSpec.term,NF622TermSpec.coeff,neutralNF607CosTerm,
        ← hc]

theorem neutralNF624PoleSpec_term (s : Bool) :
    (neutralNF624PoleSpec s).term = neutralNF607SinhTerm s := by
  have he := neutralNF616Pole s
  cases s <;>
    simp [neutralNF624PoleSpec,NF622TermSpec.term,NF622TermSpec.coeff,
      neutralNF616Signed,neutralNF607SinhTerm] at he ⊢ <;> exact he.symm

def neutralNF624SelectedSpec (i : Fin 242) (s : Bool) : NF622TermSpec :=
  if hi : i.val<241 then
    let node := nf545OriginalOscillatorNodeAt ⟨i.val,hi⟩
    neutralNF624OscSpec node.1 node.2 s
  else neutralNF624PoleSpec s

def neutralNF624CriticalSpec (j : Fin 4) (k : Fin 33) (s : Bool) : NF622TermSpec :=
  if k.val<32 then
    (neutralNF624OscSpec neutralNF587CriticalFrequencies[k.val]! 0 s).scale
      (neutralNF587CriticalSines[j.val]!)[k.val]!
  else (neutralNF624PoleSpec s).scale neutralNF587CriticalPoles[j.val]!

theorem neutralNF624SelectedSpec_term (i : Fin 242) (s : Bool) :
    (neutralNF624SelectedSpec i s).term = neutralNF607SelectedTerm i s := by
  unfold neutralNF624SelectedSpec neutralNF607SelectedTerm
  by_cases hi : i.val<241
  · simp only [dif_pos hi,neutralNF624OscSpec_term]
  · simp only [dif_neg hi,neutralNF624PoleSpec_term]

theorem neutralNF624CriticalSpec_term (j : Fin 4) (k : Fin 33) (s : Bool) :
    (neutralNF624CriticalSpec j k s).term = neutralNF607CriticalTerm j k s := by
  unfold neutralNF624CriticalSpec neutralNF607CriticalTerm
  by_cases hk : k.val<32
  · simp [hk,NF622TermSpec.scale_term,neutralNF624OscSpec_term]
  · simp [hk,NF622TermSpec.scale_term,neutralNF624PoleSpec_term]

def neutralNF624HBall (M : NF622Moments) (Q : ℕ) (i j : Fin 242) : NF591Ball :=
  (neutralNF622BlockRect M Q (neutralNF624SelectedSpec i) (neutralNF624SelectedSpec j)).re

def neutralNF624VBall (M : NF622Moments) (Q : ℕ) (i : Fin 242) (j : Fin 4) : NF591Ball :=
  (neutralNF622RectSum Finset.univ
    (fun k : Fin 33 => neutralNF622BlockRect M Q (neutralNF624SelectedSpec i)
      (neutralNF624CriticalSpec j k))).re

def neutralNF624AllMomentsSound (M : NF622Moments) : Prop :=
  (∀ (i j : Fin 242) (s t : Bool),
    let a := neutralNF624SelectedSpec i s
    let b := neutralNF624SelectedSpec j t
    (M (a.key.add b.key) (a.degree+b.degree)).Contains
      (neutralNF620J (a.key.add b.key).value (a.degree+b.degree))) ∧
  (∀ (i : Fin 242) (j : Fin 4) (k : Fin 33) (s t : Bool),
    let a := neutralNF624SelectedSpec i s
    let b := neutralNF624CriticalSpec j k t
    (M (a.key.add b.key) (a.degree+b.degree)).Contains
      (neutralNF620J (a.key.add b.key).value (a.degree+b.degree)))

theorem neutralNF624HBall_sound (M : NF622Moments) (Q : ℕ)
    (hQ : 0<Q) (hM : neutralNF624AllMomentsSound M) (i j : Fin 242) :
    (neutralNF624HBall M Q i j).Contains (neutralNF606PhysicalH i j) :=
  neutralNF622H_of_specs M Q hQ i j _ _
    (neutralNF624SelectedSpec_term i) (neutralNF624SelectedSpec_term j) (hM.1 i j)

theorem neutralNF624VBall_sound (M : NF622Moments) (Q : ℕ)
    (hQ : 0<Q) (hM : neutralNF624AllMomentsSound M) (i : Fin 242) (j : Fin 4) :
    (neutralNF624VBall M Q i j).Contains (neutralNF606PhysicalV i j) :=
  neutralNF622V_of_specs M Q hQ i j _ _
    (neutralNF624SelectedSpec_term i) (neutralNF624CriticalSpec_term j) (hM.2 i j)

end
end WeilDefect
