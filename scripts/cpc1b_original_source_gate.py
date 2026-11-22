#!/usr/bin/env python3
"""CP-C1(B) cheap fail-closed original IV009 source/interface audit, NOT LEAN.

Run --upstream in the genuine full IV009 checkout. Only a pinned Lean
kernel build + genuine standard-only #print axioms can promote results.
"""
import argparse
import hashlib
from fractions import Fraction as Q
from pathlib import Path
import re

SRC = 'WeilDefect/Arithmetic/CP_C1B_OriginalNineProbeSource.lean'
IV009 = 'WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean'
IV008 = 'WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean'
SHA_IV009 = 'fa794132d438d095436879c4f78d9340ea29be02'
SHA_IV008 = '0a7b6cc16670160c6f4b338a36c6d51ae730dde7'
DECL = (
 'neutralCPC1BOriginal_exactTwoProbe',
 'neutralCPC1BOriginal_hermitian',
 'neutralCPC1BOriginal_diagonal_im_zero',
 'neutralCPC1BOriginal_phaseResponse',
 'neutralCPC1BOriginal_re_from_three_probes',
 'neutralCPC1BOriginal_im_from_three_probes',
)
UPSTREAM = (
 'neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal',
 'neutralIV008OriginalMixedEntry_hermitian',
)

def blob(path):
    data = Path(path).read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def audit_file(path):
    content=Path(path).read_text()
    assert not re.search(r'(?m)^\s*(axiom|opaque|constant)\b',content)
    assert not re.search(r'(?m)\b(sorry|admit|native_decide)\b',content)
    assert re.search(r'^import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization$',content,re.M)
    assert 'import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportExtension' not in content
    assert 'Zeta23.EF.literatureRHS' in content
    assert 'neutralWindowCorrelation' in content
    assert 'neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal' in content
    assert 'neutralIV008OriginalMixedEntry_hermitian' in content
    for name in DECL:
        assert len(re.findall(r'(?m)^theorem '+re.escape(name)+r'\b',content))==1,name
    observed=re.findall(r'(?m)^#print axioms\s+(\S+)\s*$',content)
    assert observed == list(UPSTREAM+DECL),('axiom request drift',observed)
    assert 'f + Complex.I • g' in content
    assert 'neutralCPC1BOriginalMixed a f g).im' in content
    print('CP-C1(B) six original-source candidates, two original anchors, phase orientation: PASS NOT LEAN')

def upstream():
    assert blob(IV009)==SHA_IV009,'Frozen genuine IV009 source drift'
    assert blob(IV008)==SHA_IV008,'Frozen genuine IV008 source drift'
    a=Path(IV009).read_text()
    b=Path(IV008).read_text()
    assert 'theorem neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal' in a
    assert 'theorem neutralIV008OriginalMixedEntry_hermitian' in b
    assert 'Zeta23.EF.literatureRHS' in a
    print('CP-C1(B) frozen original IV009+IV008 source Git blobs: MATCH NOT LEAN')

def algebra_selftest():
    A,D,x,y=Q(3,2),Q(-7,5),Q(5,3),Q(-13,7)
    def response(vre,vim):
        return A+2*(x*vre-y*vim)+D*(vre*vre+vim*vim)
    p=response(Q(1),Q(0))
    s=response(Q(0),Q(1))
    assert (p-A-D)/2==x
    assert -(s-A-D)/2==y
    assert (s-A-D)/2 != y # wrong-sign negative control
    assert response(Q(-1),Q(0))==A-2*x+D
    print('CP-C1(B) rational +1/-1/i phase and wrong-conjugation controls: PASS NOT LEAN')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',default=SRC)
    p.add_argument('--upstream',action='store_true')
    args=p.parse_args()
    audit_file(args.source)
    algebra_selftest()
    if args.upstream:
        upstream()
    print('CP-C1(B) CHEAP PREFLIGHT PASS; NO KERNEL OR SPECTRAL CLAIM')

if __name__=='__main__':
    main()
