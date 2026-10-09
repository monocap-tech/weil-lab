#!/usr/bin/env python3
"""Independent original native high-coordinate check of NF28's retained w.
Uses the unchanged NF24 N720/K620 signed projection archive as oracle.
"""
import json,gzip,base64,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import certify_native_high_correction_nf26_106 as base
n=base.n

def run(targets,nf27,projection):
    c,pi=base.constants();powers=(2,3,4,5,7,8)
    logs={k:n.ni(n.native.log(k)) for k in powers}
    shifts=[(s*logs[k],(logs[2] if k in (4,8) else logs[k])/n.sqrt_r(F(k))) for k in powers for s in (1,-1)]
    cuts=[n.I(-n.A),n.I(n.A)]+[n.I(n.A)-t if t.l>0 else n.I(-n.A)-t for t,w in shifts];cuts.sort(key=lambda v:v.l)
    eta_unit=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    result=[]
    for row,wc in zip(targets['authenticated_compensated_targets'],nf27['parity_certificates']):
        parity=row['parity'];ids=row['retained_indices'];coeff=list(map(F,wc['exact_rational_retained_response']))
        h=118 if parity=='even' else 117
        p,b,l=base.source(ids,coeff,c,parity);test=n.basis(h)
        M,ML,ML2,cm=n.moments(cuts,len(b)+h,c,pi)
        val=n.dot(b,test,M)+n.dot(l,test,ML)
        shifted=[n.scale(n.shifted(p,t),-w) for t,w in shifts]
        for (L,U),(mp,ml) in zip(zip(cuts,cuts[1:]),cm):
            mid=F(L.h+U.l,2*n.SCALE);active=[]
            for k,(t,w) in enumerate(shifts):
                z=n.I(mid)+t;inside=-n.A<F(z.l,n.SCALE) and F(z.h,n.SCALE)<n.A
                outside=F(z.h,n.SCALE)<-n.A or F(z.l,n.SCALE)>n.A;assert inside or outside
                if inside:active.append(k)
            prime=base.sum_polys([shifted[k] for k in active]);val+=n.dot(prime,test,mp)
        oracle=sum((v*n.I(*map(F,projection[f'{i},{h}']['full'])) for i,v in zip(ids,coeff)),n.I(0))
        eta=eta_unit*F(n.sqrt_r(sum(v*v for v in coeff)).h,n.SCALE)
        paid=val+n.I(-eta,eta);assert paid.l<=oracle.h and paid.h>=oracle.l
        result.append(dict(parity=parity,test_degree=h,reconstructed_unsquared_pairing=val.ends(),original_independent_native_pairing=oracle.ends(),paid_source_error=str(eta),paid_overlap=True))
        print(parity,'independent high pairing passed',flush=True)
    return dict(milestone='NF28',status='PASS',original_native_high_coordinate_checks=result)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('targets');a.add_argument('nf27');a.add_argument('projection_b64');a.add_argument('--output',required=True);a=a.parse_args()
    traw=Path(a.targets).read_bytes();wraw=Path(a.nf27).read_bytes();praw=gzip.decompress(base64.b64decode(Path(a.projection_b64).read_bytes()))
    sha=[hashlib.sha256(v).hexdigest() for v in (traw,wraw,praw)]
    assert sha==['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346']
    r=run(json.loads(traw),json.loads(wraw),json.loads(praw)['complete_original_signed_source']);r['input_sha256']=sha;Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
