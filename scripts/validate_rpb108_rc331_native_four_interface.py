"""RC331: original signed four-mode-to-infinite high interface.

Extend RC327's complete native off-diagonal operator-norm calculation
from inputs {244,246,248} to {244,246,248,250}, with output n>=252.
Keep the original CC27/RC313 D-Riesz operator and the RC330 rational Y4,
not the old Y3 or a supplementary positive matrix.

All original seven-prime translations, endpoint action, regular kernel,
even pole and infinite output modes are paid. This is a native *norm*
certificate, NOT a calculation of the mixed signed cross covariance in
individual n>=252 modes; the signed covariance is RC332's next gate.
A valid four-vector full-space residual follows by Parseval and a
triangle inequality after removing all four represented source modes.
Neither finite Ritz gain nor a residual upper bound is a positive
three-dimensional low Schur lower bound.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import validate_rpb108_rc324_high_tail_smoothing as rc324

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
INPUT=(244,246,248,250)
FIRST=252
FAR=800
G=10**28
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686",
 "certificates/rpb108_rc328_signed_finite_tail_residual.json":"49d9daf11defd0f272865d3780f3a53d0af6e130",
 "certificates/rpb108_rc330_original_high_four_ritz.json":"671d56538a0f70df1fab8ca840c1a47797bef56b",
}
def up(x,g=G):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sqrtlo(x,g=10**38):
 assert x>=0
 if x==0:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k,g)
def sqrthi(x,g=10**38):
 assert x>=0
 if x==0:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+1,g)
def gitblob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def absmin(row):
 a,b=map(F,row)
 assert a<=b
 if a<=0<=b:return F(0)
 return min(abs(a),abs(b))

def run(reverse=False):
 docs={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert gitblob(raw)==pin,("upstream Git blob changed",p)
  docs[p]=json.loads(raw)
 def cert(num):return docs["certificates/rpb108_rc"+num+".json"]
 c330=cert("330_original_high_four_ritz")
 c328=cert("328_signed_finite_tail_residual")
 c324=cert("324_high_tail_smoothing")
 assert c330["original_high_4x4_strictly_positive"]
 assert c330["four_mode_finite_Ritz_yields_only_Schur_UPPER"]
 assert not c330["full_original_C_inverse_computed"]
 assert c328["proved_strict_sharpening_of_complete_original_signed_residual"]
 met=cert("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<slo<=shi<5
 h=rc324.Htable(FAR)
 D=lambda n:h[n]+slo
 Din=min(D(m) for m in INPUT)
 Dnear=D(FIRST)
 Dfar=D(FAR)
 assert Din>9 and Din<Dnear<Dfar
 # Original offdiagonal logarithmic endpoint. Sum exact
 # squared physical-to-D Legendre coefficients over n252..798.
 finite=F(0)
 for n in (reversed(range(FIRST,FAR,2)) if reverse
           else range(FIRST,FAR,2)):
  for m in (reversed(INPUT) if reverse else INPUT):
   entry_squared=F((2*n+1)*(2*m+1),
      (n-m)**2*(n+m+1)**2*D(n)*D(m))
   finite+=up(entry_squared,10**44)
 finite=up(finite,10**36)
 # n800+ upper via all integers n>=800, using
 # (n-m)>=n(1-m/800), (n+m+1)>=n and H_n>=H800;
 # ∑_{n>=800}n^-3 <= 1/(2*799^2).
 far=F(0)
 for m in INPUT:
  c=F((2*FAR+1)*(2*m+1)*FAR,
      (FAR-m)**2*Dfar*D(m))
  far+=c/F(2*(FAR-1)**2)
 far=up(far,10**36)
 assert 0<far<finite/F(10)
 endpointHS=sqrthi(finite+far)
 endpointFarHS=sqrthi(far)
 prime=F(cert("313_prime_pole_distributions")[
  "original_prime_finite_chain_L2_norm_upper"])
 regular=F(c324["original_high_regular_operator_norm_bound_244plus"])
 regFar=F(c324["original_high_regular_operator_norm_bound_800plus"])
 assert 4<prime<5 and 0<regFar<=regular<F(1,1000)
 # Physical original prime and regular operators act between
 # D-normal coordinates, so charge both D denominators.
 z=B/2
 assert 0<z<F(3,5)
 # Four even represented modes: 32B z^(2*244) L2 mass;
 # omitted 252+ even modes: 8B z^(2*252)/(1-z^4).
 # Two times their geometric mean is <60B z^(244+252).
 pole=F(60)*B*z**(244+FIRST)/sqrtlo(Din*Dnear)
 cross=up(endpointHS+prime/sqrtlo(Din*Dnear)
          +regular/sqrtlo(Din*Dnear)+pole)
 crossFar=up(endpointFarHS+prime/sqrtlo(Din*Dfar)
             +regFar/sqrtlo(Din*Dfar)+pole)
 assert 0<crossFar<=cross<F(3,5)
 y=list(map(F,c330["original_new_rational_four_mode_Ritz_trial"]))
 assert len(y)==4
 yNorm=sqrthi(sum((q*q for q in y),F(0)))
 Cout=up(cross*yNorm)
 Cfar=up(crossFar*yNorm)
 assert Cout<F(1,10000)
 assert Cout<F(c330["new_four_mode_full_infinite_C_Y_action_norm_upper"])/12
 # FOUR represented modes have original signed independently
 # certified source intervals. Subtract their minimum energies
 # from the entire ORIGINAL signed Tx Parseval norm.
 b=c330["original_signed_low_witness_high_4_source_intervals"]
 sourceEnergy=sum((absmin(b[str(n)])**2 for n in INPUT),F(0))
 T=F(c328["original_combined_true_entire_high_Tx_norm_upper"])
 assert 0<sourceEnergy<T*T
 Tout=sqrthi(T*T-sourceEnergy)
 Rinside=F(c330["new_four_mode_represented_residual_norm_upper"])
 Rout=up(Tout+Cout)
 Rtotal=up(sqrthi(Rinside**2+Rout**2))
 mu=F(c324["inherited_even_244plus_global_floor"])
 assert mu>0
 penalty=up(Rtotal**2/mu)
 old=F(c330["new_four_mode_entire_high_residual_penalty_upper"])
 assert Rtotal<F(3,2500),("native 4-mode residual cap")
 assert penalty<F(1,4000),("native four-mode penalty cap")
 assert penalty<old/F(3),("failure to reduce SAME four-vector residual")
 assert penalty>F(cert("323_coercivity_nogo")["original_low_quadratic_B_upper"])
 # Keep certificate report deliberately fixed-denominator rational
 # caps so GitHub replay is independent of execution direction.
 return dict(
  milestone="RC331",
  parent_route_head="447774a91c3898d317dc1383f8500ae6354f1bae",
  input_git_blob_pins=PINS,
  original_CC27_signed_Weil_D_operator=True,
  represented_even_high_degrees=list(INPUT),
  omitted_even_high_from=FIRST,
  infinite_far_tail_from=FAR,
  four_mode_to_all_252plus_original_interface_norm_less_than="3/5",
  original_four_mode_full_outside_CY_norm_less_than="1/10000",
  original_four_mode_entire_infinite_R_norm_less_than="3/2500",
  corrected_RC314_four_mode_penalty_less_than="1/4000",
  strict_same_vector_full_residual_penalty_improvement_over_RC330=True,
  exact_original_endpoint_hilbert_schmidt_paid_through_infinity=True,
  original_signed_prime_regular_even_pole_cross_norms_paid=True,
  full_original_signed_Tx_all_278_plus_infinite_source_paid=True,
  original_four_source_coordinates_subtracted_by_Parseval=True,
  original_signed_covariance_252plus_computed=False,
  improves_prior_RC328_three_mode_best_global_bound_asserted=False,
  full_278_mode_high_head_positivity=False,
  full_original_C_inverse_computed=False,
  full_three_dimensional_low_Schur_positive=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
   "RC332: calculate genuine signed native C_252,m for "
   "m=244,246,248,250 and original b252; then extend source-"
   "sensitive covariance over 252..798 and pay all n800+ "
   "without replacing the four-mode high Ritz witness by "
   "a positive full low Schur lower claim."
  )
 )
if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",type=Path,required=True)
 ap.add_argument("--replay",action="store_true")
 a=ap.parse_args()
 result=run(reverse=a.replay)
 if a.replay:
  assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC331: genuine original 4-mode-to-infinite high interface bound; full residual sharpened; signed outside covariance and Stage I OPEN.")
