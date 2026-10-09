#!/usr/bin/env python3
"""Independent rational interval consumer of NF42; no source integration."""
import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

EXPECTED={
'RPB108_NF42_BOUNDARY_RESPONSE_VALIDATION_20261009.json':'69626c40fd55c49a162a494ed70210088148dd86e80dff385698b85f78105471',
'RPB108_NF42_EVEN_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json':'e58c3ea1160fc1c632d50c6d61d7f1595919ed0707bb77a1109662b6830d50c4',
'RPB108_NF42_ODD_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json':'24655cd64c0bf8b6b7b9dce654ff10ad3085eb3b56879bc123873cde54df1d9f'}
def iv(x):
    if isinstance(x,(str,F,int)): return (F(x),F(x))
    a,b=map(F,x); assert a<=b; return a,b
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[1],-a[0]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b]; return min(p),max(p)
def div(a,b):
    assert b[0]>0 or b[1]<0
    return mul(a,(1/b[1],1/b[0]))
def overlap(a,b): return max(a[0],b[0])<=min(a[1],b[1])
def sumiv(v):
    t=iv(0)
    for x in v:t=add(t,x)
    return t
def matrix(a): return [[iv(x) for x in row] for row in a]
def mm(a,b): return [[sumiv(mul(x,y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def quad(a,h):return sumiv(mul(mul(iv(h[i]),a[i][j]),iv(h[j])) for i in range(len(h)) for j in range(len(h)))
def det2(a):return sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]))
def det3(a):
    return sumiv([mul(a[0][0],sub(mul(a[1][1],a[2][2]),mul(a[1][2],a[2][1]))),
        neg(mul(a[0][1],sub(mul(a[1][0],a[2][2]),mul(a[1][2],a[2][0])))),
        mul(a[0][2],sub(mul(a[1][0],a[2][1]),mul(a[1][1],a[2][0])))])
def pair(a):
    # Compact outward rational publication; computations above stay exact.
    size=max(abs(a[0]),abs(a[1]))
    exponent=math.floor(math.log10(float(size))) if size else 0
    scale=10**max(0,80-exponent)
    return [str(F((a[0]*scale).__floor__(),scale)),str(F((a[1]*scale).__ceil__(),scale))]
def load(root,name):
    raw=(root/'notes/data'/name).read_bytes(); assert hashlib.sha256(raw).hexdigest()==EXPECTED[name]
    return json.loads(raw)
def rank_one_controls():
    rows=[]
    for scale in [F(1),F(1,10**18)]:
        z=[F(1,2),F(1,3),scale]; base=[F(1),F(1),-scale**2/2]
        for t in [F(99,100),F(1),F(101,100)]:
            tau=F(36,59)*t
            k=[[iv((base[i] if i==j else 0)+tau*z[i]*z[j]) for j in range(3)] for i in range(3)]
            a=[r[:2] for r in k[:2]]; da=det2(a)
            assert da[0]>0
            # Exact border condensation against the updated leading block.
            b=[k[0][2],k[1][2]]
            ai=[[div(a[1][1],da),div(neg(a[0][1]),da)],[div(neg(a[1][0]),da),div(a[0][0],da)]]
            schur=sub(k[2][2],quad(ai,[b[0][0],b[1][0]]))
            expected=scale**2*(-F(1,2)+tau/(1+tau*F(13,36)))
            assert schur==iv(expected) and det3(k)==mul(da,schur)
            assert (expected>0)==(t>1) and (expected==0)==(t==1)
            # The same response credit is invariant under nonzero source scaling.
            for strength in [F(1,7),F(-3),F(10**12)]:
                assert (strength*z[2])**2/(strength**2/tau)==tau*z[2]**2
            rows.append(dict(scale=str(scale),multiplier=str(t),exact_margin=str(expected)))
    return rows
def run(root):
    val=load(root,'RPB108_NF42_BOUNDARY_RESPONSE_VALIDATION_20261009.json'); assert val['status']=='PASS'
    assert val['background_floor_newly_proved'] is False and val['whole_aperture_positive'] is False
    rows=[]
    for parity in ['even','odd']:
        name='RPB108_NF42_'+parity.upper()+'_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json'
        d=load(root,name); h=list(map(F,d['frozen_NF38_witness']))
        assert d['parity']==parity and d['aperture']=='53/50'
        assert d['background_floor_newly_proved'] is False and d['conditional_joined_Schur_certificate_passed'] is False
        assert d['actual_negative_original_form_claimed'] is False
        g=matrix(d['original_defect_source_inverse_coupling']); b=matrix(d['positive_Woodbury_denominator'])
        db=det2(b); assert b[0][0][0]>0 and db[0]>0
        bi=[[div(b[1][1],db),div(neg(b[0][1]),db)],[div(neg(b[1][0]),db),div(b[0][0],db)]]
        delta=mm(mm(transpose(g),bi),g)
        frozen=matrix(d['conditional_joined_inverse_improvement_lower_matrix'])
        assert all(overlap(delta[i][j],frozen[i][j]) for i in range(3) for j in range(3))
        # Use a different arithmetic order: g*h first, then the 2x2 inverse.
        gh=mm(g,[[iv(x)] for x in h]); improve=mm(mm(transpose(gh),bi),gh)[0][0]
        assert improve[0]>0 and overlap(improve,iv(d['conditional_frozen_witness_inverse_improvement']))
        k=matrix(d['conditional_improved_joined_Schur_lower_matrix']); kh=quad(k,h)
        leading=[row[:2] for row in k[:2]]; dk=det3(k)
        assert k[0][0][0]>0 and det2(leading)[0]>0 and dk[1]<0 and kh[1]<0
        assert overlap(kh,iv(d['improved_lower_witness_value']))
        baseline=iv(d['baseline_witness_value']); assert baseline[1]<0
        share=div(improve,neg(baseline))
        deficit=-kh[1]; assert deficit>0
        rows.append(dict(parity=parity,independent_Woodbury_entries_overlap=True,
            positive_denominator_determinant=pair(db),conditional_witness_improvement=pair(improve),
            independent_joined_determinant=pair(dk),independent_joined_witness_value=pair(kh),
            fraction_of_baseline_witness_deficit=pair(share),necessary_further_witness_credit_lower=pair(iv(deficit))[0],
            background_floor_hypothesis=d['background_floor_hypothesis'],joined_certificate_passed=False))
    return dict(milestone='CC81',integration_parent='e54ff7bc65914a73b8dbd29c408eabd55f6a50d2',
        read_only_source='f2c49f8d2ff95374d3ee2c3b1836ec772e4817dc',input_sha256=EXPECTED,
        verification_scope='independent certificate matrix arithmetic; original source integrations not replayed',
        parity_checks=rows,rank_one_residual_credit_crossings=rank_one_controls(),
        actual_defect_source_credit_source_certified_conditionally=True,
        simultaneous_six_direction_certificate=False,whole_aperture_positive=False)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    d=run(a.source_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    for r in d['parity_checks']:
        print(r['parity'],'fraction',*[float(F(x)) for x in r['fraction_of_baseline_witness_deficit']], 'remaining >',float(F(r['necessary_further_witness_credit_lower'])))
