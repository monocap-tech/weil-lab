"""RC330 — first certified ORIGINAL signed four-mode high Ritz response.

Extend CC27/RC313 original native even high compression from
{244,246,248} to {244,246,248,250}. Pin and reuse the six entire
C3 rational intervals (RC326) and all 3 native C250,m intervals
(RC329), including their true log/translation/regular/pole budgets.
Compute the missing original C250,250 diagonal from all seven
signed native Legendre prime translation overlaps and the exact
endpoint/scalar, with rigorous shift/support/weight intervals.

Establish an original high C4 strictly positive matrix via
Gershgorin (in addition to Sylvester 4th determinant).
Construct a rational native four-coordinate Ritz response to
RC323's x=(3/25)v0-(23/8)w2+w4 from the complete signed
b244,b246,b248,b250, retaining pinned native error intervals.

Compare its certified gain against the BEST POSSIBLE original
three-mode inverse gain, using the exact finite Schur inverse
variational identity:
   Delta3_max = Delta3(yold)
                + (b3-C3*yold)^T C3^-1 (b3-C3*yold)
          <= Delta3(yold)+||b3-C3*yold||² / lambda_min(C3).
The entire three-mode residual norm and lambda_min are pinned
RC326. A strict 4>3 bound proves the adverse omitted n250
source is actually useful after including that mode in the trial.

The new Y4 whole-infinite high residual is paid conservatively
using ||Tx|| and ||C|| ||Y4||; it need NOT beat the signed RC328
three-mode full residual. A finite Ritz improvement certifies
only an UPPER Schur bound, not the full signed C^-1 nor a
positive 3-dimensional low Schur/Stage I/RH theorem.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from math import isqrt
from fractions import Fraction as F
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc324_high_tail_smoothing as rc324
import validate_rpb108_rc325_native_high_2x2 as rc325
import validate_rpb108_rc326_native_high_3x3_residual as rc326

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
N=(244,246,248,250)
OLD=N[:3]
OUT=10**27
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc322_low_3d_gram.json":"ba344b44436c5c2d392a9feb5c6dc0c9892dfe88",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686",
 "certificates/rpb108_rc325_native_high_2x2.json":"27f42ff30438613e335f39e232c8ac0329f1d854",
 "certificates/rpb108_rc326_native_high_3x3_residual.json":"62a7c8fe549ed4b0d1aec799e1d4f1402ea02e06",
 "certificates/rpb108_rc328_signed_finite_tail_residual.json":"49d9daf11defd0f272865d3780f3a53d0af6e130",
 "certificates/rpb108_rc329_native_outside_covariance.json":"a43070d94934660418144cdcdd84d86b88dbf101",
}
def dn(x,g=OUT):return F(x.numerator*g//x.denominator,g)
def up(x,g=OUT):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def rlo(x,g=10**37):
 assert x>=0
 if not x:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k,g)
def rhi(x,g=10**37):
 assert x>=0
 if not x:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+1,g)
def blob(raw):return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
IV=rc325.IV
def absmax(x):return max(abs(x.l),abs(x.h))
def gram_interval(row):return IV(*map(F,row))

def native_original_prime_250_diagonal(rows,reverse=False):
 p=rc325.legendre(250)
 center=F(0)
 fault=F(0)
 for r in (list(reversed(rows)) if reverse else rows):
  L=r["el"]/B;U=r["eu"]/B
  d=rc325.nearest((L+U)/2)
  assert 0<L<=U<2 and 0<d<2
  I=rc325.overlap(p,p,d)
  # |d/dd int P250(t)P250(t+d)| <= 1+250*251:
  # include moving zero-extension boundary and real log.
  delta=max(abs(d-L),abs(U-d))
  fault+=r["ch"]*(1+250*251)*delta+2*r["cradius"]
  center-=r["c"]*I
 return IV(dn(center-fault),up(center+fault))

def all_four_det(A):
 # 4x4 Laplace minors exactly with rational intervals.
 def determinant(rows):
  n=len(rows)
  if n==1:return rows[0][0]
  return sum((((-1)**j)*rows[0][j]*
    determinant([r[:j]+r[j+1:] for r in rows[1:]])
       for j in range(n)),IV(0))
 return determinant(A)

def run(reverse=False):
 documents={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert blob(raw)==pin,("upstream input changed",p)
  documents[p]=json.loads(raw)
 def cert(k):return documents["certificates/rpb108_rc"+k+".json"]
 c326=cert("326_native_high_3x3_residual")
 c329=cert("329_native_outside_covariance")
 c328=cert("328_signed_finite_tail_residual")
 c324=cert("324_high_tail_smoothing")
 assert c326["native_original_high_3x3_strictly_positive"]
 assert c329["certified_strict_negative_original_degree250_covariance"]
 assert c328["proved_strict_sharpening_of_complete_original_signed_residual"]
 mat={}
 for k,v in c326["original_high_3x3_C_intervals"].items():
  i,j=map(int,k.split("_"));mat[i,j]=gram_interval(v)
 for m,v in c329["original_high_native_C_250_vs_244_246_248_intervals"].items():
  mat[int(m),250]=gram_interval(v)
 assert len(mat)==9
 rows=rc318.source_info()
 prim250=native_original_prime_250_diagonal(rows,reverse)
 met=cert("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 gamma=cert("322_low_3d_gram")["refined_Euler_Maclaurin_gamma"]
 cLo,cHi=rc324.scalar_original(gamma)
 h=rc324.Htable(500)
 n=250
 endpoint=2*(h[2*n]-h[n])+F(1,2*n+1)
 reg=F(c324["original_high_regular_operator_norm_bound_244plus"])
 pole=F(100)*B*(B/2)**(2*n)
 phys=((IV(h[n]+endpoint)+IV(cLo,cHi))/F(2*n+1)
       +prim250+IV(-reg,reg)+IV(0,pole/F(2*n+1)))
 factor=IV(2*n+1)/IV(h[n]+slo,h[n]+shi)
 q=phys*factor
 mat[250,250]=IV(dn(q.l),up(q.h))
 assert len(mat)==10
 C=[[mat[min(i,j),max(i,j)] for j in N] for i in N]
 # Strict 4-dimensional Loewner: actual original
 # interval Gershgorin verifies all row lower margins.
 rowfloors=[
  C[i][i].l-sum((absmax(C[i][j]) for j in range(4) if j!=i),F(0))
  for i in range(4)]
 gmin=min(rowfloors)
 assert gmin>F(1,4),("full original signed high 4x4 Gershgorin floor")
 oldDet=F(c326["native_original_high_3x3_determinant_lower"])
 assert oldDet>0
 det4=all_four_det(C)
 assert det4.l>0,("original signed high 4x4 determinant")
 b={}
 oldb=cert("325_native_high_2x2")[
     "low_R323_witness_native_high_response"]
 for n in N[:2]:b[n]=gram_interval(oldb[str(n)])
 b[248]=gram_interval(c326["low_witness_high_248_signed_source_interval"])
 b[250]=gram_interval(c329["original_joint_signed_b_250_interval"])
 assert all(b[n].l*b[n].h>0 for n in N)
 oldY=list(map(F,c326["explicit_original_high_3mode_Ritz_trial"]))
 oldC=C[:3]
 oldResponse=b
 # Best 3-mode gain <= gain(y_old)+residual^2/lambda_min.
 # Use the EXACT original interval 3x3 and signed source,
 # NOT the weak RC326 approximate gain lower alone.
 gain3=2*sum((oldY[i]*oldResponse[N[i]] for i in range(3)),IV(0))
 for i in range(3):
  for j in range(i,3):
   gain3-=(2 if i!=j else 1)*oldY[i]*oldY[j]*oldC[i][j]
 residual3=F(c326["explicit_represented_3mode_residual_norm_upper"])
 lambda3=F(c326["native_original_high_3x3_Gershgorin_floor_lower"])
 assert lambda3>0
 best3Upper=up(gain3.h+residual3**2/lambda3)
 # Actual 4-mode rational trial midpoint inverse, verified
 # by exact rational interval arithmetic after rounding.
 center=[[F((C[i][j].l+C[i][j].h)/2) for j in range(4)]
        for i in range(4)]
 bcenter=[(b[n].l+b[n].h)/2 for n in N]
 y=rc326.inverse_rational(center,bcenter)
 assert len(y)==4
 gain4=2*sum((y[i]*b[N[i]] for i in range(4)),IV(0))
 for i in range(4):
  for j in range(i,4):
   gain4-=(2 if i!=j else 1)*y[i]*y[j]*C[i][j]
 assert gain4.l>0
 strict=dn(gain4.l-best3Upper)
 assert strict>F(1,10**12),(
   "native four-mode signed Ritz must beat optimal 3-mode")
 represented=[]
 for i in range(4):
  R=b[N[i]]-sum((C[i][j]*y[j] for j in range(4)),IV(0))
  represented.append(R)
 representedNorm=up(rhi(sum((absmax(v)**2 for v in represented),F(0))))
 # Whole infinite ORIGINAL high residual is paid:
 # ||P_high Tx|| rigorously inherited RC328; high action
 # of Y is bounded using the original native ||N0|| upper.
 T=F(c328["original_combined_true_entire_high_Tx_norm_upper"])
 globalC=F(c326["original_full_D_to_D_N0_operator_norm_upper"])
 ynorm=up(rhi(sum((v*v for v in y),F(0))))
 Yaction=up(globalC*ynorm)
 totalR=up(T+Yaction)
 mu=F(c324["inherited_even_244plus_global_floor"])
 penalty=up(totalR**2/mu)
 assert representedNorm<totalR
 low=F(cert("323_coercivity_nogo")["original_low_quadratic_B_upper"])
 originalSchurUpper=up(low-gain4.l)
 # Do not pretend Y4 has the independently paid RC328
 # Y3 residual: retain separate original high-vector data.
 return dict(
  milestone="RC330",
  parent_route_head="f5b1f41d3c5fb8147a7db277a166cbb4463f3abe",
  pinned_upstream_git_blobs=PINS,
  original_CC27_signed_Weil_D_operator=True,
  original_native_high_degrees=list(N),
  new_signed_prime_250_diagonal_overlap_count=7,
  complete_original_prime_real_log_shift_errors_paid=True,
  original_native_signed_prime_250_diagonal_interval=prim250.out(),
  original_native_high_C_4x4_intervals={
   f"{i}_{j}":mat[i,j].out() for i in N for j in N if j>=i},
  original_high_4x4_leading_3x3_determinant_lower=str(oldDet),
  original_high_4x4_determinant_lower=str(dn(det4.l)),
  original_high_4x4_all_row_Gershgorin_floor_lower=str(dn(gmin)),
  original_high_4x4_strictly_positive=True,
  original_signed_low_witness_high_b250_interval=b[250].out(),
  original_signed_low_witness_high_4_source_intervals={
   str(i):b[i].out() for i in N},
  prior_exact_rational_three_mode_trial=[str(v) for v in oldY],
  prior_three_mode_Ritz_gain_upper=str(up(gain3.h)),
  prior_optimal_original_three_mode_Ritz_gain_upper=str(best3Upper),
  original_new_rational_four_mode_Ritz_trial=[str(v) for v in y],
  original_new_four_mode_Ritz_gain_lower=str(dn(gain4.l)),
  strict_four_mode_gain_over_optimal_prior_three_mode_lower=str(strict),
  new_original_full_Schur_witness_Ritz_upper=str(originalSchurUpper),
  new_four_mode_represented_residual_norm_upper=str(representedNorm),
  new_four_mode_full_infinite_high_T_source_norm_upper=str(T),
  new_four_mode_full_infinite_C_Y_action_norm_upper=str(Yaction),
  new_four_mode_entire_infinite_residual_norm_upper=str(totalR),
  new_four_mode_entire_high_residual_penalty_upper=str(penalty),
  four_mode_finite_Ritz_yields_only_Schur_UPPER=True,
  full_original_C_inverse_computed=False,
  full_three_dimensional_low_Schur_positive=False,
  full_278_high_head_positivity=False,
  full_rank317_original_Schur_positive=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
   "RC331: calculate signed original C250-to-252+ high source "
   "and use the certified 4-mode Ritz Y to improve its "
   "full infinite residual with native cross-to-rest action, "
   "without substituting a finite Ritz upper bound for "
   "full three-dimensional Schur lower positivity."
  )
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 args=p.parse_args()
 result=run(reverse=args.replay)
 if args.replay:
  assert result==json.loads(args.output.read_text(encoding="utf-8"))
 else:
  args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC330: ORIGINAL signed high 4x4 positive; rational 4mode Ritz beats OPTIMAL 3mode. Full high inverse and Stage I OPEN.")
