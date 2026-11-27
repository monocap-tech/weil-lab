import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalHybridEndpoint

namespace WeilDefect
noncomputable section

/-! W02-NF-08: uncompiled generic containment candidate. -/
def nf618W02RectPow (a : NF591Rect) (Q : ℕ) : ℕ → NF591Rect
  | 0 => NF591Rect.one
  | n+1 => if n=0 then a else (nf618W02RectPow a Q n).mulQ a Q

theorem nf618W02RectPow_sound (a : NF591Rect) (z : ℂ)
    (Q : ℕ) (hQ : 0<Q) (ha : a.Contains z) (n : ℕ) :
    (nf618W02RectPow a Q n).Contains (z^n) := by
  induction n with
  | zero => simpa [nf618W02RectPow] using NF591Rect.contains_one
  | succ n ih =>
    by_cases hn : n=0
    · subst n
      simpa [nf618W02RectPow] using ha
    · simpa only [nf618W02RectPow, if_neg hn, pow_succ] using
        NF591Rect.contains_mulQ ih ha Q hQ

theorem nf618W02Phase_add (f g : ℚ) :
    nf618HybridPhase (f+g) = nf618HybridPhase f * nf618HybridPhase g := by
  unfold nf618HybridPhase
  rw [← Complex.exp_add]
  congr 1
  push_cast
  ring

theorem nf618W02Phase_nat (f : ℚ) (n : ℕ) :
    nf618HybridPhase ((n:ℚ)*f) = nf618HybridPhase f ^ n := by
  induction n with
  | zero => simp [nf618HybridPhase]
  | succ n ih =>
    rw [show ((n+1:ℕ):ℚ)*f=(n:ℚ)*f+f by push_cast; ring,
      nf618W02Phase_add, ih, pow_succ]

theorem nf618W02Phase_turn (t : ℤ) :
    nf618HybridPhase ((t:ℚ)*(10/11)) = 1 := by
  unfold nf618HybridPhase
  have he : Complex.I * ((2*Real.pi*(((t:ℚ)*(10/11):ℚ):ℝ):ℝ):ℂ) *
      (11/10) = (t:ℂ)*(2*(Real.pi:ℂ)*Complex.I) := by
    push_cast
    ring
  rw [he, Complex.exp_int_mul_two_pi_mul_I]

theorem nf618W02Phase_decompose (f : ℚ) (t : ℤ) (q r : ℕ)
    (positive : Bool)
    (hf : f=(t:ℚ)*(10/11)+(q:ℚ)*(5/22)+
      (if positive then (r:ℚ)*(1/1408) else -((r:ℚ)*(1/1408)))) :
    nf618HybridPhase f =
      nf618HybridPhase (5/22)^q *
      (if positive then nf618HybridPhase (1/1408)^r
        else starRingEnd ℂ (nf618HybridPhase (1/1408)^r)) := by
  rw [hf, nf618W02Phase_add, nf618W02Phase_add,
    nf618W02Phase_turn, one_mul, nf618W02Phase_nat]
  cases positive <;> simp [nf618HybridPhase_neg, nf618W02Phase_nat]

def nf618W02PhaseRect (seed quarter : NF591Rect) (Q q r : ℕ)
    (positive : Bool) : NF591Rect :=
  let a := nf618W02RectPow seed Q r
  (nf618W02RectPow quarter Q q).mulQ
    (if positive then a else nf618HybridConj a) Q

theorem nf618W02PhaseRect_sound (seed quarter : NF591Rect)
    (Q : ℕ) (hQ : 0<Q)
    (hs : seed.Contains (nf618HybridPhase (1/1408)))
    (hq : quarter.Contains (nf618HybridPhase (5/22)))
    (f : ℚ) (t : ℤ) (q r : ℕ) (positive : Bool)
    (hf : f=(t:ℚ)*(10/11)+(q:ℚ)*(5/22)+
      (if positive then (r:ℚ)*(1/1408) else -((r:ℚ)*(1/1408)))) :
    (nf618W02PhaseRect seed quarter Q q r positive).Contains
      (nf618HybridPhase f) := by
  rw [nf618W02Phase_decompose f t q r positive hf]
  have hr := nf618W02RectPow_sound seed _ Q hQ hs r
  have hquarter := nf618W02RectPow_sound quarter _ Q hQ hq q
  cases positive with
  | false =>
    simpa [nf618W02PhaseRect] using
      NF591Rect.contains_mulQ hquarter (nf618HybridConj_sound _ _ hr) Q hQ
  | true =>
    simpa [nf618W02PhaseRect] using NF591Rect.contains_mulQ hquarter hr Q hQ

theorem nf618W02RootTable_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (t : NF624KeyTable) (Q : ℕ) (hQ : 0<Q)
    (Rp Rn seed quarter : NF591Rect)
    (hrp : Rp.Contains (Complex.exp ((t.key.h:ℂ)*(11/10))))
    (hrn : Rn.Contains (Complex.exp (((-t.key.h:ℚ):ℂ)*(11/10))))
    (hs : seed.Contains (nf618HybridPhase (1/1408)))
    (hq : quarter.Contains (nf618HybridPhase (5/22)))
    (turns : ℤ) (q r : ℕ) (positive : Bool)
    (hf : t.key.f=(turns:ℚ)*(10/11)+(q:ℚ)*(5/22)+
      (if positive then (r:ℚ)*(1/1408) else -((r:ℚ)*(1/1408))))
    (hd : 0<t.key.lower)
    (hc : ∀ n < t.rows.size, neutralNF617MomentRowCheck
      (nf618HybridCache p t.key.h t.key.f Q Rp Rn
        (nf618W02PhaseRect seed quarter Q q r positive) true)
      t.key.lower Q t.rows n = true) : neutralNF690TableSound t := by
  apply nf618HybridTable_sound p hp t Q hQ Rp Rn
    (nf618W02PhaseRect seed quarter Q q r positive) hrp hrn true _ hd hc
  simpa using nf618W02PhaseRect_sound seed quarter Q hQ hs hq
    t.key.f turns q r positive hf

#print axioms nf618W02RectPow_sound
#print axioms nf618W02Phase_add
#print axioms nf618W02Phase_nat
#print axioms nf618W02Phase_turn
#print axioms nf618W02Phase_decompose
#print axioms nf618W02PhaseRect_sound
#print axioms nf618W02RootTable_sound

end
end WeilDefect
