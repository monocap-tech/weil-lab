"""RC334: original signed five-coordinate high Ritz repair of adverse n254.

Original CC27/RC313 Weil D-Riesz operator. Pin native RC330 original
four-block, RC333 C254,m and b254, compute original C254254 from
seven rational Legendre translation overlaps with all original
coefficient, log and support uncertainties plus endpoint/scalar,
regular/pole and D input/output factors.

Prove positive original C5 by all-row Gershgorin; calculate a rational
five-mode Ritz trial. Compare its gain to OPTIMAL four-mode response
using a rigorous finite residual correction for the old Y4 and its
positive C4 floor. A finite Ritz gain proves only a full Schur UPPER
along one low witness, never full low Schur positive LOWER.

Do not transport RC331-333 whole-space residual onto the changed
Y5. All infinite high outputs are instead paid by the native global
operator bound; sharper Y5 source-sensitive coupling is RC335.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc324_high_tail_smoothing as rc324
import validate_rpb108_rc325_native_high_2x2 as rc325
import validate_rpb108_rc326_native_high_3x3_residual as rc326

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
OLD=(244,246,248,250)
N=OLD+(254,)
NEW=254
G=10**27
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc322_low_3d_gram.json":"ba344b44436c5c2d392a9feb5c6dc0c9892dfe88",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686",
 "certificates/rpb108_rc326_native_high_3x3_residual.json":"62a7c8fe549ed4b0d1aec799e1d4f1402ea02e06",
 "certificates/rpb108_rc328_signed_finite_tail_residual.json":"49d9daf11defd0f272865d3780f3a53d0af6e130",
 "certificates/rpb108_rc330_original_high_four_ritz.json":"671d56538a0f70df1fab8ca840c1a47797bef56b",
 "certificates/rpb108_rc332_signed_252_covariance.json":"b6d1931ff2b9e6675577ca8cda253b9b940f8875",
 "certificates/rpb108_rc333_signed_254_cumulative.json":"b57a9d2e9f42cc642bfb5d52d6b6cb2bb46dbb19",
}
IV=rc325.IV
def down(x,g=G):return F(x.numerator*g//x.denominator,g)
def up(x,g=G):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def rhi(x,g=10**37):
 assert x>=0
 if not x:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+1,g)
def hashblob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def absmax(z):return max(abs(z.l),abs(z.h))
def interval(ar):return IV(*map(F,ar))

def new_prime_diagonal(rows,reverse=False):
 p=rc325.legendre(NEW)
 center=F(0);fault=F(0)
 for r in (list(reversed(rows)) if reverse else rows):
  lo,hi=r["el"]/B,r["eu"]/B
  d=rc325.nearest((lo+hi)/2)
  assert 0<lo<=hi<2 and 0<d<2
  exact=rc325.overlap(p,p,d)
  shift=max(abs(d-lo),abs(hi-d))
  fault+=r["ch"]*(1+NEW*(NEW+1))*shift+2*r["cradius"]
  center-=r["c"]*exact
 return IV(down(center-fault),up(center+fault))

def run(reverse=False):
 docs={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert hashblob(raw)==pin,("upstream blob drift",p)
  docs[p]=json.loads(raw)
 def cert(k):return docs["certificates/rpb108_rc"+k+".json"]
 c330=cert("330_original_high_four_ritz")
 c333=cert("333_signed_254_cumulative")
 c332=cert("332_signed_252_covariance")
 c324=cert("324_high_tail_smoothing")
 c326=cert("326_native_high_3x3_residual")
 assert c330["original_high_4x4_strictly_positive"]
 assert c333["original_degree254_covariance_strictly_negative"]
 assert c333["strict_cumulative_residual_improvement_over_RC332"]
 assert c332["degree252_original_covariance_strictly_positive"]
 assert not c330["full_original_C_inverse_computed"]
 # Pin full ORIGINAL signed C4, not a diagonal surrogate.
 cells={}
 for k,ar in c330["original_native_high_C_4x4_intervals"].items():
  a,b=map(int,k.split("_"));cells[a,b]=interval(ar)
 assert len(cells)==10
 for m,ar in c333["exact_native_original_signed_C_254_high_intervals"].items():
  cells[int(m),NEW]=interval(ar)
 assert len(cells)==14
 met=cert("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<slo<=shi<5
 gamma=cert("322_low_3d_gram")["refined_Euler_Maclaurin_gamma"]
 cLo,cHi=rc324.scalar_original(gamma)
 h=rc324.Htable(2*NEW)
 rows=rc318.source_info()
 assert len(rows)==7
 prime=new_prime_diagonal(rows,reverse)
 reg=F(c324["original_high_regular_operator_norm_bound_244plus"])
 pole=100*B*(B/2)**(2*NEW)
 endpoint=2*(h[2*NEW]-h[NEW])+F(1,2*NEW+1)
 phys=(IV(h[NEW]+endpoint)+IV(cLo,cHi))/F(2*NEW+1)
 phys+=prime+IV(-reg,reg)+IV(0,pole/F(2*NEW+1))
 factor=IV(2*NEW+1)/IV(h[NEW]+slo,h[NEW]+shi)
 diag=phys*factor
 cells[NEW,NEW]=IV(down(diag.l),up(diag.h))
 assert len(cells)==15
 C=[[cells[min(a,b),max(a,b)] for b in N] for a in N]
 floors=[C[i][i].l-sum((absmax(C[i][j]) for j in range(5) if j!=i),F(0))
         for i in range(5)]
 floor5=min(floors)
 assert floor5>F(1,5),("five-mode ORIGINAL high block Gershgorin positivity")
 b={int(m):interval(ar) for m,ar in
       c330["original_signed_low_witness_high_4_source_intervals"].items()}
 b[NEW]=interval(c333["exact_original_signed_b254_interval"])
 assert len(b)==5 and all(b[k].l*b[k].h>0 for k in N)
 Y4=list(map(F,c330["original_new_rational_four_mode_Ritz_trial"]))
 assert len(Y4)==4
 # Rigorous best-four Ritz gain <= gain(Y4) + ||b4-C4Y4||²/lambda4.
 # This upper must be compared against the NEW signed gain lower.
 gain4=2*sum((Y4[i]*b[N[i]] for i in range(4)),IV(0))
 for i in range(4):
  for j in range(i,4):
   gain4-=(2 if i!=j else 1)*Y4[i]*Y4[j]*C[i][j]
 oldResidual=F(c330["new_four_mode_represented_residual_norm_upper"])
 lambda4=F(c330["original_high_4x4_all_row_Gershgorin_floor_lower"])
 assert lambda4>F(1,4) and oldResidual>0
 best4Upper=up(gain4.h+oldResidual**2/lambda4)
 assert best4Upper>F(c330["original_new_four_mode_Ritz_gain_lower"])
 # Actual ORIGINAL five-coordinate native midpoint Ritz vector, exact rational.
 centers=[[(C[i][j].l+C[i][j].h)/2 for j in range(5)] for i in range(5)]
 source=[(b[n].l+b[n].h)/2 for n in N]
 Y5=rc326.inverse_rational(centers,source)
 assert len(Y5)==5 and Y5[4]>0
 gain5=2*sum((Y5[i]*b[N[i]] for i in range(5)),IV(0))
 for i in range(5):
  for j in range(i,5):
   gain5-=(2 if i!=j else 1)*Y5[i]*Y5[j]*C[i][j]
 assert gain5.l>0
 diff=down(gain5.l-best4Upper)
 assert diff>F(1,10**10),("new 5-mode gain does not exceed optimal 4-mode")
 # Original represented residual check; not transferred to infinity.
 represent=[b[N[i]]-sum((C[i][j]*Y5[j] for j in range(5)),IV(0))
            for i in range(5)]
 represented=up(rhi(sum((absmax(q)**2 for q in represent),F(0))))
 # Conservative NEW Y5 whole original-infinite high residual:
 # RC328 source norm and RC326 whole original C high norm.
 # RC333's improved Y4 full residual cannot be reused for Y5.
 T=F(cert("328_signed_finite_tail_residual")[
  "original_combined_true_entire_high_Tx_norm_upper"])
 globalC=F(c326["original_full_D_to_D_N0_operator_norm_upper"])
 yNorm=up(rhi(sum((q*q for q in Y5),F(0))))
 CYbound=up(globalC*yNorm)
 R=up(T+CYbound)
 mu=F(c324["inherited_even_244plus_global_floor"])
 penalty=up(R**2/mu)
 assert represented<R and R<F(1,100)
 assert penalty>F(cert("323_coercivity_nogo")["original_low_quadratic_B_upper"])
 print("RC334_EXACT_INTERVAL_DIAGNOSTICS_BEGIN",flush=True)
 print(json.dumps({
  "new_original_prime_C254254_diagonal":prime.out(),
  "new_original_C254254_diagonal":cells[NEW,NEW].out(),
  "original_five_high_row_gershgorin_floor_lower":str(down(floor5)),
  "original_old_Y4_gain_interval":gain4.out(),
  "optimal_original_four_mode_Ritz_gain_upper":str(best4Upper),
  "new_original_five_mode_rational_trial":[str(q) for q in Y5],
  "new_original_five_mode_Ritz_gain_interval":gain5.out(),
  "strict_original_five_vs_optimal_four_gain_lower":str(diff),
  "new_original_represented_five_residual_norm_upper":str(represented),
  "new_original_infinite_Y5_residual_norm_upper":str(R),
  "new_original_infinite_Y5_penalty_upper":str(penalty),
  "old_RC333_Y4_infinite_residual_norm_upper":
   c333["selected_original_entire_high_residual_norm_upper"],
 },sort_keys=True),flush=True)
 print("RC334_EXACT_INTERVAL_DIAGNOSTICS_END",flush=True)
 return dict(
  milestone="RC334",
  parent_route_head="472088bcfd39fa374b9fed2d0c960d976ef5af48",
  pinned_original_upstream_git_blobs=PINS,
  original_CC27_signed_Weil_D_operator=True,
  original_native_high_degrees=list(N),
  new_original_prime_diagonal_exact_legendre_overlap_count=7,
  original_prime_real_log_support_weight_errors_paid=True,
  original_endpoint_scalar_regular_even_pole_paid=True,
  original_high_five_mode_strictly_positive=True,
  original_high_5x5_Gershgorin_floor_strictly_above_one_fifth=True,
  five_mode_gain_strictly_above_optimal_four=True,
  new_five_mode_residual_includes_entire_infinite_high_space=True,
  original_RC333_four_mode_infinite_bound_not_transported=True,
  full_original_C_inverse_computed=False,
  full_three_dimensional_low_Schur_positive=False,
  full_278_high_head_positivity=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
   "RC335: recover native 5-mode-to-omitted 252 and 256+ cross action "
   "with actual signed C252,254 and signed original b252, plus whole "
   "infinite residual on the NEW Y5; do not borrow RC333 Y4 residual "
   "or mistake finite high Ritz Schur upper for global low Schur lower."
  )
 )

if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",type=Path,required=True)
 ap.add_argument("--replay",action="store_true")
 args=ap.parse_args()
 d=run(reverse=args.replay)
 if args.replay:assert d==json.loads(args.output.read_text(encoding="utf-8"))
 else:args.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC334: ORIGINAL signed native 5-mode C strictly positive; five Ritz beats OPTIMAL four. Full C inverse and Stage I OPEN.")
