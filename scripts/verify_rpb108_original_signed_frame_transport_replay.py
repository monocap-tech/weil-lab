#!/usr/bin/env python3
"""Stdlib rational replay of error ledger; native frame rebuilt in producer."""
import hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dy(v):return F(int(v[0]))*F(2)**int(v[1])
z,b,r=map(lambda p:json.loads(Path(p).read_bytes()),sys.argv[1:4])
assert z['block_input_sha256']==sha(sys.argv[2])=='2cb869033f2c6722d356e769f35fc0e1b041ae46a8c11360e66cd7d2c694c548'
assert z['rank_input_sha256']==sha(sys.argv[3])=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
assert z['working_precision_bits']==4096 and z['flint_version']=='0.8.0'
assert z['retained_source_count']==len(b['rows'])==r['retained_physical_rank_upper']==242
assert z['critical_target_count']==4
err=list(map(F,z['physical_frame_error_row_upper']));assert len(err)==242 and min(err)>=0 and max(err)<F(1,100)
assert F(z['physical_frame_Gram_lower'])==1-F(1,100) and F(z['physical_frame_Gram_upper'])==1+F(1,100)
R=z['transported_independent_box_radius_intervals'];assert len(R)==242 and all(len(row)==4 for row in R)
assert all(0<=F(v[0])<=F(v[1]) for row in R for v in row)
i=z['worst_box_row'];t=z['worst_box_target'];assert 0<=i<242 and 0<=t<4
column=z['worst_box_exact_dyadic_frame_column'];assert len(column)==242
exact=sum((abs(dy(d))*dy(row['entries'][t]['signed_native'][1]) for d,row in zip(column,b['rows'])),F(0))
assert F(R[i][t][0])<=exact<=F(R[i][t][1]);assert F(z['worst_box_radius_lower'])==F(R[i][t][0])>10**30
assert F(z['worst_box_radius_lower'])==max(F(v[0]) for row in R for v in row)
E=z['frame_Frobenius_norm_power_two_exponent'];lo,hi=map(F,z['frame_Frobenius_norm_interval']);assert 0<lo<=hi<2**E
assert sum((dy(d)**2 for d in column),F(0))<=hi**2
q=z['diagnostic_transported_Frobenius_error_target_bits'];n=z['uniform_raw_entry_absolute_error_sufficient_bits'];assert q==80 and n==E+5+q
assert hi**2*968*F(2)**(-2*n)<F(2)**(-2*q)
assert z['diagnostic_budget_is_Schur_budget'] is False
S=z['physical_critical_quotient_Gram_intervals'];assert len(S)==4 and all(len(row)==4 for row in S)
for i in range(4):
 for j in range(4):
  l,h=map(F,S[i][j]);assert l<=h
  a,c=map(F,S[j][i]);assert max(l,a)<=min(h,c)
 assert F(S[i][i][0])>0
for k in ['physical_frame_verified','current_independent_raw_box_transport_inconclusive','quotient_diagonal_positive']:assert z[k] is True
for k in ['quotient_conditioning_certified','actual_analytic_correlated_error_lower_bound_claimed','precision_only_change_without_Laplace_tail_change_sufficient_claimed','full_selected_signed_matrix_computed','strong_complementary_coupling_computed','signed_Schur_certified']:assert z[k] is False
assert z['W_ODD_NEG']==z['inherited_original_domain_review']=='OPEN'
print('EXACT FRAME ERROR LEDGER REPLAY PASS; native Gram/transform certification is separate; W-ODD-NEG OPEN')
