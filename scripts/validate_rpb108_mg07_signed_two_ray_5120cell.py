#!/usr/bin/env python3
"""NF: whole-real genuine original signed odd form on MG07 source-stop rays.

Certifies Q_o(f)=<f,(Ao-Kminus-2ss*)f> via exact original m(ξ):
  2∫_[0,12] m(ξ)|T_f(ξ)|² dξ - 2|<f,s>|²
  - a fully-paid possible negative Kminus action on |ξ|>12.
The positive Ao action in the tail is discarded (nonnegative).
No SI29/PSD or RH claim. This is original signed operator data, not
the source-only MG07 sufficient-method inequality.

Uses the inherited SI06/SM43A all-real multiplier curvature <2300,
original true SI42 Fourier endpoint intervals, and SI08 certified
original Kminus total L1 mass <38. Low-band m is smooth: NO κ kink.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from validate_rpb108_si06_negative_band import B,PI
from validate_rpb108_si12_even_supported_inverse import sinh_bounds,cosh_bounds
from validate_rpb108_si14_odd_multiband_nogo import cos_sin_pi_multiple
from validate_rpb108_si08_multiband_rank import cover
from validate_rpb108_sm43_positive_affine_error import LOWARCH
from validate_rpb108_mg07_two_source_original_physical_pole_input import (
  CENTER,RAYS,evaluate as physical_anchor,add,scl,mul)
from validate_rpb108_mg07_two_source_endpoint_log_tail import (
  PI_LO,PI_UP,abs_upper)
from validate_rpb108_mg07_two_source_original_low32_affine_stop import (
  D2,below,above,signed_m_at,qbasis,qinterval,cell_affine_exact_lower,
  hyperbolic_interval)
from validate_rpb108_mg07_original_low12_960cell_stop import (
  exact_original_J_membership)
ROOT=Path(__file__).resolve().parents[1]
CUT=F(12)
CURVE=F(2300)
REGIONS=(
  (F(0),F(1),F(1,4096)),
  (F(1),F(2),F(1,256)),
  (F(2),F(4),F(1,128)),
  (F(4),CUT,F(1,64)),
)

def certified_negative_high12_mass_and_packets():
  """Analytic exact Fourier packet isolation removes huge 2-IBP bound.

  For k=2*pi*xi and omega=2*pi*c,
     Tu = [-2k sin(omega B) cos(kB)+2omega cos(omega B) sin(kB)]
           /(k²-omega²)
     Ts = [-2k sinh(B/2) cos(kB)+cosh(B/2) sin(kB)]
           /(k²+1/4).
  Rearrange around the CANCELLING physical f(B) and f'(B).
  For xi>=12, k|Tf| has a rational upper independent of xi.
  """
  assert CUT==12 and CENTER==F(37,64)
  assert PI[0]>PI_LO and PI[1]<PI_UP
  clusters,mass=cover()
  assert len(clusters)==107 and mass<F(38)
  sn,cs=cos_sin_pi_multiple(2*B*CENTER)
  sh=sinh_bounds(B/2)
  ch=cosh_bounds(B/2)
  omega=(2*PI[0]*CENTER,2*PI[1]*CENTER)
  wup=2*PI_UP*CENTER
  kmin=2*PI_LO*CUT
  assert kmin>wup
  denom=kmin*kmin-wup*wup
  data=[]
  for a,b,label in RAYS:
    ep=above(abs_upper(add(scl(a,sn),scl(b,sh))),10**12)
    der=above(abs_upper(add(scl(a,mul(omega,cs)),scl(F(b,2),ch))),10**12)
    n1=F(a)*abs_upper(sn)*wup*wup+F(b)*sh[1]/4
    n2=F(a)*wup*abs_upper(cs)*wup*wup+F(b)*ch[1]/8
    # |k T| <= 2ep+2der/kmin+2n1/denom+2n2/(kmin*denom)
    # since k>=kmin and |sin/cos kB|<=1.
    beta=above((ep+der/kmin+n1/denom+n2/(kmin*denom))/PI_LO,10**9)
    assert beta>0
    upper=above(mass*(beta/CUT)**2,10**6)
    data.append({
      'ray':label,'endpoint_upper':str(ep),'derivative_upper':str(der),
      'true_Fourier_xi_times_amplitude_upper_high12':str(beta),
      'full_original_Knegative_L1_mass_upper':str(mass),
      'true_signed_high12_negative_action_upper':str(upper),
      'beta_display':float(beta),
      'negative_tail_display':float(upper)})
  return data

def verify():
  membership=exact_original_J_membership()
  assert membership['original_SM35_J_source_dim']==470
  assert D2<900 and LOWARCH<1400 and D2+LOWARCH<CURVE
  tail=certified_negative_high12_mass_and_packets()
  physical=physical_anchor()
  sh=hyperbolic_interval(B/2,'sinh')
  ch=hyperbolic_interval(B/2,'cosh')
  second=[
    above(4*PI[1]**2*(F(a)*2*B**3/3+F(b)*2*B**3/3*sh.h))
    for a,b,_ in RAYS]
  running=[F(0) for _ in RAYS]
  blocks=[[F(0) for _ in RAYS] for _ in REGIONS]
  count=0
  for ri,(left,right,h) in enumerate(REGIONS):
    n=int((right-left)/h)
    assert left+n*h==right
    for j in range(n):
      l=left+j*h;r=l+h;mid=(l+r)/2
      ivl=signed_m_at(l);ivr=signed_m_at(r)
      u=(ivl[0]+ivl[1])/2
      v=(ivr[0]+ivr[1])/2
      m0=(u+v)/2
      m1=(v-u)/h
      eps=above(max((ivl[1]-ivl[0])/2,(ivr[1]-ivr[0])/2)
                +CURVE*h*h/8)
      basis=qbasis(mid,sh,ch)
      for k,(aa,bb,_) in enumerate(RAYS):
        T,Tp=qinterval(basis,aa,bb)
        amp=(T[0]+T[1])/2
        deriv=(Tp[0]+Tp[1])/2
        E=above((T[1]-T[0])/2+(Tp[1]-Tp[0])*h/4
                 +second[k]*h*h/8)
        low=below(2*cell_affine_exact_lower(
          m0,m1,amp,deriv,h,eps,E),10**6)
        blocks[ri][k]+=low
        running[k]+=low
      count+=1
  assert count==4096+256+256+512==5120
  out=[]
  for i,(a,b,label) in enumerate(RAYS):
    assert physical['rays'][i]['purpose']==label==tail[i]['ray']
    pole_hi=F(physical['rays'][i][
      'genuine_Astar_pole_subtraction_2overlap_squared_interval'][1])
    high_hi=F(tail[i]['true_signed_high12_negative_action_upper'])
    signed_lower=running[i]-pole_hi-high_hi
    out.append({
      'ray':label,
      'signed_low0_12_original_multiplier_lower':str(running[i]),
      'genuine_original_pole_payment_upper':str(pole_hi),
      'signed_high12_negative_action_upper':str(high_hi),
      'complete_original_signed_Q_odd_lower':str(signed_lower),
      'strict_original_Q_odd_positive':signed_lower>0,
      'display_lower':float(signed_lower)})
  record={
    'status':'EXACT_ORIGINAL_SIGNED_STOPPING_RAY_5120CELL_CERTIFICATE'
           if all(z['strict_original_Q_odd_positive'] for z in out)
           else 'HONEST_INCONCLUSIVE_ORIGINAL_SIGNED_RAYS',
    'exact_original_J_membership':membership,
    'original_signed_multiplier_all_seven_prime_powers':True,
    'original_quarter_digamma_source':True,
    'global_multiplier_curvature_upper':str(CURVE),
    'entire_whole_real_Knegative_high12_paid':True,
    'signed_frequency_cells':count,
    'frequency_regions':[
      {'from':str(l),'to':str(r),'width':str(h),
       'ray_signed_lower_contributions':
        {RAYS[k][2]:str(blocks[i][k]) for k in range(len(RAYS))}}
      for i,(l,r,h) in enumerate(REGIONS)],
    'true_rays':out,'high_negative_tail':tail,
    'signed_odd_operator_positive_ON_ALL_HILBERT_SPACE':'OPEN',
    'SI29_augmented_Ritz':'OPEN',
    'even_CC27_Weil_RH':'OPEN'
  }
  return record

if __name__=='__main__':
  result=verify()
  p=ROOT/'artifacts/mg07_original_signed_two_ray_5120cell.json'
  p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text(json.dumps(result,indent=2)+'\n')
  print('Original full signed Wodd two-ray exact lower:',
        [(r['ray'],r['display_lower']) for r in result['true_rays']],
        'status',result['status'],flush=True)
  # Inconclusive is a valid diagnostic, not an accepted false positivity.
  # The CI independently checks strict positivity before marking acceptance.
