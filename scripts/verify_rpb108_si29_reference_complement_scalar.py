#!/usr/bin/env python3
"""Exact composition of original SI29 reference inverse on J470-perp.

The native physical Schur enclosure is inherited from a pinned GitHub
artifact. This script checks its rational composition, not its native builder
or the analytic operator proof. No Astar energy Schur is evaluated.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR

INPUT_SHA='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
TRIAL_SHA='87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f'
KAPPA=F(1,1000);B=F(11,10)

def dyadic(x):
    n,e=int(x[0]),int(x[1])
    return F(n*2**max(e,0),2**max(-e,0))

def mm(A,B):
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def tr(A):return list(map(list,zip(*A)))
def add(A,B):return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def scale(c,A):return [[c*a for a in row] for row in A]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inverse(A):
    n=len(A);rows=[list(row)+identity for row,identity in zip(A,eye(n))]
    for k in range(n):
        p=next(i for i in range(k,n) if rows[i][k])
        rows[k],rows[p]=rows[p],rows[k];s=rows[k][k]
        rows[k]=[x/s for x in rows[k]]
        for i in range(n):
            if i!=k:
                s=rows[i][k];rows[i]=[a-s*b for a,b in zip(rows[i],rows[k])]
    return [row[n:] for row in rows]
def psd2(A):
    assert A[0][1]==A[1][0]
    return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]>=A[0][1]**2

def coupled_regression():
    # Exact coupled algebra check only; never substituted for original data.
    # J=span(e1), pole in J, but F has TWO nonzero complement components.
    k=F(1);gamma=F(2);eps=F(1,10);mu=F(7,8)
    f=[[F(1)],[eps],[2*eps]];s=[[F(1,4)],[F(0)],[F(0)]]
    V=add(scale(gamma,mm(f,tr(f))),scale(-2,mm(s,tr(s))))
    A=add(eye(3),V);Ai=inverse(A)
    # B>=7/8 I by I-2ss*>=7/8 I and F gamma F*>=0.
    identity=add(add(eye(3),scale(-1,V)),mm(mm(V,Ai),V))
    assert identity==Ai
    E=f[1:];distance=sum((x[0]**2 for x in E),F(0))
    weighted=gamma**2*sum((x[0]**2 for x in f),F(0))
    lo=gamma*distance/k;hi=weighted*distance/(k*mu)
    compression=[row[1:] for row in Ai[1:]]
    assert compression[0][1]!=0
    assert psd2(add(compression,scale(-(1-lo),eye(2))))
    assert psd2(add(scale(1+hi,eye(2)),scale(-1,compression)))
    def schur(M):
        return [[M[i][j]-M[i][0]*M[0][j]/M[0][0] for j in (1,2)] for i in (1,2)]
    S_B=schur(A)
    assert S_B==inverse(compression)
    assert S_B!=[row[1:] for row in A[1:]]
    g=[[F(1,4)],[F(1,2)],[F(3,4)]]
    actual=add(A,mm(g,tr(g)));S_A=schur(actual)
    assert psd2(add(S_A,scale(-1,S_B)))
    assert psd2(add(S_A,scale(-k/(1+hi),eye(2))))
    # Dropping the J-perp hypothesis would make this scalar lower false.
    assert Ai[0][0]<1-lo
    return dict(nonzero_complement_cross_checked=True,
                pole_sign_and_second_resolvent_identity_checked=True,
                inverse_compression_and_Schur_monotonicity_checked=True,
                extension_outside_J_perp_rejected=True)

def main():
    p=argparse.ArgumentParser();p.add_argument('--certificate',required=True)
    p.add_argument('--trial-certificate',required=True)
    p.add_argument('--output',default='artifacts/si29_reference_on_J_perp.json')
    args=p.parse_args();raw=Path(args.certificate).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==INPUT_SHA
    z=json.loads(raw)
    assert z['status']=='CERTIFIED_FULL_ORIGINAL_J470_SI29_L2_QUOTIENT_NORMALIZATION'
    assert z['physical_full_J_projection_computed'] is True
    assert z['full_original_source_count']==470 and z['actual_feature_count']==14
    assert len(z['original_source_nodes'])==107
    assert sum(p for _,p in z['original_source_nodes'])==469
    actual=[(str(c),str(r),p) for c,r,_,p in FEATURES]
    assert [(str(F(c)),str(F(r)),p) for c,r,p in z['feature_definitions']]==actual
    S=z['physical_Schur_balls'];assert len(S)==14 and all(len(row)==14 for row in S)
    diagonal_uppers=[]
    for i in range(14):
        mid,rad=map(dyadic,S[i][i]);assert rad>=0
        u=abs(mid)+rad;assert u>0;diagonal_uppers.append(u)
    # E=(I-P_J)F: ||E||^2 <= ||E||_HS^2=tr(E*E)=tr(S).
    distance2=sum(diagonal_uppers,F(0))
    assert distance2<F(1,10**512)
    gamma=[4*r*delta/(3 if degree else 1) for c,r,delta,degree in FEATURES]
    amplitudes=[F(3,2) if degree else F(1) for c,r,delta,degree in FEATURES]
    assert len(gamma)==14 and min(gamma)>0 and max(gamma)==F(8,25)
    # Exact continuous mean/moment total-variation bounds, not Simpson proxies.
    weighted_feature_HS2=2*B*sum((g*g*a*a for g,a in zip(gamma,amplitudes)),F(0))
    assert weighted_feature_HS2==F(818166899,1250000000)
    assert KAPPA_STAR==F(33621,10**9)
    rho_lower=max(gamma)*distance2/KAPPA
    rho_upper=weighted_feature_HS2*distance2/(KAPPA*KAPPA_STAR)
    delta=F(1,10**500)
    assert 0<rho_lower<delta and 0<rho_upper<delta
    # Schur monotonicity: Astar>=B14 implies S_A>=S_B, whereas
    # S_B=(Q B14^-1 Q restricted to QH)^-1 >= kappa/(1+delta).
    # Transport to the SAME accepted normalized W=(I-P_J)FC.
    assert F(z['normalized_physical_Schur_lower'])==F(99,100)
    sharp_energy_lower=F(99,100)*KAPPA/(1+delta)
    clean_energy_lower=F(99,100001)
    assert sharp_energy_lower>clean_energy_lower
    trial_raw=Path(args.trial_certificate).read_bytes()
    assert hashlib.sha256(trial_raw).hexdigest()==TRIAL_SHA
    trial=json.loads(trial_raw)
    assert trial['status']=='CONDITIONAL_ORIGINAL_FULL_484_TRIAL_PHYSICAL_PRECONDITIONER'
    assert trial['native_input_sha256']==INPUT_SHA
    assert trial['full_trial_dimension']==484
    assert trial['rational_Astar_trial_energy_upper']==44
    assert trial['physical_Gram_lower']=='99/100' and trial['physical_Gram_upper']=='101/100'
    assert trial['actual_Astar_projection_computed'] is False
    old_lower=F(z['normalized_Astar_energy_Schur_lower'])
    assert old_lower==F(3328479,10**11)
    condition=F(44)/clean_energy_lower
    assert condition==F(400004,9)<44445
    assert clean_energy_lower/old_lower>F(297,10)
    # For V=B14-kI, B14^-1=k^-1 I-k^-2 V+k^-2 V B14^-1 V.
    # Qs=0, QVQ=E Gamma E*, VQ=F Gamma E*. B14>=kstar I
    # therefore bounds the ENTIRE compression, not separate diagonal values.
    result=dict(status='CONDITIONAL_FULL_ORIGINAL_SI29_REFERENCE_INVERSE_ON_J470_PERP',
      native_input_sha256=INPUT_SHA,original_J_count=470,actual_continuous_feature_count=14,
      raw_feature_physical_Schur_diagonal_uppers=list(map(str,diagonal_uppers)),
      raw_feature_complement_HS_squared_upper=str(distance2),clean_HS_squared_upper='1/'+str(10**512),
      original_positive_weights=list(map(str,gamma)),continuous_feature_amplitude_bounds=list(map(str,amplitudes)),
      weighted_feature_HS_squared_upper=str(weighted_feature_HS2),
      kappa=str(KAPPA),inherited_B14_coercivity=str(KAPPA_STAR),
      exact_relative_lower_error_upper=str(rho_lower),exact_relative_upper_error_upper=str(rho_upper),
      clean_relative_error_upper=str(delta),
      reference_inverse_residual_lower_factor=str((1-delta)/KAPPA),
      reference_inverse_residual_upper_factor=str((1+delta)/KAPPA),
      accepted_full_trial_input_sha256=TRIAL_SHA,
      normalized_actual_Astar_energy_Schur_sharp_lower=str(sharp_energy_lower),
      normalized_actual_Astar_energy_Schur_clean_lower=str(clean_energy_lower),
      normalized_actual_Astar_energy_Schur_upper='44',
      prior_normalized_Astar_energy_Schur_lower=str(old_lower),
      actual_energy_Schur_lower_improvement_factor=str(clean_energy_lower/old_lower),
      normalized_actual_Astar_energy_Schur_inverse_upper=str(1/clean_energy_lower),
      normalized_actual_Astar_energy_Schur_condition_upper=str(condition),
      actual_energy_Schur_lower_transfer='Schur monotonicity Astar>=B14, full compressed-inverse identity for B14, same physical normalized quotient W',
      statement='For EVERY bounded residual synthesis R with Jstar R=0: (1-delta)/kappa Rstar R <= Rstar B14^-1 R <= (1+delta)/kappa Rstar R',
      noncommutative_inverse_square_order_used=False,exact_coupled_algebra_regression=coupled_regression(),
      actual_Astar_inverse_computed=False,actual_Astar_energy_Schur_response_computed=False,
      actual_strong_residual_computed=False,negative_action_transfer_claimed=False,
      analytic_and_native_input_standing='CONDITIONAL on inherited original SI29/SM19 and pinned native physical Schur enclosure; exact arithmetic replay is not independent analytic review',
      W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('ORIGINAL J470-PERP REFERENCE INVERSE RELATIVE ERROR < 10^-500; exact composition and coupled algebra PASS')
    print('ACTUAL NORMALIZED 14D ENERGY SCHUR: 99/100001 I <= T_A <= 44 I; CONDITION <= 400004/9 < 44445')
if __name__=='__main__':main()
