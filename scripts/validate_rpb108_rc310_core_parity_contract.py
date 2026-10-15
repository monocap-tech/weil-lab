"""RC310: two-parity dense-core original Weil action identity audit.

Independently construct the finite Legendre output of the native
endpoint, physical regular convolution, seven paired signed prime
translations and signed rank-two pole on both even/odd polynomials.
Regress four pinned RC237/RC240 original-action columns P2-P5,
and two nontrivial signed same-parity mixtures. Pay the original
log(2) and physical D-parameter intervals. Show the rank317
finite diagonal augmentation extends boundedly to the common carrier,
and formulate exact conditional dense-core uniqueness.

This verifies an inherited native *MODEL* on finite test degrees.
It does not derive from first principles the canonical Weil explicit
formula for every Legendre basis vector, nor prove positivity,
spectral lower bound, RC292 inverse or RH.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

import validate_rpb108_rc237_two_trial_signed_response as native
import validate_rpb108_rc309_endpoint_schur as endpoint
ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
GRID=10**30
o=native.orig
TEST_DEGREES=(2,3,4,5)
MIXES=({"label":"signed_even_P2_minus_P4_over_3",
         "a":{2:F(1),4:F(-1,3)}},
       {"label":"signed_odd_P3_minus_P5_over_2",
         "a":{3:F(1),5:F(-1,2)}})
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
 "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc43_native_prime_head.json":
 "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc46_native_archimedean_head.json":
 "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc237_two_trial_signed_response.json":
 "04bf1539dda4cfd79b4ecdc2d3e310daa2d3b657",
 "certificates/rpb108_rc240_three_trial_signed_response.json":
 "6c41b7f196052fea179b956099fb69cc5d07813c",
 "certificates/rpb108_rc283_reduced_reference.json":
 "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc308_bounded_arch_pole.json":
 "2461485678ec998ed7449e8a6141a3b71e083f35",
 "certificates/rpb108_rc309_endpoint_schur.json":
 "d3f11a563486c7adb9128252092820ad7f1ef189",
 "scripts/validate_rpb108_rc237_two_trial_signed_response.py":
 "d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2",
 "scripts/validate_rpb108_rc309_endpoint_schur.py":
 "c12ca56b934273603b6a63e657d1460c268ed84a",
}

def ceil_grid(x):
 assert x>=0
 return F((x.numerator*GRID+x.denominator-1)//x.denominator,GRID)

def addpoly(a,b):
 v=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):v[i]+=x
 for i,x in enumerate(b):v[i]+=x
 return v

def qpoly(a):
 deg=max(a)
 r=[F(0)]*(deg+1)
 for d,w in a.items():
  for j,c in enumerate(o.legendre(d)):
   r[j]+=w*c
 assert all(x==0 for j,x in enumerate(r) if j%2!=(deg%2))
 return r

def reg_source(q, parity, reg):
 """Direct transformed-input physical left integral and parity reflect."""
 assert parity in (0,1)
 v=[sum((q[k]*comb(k,m)*2**m*(-1)**(k-m)
         for k in range(m,len(q))),F(0)) for m in range(len(q))]
 left=[F(0)]*(len(reg)+len(q))
 for k,c in enumerate(reg):
  for m,b in enumerate(v):
   if not b:continue
   left[k+m+1]+=2*B*c*(2*B)**k*b*F(
     factorial(k)*factorial(m),factorial(k+m+1))
 ans=[sum((left[k]*comb(k,l)/2**k
            for k in range(l,len(left))),F(0))
         *(1+(-1)**(parity+l)) for l in range(len(left))]
 assert all(ans[l]==0 for l in range(len(ans)) if l%2!=parity)
 return ans

def direct_regression_low_kernel(q,parity,reg):
 """Independent untransformed physical integral in t variable."""
 left=[F(0)]*(len(reg)+len(q))
 for k,c in enumerate(reg):
  for m,w in enumerate(q):
   if not w:continue
   t=B**(k+1)*c*w
   for j in range(k+1):
    b=t*comb(k,j)*(-1)**j/F(j+m+1)
    left[k+m+1]+=b
    left[k-j]-=b*(-1)**(j+m+1)
 return [left[l]*(1+(-1)**(parity+l)) for l in range(len(left))]

def prime_source(q, parity, prime, output):
 """Direct signed translated source; no stored column reused."""
 terms=[]
 for row in prime["active_prime_powers"]:
  lo,hi=F(row["translation_lower"]),F(row["translation_upper"])
  cl,ch=F(row["coefficient_lower"]),F(row["coefficient_upper"])
  ell=(lo+hi)/2;c=(cl+ch)/2
  for sg in (-1,1):
   off=sg*ell/B
   l=max(F(-1),-1-off);r=min(F(1),1-off)
   polynomial=[-c*sum((q[k]*comb(k,m)*off**(k-m)
                for k in range(m,len(q))),F(0))
               for m in range(len(q))]
   terms.append((l,r,polynomial))
 knots=sorted({F(-1),F(1)}|{k for l,r,_ in terms for k in (l,r)})
 pieces=[]
 for l,r in zip(knots,knots[1:]):
  mid=(l+r)/2
  z=[sum((poly[k] for a,b,poly in terms if a<mid<b),F(0))
     for k in range(len(q))]
  pieces.append((l,r,z))
 assert len(terms)==14 and len(pieces)==15
 for l,r,p in pieces:
  assert next(poly for a,b,poly in pieces if a==-r and b==-l)==[
      (-1)**(parity+k)*c for k,c in enumerate(p)]
 out=[]
 for n in range(output+1):
  if n%2!=parity:out.append(F(0));continue
  leg=o.legendre(n)
  out.append(F(2*n+1,2)*sum((
   o.integral(o.product(poly,leg),l,r) for l,r,poly in pieces),F(0)))
 return out,pieces

def pole_source(q, parity, output):
 """Native parity-signed degree-40 rank-two analytic pole source."""
 phi=[F(11,20)**k/factorial(k) if k%2==parity else F(0)
      for k in range(41)]
 moment=B*o.integral(o.product(q,phi))
 poly=[2*(-1)**parity*moment*coeff for coeff in phi]
 return [o.project(poly,n) if n%2==parity else F(0)
         for n in range(output+1)],moment

def components(a,reg,prime,H,output):
 parity=next(iter(a))%2
 assert all(d%2==parity for d in a)
 q=qpoly(a)
 r=reg_source(q,parity,reg)
 pc,pieces=prime_source(q,parity,prime,output)
 pole,moment=pole_source(q,parity,output)
 rcoeff=[o.project(r,n) if n%2==parity else F(0)
         for n in range(output+1)]
 ec=[sum((w*endpoint.E(n,d,H) for d,w in a.items()),F(0))
     for n in range(output+1)]
 diag=[a.get(n,F(0)) for n in range(output+1)]
 # Original model numerator without diagonal log2 and 789/125.
 num=[ec[n]-rcoeff[n]+pc[n]+pole[n] for n in range(output+1)]
 return dict(parity=parity,regular=rcoeff,prime=pc,pole=pole,
             endpoint=ec,diagonal=diag,numerator=num,
             pole_moment=moment,regular_source=r,segments=pieces)

def add_arrays(cs,coeff):
 out={}
 for key in ("regular","prime","pole","endpoint","diagonal","numerator"):
  out[key]=[sum((w*cs[d][key][n] for d,w in coeff.items()),F(0))
            for n in range(len(next(iter(cs.values()))[key]))]
 return out

def run(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  h=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert h==sha,(path,"pinned source changed")
  if path.endswith(".json"):data[path]=json.loads(raw)
 def get(name):return data["certificates/rpb108_rc"+name+".json"]
 m=get("129_four_vector_joint_moment")
 sl=F(m["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sh=F(m["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert F(3)<sl<=sh<F(5)
 reg=list(map(F,get("46_native_archimedean_head")[
                  "regular_kernel_coefficients"]))
 assert len(reg)==193
 prime=get("43_native_prime_head")
 assert len(prime["active_prime_powers"])==7
 C=F(get("309_endpoint_schur")[
    "conditional_abstract_original_action_model_bound"])
 assert C>0
 a237=get("237_two_trial_signed_response")[
      "parity_two_trial_signed_response_certificates"]
 a240=get("240_three_trial_signed_response")[
      "parity_three_trial_signed_response_certificates"]
 known={
   2:a237[0]["new_complete_original_action"],
   3:a237[1]["new_complete_original_action"],
   4:a240[0]["new_complete_original_action"],
   5:a240[1]["new_complete_original_action"]
 }
 assert [known[d]["input"] for d in TEST_DEGREES]==[
       "P2","P3","P4","P5"]
 H=[F(0)]
 for n in range(1,50):H.append(H[-1]+F(1,n))
 ll,lh=endpoint.log2_interval()
 assert ll==F(get("309_endpoint_schur")["original_log2_lower"])
 assert lh==F(get("309_endpoint_schur")["original_log2_upper"])
 output=12
 columns={}
 cases=[]
 for d in (reversed(TEST_DEGREES) if reverse else TEST_DEGREES):
  c=components({d:F(1)},reg,prime,H,output)
  parity=d%2
  assert c["parity"]==parity
  assert c["regular_source"]==native.regular_poly(d,reg)
  # Independent t-integral of first 7 Taylor terms is another
  # construction of the SAME original regular source, both parities.
  assert reg_source(o.legendre(d),parity,reg[:7])==(
   direct_regression_low_kernel(o.legendre(d),parity,reg[:7]))
  # Native pole sign convention must be identical on both parity
  # blocks; odd is negative, even is positive.
  low=known[d]["finite_original_D_action"]
  for n in range(output+1):
   if n%2!=parity:
    assert low[n]["coefficient"]==low[n]["radius"]=="0"
    assert all(c[x][n]==0 for x in (
       "regular","prime","pole","endpoint","numerator"))
    continue
   numerator=c["numerator"][n]-F(789,125)*c["diagonal"][n]
   values=[F(n==d)+(numerator-L*c["diagonal"][n])/(H[n]+s)
           for L in (ll,lh) for s in (sl,sh)]
   midpoint=F(low[n]["coefficient"])
   radius=F(low[n]["radius"])
   assert radius>=0 and all(
       midpoint-radius<=v<=midpoint+radius for v in values),(
           "original full native action profile disagrees",d,n)
  # Independently compare original prime and pole low action to
  # inherited RC237 evaluator's same source.
  # Entire 65-output legacy native prime evaluator is expensive;
  # finite tested values must agree with same exact model.
  p_old,t_old,f_old,segs=native.prime_poly(d,prime,reverse)
  assert all(c["prime"][n]==p_old[n] for n in range(output+1))
  assert len(segs)==15 and t_old>=0 and f_old>=0
  columns[d]=c
  cases.append(dict(
     input_degree=d,parity="odd" if parity else "even",
     checked_original_low_modes=output+1,
     original_complete_enclosure_containment_passed=True,
     direct_regular_source_matches_native=True,
     independent_regular_physical_integral_matches=True,
     direct_seven_prime_source_matches_independent_native=True,
     signed_pole_sign_correct=True,
     model_matched_pinned_certified_original_action=True))
  print("RC310 original model profile P"+str(d)+" both "+
        "direct-source and archival intervals passed",flush=True)

 mixes=[]
 for item in MIXES:
  coeff=item["a"]
  direct=components(coeff,reg,prime,H,output)
  independent=add_arrays(columns,coeff)
  for field in independent:
   assert direct[field]==independent[field],(
     "direct polynomial vs columns",item["label"],field)
  # Check explicit physical integral on signed polynomial too.
  assert reg_source(qpoly(coeff),direct["parity"],reg[:7])==(
    direct_regression_low_kernel(qpoly(coeff),
                                direct["parity"],reg[:7]))
  assert direct["pole_moment"]==sum((
     w*columns[d]["pole_moment"] for d,w in coeff.items()),F(0))
  mixes.append(dict(
    source=item["label"],parity="odd" if direct["parity"] else "even",
    signed_coefficients={str(d):str(a) for d,a in coeff.items()},
    output_through_degree=output,
    all_five_source_components_and_diagonal_superposition_exact=True,
    direct_signed_prime_translation_is_independent_of_basis_column_sum=True,
    direct_signed_regular_physical_integral_exact=True,
    exact_direct_odd_pole_sign_when_applicable=True))
 assert len(cases)==4 and len(mixes)==2

 # The rank-317 augmentation is a distinct diagonal finite-rank
 # contribution, NOT silently part of the native original action.
 ref=get("283_reduced_reference")
 assert ref["proposed_buffered_reference_rank"]==317
 opt=ref["reduced_reference_options"]
 assert len(opt)==2 and opt[0]["parity"]=="even" and opt[1]["parity"]=="odd"
 even=opt[0]["reduced_reference_options"][1]
 odd=opt[1]["reduced_reference_options"][1]
 assert even["new_low_reference_rank"]==122
 assert odd["new_low_reference_rank"]==195
 assert even["first_discarded_matching_degree"]==244
 assert odd["first_discarded_matching_degree"]==391
 le,lo=F(opt[0]["parameter_lambda"]),F(opt[1]["parameter_lambda"])
 assert le>0 and lo>0
 augmentation_norm=max(le,lo)/sl
 augmented_model_bound=C+augmentation_norm
 assert augmented_model_bound>0 and augmentation_norm>0
 # General finite-rank diagonal positive A with coefficients
 # (lambda_parity/(H_d+s))*input_legendre_coordinate on retained
 # indices is bounded on H_D with ||A|| <= max(lambda)/s_lower.
 # Its nonnegative quadratic form does NOT prove full positivity.
 for d in TEST_DEGREES:
  lam=le if d%2==0 else lo
  assert lam/(H[d]+sh)<=lam/(H[d]+sl)<=augmentation_norm

 return dict(
   milestone="RC310",
   parent_merge_commit="e0a04dd0beea2b6d0c2ab34db6919cb301e7a430",
   pinned_source_git_blobs=PINS,
   native_core_formula=(
      "N_model=I+D_s^-1(E-(log2+789/125)I-R+P+Pole), "
      "with all original parity signs and finite metric interval paid"),
   even_and_odd_original_archival_column_regressions=sorted(
       cases,key=lambda a:a["input_degree"]),
   genuinely_direct_signed_source_superposition_regressions=sorted(
       mixes,key=lambda a:a["source"]),
   all_five_source_terms_exactly_linear_for_finite_polynomial_inputs=True,
   original_native_low_action_model_agrees_with_pinned_P2_P3_P4_P5=True,
   original_even_and_odd_regular_integral_normalizations_checked=True,
   all_seven_original_prime_power_pairs_retained=True,
   odd_pole_rank_one_sign_negative_certified=True,
   even_pole_rank_one_sign_positive_certified=True,
   bounded_abstract_native_model_D_operator_norm_upper=str(C),
   canonical_action_dense_polynomial_core_candidate=True,
   bounded_extension_uniqueness_if_canonical_core_identity_proved=True,
   source_identity_independently_derived_from_full_canonical_Weil_explicit_formula=False,
   full_original_operator_equated_to_canonical_Weil_action=False,
   rank317_even_reference_rank=122,
   rank317_odd_reference_rank=195,
   rank317_positive_diagonal_augmentation_bounded_separately=True,
   rank317_augmentation_D_to_D_operator_norm_upper=str(augmentation_norm),
   abstract_augmented_model_D_to_D_operator_norm_upper=str(
       augmented_model_bound),
   augmented_model_positivity_not_inferred_from_diagonal_positivity=True,
   positive_spectral_lower_bound_established=False,
   actual_signed_inverse_response_certified=False,
   remaining_314_principal_Schur_positive=False,
   full_original_Weil_form_positivity_certified=False,
   Stage_I_closed=False,F4=False,RH=False,Lean=False,
   next_cursor=(
      "RC311: prove from the original canonical explicit formula that "
      "its polynomial-core coefficients coincide with the full native "
      "even/odd model at EVERY input degree, not just P2-P5; "
      "test potential diagonal/distributional missing terms. "
      "Then address the 314-Schur spectral lower bound. "
      "Finite-degree archival regressions alone do not suffice.")
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 args=p.parse_args()
 val=run(args.replay)
 if args.replay:
  assert val==json.loads(args.output.read_text(encoding="utf-8"))
 else:
  args.output.write_text(json.dumps(val,sort_keys=True,indent=2)+"\n",
                          encoding="utf-8")
 print("RC310 VALIDATED: direct even/odd native dense-core profiles, "
       "finite-rank augmentation bounded, original canonical "
       "identification and positivity remain OPEN",flush=True)
