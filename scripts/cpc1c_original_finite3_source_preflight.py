#!/usr/bin/env python3
"""CP-C1(C) cheap original-source Fin3 check; NOT a Lean proof."""
import hashlib
import re
from pathlib import Path
SRC=Path("WeilDefect/Arithmetic/CP_C1C_OriginalCompleteDivisorFinite3.lean")
IV008=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean")
IV009=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean")
NEW=[
 "neutralCPC1C_originalFiniteThree_matrix_eq_divisor",
 "neutralCPC1C_originalFiniteThree_diagonal_eq_divisorEnergy",
 "neutralCPC1C_originalFiniteThree_divisorHermitian",
]
UPSTREAM=[
 "neutralIV008OriginalMixedEntry_eq_divisor",
 "neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal",
]
def blob(p):
 b=p.read_bytes()
 return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def main():
 s=SRC.read_text()
 assert blob(IV008)=="0a7b6cc16670160c6f4b338a36c6d51ae730dde7"
 assert blob(IV009)=="fa794132d438d095436879c4f78d9340ea29be02"
 assert re.findall(r'(?m)^theorem (neutralCPC1C_originalFiniteThree_\w+)\b',s)==NEW
 assert re.findall(r'(?m)^#print axioms (\w+)\s*$',s)==UPSTREAM+NEW
 assert s.rstrip().endswith("end\nend WeilDefect")
 assert s.startswith("import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization\n")
 for needle in [
 "neutralIV008OriginalMixedEntry_eq_divisor a s hs i j",
 "neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal",
 "neutralIV008OriginalDivisorEntry_hermitian",
 ]: assert needle in s,needle
 assert not re.search(r'(?m)^\s*(axiom|opaque|constant|unsafe)\b',s)
 assert not re.search(r'\b(?:sorry|admit|native_decide|sorryAx)\b',s)
 assert "import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportExtension" not in s
 print("CP-C1(C): 3 candidate declarations, 5 axiom prints, 2 source blobs PASS. NOT LEAN")
if __name__=="__main__": main()
