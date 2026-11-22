#!/usr/bin/env python3
"""CP-C1(B) original v4.34 source-only / genuine Lean receipt gate.

preflight / selftest = NOT LEAN. verify requires real compiled .olean and
eight genuine multiline print-axioms reports with standard-only trust.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

SRC=Path('WeilDefect/Arithmetic/CP_C1B_OriginalNineProbeSource.lean')
OBJ=Path('.lake/build/lib/lean/WeilDefect/Arithmetic/CP_C1B_OriginalNineProbeSource.olean')
LOG=Path('cpc1b-original-kernel-axioms.log')
OUT=Path('cpc1b-original-kernel-receipt.json')
IV009=Path('WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean')
IV008=Path('WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean')
BLOBS={
    IV009:'fa794132d438d095436879c4f78d9340ea29be02',
    IV008:'0a7b6cc16670160c6f4b338a36c6d51ae730dde7',
}
UPSTREAM=[
    'neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal',
    'neutralIV008OriginalMixedEntry_hermitian',
]
NEW=[
    'neutralCPC1BOriginal_exactTwoProbe',
    'neutralCPC1BOriginal_hermitian',
    'neutralCPC1BOriginal_diagonal_im_zero',
    'neutralCPC1BOriginal_phaseResponse',
    'neutralCPC1BOriginal_re_from_three_probes',
    'neutralCPC1BOriginal_im_from_three_probes',
]
NAMES=UPSTREAM+NEW
ALLOWED={'propext','Classical.choice','Quot.sound'}
REPORT=re.compile(
    r"'WeilDefect\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|(does not depend on any axioms))",
    re.S,
)

def blob(p):
    data=p.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def preflight():
    s=SRC.read_text()
    assert re.findall(r'(?m)^theorem (neutralCPC1BOriginal_\w+)\b',s)==NEW
    assert re.findall(r'(?m)^#print axioms (\w+)\s*$',s)==NAMES
    for marker in (
        'import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization',
        'Zeta23.EF.literatureRHS',
        'neutralWindowCorrelation',
        'neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal',
        'neutralIV008OriginalMixedEntry_hermitian',
        'f + Complex.I • g',
        'neutralCPC1BOriginal_im_from_three_probes',
    ):
        assert marker in s,marker
    assert not re.search(r'(?m)^\s*(?:axiom|opaque|constant|unsafe)\b',s)
    assert not re.search(r'\b(?:sorry|admit|native_decide|sorryAx)\b',s)
    assert 'import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportExtension' not in s
    for p,expected in BLOBS.items():
        assert blob(p)==expected,('genuine original source drift',str(p),blob(p))
    assert Path('lean-toolchain').read_text().strip()=='leanprover/lean4:v4.34.0'
    assert Path('lakefile.toml').is_file()
    print('CP-C1(B) six source declarations + eight axiom requests + two frozen IV blobs: PASS NOT LEAN')

def parse_reports(raw):
    assert not re.search(r'error:|##\[error\]|sorryAx|unsolved goals',raw,re.I)
    rows=REPORT.findall(raw)
    assert len(rows)==len(NAMES),('wrong print count',len(rows),len(NAMES))
    found={}
    for name,inside,none in rows:
        assert name in NAMES and name not in found,('unexpected/duplicate declaration',name)
        assert bool(inside)!=bool(none),('malformed axiom declaration',name)
        vals=[] if none else [v.strip() for v in inside.split(',') if v.strip()]
        assert len(vals)==len(set(vals))
        assert set(vals)<=ALLOWED,('nonstandard Lean axioms',name,vals)
        found[name]=vals
    assert set(found)==set(NAMES),('missing names',sorted(set(NAMES)-set(found)))
    return found

def selftest():
    prefix="info: CP_C1B.lean:2:0: "
    lines=[
        prefix+"'WeilDefect."+n+"' depends on axioms: [propext,\n  Classical.choice,\n  Quot.sound]\n"
        for n in NAMES
    ]
    raw=''.join(lines)
    assert len(parse_reports(raw))==8
    bad=(
        raw.replace('Quot.sound','sorryAx',1),
        raw.replace('Quot.sound','other.axiom',1),
        raw+lines[0],
        raw.replace("'WeilDefect."+NAMES[0]+"'","'WeilDefect.unknown'",1),
        raw.replace("'WeilDefect."+NAMES[0]+"'","'WeilDefect."+NAMES[1]+"'",1),
        raw.replace(' depends on axioms:',' error: depends on axioms:',1),
    )
    for b in bad:
        try: parse_reports(b)
        except AssertionError: pass
        else: raise AssertionError('invalid fake axiom transcript accepted')
    print('CP-C1(B) true multiline axiom parser plus six negative controls PASS NOT LEAN')

def verify():
    preflight()
    assert OBJ.is_file() and OBJ.stat().st_size>0,'compiled .olean missing'
    assert LOG.is_file() and LOG.stat().st_size>0,'genuine Lean stdout missing'
    found=parse_reports(LOG.read_text())
    receipt={
        'schema':'CP-C1B-original-Weil-nine-probe-Lean4.34-v1',
        'status':'GENUINE KERNEL + AXIOM PASS',
        'original_dependency_git_blobs':{str(k):v for k,v in BLOBS.items()},
        'source_sha256':{str(p):sha256(p) for p in [
            SRC,IV009,IV008,Path('lean-toolchain'),Path('lakefile.toml')]},
        'compiled_olean_sha256':sha256(OBJ),
        'genuine_standard_axioms':found,
        'original_three_bump_Schwartz_instances':False,
        'independent_spectral_dictionary':False,
        'complete_zero_roster':False,
        'support_independent_positivity':False,
        'RH':False,
    }
    OUT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print('CP-C1(B) 6/6 REAL ORIGINAL WEIL KERNEL + 2 UPSTREAM AXIOM AUDITS PASS')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=('preflight','selftest','verify'))
    mode=p.parse_args().mode
    {'preflight':preflight,'selftest':selftest,'verify':verify}[mode]()
