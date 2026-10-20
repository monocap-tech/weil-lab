#!/usr/bin/env python3
"""MG25: exact source-aware matrix-residual acceptance gate (finite algebraic pilot).

Given full-frequency LOEWNER source brackets
 Hlo <= H <= Hup, Lg <= G=F*Astar F <= Ug, S <= Sup
and an exact rational candidate B with Y=F B, certify
 R*R = H-G B-B^T G+B^T S B
 <= Hup-Gc B-B^T Gc+B^T Sup B + 2||E|| ||B|| I
where Gc=(Lg+Ug)/2 and E=(Ug-Lg)/2 >= 0.

The norm bounds are exact-rational, not floating eigen estimates.
A strict Gershgorin lower margin for Hlo-Rupper provides a source
one-step contraction in the actual ambient H metric.

This standalone run uses an explicit NONTRIVIAL 3D pole-corrected rational
surrogate, and an adversarial wide-enclosure rejection. It makes NO claim
that MG24's still-running full original 24D brackets have been validated
or imply a matrix contraction, much less a 470-source inverse or RH.
"""
import argparse,json,sys
from fractions import Fraction as Q
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

def m(x):return [[Q(y) for y in row] for row in x]
def T(a):return [list(x) for x in zip(*a)]
def mm(a,b):
    assert a and b and len(a[0])==len(b)
    return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in T(b)]
            for row in a]
def plus(a,b):
    assert len(a)==len(b) and len(a[0])==len(b[0])
    return [[x+y for x,y in zip(row,col)] for row,col in zip(a,b)]
def mul(t,a):return [[Q(t)*x for x in row] for row in a]
def sub(a,b):return plus(a,mul(-1,b))
def Id(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def shift(a,t):return plus(a,mul(t,Id(len(a))))
def diag(x):
    n=len(x)
    return [[Q(x[i]) if i==j else Q(0) for j in range(n)]
            for i in range(n)]
def sq(a):
    assert all(len(r)==len(a) for r in a)
    assert a==T(a)
    return len(a)
def psd(a):
    """Exact symmetric rational LDL/Schur elimination, including zero pivots."""
    n=sq(a)
    a=[list(r) for r in a]
    for k in range(n):
        pivot=a[k][k]
        if pivot<0:return False
        if pivot==0:
            if any(a[k][j] for j in range(k+1,n)):return False
            continue
        for i in range(k+1,n):
            for j in range(i,n):
                a[i][j]-=a[i][k]*a[j][k]/pivot
                a[j][i]=a[i][j]
        for i in range(k+1,n):
            a[i][k]=a[k][i]=Q(0)
    return True
def gersh_lower(a):
    n=sq(a)
    return min((a[i][i]-sum((abs(a[i][j]) for j in range(n)
                        if i!=j),Q(0)) for i in range(n)))
def norm_upper(a):
    """||A||_2 <= max(||A||_1, ||A||_inf), rational exact."""
    assert a and all(len(row)==len(a[0]) for row in a)
    row=max(sum((abs(x) for x in r),Q(0)) for r in a)
    col=max(sum((abs(x) for x in c),Q(0)) for c in T(a))
    return max(row,col)
def solve(a,b):
    """Exact Gaussian solve; candidate construction only, not a spectral proof."""
    n=sq(a);assert len(b)==n
    q=[list(a[i])+list(b[i]) for i in range(n)]
    mcols=len(b[0])
    for j in range(n):
        k=next((i for i in range(j,n) if q[i][j]),None)
        if k is None:raise ValueError("singular trial action surrogate")
        q[j],q[k]=q[k],q[j]
        pivot=q[j][j]
        q[j]=[x/pivot for x in q[j]]
        for i in range(n):
            if i==j:continue
            s=q[i][j]
            if s:q[i]=[x-s*y for x,y in zip(q[i],q[j])]
    return [row[n:n+mcols] for row in q]
def serialize(a):return [[str(x) for x in row] for row in a]

def residual_upper(Hlo,Hup,Lg,Ug,Sup,B):
    n=sq(Hlo)
    assert n==sq(Hup)==sq(Lg)==sq(Ug)==sq(Sup)
    assert len(B)==n and all(len(x)==n for x in B)
    assert psd(sub(Hup,Hlo)), "physical Gram bracket invalid"
    E=mul(Q(1,2),sub(Ug,Lg))
    assert psd(E), "G Loewner interval invalid"
    Gc=mul(Q(1,2),plus(Ug,Lg))
    e=norm_upper(E)
    beta=norm_upper(B)
    # B may be nonsymmetric/noncommuting; keep BOTH mixed G terms.
    result=shift(plus(
        sub(sub(Hup,mm(Gc,B)),mm(T(B),Gc)),
        mm(mm(T(B),Sup),B)),2*e*beta)
    assert result==T(result)
    margin=gersh_lower(sub(Hlo,result))
    Hcap=norm_upper(Hup)
    assert Hcap>0
    gap=max(Q(0),min(Q(1),margin/Hcap)) if margin>0 else Q(0)
    return {"Rupper":result,"margin":margin,"gap":gap,
            "G_center":Gc,"G_error_opnorm_upper":e,
            "candidate_B_opnorm_upper":beta,
            "positive_contraction_certified":bool(margin>0 and gap>0)}

def true_pole_case():
    """Independent genuine rank-one mixed pole test with Ao and s noncommuting."""
    Ao=diag([2,3,5])
    s=m([[Q(1,5)],[Q(1,3)],[Q(1,2)]])
    P=mm(s,T(s))
    A=plus(Ao,mul(-2,P))
    assert A==T(A)
    H=Id(3)
    G=A
    S=mm(A,A)
    b=s
    c=mm(Ao,s)
    sigma=mm(T(s),s)[0][0]
    predicted=plus(sub(Ao,mul(2,P)),m([[0]*3]*3))
    predictedS=plus(sub(sub(mm(Ao,Ao),mul(2,mm(c,T(b)))),
                            mul(2,mm(b,T(c)))),
                    mul(4*sigma,mm(b,T(b))))
    wrongS=plus(mm(Ao,Ao),mul(4*sigma,mm(b,T(b))))
    assert predicted==G and predictedS==S and wrongS!=S
    assert psd(G), "surrogate pole correction must remain positive"
    return H,G,S,sigma

def pilot_case(wide):
    H,G,S,sigma=true_pole_case()
    eps=Q(3) if wide else Q(1,100000)
    Lg=shift(G,-eps)
    Ug=shift(G,eps)
    Slo=shift(S,-eps)
    Sup=shift(S,eps)
    assert psd(sub(G,Lg)) and psd(sub(Ug,G))
    assert psd(sub(S,Slo)) and psd(sub(Sup,S))
    assert psd(sub(H,H))
    B=solve(S,G)  # exact least-squares candidate, not proof
    cert=residual_upper(H,H,Lg,Ug,Sup,B)
    Ractual=plus(sub(sub(H,mm(G,B)),mm(T(B),G)),
                 mm(mm(T(B),S),B))
    assert psd(sub(cert["Rupper"],Ractual)), "invalid mixed uncertainty upper"
    assert psd(Ractual), "actual squared residual cannot be negative"
    if wide:
        assert not cert["positive_contraction_certified"]
    else:
        assert cert["positive_contraction_certified"]
        assert cert["gap"]>Q(9,10)
    return {
      "fixture":"wide_adversarial_bracket" if wide else "tight_coupled_pole",
      "true_original_operator_mode":False,
      "surrogate_dimension":3,
      "nontrivial_true_rank_one_pole_correction":True,
      "full_mixed_S_pole_identity_exact":True,
      "genuine_noncommuting_pole_correction":True,
      "trial_B_is_full_matrix_not_scalar":True,
      "direct_true_residual_dominated_by_interval_upper":True,
      "source_B":[[str(x) for x in row] for row in B],
      "G_interval_half_width":str(eps),
      "rigorous_G_opnorm_error_upper":str(cert["G_error_opnorm_upper"]),
      "rigorous_B_opnorm_upper":str(cert["candidate_B_opnorm_upper"]),
      "source_metric_Gershgorin_margin":str(cert["margin"]),
      "certified_one_step_squared_residual_gap":str(cert["gap"]),
      "strict_source_one_step_contraction":cert["positive_contraction_certified"],
      "cannot_iterate_finite_source_contraction":True,
      "full470_resolvent_and_signed_cap":"OPEN"
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default=
        "artifacts/mg25_source_aware_mixed_residual_algebraic_gate.json")
    args=p.parse_args()
    a=pilot_case(False)
    b=pilot_case(True)
    assert a["strict_source_one_step_contraction"]
    assert not b["strict_source_one_step_contraction"]
    out={
        "status":"EXACT_FRACTION_SOURCE_AWARE_ROBUST_RESIDUAL_ALGEBRA_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "mg24_original_coupled_matrix_inputs_accepted":False,
        "actual_original_full_frequency_24D_trial_certified":False,
        "actual_original_470D_trial_certified":False,
        "source_geometry_general_mixed_B_trial_verified_on_surrogate":True,
        "full_rank_one_pole_mixed_source_action_verified_on_surrogate":True,
        "both_mixed_cross_terms_are_mandatory":True,
        "exact_Loewner_uncertainty_opnorm_paid":True,
        "adverse_uncertainty_refuses_promotion":True,
        "independent_original_Fourier_and_form_domain_audit":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "pilot_cases":[a,b],
        "next_original_gate":"Use verified MG24 full 24D Loewner bracket data, reconstruct original H metric, construct independently rationalized source-aware trial B, and certify Hlo-Rupper strictly positive. Even then full470 and signed51/56 remain open."
    }
    from pathlib import Path
    root=Path(__file__).resolve().parents[1]
    dst=root/args.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG25 exact robust source-aware mixed trial:",json.dumps({
        "tight_gap":float(Q(a["certified_one_step_squared_residual_gap"])),
        "adversarial_rejected":not b["strict_source_one_step_contraction"],
        "original24_470_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":main()
