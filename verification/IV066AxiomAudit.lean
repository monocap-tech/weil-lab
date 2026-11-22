/-!
IV066 direct source axiom audit. Run only after IV066OriginalSourcePilot compiles.
The output must be independently checked; #print axioms alone is not a receipt.
-/
import WeilDefect.Arithmetic.IV066OriginalSourcePilot

#print axioms WeilDefect.iv066_sourceCorrelation_orientation
#print axioms WeilDefect.iv066_original_general_source_summable
#print axioms WeilDefect.iv066_original_general_source_signed
#print axioms WeilDefect.iv066_original_mixed_weilTest_signed
#print axioms WeilDefect.iv066_gamma_literal_native
#print axioms WeilDefect.iv066_native_signed_multiplier