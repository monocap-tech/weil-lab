#!/usr/bin/env python3
"""Emit literal scaled proposals from original historical and payment receipts.

Pilot uses the actual Arb-baseline r and checks only two selected-box
rows. Full requires moment-derived entries AND their exact cache and
payment receipts. Neither path asserts analytic enclosure custody.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_nf623_uniform_physical_payments import (
    Q, N, TNUM, FROZEN_SHA, dyad, common_dyads, read_jsonl
)
sys.set_int_max_str_digits(0)
MODULE='WeilDefect.Generated.NF630'
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSelectedRowReceipt'
ROW='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRowClosure'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def rat(x):
    return F(int(x[0]),int(x[1]))

def qlit(x):
    return f'({x.numerator}:ℚ)/{x.denominator}'

def array(xs):
    return '#['+',\n  '.join(f'({int(x)}:ℤ)' for x in xs)+']'

def filetext(imports,body):
    return ''.join('import '+s+'\n' for s in imports)+'\nnamespace WeilDefect\n\n'+body+'\n\nend WeilDefect\n'

def historical(root,path):
    from verify_nf380_original_archived_signed_dual import FRAME_SHA
    f=root/'notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json'
    assert sha(f)==FROZEN_SHA
    frozen=json.loads(f.read_text())
    hd,*rs=read_jsonl(path)
    assert hd['schema']=='NF613-original-physical-entry-balls-v1'
    assert hd['frame_sha256']==FRAME_SHA and hd['frozen_sha256']==FROZEN_SHA
    assert [r['row'] for r in rs]==list(range(N))
    dig=hashlib.sha256()
    for r in rs:
        assert len(r['D'])==N
        for d in r['D']:
            dig.update((json.dumps(d,separators=(',',':'))+'\n').encode())
    assert dig.hexdigest()==FRAME_SHA
    flat,S=common_dyads([dyad(d) for r in rs for d in r['D']])
    D=[flat[i*N:(i+1)*N] for i in range(N)]
    y,U=common_dyads([dyad(v) for v in hd['y0']])
    crit=frozen['original_exact_native_original_four_critical_coefficients_mid_radius']
    assert len(crit)==4 and all(dyad(r)==0 for _,r in crit)
    w,T=common_dyads([F(t,2**20)-dyad(m) for t,(m,_) in zip(TNUM,crit)])
    mid,rad=zip(*[tuple(map(dyad,r)) for r in
        frozen['original_exact_native_raw_selected_coefficients_mid_radius']])
    assert len(y)==len(mid)==N and all(x>=0 for x in rad)
    return D,S,y,U,w,T,mid,rad,FRAME_SHA

def payment_receipt(path,entry_hash,frame_hash):
    p=json.loads(path.read_text())
    assert p['schema']=='NF623-uniform-physical-payments-v1'
    assert p['entry_sha256']==entry_hash and p['frame_sha256']==frame_hash
    assert p['frozen_sha256']==FROZEN_SHA and p['all_pass']
    assert p['row_defect_pass'] and p['selected_payments_pass']==N
    assert [x['i'] for x in p['rows']]==list(range(N))
    return p

def emit_pilot(out,D,S,y,U,mid,rad,p):
    r=rat(p['r'])
    body=f'def nf630PilotY : Array ℤ := {array(y)}\n\n'
    body+=f'def nf630PilotS : ℕ := {S}\ndef nf630PilotU : ℕ := {U}\n'
    body+=f'def nf630PilotR : ℚ := {qlit(r)}\n\n'
    body+='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
    for i in (0,N-1):
        d=D[i]
        dy=sum(a*b for a,b in zip(d,y))
        mass=sum(map(abs,d))
        payment=abs(F(dy,S*U)-mid[i])+F(mass,S)*2*r
        assert payment==rat(p['rows'][i]['selected_payment'])
        assert rad[i]==rat(p['rows'][i]['selected_radius']) and payment<=rad[i]
        name=f'nf630PilotD{i}'
        body+=f'def {name} : Array ℤ := {array(d)}\n\n'
        args=f'(fun j : Fin 242 => {name}[j.val]!) (fun j : Fin 242 => nf630PilotY[j.val]!) nf630PilotS nf630PilotU nf630PilotR {i} ({dy}:ℤ) ({mass}:ℤ)'
        body+=f'theorem nf630PilotGate{i} :\n    neutralNF630SelectedRowCheck {args} = true := by\n  decide +kernel\n\n'
        body+=f'#print axioms nf630PilotGate{i}\n\n'
    (out/'Pilot.lean').write_text(filetext([BASE],body))

def emit_full(out,D,S,y,U,w,T,mid,rad,entries,cache,p,entry_hash,historical_hash,frame_hash):
    h,*er=read_jsonl(entries)
    assert h['schema']=='NF622-original-physical-entry-balls-v1' and h['scale']=='10^2600'
    assert [r['row'] for r in er]==list(range(N))
    H=[[0]*N for _ in range(N)]
    V=[]; EH=EV=0
    for i,row in enumerate(er):
        assert len(row['H_lower'])==i+1 and len(row['V'])==4
        for j,(m,e) in enumerate(row['H_lower']):
            m,e=int(m),int(e); assert e>=0
            H[i][j]=H[j][i]=m; EH=max(EH,e)
        vv=[tuple(map(int,v)) for v in row['V']]
        assert all(e>=0 for _,e in vv)
        V.append([m for m,_ in vv]); EV=max(EV,max(e for _,e in vv))
    ch,*cr=read_jsonl(cache)
    assert ch['schema']=='NF626-integer-center-cache-v1'
    assert ch['entry_sha256']==entry_hash and ch['historical_sha256']==historical_hash
    assert ch['frame_sha256']==frame_hash and ch['frozen_sha256']==FROZEN_SHA
    assert {k:int(v) for k,v in ch['scales'].items()}==dict(S=S,Q=Q,T=T,U=U)
    assert list(map(int,ch['y']))==y and list(map(int,ch['w']))==w
    assert rat(ch['eH'])==rat(p['uniform_H_radius'])==F(EH,Q)
    assert rat(ch['eV'])==rat(p['uniform_V_radius'])==F(EV,Q)
    assert rat(ch['r'])==rat(p['r'])
    assert [r['i'] for r in cr]==list(range(N))
    matrices=dict(D=D,H=H,V=V,HD=[list(map(int,x['HD'])) for x in cr],
                  A=[list(map(int,x['A'])) for x in cr])
    for name,rows in matrices.items():
        assert len(rows)==N and all(len(x)==(4 if name=='V' else N) for x in rows)
    imports=[]
    for start in range(0,N,4):
        name=f'Rows{start:03d}'
        imports.append(MODULE+'.'+name)
        body=''
        for k,rows in matrices.items():
            for i in range(start,min(start+4,N)):
                body+=f'def nf630{k}{i:03d} : Array ℤ := {array(rows[i])}\n\n'
        (out/(name+'.lean')).write_text(filetext(['Mathlib'],body))
    body=''
    for k in matrices:
        body+=f'def nf630{k} : Array (Array ℤ) := #['+', '.join(f'nf630{k}{i:03d}' for i in range(N))+']\n\n'
    vs=dict(y=y,w=w,**{k:[int(row[k]) for row in cr] for k in ('Vw','b','Ay','Dy')})
    for k,xs in vs.items():
        body+=f'def nf630{k} : Array ℤ := {array(xs)}\n\n'
    body+='def nf630Inputs : NF626ScaledInputs :=\n  ⟨'+',\n   '.join(
        [f'fun i j => (nf630{k}[i.val]!)[j.val]!' for k in ('D','H','V')]+
        ['fun i => nf630y[i.val]!','fun i => nf630w[i.val]!',str(S),str(Q),str(U),str(T),
         qlit(F(EH,Q)),qlit(F(EV,Q)),qlit(rat(p['r']))])+'⟩\n\n'
    body+='def nf630Cache : NF626CenterCache :=\n  ⟨'+',\n   '.join(
        [f'fun i j => (nf630{k}[i.val]!)[j.val]!' for k in ('HD','A')]+
        [f'fun i => nf630{k}[i.val]!' for k in ('Vw','b','Ay','Dy')])+'⟩\n'
    (out/'Data.lean').write_text(filetext([ROW,*imports],body))
    # First actual row only for bounded kernel feasibility. The remaining
    # rows are available as literal data, not certified.
    body='''set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem nf630WGate : nf630Inputs.wCheck = true := by
  decide +kernel

theorem nf630ParamGate : neutralNF629Parameters nf630Inputs = true := by
  decide +kernel

theorem nf630CacheRow0 : neutralNF629CacheRow nf630Cache nf630Inputs 0 = true := by
  decide +kernel

theorem nf630PayRow0 : nf630Cache.fastPayGate nf630Inputs 0 = true := by
  decide +kernel

#print axioms nf630CacheRow0
#print axioms nf630PayRow0'''
    (out/'RowTrial.lean').write_text(filetext([MODULE+'.Data'],body))

def main():
    ap=argparse.ArgumentParser()
    for k in ('root','historical','payments','output'):
        ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--entries',type=Path)
    ap.add_argument('--cache',type=Path)
    a=ap.parse_args()
    assert bool(a.entries)==bool(a.cache)
    a.output.mkdir(parents=True,exist_ok=True)
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    entry_hash=sha(a.entries or a.historical)
    p=payment_receipt(a.payments,entry_hash,frame)
    if a.entries:
        assert p['evidence']=='NF622 moment-derived external entry enclosures'
        emit_full(a.output,D,S,y,U,w,T,mid,rad,a.entries,a.cache,p,entry_hash,sha(a.historical),frame)
    else:
        assert p['evidence']=='NF613 Arb entry enclosures converted outward to fixed-point'
        emit_pilot(a.output,D,S,y,U,mid,rad,p)
    m={'schema':'NF630-literal-payment-proposals-v1',
       'mode':'moment-full' if a.entries else 'historical-baseline-two-row',
       'historical_sha256':sha(a.historical),'entry_sha256':entry_hash,
       'payment_sha256':sha(a.payments),'cache_sha256':sha(a.cache) if a.cache else None,
       'files':[{'file':x.name,'sha256':sha(x)} for x in sorted(a.output.glob('*.lean'))],
       'scope':'untrusted proposals, not physical analytic custody'}
    (a.output/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
    print(m['mode'],len(m['files']),'Lean proposal modules')

if __name__=='__main__': main()
