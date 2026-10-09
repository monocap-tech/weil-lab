#!/usr/bin/env python3
"""DNE1 exact Fraction graph and parity-fold controls.

No numerical zeta ground eigenfunction or unrestricted ground transform is
asserted. The continuous native kernel identity is proved analytically
in the DNE1 report, not from these finite controls.
"""
from fractions import Fraction as F
import json

def run():
    checks = 0
    def check(v):
        nonlocal checks
        assert v
        checks += 1

    for b in (F(1,4),F(1),F(9,4)):
        for p in (F(0),b/F(4),b/F(2),b):
            # H=[[-b,-b-p],[-b-p,-b]] with positive even ground.
            # Q=H+2c*c, c=(sqrt(b),sqrt(b)); all selected b are squares.
            root={F(1,4):F(1,2),F(1):F(1),F(9,4):F(3,2)}[b]
            H=[[-b,-b-p],[-b-p,-b]]
            c=[root,root]
            Q=[[H[i][j]+2*c[i]*c[j] for j in range(2)] for i in range(2)]
            check(Q==[[b,b-p],[b-p,b]])
            check(H[0][0]+H[0][1]==-2*b-p)
            check(H[0][0]-H[0][1]==p)
            check(Q[0][0]+Q[0][1]==2*b-p>0)
            check(Q[0][0]-Q[0][1]==p>=0)
            h=[F(1),F(-1)]
            qh=sum(h[i]*Q[i][j]*h[j] for i in range(2) for j in range(2))
            check(qh==2*p)
            check(p==0 and qh==0 or p>0 and qh>0)
            # φ=(1,1)/sqrt(2), u=(1,-1).
            # Dφ=(b+p)/2 * (u1-u2)^2; ||φu||²=1.
            D=F(1,2)*(b+p)*4
            check(D==(-2*b-p)*(-1)+p) # lambda1-lambda0 = 2b+2p
            check(D-(-(-2*b-p))==p) # strict surplus iff p>0

    # Folded odd jump identity for any symmetric decreasing nonlocal kernel.
    # Non-native rational toy weights: near-side 3, reflected cross matrix
    # [[2,1],[1,1/2]]. Tests algebra, not numeric digamma j.
    phi=[F(1),F(2)]
    reflected=[[F(2),F(1)],[F(1),F(1,2)]]
    within=[[F(0),F(3)],[F(3),F(0)]]
    for u in ([F(1),F(2)],[F(-1),F(3)],[F(3),F(-2)],[F(0),F(1)]):
        fullphi=phi+phi
        fullu=list(u)+[-t for t in u]
        def kernel(i,j):
            if (i<2)==(j<2):
                return within[i%2][j%2]
            return reflected[i%2][j%2]
        Dfull=sum((fullphi[i]*fullphi[j]*kernel(i,j)*
                   (fullu[i]-fullu[j])**2 for i in range(4)
                   for j in range(4)),F(0))/2
        Dfold=sum((phi[i]*phi[j]*
                  (within[i][j]*(u[i]-u[j])**2+
                   reflected[i][j]*(u[i]+u[j])**2)
                 for i in range(2) for j in range(2)),F(0))
        floor=4*sum((phi[i]*u[i]**2*
                sum((reflected[i][j]*phi[j] for j in range(2)),F(0))
                for i in range(2)),F(0))
        check(Dfull==Dfold)
        check(Dfull>=floor)
    return {
        "stage":"DNE1 ground-state jump exact finite controls",
        "all_passed":True,
        "rational_checks":checks,
        "new_original_zeta_interval_sign":False,
        "real_ground_state_regularization_checked":False,
        "original_contact_excluded":False,
        "RH_proved":False,
        "lean_certified":False
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
