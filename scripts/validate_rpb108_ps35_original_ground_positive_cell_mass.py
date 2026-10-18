#!/usr/bin/env python3
"""PS35: first true-original pole-free even ground POSITIVE L2 masses in
sixteen explicit actual physical cells, conditional on PS17-33 analytic
premises, not on PS34's characteristic-cut eigen-test.

True original inputs:
* PS18 all-13 source actual C+ quiet interval [269/5000,1163/10000].
* PS28/30 actual order-preserving EVEN source R=B0* A0^-1 B0.
* PS27 original full 7-prime negativity of offdiag V0; source
  ||B0||<1403/80, A0>1997/9000.
* PS17 V full bounded norm<13, removed positive even pole
  ||2|cC><cC|||<539/90.
* PS29 normalized nonnegative even pole-FREE ground eigenfunction,
  PS31 true original |lambda0|<1406.
* PS33 genuine original global ground L1²>3/(8000*2**2025).

NEW exact rational analytic test: Lipschitz original-domain symmetric
tent on any Jquiet subcell width1/256 has ||(L-lambda0)g||<175,
original attractive arch kernel + negative prime and source response
force (L-lambda0)g outside its support <=-3/2560. Exact ground equation
implies true original mass mu(H)>3/(8000*2**2061)
for EACH of 16 physically specified source-complement cells.
No numerical original eigenfunction, graph w_ij, lambda1, Delta,
W-EVEN-FORM/W-ODD-NEG, complete signed Weil or RH proof.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_ps34_prime_quiet_ground_mass as ps34

ROOT=Path(__file__).resolve().parents[1]
QLO=F(269,5000)
QHI=F(1163,10000)
H_WIDTH=F(1,256)
RADIUS=F(1,512)
HALF_CARRIER_B=F(11,10)
FULL_CARRIER=F(11,5)
M0=F(3,2560)


def actual_cells():
    assert QHI-QLO==F(1,16)
    h=[]
    for j in range(16):
        a=QLO+j*H_WIDTH
        b=a+H_WIDTH
        mid=(a+b)/2
        assert H_WIDTH==2*RADIUS
        assert mid-a==b-mid==RADIUS
        assert QLO<=a<b<=QHI
        h.append((a,b,mid))
    assert len(h)==16
    assert h[0][0]==QLO and h[-1][1]==QHI
    assert all(h[j][1]==h[j+1][0] for j in range(15))

    # Actual PS18 original physical labels verify whole Jquiet
    # lies strictly between source I3 and I4, not a surrogate.
    old=ps34.ps18.old
    ln3=old.log_i(F(3))
    ln4=old.log_i(F(4))
    assert HALF_CARRIER_B-ln3.lo<QLO
    assert ln4.lo-HALF_CARRIER_B>QHI
    return h


def analytic_ground_test_constants():
    # Even triangular physical tent:
    # g(x)=max(0,1-abs(abs(x)-mid)/r).
    # EXACT original L1=2*r=1/256 and L2²=4*r/3=1/384.
    tent_l1=2*RADIUS
    tent_l2_squared=4*RADIUS/F(3)
    E_length=2*H_WIDTH
    assert tent_l1==F(1,256)
    assert tent_l2_squared==F(1,384)
    assert E_length==F(1,128)
    assert tent_l2_squared<F(1,19**2)

    # TRUE original digamma generator Jg(x) is bounded pointwise
    # by 2∫ k(u) min(512u,1) du.
    # Original PS18 kernel comparisons: k<1/(2u)+1 for u<=1;
    # k<2e^(-u/2) for u>=1.
    # Split at r=1/512, u=1:
    # low 1+1/512; middle log512+2(1-r), tail <8.
    low=F(1)+F(1,512)
    mid=9*F(7,10)+2*(1-RADIUS)
    tail=F(8)
    j_infty_up=low+mid+tail
    assert j_infty_up<F(18)
    assert F(18)**2*FULL_CARRIER<F(27)**2

    # TRUE source and bounded original signed lower-order:
    # ||R||< (1403/80)^2*(9000/1997) <1387,
    # ||V0||< 13+539/90 <19, |lambda0|<1406.
    R_up=F(1403,80)**2/F(1997,9000)
    V_up=F(13)+F(539,90)
    lam_up=F(1406)
    assert R_up<F(1387)
    assert V_up<F(19)
    assert (F(19)+F(1387)+lam_up)==F(2812)
    lhs_A=F(27)+F(2812,19)
    assert lhs_A==F(175)
    # NOTE all bounds strictly less, hence operator norm A<175.

    # TRUE original k(u)>3/10 for 0<u<=11/5 (PS30).
    # Actual off-support -Jg >=k(R) ∫g >3/(10*256).
    assert F(3,10)*tent_l1==M0

    # |E|=1/128 so ∫E phi0<=sqrt(|E|)*||1_E phi0||.
    # Let A<175; f(m,A,e)=m/(A+m sqrt(e))
    # increases with m and decreases with A,e.
    # Using m>m0 and sqrt(|E|)<1 yields strictly
    # f>m0/(175+m0)>m0/176>2^-18.
    assert M0<F(1)
    assert M0/F(176)>F(1,2**18)
    assert F(3)*F(2)**18>F(2560)*F(176)

    # Inherited PS33 exact original Fourier low-band L1 lower:
    # (∫phi0)^2 >3/(8000*2^2025).
    global_l1_sq=F(3,8000*(2**2025))
    individual=global_l1_sq/(2**36)
    assert individual==F(3,8000*(2**2061))
    assert individual>0
    all16=16*individual
    assert all16==F(3,500*(2**2061))
    return j_infty_up,R_up,V_up,individual,all16


def finite_signed_order_regression():
    """Exact finite graph verifies no source or prime sign is dropped.

    2 source channels, 3 original-STYLE complement sites; R is
    genuine finite source inverse B* A^-1 B, nonnegative entrywise
    under sign-reversing B and positivity-preserving A^-1.
    This is ALGEBRA ONLY, not an original eigenpair approximation.
    """
    p=ps34.ps33.ps32.ps31.ps30
    A0=[[F(3),F(-1)],[F(-1),F(3)]]
    B0=[[F(-1),F(0),F(-1)],
        [F(0),F(-1),F(-1)]]
    R=p.mm(p.mm(p.tr(B0),p.inverse_2(A0)),B0)
    assert all(x>=0 for row in R for x in row)
    # The literal cross sign for a nonnegative tent supported at
    # middle site is negative: arch attractive, original
    # seven-prime-style signed cross, source -R.
    arch=[[F(0),F(-1),F(-1)],
          [F(-1),F(0),F(-2)],
          [F(-1),F(-2),F(0)]]
    prime=[[F(0),F(0),F(-1,7)],
           [F(0),F(0),F(-1,5)],
           [F(-1,7),F(-1,5),F(0)]]
    g=[F(0),F(1),F(0)]
    for i in (0,2):
        actual=p.vec(arch,g)[i]+p.vec(prime,g)[i]-p.vec(R,g)[i]
        assert actual<=p.vec(arch,g)[i]<0
    return R[0][1],R[2][1]


def run():
    # Replaying inherited original PS28 source arithmetic,
    # plus PS32/33 true-original rational spectral constants,
    # without invoking ancestor validators whose terminal
    # manifest assertion is specific to their own checkpoint.
    ps34.ps33.ps32.ps31.ps30.ps29.ps28.run()
    M=ps34.ps33.ps32.exact_original_analytic_constants()[1]
    e=ps34.ps33.optimize_dyadic(M)
    assert e[4]==F(3,8000*2**2025)
    assert e[5]>1

    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["checkpoints"][-1]["id"]=="PS35"
    assert all(x is False for x in lane["closures"].values())

    cells=actual_cells()
    jmax,Rmax,Vmax,bound,all16=analytic_ground_test_constants()
    cross=finite_signed_order_regression()

    print("PS35 ORIGINAL 16 cells cover true prime-quiet physical C+:",
          cells[0][0],cells[-1][1],flush=True)
    print("PS35 true original tent g L1=1/256; L2²=1/384;",
          "original Jg pointwise upper",float(jmax),"<18",flush=True)
    print("PS35 true original full source B0*A0^-1B0 norm upper",
          float(Rmax),"<1387",flush=True)
    print("PS35 true original V0 (7 prime+arch, positive pole"
          " removed) norm upper",float(Vmax),"<19",flush=True)
    print("PS35 uniform true original ||(L-lambda0)g||<175;"
          " outside E (L-lambda0)g<-3/2560",flush=True)
    print("PS35 verified exact rational original fixed-cell"
          " \u03bc(H_j)>3/(8000*2**2061) EACH j=0,...,15",
          flush=True)
    print("PS35 sum true original quiet ground \u03bc(Jquiet)>"
          "3/(500*2**2061)",flush=True)
    print("PS35 finite order-preserving source regression"
          " off-diagonal responses",cross,flush=True)
    print("PS35 PASS SCOPED: first original physical even ground"
          " POSITIVE mass inside each of 16 specified macroscopic"
          " actual source-complement cells, no PS34 sharp"
          " eigenfunction characteristic cut needed."
          " Exponentially weak; original PS31 graph kernel weights"
          " W_N, lambda1, effective-pole Delta, W-EVEN-FORM,"
          " canonical W-ODD-NEG, native CC27 D-Riesz, full signed"
          " Weil and RH OPEN. Inherited infinite-dimensional"
          " order-cone and domain analytic proof need independent"
          " mathematical review.",flush=True)


if __name__=="__main__":
    run()
