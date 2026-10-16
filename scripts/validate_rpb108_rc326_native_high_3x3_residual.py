"""RC326 — a genuine native signed high three-mode block, an improved
three-coordinate Ritz trial, and a FULL-SPACE PAID residual (coarse).

Original CC27 / RC313 even D-Riesz operator, no augmented proxy.
RC325's first 244/246 high block is reused byte-for-byte.
Compute the original native C[244,248], C[246,248], C[248,248]
using exact rational Legendre polynomial overlap, moving support
Lipschitz and coefficient intervals; reconstruct original signed
low-witness b248 independently with RC323 fixed-point recurrence.
Certify full 3x3 high block positive and strictly improved Ritz
reduction compared to OPTIMAL 244/246 finite inverse.

Crucially PAY the residual R=T x-C Y in the COMPLETE original high
carrier: explicit three represented modes and the infinite complement
using the original D->D operator norm and independently pinned
whole-source bounds on Tv0,Tw2,Tw4. The bound is conservative and
DOES NOT imply positive full 3D Schur. No actual C^{-1} claim.

Also explicitly pay coupling of the chosen Ritz vector into *all*
unrepresented modes including the n>=800 tail by ||C|| ||Y||.
This is a valid full tail-action upper but is not a sharp E norm,
a finite 278x278 head inverse, or complete Stage I.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc321_p4_boundary_native as rc321
import validate_rpb108_rc323_coercivity_nogo as rc323
import validate_rpb108_rc324_high_tail_smoothing as rc324
import validate_rpb108_rc325_native_high_2x2 as rc325

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
NEW=248
DEGREES=(244,246,248)
GRID=10**25
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc318_p0_signed_schur.json":"85dbc5bc373de9922bfe17a6d43ab2cef7178cd6",
 "certificates/rpb108_rc320_boundary_cancelled_schur.json":"fe8821aaba62ba50c2a8eba1a2fa0020ba818003",
 "certificates/rpb108_rc321_p4_boundary_native.json":"26eedd29ee80063c7b8ccc5f1d5de025e7050842",
 "certificates/rpb108_rc322_low_3d_gram.json":"ba344b44436c5c2d392a9feb5c6dc0c9892dfe88",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686",
 "certificates/rpb108_rc325_native_high_2x2.json":"27f42ff30438613e335f39e232c8ac0329f1d854",
}
IV=rc325.IV
def iv(x):return rc325.iv(x)
def dn(x):return rc325.dn(x,GRID)
def up(x):return rc325.up(x,GRID)
def sqrtup(x):return rc325.root(x,True)
def sqrtlo(x):return rc325.root(x,False)
def blob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def prime_new_pairs(rows,reverse=False):
 polys={n:rc325.legendre(n) for n in DEGREES}
 out={}
 for i,j in ((244,248),(246,248),(248,248)):
  center=F(0);err=F(0)
  for r in (list(reversed(rows)) if reverse else rows):
   a,b=r["el"]/B,r["eu"]/B
   d=rc325.nearest((a+b)/2)
   assert 0<a<=b<2 and 0<d<2
   overlap=rc325.overlap(polys[i],polys[j],d)
   # Leibniz and Markov: d Iij/dd bounded by
   # 1 + j(j+1). Both moved zero-extension boundaries
   # and the whole log interval are paid.
   delta=max(abs(a-d),abs(b-d))
   err+=r["ch"]*(1+j*(j+1))*delta+2*r["cradius"]
   center-=r["c"]*overlap
  out[i,j]=IV(dn(center-err),up(center+err))
 return out

def source_at_248(rows,slo,shi,full_source_error,reverse=False):
 h=rc324.Htable(NEW)
 n=NEW
 A=[rc323.IV(0),rc323.IV(0),rc323.IV(0)]
 for r in (list(reversed(rows)) if reverse else rows):
  z=r["z"];d=1-z
  polys=([F(1)],
    [(3*d*d-3)/2,3*d,F(3,2)],
    rc321.poly_shift_F(d))
  pvals=rc323.P_intervals_at_center(z,800)
  moments=rc323.multiplication_moments(n,pvals)
  for k,cs in enumerate(polys):
   val=sum((c*moments[j] for j,c in enumerate(cs)),rc323.IV(0))
   A[k]=(A[k]-(2*n+1)*r["c"]*val).grid(10**35)
 e0=F(2*n+1,n*(n+1))
 e2=F(6*(2*n+1),n*(n+1)*(n-2)*(n+3))
 e4=F(14*(2*n+1),(n-4)*(n+5)*(n-2)*(n+3))
 weights=[
   F(3,25)*(IV(1)/IV(slo,shi).sqrt()),
   -F(23,8)*(IV(5).sqrt()/IV(slo+F(3,2),shi+F(3,2)).sqrt()),
   IV(3)/IV(slo+F(25,12),shi+F(25,12)).sqrt(),
 ]
 amp=sum((weights[k]*(IV(A[k].lo,A[k].hi)+(e0,e2,e4)[k])
       for k in range(3)),IV(0))
 den=IV((2*n+1)*(h[n]+slo),(2*n+1)*(h[n]+shi)).sqrt()
 b=amp/den
 return IV(dn(b.l-full_source_error),up(b.h+full_source_error))

def native_C_new_pairs(prime,slo,shi,cLo,cHi,reg):
 h=rc324.Htable(2*NEW)
 out={}
 for i,j in ((244,248),(246,248),(248,248)):
  if i==j:
   endpoint=2*(h[2*i]-h[i])+F(1,2*i+1)
   term=(IV(h[i]+endpoint)+IV(cLo,cHi))/(2*i+1)
  else:
   term=IV(F(1,(j-i)*(i+j+1)))
  term+=prime[i,j]+IV(-reg,reg)
  pole=100*B*(B/2)**(i+j)
  if i==j:term+=IV(0,pole/F(2*i+1))
  else:term+=IV(-pole,pole)/IV((2*i+1)*(2*j+1)).sqrt()
  factor=IV((2*i+1)*(2*j+1)).sqrt()/(
    IV(h[i]+slo,h[i]+shi)*IV(h[j]+slo,h[j]+shi)).sqrt()
  q=term*factor
  out[i,j]=IV(dn(q.l),up(q.h))
 return out

def det3(a):
 x,y,z=a[0]
 _,w,v=a[1]
 _,_,q=a[2]
 return x*w*q+2*y*z*v-x*v*v-w*z*z-q*y*y

def inverse_rational(mat,vec):
 # Gauss-Jordan pivot exact rational with no floating point.
 n=len(mat)
 a=[[F(x) for x in row]+[vec[i]] for i,row in enumerate(mat)]
 for i in range(n):
  pivot=a[i][i]
  assert pivot>0
  for j in range(i,n+1):a[i][j]/=pivot
  for k in range(n):
   if k==i:continue
   factor=a[k][i]
   for j in range(i,n+1):a[k][j]-=factor*a[i][j]
 return [rc325.nearest(a[i][-1],10**16) for i in range(n)]

def run(reverse=False):
 docs={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert blob(raw)==pin,("upstream certificate blob changed",p)
  docs[p]=json.loads(raw)
 def cert(n):return docs["certificates/rpb108_rc"+n+".json"]
 assert cert("325_native_high_2x2")["original_high_C_244_246_2by2_strict_positive"]
 assert not cert("325_native_high_2x2")["full_high_residual_paid"]
 assert cert("324_high_tail_smoothing")["original_even_far_high_D_floor_strict_positive"]
 rows=rc318.source_info()
 prime=prime_new_pairs(rows,reverse)
 met=cert("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 cLo,cHi=rc324.scalar_original(cert("322_low_3d_gram")[
  "refined_Euler_Maclaurin_gamma"])
 reg=F(cert("324_high_tail_smoothing")[
  "original_high_regular_operator_norm_bound_244plus"])
 mat_new=native_C_new_pairs(prime,slo,shi,cLo,cHi,reg)
 old=cert("325_native_high_2x2")["original_native_C_2by2_intervals"]
 C={}
 for key,interval in old.items():
  i,j=map(int,key.split("_"));C[i,j]=IV(*map(F,interval))
 C.update(mat_new)
 assert len(C)==6
 a,t,u=C[244,244],C[244,246],C[244,248]
 d,v,w=C[246,246],C[246,248],C[248,248]
 M=[[a,t,u],[t,d,v],[u,v,w]]
 det2=a*d-t*t
 det=det3(M)
 assert a.l>0 and det2.l>0 and det.l>F(1,100)
 # An independent positive lower bound on the least eigenvalue
 # of the exact original 3x3 high matrix from Gershgorin.
 absmax=lambda z:max(abs(z.l),abs(z.h))
 gmin=min(a.l-absmax(t)-absmax(u),
    d.l-absmax(t)-absmax(v),
    w.l-absmax(u)-absmax(v))
 assert gmin>F(1,4)
 old_response=cert("325_native_high_2x2")[
  "low_R323_witness_native_high_response"]
 b={int(k):IV(*map(F,val)) for k,val in old_response.items()}
 full_err=F(cert("323_coercivity_nogo")[
   "complete_original_high_source_error_upper"])
 b[248]=source_at_248(rows,slo,shi,full_err,reverse)
 assert all(b[k].l*b[k].h>0 for k in DEGREES)
 centers=[[F((M[i][j].l+M[i][j].h)/2) for j in range(3)] for i in range(3)]
 bcent=[(b[k].l+b[k].h)/2 for k in DEGREES]
 y=inverse_rational(centers,bcent)
 assert len(y)==3 and y[0]>0
 # A signed ORIGINAL Ritz (not a global high inverse).
 gain=sum((2*y[i]*b[DEGREES[i]] for i in range(3)),IV(0))
 for i in range(3):
  for j in range(i,3):
   gain-=(2 if i!=j else 1)*y[i]*y[j]*M[i][j]
 assert gain.l>0
 # Even optimal 2x2 correction from exact interval inverse:
 # D=ad-t², b^T A^-1 b =
 # (d b0² + a b1² - 2t b0 b1)/D.
 prior_num=d*b[244].sq()+a*b[246].sq()-2*t*b[244]*b[246]
 prior_optimal=prior_num/det2
 assert prior_optimal.l>0
 gain_minus_optimal=gain.l-prior_optimal.h
 assert gain_minus_optimal>0,(
  "third high mode Ritz fails to exceed optimal 244/246 correction")
 # Pay the TRUE residual through the ENTIRE infinite high space.
 # T x is bounded globally by the three pinned complete source
 # envelopes, not the finite 3-mode projection alone.
 T0=sqrtup(F(cert("318_p0_signed_schur")[
  "complete_even_D_high_source_Tv0_norm_squared_upper"]))
 T2=F(cert("320_boundary_cancelled_schur")[
  "entire_original_boundary_cancelled_D_high_response_norm_upper"])
 T4=F(cert("321_p4_boundary_native")[
  "full_original_D_high_source_norm_upper"])
 Twhole=up(F(3,25)*T0+F(23,8)*T2+T4)
 assert 0<Twhole<F(1,100)
 Mglobal=F(cert("313_prime_pole_distributions")[
  "improved_original_native_Weil_D_to_D_operator_norm_upper"])
 assert 9<Mglobal<11
 ynorm=sqrtup(sum((k*k for k in y),F(0)))
 # C=P_high N0 P_high so ||C||<=||N0||<=Mglobal.
 # Thus ||C Y||<=Mglobal||Y|| in the FULL infinite high
 # Hilbert space, including far tail, all coupling. This is
 # coarse, but a genuine fully paid R norm bound.
 crossToEntireComplement=up(Mglobal*ynorm)
 rwhole=up(Twhole+crossToEntireComplement)
 # The signed original represented 3x3 high residual is
 # b_i -(C_3 y)_i. Its actual norm is MUCH smaller than the
 # whole residual; it is not substituted for the whole.
 represented=[]
 for i,k in enumerate(DEGREES):
  residual=b[k]-sum((M[i][j]*y[j] for j in range(3)),IV(0))
  represented.append(residual)
 rep_norm=sqrtup(sum((max(abs(x.l),abs(x.h))**2 for x in represented),F(0)))
 assert rep_norm<rwhole
 evenFloor=F(cert("324_high_tail_smoothing")[
  "inherited_even_244plus_global_floor"])
 signedSchurResidualCorrectionUpper=up(rwhole*rwhole/evenFloor)
 Bxx=F(cert("323_coercivity_nogo")[
  "original_low_quadratic_B_upper"])
 return dict(
  milestone="RC326",
  parent_route_head="477c757619a82d282219832ca448338045150db7",
  pinned_upstream_git_blobs=PINS,
  native_original_signed_CC27_operator=True,
  high_block_degrees=list(DEGREES),
  additional_prime_rational_center_overlap_integrals=21,
  all_original_prime_shift_edge_log_errors_paid=True,
  original_high_3x3_C_intervals={
    f"{i}_{j}":C[i,j].out() for i in DEGREES for j in DEGREES if j>=i},
  native_original_high_3x3_leading_2x2_minor_lower=str(dn(det2.l)),
  native_original_high_3x3_determinant_lower=str(dn(det.l)),
  native_original_high_3x3_Gershgorin_floor_lower=str(dn(gmin)),
  native_original_high_3x3_strictly_positive=True,
  low_witness_high_248_signed_source_interval=b[248].out(),
  explicit_original_high_3mode_Ritz_trial=[str(v) for v in y],
  exact_native_three_mode_Ritz_reduction_lower=str(dn(gain.l)),
  optimal_native_two_mode_Ritz_reduction_upper=str(up(prior_optimal.h)),
  strict_Ritz_improvement_over_optimal_2mode_lower=str(dn(gain_minus_optimal)),
  original_witness_Schur_three_mode_trial_upper=str(up(Bxx-gain.l)),
  independently_pinned_whole_original_high_source_Tx_norm_upper=str(Twhole),
  original_full_D_to_D_N0_operator_norm_upper=str(Mglobal),
  actual_Ritz_trial_full_high_action_CY_norm_upper=str(crossToEntireComplement),
  explicit_represented_3mode_residual_norm_upper=str(rep_norm),
  complete_infinite_high_residual_T_minus_CY_norm_upper=str(rwhole),
  RC314_correct_sign_full_high_residual_penalty_upper=str(signedSchurResidualCorrectionUpper),
  infinite_even_far_tail_action_included_via_global_norm=True,
  sharp_head_to_far_tail_coupling_operator_norm_certified=False,
  full_head_278x278_positive=False,
  exact_native_high_inverse_computed=False,
  full_signed_3D_Schur_positive=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
    "RC327: improve the *whole-space* T-CY residual by deriving "
    "native source-resolved C*v244,v246,v248 Parseval and "
    "separating 278 finite-head coupling from the strongly "
    "coercive n>=800 far tail. RC326 proves three-mode positive "
    "high compression and a valid—but very conservative—full "
    "infinite residual. The true 3D Schur lower bound stays OPEN."
  ))
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 d=run(reverse=a.replay)
 if a.replay:assert d==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC326: native original high 3x3 positive, third Ritz improvement, entire infinite residual paid (conservative). Full Schur and Stage I OPEN.")
