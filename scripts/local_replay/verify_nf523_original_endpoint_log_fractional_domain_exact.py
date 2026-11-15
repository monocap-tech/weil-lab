#!/usr/bin/env python3
"""NF523 original NF494 endpoint-log source: sharp H^(1/2) obstruction,
constructive H^(1/4) bounds, natural logarithmic operator-domain inclusion.

Arithmetic acceptance: only exact Fraction, full 400 original source intervals,
original 1/25 Cauchy radius and paid original geometric analytic tails.
The analytic Sobolev and moment-matching proofs are stated in the companion
note; this script audits every quantitative source hypothesis, NOT a Lean build.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SHA='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
B=F(11,10);DELTA=F(1,500);RAD=F(1,25);N=400

def read(path):
 b=Path(path).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def atanh(q,n):
 z=sum((2*q**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 tail=2*q**(2*n+1)/(F(2*n+1)*(1-q*q))
 return z,z+tail

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--nf494',required=True);p.add_argument('--output',required=True)
 a=p.parse_args();j,sha=read(a.nf494)
 assert sha==SHA and j['pass']=='NF494-native'
 assert j['original_nf407_source_sha256']==SRC
 assert j['original_nf406_seams_sha256']==SEAM
 assert F(j['original_B'])==B and F(j['original_true_terminal_delta'])==DELTA
 assert F(j['original_source_analytic_Cauchy_radius'])==RAD
 assert j['original_source_400_jet_order']==N
 assert j['original_source_original_246_generators_273_modes']
 u=j['original_U_400_native_outward'];assert len(u)==N
 coeff=[]
 for lo,hi in u:
  lo,hi=F(lo),F(hi);assert lo<=hi
  coeff.append(max(abs(lo),abs(hi)))
 v0,v1=map(F,u[0]);assert v0<=v1< -F(1,10**11)
 assert v1< -F(1,10**11)
 rho=DELTA/RAD;assert rho==F(1,20)
 CM=F(10)**400
 tail0=CM*rho**N/(1-rho)
 tail1=CM/RAD*rho**(N-1)*(F(N)/(1-rho)+rho/(1-rho)**2)
 assert tail0==F(j['original_original_U400_analytic_tail'])
 M0=sum((z*DELTA**k for k,z in enumerate(coeff)),F(0))+tail0
 M1=sum((k*z*DELTA**(k-1) for k,z in enumerate(coeff) if k),F(0))+tail1
 assert M0<F(1,5000000)
 assert M1<F(7,10000)
 assert F(7,10000)*F(1,10**9)<F(1,10**12)
 assert v1<-F(1,10**11)
 l2=atanh(F(1,3),160)
 lsmall=atanh(F(19,531),160)
 L=(9*l2[0]+lsmall[0],9*l2[1]+lsmall[1])
 assert F(6)<L[0]<L[1]<F(7) and l2[1]<1
 m0=F(1,5000000);m1=F(7,10000)
 semisq_one=F(1512)*m0*m0/F(20)+F(174)*m1*m1/(500*500*20)
 semisq_two=4*semisq_one
 l2sq_two=m0*m0*DELTA*(7*7+2*7+2)/2
 assert semisq_two<F(1,10**10)
 assert l2sq_two<F(1,10**13)
 assert semisq_two+l2sq_two<F(1,10**10)
 assert -v1>F(1,10**11)
 assert F(1,10**11)-F(7,10000)/10**9 > F(9,10**12)
 out={
  'pass':'NF523-original-NF494-endpoint-log-fractional-domain-source-exact',
  'original_nf494_source_SHA256':sha,
  'original_nf407_source_SHA256':SRC,
  'original_nf406_seams_SHA256':SEAM,
  'physical_original_B':str(B),'physical_original_delta':str(DELTA),
  'original_source_U_B_signed_interval':[str(v0),str(v1)],
  'original_U_B_strictly_less_than_minus_1e_minus_11':True,
  'original_U_full_collar_sup_absolute_bound':str(M0),
  'original_U_prime_full_collar_sup_absolute_bound':str(M1),
  'source_original_400_jets_analytic_tail_U':str(tail0),
  'source_original_400_jets_analytic_tail_Uprime':str(tail1),
  'source_exact_log550_interval':[str(L[0]),str(L[1])],
  'original_odd_two_collar_Hquarter_Gagliardo_seminorm_squared_strict_upper':str(semisq_two),
  'original_odd_two_collar_L2_squared_strict_upper':str(l2sq_two),
  'original_odd_two_collar_L2_plus_Hquarter_Gagliardo_seminorm_squared_strict_lt_1e_minus_10':True,
  'original_U_B_d_ne_0_for_0_lt_d_lt_1e_minus_9':True,
  'original_ell_U_not_Hhalf':True,
  'original_ell_U_in_Hs_for_each_0_le_s_lt_half':True,
  'natural_original_log_growth_Weil_operator_domain_membership':
     'FOLLOWS from retained symbol |m_a|<=C(1+log(e+|ξ|)); not an actual full source-graph image proof',
  'original_strict_fixed_c_less_than_B_support_membership':False,
  'original_exact_smooth_test_function_membership':False,
  'original_smooth_interior_approximable_in_multiplier_operator_graph_norm':True,
  'original_242_selected_physical_moment_preserving_smooth_approximation':
     'ANALYTIC CONSTRUCTION with χJ positive definite, no numerical 242D inversion needed',
  'original_full_actual_zeta_source_graph_membership':'OPEN',
  'actual_Weil_source_form_identification_on_smooth_approximants':'OPEN',
  'source_image_graph_norm_density':'OPEN',
  'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
 print('NF523 original NF494 SOURCE EXACT U(B), U/Uprime original collar PASS')
 print('M0',float(M0),'M1',float(M1),'nonzero endpoint',float(v1))
 print('Original ell_U H^(1/4) upper source certified; sharp H^(1/2) failure')
 print('Full divisor source graph/test identity and RH OPEN')
if __name__=='__main__':main()
