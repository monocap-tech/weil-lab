#!/usr/bin/env python3
"""NF382 exact optimal robust two-direction signed dual.

No original n513 result is created by this code. Original inputs must pass
the entire NF381 SHA and overlap preflight before any native report is accepted.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
import nf381_exact_joint_information_gate as parent

def optimal(a,b,G1,G2,C):
    """Maximize (a*x+b*y)^2/(G1*x^2+2*C*x*y+G2*y^2) for x,y>=0."""
    a,b,G1,G2,C=map(F,(a,b,G1,G2,C))
    assert a>=0 and b>=0 and G1>0 and G2>0 and C>=0
    assert C*C<G1*G2, 'upper Gram is not SPD'
    x,y=G2*a-C*b,G1*b-C*a
    if x>0 and y>0:
        d=(G2*a*a-2*C*a*b+G1*b*b)/(G1*G2-C*C)
        assert d>=a*a/G1 and d>=b*b/G2
        return d,'optimal-interior',x,y
    if a*a/G1>=b*b/G2:
        return a*a/G1,'first-only',F(1),F(0)
    return b*b/G2,'second-only',F(0),F(1)

def self_test():
    # Abstract rational fixtures ONLY; never original-object evidence.
    cases=[
      (1,2,1,1,F(1,4),F(64,15)),
      (1,2,1,1,F(4,5),F(4)),
      (1,1,1,1,F(1,4),F(8,5)),
      (0,2,1,1,F(1,4),F(4)),
      (1,0,1,1,F(1,4),F(1)),
      (1,2,2,3,F(1,2),F(36,23)),
      (1,1,1,1,0,F(2)),
      (0,0,1,1,F(1,4),F(0)),
    ]
    for a,b,G1,G2,C,expected in cases:
        d,kind,x,y=optimal(a,b,G1,G2,C)
        assert d==expected,(kind,d,expected)
        assert x>=0 and y>=0
        if x or y:
            assert d==(F(a)*x+F(b)*y)**2/(F(G1)*x*x+2*F(C)*x*y+F(G2)*y*y)
        for k in range(-8,9):
            c=F(C)*F(k,8)
            true=(F(G2)*F(a)**2-2*c*F(a)*F(b)+F(G1)*F(b)**2)/(F(G1)*F(G2)-c*c)
            assert d<=true
    print('NF382 8 exact-rational algebra fixtures PASS (not original n513 data)')

def preflight_512(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==parent.SHA512
    j=json.loads(raw)
    assert j['unfitted_n']==512 and j['original_signed_32_CE_BP_overlaps'] is True
    g1lo,g1hi=parent.valuepair(j,'outside_E4_norm2_interval')
    assert 0<g1lo<=g1hi<parent.B
    assert F(1445,100000)<parent.B-g1lo<F(1446,100000)
    print('NF382 original n512 native SHA PASS; g513>0.01446 would suffice for robust Gram independence; n513 unmeasured')
    return g1lo,g1hi

def evaluate(path512,path513):
    # Parent preserves original physical/signed overlap checks and SHA pins.
    old=parent.evaluate(path512,path513)
    a=json.loads(Path(path512).read_bytes())
    b=json.loads(Path(path513).read_bytes())
    g1=parent.valuepair(a,'outside_E4_norm2_interval')
    g2=parent.valuepair(b,'outside_E4_norm2_interval')
    h1=parent.valuepair(a,'complete_original_signed_u4_qperp_interval')
    h2=parent.valuepair(b,'complete_original_signed_u4_qperp_interval')
    l1,l2=parent.abs_lower(h1),parent.abs_lower(h2)
    s1=1 if h1[0]>0 else -1 if h1[1]<0 else 0
    s2=1 if h2[0]>0 else -1 if h2[1]<0 else 0
    C=F(old['certified_physical_joint_cross_abs_upper'])
    d,kind,x,y=optimal(l1,l2,g1[1],g2[1],C)
    assert (x==0 or s1!=0) and (y==0 or s2!=0)
    grid=F(old['certified_squared_dual_lower_best_rational_ray'])
    best=max(grid,d)
    return {
       'standing':'NF382 CERTIFIED OPTIMAL ROBUST TWO-RAY LOWER ON SHA-PINNED ORIGINAL INPUT ONLY',
       'source_native_512_sha256':parent.SHA512,
       'source_native_513_sha256':old['source_native_513_sha256'],
       'nf381_all_original_overlap_and_sha_checks':True,
       'physical_cross_abs_upper':str(C),
       'signed_abs_lower_512':str(l1),'signed_abs_lower_513':str(l2),
       'physical_norm2_upper_512':str(g1[1]),'physical_norm2_upper_513':str(g2[1]),
       'optimal_ray_kind':kind,'signed_ray_weight_512':str(s1*x),
       'signed_ray_weight_513':str(s2*y),
       'optimal_robust_dual_squared_lower':str(d),
       'nf381_fixed_grid_squared_lower':str(grid),
       'combined_certified_joint_squared_lower':str(best),
       'original_nf370_direction_four_budget':str(parent.BUDGET),
       'nf370_sufficient_method_obstructed':best>parent.BUDGET,
       'actual_full_joint_Gram_known':False,
       'whole_strong_residual_upper_computed':False,
       'whole_inverse_computed':False,'operator_domain_audit':'OPEN',
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--self-test',action='store_true')
    p.add_argument('--preflight-512')
    p.add_argument('--original-512')
    p.add_argument('--native-513')
    p.add_argument('--output')
    args=p.parse_args()
    if args.self_test:self_test()
    if args.preflight_512:preflight_512(args.preflight_512)
    if args.original_512 or args.native_513 or args.output:
        if not (args.original_512 and args.native_513 and args.output):
            p.error('Original n512, native n513, and output are ALL required')
        report=evaluate(args.original_512,args.native_513)
        Path(args.output).parent.mkdir(parents=True,exist_ok=True)
        Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
        print('NF382 certified joint lower:',report['combined_certified_joint_squared_lower'],
              'NF370 specific STOP?',report['nf370_sufficient_method_obstructed'])
    elif not (args.self_test or args.preflight_512):
        p.error('Specify --self-test, --preflight-512, or all native inputs')

if __name__=='__main__':main()
