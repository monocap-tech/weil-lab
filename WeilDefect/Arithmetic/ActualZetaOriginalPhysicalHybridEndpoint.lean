import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSemanticEndpointCache

namespace WeilDefect
noncomputable section

/-! Candidate: reuse a certified signed phase by exact rectangle conjugation.
The original table, frequency and residual checks remain unchanged.
Native compilation and strict axiom audit are required before adoption. -/

def nf618HybridConj (a : NF591Rect) : NF591Rect :=
  ⟨a.re, a.im.neg⟩

theorem nf618HybridConj_sound (a : NF591Rect) (z : ℂ)
    (hz : a.Contains z) :
    (nf618HybridConj a).Contains (starRingEnd ℂ z) := by
  constructor
  · simpa [nf618HybridConj] using hz.1
  · simpa [nf618HybridConj] using NF591Ball.contains_neg hz.2

def nf618HybridPhase (f : ℚ) : ℂ :=
  Complex.exp (Complex.I * ((2*Real.pi*(f:ℝ):ℝ):ℂ) * (11/10))

theorem nf618HybridPhase_neg (f : ℚ) :
    nf618HybridPhase (-f) = starRingEnd ℂ (nf618HybridPhase f) := by
  unfold nf618HybridPhase
  let x : ℝ := 2*Real.pi*(f:ℝ)
  have ha : (Complex.I * ((2*Real.pi*((-f:ℚ):ℝ):ℝ):ℂ) * (11/10)) =
      -((x:ℂ) * ((11/10:ℝ):ℂ) * Complex.I) := by
    dsimp [x]
    push_cast
    ring
  have hb : (Complex.I * ((2*Real.pi*(f:ℝ):ℝ):ℂ) * (11/10)) =
      (x:ℂ) * ((11/10:ℝ):ℂ) * Complex.I := by
    dsimp [x]
    push_cast
    ring
  rw [ha, hb]
  have hconj : (starRingEnd ℂ) ((x:ℂ) * ((11/10:ℝ):ℂ) * Complex.I) =
      -((x:ℂ) * ((11/10:ℝ):ℂ) * Complex.I) := by
    simp only [map_mul, Complex.conj_ofReal, Complex.conj_I]
    ring
  rw [← hconj]
  first | exact Complex.exp_conj _ | exact (Complex.exp_conj _).symm
        | simp [Complex.exp_conj]

def nf618HybridCache (p : NF591Ball) (h f : ℚ) (Q : ℕ)
    (Rp Rn P : NF591Rect) (positive : Bool) : NF617MomentCache :=
  let Pp := if positive then P else nf618HybridConj P
  let Pn := if positive then nf618HybridConj P else P
  ⟨neutralNF615LambdaRect p h f Q, Rp.mulQ Pp Q, Rn.mulQ Pn Q⟩

theorem nf618HybridEndpoint_sound (h f : ℚ) (Q : ℕ) (hQ : 0<Q)
    (R P : NF591Rect)
    (hr : R.Contains (Complex.exp ((h:ℂ)*(11/10))))
    (hp : P.Contains (nf618HybridPhase f)) :
    (R.mulQ P Q).Contains (Complex.exp (neutralNF615Lambda h f*(11/10))) := by
  unfold neutralNF615Lambda
  rw [add_mul, Complex.exp_add]
  exact NF591Rect.contains_mulQ hr hp Q hQ

theorem nf618HybridCache_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (h f : ℚ) (Q : ℕ) (hQ : 0<Q) (Rp Rn P : NF591Rect)
    (hrp : Rp.Contains (Complex.exp ((h:ℂ)*(11/10))))
    (hrn : Rn.Contains (Complex.exp (((-h:ℚ):ℂ)*(11/10))))
    (positive : Bool)
    (hs : P.Contains (nf618HybridPhase (if positive then f else -f))) :
    (nf618HybridCache p h f Q Rp Rn P positive).SemanticSound ⟨h,f⟩ := by
  let Pp := if positive then P else nf618HybridConj P
  let Pn := if positive then nf618HybridConj P else P
  have hpp : Pp.Contains (nf618HybridPhase f) := by
    cases positive with
    | false =>
      have h := nf618HybridConj_sound P _ (show P.Contains (nf618HybridPhase (-f)) from hs)
      rw [← nf618HybridPhase_neg (-f), neg_neg] at h
      exact h
    | true => exact hs
  have hpn : Pn.Contains (nf618HybridPhase (-f)) := by
    cases positive with
    | false => exact hs
    | true =>
      have h := nf618HybridConj_sound P _ (show P.Contains (nf618HybridPhase f) from hs)
      rw [← nf618HybridPhase_neg f] at h
      exact h
  have hpos := nf618HybridEndpoint_sound h f Q hQ Rp Pp hrp hpp
  have hneg := nf618HybridEndpoint_sound (-h) (-f) Q hQ Rn Pn hrn hpn
  rw [neutralNF615Lambda_neg, neg_mul, ← mul_neg] at hneg
  refine ⟨neutralNF615LambdaRect_sound p hp h f Q hQ, ?_, ?_⟩
  · simpa [nf618HybridCache, Pp, Pn, NF616Frequency.value] using hpos
  · simpa [nf618HybridCache, Pp, Pn, NF616Frequency.value] using hneg

theorem nf618HybridTable_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (t : NF624KeyTable) (Q : ℕ) (hQ : 0<Q) (Rp Rn P : NF591Rect)
    (hrp : Rp.Contains (Complex.exp ((t.key.h:ℂ)*(11/10))))
    (hrn : Rn.Contains (Complex.exp (((-t.key.h:ℚ):ℂ)*(11/10))))
    (positive : Bool)
    (hs : P.Contains (nf618HybridPhase (if positive then t.key.f else -t.key.f)))
    (hd : 0<t.key.lower)
    (hc : ∀ n < t.rows.size, neutralNF617MomentRowCheck
      (nf618HybridCache p t.key.h t.key.f Q Rp Rn P positive)
      t.key.lower Q t.rows n = true) : neutralNF690TableSound t := by
  exact neutralNF690TableSound_of_semantic_cache
    (nf618HybridCache p t.key.h t.key.f Q Rp Rn P positive) t
    (nf618HybridCache_sound p hp t.key.h t.key.f Q hQ Rp Rn P hrp hrn positive hs)
    hd Q hQ hc

end
end WeilDefect
