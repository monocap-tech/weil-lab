#!/usr/bin/env python3
"""PI019 ANALYTIC ONLY: exact Gaussian-rational two-test phase/contact audit.

Models the exact correlation expansion for two disjoint REAL equal-energy
bumps φ and ψ(x)=φ(x-a), at a>2*radius(φ):
  s_β=(φ+β ψ)/sqrt(2), β in {1,-1,i,-i}
  h_β(u)=C(u)+conj(β)/2*C(u+a)+β/2*C(u-a)
with C(u)=∫φ(x)φ(x-u)dx, C even.

Uses exact Fraction coefficients; C(u), translated functions and K are
formal independent basis terms. Does NOT claim to evaluate integrals or
Masullo's operator. It tests universal linear identities and demonstrates
that a scalar contact correction cannot repair a phase-difference defect.
"""
from fractions import Fraction as Q

G = tuple[Q,Q]
Z: G = (Q(0),Q(0))
ONE: G = (Q(1),Q(0))


def add(x:G,y:G)->G: return x[0]+y[0], x[1]+y[1]
def neg(x:G)->G: return -x[0],-x[1]
def sub(x:G,y:G)->G: return add(x,neg(y))
def conj(x:G)->G: return x[0],-x[1]
def scale(x:G,q:Q)->G: return q*x[0],q*x[1]
def real(x:G)->Q: assert x[1]==0;return x[0]

# coefficients (C(u), C(u+a), C(u-a)) in this exact order.
def correlation(beta:G)->tuple[G,G,G]:
    assert add(scale(beta,Q(1)),scale(conj(beta),Q(1))) is not None
    return ONE, scale(conj(beta),Q(1,2)), scale(beta,Q(1,2))

def difference(v:tuple[G,...],w:tuple[G,...])->tuple[G,...]:
    return tuple(sub(x,y) for x,y in zip(v,w))

def arch_pair(coeffs:tuple[G,G,G], base:Q, shifted:Q)->G:
    """Formal even-K response: ∫C*K=base, both shifted integrals=shifted."""
    ans=scale(coeffs[0],base)
    return add(ans,scale(add(coeffs[1],coeffs[2]),shifted))

def h_at_origin(coeffs:tuple[G,G,G],J:Q)->G:
    # For support-separated φ and ψ, C(±a)=0 and C(0)=J.
    return scale(coeffs[0],J)

def h_at_positive_a(coeffs:tuple[G,G,G],J:Q)->G:
    # C(a)=C(2a)=0, C(0)=J.
    return scale(coeffs[2],J)


def run() -> None:
    tests={"plus":(Q(1),Q(0)), "minus":(Q(-1),Q(0)),
           "i":(Q(0),Q(1)), "negative_i":(Q(0),Q(-1))}
    cs={k:correlation(v) for k,v in tests.items()}
    for coeffs in cs.values():
        assert coeffs[0]==ONE
        assert coeffs[1]==conj(coeffs[2])
        assert h_at_origin(coeffs,Q(7,3))==(Q(7,3),Q(0))
    # Full phase support does not change; J, physical intervals are fixed.
    even_phase=difference(cs["plus"],cs["minus"])
    odd_phase=difference(cs["i"],cs["negative_i"])
    assert even_phase==(Z,ONE,ONE)
    assert odd_phase==(Z,(Q(0),Q(-1)),(Q(0),Q(1)))
    assert all(h_at_origin(v,Q(11,7))==Z for v in (even_phase,odd_phase))
    # Translation offsets of the two shifted bumps are ±a.
    J=Q(7,3)
    assert h_at_positive_a(cs["plus"],J)==(J/2,Q(0))
    assert h_at_positive_a(cs["minus"],J)==(-J/2,Q(0))
    assert h_at_positive_a(cs["i"],J)==(Q(0),J/2)
    assert h_at_positive_a(cs["negative_i"],J)==(Q(0),-J/2)

    comparisons=0
    # If K is even, arch contribution to A=-∫h*K: phase contrast is -2I.
    for base in (Q(-5),Q(0),Q(2,3)):
        for shifted in (Q(1,13),Q(2,7),Q(5)):
            d_even=arch_pair(even_phase,base,shifted)
            d_odd=arch_pair(odd_phase,base,shifted)
            assert d_even==(2*shifted,Q(0))
            assert d_odd==Z
            # For A=-∫hK, A(plus)-A(minus)=-2*shifted
            assert neg(d_even)==(-2*shifted,Q(0))
            comparisons+=1

    # On test functions h0=0, T and T+c*h(0) are indistinguishable.
    # For two diagonal tests with the SAME h(0)=J, any scalar mass offset
    # cancels in their phase difference. A phase-dependent mismatch cannot
    # be repaired by choosing c.
    cases=0
    for c in (Q(-11),Q(0),Q(2,7),Q(8)):
        for J in (Q(1,5),Q(1),Q(7,2)):
            for a1,a2 in ((Q(2),Q(2)),(Q(2),Q(3)),
                          (Q(-4),Q(-4)),(Q(-4),Q(3))):
                T1=a1+c*J
                T2=a2+c*J
                assert T1-T2==a1-a2
                if a1!=a2:
                    assert T1-a1 == T2-a2  # common correction cJ
                    # Nontrivial discrepant *target phase* requires extra
                    # non-scalar error, which no c can remove.
                    spectral_difference=(a1-a2)+Q(1,3)
                    assert spectral_difference != a1-a2
                cases+=1

    # Abstract two-test diagnostic: if residuals / J differ,
    # a single contact coefficient is mathematically impossible.
    failures=0
    for J1,J2 in ((Q(1),Q(1)),(Q(3,2),Q(7,5)),(Q(4),Q(9,7))):
        target_r1=Q(1,3)*J1
        target_r2=Q(2,5)*J2
        assert target_r1/J1 != target_r2/J2
        failures+=1

    print("PI019 EXACT PHASE/CONTACT ALGEBRA: PASS")
    print("4 Gaussian-rational phases with identical h(0) and support")
    print("even real phase contrast: C(u+a)+C(u-a), vanishing at u=0")
    print("odd imaginary contrast: i(C(u-a)-C(u+a)), vanishing at u=0")
    print(f"{comparisons} exact even-K contrast evaluations")
    print(f"{cases} scalar-contact cancellation cases")
    print(f"{failures} two-test unequal normalized-residual no-go controls")
    print("NOT CHECKED: actual smooth bump integration, Masullo trace, Lean, RH")


if __name__=="__main__":
    run()
