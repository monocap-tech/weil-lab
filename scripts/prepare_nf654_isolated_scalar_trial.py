#!/usr/bin/env python3
"""Validate NF639 literal proposals and every selected fee against frozen source.
Only rewrite the import in Params.lean; all 242 row modules remain byte-identical.
"""
import argparse,hashlib,json,re,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
def sha(b): return hashlib.sha256(b).hexdigest()
def rat(x): return F(*map(int,x))
def dyad(x):
    n,e=map(int,x)
    return F(n*2**e) if e>=0 else F(n,2**(-e))
def main():
    p=argparse.ArgumentParser()
    for k in ('root','proposals','payments','output'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    manifest=a.proposals/'manifest.json'
    assert sha(manifest.read_bytes())=='efcb46ca6eabeae80d0beb21f8627773d23b71002c26fed82f68f47e56bbf896'
    m=json.loads(manifest.read_text())
    assert m['rows']==242 and m['external_scalar_replay']=='PASS'
    names={'Params.lean'}|{f'Row{i:03d}.lean' for i in range(242)}
    assert {x['file'] for x in m['files']}==names and len(m['files'])==243
    for x in m['files']:
        assert sha((a.proposals/x['file']).read_bytes())==x['sha256']
    raw=a.payments.read_bytes(); pay=json.loads(raw)
    assert sha(raw)==m['payment_sha256'] and pay['entry_sha256']==m['entry_sha256']
    frozen=(a.root/'notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json').read_bytes()
    assert sha(frozen)==pay['frozen_sha256']=='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
    box=[(dyad(x),abs(dyad(y))) for x,y in json.loads(frozen)['original_exact_native_raw_selected_coefficients_mid_radius']]
    assert len(box)==len(pay['rows'])==242
    dig=sha(''.join(f'{x.numerator}/{x.denominator}|{y.numerator}/{y.denominator}\n' for x,y in box).encode())
    assert dig=='c7bd38119d51b2480f7d9fbb2977f11c8a0cfe9d844069722a785bcbeaf91f62'
    params=(a.proposals/'Params.lean').read_text()
    ns={k:int(v) for k,v in re.findall(r'def nf639([SQTU]) : ℕ := (\d+)',params)}
    S,Q,T,U=[ns[k] for k in 'SQTU']
    assert min(S,Q,T,U)>0 and Q==10**2600
    v={k:F(int(n),int(d)) for k,n,d in re.findall(r'def nf639(EH|EV|R) : ℚ := \((-?\d+):ℚ\)/(\d+)',params)}
    eh,ev,r=[v[k] for k in ('EH','EV','R')]
    assert (eh,ev,r)==tuple(rat(pay[k]) for k in ('uniform_H_radius','uniform_V_radius','r'))
    assert min(eh,ev,r)>=0
    ratios=[]
    for i,(rec,(mid,rad)) in enumerate(zip(pay['rows'],box)):
        assert rec['i']==i and rec['pass']
        row=(a.proposals/f'Row{i:03d}.lean').read_text()
        vs=list(map(int,re.findall(r'\((-?\d+):ℤ\)',row))); assert len(vs)==9
        de,co,to,wm,ym,ma,b,ay,dy=vs
        assert min(de,co,to,wm,ym,ma)>=0
        defect=F(de,Q*S*S)+F(co*to,S*S)*eh
        residual=abs(F(b,Q*S*T)-F(ay,Q*S*S*U))+F(co*wm,S*T)*ev+F(co*ym,S*S*U)*eh
        selected=abs(F(dy,S*U)-mid)+F(ma,S)*2*r
        assert defect==rat(rec['defect_upper'])<=F(1,100)
        assert residual==rat(rec['residual_upper'])<=r
        assert selected==rat(rec['selected_payment']) and rad==rat(rec['selected_radius']) and 0<=selected<rad
        ratios.append(selected/rad)
    assert max(range(242),key=lambda i:ratios[i])==87
    a.output.mkdir(parents=True,exist_ok=True)
    old=b'import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentReceipts\n'
    new=b'import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentCore\n'
    for x in m['files']:
        n=x['file']; data=(a.proposals/n).read_bytes()
        if n=='Params.lean':
            # The only permitted source normalization is this import.
            # Both historical and already-isolated retained Params forms
            # are accepted only after all original file hashes are verified.
            assert data.count(old)+data.count(new)==1
            if old in data:
                data=data.replace(old,new)
            assert data.count(new)==1
        else: assert sha(data)==x['sha256']
        (a.output/n).write_bytes(data)
    report={'schema':'NF654-literal-scalar-trial-preflight-v1','proposal_manifest_sha256':sha(manifest.read_bytes()),'frozen_normalized_box_sha256':dig,'all_scalar_fees_replayed':242,'strict_selected_rows':242,'worst_selected_row':87,'max_ratio':str(max(ratios)),'unchanged_row_bytes':242,'scope':'external arithmetic; kernel proof pending'}
    (a.output/'nf654-preflight.json').write_text(json.dumps(report,indent=2)+'\n')
    print('NF654 all 726 fees exactly replayed against actual source and receipts; 242 unchanged scalar modules',flush=True)
if __name__=='__main__':main()
