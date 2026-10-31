#!/usr/bin/env python3
"""NF405 ORIGINAL source-tail boundary-principal-part extraction.

For unchanged u4, the true odd sine transform has
T_u(xi)=-u4(B) cos(2*pi*B*xi)/(pi*xi)+R_u(xi).
Certifies m*R_u over |xi|>2^24 with original NF375 sine / NF374
derivative curvature and supported pole. Leading term MUST be kept
as an actual function in a future physical centered integral;
this is not a certified full multiplier norm.
"""
import argparse,hashlib,json,math,re,sys
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path
from nf375_cutoff_reduction import calc,CAP_A,CAP_D,CAP_K,upward,NATIVE_SHA
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);HALF=B/2
ORIGINAL_NF375='03c709571046d3f09307614aaded9749f5a15ba1'
ORIGINAL_NF401='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
BALL=re.compile(r'^\[([^ ]+) \+/- ([^\]]+)\]$')
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest(),hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
def ball(s):
 m=BALL.fullmatch(str(s));assert m is not None
 a,r=map(lambda q:F(Decimal(q)),m.groups())
 assert r>=0
 return a-r,a+r
def sinh_bounds(N=80):
 t=sum((HALF**(2*k+1)/math.factorial(2*k+1) for k in range(N)),F(0))
 q=HALF**(2*N+1)/math.factorial(2*N+1)
 rat=HALF*HALF/F((2*N+2)*(2*N+3))
 assert F(0)<rat<F(1,4)
 return t,t+q/(1-rat)
def run(p):
 nf375,sha375,git375=read(p.nf375)
 nf374,sha374,_=read(p.nf374)
 center,center_sha,_=read(p.center)
 projection,n401,_=read(p.nf401)
 assert git375==ORIGINAL_NF375
 assert sha374==NATIVE_SHA
 assert nf375['native_report_sha256']==sha374
 assert projection['original_242D_multiplier_column_scalar_contraction_pass'] is True
 assert n401==center['original_nf401_selected_native_sha256']==ORIGINAL_NF401
 assert nf374['native_parent_physical_quotient_overlap_pass'] is True
 assert nf375['measured_original_lowband'] is False
 assert center['actual_original_full_supported_centered_scalar_integrated'] is False
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in (nf375,nf374,center,projection))
 jet=nf374['boundary_jets'][3];cur=nf374['nf374_curvature'][3]
 assert jet['direction']==cur['direction']==nf375['directions'][3]['direction']==4
 assert upward(jet['w_endpoint_abs_upper'])<CAP_A[3]
 assert upward(jet['w_derivative_abs_upper'])<CAP_D[3]
 assert upward(cur['K_integral_abs_upper'])<CAP_K[3]
 row=nf375['directions'][3]
 a1,a3,b=[F(row[k]) for k in ('signed_original_first_sine_moment','original_sine_absolute_cubic_moment','original_sinh_coefficient')]
 assert b<0 and a3>0
 whole,parts,Js=calc(24,a1,a3,b,CAP_A[3],CAP_D[3],CAP_K[3])
 j2,j4,j8=Js
 assert whole==F(row['dyadic_cutoff_options'][4]['highband_upper'])
 # The first-order *endpoint jump* is removed as one common signed
 # function of frequency, before any abs-value majorant.
 # The sine source's endpoint is exactly zero for original 5n/11.
 shlo,shhi=sinh_bounds()
 wl=ball(jet['w_endpoint_interval'][0])[0]
 wh=ball(jet['w_endpoint_interval'][1])[1]
 assert 0<wl<wh<CAP_A[3]
 # u4(B)=b*sinh(B/2)-w4(B), where u4=f_(Te4)-w4,
 # and the original sine frequency grid vanishes at x=B.
 ulo=b*shhi-wh
 uhi=b*shlo-wl
 assert ulo<=uhi<0
 # Pointwise upper on the remainder's original true Fourier
 # sine transform times the complete signed multiplier, both signs:
 # source sine A1/xi^2 + A3/xi^4, sinh derivative, matched w'
 # and w'' all included in the SAME residual tail.
 sine=abs(a1)*j4/6+a3*j8/6
 pole_rem=abs(b)*j4/12
 matched_rem=(CAP_D[3]+CAP_K[3])*j4/18
 rem=sine+pole_rem+matched_rem
 assert rem>0
 assert rem < F(1,10**16)
 # The first-order endpoint principal part retained separately has
 # ||m*leading|| <= |u4(B)|/3 * sqrt(J2) (pi>3).
 leading_cap=max(abs(ulo),abs(uhi))*j2/3
 assert 0<leading_cap and leading_cap+rem>=whole*F(1,2)
 # NF404 source-verified centered power target. The corrected physical
 # low-frequency FUNCTION v_L(x)+endpoint_principal_part(x)-a*s(x)
 # must be integrated on I, not on R and not using the tail alone.
 E0=F(center['original_selected_after_pole_shear_power_lower_exact'])
 E1=F(center['original_selected_after_pole_shear_power_upper_exact'])
 gamma2=F(center['exact_source_original_full_complement_power_budget'])
 Rcap=F(332,10**13);delta=gamma2/2
 assert E1+delta<Rcap**2
 fee=delta+2*Rcap*rem+rem**2+E1-E0
 assert fee<gamma2
 out={
  'pass':'NF405','standing':'ORIGINAL SOURCE ENDPOINT-EXTRACTED MULTIPLIER HIGHBAND REMAINDER CERTIFIED; PHYSICAL INTEGRAL OPEN',
  'nf375_source_blob':git375,'nf374_native_sha256':sha374,
  'nf404_centering_sha256':center_sha,'nf401_selected_native_sha256':n401,
  'source_original_fourth_cutoff':2**24,
  'original_source_sinh_coefficient':str(b),
  'original_matched_exterior_endpoint_interval':[str(wl),str(wh)],
  'original_actual_matched_u4_endpoint_interval':[str(ulo),str(uhi)],
  'source_original_higher_sine_remainder_tail':str(sine),
  'source_original_pole_derivative_remainder_tail':str(pole_rem),
  'source_original_matched_exterior_derivative_curvature_tail':str(matched_rem),
  'source_original_complete_signed_endpoint_extracted_L2_remainder_upper':str(rem),
  'source_original_endpoint_principal_part_L2_upper':str(leading_cap),
  'original_unchanged_nf375_whole_highband_upper':str(whole),
  'original_half_budget_delta':str(delta),
  'original_source_centered_norm_cross_fee':str(2*Rcap*rem+rem*rem),
  'original_source_exact_half_budget_with_endpoint_extraction_pass':True,
  'source_original_endpoint_principal_part_formula':'T_lead(xi)=-u4(B) cos(2*pi*(11/10)*xi)/(pi*xi) for |xi|>2^24, multiplied by original signed m(xi)',
  'future_physical_positive_integrand':'|1_I [inverse_fourier_lowband(m*uhat4)+inverse_fourier_endpoint_principal_tail(m*T_lead)-a*sinh(x/2)]|^2',
  'full_signed_original_endpoint_principal_part_physically_evaluated':False,
  'original_full_supported_centered_scalar_measured':False,
  'original_lowband_J_perp_upper_measured':False,
  'new_signed_kernel_cells':0,'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dest=Path(p.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF405 source-tail original H24:',float(whole))
 print('NF405 source-tail matched first-order endpoint residual:',float(rem))
 print('NF405 half-budget residual fee compatible at existing 2^24: PASS')
 print('NF405 physical leading tail and whole centered energy UNMEASURED')
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name,d in [('nf374','NF374_original_correlated_curvature_native.json'),('nf375','NF375_reduced_cutoff_exact.json'),('center','NF404_original_selected_pole_shear_exact.json'),('nf401','NF401_original_242D_selected_column_source_native.json')]:
  p.add_argument('--'+name,default='notes/data/provisional/'+d)
 p.add_argument('--output',required=True)
 run(p.parse_args())
