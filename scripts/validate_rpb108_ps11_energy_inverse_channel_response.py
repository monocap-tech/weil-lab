#!/usr/bin/env python3
"""PS11 exact rational TRUE original H inverse series and five-mode response.

Replays original seven-prime signed PS10/PS09/PS07/PS06/PS03/RC315.
Certifies sign-respecting graph perturbation, convergent 65/97-term
preconditioned true inverse error, nonzero P13 leakage, sharpened signed
pole IMS correction and channel inverse-Gram spectral error. No numeric
H inverse, F_N matrix, actual Schur PSD, full Weil positivity or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps10_full_prime_graph as ps10

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    # Independently replay the complete pinned original SI10/CC27 source
    # and full seven-prime physical channel graph.
    ps10.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(x is False for x in lane["closures"].values())

    pi=old.pi_iv()
    gamma=old.gamma_iv()
    ln2=old.log_i(F(2))
    ln9=old.log_i(F(9))
    arch_const=-gamma-pi/2-3*ln2-old.log_i(pi)
    weights={}
    for n,base in ORIGINAL:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        weights[n]=old.log_i(F(base))/root
        assert weights[n].lo>0
    W=sum(weights.values(),old.IV(0))
    assert F(3)<W.lo<=W.hi<F(4)
    sinh,cosh=old.sinh_cosh_iv(B/2)
    sinh_B=2*sinh*cosh
    cosh_B=cosh*cosh+sinh*sinh
    assert sinh_B.hi<F(7,5)
    assert cosh_B.hi<F(7,4)

    # True original signed even/odd rank-one poles:
    # ||c||²=B+sinh(B) and ||s||²=sinh(B)-B.
    # Unlike PS06/PS08, the lower form bound DOES NOT charge positive c.
    vlo=arch_const.lo-2*W.hi-2*(sinh_B.hi-B)
    vhi=arch_const.hi+2*W.hi+2*(B+sinh_B.hi)
    assert -F(13)<vlo<-F(12)
    assert F(6)<vhi<F(7)
    assert -vlo>vhi
    assert 20+vlo>F(7)
    # D=J+20 I, S=D^-1/2 V D^-1/2, self-adjoint norm <13/20.
    s_bound=F(13,20)
    assert (-vlo)/20<s_bound and vhi/20<s_bound

    # Exact genuine original H^-1 operator-norm geometric Neumann tail.
    # T_N = D^-1/2 sum_{k=0}^N (-S)^k D^-1/2;
    # all T_N positive because scalar geometric polynomial >0
    # on [-13/20,13/20].
    def err(N):
        return F(1,20)*s_bound**(N+1)/(1-s_bound)
    err64=err(64)
    err96=err(96)
    assert err64<F(1,10**13)
    assert err64<F(1,3_000_000**2)
    assert err96<F(1,9*10**18)
    assert err96<F(1,3_000_000_000**2)
    assert 20+vlo>7

    # Literal inverse-series compressed onto five-mode PS10
    # physical U5.  F=U5*H^-1 U5 and F_N=U5*T_N U5:
    # norm error <eps_N by isometry of U5. Full leakage is included,
    # not omitted as if U5 reduced the original operator.
    # ||F||,||F_N||<4/25, so the operator square-root Holder estimate
    # gives the following exact rational errors for the signed
    # compact five-channel spectral representatives.
    rho_square=old.IV(0)
    for n,base in ORIGINAL:
        rho_square+=old.log_i(F(base))**2/F(n)
    assert F(1419,1000)**2<rho_square.lo<=rho_square.hi<F(1420,1000)**2
    rho_upper=F(71,50)
    assert rho_upper*rho_upper>rho_square.hi
    assert F(1,7)+err64<F(4,25)
    sp64=rho_upper*F(4,5)/F(3_000_000)
    sp96=rho_upper*F(4,5)/F(3_000_000_000)
    assert sp64<F(1,2_500_000)
    assert sp96<F(1,2_500_000_000)
    # Truly normalized original whole-prime IMS response:
    # ||H^-1/2 Rprime H^-1/2|| < rho7/7 < .203
    assert rho_upper/F(7)<F(203,1000)

    # PS10 disjoint channel P13 does NOT reduce actual full H.
    # Choose right seam of the true left log2 leaf. Adjacent
    # normalized step functions on either side have support
    # diameter 2 eps << log2 and all seven prime cross terms ZERO.
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    eps=old.IV(delta.lo/64,delta.hi/64)
    assert eps.lo>0 and 2*eps.hi<ln2.lo
    offsets={F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
    offsets|={F(9,n) for n in (2,4,5,7,8)}
    logs={x:(old.IV(0) if x==1 else old.log_i(x)) for x in offsets}
    sortkeys=sorted(offsets,key=lambda x:logs[x].lo)
    idx=sortkeys.index(F(2))
    assert idx>0 and idx<len(sortkeys)-1
    nextoff=logs[sortkeys[idx+1]]
    assert nextoff.lo-logs[F(2)].hi>delta.hi+eps.hi
    x0_lo=-B+logs[F(2)].lo+delta.lo
    x0_hi=-B+logs[F(2)].hi+delta.hi
    assert -B<x0_lo<=x0_hi<B
    assert x0_hi+eps.hi < -B+nextoff.lo
    # Exact original arch b(f,g) <= -log2+eps/4; original signed
    # poles contribute absolute <=2eps cosh(B), graph mass zero.
    mix_upper=-ln2.lo+eps.hi/F(4)+2*eps.hi*cosh_B.hi
    assert mix_upper<-F(69,100)
    # Cross form nonzero => P13 not reducing the original H and hence
    # not commuting with H^-1 or H^-1/2. Does NOT certify
    # a numerical lower bound for the inverse leakage norm.

    # Localized original signed pole IMS remainder rank <=6.
    # For v=c,s, e_v=||1_E v||; |α v|<=e_v and
    # ||(β-1)v||<=e_v. Rank-one perturbation gives
    # ||R_pole|| <=2Σ(e_v²+2||v|| e_v).
    assert cosh.hi<F(7,6) and sinh.hi<F(7,12)
    assert B+sinh_B.hi<F(8,5)**2
    assert sinh_B.hi-B<F(1,2)**2
    assert 2*delta.hi*cosh.hi**2<F(9,100)**2
    assert 2*delta.hi*sinh.hi**2<F(9,200)**2
    pole_hi=2*((F(9,100)**2+2*F(8,5)*F(9,100))
              +(F(9,200)**2+2*F(1,2)*F(9,200)))
    assert pole_hi==F(549,800)
    assert pole_hi<F(7,10)
    assert pole_hi/F(7)<F(1,10)
    assert (rho_upper+pole_hi)/7<F(303,1000)

    print("PS11 original signed V lower/upper",float(vlo),float(vhi),flush=True)
    print("PS11 whole original graph H positive scalar lower",float(20+vlo),flush=True)
    print("PS11 true preconditioned relative S norm upper",float(s_bound),flush=True)
    print("PS11 source Neumann 65-term true H inverse error upper",float(err64),flush=True)
    print("PS11 source Neumann 97-term true H inverse error upper",float(err96),flush=True)
    print("PS11 full-physical P13 complement seam H form cross upper",float(mix_upper),flush=True)
    print("PS11 full prime IMS exact sharp rho7 upper",float(rho_upper),flush=True)
    print("PS11 5-mode inverse Gram normalized prime op upper",float(rho_upper/7),flush=True)
    print("PS11 source Gram 65-term spectral sandwich error upper",float(sp64),flush=True)
    print("PS11 source Gram 97-term spectral sandwich error upper",float(sp96),flush=True)
    print("PS11 true signed original localized pole IMS norm upper",float(pole_hi),flush=True)
    print("PS11 combined normalized prime-and-pole IMS upper",float((rho_upper+pole_hi)/7),flush=True)
    print("PS11 PASS SCOPED: true original full graph H >= J+7;"
          " nonzero 13-channel inverse leakage; exact complete"
          " signed five-fiber inverse Gram spectral reduction;"
          " true H^-1 Neumann source series errors <1e-13 (65 terms)"
          " and <1/(9e18) (97 terms); localized original pole"
          " IMS correction <0.68625. No energy base solve,"
          " finite Gram entries, arch PSD, CC27 transfer, Weil or RH.",flush=True)

if __name__=="__main__":
    run()
