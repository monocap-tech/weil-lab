import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentBank
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFastMomentTable

namespace WeilDefect

/-! NF628: kernel checks are local to a literal chunk. Joining
chunks is an exact structural operation, not a fresh numerical
verification of the whole bank. -/

def neutralNF628FastKeyCheck (p : NF591Ball) (t : NF624KeyTable) : Bool :=
  neutralNF621FastTableCheck p t.key neutralNF616Q neutralNF616ExpN t.rows

def neutralNF628ChunkCheck (chunk : Array NF624KeyTable) : Bool :=
  let p := neutralNF592PiBall neutralNF616Q neutralNF616AtanN
  chunk.toList.all (neutralNF628FastKeyCheck p)

def neutralNF628Join (chunks : List (Array NF624KeyTable)) : Array NF624KeyTable :=
  (chunks.flatMap Array.toList).toArray

theorem neutralNF628Bank_of_chunks (chunks : List (Array NF624KeyTable))
    (hc : chunks.all neutralNF628ChunkCheck = true) :
    neutralNF624BankCheck (neutralNF628Join chunks) = true := by
  let bank := neutralNF628Join chunks
  change neutralNF624BankCheck bank = true
  unfold neutralNF624BankCheck
  apply List.all_eq_true.mpr
  intro i hi
  have hi' : i < bank.size := List.mem_range.mp hi
  have hli : i < bank.toList.length := by simpa using hi'
  have hm : neutralNF624BankRead bank i ∈ bank.toList := by
    have hget : bank.toList[i] ∈ bank.toList := List.getElem_mem hli
    simpa [neutralNF624BankRead,hi'] using hget
  have hm' : neutralNF624BankRead bank i ∈ chunks.flatMap Array.toList := by
    simpa [bank,neutralNF628Join] using hm
  obtain ⟨chunk,hchunk,ht⟩ := List.mem_flatMap.mp hm'
  have hgood := (List.all_eq_true.mp hc) chunk hchunk
  unfold neutralNF628ChunkCheck at hgood
  have hkey := (List.all_eq_true.mp hgood) _ ht
  unfold neutralNF628FastKeyCheck at hkey
  rw [neutralNF621FastTableCheck_eq] at hkey
  exact hkey

end WeilDefect
