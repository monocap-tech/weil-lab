import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalCoverageGate

namespace WeilDefect

/-! NF624: sorted table search proposes an index. Its correctness
does NOT become an unverified premise: exact lookup and coverage
gates still check every requested key and degree. A search failure
returns bank.size, which the lookup gate rejects. -/

def neutralNF624KeyLT (a b : NF616Frequency) : Bool :=
  decide (a.h < b.h ∨ (a.h = b.h ∧ a.f < b.f))

def neutralNF624Search (bank : Array NF624KeyTable) (k : NF616Frequency) :
    ℕ → ℕ → ℕ → ℕ
  | 0, _, _ => bank.size
  | fuel+1, lo, hi =>
    if lo < hi then
      let m := (lo+hi)/2
      let t := neutralNF624BankRead bank m
      if t.key=k then m
      else if neutralNF624KeyLT t.key k then
        neutralNF624Search bank k fuel (m+1) hi
      else neutralNF624Search bank k fuel lo m
    else bank.size

def neutralNF624Index (bank : Array NF624KeyTable) (k : NF616Frequency) : ℕ :=
  neutralNF624Search bank k 16 0 bank.size

theorem neutralNF624Index_coverage (bank : Array NF624KeyTable)
    (hc : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true) :
    neutralNF624Coverage bank (neutralNF624Index bank) :=
  neutralNF624CoverageCheck_sound bank _ hc

end WeilDefect
