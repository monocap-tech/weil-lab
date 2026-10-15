"""RC308: common bounded L2 carrier for nominal prime, regular, and pole.

From RC46's certified regular archimedean kernel r(t) on [0,2B],
the even/odd native regular-source formula is a symmetric physical
convolution with r(|x-y|); Schur gives ||R||<=2B sup |r|.
A per-monomial outward rational bound pays the full degree-192
regular polynomial and its certified uniform kernel error, with
no degree cap on the L2 input.

The inherited native pole source is the difference of rank-one
even cosh and odd sinh kernels. Its exact nonzero spectral norm is
2(B+sinh(B)); rational Taylor bounds pay the degree-40 polynomial
approximations and their entire exponential tails.

Together with RC307's nominal seven-prime L2-bound, the sum of
these THREE source components extends by density to bounded L2.
Thus D^-1 of their sum acts boundedly on the physical D-form
completion. This is NOT the full Weil operator: the remaining
singular/endpoint source, original diagonal terms, arbitrary
repeated full action, Schur positivity, Stage I, F4 and RH OPEN.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial, comb, isqrt
from pathlib import Path
import validate_rpb108_rc237_two_trial_signed_response as native

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
HALF=B/2
GRID=10**60
MIX={4:F(1),6:F(-1,2),8:F(1,3),10:F(-1,5)}
o=native.orig
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":
  "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc43_native_prime_head.json":
  "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc303_direct_polynomial_prime.json":
  "cc71c9a961230ecedeb65947afae15ba37f0abbe",
 "certificates/rpb108_rc306_adaptive_markov.json":
  "29123b028e6d9c8f69e31c0b61f3a04c3ade33c7",
 "certificates/rpb108_rc307_direct_prime_completion.json":
  "10eff4ea9bf4199cff580a92a379e6d04ae87eb1",
 "scripts/validate_rpb108_rc237_two_trial_signed_response.py":
  "d13e909c8aa8b91d5b55ec5e5f5179cdaf9325d2",
}

def ceiling(x):
 assert x>=0
 return F((x.numerator*GRID+x.denominator-1)//x.denominator,GRID)

def floor_pos(x):
 assert x>=0
 return F(x.numerator*GRID//x.denominator,GRID)

def sqrt_up(x):
 assert x>=0
 if x==0:return F(0)
 return F(isqrt(x.numerator*GRID*GRID//x.denominator)+1,GRID)

def polyadd(a,b):
 r=[F(0)]*max(len(a),len(b))
 for k,x in enumerate(a):r[k]+=x
 for k,x in enumerate(b):r[k]+=x
 return r

def weighted_legendre_poly(y):
 p=[F(0)]
 for d,v in y.items():
  p=polyadd(p,[v*c for c in o.legendre(d)])
 assert len(p)==11 and all(p[k]==0 for k in range(1,len(p),2))
 return p

def regular_source_from_mixed_poly(q,reg):
 # Physical convolution left-source change of coordinates:
 # q(2u-1) for u in [0,1], with r(2B(u-v)).
 # Native evenness adds the right reflected source. Unlike
 # four independent columns, this evaluates the input q itself.
 vals=[sum((q[k]*comb(k,m)*2**m*(-1)**(k-m)
        for k in range(m,len(q))),F(0))
       for m in range(len(q))]
 left=[F(0)]*(len(reg)+len(q))
 for k,a in enumerate(reg):
  for m,v in enumerate(vals):
   left[k+m+1]+=2*B*a*(2*B)**k*v*F(
      factorial(k)*factorial(m),factorial(k+m+1))
 # u=(x+1)/2: left((x+1)/2) + left((1-x)/2)
 result=[sum((left[k]*comb(k,l)/2**k
         for k in range(l,len(left))),F(0))*(1+(-1)**l)
         for l in range(len(left))]
 assert all(result[l]==0 for l in range(1,len(result),2))
 return result

def direct_convolution_low_kernel(q,reg):
 # Independent direct physical convolution identity:
 # left(x) = B integral_-1^x r(B(x-t)) q(t) dt,
 # and for even q, right(x)=left(-x).
 # Expand (x-t)^k using binomial and integrate each t^m.
 # Restrict this regression to the first 7 Taylor terms to keep
 # exact rational polynomial arithmetic modest.
 deg=len(q)+len(reg)
 left=[F(0)]*deg
 for k,a in enumerate(reg):
  for m,v in enumerate(q):
   if not v:continue
   c=B**(k+1)*a*v
   for j in range(k+1):
    t=c*comb(k,j)*(-1)**j/F(j+m+1)
    left[k+m+1]+=t
    left[k-j]+= -t*(-1)**(j+m+1)
 result=[left[l]*(1+(-1)**l) for l in range(deg)]
 return result

def exponential_upper(z):
 assert z>0 and z<F(1)
 # Taylor degree 40 plus rigorous geometric ratio after k=41.
 terms=[z**k/factorial(k) for k in range(41)]
 tail=(z**41/factorial(41))/(1-z/F(42))
 exact_upper=sum(terms,F(0))+tail
 assert exact_upper>0
 return ceiling(exact_upper),ceiling(tail)

def sinh_interval(z):
 assert 0<z<F(2)
 # Positive Taylor expansion sum_{j>=0} z^(2j+1)/(2j+1)!.
 # After index j=20 (degree 41), next term at degree43;
 # subsequent term ratios <= z^2/(44*45).
 low=sum((z**(2*j+1)/factorial(2*j+1)
          for j in range(21)),F(0))
 remainder=(z**43/factorial(43))/(1-z*z/F(44*45))
 return floor_pos(low),ceiling(low+remainder)

def run(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  h=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert h==sha,(path,"inherited blob changed")
  data[path]=json.loads(raw) if path.endswith(".json") else None
 def get(s):return data["certificates/rpb108_rc"+s+".json"]
 arch=get("46_native_archimedean_head")
 prime=get("43_native_prime_head")
 prior=get("307_direct_prime_completion")
 mom=get("129_four_vector_joint_moment")
 rc303=get("303_direct_polynomial_prime")
 assert prior["dimension_free_nominal_prime_component_extends_to_full_L2_by_density"]
 assert not prior["full_archimedean_pole_endpoint_operator_bounded_on_common_carrier"]
 assert rc303["direct_native_prime_translation_available_for_signed_polynomials"]
 reg=[F(x) for x in arch["regular_kernel_coefficients"]]
 assert arch["regular_kernel_degree"]==192
 assert len(reg)==193
 eps=F(arch["regular_kernel_uniform_error_upper"])
 assert eps>0
 sl=F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sh=F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 0<sl<=sh
 prime_bound=2*sum((F(t["coefficient_upper"])
                    for t in prime["active_prime_powers"]),F(0))
 assert prime_bound==F(prior[
   "dimension_free_nominal_prime_L2_to_L2_norm_upper"])
 assert 0<prime_bound<F(8)

 # Schur supnorm bound for the exact physical convolution kernel.
 # Use each rational absolute Taylor monomial individually with
 # outward GRID rounding; prevents giant rational denominator
 # explosions when summing 193 unrelated rational coefficients.
 terms=[ceiling(abs(c)*(2*B)**k) for k,c in enumerate(reg)]
 sup_poly=sum(terms,F(0))
 sup_kernel=sup_poly+ceiling(eps)
 reg_full=2*B*sup_kernel
 reg_model=2*B*sup_poly
 reg_diff=2*B*ceiling(eps)
 assert F(0)<sup_poly<F(1)
 assert 0<reg_full<F(3,2)
 assert reg_full==reg_model+reg_diff

 # Exact native regular kernel regression on a genuinely signed
 # source polynomial q (not merely preassembled input columns).
 q=weighted_legendre_poly(MIX)
 src=regular_source_from_mixed_poly(q,reg)
 parts=[native.trial.regular_poly(d,reg) for d in MIX]
 check=[sum((MIX[d]*parts[j][n] if n<len(parts[j])
            else F(0) for j,d in enumerate(MIX)),F(0))
       for n in range(len(src))]
 assert src==check,("full regular source mismatch",len(src))
 low=regular_source_from_mixed_poly(q,reg[:7])
 independent=direct_convolution_low_kernel(q,reg[:7])
 assert low==independent,("physical convolution normalization mismatch")
 assert all(src[k]==0 for k in range(1,len(src),2))
 print("RC308: exact mixed polynomial archimedean convolution "
       "and independent physical integral passed",flush=True)

 # Rank-two pole action on complete even/odd L2 physical carrier.
 # phi_even=cosh(B x/2), phi_odd=sinh(B x/2), x normalized.
 # P_pole q=2 <q,phi_even> phi_even -
 #          2 <q,phi_odd> phi_odd.
 # Orthogonality gives operator norm 2||phi_even||²
 # =2(B+sinh(B)) (the odd eigenvalue has smaller modulus).
 slo,shi=sinh_interval(B)
 pole_lo=2*(B+slo)
 pole_hi=2*(B+shi)
 assert 0<pole_lo<=pole_hi<F(6)
 assert 2*(shi-B)<pole_hi
 exp_hi,taylortail=exponential_upper(HALF)
 # Every even/odd Taylor 40 partial sum differs pointwise by
 # <= full exponential tail. Both u and truncated p have sup
 # <= exp_hi, so 2||u⊗u-p⊗p|| <= 8B exp_hi tail.
 pole_diff=8*B*exp_hi*taylortail
 assert pole_diff>0 and pole_diff<F(1,10**35)

 from math import factorial
 pole_moments={}
 phi={}
 for parity in (0,1):
  phi[parity]=[HALF**k/factorial(k) if k%2==parity
               else F(0) for k in range(41)]
 for d,w in MIX.items():
  moment=B*o.integral(o.product(o.legendre(d),phi[0]))
  pole_moments[d]=moment
 mixed_phi_moment=B*o.integral(o.product(q,phi[0]))
 assert mixed_phi_moment==sum((MIX[d]*pole_moments[d] for d in MIX),F(0))
 # No parity confusion: even pole sign +, odd pole sign -.
 assert all(d%2==0 for d in MIX)
 def applied_pole(k):
  return 2*mixed_phi_moment*phi[0][k] if k<len(phi[0]) else F(0)
 assert applied_pole(1)==0
 assert applied_pole(0)==2*mixed_phi_moment

 # The complete NOMINAL SOURCE SUM: prime + regular + pole.
 # Regular sign in Weil action is negative, but norms use triangle.
 bounded_sum=prime_bound+reg_full+pole_hi
 # D metric:  ||D^-1 S q||_D <= ||Sq||_2/sqrt(s_low)
 # and ||q||_2<=||q||_D/sqrt(s_low).
 full_D_norm=ceiling(bounded_sum/sl)
 assert 0<bounded_sum<F(15)
 assert full_D_norm<F(4)
 # The old RC307 prime-only norm cannot certify this combined
 # three-component operator; this checkpoint genuinely extends
 # domain coverage, while excluding the endpoint and diagonal.
 assert full_D_norm>F(prior[
    "dimension_free_nominal_prime_D_to_D_inverse_norm_upper"])
 # Regular source approximation and Taylor pole patch also have
 # operator norm error on ALL even/odd L2:
 total_analytic_model_error=reg_diff+pole_diff
 assert total_analytic_model_error>0

 return dict(
  milestone="RC308",
  parent_merge_commit="35c1fb0311f44f23a7eee6830ff60411274b9ec8",
  input_git_blob_pins=PINS,
  regular_physical_convolution_kernel_max_distance=str(2*B),
  regular_kernel_polynomial_degree=192,
  regular_kernel_absolute_monomial_majorant_upper=str(sup_poly),
  regular_kernel_uniform_error_upper=str(ceiling(eps)),
  regular_actual_kernel_Linfty_upper=str(sup_kernel),
  regular_original_physical_L2_operator_norm_upper=str(reg_full),
  regular_polynomial_model_L2_operator_norm_upper=str(reg_model),
  regular_kernel_approximation_L2_operator_norm_upper=str(reg_diff),
  full_mixed_signed_input_original_regular_polynomial_degree=len(src)-1,
  exact_mixed_signed_polynomial_regular_source_regression=True,
  physical_integral_vs_native_regular_monomial_low_kernel_regression=True,
  regular_convolution_L2_extension_by_density_under_kernel_identity=True,
  pole_even_hyperbolic_source="cosh(Bx/2)",
  pole_odd_hyperbolic_source="sinh(Bx/2)",
  certified_sinh_B_lower=str(slo),
  certified_sinh_B_upper=str(shi),
  exact_pole_rank_two_L2_operator_norm_lower=str(pole_lo),
  exact_pole_rank_two_L2_operator_norm_upper=str(pole_hi),
  pole_even_rank_one_plus_odd_rank_one_minus=True,
  pole_degree40_Taylor_uniform_tail_upper=str(taylortail),
  pole_degree40_approximation_L2_operator_error_upper=str(pole_diff),
  mixed_even_input_phi_moment_exact=str(mixed_phi_moment),
  mixed_even_input_pole_output_degree0_coefficient_exact=str(applied_pole(0)),
  nominal_prime_L2_operator_norm_upper=str(prime_bound),
  three_component_nominal_source_L2_operator_norm_upper=str(bounded_sum),
  three_component_D_inverse_D_to_D_norm_upper=str(full_D_norm),
  regular_plus_pole_polynomial_model_L2_error_upper=str(total_analytic_model_error),
  three_component_operator_extends_boundedly_to_physical_L2=True,
  three_component_D_inverse_operator_extends_to_D_energy_completion=True,
  full_endpoint_singular_source_bounded_on_common_L2=False,
  full_original_Weil_operator_on_common_carrier_certified=False,
  complete_original_diagonal_Weil_action_included=False,
  complete_original_Weil_action_iterability_certified=False,
  RC292_signed_Chebyshev_inverse_response_certified=False,
  remaining_314_principal_Schur_positive=False,
  original_Weil_form_positivity_certified=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
   "RC309: resolve the endpoint/diagonal Legendre operator's "
   "boundedness or closed-graph mapping on the SAME D-energy "
   "carrier, with its singular off-diagonal Hilbert-transform "
   "structure explicitly paid. Only after the complete original "
   "action is defined and stable may RC292 Chebyshev iterates "
   "be applied to their own outputs.")
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 result=run(reverse=a.replay)
 if a.replay:
  assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC308 VALIDATED: common physical L2 carrier for prime, regular "
       "archimedean, and rank-two pole; full endpoint OPEN",flush=True)
