#!/usr/bin/env python3
"""CP032 original-source-oriented termwise outward rational manifest.

Source: CP031 *independent* exact rational Euler-Maclaurin reimplementation.
This is NOT original CP025 pinned replay, an original Lean source-membership
proof, a compiler receipt, or an RH/Weil theorem. Generated integers may
only be used as targets of Lean proofs, never as new axioms.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
import argparse
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / 'scripts/cp031_independent_original_six_scalar_interval_crosscheck.py'
ENGINE_BLOB = '61b0cc0577986753a74f61cd51aa8391023161e2'
CELL = 10**15
FINAL = 10**9
HEIGHTS = {'left':Q(15005352,100000), 'right':Q(15005353,100000)}
EXPECTED = {
    'left': {'real':[-516,-515], 'imag':[-447,-446], 'rotated':[-682,-681]},
    'right':{'real':[11733,11734], 'imag':[10158,10159], 'rotated':[15519,15520]}
}
def git_blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def load():
    if git_blob(ENGINE) != ENGINE_BLOB:
        raise ValueError('CP031 independent engine blob identity mismatch')
    spec=importlib.util.spec_from_file_location('cp032_frozen_cp031',ENGINE)
    if spec is None or spec.loader is None:
        raise ValueError('CP031 independent rational engine unavailable')
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    if m.S != 10**55:
        raise ValueError('CP031 interval fixed precision drift')
    return m

def outer(interval, src=10**55, d=CELL):
    return [interval.l*d//src, -(-interval.h*d//src)]
def add_all(cells):
    return [sum(x[0] for x in cells), sum(x[1] for x in cells)]
def neg(c):return [-c[1],-c[0]]
def sub(a,b):return add_all([a,neg(b)])
def mul(a,b,d=CELL):
    v=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
    return [min(v)//d, -(-max(v)//d)]
def downsample(c):
    return [c[0]*FINAL//CELL,-(-c[1]*FINAL//CELL)]
def contains(a,b):return a[0]<=b[0] and b[1]<=a[1]

def sanity():
    assert Q(15005352,100000)==Q('150.05352')
    assert Q(15005353,100000)==Q('150.05353')
    assert mul([1,2],[-3,-2],1)==[-6,-2]
    assert sub([1,3],[4,5])==[-4,-1]
    assert downsample([-1000001,1000001])==[-2,2]
    assert contains([-3,2],[-3,1]) and not contains([-2,2],[-3,1])

def one(t,side,m):
    s=m.C(Q(1,2),t)
    terms=[]
    for n in range(1,256):
        sn,co=m.trig(t*m.lnq(n))
        z=m.C(co*m.invsqrt(n),-sn*m.invsqrt(n))
        terms.append({'kind':'dirichlet','n':n,'re':outer(z.r),'im':outer(z.i)})
    sn,co=m.trig(t*m.LOG256)
    base=m.C(co*Q(1,16),-sn*Q(1,16))
    pole=base*256/(s-1)
    half=base/2
    terms += [{'kind':'pole','re':outer(pole.r),'im':outer(pole.i)},
              {'kind':'half','re':outer(half.r),'im':outer(half.i)}]
    p=m.C(1)
    for j in range(11):
        p=p*(s+j)
        if j%2==0:
            k=(j+2)//2
            b=m.BERNOULLI[k-1]
            z=p*base*(b/factorial(2*k)/256**(2*k-1))
            terms.append({'kind':'bernoulli','k':k,'B':str(b),
                          're':outer(z.r),'im':outer(z.i)})
    if len(terms)!=263:
        raise ValueError('genuine 255+1+1+6 term count drift')
    re=add_all([v['re'] for v in terms])
    im=add_all([v['im'] for v in terms])
    th=m.source_theta_stirling2(t)
    st,ct=m.trig(th)
    sine,cosine=outer(st),outer(ct)
    rotated=sub(mul(cosine,re),mul(sine,im))
    coarse={'real':downsample(re),'imag':downsample(im),
            'rotated':downsample(rotated)}
    bulk=m.original_A(t)
    sin2,cos2=m.trig(m.source_theta_stirling2(t))
    bulk_rot=(m.C(cos2,sin2)*bulk).r
    if not all(contains(src,chk) for src,chk in zip(
        [re,im,rotated],map(outer,[bulk.r,bulk.i,bulk_rot]))):
        raise ValueError('termwise sum fails to enclose independent bulk arithmetic')
    if not all(contains(EXPECTED[side][key],coarse[key]) for key in coarse):
        raise ValueError('termwise 10^-9 cells disagree with CP031')
    if max(map(abs,re))>10**11 or max(map(abs,im))>10**11:
        raise ValueError('CP030 component threshold fails')
    if side=='left' and coarse['rotated'][1]>-200:
        raise ValueError('CP030 strict negative rotated threshold fails')
    if side=='right' and coarse['rotated'][0]<1000:
        raise ValueError('CP030 strict positive rotated threshold fails')
    return {'t':str(t),'terms_255_dirichlet_1_pole_1_half_6_Bernoulli':terms,
            'sine_cell_10pow15':sine,'cosine_cell_10pow15':cosine,
            'A_real_sum_10pow15':re,'A_imag_sum_10pow15':im,
            'rotated_real_cell_10pow15':rotated,
            'coarse_cells_10pow9':coarse,'source_Lean_membership_paid':False}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--receipt',type=Path)
    a=p.parse_args()
    sanity()
    m=load()
    points={}
    for side,t in HEIGHTS.items():
        points[side]=one(t,side,m)
        print('CP032',side,points[side]['coarse_cells_10pow9'],'PASS EXTERNAL NOT LEAN')
    out={'status':'CP032_526_SOURCE_ORIENTED_TERM_CELLS_PASS_EXTERNAL_NOT_LEAN',
         'source_engine_git_blob':git_blob(ENGINE),
         'original_source_verified_in_Lean':False,
         'actual_pinned_CP025_replay':False,
         'term_count_per_endpoint':263,'cell_denominator':CELL,
         'summary_denominator':FINAL,'points':points,
         'genuine_526_term_memberships_Lean_paid':False,
         'genuine_phase_memberships_Lean_paid':False,
         'unconditional_original_zeta_zero_Lean_accepted':False,
         'original_rank53_accepted':False,
         'global_signed_Weil_positive_or_RH':False}
    if a.receipt:
        a.receipt.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print('CP032 ALL 526 EXTERNAL INTERVAL TERM CELLS PASS; NO LEAN PAYMENT')

if __name__=='__main__':
    try:main()
    except (ValueError,AssertionError,OSError,ZeroDivisionError) as e:
        raise SystemExit('CP032 NOT LEAN / FAIL CLOSED: '+str(e))
