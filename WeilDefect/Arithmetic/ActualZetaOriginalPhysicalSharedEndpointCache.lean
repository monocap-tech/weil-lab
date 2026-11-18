import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalChunkedBank

namespace WeilDefect

/-! NF634: the shared endpoint bank is a proposal, not a trusted oracle.
Its exact per-key identities are premises separate from the moment
residual gates. Both signs use the same reduced-phase lookup. -/

def neutralNF634PhaseReduced (p : NF591Ball) (u : ℚ) (Q N : ℕ) : NF591Rect :=
  let a := neutralNF593SmallExp
    ⟨⟨0,0⟩,(p.mul (NF591Ball.exactQ (u/2) Q)).round Q⟩ Q N
  let b := a.mulQ a Q
  b.mulQ b Q

theorem neutralNF634PhaseReduced_eq (p : NF591Ball) (f : ℚ) (Q N : ℕ) :
    neutralNF634PhaseReduced p (neutralNF592Reduced f) Q N =
      neutralNF593Phase p f Q N := rfl

def neutralNF634SharedCache (p : NF591Ball) (R P : ℚ → NF591Rect)
    (k : NF616Frequency) : NF617MomentCache :=
  ⟨neutralNF615LambdaRect p k.h k.f neutralNF616Q,
    (R k.h).mulQ (P (neutralNF592Reduced k.f)) neutralNF616Q,
    (R (-k.h)).mulQ (P (neutralNF592Reduced (-k.f))) neutralNF616Q⟩

theorem neutralNF634SharedCache_eq (p : NF591Ball) (R P : ℚ → NF591Rect)
    (k : NF616Frequency)
    (hr : R k.h = neutralNF621RealEndpoint k.h neutralNF616Q neutralNF616ExpN)
    (hrn : R (-k.h) = neutralNF621RealEndpoint (-k.h) neutralNF616Q neutralNF616ExpN)
    (hp : P (neutralNF592Reduced k.f) =
      neutralNF634PhaseReduced p (neutralNF592Reduced k.f) neutralNF616Q neutralNF616ExpN)
    (hpn : P (neutralNF592Reduced (-k.f)) =
      neutralNF634PhaseReduced p (neutralNF592Reduced (-k.f)) neutralNF616Q neutralNF616ExpN) :
    neutralNF634SharedCache p R P k =
      neutralNF621Cache p k neutralNF616Q neutralNF616ExpN := by
  unfold neutralNF634SharedCache neutralNF621Cache neutralNF621Endpoint
  rw [hr,hrn,hp,hpn,neutralNF634PhaseReduced_eq,neutralNF634PhaseReduced_eq]

def neutralNF634SharedKeyCheck (p : NF591Ball) (R P : ℚ → NF591Rect)
    (t : NF624KeyTable) : Bool :=
  let k := t.key
  let c := neutralNF634SharedCache p R P k
  decide (0<neutralNF616Q ∧ 0<neutralNF616ExpN ∧ |k.h|≤1 ∧
    0<k.lower ∧ 0<t.rows.size) &&
  (List.range t.rows.size).all (neutralNF617MomentRowCheck c k.lower neutralNF616Q t.rows)

theorem neutralNF634SharedKeyCheck_eq (p : NF591Ball) (R P : ℚ → NF591Rect)
    (t : NF624KeyTable)
    (hc : neutralNF634SharedCache p R P t.key =
      neutralNF621Cache p t.key neutralNF616Q neutralNF616ExpN) :
    neutralNF634SharedKeyCheck p R P t = neutralNF628FastKeyCheck p t := by
  unfold neutralNF634SharedKeyCheck neutralNF628FastKeyCheck neutralNF621FastTableCheck
  dsimp only
  rw [hc]

def neutralNF634SharedChunkCheck (p : NF591Ball) (R P : ℚ → NF591Rect)
    (chunk : Array NF624KeyTable) : Bool :=
  chunk.toList.all (neutralNF634SharedKeyCheck p R P)

theorem neutralNF634OriginalChunk_of_shared (p : NF591Ball) (R P : ℚ → NF591Rect)
    (chunk : Array NF624KeyTable)
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hc : ∀ t ∈ chunk.toList, neutralNF634SharedCache p R P t.key =
      neutralNF621Cache p t.key neutralNF616Q neutralNF616ExpN)
    (hg : neutralNF634SharedChunkCheck p R P chunk = true) :
    neutralNF628ChunkCheck chunk = true := by
  unfold neutralNF628ChunkCheck
  dsimp only
  rw [hpi]
  apply List.all_eq_true.mpr
  intro t ht
  rw [← neutralNF634SharedKeyCheck_eq p R P t (hc t ht)]
  exact (List.all_eq_true.mp hg) t ht

theorem neutralNF634Bank_of_shared (p : NF591Ball) (R P : ℚ → NF591Rect)
    (chunks : List (Array NF624KeyTable))
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hc : ∀ chunk ∈ chunks, ∀ t ∈ chunk.toList,
      neutralNF634SharedCache p R P t.key =
        neutralNF621Cache p t.key neutralNF616Q neutralNF616ExpN)
    (hg : ∀ chunk ∈ chunks, neutralNF634SharedChunkCheck p R P chunk = true) :
    neutralNF624BankCheck (neutralNF628Join chunks) = true := by
  apply neutralNF628Bank_of_chunks
  apply List.all_eq_true.mpr
  intro chunk hm
  exact neutralNF634OriginalChunk_of_shared p R P chunk hpi (hc chunk hm) (hg chunk hm)

end WeilDefect
