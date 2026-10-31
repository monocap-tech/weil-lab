#!/usr/bin/env python3
"""NF423 simultaneous true ORIGINAL source-correlated z^(0..3)(9/10).

One physical 38+360 t-panel sweep builds all FOUR derivatives from the SAME
source u Taylor jets and the SAME kernel moment weights; no repeating the
original 398 t integrals separately for each derivative. Exact NF422 all-order
moving physical arch transfer, NF421 corrected odd endpoint sign, original
242 selected+4 critical source and seven true signed prime branches.

The source Taylor and kernel tails, source-radius uncertainties and t=0
removable pole are bounded by exact rationals. Independent parents NF416,
NF419 and NF421 must overlap; n=3 is newly evaluated. This is a jet at ONE
physical x0, not a cellwise Chebyshev certificate or NF404 scalar.
"""
import argparse,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
import nf416_original_cell6_full_I0_regularized_taylor as old416
import nf415_original_cell6_I1_correlated_taylor_native as old415
from nf415_original_cell6_I1_validated_acb import read,native_source,A,C
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10);T1=F(2,5);T2=F(4)
MAX=3;NS=300;N0=530;NH=60;NK0=160;NK1=48
TAU=F(1,50);STEP=F(1,100);RHO=F(1,200)
POLE=F(6677356497477490213,4611686018427387904)
WEIGHTS={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
def derivcoef(js,n,q):
 v=js[n+q]
 for k in range(1,q+1):v=v*(n+k)
 return v
def moment_weights(ker,degree):
 # ∫_{-rho}^{rho} K(t0+s) s^n ds with analytic K Taylor.
 rp=[arb(1)]
 rho=A(RHO)
 for j in range(degree+len(ker)+2):rp.append(rp[-1]*rho)
 w=[]
 for n in range(degree+1):
  w.append(sum((ker[k]*2*rp[n+k+1]/(n+k+1) for k in range(len(ker)) if (n+k)%2==0),arb(0)))
 return w
def small_all(js):
 # Exact zero-removable H=tK derivative moments, shared n-moment
 # weights across all source derivative orders.
 H=old416.H_series_at_zero()
 tau=A(TAU);powers=[arb(1)]
 for i in range(N0+NH+2):powers.append(powers[-1]*tau)
 result=[arb(0) for _ in range(MAX+1)]
 for n in range(2,N0+1,2):
  weight=sum((A(q)*powers[n+j]/(n+j) for j,q in enumerate(H)),arb(0))
  for order in range(MAX+1):
   result[order]+=-derivcoef(js,n,order)*weight/(2**n)
 return result
def panel_all(t0,side,groups,pole,pi,ux):
 # Physical original panel midpoint t0. The source Taylor at each
 # translated location is computed ONCE to order NS+MAX.
 assert side in ('I0','I1')
 minus=old416.original_jets(X-t0/2,groups,pole,pi,NS+MAX)
 plus=(old416.original_jets(X+t0/2,groups,pole,pi,NS+MAX) if side=='I0' else None)
 ker=old416.K_series_at(t0) if side=='I0' else old415.kernel_jets(t0)
 assert len(ker)==(NK0+1 if side=='I0' else NK1+1)
 weights=moment_weights(ker,NS)
 ans=[arb(0) for _ in range(MAX+1)]
 fp=arb(1);fm=arb(1)
 for n in range(NS+1):
  if n:fp/=2;fm/=(-2)
  for q in range(MAX+1):
   v=(ux[q] if n==0 else arb(0))
   vm=derivcoef(minus,n,q)*fm
   if side=='I0':
    vp=derivcoef(plus,n,q)*fp
    D=v-(vp+vm)/2
   else:D=(v-vm)/2
   ans[q]+=weights[n]*D
 return ans
def source_at_and_derivatives(y,grouped,pole,pi):
 # Native real Arb source point y can include actual log(n) shift.
 z=[arb(0) for _ in range(MAX+1)]
 for f,terms in grouped:
  iw=acb(arb(0),2*pi*A(f))
  phase=(iw*C(y)).exp()
  for k,q in terms:
   for n in range(MAX+1):
    s=acb(0)
    falling=1
    for j in range(min(n,k)+1):
     if j:falling*=k-j+1
     s+=A(q*math.comb(n,j)*falling)*A(y)**(k-j)*(iw**(n-j))*phase
    z[n]+=s.imag if k%2==0 else s.real
 for n in range(MAX+1):
  z[n]+=A(pole)/(2**n)*((C(y)/2).sinh().real if n%2==0 else (C(y)/2).cosh().real)
 return z
def kvals(t):
 r=(-t).exp();k=(-t/4).exp()/(1-r)
 l=-arb(1)/4-r/(1-r)
 return [k,k*l,k*(l*l+r/(1-r)**2)]
def interval_enclose(v,ep,digits=76):
 # Full exact outward Arb enclosure + exact rational analytic errors.
 m,r,e=v.mid_rad_10exp(digits)
 t=F(10)**int(e)
 return [F(int(m)-int(r))*t-ep,F(int(m)+int(r))*t+ep]
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 p.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 p.add_argument('--nf416',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 p.add_argument('--nf419',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 p.add_argument('--nf421',default='notes/data/provisional/NF421_original_cell6_complete_second_xjet_native.json')
 p.add_argument('--nf422',default='notes/data/provisional/NF422_original_all_order_arch_transfer_exact.json')
 p.add_argument('--output',required=True)
 p.add_argument('--precision',type=int,default=1024)
 a=p.parse_args()
 source,sha=read(a.source);g,gsha=read(a.nf413)
 finite,fsha=read(a.nf414);z0,zsha=read(a.nf416)
 z1,zh1=read(a.nf419);z2,zh2=read(a.nf421);transfer,th=read(a.nf422)
 assert source['original_dimension']==242
 assert len(source['original_selected_generator_node_orders'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert g['original_nf407_full_native_source_sha256']==sha
 assert finite['original_nf407_source_sha256']==sha
 assert z0['original_nf407_source_sha256']==z1['original_nf407_source_sha256']==z2['original_source_sha256']==sha
 assert transfer['original_nf407_source_sha256']==sha
 assert transfer['all_original_orders_1_through_12_inductively_replayed_exact_fraction']
 assert transfer['NF421_original_analytic_third_identity_as_written_needs_correction']
 assert transfer['NF421_original_conservative_third_derivative_numerical_upper_preserved']
 assert g['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert z0['complete_original_z_pointwise_certified'] and z1['first_order_original_x_jet_certified'] and z2['original_true_pointwise_second_x_jet_certified']
 assert all(j['W_ODD_NEG']==j['RH']=='OPEN' for j in (source,g,finite,z0,z1,z2,transfer))
 ctx.prec=a.precision
 terms,pole,S0=native_source(source)
 assert len(terms)>=240 and S0<F(1,10**700)
 grouped={}
 for f,k,q in terms:grouped.setdefault(f,[]).append((k,q))
 grouped=sorted(grouped.items())
 assert all(k<=13 for f,vs in grouped for k,v in vs)
 assert F(882)<max(f for f,vs in grouped)<F(883)
 Uraw=sum((abs(v)*B**k for f,k,v in terms),abs(pole))
 assert Uraw<10**160
 # Source analytic point-independent derivative remainder envelope:
 # derivative order<=3 adds <=10^12 to original native degree-530
 # t=0 Taylor tail and degree-300 regular panel tail.
 Rs=F(8*3**62)*Uraw*F(62)**518/math.factorial(518)
 Rr=F(3**16)*Uraw*F(16)**288/math.factorial(288)
 R3s=10**12*Rs;R3r=10**12*Rr
 RH=6*TAU**(NH+1)/(1-TAU)
 # True |D_t u'''| <= ||u''''||2 sqrt(t) conservatively
 # after Cauchy-Schwarz, NF421 ||u''''||2<16384.
 E0small=6*R3s/531+F(10**5)*RH
 RK0=81*F(2,5)**161/F(3,5)
 E0large=(T1-TAU)*(100*R3r+RK0*(50000+R3r))
 RK1=81*(STEP/T1)**49/(1-STEP/T1)
 E1=(T2-T1)*(5*R3r+RK1*(50000+R3r))
 S2=F(g['native_second_derivative_source_coefficient_radii_uniform_exact'])
 S5=10**20*S0
 Ecos=S5*T1*T1/8+20*(10**12*S0)+10**26*S0
 E=E0small+E0large+E1+Ecos
 assert E0small<F(1,10**20) and E0large<F(1,10**20)
 assert E1<F(1,10**20) and E<F(1,10**19)
 pi=arb.pi()
 source_x=old416.original_jets(X,grouped,pole,pi,N0+MAX)
 ux=[derivcoef(source_x,0,n) for n in range(MAX+1)]
 end=old416.original_jets(B,grouped,pole,pi,MAX)
 v=[derivcoef(end,0,n) for n in range(MAX+1)]
 I0=small_all(source_x)
 I1=[arb(0) for _ in range(MAX+1)]
 n0=int((T1-TAU)/STEP);n1=int((T2-T1)/STEP)
 assert (n0,n1)==(38,360)
 for j in range(n0):
  t0=TAU+(2*j+1)*RHO
  w=panel_all(t0,'I0',grouped,pole,pi,ux)
  for n in range(MAX+1):I0[n]+=w[n]
  if (j+1)%10==0 or j==n0-1:print('NF423 shared original source I0 panel',j+1,'/',n0,flush=True)
 for j in range(n1):
  t0=T1+(2*j+1)*RHO
  w=panel_all(t0,'I1',grouped,pole,pi,ux)
  for n in range(MAX+1):I1[n]+=w[n]
  if (j+1)%60==0:print('NF423 shared original source I1 panel',j+1,'/',n1,flush=True)
 x=A(X);d=A(B-X);t1=A(T1);t2=A(T2)
 phi=((d/A(B))*(d/4).cosh()/(d/4).sinh()).log()+2*((-d/2).exp()).atan()
 J2=2*((-t2/4).exp().atanh()+(-t2/4).exp().atan())
 c=(arb(1)/4).digamma()-pi.log()+(J2+phi)/2
 L=(A(B)/d).log();AA=c+L/2
 k1,k2=kvals(t1),kvals(t2)
 assert abs(AA)<16
 arch=[];primes=[];centers=[];full=[]
 branches=finite['hotspot_points'][1]['all_seven_true_prime_branches']
 assert [z['n'] for z in branches]==list(WEIGHTS)
 assert [z['branch'] for z in branches]==[z['branch'] for z in z1['original_all_seven_signed_prime_derivative_branches']]
 assert [z['branch'] for z in branches]==[z['branch'] for z in z2['original_seven_signed_prime_derivative_branches']]
 for n in range(MAX+1):
  archpart=AA*ux[n]+I0[n]+I1[n]
  if n==0:archpart-=v[0]*L/2
  else:
   for j in range(n):
    m=n-1-j
    archpart+=v[j]*((-2)**m*k1[m]+(-1)**j*2**m*k2[m])
   archpart-=v[0]*math.factorial(n-1)/(2*d**n)
  arch.append(archpart)
  pvalue=arb(0)
  for (nprime,base),b in zip(WEIGHTS.items(),branches):
   h=arb(nprime).log();w=arb(base).log()/arb(nprime).sqrt()
   seam=abs(A(B)-h)
   assert x<seam or x>seam
   if h<A(B) and x<seam:
    assert b['branch']=='both'
    q=source_at_and_derivatives(x+h,grouped,pole,pi)[n]+source_at_and_derivatives(x-h,grouped,pole,pi)[n]
   elif h>A(B) and x<seam:
    assert b['branch']=='neither'
    q=arb(0)
   else:
    assert b['branch']=='post-seam'
    q=source_at_and_derivatives(x-h,grouped,pole,pi)[n]
    if n==0:q+=v[0]
   pvalue-=w*q
  primes.append(pvalue)
  center=-A(POLE)/(2**n)*((x/2).sinh() if n%2==0 else (x/2).cosh())
  centers.append(center)
  full.append(archpart+pvalue+center)
 bounds=[interval_enclose(z,E) for z in full]
 previous=[
 [F(x) for x in z0['original_true_full_z_cell6_at_x9over10_outward_interval']],
 [F(x) for x in z1['true_original_complete_zprime_at_9over10_outward_rational_interval']],
 [F(x) for x in z2['true_original_complete_zsecond_at_x9over10_outward_rational_interval']]]
 for n in range(3):
  assert bounds[n][0]<=previous[n][1] and previous[n][0]<=bounds[n][1],('previous original source derivative mismatch',n)
 assert bounds[3][0]<bounds[3][1]
 assert bounds[3][0]>-1540338 and bounds[3][1]<1540338
 assert all(hi-lo<F(1,10**18) for lo,hi in bounds)
 result={
 'pass':'NF423','standing':'ORIGINAL SOURCE-CORRELATED FOUR SIMULTANEOUS PHYSICAL RESPONSE JETS z^(0..3)(9/10) FROM SINGLE SHARED 398 PANEL SWEEP; NO FULL-CELL MODEL',
 'original_nf407_source_sha256':sha,'original_nf413_full_source_curvature_sha256':gsha,
 'original_nf414_finite_and_signed_primes_sha256':fsha,
 'original_nf416_complete_point_parent_sha256':zsha,
 'original_nf419_complete_first_jet_parent_sha256':zh1,
 'original_nf421_complete_second_jet_parent_sha256':zh2,
 'original_nf422_all_order_transfer_sha256':th,
 'original_source_242_selected_plus_four_critical_preserved':True,
 'original_all_seven_signed_prime_branches_preserved':True,
 'original_true_physical_x':'9/10','original_cell':6,
 'all_four_original_derivative_orders_computed_simultaneously':[0,1,2,3],
 'full_source_Taylor_each_rational_panel_evaluated_once_for_all_orders':True,
 'full_kernel_moment_weights_each_rational_panel_evaluated_once_for_all_orders':True,
 'full_original_shared_I0_panel_count':n0,
 'full_original_shared_I1_panel_count':n1,
 'original_full_source_t0_removal_H_tK':True,
 'original_corrected_NF422_parity_endpoint_transfer':True,
 'original_all_original_source_analytic_tails_paid_exactly':True,
 'original_shared_source_tiny_Taylor_order':N0,
 'original_shared_source_regular_Taylor_order':NS,
 'original_source_raw_triangle_exact':str(Uraw),
 'original_source_coefficient_radius_S0_exact':str(S0),
 'source_derivative_third_t0_tail_exact':str(R3s),
 'source_derivative_third_regular_tail_exact':str(R3r),
 'original_zero_t_analytic_source_tail_error_exact':str(E0small),
 'original_I0_regular_analytic_source_tail_error_exact':str(E0large),
 'original_I1_regular_analytic_source_tail_error_exact':str(E1),
 'original_true_source_coefficient_charge_exact':str(Ecos),
 'original_source_shared_response_per_order_integral_error_bound_exact':str(E),
 'original_true_full_response_z_derivatives_0_to_3_source_paid_rational_intervals':[[str(lo),str(hi)] for lo,hi in bounds],
 'original_previous_z0_zprime_zsecond_outward_intersections_checked':True,
 'original_true_zthird_point_certified':True,
 'original_entire_macro_0p899_to_0p901_x_Taylor_jet_coefficients_at_other_centers_certified':False,
 'original_entire_cell6_source_interpolation_model_certified':False,
 'original_NF410_signed_original_z_p_and_z2_integrated':False,
 'original_NF404_complete_centered_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+'\n')
 for n in range(4):print('NF423 original full response order',n,str(full[n])[:180],flush=True)
 print('NF423 original all lower jets independent native overlap and true zthird source-paid; complete x cell / NF404 OPEN',flush=True)
if __name__=='__main__':main()
