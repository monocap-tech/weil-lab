#!/usr/bin/env python3
"""Independent exact tail/count/Schur composition and noncommuting countermodels."""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
PINS=['f1149e27da8a0e1d90e48b8ee0eb8a0a0b8ef51d0910499a7fcd19a082efca07','19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b','a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922']
def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def scale(a,c):return [[c*x for x in row] for row in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def det(a):
    if len(a)==1:return a[0][0]
    return sum(((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a))),Q(0))
def psd(a):
    from itertools import combinations
    for k in range(1,len(a)+1):
        for ix in combinations(range(len(a)),k):assert det([[a[i][j] for j in ix] for i in ix])>=0
def regressions():
    # Exact noncommuting finite model. H is A^-1; L is ACTUAL K^(1/2).
    L=[[Q(2),Q(1,100),Q(1,200)],[Q(1,100),Q(1,50),Q(0)],[Q(1,200),Q(0),Q(1,60)]]
    H=[[Q(10000),Q(1),Q(0)],[Q(1),Q(2),Q(1,8)],[Q(0),Q(1,8),Q(1)]]
    psd(L);psd(H);K=mm(L,L);B=mm(L,mm(H,L));beta=Q(17,8)
    epsilon=max(sum(abs(K[i][j]) for j in (1,2)) for i in (1,2))
    psd([[beta*Q(i==j)-H[i+1][j+1] for j in range(2)] for i in range(2)])
    psd([[epsilon*Q(i==j)-K[i+1][j+1] for j in range(2)] for i in range(2)])
    # Deflate range(L P), NOT range(P). Projection is exact rational.
    v=[[row[0]] for row in L];norm=mm(tr(v),v)[0][0];Pi=scale(mm(v,tr(v)),1/norm)
    R=add([[Q(i==j) for j in range(3)] for i in range(3)],scale(Pi,-1))
    psd(add(scale(R,beta*epsilon),scale(mm(R,mm(B,R)),-1)))
    assert B[1][1]>beta*epsilon  # False shortcut: physical Q B Q bound.
    assert mm(H,K)!=mm(K,H)
    # Both diagonal blocks below one do NOT control their full mixed Schur.
    small=[[Q(99,100),Q(1,10)],[Q(1,10),Q(1,50)]];psd(small)
    assert small[0][0]<1 and small[1][1]<1
    assert (1-small[0][0])*(1-small[1][1])-small[0][1]**2<0
    assert 1-small[0][0]-small[0][1]**2/(1-small[1][1])<0
def main():
    assert len(sys.argv)==5
    z=json.load(open(sys.argv[1]));raw=[Path(p).read_bytes() for p in sys.argv[2:]]
    assert [hashlib.sha256(x).hexdigest() for x in raw]==PINS
    r,e,c=map(json.loads,raw)
    assert z['input_sha256']==dict(zip(['reference','envelope','critical'],PINS))
    assert z['status']=='CONDITIONAL_ORIGINAL_BS_INFINITE_TAIL_AND_FINITE_COUNT_UPPER'
    assert r['original_J_count']==e['original_source_count']==z['original_physical_source_count']==470
    assert r['native_input_sha256']==e['input_sha256']['native']=='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
    eps=Q(e['whole_envelope_complement_upper']);delta=Q(1,10**500);k=Q(1,1000);ks=Q(33621,10**9)
    assert Q(r['clean_relative_error_upper'])==delta and Q(r['kappa'])==k and Q(r['inherited_B14_coercivity'])==ks
    beta=Q(r['reference_inverse_residual_upper_factor']);assert beta==(1+delta)/k
    assert Q(z['compressed_actual_Astar_inverse_upper'])==beta and Q(z['physical_complement_negative_upper'])==eps
    assert Q(z['inverse_compression_relative_error'])==delta and Q(z['inherited_global_Astar_floor'])==ks and Q(z['physical_complement_floor'])==k
    tail=eps*(1+delta)/k;level=1-Q(3,10**12)
    assert tail==Q(z['BS_complement_operator_upper'])==Q(z['eigenvalue_upper'])<Q(2431,10**8)==Q(z['clean_BS_complement_operator_upper'])<level
    assert z['BS_deflation_rank_upper']==470 and z['eigenvalue_index']==471
    assert Q(z['fourth_eigenvalue_lower'])==Q(c['fourth_BS_eigenvalue_lower'])>level==Q(z['critical_level'])
    assert z['critical_count_lower']==c['near_critical_dimension_lower']==4 and z['critical_count_upper']==z['original_negative_index_upper']==470
    coarse=eps/ks;assert Q(z['global_coercivity_only_tail_upper'])==coarse
    assert Q(z['tail_improvement_factor'])==coarse/tail>Q(297,10)
    assert Q(z['complement_inverse_upper'])==1/(1-tail)
    assert Q(z['generic_mixed_Schur_price'])==tail/(1-tail)
    assert Q(z['generic_sufficient_finite_threshold'])==1-tail
    for k in ['actual_physical_Q_B_Q_bound_claimed','physical_and_BS_deflation_spaces_identified','compressed_multiplier_square_identity_used','actual_BS_projection_computed','actual_finite_BS_block_computed','actual_mixed_BS_block_computed','finite_gate_certified','exact_critical_count_certified','global_true_BS_norm_upper_one_certified','full_signed_positivity_certified']:assert z[k] is False
    assert z['W_ODD_NEG']==z['inherited_original_domain_review']=='OPEN'
    regressions()
    print('INDEPENDENT ORIGINAL BS TAIL/COUNT REPLAY PASS: lambda471 <0.00002431, 4<=critical count<=470; wrong physical projection and omitted mixed Schur rejected; finite signed gate OPEN')
if __name__=='__main__':main()
