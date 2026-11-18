#!/usr/bin/env python3
"""Emit all 242 widened scalar payment rows; exactly validate retained
receipt values and provenance without regenerating matrix products.
Mass and dot-product identities remain independent Lean obligations.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from emit_nf630_original_literal_payments import historical, payment_receipt, sha, rat, qlit, filetext
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA

BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentReceipts'
MODULE='WeilDefect.Generated.NF639'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'

def main():
    ap=argparse.ArgumentParser()
    for key in ('root','historical','entries','payments','cache','output'):
        ap.add_argument('--'+key,type=Path,required=True)
    a=ap.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    entry_hash,historical_hash=sha(a.entries),sha(a.historical)
    p=payment_receipt(a.payments,entry_hash,frame)
    eH,eV,r=map(rat,(p['uniform_H_radius'],p['uniform_V_radius'],p['r']))
    cols=[sum(abs(row[i]) for row in D) for i in range(N)]
    total=sum(cols); wm=sum(map(abs,w)); ym=sum(abs(v)*c for v,c in zip(y,cols))
    aden=Q*S*S; bden=Q*S*T
    files=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(filetext(imports,body))
        files.append({'file':path.name,'sha256':sha(path)})
    def params():
        body=''
        for k,v in [('S',S),('Q',Q),('T',T),('U',U)]:
            body+=f'def nf639{k} : ℕ := {v}\n'
        for k,v in [('EH',eH),('EV',eV),('R',r)]:
            body+=f'def nf639{k} : ℚ := {qlit(v)}\n'
        return body
    write('Params',[BASE],params())
    gates=[]
    with gzip.open(a.cache,'rt') as f:
        header=json.loads(next(f))
        assert header['schema']=='NF626-integer-center-cache-v1'
        assert header['entry_sha256']==entry_hash and header['historical_sha256']==historical_hash
        assert header['frame_sha256']==frame and header['frozen_sha256']==FROZEN_SHA
        assert {k:int(v) for k,v in header['scales'].items()}==dict(S=S,Q=Q,T=T,U=U)
        assert list(map(int,header['y']))==y and list(map(int,header['w']))==w
        assert [rat(header[k]) for k in ('eH','eV','r')]==[eH,eV,r]
        for i,line in enumerate(f):
            q=json.loads(line)
            assert q['i']==i<N
            A=list(map(int,q['A'])); b,ay,dy=map(int,(q['b'],q['Ay'],q['Dy']))
            assert len(A)==N
            defect=sum(abs((aden if i==j else 0)-v) for j,v in enumerate(A))
            col=cols[i]; mass=sum(map(abs,D[i]))
            assert dy==sum(x*z for x,z in zip(D[i],y))
            assert ay==sum(x*z for x,z in zip(A,y))
            row=F(defect,aden)+F(col*total,S*S)*eH
            res=abs(F(b,bden)-F(ay,aden*U))+F(col*wm,S*T)*eV+F(col*ym,S*S*U)*eH
            pay=abs(F(dy,S*U)-mid[i])+F(mass,S)*2*r
            pr=p['rows'][i]
            assert row==rat(pr['defect_upper']) and res==rat(pr['residual_upper'])
            assert pay==rat(pr['selected_payment']) and rad[i]==rat(pr['selected_radius'])
            assert row<=F(1,100) and res<=r and pay<=rad[i]
            v=f'nf639Row{i:03d}'
            coords=[defect,col,total,wm,ym,mass,b,ay,dy]
            body=OPT+f'def {v} : NF639PaymentRow := ⟨'+','.join(f'({x}:ℤ)' for x in coords)+'⟩\n\n'
            body+=f'theorem {v}Check : {v}.gate nf639S nf639Q nf639T nf639U nf639EH nf639EV nf639R {i}=true := by\n  decide +kernel\n\n'
            body+=f'#print axioms {v}Check'
            write(f'Row{i:03d}',[MODULE+'.Params'],body)
            gates.append(v)
    assert len(gates)==N
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF639-scalar-payment-proposals-v1',
        'rows':N,'external_scalar_replay':'PASS','entry_sha256':entry_hash,
        'historical_sha256':historical_hash,'payment_sha256':sha(a.payments),
        'cache_sha256':sha(a.cache),'files':files,'scope':'scalar gates only; mass and center-product custody separate'},indent=2)+'\n')
    print('NF639 242/242 widened row, residual and selected scalar payments independently replayed; literal proposals emitted')

if __name__=='__main__': main()
