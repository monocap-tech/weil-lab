#!/usr/bin/env python3
"""Extract the FCT-02 generic candidate from a local Weil-Lab git object store.
No network, repository writes, workflow activation, or compiler acceptance implied.
Usage: python fct02_extract.py /path/to/weil-lab --output FCT02Generic.lean
"""
import argparse, hashlib, json, pathlib, re, subprocess
REV='6c6f6e43c3e64ea474e8aa5c9a43a378b00c39bf'
SOURCES=[
('CoercivityLemmas','b96b88cc7a0790c8a840ecc51ad57e6fff983eae'),
('CongruenceInterval','de37c001b9951d67f7336b5669ed668eff83d0f3'),
('DiagonalDominance','dd79ca33cc053a96810966325d4457c0d42a5d89'),
('DominanceTransfer','7064189b187d53e11c9bb73bc2313eabd7939847'),
('CoercivityClosure','9796960dd019e11c4091fa9d0ecbdd5a19654086'),
('RealIntervalTransport','e9bc2f05b80611139223cf1e70ad3a6404c70a67'),
('IntegerRealScale','0b6a558b9fe970a735ad494ae52acd3ea71d91a7'),
('TransformedDominance','e8c84c23da4949b9a48868fc7f864b192908fcd4'),
('PreconditionerFrame','b9c2133a6234ffa336e6db77979e1e56b49b2ddb')]
EXCLUDED=set('neutralNF661Source neutralNF661PhysicalH neutralNF661PhysicalH_symm neutralNF662OriginalPhysicalLower_to_full neutralNF662OriginalPhysicalCongruence_enclosed neutralNF664ActualPhysicalB neutralNF664ActualPhysicalB_symm neutralNF664PhysicalTransformed_coercivity'.split())
DECL=re.compile(r'^(?:theorem|def) (neutralNF\w+)\b',re.M)
END=re.compile(r'^#print axioms|^end(?:\s|$)',re.M)
REF=re.compile(r'neutralNF\w+')

def blobsha(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def extract(s):
    # The pinned modules use non-nested block comments; remove only comments.
    s=re.sub(r'/-[\s\S]*?-/', '', s)
    ms=list(DECL.finditer(s))
    return [(m[1],END.split(s[m.start():ms[i+1].start() if i+1<len(ms) else len(s)],maxsplit=1)[0].strip()) for i,m in enumerate(ms)]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('repo',type=pathlib.Path)
    p.add_argument('--output',type=pathlib.Path,default=pathlib.Path('FCT02Generic.lean'))
    a=p.parse_args()
    decls=[]; excluded=set(); manifest=[]
    for suffix,expected in SOURCES:
        path=f'WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGram{suffix}.lean'
        b=subprocess.check_output(['git','-C',str(a.repo),'show',f'{REV}:{path}'])
        actual=blobsha(b)
        if actual!=expected: raise ValueError(f'blob mismatch: {path}: {actual} != {expected}')
        kept=[]
        for name,body in extract(b.decode('utf-8')):
            if name in EXCLUDED: excluded.add(name); continue
            decls.append((name,body)); kept.append(name)
        manifest.append(dict(path=path,git_blob=actual,retained=kept))
    if excluded!=EXCLUDED or len(decls)!=34 or len({n for n,_ in decls})!=34:
        raise ValueError('unexpected declaration set')
    if sum(len(body.splitlines()) for _,body in decls)!=612:
        raise ValueError('unexpected body line count')
    seen=set()
    for name,body in decls:
        missing=set(REF.findall(body))-{name}-seen
        if missing: raise ValueError(f'{name}: unresolved or forward reference: {missing}')
        seen.add(name)
    source='import Mathlib\n\nnamespace WeilDefect\n\nnoncomputable section\nopen Finset\n\n'+ '\n\n'.join(b for _,b in decls)+'\n\n'+'\n'.join('#print axioms '+n for n,_ in decls)+'\n\nend\nend WeilDefect\n'
    # This is an isolated candidate, not a module to import alongside legacy definitions.
    a.output.write_bytes(source.encode('utf-8'))
    receipt=dict(revision=REV,sources=manifest,excluded=sorted(excluded),declarations=34,body_lines=612,unresolved_project_references=0,forward_project_references=0,output_sha256=hashlib.sha256(source.encode()).hexdigest(),classification='static extraction; compiler and axiom audit not executed')
    a.output.with_suffix('.manifest.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__': main()
