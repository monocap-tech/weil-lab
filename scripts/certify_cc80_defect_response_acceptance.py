#!/usr/bin/env python3
"""CC80: source-status audit and exact matrix controls; no Weil source replay."""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

EXPECTED = {
35:'ab9e4ebd605063b6c3a929b96be9f0fc20c380c658f51d6055475e4b3ed1e3c9',
36:'51720dd0aa541f4d91c1dcbbc7ccc80d4b8b8d426bb998a0113377f0c8bd396d',
37:'45de7cb79e330d3e3bc534c2bd179de118924063de7a5987f405cf7b44a0dd78',
38:'f64f6d2d7f062b7e4306c8c74dc50c8370c266db9e424e79df8e40526b3cda96',
39:'4397d18a78fe8bf56d6928e7c4e438874ce4607e6d81c4418b4d989d67ee476c',
40:'cdb914cdd7e8b8d0575d9f1f997ad0b5d3a22696a77fe0d5f2ce42e542ae949c',
41:'21fe1825a090bb37135fe2d34ae68502f242b3567467ea8289e2ea736fbb3450'}

def mat(rows): return [[F(x) for x in row] for row in rows]
def tr(a): return list(map(list,zip(*a)))
def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def neg(a): return [[-x for x in r] for r in a]
def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def diag(v): return [[F(x) if i==j else F(0) for j in range(len(v))] for i,x in enumerate(v)]
def inv(a):
    n=len(a); w=[r[:]+e for r,e in zip(a,diag([1]*n))]
    for i in range(n):
        j=next(j for j in range(i,n) if w[j][i]); w[i],w[j]=w[j],w[i]
        p=w[i][i]; w[i]=[x/p for x in w[i]]
        for j in range(n):
            if j!=i:
                p=w[j][i]; w[j]=[x-p*y for x,y in zip(w[j],w[i])]
    return [r[n:] for r in w]
def pivots(a):
    w=[r[:] for r in a]; out=[]
    for i in range(len(w)):
        p=w[i][i]; out.append(p)
        if not p: break
        for j in range(i+1,len(w)):
            for k in range(i+1,len(w)): w[j][k]-=w[j][i]*w[i][k]/p
    return out
def serial(a): return [[str(x) for x in r] for r in a]

def controls():
    # Actual finite PSD defect and its exact boundary-source minorant.
    a0=diag([1,1,1]); d=diag([0,1,2]); a=add(a0,d)
    y=mat([[0,0],[1,0],[0,1]]); f=mul(d,y); dy=mul(tr(y),f)
    assert mul(mul(f,inv(dy)),tr(f))==d
    r=mat([[1,0,1],[0,1,1],[1,1,0]])
    c=mul(mul(tr(f),inv(a0)),r)
    b=add(dy,mul(mul(tr(f),inv(a0)),f))
    credit=mul(mul(tr(c),inv(b)),c)
    exact=mul(mul(tr(r),add(inv(a0),neg(inv(a)))),r)
    assert credit==exact
    assert len(pivots(b))==2 and all(x>0 for x in pivots(b))
    # Full-block genuine crossings with positive high and native blocks.
    crossings=[]; levels=[]
    for scale in [F(1),F(1,10**18)]:
        aa=diag([1,2,3]); rr=diag([1,1,scale])
        response=mul(mul(tr(rr),inv(aa)),rr)
        for sign in [F(-1,100),F(0),F(1,100)]:
            schur=diag([scale**2,scale**2,sign*scale**2]); q=add(response,schur)
            assert all(v>0 for v in pivots(q))
            recovered=add(q,neg(mul(mul(tr(rr),inv(aa)),rr)))
            assert recovered==schur
            crossings.append(dict(scale=str(scale),parameter=str(sign),last_pivot=str(recovered[2][2]),native_positive=True,high_positive=True))
        # Null full block kills (e3,-A^-1 R e3), so Qfull+delta I
        # has exact physical ground level delta, not just a high-block shift.
        q=add(response,diag([scale**2,scale**2,0]))
        full=[q[i]+tr(rr)[i] for i in range(3)]+[rr[i]+aa[i] for i in range(3)]
        z=[F(0),F(0),F(1),F(0),F(0),-scale/3]
        assert all(sum(x*y for x,y in zip(row,z))==0 for row in full)
        for delta in [F(1,1000),F(1,10),F(2)]:
            shifted=add(full,diag([delta]*6))
            assert all(x>0 for x in pivots(shifted))
            assert [sum(x*y for x,y in zip(row,z)) for row in shifted]==[delta*x for x in z]
            levels.append(dict(scale=str(scale),whole_mass_shift=str(delta),exact_ground_level=str(delta)))
    # Paying a negative witness is not a full joined matrix certificate.
    v=diag([-1,1,-1]); l=diag([2,0,0]); k=add(v,l)
    assert k[0][0]>0 and k[2][2]<0
    # A mass-relative error can change sign at the paid acceptance margin.
    mass=diag([1,4,9]); center=diag([F(1,10),F(4,10),F(9,10)])
    budgets=[]
    for eps in [F(9,100),F(1,10),F(11,100)]:
        paid=add(center,neg(diag([eps,4*eps,9*eps])))
        budgets.append(dict(error_budget=str(eps),mass_relative_margin=str(F(1,10)-eps)))
    return dict(Woodbury_exact_control=serial(credit),genuine_full_block_crossings=crossings,
        positive_whole_physical_mass_controls=levels,witness_only_pass_full_matrix_fail=True,
        mass_relative_error_crossings=budgets)

def run(root):
    audit=[]
    for n in range(35,42):
        paths=list(root.glob('notes/data/RPB108_NF%d_*VALIDATION*.json'%n)); assert len(paths)==1
        p=paths[0]; raw=p.read_bytes(); assert hashlib.sha256(raw).hexdigest()==EXPECTED[n]
        d=json.loads(raw); assert d['status']=='PASS'
        assert d.get('whole_aperture_positive') is False
        for key in ['actual_original_inverse_certified','actual_original_inverse_improvement_certified','actual_inverse_improvement_lower_bound_certified','six_retained_direction_plus_all_F_certified']:
            if key in d: assert d[key] is False
        audit.append(dict(milestone=d['milestone'],path=str(p.relative_to(root)),sha256=hashlib.sha256(raw).hexdigest(),published_status=d['status'],parity_status=[x['status'] for x in d['parity_checks']]))
    return dict(milestone='CC80',integration_parent='dd93e5cc7d003d44cdc240c5710f4c253dc1346f',
        read_only_source='4d2a5d7d3857854677a223ca38d03b13358f40e9',source_manifest_audit=audit,
        verification_scope='published validation manifests audited; original arithmetic producers not replayed',
        controls=controls(),conditional_full_matrix_acceptance='V38 + C* B^-1 C - epsilon M > 0',
        actual_defect_source_credit_certified=False,simultaneous_six_direction_certificate=False,
        whole_aperture_positive=False)
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('source_root',type=Path); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    result=run(a.source_root); a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+'\n'); print('CC80 PASS: source-manifest audit and exact acceptance controls only')
