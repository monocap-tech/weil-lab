#!/usr/bin/env python3
"""CP-C1(D) original nine-real-probe source preflight (NOT LEAN)."""
import hashlib
import re
from pathlib import Path
HERE=Path('WeilDefect/Arithmetic')
SRC=HERE/'CP_C1D_OriginalNineProbeCompatibility.lean'
ORIGINAL={
 HERE/'ActualZetaPhaseIVOriginalMixedHermitian.lean':'0a7b6cc16670160c6f4b338a36c6d51ae730dde7',
 HERE/'ActualZetaPhaseIVOriginalSchwartzPolarization.lean':'fa794132d438d095436879c4f78d9340ea29be02',
}
NAMES=[
 'neutralCPC1D_original_re_from_physicalProbes',
 'neutralCPC1D_original_im_from_physicalProbes',
 'neutralCPC1D_divisor_re_from_physicalProbes',
 'neutralCPC1D_divisor_im_from_physicalProbes',
 'neutralCPC1D_original_eq_target_of_nine_phase_readings',
]
PRINTS=[
 'neutralIV008OriginalMixedEntry_eq_divisor',
 'neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal',
]+NAMES
def blob(p):
    b=p.read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def main():
    s=SRC.read_text()
    for p,expected in ORIGINAL.items():
        actual=blob(p)
        assert actual==expected,(p,actual,expected)
    assert re.findall(r'(?m)^theorem (neutralCPC1D_\w+)\b',s)==NAMES
    assert re.findall(r'(?m)^#print axioms (\w+)\s*$',s)==PRINTS
    assert s.startswith('import WeilDefect.Arithmetic.CP_C1B_OriginalNineProbeSource\n')
    assert 'import WeilDefect.Arithmetic.CP_C1C_OriginalCompleteDivisorFinite3\n' in s
    for marker in [
      'neutralCPC1BOriginal_re_from_three_probes',
      'neutralCPC1BOriginal_im_from_three_probes',
      'neutralIV008OriginalMixedEntry_eq_divisor',
      'neutralIV008OriginalMixedEntry_hermitian',
      'neutralIV008OriginalMixedDiagonal_im_zero',
      '(hPhase i j hij).symm',
      'hOriginalHerm j i',
      'conj (T i j) = T j i',
      'i < j →',
    ]: assert marker in s,marker
    assert s.rstrip().endswith('end\nend WeilDefect')
    assert not re.search(r'(?m)^\s*(axiom|opaque|constant|unsafe)\b',s)
    assert not re.search(r'\b(?:sorry|admit|native_decide|sorryAx)\b',s)
    print('CP-C1(D) five original-source theorem candidates, 7 source+new axiom requests, 2 immutable IV source blobs: PASS (NOT LEAN)')
if __name__=='__main__': main()
