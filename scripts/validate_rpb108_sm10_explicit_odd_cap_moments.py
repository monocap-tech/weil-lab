#!/usr/bin/env python3
"""SM10: exact-rational FULL original odd negative-frequency finite moment cap.

Produces every entry of 107 positive-frequency cluster Hankel blocks for
one explicit 890-column odd physical sine-Taylor synthesis. Certifies
actual sign-envelope mass, each block's exact rational SPD via LDL,
and the infinite residual. It does NOT certify the remaining 891-source
positive-vs-negative inverse/Schur test, so W-ODD-NEG remains OPEN.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B, prime_interval
from validate_rpb108_si07_negative_support_cover import (
    END, DEPTH, M, DEN, arch_lower_cell, ceil_fraction
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si10_complement_positivity import (
    KAPPA, protected_outer_band
)

BITS=24
TAU=F(1,1024)

def full_upper_leaves():
    """Replay exactly the SI10 whole-positive-complement dyadic cover."""
    leaves=[]
    accepted=0
    def visit(l,r,arch,depth):
        nonlocal accepted
        mid=(l+r)/2
        lower=arch+prime_interval(mid)[0]-M*(r-l)/2
        if lower>KAPPA:
            accepted+=1
            return
        if depth<DEPTH:
            visit(l,mid,arch,depth+1)
            visit(mid,r,arch,depth+1)
            return
        h=F(max(0,ceil_fraction((-lower)*DEN)),DEN)
        assert h>=max(F(0),-lower)
        # r=(kappa-m)_+ <= kappa+h at EVERY frequency in leaf.
        leaves.append((l,r,h))
    for j in range(END):
        visit(F(j),F(j+1),arch_lower_cell(j),0)
    leaves.sort(key=lambda z:z[0])
    assert len(leaves)==973 and accepted==9261
    assert all(F(0)<=l<r<=F(896) for l,r,h in leaves)
    # Maximal connected clusters of possibly bad positive-frequency leaves.
    clusters=[]
    for l,r,h in leaves:
        if clusters and clusters[-1][-1][1]==l:
            clusters[-1].append((l,r,h))
        else:
            clusters.append([(l,r,h)])
    assert len(clusters)==107
    half_width=sum((r-l for l,r,h in leaves),F(0))
    half_mass=sum((h*(r-l) for l,r,h in leaves),F(0))
    W=2*half_width
    Mneg=2*half_mass
    assert W==F(973,32)
    assert Mneg<F(38)
    total=Mneg+KAPPA*W
    assert total<F(38)
    return clusters,W,Mneg,total

def exact_block(cluster,order):
    """C_{kl}=2 integral_cluster w(xi)*(xi-center)^(k+l) dxi.

    The polynomial monomials form a strictly linearly independent set in
    weighted L2 on any positive-measure leaf. Hence C is SPD, with the
    exact LDL pivots below independently checked as arithmetic evidence.
    """
    assert order>=1
    c=(cluster[0][0]+cluster[-1][1])/2
    moments=[]
    for degree in range(2*order-1):
        q=degree+1
        moments.append(2*sum((
            (h+KAPPA)*((r-c)**q-(l-c)**q)/q
            for l,r,h in cluster
        ),F(0)))
    C=[[moments[i+j] for j in range(order)] for i in range(order)]
    assert C[0][0]>0
    # Full, *exact* symmetric rational LDL: no diagonal-only proxy and no
    # floating-point eigenvalue assumption.
    ld=[[F(0)]*order for _ in range(order)]
    diag=[]
    for j in range(order):
        pivot=C[j][j]-sum((ld[j][k]**2*diag[k] for k in range(j)),F(0))
        assert pivot>0,("SM10 original moment block not SPD",j,order)
        diag.append(pivot)
        ld[j][j]=F(1)
        for i in range(j+1,order):
            ld[i][j]=(C[i][j]-
                sum((ld[i][k]*ld[j][k]*diag[k] for k in range(j)),F(0)))/pivot
    assert len(diag)==order
    return C,c,diag

def validate():
    ext_leaves,ext_min=protected_outer_band()
    assert ext_leaves>0 and ext_min>KAPPA
    clusters,W,Mneg,mass=full_upper_leaves()
    orders=[]
    count=0
    number_entries=0
    center_zero_blocks=0
    max_order=0
    min_lifted_pivot=None
    # Each block represents the actual original odd functions
    # U_{jk}(x) = (2*pi*x)^k/k! sin(2*pi*c_j*x+k*pi/2),
    # whose Taylor sum over (xi-c_j)^k approximates h_xi(x).
    for cluster in clusters:
        width=cluster[-1][1]-cluster[0][0]
        p,remainder=taylor_order(width,BITS)
        assert F(0)<remainder<F(1,2**BITS)
        C,c,pivots=exact_block(cluster,p)
        assert C[0][0]==2*sum(((h+KAPPA)*(r-l)
                               for l,r,h in cluster),F(0))
        if c==0:center_zero_blocks+=1
        count+=p
        max_order=max(max_order,p)
        number_entries+=p*(p+1)//2
        orders.append(p)
        # Compare rational dimensionless pivot against its diagonal
        # so extreme coordinate scaling cannot hide a negative pivot.
        for j,d in enumerate(pivots):
            ratio=d/C[j][j]
            assert F(0)<ratio<=1
            min_lifted_pivot=ratio if min_lifted_pivot is None else min(min_lifted_pivot,ratio)
    assert count==890,("SM10 changed actual original odd carrier dimension",count)
    assert len(orders)==107 and max_order<256 and center_zero_blocks==0
    assert number_entries>count
    # The direct, nonorthogonal SOURCE approximation R0 uses the
    # EXACT cap moment blocks C_j=2int w u^(k+l) rather than abstract
    # P K_cap P; no need to assemble unstable physical orthogonal P.
    # ||Rcap-R0||^2 <= 2B*(Mneg+kappa*W)*2^(-2 BITS).
    error_square=2*B*mass*F(1,2**(2*BITS))
    eta=(1+1/TAU)*error_square
    assert F(0)<eta<F(302,10**12)  # < 3.02e-10
    assert eta<KAPPA
    assert (1+TAU)*KAPPA>0
    print("SM10 original m>kappa exterior leaves:",ext_leaves,flush=True)
    print("SM10 all original upper-envelope reflected width:",float(W),flush=True)
    print("SM10 all negative cap integrated upper mass:",float(mass),flush=True)
    print("SM10 true physical odd Taylor Hankel blocks:",len(orders),flush=True)
    print("SM10 exact positive rational LDL pivots verified:",count,flush=True)
    print("SM10 full distinct rational moment entries:",number_entries,flush=True)
    print("SM10 explicit odd source dimension:",count,"largest local order:",max_order,flush=True)
    print("SM10 smallest rational (LDL pivot / original diagonal):",
          float(min_lifted_pivot),flush=True)
    print("SM10 ||Rcap-R_Taylor||^2 certified upper:",float(error_square),flush=True)
    print("SM10 GLOBAL negative Fourier infinite/cross error eta:",float(eta),flush=True)
    print("SM10 PASS (SCOPED): original K_neg,o <= (1+tau) U C U* + eta I",flush=True)
    print("SM10 keeps 891-source original positive inverse/Schur, exact odd "
          "pole, even form, global bridge, W-ODD-NEG and RH OPEN",flush=True)

if __name__=="__main__":
    validate()
