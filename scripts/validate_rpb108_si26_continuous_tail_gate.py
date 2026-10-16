#!/usr/bin/env python3
"""SI26 — certify the ENTIRE omitted first-Legendre tail of SI23's continuous
outer bands, and a TWO-SIDED original physically supported odd inverse
comparison for the SI25 eight-feature reference.

The result rules out completing the rank-one pole threshold by restoring
higher moments on THESE TWO OUTER BANDS ALONE. It does NOT rule out a stronger
original A_o or positivity of the original signed Weil operator.

Acceptance inequalities are exact fractions, not floating approximations.
"""
from fractions import Fraction as F

from validate_rpb108_si25_first_moment_bessel import (
    FEATURES, SIX_CENTERS, SIX_RADII, SIX_DELTAS,
    MOMENT_IDS, feature_terms, linear_interval, bilinear_interval,
)
from validate_rpb108_si21_odd_jensen_four import (
    B, PI, KAPPA, outward, midpoint, solve_exact, variational_lower,
    certify_original_window,
)
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

def linear_positive_remainder_upper(q, matrix, z):
    """Upper bound on q* M^-1 q with full exact physical interval enclosures.

    For actual PSD M >= diag(1/gamma), let w = q - Mz. Then
      q*M^-1 q = 2 z*q - z*Mz + w*M^-1 w
                <= upper_dual + gamma_max ||w||^2.
    The upper dual and every residual interval retain all SIGNED off-diagonal
    terms, and the expression holds with the true supported physical Gram.
    """
    n=len(q)
    upper=F(0)
    residual_squared=F(0)
    for i in range(n):
        t=2*z[i]
        upper += t*(q[i][1] if t>=0 else q[i][0])
    for i in range(n):
        for j in range(n):
            t=z[i]*z[j]
            # Negative of a signed matrix quadratic: choose LOWER matrix
            # endpoint for positive t, and UPPER for negative t.
            upper -= t*(matrix[i][j][0] if t>=0 else matrix[i][j][1])

    res_intervals=[]
    for i in range(n):
        lo,hi=q[i]
        for j in range(n):
            t=z[j]
            if t>=0:
                lo -= t*matrix[i][j][1]
                hi -= t*matrix[i][j][0]
            else:
                lo -= t*matrix[i][j][0]
                hi -= t*matrix[i][j][1]
        res_intervals.append((lo,hi))
        rad=max(abs(lo),abs(hi))
        residual_squared+=rad*rad
    assert residual_squared>0
    return upper,residual_squared,res_intervals


def certify():
    assert len(FEATURES)==8 and MOMENT_IDS==(4,5)
    assert len(SIX_CENTERS)==len(SIX_RADII)==len(SIX_DELTAS)==6
    original=[certify_original_window(c,d)
              for c,d in zip(SIX_CENTERS[:4],SIX_DELTAS[:4])]
    assert all(m>KAPPA+d for m,d in zip(original,SIX_DELTAS[:4]))
    si13=certify_window()
    delta=F(1399,1000)
    assert si13>KAPPA+delta
    r=F(3,100)
    assert SIX_RADII[4]==r==SIX_RADII[5]
    assert SIX_DELTAS[4]==delta==SIX_DELTAS[5]
    assert SIX_CENTERS[4]==F(1,4) and SIX_CENTERS[5]==F(7,20)

    # The true frequency Hilbert map H(u)(x)=sin(2pi(c+ru)x)
    # is projected onto span(1,u) in L²([-1,1],du).
    # Its signed original continuous operator remainder after the
    # first two Legendre moments is PSD:
    #
    #   R_J = T_J - 4r|g0><g0| - (4r/3)|g1><g1| >=0.
    #
    # Orthogonal projection minimizes L² error, so subtracting the
    # first-order Taylor polynomial h_c + r u h'_c yields the bound
    #   |H(u,x)-h_c(x)-r u h'_c(x)|
    #     <= ((2*pi*r)^2/2) x² u².
    #
    # Integrate its SQUARED bound in x,u:
    #   int_-B^B x^4 dx=2 B^5/5,
    #   int_-1^1 u^4 du=2/5.
    # Since T_J =2r int_-1^1 |H(u)><H(u)|du,
    #   Tr R_J <= 2r (2pi r)^4 B^5 /25.
    # This is an absolute operator-norm bound, not a source-only test.
    #
    # Both disjoint intervals have margin delta, thus with
    # C23 = C8 + delta(R_J1+R_J2):
    #   0<=C23-C8<=epsilon I, epsilon=delta*2*single_tail.
    single_tail=2*r*(2*PI[1]*r)**4*B**5/F(25)
    epsilon=2*delta*single_tail
    assert F(0)<single_tail<F(5,10**6)
    assert F(0)<epsilon<F(14,10**6)   # <1.4e-5
    assert epsilon/KAPPA<F(14,1000)   # <1.4% inverse perturbation ratio

    # Reconstruct the ENTIRE actual eight-feature physical signed Gram
    # and odd source intervals. The degree-one moments use the SAME
    # rigorous composite Simpson fourth derivative bound as SI25.
    gamma=[4*t*d/(3 if deg else 1) for c,t,d,deg in FEATURES]
    tau=[]
    for c,t,d,deg in FEATURES:
        beta=2*PI[1]*t*B
        if deg==0:
            err=beta**4/F(180)
        else:
            err=3*(4*beta**3+beta**4)/F(180)*(F(1,4))**4
        tau.append(err)
    assert max(tau)<F(11,10**6)

    q=[]
    terms=[]
    for i,(c,t,d,deg) in enumerate(FEATURES):
        tv=feature_terms(c,t,deg)
        terms.append(tv)
        lo,hi=linear_interval(tv)
        err=F(3,4)*tau[i]
        q.append(outward((lo-err,hi+err),12))
    H=[]
    for i in range(8):
        row=[]
        for j in range(8):
            lo,hi=bilinear_interval(terms[i],terms[j])
            err=4*B*(tau[i]+tau[j])
            row.append(outward((lo-err,hi+err),12))
        H.append(row)
    assert all(H[i][j]==H[j][i] for i in range(8) for j in range(8))

    M=[[(lo/KAPPA+(1/gamma[i] if i==j else 0),
         hi/KAPPA+(1/gamma[i] if i==j else 0))
        for j,(lo,hi) in enumerate(H[i])] for i in range(8)]
    z=solve_exact([[midpoint(span) for span in row] for row in M],
                  [midpoint(span) for span in q])
    lower_correction=variational_lower(q,M,z)
    dual_upper,residual_squared,residual_intervals=linear_positive_remainder_upper(
        q,M,z)
    upper_correction=dual_upper+max(gamma)*residual_squared
    assert F(0)<lower_correction<upper_correction

    Slo0,Shi0=sinh_bounds(B)
    Slo,Shi=Slo0-B,Shi0-B
    # The reference C8 is an EXACT physical positive rank-eight operator,
    # therefore Woodbury is an IDENTITY for its inverse (and merely an
    # upper bound on the unknown original A_o inverse).
    #
    # Correction UPPER -> inverse LOWER, opposite to SI25's direction.
    C8_pole_lower=2*(Slo/KAPPA-upper_correction/KAPPA**2)
    C8_pole_upper=2*(Shi/KAPPA-lower_correction/KAPPA**2)
    assert 0<C8_pole_lower<C8_pole_upper
    assert C8_pole_lower>F(2)  # certify the full reference pole fails <=1
    assert C8_pole_upper<F(13,6) # reproduces the SI25 upper

    # C8<=C23<=C8+epsilon I by PSD Bessel tail and trace bound.
    # Functional calculus gives for t>=kappa:
    #     1/(t+epsilon) >= (1-epsilon/kappa)/t.
    # Thus for the actual original s source:
    # 2<s,C23^-1 s> >= (1-epsilon/kappa) 2<s,C8^-1 s>.
    C23_pole_lower=(1-epsilon/KAPPA)*C8_pole_lower
    assert C23_pole_lower>F(197,100)  # >1.97, far beyond pole threshold 1

    # Since C23 >= C8, the possible *improvement* in reference pole
    # response is itself bounded in absolute magnitude:
    # 0 <= response(C8)-response(C23)
    #   <= epsilon/kappa * response(C8) <= epsilon/kappa * C8_pole_upper.
    maximum_tail_gain=(epsilon/KAPPA)*C8_pole_upper
    assert maximum_tail_gain<F(3,100)  # <0.03

    print("SI26 PASS: complete continuous outer-band Legendre remainder and two-sided reference inverse")
    print("signed original SI13 complete frequency-band m min:",float(si13))
    print("single outer-band PSD tail operator norm UPPER:",float(single_tail))
    print("two weighted tails operator norm epsilon UPPER:",float(epsilon))
    print("full SI25 eight-feature reference pole inverse LOWER:",float(C8_pole_lower))
    print("full SI25 eight-feature reference pole inverse UPPER:",float(C8_pole_upper))
    print("full SI23 continuous outer-band reference pole inverse LOWER:",float(C23_pole_lower))
    print("maximum possible extra inverse response gain from ALL higher outer-band moments:",
          float(maximum_tail_gain))
    print("rational residual squared upper / gamma_max:",float(residual_squared),float(max(gamma)))
    print("eight residual interval radii:",
          [float(max(abs(a),abs(b))) for a,b in residual_intervals])
    print("Original full A_o may be much stronger than C23; NO original pole lower")
    print("NO complete signed K BS, original Weil positivity, Stage I, F4, Lean, or RH")

if __name__=="__main__":
    certify()
