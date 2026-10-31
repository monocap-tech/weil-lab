#!/usr/bin/env python3
"""NF417: full ORIGINAL 246-generator signed/regularized z at hotspot cell 3 or 7.

Generalizes verified NF415 I1 and NF416 symmetric I0 analytic polynomial
integrators without modifying source, prime signs, support, or NF404 center.
Recomputes all rigorous I0/I1 source, kernel and coefficient-radius bounds
for the exact *new* original physical x and integration limits.
Zero Gauss quadrature. True pointwise only; no cellwide scalar claim.
"""
import argparse, json, math, sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb, ctx
import nf415_original_cell6_I1_correlated_taylor_native as n415
import nf416_original_cell6_full_I0_regularized_taylor as n416
from nf415_original_cell6_I1_validated_acb import read,native_source,U,A,C
if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
B=F(11,10)
POINTS={3:F(7,20),7:F(26,25)}
def certify(cell,source,nf413,nf414,parent_source_sha):
 x=POINTS[cell]
 t1=2*(B-x)
 t2=2*(B+x)
 assert t1>n416.TAU
 assert (t1-n416.TAU)/n416.STEP==int((t1-n416.TAU)/n416.STEP)
 assert (t2-t1)/n415.STEP==int((t2-t1)/n415.STEP)
 assert t1>0 and t2<=F(22,5)
 assert nf414["hotspot_points"][[3,6,7].index(cell)]["rational_physical_x"]==str(x)
 n416.X=x;n416.T=t1
 n415.X=x;n415.LEFT=t1;n415.RIGHT=t2
 terms,pole,S0=native_source(source)
 grouped={}
 for f,k,q in terms:grouped.setdefault(f,[]).append((k,q))
 grouped=sorted(grouped.items())
 assert len(terms)>=240
 assert max(k for f,vals in grouped for k,v in vals)<=13
 fmax=max(f for f,vs in grouped)
 assert F(882)<fmax<F(883)
 assert max(F(7)*abs(f)*n416.TAU/2 for f,vs in grouped)<62
 assert max(F(7)*abs(f)*n416.RHO_S for f,vs in grouped)<16
 Uraw=sum((abs(q)*B**k for f,k,q in terms),abs(pole))
 assert Uraw<F(10)**160
 pi=arb.pi()
 src=U(source)
 ux=src.at(C(x)).real
 # Original I0 true physical domain [0, t1] with 2 pieces.
 # Exactly same source-tail lemma as NF416, independent of x.
 Rs=F(8*3**62)*Uraw*F(62)**(n416.NS_TINY-13+1)/math.factorial(n416.NS_TINY-13+1)
 RH=F(6)*n416.TAU**(n416.NH+1)/(1-n416.TAU)
 E_small=F(6)*Rs/(n416.NS_TINY+1)+n416.TAU*F(6)*RH
 assert Rs<F(1,10**60) and RH<F(1,10**100) and E_small<F(1,10**60)
 I0tiny=n416.tiny_analytic_integral(grouped,pole,pi,ux)
 # For t in [tau,t1], center>=.025, analytic K disk <=81 and
 # ratio 2rho/.025 <= 2/5. Real K<=2/tau=100.
 Rsource=F(3**16)*Uraw*F(16)**(n416.NS-13+1)/math.factorial(n416.NS-13+1)
 RK0=F(81)*F(2,5)**(n416.NK+1)/F(3,5)
 assert Rsource<F(1,10**42) and RK0<F(1,10**60)
 E0_regular=(t1-n416.TAU)*(100*Rsource+RK0*(F(1030)+Rsource))
 assert E0_regular<F(1,10**38)
 p0=int((t1-n416.TAU)/n416.STEP)
 I0regular=arb(0)
 for j in range(p0):
  mid=n416.TAU+(2*j+1)*n416.RHO
  I0regular+=n416.large_panel(mid,grouped,pole,pi,ux)
  if (j+1)%40==0 or j+1==p0:
   print('NF417 cell',cell,'original I0 panel',j+1,'/',p0,flush=True)
 # Correct 0<t<t1 ORIGINAL source difference error is controlled by
 # full physical NF413 derivative coefficient radii; not S0/t.
 S2=F(nf413['native_second_derivative_source_coefficient_radii_uniform_exact'])
 assert S2<F(1,10**735)
 E0_coeff=S2*t1*t1/8
 E0=E_small+E0_regular+E0_coeff
 raw0=n415.enclosed(I0tiny+I0regular,95)
 i0=[F(raw0[0])-E0,F(raw0[1])+E0]
 assert i0[0]<i0[1] and i0[1]-i0[0]<F(1,10**40)
 # Original I1 true physical domain [2(B-x),2(B+x)], x-dependent;
 # SAME selected+critical source but separate one-sided physical kernel.
 # For complex Taylor disk |t-mid|<=mid/2, Re(t)>=t1/2.
 # K bound |K|<1+2/t1<81 for both new t1 (.12,1.5).
 eta=2*n415.RHO/t1
 assert 0<eta<F(1,10)
 RK1=F(81)*eta**(n415.NK+1)/(1-eta)
 Kreal=F(2)/t1
 E1=(t2-t1)*(Kreal*Rsource+RK1*(F(520)+Rsource))
 assert E1<F(1,10**39),('actual I1 tail unresolved',str(E1)[:120])
 # Every source-uncertain translated value <=S0 and |K|<2/t;
 # since 1/2 [δu(x)-δu(x-t/2)] <= S0, use rational
 # ∫2/t <=2*(t2/t1-1) (ln y <=y-1).
 E1_coeff=2*(t2/t1-1)*S0
 p1=int((t2-t1)/n415.STEP)
 I1=arb(0)
 for j in range(p1):
  mid=t1+(2*j+1)*n415.RHO
  I1+=n415.panel(mid,grouped,pole,ux,pi)
  if (j+1)%60==0 or j+1==p1:
   print('NF417 cell',cell,'original I1 panel',j+1,'/',p1,flush=True)
 raw1=n415.enclosed(I1,95)
 i1=[F(raw1[0])-E1-E1_coeff,F(raw1[1])+E1+E1_coeff]
 assert i1[0]<i1[1] and i1[1]-i1[0]<F(1,10**39)
 # NF414 finite piece includes complete seven true signed prime powers
 # with exact original C0 seam branches and original centered coefficient.
 original_nf414=nf414['hotspot_points'][[3,6,7].index(cell)]
 finite=original_nf414['original_z_finite_known_part_source_paid_rational_interval']
 Z=[F(finite[0])+i0[0]+i1[0], F(finite[1])+i0[1]+i1[1]]
 assert Z[1]-Z[0]<F(1,10**38) and Z[0]<Z[1]
 return {
  "cell":cell,"x":str(x),"original_B":"11/10",
  "original_I0_true_t_interval":["0",str(t1)],
  "original_I1_true_t_interval":[str(t1),str(t2)],
  "full_original_242_selected_4_critical_physical_source":True,
  "original_prime_signed_all_7_from_NF414":True,
  "original_t0_singularity_removed_by_H":True,
  "original_I0_symmetric_both_shifts":True,
  "original_I1_true_one_sided_source":True,
  "source_tiny_order":n416.NS_TINY,"H_tiny_order":n416.NH,
  "source_regular_order":n416.NS,"I0_regular_kernel_order":n416.NK,
  "I1_kernel_order":n415.NK,
  "I0_regular_panels":p0,"I1_panels":p1,
  "exact_original_max_frequency":str(fmax),
  "original_raw_source_triangle_U":str(Uraw),
  "original_coefficient_source_S0":str(S0),
  "original_coefficient_source_second_derivative_S2":str(S2),
  "I0_tiny_source_tail":str(Rs),"I0_tiny_H_tail":str(RH),
  "I0_tiny_integrated_error":str(E_small),
  "I0_regular_source_tail":str(Rsource),
  "I0_regular_kernel_tail":str(RK0),
  "I0_regular_integrated_error":str(E0_regular),
  "I0_source_native_coefficient_error":str(E0_coeff),
  "I0_total_error":str(E0),
  "original_true_I0_outward_rational_interval":[str(x) for x in i0],
  "original_true_I0_width_exact":str(i0[1]-i0[0]),
  "I1_kernel_complex_disk_ratio":str(eta),
  "I1_kernel_tail":str(RK1),
  "I1_source_tail":str(Rsource),
  "I1_integrated_error":str(E1),
  "I1_source_native_coefficient_error":str(E1_coeff),
  "original_true_I1_outward_rational_interval":[str(x) for x in i1],
  "original_true_I1_width_exact":str(i1[1]-i1[0]),
  "original_NF414_finite_z_known_outward_rational_interval":finite,
  "original_true_complete_z_pointwise_rational_interval":[str(x) for x in Z],
  "original_true_complete_z_pointwise_width_exact":str(Z[1]-Z[0]),
  "true_original_complete_z_pointwise_certified":True,
  "entire_original_cell_z_certified":False,
  "original_NF404_whole_scalar_certified":False,
  "original_W_ODD_NEG":"OPEN","RH":"OPEN"
 }
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--cell',type=int,required=True,choices=[3,7])
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 ap.add_argument('--precision',type=int,default=1024)
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 s,ssha=read(a.source); g,gsha=read(a.nf413); f,fsha=read(a.nf414)
 assert ssha==g['original_nf407_full_native_source_sha256']==f['original_nf407_source_sha256']
 assert g['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in [s,g,f])
 ctx.prec=a.precision
 out=certify(a.cell,s,g,f,ssha)
 out.update({"pass":"NF417","standing":"FULL ORIGINAL 242+4 PHYSICAL z POINTWISE NATIVE INTERVAL ONLY, ORIGINAL ALL EIGHT CELLWISE NORM AND RH OPEN",
   "nf407_original_source_sha256":ssha,"nf413_curvature_sha256":gsha,
   "nf414_seven_signed_prime_finite_sha256":fsha,
   "native_precision_bits":a.precision,
   "complete_original_source_one_sided_cellwide_z_certified":False,
   "original_nf410_signed_principal_z_cross_certified":False,
   "original_nf404_complete_centered_scalar_certified":False,
   "original_J242_perp_lowband":"OPEN","operator_domain":"OPEN",
   "infinite_inverse":"OPEN","W_ODD_NEG":"OPEN"})
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+"\n")
 print("NF417 original 246-source complete z point",a.cell,POINTS[a.cell], "interval enclosure SUCCESS",flush=True)
 print("NF417 I0",str(out['original_true_I0_outward_rational_interval'][0])[:120],flush=True)
 print("NF417 I1",str(out['original_true_I1_outward_rational_interval'][0])[:120],flush=True)
 print("NF417 full physical z point, cellwide and NF404 scalar OPEN",flush=True)
if __name__=="__main__":main()
