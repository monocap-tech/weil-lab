"""Exact CC1 controls; no actual graph, spectral solver, interval or Lean claim."""
from fractions import Fraction as F
import json

def run():
    checks = 0
    def check(value):
        nonlocal checks
        assert value
        checks += 1
    def psd(a, b, c):
        return a >= 0 and c >= 0 and a*c-b*b >= 0
    # Full scalar E/F operator with nonzero anchor coupling. Compute its
    # transformed perturbation exactly rather than discarding the coupling.
    for c0 in [F(1),F(3,2)]:
        for k in [F(-1,3),F(0),F(2,5)]:
            for s in [F(1,20),F(1,4)]:
                a0=s+k*k/c0
                T=k/c0
                for dc in [F(-1,10),F(1,7)]:
                    c=c0+dc
                    for eta_signed in [F(-1,100),F(1,100)]:
                        # Choose D_EF so Pi_F D W is eta_signed exactly.
                        dk=eta_signed+dc*T
                        for alpha_signed in [F(-1,200),F(1,200)]:
                            da=alpha_signed+2*T*dk-T*T*dc
                            aa,kk=a0+da,k+dk
                            check(da-2*T*dk+T*T*dc==alpha_signed)
                            check(dk-dc*T==eta_signed)
                            alpha,eta=abs(alpha_signed),abs(eta_signed)
                            t=s-alpha-eta*eta/c
                            check(t>0)
                            exact_schur=aa-kk*kk/c
                            check(exact_schur>=t)
                            ell_b=abs(T)+eta/c
                            d=t*c/(t+c*(1+ell_b*ell_b))
                            check(psd(aa-d,kk,c-d))
                            # Universal norm conversion, including cross term.
                            x=t-d*(1+ell_b*ell_b)
                            y=c-d
                            check(x*y-(d*ell_b)**2==d*d)
                            check(x>=0 and y>=0)
                            # Compact-mass metric; physical lower bound differs.
                            for mass in [F(1,3),F(1,2)]:
                                check(psd(aa-d,kk,c-d*mass))
                                # Mass-shifted resolvent's trace/determinant
                                # eigenvalue invariants, for J=diag(1,sqrt(mass)).
                                beta=F(10)
                                det=(aa+beta)*(c+beta*mass)-kk*kk
                                check(det>0)
                                check(mass/det ==
                                      1/((aa+beta)*(c/mass+beta)-kk*kk/mass))
                            # Choose complete positive squared Gram=p2 I.
                            # N*N=p2 I-A is PSD, and its gain upper bound follows.
                            p2=F(10)
                            check(psd(p2-aa,-kk,p2-c))
                            check(psd(aa-d,kk,c-d))
                            check(0<d/p2<1)
    # Approximate graph residual controls in exact scalar coordinates.
    for c0,k,Z in [(F(2),F(1),F(1,3)),(F(3),F(-2),F(-1,2))]:
        T=k/c0
        r=abs(k-c0*Z)
        e=r/c0
        check(abs(T-Z)==e)
        # A rank-one perturbation D=u u*: exact norm omega=||u||^2.
        u,v=F(1,3),F(-2,5)
        omega=u*u+v*v
        alpha=(u-v*T)**2
        alpha_z=(u-v*Z)**2
        # ||W_Z|| <= 1+|Z| is a rational upper enclosure.
        Lz=1+abs(Z)
        check(alpha<=alpha_z+omega*(2*Lz*e+e*e))
        eta=abs(v*(u-v*T))
        eta_z=abs(v*(u-v*Z))
        check(eta<=eta_z+omega*e)
    # Retained positivity alone is false; dropping coupling fails.
    check(F(1,10)>0 and F(1)>0)
    check(F(1,10)-F(1,2)**2<0)
    # PS2's fixed finite-block/fixed-coupling counterexample survives CC1:
    # D_WW contains the complement-sensitive loss on the completed graph.
    c0,k,s=F(93,100),F(7),F(1,320*10**27)
    zstar=s*c0*c0/(k*k+s*c0)
    for scale in [F(1,2),F(1),F(3,2)]:
        z=scale*zstar
        c=c0-z
        T=k/c0
        alpha=z*T*T
        eta=z*T
        t=s-alpha-eta*eta/c
        check(t==s-k*k*z/(c0*c))
        check((t>0)==(scale<1))
        check((t==0)==(scale==1))
        check((t<0)==(scale>1))
    # Canonical complement conversion from physical bound and Garding.
    cphys,B,kappa=F(93,100),F(24),F(1,10)
    c0=kappa*cphys/(cphys+B)
    check(c0==F(93,24930))
    check(F(19,100)>c0)
    # Conditional polynomial-scale example. omega is stipulated here,
    # not an actual Weil perturbation certificate.
    s,L,K,c0=F(1,10**34),F(2),F(3),F(1,100)
    eps=s/(4*L*K)
    omega=F(1,1000)
    c=c0-omega
    eta=K*eps
    alpha=L*eta
    check(omega<c0/2)
    check(alpha+eta*eta/c<s/2)
    check(eps>F(1,10**37))
    # Local joint update can stall at contact with a separated complement.
    for j in range(1,20):
        gap=F(1,2**j)
        step=gap/2
        newgap=gap-step
        g2=1-newgap
        check(newgap>0 and g2<1)
        check(newgap==F(1,2**(j+1)))
    # Original positive eigenmode mass term is never removed.
    p2,n2,mass,mu=F(4),F(1),F(2),F(3,2)
    check(p2-n2==mu*mass)
    check(n2/p2<1)
    check((n2+mu*mass)/p2==1)
    # Rational logarithm enclosures check the complete prime-power dictionary
    # at 21/20; this is geometry only, not an operator sign calculation.
    def logs(n):
        z=F(n-1,n+1)
        lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(200)),F(0))
        hi=lo+2*z**401/(F(401)*(1-z*z))
        return lo,hi
    check(logs(7)[1]<2)
    check(2<logs(8)[0]<logs(8)[1]<F(21,10))
    check(logs(9)[0]>F(21,10))
    return {'passed':True,'checks':checks,'outcome':'B: conditional joint theorem',
            'actual_graph_computed':False,'new_actual_aperture':False,
            'new_actual_gain_constant':False,'interval_archives_replayed':False,
            'analytic_proof_written':True,'lean_certified':False,
            'scope':'finite rational graph, Schur, mass, gain, residual, crossing and threshold controls'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
