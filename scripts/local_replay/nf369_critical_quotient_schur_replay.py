#!/usr/bin/env python3
"""NF369: independent dyadic interval replayer of the actual 4x4 projected quotient Schur.
Reads output of the original-native producer. Never promotes a finite probe to full Schur.
"""
import argparse,json,sys
from fractions import Fraction as F
sys.set_int_max_str_digits(100000)

def dyad(p):
    n,e=map(int,p)
    return F(n<<e) if e>=0 else F(n,1<<(-e))
def interval(ball):
    c,r=map(dyad,ball)
    assert r>=0
    return c-r,c+r
def center_radius(ball):
    c,r=map(dyad,ball)
    assert r>=0
    return c,r
def matrix(obj,key):
    A=obj[key]
    assert len(A)==4 and all(len(row)==4 for row in A)
    return [[center_radius(A[i][j]) for j in range(4)] for i in range(4)]
def lower_admissible(A,shift):
    lo=[[A[i][j][0]-A[i][j][1] for j in range(4)] for i in range(4)]
    hi=[[A[i][j][0]+A[i][j][1] for j in range(4)] for i in range(4)]
    # Symmetry is an interval intersection, not equality of rounded centers.
    for i in range(4):
        for j in range(4):
            assert max(lo[i][j],lo[j][i]) <= min(hi[i][j],hi[j][i])
    M=[[(A[i][j][0]+A[j][i][0])/2 for j in range(4)] for i in range(4)]
    R=[[max(abs(M[i][j]-lo[i][j]),abs(hi[i][j]-M[i][j]),
            abs(M[i][j]-lo[j][i]),abs(hi[j][i]-M[i][j])) for j in range(4)] for i in range(4)]
    rho=max(sum(row,F(0)) for row in R)
    return [[M[i][j]-(rho+shift)*F(i==j) for j in range(4)] for i in range(4)],rho
def ldlt_pd(A):
    L=[[F(i==j) for j in range(4)] for i in range(4)]
    d=[]
    for k in range(4):
        v=A[k][k]-sum((L[k][i]**2*d[i] for i in range(k)),F(0))
        if v<=0:return False,k
        d.append(v)
        for j in range(k+1,4):
            L[j][k]=(A[j][k]-sum((L[j][i]*L[k][i]*d[i] for i in range(k)),F(0)))/v
    return True,None
def main():
    p=argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("--report",required=True)
    a=p.parse_args()
    x=json.load(open(a.input))
    assert x["selected_rank"]==242 and x["existing_critical_witness_count"]==4
    assert not x["nf369_actual_full_complement_upper_computed"]
    assert x["full_original_odd_mixed_sign_certified"] is False if "full_original_odd_mixed_sign_certified" in x else True
    W=matrix(x,"nf369_original_four_mode_signed_Gram_native")
    P=matrix(x,"nf369_selected_critical_Gram_native")
    B=matrix(x,"nf369_selected_to_original_quotient_signed_coupling_native")
    C=matrix(x,"actual_exterior_signed_Gram_native")
    D=matrix(x,"nf369_quotient_Galerkin_correction_lower_native")
    for i in range(4):
        for j in range(4):
            # Recompose W(F,F)=W(PF,PF)+W(PF,QF)+W(QF,PF)+W(QF,QF).
            lower=sum((v[0]-v[1] for v in (P[i][j],B[i][j],B[j][i],C[i][j])),F(0))
            upper=sum((v[0]+v[1] for v in (P[i][j],B[i][j],B[j][i],C[i][j])),F(0))
            assert lower<=W[i][j][0]+W[i][j][1]
            assert upper>=W[i][j][0]-W[i][j][1]
    delta=F(x["nf369_quotient_response_remainder_upper"])
    assert delta>0
    # Actual p+span(QF) Schur = P - D_E. Dlow <= D_E <= Dlow+delta*I.
    # Thus P-Dlow-delta*I <= actual Galerkin Schur <= P-Dlow.
    S=[[(P[i][j][0]-D[i][j][0],P[i][j][1]+D[i][j][1]) for j in range(4)] for i in range(4)]
    Alo,rho=lower_admissible(S,delta)
    positive,failed_pivot=ldlt_pd(Alo)
    # A negative diagonal even in the UPPER bound is a valid finite negative extension.
    negative_axes=[i for i in range(4) if S[i][i][0]+S[i][i][1]<0]
    # The identity D_E>=D_low and genuine signed positivity of Q imply this is a method result.
    report=dict(
        standing="NF369 original 4x4 quotient Galerkin only, inherited form/domain premises",
        full_infinite_schur_upper=False,
        fixed_rank=242,original_four_mode_count=4,
        matched_projection_recomposition=True,
        quotient_schur_positive_certified=positive,
        finite_negative_extension_axis_certified=bool(negative_axes),
        negative_axes=negative_axes,
        inconclusive=not positive and not negative_axes,
        radius_operator_upper_approx=float(rho),
        finite_probe_inverse_remainder_upper_approx=float(delta),
        conditional_original_domain_review="OPEN",
        W_ODD_NEG="OPEN",RH="OPEN")
    with open(a.report,"w") as f:json.dump(report,f,indent=2);f.write("\n")
    print("NF369 original complete four-mode/selected/quotient exact rational recomposition PASS")
    print("Finite 4-probe Schur positive",positive,"negative axis",negative_axes,
          "inconclusive",report["inconclusive"])
    print("Full infinite exterior Schur UPPER remains UNCOMPUTED")
if __name__=="__main__":main()
