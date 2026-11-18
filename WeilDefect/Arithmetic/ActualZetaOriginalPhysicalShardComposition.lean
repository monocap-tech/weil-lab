import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBooleanClosure
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFastMomentTable

namespace WeilDefect

/-! NF625: shard truth can be composed without recomputing every
Taylor series in a monolithic Boolean kernel reduction. Reuse the
accepted reference specification, with the candidate NF621 cache
equality as the only permission to change the evaluator. -/

def neutralNF625FastBankRow (bank : Array NF624KeyTable) (i : ℕ) : Bool :=
  let t := neutralNF624BankRead bank i
  neutralNF621FastTableCheck
    (neutralNF592PiBall neutralNF616Q neutralNF616AtanN)
    t.key neutralNF616Q neutralNF616ExpN t.rows

theorem neutralNF625Bank_of_fast_rows (bank : Array NF624KeyTable)
    (h : ∀ i < bank.size, neutralNF625FastBankRow bank i = true) :
    neutralNF624BankCheck bank = true := by
  unfold neutralNF624BankCheck
  apply List.all_eq_true.mpr
  intro i hi
  have he := h i (List.mem_range.mp hi)
  unfold neutralNF625FastBankRow at he
  rw [neutralNF621FastTableCheck_eq] at he
  exact he

/-- Arbitrarily partition the literal indices into finite pieces.
The partition coverage and each shard's actual checked truth are
explicit obligations, not assumptions about the external manifest. -/
def neutralNF625ShardCheck (bank : Array NF624KeyTable) (ids : List ℕ) : Bool :=
  ids.all (neutralNF625FastBankRow bank)

theorem neutralNF625Bank_of_shards (bank : Array NF624KeyTable)
    (pieces : List (List ℕ))
    (hcover : ∀ i < bank.size, ∃ ids ∈ pieces, i ∈ ids)
    (hchecks : ∀ ids ∈ pieces, neutralNF625ShardCheck bank ids = true) :
    neutralNF624BankCheck bank = true := by
  apply neutralNF625Bank_of_fast_rows
  intro i hi
  obtain ⟨ids,hids,hi'⟩ := hcover i hi
  exact (List.all_eq_true.mp (hchecks ids hids)) i hi'

end WeilDefect
