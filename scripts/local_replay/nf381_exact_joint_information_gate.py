#!/usr/bin/env python3
"""NF381: exact Fraction two-direction source-adapted signed response screen.

Two original supported integer sine harmonics are physically orthogonal exactly.
The only uncertified cross projection is bounded by Bessel/Cauchy in the fixed
original selected+fitted carrier, not guessed zero.
This is a lower bound on a TWO-dimensional exterior dual only, not a full norm.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
SHA512='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
B=F(11,10)
BUDGET=F(2401,2*10**28)

def valuepair(o,k):
    x=tuple(F(v) for v in o[k]);assert len(x)==2 and x[0]<=x[1],k;return x

def abs_lower(pair):
    l,h=pair
    return l if l>0 else -h if h<0 else F(0)

def abs_upper(pair):return max(abs(pair[0]),abs(pair[1]))

def square_floor_root(x, scale=10**65):
    from math import isqrt
    assert x>=0
    q=x*scale*scale
    return F(isqrt(q.numerator//q.denominator),scale)

def square_ceil_root(x, scale=10**65):
    from math import isqrt
    assert x>=0
    q=x*scale*scale
    n=q.numerator//q.denominator
    z=isqrt(n)
    if z*z < q:z+=1
    return F(z,scale)

def evaluate(p512,p513,sha513=None):
    raw512=Path(p512).read_bytes()
    assert hashlib.sha256(raw512).hexdigest()==SHA512
    if sha513:assert hashlib.sha256(Path(p513).read_bytes()).hexdigest()==sha513
    a=json.loads(raw512);b=json.loads(Path(p513).read_bytes())
    assert a['unfitted_n']==512 and b['unfitted_n']==513
    for o in (a,b):
        assert o['selected_rank']==242 and o['critical_count']==4
        assert o['original_physical_16_Gram_overlaps'] is True
        assert o['original_signed_32_CE_BP_overlaps'] is True
        assert o['original_WJJ_WJF_archived_cells_reused']==30371
        assert o['original_lowband_integral_computed'] is False
        assert o['entire_exterior_inverse_computed'] is False
        assert o['W_ODD_NEG']==o['RH']=='OPEN'
        assert F(o['original_direction_four_squared_residual_budget'])==BUDGET
        assert o['original_rank_sha256']==a['original_rank_sha256']
        assert o['original_source_sha256']==a['original_source_sha256']
        assert o['parent_original_archive_sha256']==a['parent_original_archive_sha256']
    g1=valuepair(a,'outside_E4_norm2_interval')
    g2=valuepair(b,'outside_E4_norm2_interval')
    h1=valuepair(a,'complete_original_signed_u4_qperp_interval')
    h2=valuepair(b,'complete_original_signed_u4_qperp_interval')
    assert 0<g1[0]<=g1[1]<=B and 0<g2[0]<=g2[1]<=B
    # Physical sine n=512 and n=513 have exact <v512,v513>=0.
    # q=(I-P_(J+F4))v, so cross=-<P_V v512,P_V v513>.
    # Since ||v_i||²=B and ||q_i||²=g_i, |cross|<=sqrt((B-g1)(B-g2)).
    crosscap=square_ceil_root((B-g1[0])*(B-g2[0]))
    assert crosscap**2<g1[0]*g2[0], 'independence not certified by coarse cross cap'
    # Exact fully rigorous optimal-in-subset lower witnesses: q1, q2,
    # and q1+t*q2 for t= ±{1/4,1/2,1,2,4}. Denom use actual upper
    # physical mass + 2|t| crosscap. Numerator use interval lower.
    rays=[]
    for t in [F(0),F(1,4),F(-1,4),F(1,2),F(-1,2),F(1),F(-1),F(2),F(-2),F(4),F(-4)]:
        lo=h1[0]+t*(h2[0] if t>=0 else h2[1])
        hi=h1[1]+t*(h2[1] if t>=0 else h2[0])
        lower=abs_lower((lo,hi))**2/(g1[1]+t*t*g2[1]+2*abs(t)*crosscap)
        rays.append((lower,t))
    rays.append((abs_lower(h2)**2/g2[1],'q513 only'))
    best,which=max(rays,key=lambda x:x[0]);single=abs_lower(h1)**2/g1[1]
    assert best>=single
    # The true full two-witness Gram inverse always dominates all tested rays.
    # A lower witness cannot upper-bound the full pair or the full complement.
    return dict(standing='EXACT FRACTION CERTIFIED TWO-WITNESS JOINT DUAL LOWER ONLY',
      source_native_512_sha256=SHA512,source_native_513_sha256=hashlib.sha256(Path(p513).read_bytes()).hexdigest(),
      original_n_values=[512,513],original_source_count=242,original_critical_count=4,
      original_orthogonality='supported sine harmonics n512,n513 exactly orthogonal on [-11/10,11/10]',
      certified_physical_joint_cross_abs_upper=str(crosscap),
      certified_physical_G_strictly_SPD=True,
      certified_squared_dual_lower_best_rational_ray=str(best),
      certified_squared_dual_lower_best_ray=str(which),
      original_single_512_squared_dual_lower=str(single),
      certified_joint_lower_as_fraction_of_budget=str(best/BUDGET),
      original_direction_four_squared_budget=str(BUDGET),
      fixed_sufficient_method_obstructed_by_this_joint_lower=best>BUDGET,
      original_full_two_witness_dual_upper_computed=False,
      original_lowband_integral_computed=False,whole_original_exterior_strong_residual_upper=False,
      whole_infinite_inverse_computed=False,analytic_domain_review='OPEN',W_ODD_NEG='OPEN',RH='OPEN')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--original-512',required=True)
    ap.add_argument('--native-513',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    d=evaluate(args.original_512,args.native_513)
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(d,indent=2)+'\n')
    print('NF381 rigorously certified joint original two-direction lower:',d['certified_joint_lower_as_fraction_of_budget'],'full exterior/RH OPEN')

if __name__=='__main__':main()
