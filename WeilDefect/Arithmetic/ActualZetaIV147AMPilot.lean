import WeilDefect.Arithmetic.ActualZetaIV146AMCellData

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem neutralIV147Data_size : neutralIV146HChunks.size = 128 := by decide
theorem neutralIV147Shifts_size : neutralIV146Shifts.length = 48 := by decide
theorem neutralIV147Pilot_row : neutralIV146RowOK 6572 = true := by decide
theorem neutralIV147Pilot_block : neutralIV146BlockOK 0 = true := by decide

#print axioms neutralIV147Data_size
#print axioms neutralIV147Shifts_size
#print axioms neutralIV147Pilot_row
#print axioms neutralIV147Pilot_block
end WeilDefect
