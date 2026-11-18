import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerBoundary
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalChunkedBank

namespace WeilDefect

/-! NF638: one integer certificate per actual nonzero frequency.
The denotation fixes the exact rows and the key of the reference
table by construction. Only the three input cache rectangles
require separate reference identities; all boundary and row gates
are on integer coordinates. -/

structure NF638Table where
  key : NF616Frequency
  d : ℤ
  e : ℤ
  cache : NF638Cache
  rows : Array NF637Row

def NF638Table.read (t : NF638Table) (n : ℕ) : NF637Row :=
  t.rows[n]?.getD ⟨0,0,0⟩

def NF638Table.keyTable (t : NF638Table) (Q : ℕ) : NF624KeyTable :=
  ⟨t.key,t.rows.map (fun q => q.denote Q)⟩

theorem NF638Table.read_denote (t : NF638Table) (Q n : ℕ)
    (hn : n<t.rows.size) :
    neutralNF617MomentRead (t.keyTable Q).rows n=(t.read n).denote Q := by
  have he : t.rows[n]?=some t.rows[n] := by simp [hn]
  simp [NF638Table.keyTable,neutralNF617MomentRead,NF638Table.read,he]

def NF638Table.rowGate (t : NF638Table) (Q : ℕ) (n : ℕ) : Bool :=
  t.cache.boundaryGate Q n &&
    match n with
    | 0 => neutralNF637BaseGate (t.cache.boundary Q 0) t.cache.z
        (t.read 0) Q t.d t.e
    | m+1 => neutralNF637SuccGate (t.cache.boundary Q (m+1)) t.cache.z
        (t.read (m+1)) (t.read m) Q m t.d t.e

def NF638Table.paramGate (t : NF638Table) (Q N : ℕ) : Bool :=
  decide (0<Q ∧ 0<N ∧ |t.key.h|≤1 ∧ 0<t.key.lower ∧
    0<t.rows.size ∧ t.key.lower=(t.d:ℚ)/t.e)

def NF638Table.check (t : NF638Table) (Q N : ℕ) : Bool :=
  t.paramGate Q N && (List.range t.rows.size).all (t.rowGate Q)

theorem NF638Table.row_to_ref (t : NF638Table) (Q n : ℕ)
    (hQ : 0<Q) (hn : n<t.rows.size)
    (hd : t.key.lower=(t.d:ℚ)/t.e)
    (h : t.rowGate Q n=true) :
    neutralNF617MomentRowCheck (t.cache.denote Q) t.key.lower Q
      (t.keyTable Q).rows n=true := by
  cases n with
  | zero =>
    simp only [NF638Table.rowGate,Bool.and_eq_true] at h
    have hg := neutralNF637Base_to_ref _ _ _ Q t.d t.e hQ
      ((t.read 0).point_denote Q hQ) h.2
    rw [NF638Cache.boundary_denote _ _ _ hQ h.1,← hd] at hg
    simp only [neutralNF617MomentRowCheck,t.read_denote Q 0 hn,Bool.and_eq_true]
    exact ⟨decide_eq_true hg.1,hg.2⟩
  | succ m =>
    simp only [NF638Table.rowGate,Bool.and_eq_true] at h
    have hp : m<t.rows.size := by omega
    have hg := neutralNF637Succ_to_ref _ _ _ _ Q m t.d t.e hQ
      ((t.read (m+1)).point_denote Q hQ) ((t.read m).point_denote Q hQ)
      (neutralNF638NatRect_denote Q (m+1) hQ) h.2
    rw [NF638Cache.boundary_denote _ _ _ hQ h.1,← hd] at hg
    simp only [neutralNF617MomentRowCheck,t.read_denote Q (m+1) hn,
      t.read_denote Q m hp,Bool.and_eq_true]
    exact ⟨decide_eq_true hg.1,hg.2⟩

theorem NF638Table.to_ref (t : NF638Table) (p : NF591Ball) (Q N : ℕ)
    (hc : t.cache.denote Q=neutralNF617Cache p t.key Q N)
    (hg : t.check Q N=true) :
    neutralNF617NonzeroTableCheck p (t.keyTable Q).key Q N
      (t.keyTable Q).rows=true := by
  simp only [NF638Table.check,Bool.and_eq_true] at hg
  have hp : 0<Q ∧ 0<N ∧ |t.key.h|≤1 ∧ 0<t.key.lower ∧
    0<t.rows.size ∧ t.key.lower=(t.d:ℚ)/t.e := of_decide_eq_true hg.1
  have hsize : (t.keyTable Q).rows.size=t.rows.size := by
    simp [NF638Table.keyTable]
  unfold neutralNF617NonzeroTableCheck
  change (decide (0<Q ∧ 0<N ∧ |t.key.h|≤1 ∧ 0<t.key.lower ∧
      0<(t.keyTable Q).rows.size) &&
    (List.range (t.keyTable Q).rows.size).all
      (neutralNF617MomentRowCheck (neutralNF617Cache p t.key Q N)
        t.key.lower Q (t.keyTable Q).rows))=true
  simp only [Bool.and_eq_true,hsize]
  refine ⟨decide_eq_true ⟨hp.1,hp.2.1,hp.2.2.1,hp.2.2.2.1,hp.2.2.2.2.1⟩,?_⟩
  apply List.all_eq_true.mpr
  intro n hn
  rw [← hc]
  exact t.row_to_ref Q n hp.1 (List.mem_range.mp hn) hp.2.2.2.2.2
    ((List.all_eq_true.mp hg.2) n hn)

theorem NF638Table.to_original (t : NF638Table) (p : NF591Ball)
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hc : t.cache.denote neutralNF616Q=
      neutralNF621Cache p t.key neutralNF616Q neutralNF616ExpN)
    (hg : t.check neutralNF616Q neutralNF616ExpN=true) :
    neutralNF628FastKeyCheck
      (neutralNF592PiBall neutralNF616Q neutralNF616AtanN)
      (t.keyTable neutralNF616Q)=true := by
  unfold neutralNF628FastKeyCheck
  rw [hpi,neutralNF621FastTableCheck_eq]
  exact t.to_ref p _ _ (hc.trans (neutralNF621Cache_eq _ _ _ _)) hg

def neutralNF638Chunk (ts : List NF638Table) : Array NF624KeyTable :=
  (ts.map (fun t => t.keyTable neutralNF616Q)).toArray

theorem neutralNF638Chunk_of_checks (ts : List NF638Table) (p : NF591Ball)
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hc : ∀ t ∈ ts, t.cache.denote neutralNF616Q=
      neutralNF621Cache p t.key neutralNF616Q neutralNF616ExpN)
    (hg : ts.all (fun t => t.check neutralNF616Q neutralNF616ExpN)=true) :
    neutralNF628ChunkCheck (neutralNF638Chunk ts)=true := by
  unfold neutralNF628ChunkCheck neutralNF638Chunk
  simp only [List.toList_toArray]
  apply List.all_eq_true.mpr
  intro u hu
  obtain ⟨t,ht,rfl⟩ := List.mem_map.mp hu
  exact t.to_original p hpi (hc t ht) ((List.all_eq_true.mp hg) t ht)

end WeilDefect
