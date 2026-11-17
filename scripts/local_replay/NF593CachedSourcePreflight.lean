import WeilDefect.Arithmetic.ActualZetaOriginalCachedSourceJets

/- NF593 independent executable preflight, not a theorem.
   Print every exact integer interval endpoint for comparison with
   the separately generated NF591 receipt. Fail closed on any
   non-integral scaled endpoint or failed ceiling. -/
open WeilDefect

def main : IO Unit := do
  let table := neutralNF593OriginalTable
  unless table.size == 400 do
    throw (IO.userError "NF593 source table size mismatch")
  unless neutralNF593CheckTable table 400 do
    throw (IO.userError "NF593 original ceiling check failed")
  for n in List.range 400 do
    let b := neutralNF593ReadBall table n
    let lo : ℚ := (b.mid-b.rad)*(neutralNF592Q:ℚ)
    let hi : ℚ := (b.mid+b.rad)*(neutralNF592Q:ℚ)
    let l : ℤ := ⌊lo⌋
    let h : ℤ := ⌊hi⌋
    unless (l:ℚ) == lo && (h:ℚ) == hi do
      throw (IO.userError s!"NF593 nonintegral receipt endpoint at {n}")
    IO.println s!"NF593_ROW {n} {l} {h}"
  IO.println "NF593_LEAN_EXECUTABLE_PASS"
