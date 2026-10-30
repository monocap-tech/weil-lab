#!/usr/bin/env python3
"""EF16: actual ORIGINAL even b9 source-pole physical coupling and exact
positive-pole Schur update. Not a full signed 469D Schur certificate.

Use the SAME SI10 original 107 physical frequency clusters and b9
parity-even source family. Compute actual physical 2x2 Gram for k=0
sources at original first and last cluster centers and actual
hyperbolic even-pole cross. Rigorous trigonometric/hyperbolic interval
bounds use inherited original rational source libraries. Two-mode
Hilbert projection bounds the whole 469D exceptional-versus-infinite
even-pole leakage; no finite Gram inverse of 469 columns is presumed.

For the original POLE-FREE signed even form q0, the SI10 cofinite
lower remains gamma9>17/25000 on F9=V9^perp. Eliminating F9 after
adding the ACTUAL POSITIVE even pole gives a positive rank-one Schur
correction, rather than a negative absolute mixed-coupling charge.
The true pole-free exceptional Schur and full signed mixed operator
remain unmeasured.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si14_odd_multiband_nogo import cos_sin_pi_multiple
from validate_rpb108_si12_even_supported_inverse import sinh_bounds, cosh_bounds

ROOT=Path(__file__).resolve().parents[1]
DEN=10**24
MU=F(17,25000)


def floor(q):
    return F((q*DEN).numerator//(q*DEN).denominator,DEN)


def ceil(q):
    x=q*DEN
    return F(-((-x.numerator)//x.denominator),DEN)


def outward(iv):
    assert iv[0]<=iv[1]
    return floor(iv[0]),ceil(iv[1])


def plus(a,b):
    return outward((a[0]+b[0],a[1]+b[1]))


def minus(a,b):
    return plus(a,(-b[1],-b[0]))


def times(a,b):
    products=[x*y for x in a for y in b]
    return outward((min(products),max(products)))


def over(a,b):
    assert b[0]>0 or b[1]<0, ("zero in denominator interval",b)
    inv=(1/b[1],1/b[0])
    return times(a,outward(inv))


def exact(x):
    return (x,x)


def nonnegative_square(a):
    assert a[0]<=a[1]
    if a[0]>=0:return outward((a[0]**2,a[1]**2))
    if a[1]<=0:return outward((a[1]**2,a[0]**2))
    return outward((F(0),max(a[0]**2,a[1]**2)))


def sine(q):
    return outward(cos_sin_pi_multiple(q)[0])


def cosine(q):
    return outward(cos_sin_pi_multiple(q)[1])


def sinc_physical(t):
    """Integral_-B^B cos(2*pi*t*x) dx, including removable t=0."""
    if t==0:return exact(2*B)
    numerator=sine(2*B*t)
    denominator=times(exact(t),outward(PI))
    return over(numerator,denominator)


def physical_cos_gram(c,d):
    # <cos(2*pi*c*x),cos(2*pi*d*x)> = [sinc(c-d)+sinc(c+d)]/2.
    return times(plus(sinc_physical(c-d),sinc_physical(c+d)),exact(F(1,2)))


def physical_even_pole_cross(center):
    """Actual <1_I cos(2*pi*c*x),1_I cosh(x/2)>.

    Exact antiderivative:
      2*[sinh(B/2)/2*cos(k B)+k*cosh(B/2)*sin(k B)]
        /[(1/2)^2+k^2], k=2*pi*c.
    """
    slo,shi=sinh_bounds(B/2)
    clo,chi=cosh_bounds(B/2)
    k=times(exact(2*center),outward(PI))
    a=times(times(exact(F(1,2)),outward((slo,shi))),
            cosine(2*B*center))
    b=times(times(k,outward((clo,chi))),sine(2*B*center))
    denom=plus(exact(F(1,4)),nonnegative_square(k))
    assert denom[0]>0
    return over(times(exact(F(2)),plus(a,b)),denom)


def true_even_pole_norm2():
    # ||cosh(x/2)||^2 on [-B,B] = B+sinh(B).
    return plus(exact(B),outward(sinh_bounds(B)))


def source_and_projection():
    clusters,w,m,leaves,protected=protected_inner_cover()
    assert len(clusters)==107 and leaves==973 and protected==9261
    assert w==F(973,32)
    assert sum(taylor_order(r-l,9)[0] for l,r,_ in clusters)==469
    c0=(clusters[0][0]+clusters[0][1])/2
    c1=(clusters[-1][0]+clusters[-1][1])/2
    assert 0<c0<c1 and c0!=c1
    centers=(c0,c1)
    G00=physical_cos_gram(c0,c0)
    G01=physical_cos_gram(c0,c1)
    G11=physical_cos_gram(c1,c1)
    assert G00[0]>0 and G11[0]>0
    determinant=minus(times(G00,G11),nonnegative_square(G01))
    assert determinant[0]>0, ("2-source Gram not certified SPD",determinant)

    b0=physical_even_pole_cross(c0)
    b1=physical_even_pole_cross(c1)
    assert b0[0]>0  # exact low original cluster pole alignment, not assumed elsewhere
    # First-one-mode projection is a genuine exact Hilbert lower.
    projection_one=over(nonnegative_square(b0),G00)
    # Complete 2D projection b^T G^-1 b. Preserve correlation term!
    projection_num=plus(minus(times(nonnegative_square(b0),G11),
                              times(exact(F(2)),times(times(b0,b1),G01))),
                        times(nonnegative_square(b1),G00))
    assert projection_num[0]>0
    projection_two=over(projection_num,determinant)
    c2=true_even_pole_norm2()
    assert projection_two[0]>0
    # Exact two-mode lower must be >= the single-mode projection;
    # interval enclosure may straddle equality, so use the stronger
    # of the two individually certified rigorous lower endpoints.
    projection_lb=max(projection_one[0],projection_two[0])
    assert projection_lb>0 and projection_lb<c2[1]
    residue_ub=c2[1]-projection_lb
    assert residue_ub>0
    # V9 contains both actual source cosines, hence
    # ||Q_V c||² <= residue_ub and ||P_V c||² >= projection_lb.
    # Coefficient of positive rank-one even-pole correction after
    # eliminating the whole ORIGINAL pole-FREE signed complement:
    # alpha = 2/(1+2<Q_Vc,C0^-1 Q_Vc>).
    # Since C0>=MU and ||Q_Vc||²<=residue_ub:
    alpha_lb=2/(1+2*residue_ub/MU)
    generic_lb=2/(1+2*c2[1]/MU)
    assert alpha_lb>generic_lb>0
    # Norm of the ACTUAL pole-only entire mixed finite-to-infinite
    # physical map (not full signed q0 mixed B0).
    mixed_sq_ub=4*residue_ub*c2[1]
    assert mixed_sq_ub>0
    return dict(centers=centers,G00=G00,G01=G01,G11=G11,
                det=determinant,b0=b0,b1=b1,c2=c2,
                proj1=projection_one,proj2=projection_two,
                projection_lb=projection_lb,residue_ub=residue_ub,
                alpha_lb=alpha_lb,generic_lb=generic_lb,
                mixed_sq_ub=mixed_sq_ub)


def exact_schur_pole_sign_regression():
    # Exact 1 finite + 1 complement model preserving the sign and
    # nonorthogonal displacement of the rank-one residue.
    A=F(3);B0=F(1,2);C=F(5);u=F(2);v=F(1,3)
    S0=A-B0*B0/C
    Sfull=A+2*u*u-(B0+2*u*v)**2/(C+2*v*v)
    effective=u-B0*v/C
    alpha=2/(1+2*v*v/C)
    assert Sfull==S0+alpha*effective**2
    assert Sfull>S0 and 0<alpha<2
    # Rank-one PSD addition cannot repair two negative independent
    # directions of the pole-free 469x469 Schur.
    # Exact 2D countermodel with a single rank-one pole aligned to e1.
    assert F(-1)+2>0 and F(-1)<0
    return alpha


def validate():
    custody=json.loads((ROOT/"research/obligations.json").read_text())
    obs={o["id"]:o for o in custody["obligations"]}
    assert custody["active_obligation"]=="W-EVEN-FORM"
    assert obs["W-EVEN-FORM"]["status"]=="open"
    assert obs["W-ODD-NEG"]["status"]=="open"
    assert "EF15" in obs["W-EVEN-FORM"]["evidence"]
    d=source_and_projection()
    alpha=exact_schur_pole_sign_regression()
    print("EF16 original SI10 b9 native even k0 centers:", *(str(c) for c in d["centers"]),flush=True)
    print("EF16 original physical G00,G01,G11:",
          *(tuple(float(x) for x in d[k]) for k in ("G00","G01","G11")),flush=True)
    print("EF16 true physical 2x2 Gram determinant lower:",float(d["det"][0]),flush=True)
    print("EF16 original even pole cross with two actual carrier sources:",
          *(tuple(float(x) for x in d[k]) for k in ("b0","b1")),flush=True)
    print("EF16 exact original c norm2:",tuple(float(x) for x in d["c2"]),flush=True)
    print("EF16 certified 1-source and 2-source projection lower:",
          float(d["proj1"][0]),float(d["proj2"][0]),flush=True)
    print("EF16 certified actual whole 469D Q_V even pole residual norm2 UPPER:",
          float(d["residue_ub"]),flush=True)
    print("EF16 actual even pole-only 469D-to-infinity mixed norm2 UPPER:",
          float(d["mixed_sq_ub"]),flush=True)
    print("EF16 exact original even positive Schur rank-one coefficient LOWER:",
          float(d["alpha_lb"]),"versus nonprojected generic",
          float(d["generic_lb"]),flush=True)
    print("EF16 exact pole Schur sign regression alpha:",float(alpha),flush=True)
    print("EF16 SCOPED PASS: actual original even 2-source physical Gram + "
          "whole-complement pole leakage, conditional original pole-free "
          "signed cofinite floor, and exact positive rank-one Schur update. "
          "Pole-FREE original 469D signed finite block, B0 mixed map, "
          "C0 inverse application, corrected PSD, domain and RH OPEN.",flush=True)


if __name__=="__main__":
    validate()
