"""RC303: direct native signed prime action for a polynomial source.

Reconstructs the active-prime translated *input polynomial itself*
(rather than merely summing five stored source-action columns), derives
its exact finite output and Parseval prime tail, and compares the direct
result to degree-parameterized P4/P6/P8/P10 basis formulas. Materializes
a genuinely new P10 low-output original-action column with all omitted
D-energy components and a mixed polynomial original-action certificate.

Scope: explicit finite polynomial inputs of even degree at most 10,
under imported degree-dependent endpoint/prime/kernel estimates.
The action is NOT evaluated on arbitrary Chebyshev recurrence outputs,
nor is the inherited analytic uniformity proved for unbounded degree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path

import validate_rpb108_rc240_three_trial_signed_response as legacy

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
CUT = 64
o = legacy.orig
up = legacy.up
down = legacy.down
root = legacy.root
D = (4, 6, 8, 10)
Y = {4: F(1), 6: F(-1,2), 8: F(1,3), 10: F(-1,5)}

PINS = {
    "certificates/rpb108_rc43_native_prime_head.json":
        "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
    "certificates/rpb108_rc46_native_archimedean_head.json":
        "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
    "certificates/rpb108_rc129_four_vector_joint_moment.json":
        "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc240_three_trial_signed_response.json":
        "6c41b7f196052fea179b956099fb69cc5d07813c",
    "certificates/rpb108_rc296_native_p6_action.json":
        "ff03088daa67d681e0371e92c40576d8c3219b4b",
    "certificates/rpb108_rc299_native_p8_action.json":
        "755dab2b4ab9e62b3f6a26be139ed29942647021",
    "certificates/rpb108_rc302_polynomial_action_interface.json":
        "c4d90de842526e9dfa11f1baf439e15ae3939b5b",
    "scripts/validate_rpb108_rc237_two_trial_signed_response.py":
        "d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2",
    "scripts/validate_rpb108_rc240_three_trial_signed_response.py":
        "9e1f46907a3c96d2f916d709163d0dea0db5190a",
    "scripts/validate_rpb108_rc299_native_p8_action.py":
        "886c517603d56c67107b46382b3d6b31b5be68eb",
}


def addpoly(a,b):
    z = [F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    return z


def weighted_polynomial(y):
    assert all(isinstance(d,int) and d%2==0 and 4<=d<=10
               for d in y)
    q=[F(0)]*11
    for d,v in y.items():
        for k,c in enumerate(o.legendre(d)):
            q[k]+=v*c
    assert any(q) and all(q[k]==0 for k in range(1,11,2))
    return q


def native_prime_on_polynomial(q,prime,reverse=False):
    """Actual signed translated source polynomial: no source-column sum."""
    assert len(q)==11 and all(q[k]==0 for k in range(1,11,2))
    mass=B*o.integral(o.product(q,q))
    assert mass>0
    A=sum(map(abs,q),F(0))
    der=sum((k*abs(v) for k,v in enumerate(q)),F(0))/B
    fault=F(0)
    terms=[]
    for row in prime["active_prime_powers"]:
        el,eh=map(F,(row["translation_lower"],row["translation_upper"]))
        cl,ch=map(F,(row["coefficient_lower"],row["coefficient_upper"]))
        ell=(el+eh)/2;c=(cl+ch)/2
        de=(eh-el)/2;dc=(ch-cl)/2
        assert de>=0 and dc>=0 and ch>=0
        fault+=2*(dc*root(mass)+ch*root(
            2*de*A*A+2*B*de*de*der*der))
        for sign in (-1,1):
            off=sign*ell/B
            l=max(F(-1),-1-off)
            r=min(F(1),1-off)
            poly=[-c*sum((q[k]*comb(k,m)*off**(k-m)
                          for k in range(m,len(q))),F(0))
                  for m in range(len(q))]
            terms.append((l,r,poly))
    knots=sorted({F(-1),F(1)} | {
        v for l,r,_ in terms for v in (l,r)})
    segments=[]
    for l,r in zip(knots,knots[1:]):
        mid=(l+r)/2
        poly=[sum((v[k] for a,b,v in terms if a<mid<b),F(0))
              for k in range(len(q))]
        segments.append((l,r,poly))
    assert len(terms)==14 and len(segments)==15
    for l,r,v in segments:
        reflection=next(vv for a,b,vv in segments
                        if a==-r and b==-l)
        assert reflection==[(-1)**k*c for k,c in enumerate(v)]
    norm=B*sum((
        o.integral(o.product(v,v),l,r)
        for l,r,v in segments),F(0))
    coefficients=[]
    for n in range(CUT+1):
        if n%2:
            coefficients.append(F(0))
            continue
        pieces=[o.integral(o.product(v,o.legendre(n)),l,r)
                for l,r,v in segments]
        if reverse:pieces.reverse()
        coefficients.append(F(2*n+1,2)*sum(pieces,F(0)))
    finite=sum((o.mass(n)*v*v for n,v in enumerate(coefficients)),
               F(0))
    tail=norm-finite
    assert tail>=0
    assert all(coefficients[n]==0 for n in range(1,CUT+1,2))
    return coefficients,up(tail),up(fault),dict(
        active_prime_powers=7,signed_translation_terms=14,
        exact_piecewise_segments=15,parity="even",
        direct_polynomial_mass_squared=str(mass),
        full_prime_L2_mass_squared=str(norm),
        signed_finite_prime_L2_mass_squared=str(finite),
        omitted_prime_L2_energy_upper=str(up(tail)),
        direct_prime_arithmetic_fault_upper=str(up(fault)))


def generic_low_action(d,reg,prime,eps,sl,sh,reverse=False):
    """RC299 degree-parameterized exact formula; explicitly now d=10."""
    assert d in (4,6,8,10) and 65>3*d+1 and sl>0 and sl<=sh
    regpoly=legacy.trial.regular_poly(d,reg)
    rc=[o.project(regpoly,n) for n in range(len(regpoly))]
    pc,pt,pfault,segs=legacy.trial.prime_poly(d,prime,reverse)
    assert len(pc)==65 and len(segs)==15
    rtail=up(sum((o.mass(n)*v*v for n,v in enumerate(rc)
                  if n>CUT),F(0)))
    phi=[F(11,20)**k/factorial(k) if k%2==d%2
         else F(0) for k in range(41)]
    moment=B*o.integral(o.product(o.legendre(d),phi))
    pole=[2*(-1)**d*moment*v for v in phi]
    oc=[o.project(pole,n) for n in range(CUT+1)]
    polefault=up(16*B*(2*F(11,20)**41/factorial(41))*
                 root(o.mass(d)))
    ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0))
    lh=ll+2*F(1,3)**201/(201*(1-F(1,9)))
    out=[];rnd=F(0)
    for n in range(CUT+1):
        if (n-d)%2:
            out.append(dict(degree=n,coefficient="0",radius="0"))
            continue
        h=(2*o.H(2*n)-2*o.H(n)+F(1,2*n+1)) if n==d else F(
            2*n+1,abs(n-d)*(n+d+1))
        lo=h-(lh if n==d else 0)-rc[n]+pc[n]+oc[n]-(
            F(789,125) if n==d else 0)
        hi=h-(ll if n==d else 0)-rc[n]+pc[n]+oc[n]-(
            F(789,125) if n==d else 0)
        vals=[v/(o.H(n)+s)+F(n==d)
              for v in (lo,hi) for s in (sl,sh)]
        c=down((min(vals)+max(vals))/2)
        radius=max(c-min(vals),max(vals)-c)
        rnd+=o.mass(n)*(o.H(n)+sh)*radius*radius
        out.append(dict(degree=n,coefficient=str(c),
                        radius=str(up(radius))))
    first=66
    comp=dict(
        finite_rounding=up(rnd),
        endpoint_omitted_output=up(
            3*B/((o.H(first)+sl)*(64-d)**2)),
        regular_omitted_output=up(rtail/(o.H(first)+sl)),
        prime_omitted_output=up(pt/(o.H(first)+sl)),
        regular_kernel=up((2*B*eps)**2*o.mass(d)/sl),
        prime_arithmetic=up(pfault**2/sl),
        pole_Taylor=up(polefault**2/sl))
    total=up(sum((root(v) for v in comp.values()),F(0))**2)
    assert total>0 and all(v>=0 for v in comp.values())
    assert all(row["coefficient"]==row["radius"]=="0"
               for row in out if row["degree"]%2)
    return dict(input="P"+str(d),input_degree=d,parity="even",
        finite_original_D_action=out,
        D_energy_component_squared_errors={
            k:str(v) for k,v in comp.items()},
        complete_original_action_D_error_squared_upper=str(total),
        original_output_cutoff=64,first_omitted_even_degree=first,
        complete_active_prime_pairs=7,all_omitted_outputs_paid=True),dict(
            prime_coefficients=pc,prime_tail=pt,
            prime_fault=pfault,regular_coefficients=rc,
            regular_poly=regpoly,pole_coefficients=oc,
            log2_lower=ll,log2_upper=lh)


def mixed_source_original_low(y,parts,reg,prime,eps,sl,sh,reverse):
    """Direct polynomial prime action; other linear original-form parts."""
    assert tuple(sorted(y))==D and len(y)==4
    q=weighted_polynomial(y)
    expectedmass=sum((o.mass(d)*v*v for d,v in y.items()),F(0))
    assert B*o.integral(o.product(q,q))==expectedmass
    pc,pt,pfault,proof=native_prime_on_polynomial(q,prime,reverse)
    for n in range(CUT+1):
        expected=sum((y[d]*parts[d][1]["prime_coefficients"][n]
                      for d in D),F(0))
        assert pc[n]==expected, ("independent signed prime action",n)
    regpoly=[F(0)]
    for d in D:
        terms=parts[d][1]["regular_poly"]
        regpoly=addpoly(regpoly,[y[d]*c for c in terms])
    rc=[o.project(regpoly,n) for n in range(len(regpoly))]
    for n in range(CUT+1):
        assert rc[n]==sum((y[d]*parts[d][1][
            "regular_coefficients"][n] for d in D),F(0))
    rtail=up(sum((o.mass(n)*v*v for n,v in enumerate(rc)
                  if n>CUT),F(0)))
    oc=[sum((y[d]*parts[d][1]["pole_coefficients"][n]
             for d in D),F(0)) for n in range(CUT+1)]
    ll=parts[D[0]][1]["log2_lower"]
    lh=parts[D[0]][1]["log2_upper"]
    for d in D:assert (parts[d][1]["log2_lower"],
        parts[d][1]["log2_upper"])==(ll,lh)
    out=[];rnd=F(0)
    for n in range(CUT+1):
        if n%2:
            out.append(dict(degree=n,coefficient="0",radius="0"))
            continue
        endpoint=sum((y[d]*(
            2*o.H(2*n)-2*o.H(n)+F(1,2*n+1)
            if n==d else F(2*n+1,abs(n-d)*(n+d+1)))
            for d in D),F(0))
        diagonal=y.get(n,F(0))
        fixed=endpoint-rc[n]+pc[n]+oc[n]-F(789,125)*diagonal
        # Unknown log(2) lies between ll and lh, signed diagonal
        # contributions fully enclosed for arbitrary source signs.
        vals=[(fixed-L*diagonal)/(o.H(n)+s)+diagonal
              for L in (ll,lh) for s in (sl,sh)]
        c=down((min(vals)+max(vals))/2)
        rad=up(max(c-min(vals),max(vals)-c))
        rnd+=o.mass(n)*(o.H(n)+sh)*rad*rad
        out.append(dict(degree=n,coefficient=str(c),radius=str(rad)))
        # Direct mixed form and linear sum of the *actual* individual
        # intervals must overlap. Finite rounding is paid on both.
        a=sum((y[d]*F(parts[d][0]["finite_original_D_action"][n][
            "coefficient"]) for d in D),F(0))
        ar=sum((abs(y[d])*F(parts[d][0][
            "finite_original_D_action"][n]["radius"])
            for d in D),F(0))
        assert abs(a-c)<=ar+rad,("mixed nominal action mismatch",n)
    first=66
    # Endpoint omitted output controlled by explicit Minkowski
    # combination of the separately inherited basis bounds.
    endpoint_amp=sum((abs(y[d])*root(F(parts[d][0][
        "D_energy_component_squared_errors"][
        "endpoint_omitted_output"])) for d in D),F(0))
    source_norm=root(expectedmass)
    pole_tau=2*F(11,20)**41/factorial(41)
    polefault=up(16*B*pole_tau*source_norm)
    components=dict(
        finite_rounding=up(rnd),
        endpoint_omitted_output=up(endpoint_amp**2),
        regular_omitted_output=up(rtail/(o.H(first)+sl)),
        prime_omitted_output=up(pt/(o.H(first)+sl)),
        regular_kernel=up((2*B*eps)**2*expectedmass/sl),
        prime_arithmetic=up(pfault**2/sl),
        pole_Taylor=up(polefault**2/sl))
    total=up(sum((root(v) for v in components.values()),F(0))**2)
    return dict(
        input_even_legendre_coefficients={str(d):str(y[d]) for d in D},
        degree=10,original_output_cutoff=64,
        finite_original_D_action=out,
        directly_evaluated_prime_source=proof,
        D_energy_component_squared_errors={
            k:str(v) for k,v in components.items()},
        complete_original_D_error_squared_upper=str(total),
        all_omitted_output_terms_paid=True,
        original_action_direct_prime_not_five_column_interpolation=True,
        prime_translation_exactly_matches_signed_component_action=True,
        regular_and_pole_source_linearity_regression_exact=True,
        original_output_beyond_64_not_individually_materialized=True,
        inherited_endpoint_tail_bound_combined_by_Minkowski=True)


def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        digest=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw
                            ).hexdigest()
        assert digest==sha,(path,"pinned source changed")
        if path.endswith(".json"):
            data[path]=json.loads(raw)
    def get(s):
        return data["certificates/rpb108_rc"+s+".json"]
    prior=get("302_polynomial_action_interface")
    assert prior["N_new_V5_not_subset_V5_certified"]
    assert prior["arbitrary_even_polynomial_input_degree_above_eight_supported"] is False
    metric=get("129_four_vector_joint_moment")
    sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<sl<=sh
    arch=get("46_native_archimedean_head")
    reg=list(map(F,arch["regular_kernel_coefficients"]))
    eps=F(arch["regular_kernel_uniform_error_upper"])
    prime=get("43_native_prime_head")
    assert len(prime["active_prime_powers"])==7
    previous={
        4:get("240_three_trial_signed_response")[
            "parity_three_trial_signed_response_certificates"][0][
            "new_complete_original_action"],
        6:get("296_native_p6_action")["new_native_P6_original_action"],
        8:get("299_native_p8_action")["new_native_P8_original_action"]
    }
    columns={}
    for d in (reversed(D) if reverse else D):
        act,parts=generic_low_action(d,reg,prime,eps,sl,sh,reverse)
        if d in previous:
            for k in ("finite_original_D_action",
                      "D_energy_component_squared_errors",
                      "complete_original_action_D_error_squared_upper"):
                assert act[k]==previous[d][k],(
                    "exact original action regression",d,k)
        columns[d]=(act,parts)
        print("RC303: native original P"+str(d)+" reconstructed",
              flush=True)
    new=columns[10][0]
    assert new["finite_original_D_action"][10]["coefficient"]!="0"
    mix=mixed_source_original_low(Y,columns,reg,prime,eps,sl,sh,reverse)
    assert mix["prime_translation_exactly_matches_signed_component_action"]
    assert F(mix["complete_original_D_error_squared_upper"])>0
    print("RC303: direct mixed-degree prime polynomial verified",
          flush=True)

    # Scope of the *actual* result: the signed prime source polynomial
    # now has an exact direct finite-output evaluator and Parseval tail
    # for the specified family, NOT a dimension-free analytic theorem
    # or certified repeated infinite-dimensional operator action.
    return dict(
        milestone="RC303",
        starting_commit="be83e44cdccc7cb2435a3630bf782c19ee34e83e",
        input_git_blob_pins=PINS,
        exact_P4_P6_P8_low_original_action_regressions=True,
        first_new_input_degree_beyond_previous_V5=10,
        new_native_P10_original_action=new,
        direct_even_input_polynomial_degree_cap=10,
        direct_native_prime_translation_available_for_signed_polynomials=True,
        direct_prime_source_support_bound_tested_for_degree_10=True,
        direct_prime_15_segments_and_full_omitted_L2_energy_computed=True,
        mixed_signed_even_polynomial_action=mix,
        rank317_P10_augmentation_not_yet_certified=True,
        complete_original_output_65_through_2048_for_P10_not_certified=True,
        dimension_free_even_input_degree_uniform_analytic_tail_not_proved=True,
        arbitrary_Chebyshev_operator_recurrence_not_executed=True,
        full_original_Weil_form_positivity_not_certified=True,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor=(
          "RC304: extend direct input-polynomial signed prime projector "
          "from degree-64 to degree-2048 output for P10 and mixed "
          "sources, attach rank-317 physical P10 augmentation, "
          "and establish source-degree-uniform tail/operator bounds "
          "before any repeated Chebyshev inverse action."))
        

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--replay",action="store_true")
    a=p.parse_args()
    result=run(a.replay)
    if a.replay:
        assert result==json.loads(a.output.read_text(encoding="utf-8"))
    else:
        a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",
                            encoding="utf-8")
    print("RC303 VALIDATED: native P10 and direct mixed signed prime "
          "source; Stage I OPEN",flush=True)
