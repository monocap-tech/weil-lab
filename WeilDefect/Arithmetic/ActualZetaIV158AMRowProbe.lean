import WeilDefect.Arithmetic.ActualZetaIV146AMCellData

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- Two separate eight-row declarations in one process, to measure
whether kernel memory accumulates between independent declarations. -/
theorem neutralIV158ProbeA :
    (List.range 8).all (fun j => neutralIV146RowOK (64+j)) = true := by decide

theorem neutralIV158ProbeB :
    (List.range 8).all (fun j => neutralIV146RowOK (72+j)) = true := by decide

#print axioms neutralIV158ProbeA
#print axioms neutralIV158ProbeB
end WeilDefect
