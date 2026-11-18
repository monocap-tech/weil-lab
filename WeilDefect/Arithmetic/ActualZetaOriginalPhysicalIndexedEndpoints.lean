import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSharedEndpointCache

namespace WeilDefect

/-! NF635: finite endpoint receipt custody and cheap source coverage.
The index is untrusted; each use checks the returned parameter, and
all declared values must have separate reference equalities. Metadata
checking does not inspect any high-precision endpoint coordinate. -/

def neutralNF635ParamRead (keys : Array ℚ) (i : ℕ) : ℚ :=
  keys[i]?.getD 0

def neutralNF635Search (keys : Array ℚ) (q : ℚ) : ℕ → ℕ → ℕ → ℕ
  | 0, _, _ => keys.size
  | fuel+1, lo, hi =>
    if lo<hi then
      let m := (lo+hi)/2
      let v := neutralNF635ParamRead keys m
      if v=q then m
      else if v<q then neutralNF635Search keys q fuel (m+1) hi
      else neutralNF635Search keys q fuel lo m
    else keys.size

def neutralNF635Index (keys : Array ℚ) (q : ℚ) : ℕ :=
  neutralNF635Search keys q 16 0 keys.size

def neutralNF635ParamCheck (keys : Array ℚ) (q : ℚ) : Bool :=
  let i := neutralNF635Index keys q
  decide (i<keys.size ∧ neutralNF635ParamRead keys i=q)

structure NF635EndpointBank where
  keys : Array ℚ
  values : Array NF591Rect

def NF635EndpointBank.read (b : NF635EndpointBank) (i : ℕ) : NF591Rect :=
  b.values[i]?.getD NF591Rect.zero

def NF635EndpointBank.lookup (b : NF635EndpointBank) (q : ℚ) : NF591Rect :=
  b.read (neutralNF635Index b.keys q)

def NF635EndpointBank.Valid (b : NF635EndpointBank) (ref : ℚ → NF591Rect) : Prop :=
  b.values.size=b.keys.size ∧
  ∀ i < b.keys.size, b.read i=ref (neutralNF635ParamRead b.keys i)

theorem NF635EndpointBank.lookup_eq (b : NF635EndpointBank)
    (ref : ℚ → NF591Rect) (hv : b.Valid ref) (q : ℚ)
    (hc : neutralNF635ParamCheck b.keys q=true) :
    b.lookup q=ref q := by
  let i := neutralNF635Index b.keys q
  have h : i<b.keys.size ∧ neutralNF635ParamRead b.keys i=q :=
    of_decide_eq_true hc
  unfold NF635EndpointBank.lookup
  change b.read i=ref q
  rw [hv.2 i h.1,h.2]

def neutralNF635FrequencyCoverage (rs ps : Array ℚ) (k : NF616Frequency) : Bool :=
  neutralNF635ParamCheck rs k.h &&
  (neutralNF635ParamCheck rs (-k.h) &&
  (neutralNF635ParamCheck ps (neutralNF592Reduced k.f) &&
   neutralNF635ParamCheck ps (neutralNF592Reduced (-k.f))))

def neutralNF635KeyCoverage (rs ps : Array ℚ) (t : NF624KeyTable) : Bool :=
  neutralNF635FrequencyCoverage rs ps t.key

def neutralNF635ChunkCoverage (rs ps : Array ℚ) (chunk : Array NF624KeyTable) : Bool :=
  (chunk.toList.map NF624KeyTable.key).all (neutralNF635FrequencyCoverage rs ps)

theorem neutralNF635ChunkCoverage_of_keys (rs ps : Array ℚ)
    (chunk : Array NF624KeyTable) (ks : List NF616Frequency)
    (hk : chunk.toList.map NF624KeyTable.key=ks)
    (hc : ks.all (neutralNF635FrequencyCoverage rs ps)=true) :
    neutralNF635ChunkCoverage rs ps chunk=true := by
  unfold neutralNF635ChunkCoverage
  rw [hk]
  exact hc

def neutralNF635RealRef (h : ℚ) : NF591Rect :=
  neutralNF621RealEndpoint h neutralNF616Q neutralNF616ExpN

def neutralNF635PhaseRef (p : NF591Ball) (u : ℚ) : NF591Rect :=
  neutralNF634PhaseReduced p u neutralNF616Q neutralNF616ExpN

theorem neutralNF635Cache_of_coverage (p : NF591Ball) (R P : NF635EndpointBank)
    (hr : R.Valid neutralNF635RealRef)
    (hp : P.Valid (neutralNF635PhaseRef p))
    (t : NF624KeyTable)
    (hc : neutralNF635KeyCoverage R.keys P.keys t=true) :
    neutralNF634SharedCache p R.lookup P.lookup t.key =
      neutralNF621Cache p t.key neutralNF616Q neutralNF616ExpN := by
  simp only [neutralNF635KeyCoverage,neutralNF635FrequencyCoverage,Bool.and_eq_true] at hc
  exact neutralNF634SharedCache_eq p R.lookup P.lookup t.key
    (R.lookup_eq _ hr _ hc.1)
    (R.lookup_eq _ hr _ hc.2.1)
    (P.lookup_eq _ hp _ hc.2.2.1)
    (P.lookup_eq _ hp _ hc.2.2.2)

theorem neutralNF635Bank_of_indexed (p : NF591Ball) (R P : NF635EndpointBank)
    (chunks : List (Array NF624KeyTable))
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hr : R.Valid neutralNF635RealRef)
    (hp : P.Valid (neutralNF635PhaseRef p))
    (hc : ∀ chunk ∈ chunks, neutralNF635ChunkCoverage R.keys P.keys chunk=true)
    (hg : ∀ chunk ∈ chunks,
      neutralNF634SharedChunkCheck p R.lookup P.lookup chunk=true) :
    neutralNF624BankCheck (neutralNF628Join chunks)=true := by
  apply neutralNF634Bank_of_shared p R.lookup P.lookup chunks hpi _ hg
  intro chunk hchunk t ht
  have h := hc chunk hchunk
  unfold neutralNF635ChunkCoverage at h
  exact neutralNF635Cache_of_coverage p R P hr hp t
    ((List.all_eq_true.mp h) t.key (List.mem_map.mpr ⟨t,ht,rfl⟩))

end WeilDefect
