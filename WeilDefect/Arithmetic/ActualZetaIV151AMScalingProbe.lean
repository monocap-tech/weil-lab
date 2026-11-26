import WeilDefect.Arithmetic.ActualZetaIV146AMCellData

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- Eight contiguous rows near the least-slack row; independent of block 0. -/
theorem neutralIV151EightRows :
    (List.range 8).all (fun j => neutralIV146RowOK (6568+j)) = true := by decide

#print axioms neutralIV151EightRows
end WeilDefect
