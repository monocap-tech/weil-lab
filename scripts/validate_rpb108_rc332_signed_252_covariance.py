"""RC332: native signed first omitted n252 covariance for RC330's original Y4.

The CC27/RC313 original D-normalized signed high C is evaluated at
C[252,m], m=244,246,248,250, by 28 exact rational Legendre
translation integrals at rational centers, with actual log/support/
prime-weight errors, original logarithmic endpoint, complete RC324
regular kernel and signed even pole.

The original degree-252 low-to-high signed source is INDEPENDENTLY
reconstructed from the RC323 interval Legendre recurrence, endpoint
and original whole-source perturbation, not extrapolated from n250.
The actual signed four-mode covariance and residual are calculated.
All n>=254 original high outputs are retained in the residual through
RC331's rigorously established whole high-action bound and RC328's
signed source Parseval norm. Not a positive low Schur lower bound.

The committed certificate initially contains coarse safe caps; the
full exact output intervals are printed in a diagnostic line and can
be incorporated into a stricter certificate in a subsequent pass.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from math import isqrt
from fractions import Fraction as F
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc321_p4_boundary_native as rc321
import validate_rpb108_rc323_coercivity_nogo as rc323
import validate_rpb108_rc324_high_tail_smoothing as rc324
import validate_rpb108_rc325_native_high_2x2 as rc325

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
INPUT=(244,246,248,250)
OUT=252
ROUND=10**26
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686",
 "certificates/rpb108_rc328_signed_finite_tail_residual.json":"49d9daf11defd0f272865d3780f3a53d0af6e130",
 "certificates/rpb108_rc330_original_high_four_ritz.json":"671d56538a0f70df1fab8ca840c1a47797bef56b",
 "certificates/rpb108_rc331_native_four_interface.json":"f004126480c713639e1cdc930bd89759948d5714",
}
IV=rc325.IV
def dn(x,g=ROUND):return F(x.numerator*g//x.denominator,g)
def up(x,g=ROUND):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def root(x,upper=False,g=10**38):
 assert x>=0
 if x==0:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+int(upper),g)
def sha(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def absmin(iv):
 if iv.l<=0<=iv.h:return F(0)
 return min(abs(iv.l),abs(iv.h))
def absmax(iv):return max(abs(iv.l),abs(iv.h))
def parseiv(ar):return IV(*map(F,ar))
def source_at_252(rows,slo,shi,source_error,reverse=False):
 """Independent n252 counterpart of RC323's signed low-high rows."""
 n=OUT
 out=[rc323.IV(0),rc323.IV(0),rc323.IV(0)]
 for r in (list(reversed(rows)) if reverse else rows):
  z=r["z"];d=1-z;c=r["c"]
  polys=([F(1)],[(3*d*d-3)/2,3*d,F(3,2)],rc321.poly_shift_F(d))
  pv=rc323.P_intervals_at_center(z,rc323.STOP+6)
  mom=rc323.multiplication_moments(n,pv)
  for k,p in enumerate(polys):
   piece=sum((a*mom[j] for j,a in enumerate(p)),rc323.IV(0))
   out[k]=(out[k]-(2*n+1)*c*piece).grid(rc323.G)
 e=(F(2*n+1,n*(n+1)),
    F(6*(2*n+1),n*(n+1)*(n-2)*(n+3)),
    F(14*(2*n+1),(n-4)*(n+5)*(n-2)*(n+3)))
 roots=(rc323.IV(1)/rc323.IV(slo,shi).sqrt(),
        rc323.IV(5).sqrt()/rc323.IV(slo+F(3,2),shi+F(3,2)).sqrt(),
        rc323.IV(3)/rc323.IV(slo+F(25,12),shi+F(25,12)).sqrt())
 total=sum((rc323.VEC[k]*roots[k]*(out[k]+e[k])
            for k in range(3)),rc323.IV(0)).grid(rc323.G)
 h=rc324.Htable(n)
 den=IV((2*n+1)*(h[n]+slo),
        (2*n+1)*(h[n]+shi)).sqrt()
 value=parseiv(total.arr())/den
 # RC323 error bounds all original log/weight transport and
 # regular/pole high tails in actual D norm, hence one mode.
 return IV(dn(value.l-source_error),up(value.h+source_error))
def native_C252(rows,slo,shi,reg,reverse=False):
 """All four original signed native C252,m (not augmented)."""
 pol={n:rc325.legendre(n) for n in INPUT+(OUT,)}
 H=rc324.Htable(OUT)
 answer={}
 for m in (reversed(INPUT) if reverse else INPUT):
  center=F(0);error=F(0)
  for r in (list(reversed(rows)) if reverse else rows):
   lo,hi=r["el"]/B,r["eu"]/B
   d=rc325.nearest((lo+hi)/2)
   assert 0<lo<=hi<2 and 0<d<2
   overlap=rc325.overlap(pol[m],pol[OUT],d)
   shift=max(abs(d-lo),abs(hi-d))
   # Exact endpoint displacement and Markov/Leibniz error
   # from RC329, with the new highest output degree n252.
   error+=r["ch"]*(1+OUT*(OUT+1))*shift+2*r["cradius"]
   center-=r["c"]*overlap
  prime=IV(dn(center-error),up(center+error))
  endpoint=F(1,(OUT-m)*(OUT+m+1))
  physical=IV(endpoint)+prime+IV(-reg,reg)
  # Sign-indefinite original even pole is paid two-sided.
  pole=100*B*(B/2)**(OUT+m)
  physical+=IV(-pole,pole)/IV((2*m+1)*(2*OUT+1)).sqrt()
  dnorm=IV((2*m+1)*(2*OUT+1)).sqrt()/(
     IV(H[m]+slo,H[m]+shi)*IV(H[OUT]+slo,H[OUT]+shi)).sqrt()
  z=physical*dnorm
  answer[m]=IV(dn(z.l),up(z.h))
 return answer

def run(reverse=False):
 inputs={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert sha(raw)==pin,("upstream pin changed",p)
  inputs[p]=json.loads(raw)
 def cert(n):return inputs["certificates/rpb108_rc"+n+".json"]
 c330=cert("330_original_high_four_ritz")
 c331=cert("331_native_four_interface")
 c328=cert("328_signed_finite_tail_residual")
 c324=cert("324_high_tail_smoothing")
 c323=cert("323_coercivity_nogo")
 assert c330["original_high_4x4_strictly_positive"]
 assert c331["exact_original_endpoint_hilbert_schmidt_paid_through_infinity"]
 assert c331["original_four_mode_full_outside_CY_norm_less_than"]=="1/10000"
 met=cert("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<slo<=shi<5
 rows=rc318.source_info()
 assert len(rows)==7
 reg=F(c324["original_high_regular_operator_norm_bound_244plus"])
 assert 0<reg<F(1,1000)
 C=native_C252(rows,slo,shi,reg,reverse)
 assert len(C)==4
 original_source=source_at_252(
  rows,slo,shi,F(c323["complete_original_high_source_error_upper"]),reverse)
 y=list(map(F,c330["original_new_rational_four_mode_Ritz_trial"]))
 Cy=sum((C[m]*y[i] for i,m in enumerate(INPUT)),IV(0))
 Cy=IV(dn(Cy.l),up(Cy.h))
 covariance=original_source*Cy
 covariance=IV(dn(covariance.l),up(covariance.h))
 residual=original_source-Cy
 residual=IV(dn(residual.l),up(residual.h))
 assert absmax(original_source)<F(1,1000)
 assert absmax(Cy)<F(1,10000),("original action exceeds RC331 whole outside norm")
 assert absmax(residual)<F(1,1000)
 # Independently paid ORIGINAL complete source and high action.
 T=F(c328["original_combined_true_entire_high_Tx_norm_upper"])
 b=c330["original_signed_low_witness_high_4_source_intervals"]
 represented_energy=sum((absmin(parseiv(b[str(n)]))**2
                         for n in INPUT),F(0))
 assert 0<represented_energy<T*T
 Tout=root(T*T-represented_energy,True)
 Cout=F(c331["original_four_mode_full_outside_CY_norm_less_than"])
 Rin=F(c330["new_four_mode_represented_residual_norm_upper"])
 Rbase=up(root(Rin*Rin+(Tout+Cout)**2,True))
 # Orthogonal n252 signed split. The remaining 254+ modes
 # retain full original norm budgets, with squared known
 # energies removed only if their rigorous minima are nonzero.
 assert Tout**2>absmin(original_source)**2
 assert Cout**2>absmin(Cy)**2
 Trest=root(Tout*Tout-absmin(original_source)**2,True)
 Crest=root(Cout*Cout-absmin(Cy)**2,True)
 Rsplit=up(root(Rin*Rin+absmax(residual)**2+(Trest+Crest)**2,True))
 chosen=min(Rbase,Rsplit)
 mu=F(c324["inherited_even_244plus_global_floor"])
 penalty=up(chosen*chosen/mu)
 assert mu>0 and penalty<F(1,4000)
 assert chosen<F(3,2500)
 print("RC332_EXACT_INTERVAL_DIAGNOSTICS_BEGIN")
 print(json.dumps({
  "original_signed_C_252_cross":{str(m):C[m].out() for m in INPUT},
  "original_signed_b252_interval":original_source.out(),
  "original_four_mode_CY252_interval":Cy.out(),
  "original_signed_covariance_252_interval":covariance.out(),
  "original_signed_residual_252_interval":residual.out(),
  "baseline_infinite_residual_norm_bound":str(Rbase),
  "split_infinite_residual_norm_bound":str(Rsplit),
  "chosen_infinite_residual_norm_bound":str(chosen),
  "chosen_correct_sign_penalty_upper":str(penalty),
  "covariance_sign":("strict_positive" if covariance.l>0
     else "strict_negative" if covariance.h<0 else "undetermined"),
  "strict_residual_improvement_over_unsplit_bound":Rsplit<Rbase,
 },sort_keys=True),flush=True)
 print("RC332_EXACT_INTERVAL_DIAGNOSTICS_END",flush=True)
 return dict(
  milestone="RC332",
  parent_route_head="c62d6d2f7d37cab17586062ab9e60e1a2b7d4dbf",
  input_git_blob_pins=PINS,
  original_CC27_signed_Weil_D_operator=True,
  represented_even_high_degrees=list(INPUT),
  first_omitted_degree=OUT,
  original_signed_prime_integrals_28=True,
  original_prime_log_support_weight_errors_paid=True,
  native_original_endpoint_regular_pole_paid=True,
  independent_original_signed_source_252_rebuilt=True,
  original_signed_degree252_covariance_interval_evaluated=True,
  original_high_infinite_residual_254plus_paid=True,
  original_full_high_residual_norm_less_than="3/2500",
  original_correct_sign_penalty_less_than="1/4000",
  full_original_signed_C_inverse_computed=False,
  full_three_dimensional_low_Schur_positive=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor="RC333: certify and exploit the actual native signed covariance for omitted n254 onward, preserving the original infinite residual and strict distinction between Ritz Schur upper and full low Schur lower bounds."
 )
if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",type=Path,required=True)
 ap.add_argument("--replay",action="store_true")
 a=ap.parse_args()
 v=run(reverse=a.replay)
 if a.replay:assert v==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC332: original signed native degree252 cross and covariance calculated; full infinite residual paid; Stage I OPEN.")
