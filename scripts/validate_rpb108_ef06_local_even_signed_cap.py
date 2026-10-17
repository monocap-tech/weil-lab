#!/usr/bin/env python3
"""EF06: rigorous original signed LOCAL sharp cap for the even sector.

Refines only the 64 original SI10 unresolved dyadic leaves in [0,1],
each into four rational cells. The archimedean lower is re-evaluated at
the original leaf's exact left endpoint, not held fixed at integer 0;
prime phase interval is re-evaluated at each of 256 subcell midpoints.
The new nonnegative envelope is the MIN of the old certified envelope
and a rigorously rounded new signed lower -> negative upper, preserving
the entire all-real original signed Loewner upper elsewhere.

The critical EF05 physical cosine witness is explicitly re-screened:
its [0,1] old cap contribution is LOWER bounded, and its revised [0,1]
contribution is UPPER bounded. This is NOT a full original even
positivity proof nor proof the new GLOBAL cap is feasible.
"""
from fractions import Fraction as F

from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves, exact_block,
)
from validate_rpb108_si07_negative_support_cover import (
    arch_lower_cell, M, DEN, ceil_fraction
)
from validate_rpb108_si06_negative_band import B, prime_interval
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_ef05_even_cap_obstruction import (
    CENTER, DERIVATIVE, supported_even_fourier,
    absolute_upper, absolute_lower, rational_floor, rational_ceil
)

SPLIT=4
FOCUS_MAX=F(1)
BITS=24
TAU=F(1,65536)
OLD_EXPECTED_MASS=F(1204033883,32000000)


def improve_original_leaf(l,r,h):
    """Exact globally valid sharper local upper on the SAME signed r."""
    assert F(0)<=l<r<=1 and r-l==F(1,64)
    original_weight=h+KAPPA
    original_arch=arch_lower_cell(l)
    out=[]
    for j in range(SPLIT):
        a=l+(r-l)*j/SPLIT
        b=l+(r-l)*(j+1)/SPLIT
        mid=(a+b)/2
        # Archimedean function is monotone for nonnegative frequency.
        # The SI07 Euler/integral arch_lower_cell formula is a rational
        # lower bound at ANY rational l>=0 (not restricted to integers).
        # Original seven prime interval and |p'|<=69 pay the whole cell.
        lower=original_arch+prime_interval(mid)[0]-M*(b-a)/2
        refined=rational_ceil(max(F(0),KAPPA-lower))
        cap_weight=min(original_weight,refined)
        assert F(0)<=cap_weight<=original_weight
        # Current exact-block integration interface requires
        # h+KAPPA, so encode w'=KAPPA+h' only when >=KAPPA.
        # If w'<KAPPA, exact_block cannot store this cap without
        # a generalized moment formula; hence record weight directly.
        out.append((a,b,cap_weight))
    return out


def refined_moment_block(cluster):
    """Exact rational Hankel covariance of a list of (l,r,weight)."""
    lo=cluster[0][0];hi=cluster[-1][1]
    center=(lo+hi)/2
    p,_=taylor_order(hi-lo,BITS)
    moments=[]
    for degree in range(2*p-1):
        n=degree+1
        moments.append(2*sum((
          w*((r-center)**n-(l-center)**n)/n
          for l,r,w in cluster
        ),F(0)))
    C=[[moments[i+j] for j in range(p)] for i in range(p)]
    assert C[0][0]>0
    return C,p


def strict_rational_ldl(C):
    """Full exact-rational LDL on changed blocks; no float pivots."""
    p=len(C)
    ld=[[F(0)]*p for _ in range(p)]
    diag=[]
    for j in range(p):
        pivot=C[j][j]-sum(
            (ld[j][k]**2*diag[k] for k in range(j)),F(0)
        )
        assert pivot>0,("EF06 refined covariance singular",j,p)
        diag.append(pivot)
        ld[j][j]=F(1)
        for i in range(j+1,p):
            ld[i][j]=(C[i][j]-sum(
                (ld[i][k]*ld[j][k]*diag[k] for k in range(j)),F(0)
            ))/pivot
    return diag


def validate():
    original,W,Mneg,orig_mass=full_upper_leaves()
    assert len(original)==107 and orig_mass==OLD_EXPECTED_MASS
    new_clusters=[]
    nold=nnew=0
    old_mass=old_low_lower=new_low_upper=F(0)
    modified=[]
    low_covered=F(0)
    for cluster in original:
        local=[]
        changed=False
        for l,r,h in cluster:
            oldw=h+KAPPA
            if r<=FOCUS_MAX:
                nold+=1
                changed=True
                refined=improve_original_leaf(l,r,h)
                nnew+=len(refined)
                for a,b,w in refined:
                    assert l<=a<b<=r
                    low_covered+=b-a
                    # Each FULL subcell is paid by the true physical
                    # cosine Fourier bound, with all derivative error.
                    mid=(a+b)/2
                    f=supported_even_fourier(mid)
                    famp=rational_ceil(
                        absolute_upper(f)+DERIVATIVE*(b-a)/2
                    )
                    new_low_upper+=2*(b-a)*w*famp**2
                    local.append((a,b,w))
                # Exact old EF05 lower on the original full leaf.
                mid=(l+r)/2
                f=supported_even_fourier(mid)
                famp=max(F(0),
                  absolute_lower(f)-DERIVATIVE*(r-l)/2)
                famp=rational_floor(famp)
                old_low_lower+=2*(r-l)*oldw*famp**2
            else:
                local.append((l,r,oldw))
        if changed: modified.append(len(new_clusters))
        new_clusters.append(local)
        old_mass+=sum((2*w*(r-l) for l,r,w in local),F(0))

    assert nold==64 and nnew==256 and low_covered==FOCUS_MAX
    assert len(new_clusters)==107
    assert 0<old_mass<orig_mass
    # Source columns are the SAME original physically supported 890
    # cosine Taylor derivatives because original cluster endpoints stay.
    total_rank=0
    modified_pivots=0
    modified_entries=0
    for index,cluster in enumerate(new_clusters):
        C,p=refined_moment_block(cluster) if index in modified else (None,None)
        lo=cluster[0][0];hi=cluster[-1][1]
        q,_=taylor_order(hi-lo,BITS)
        total_rank+=q
        if index in modified:
            assert p==q
            assert all(C[i][j]==C[j][i] for i in range(p)
                       for j in range(p))
            pivots=strict_rational_ldl(C)
            assert len(pivots)==p
            modified_pivots+=p
            modified_entries+=p*(p+1)//2
    assert total_rank==890 and modified_pivots>0

    # Whole original negative-frequency Loewner bound survives:
    # r <= w_new <= w_old. New full signed mass shrinks while
    # original 107 physical clusters/Taylor error estimate is unchanged.
    error2=2*B*old_mass*F(1,2**(2*BITS))
    eta=(1+1/TAU)*error2
    assert 0<eta<KAPPA and eta<F(193,10**10)
    # EF05's UNCHANGED old cap low-energy already gives a >4.415
    # lower, and the refined cap produces a certified low-frequency
    # upper, not just a heuristic midpoint sample.
    assert old_low_lower>F(4415,1000)
    assert new_low_upper<F(3,2),("local cap still too large",float(new_low_upper))
    gain=old_low_lower-new_low_upper
    assert gain>F(29,10),("insufficient witnessed sharpening",float(gain))

    print("EF06 original SI10 full negative-cap mass:",float(orig_mass),flush=True)
    print("EF06 improved original-signed full cap mass:",float(old_mass),flush=True)
    print("EF06 strictly reduced full integrated mass:",float(orig_mass-old_mass),flush=True)
    print("EF06 old low dyadic leaves, microcells:",nold,nnew,flush=True)
    print("EF06 changed original connected clusters:",len(modified),flush=True)
    print("EF06 unchanged even source dimension:",total_rank,flush=True)
    print("EF06 exact refined Hankel LDL positive pivots:",modified_pivots,flush=True)
    print("EF06 exact refined upper covariance entries:",modified_entries,flush=True)
    print("EF06 EF05 physical cosine OLD [0,1] cap LOWER:",float(old_low_lower),flush=True)
    print("EF06 EF05 physical cosine NEW [0,1] cap UPPER:",float(new_low_upper),flush=True)
    print("EF06 physical cosine LOW band improvement LOWER:",float(gain),flush=True)
    print("EF06 full global Taylor residual delta upper:",float(eta),flush=True)
    print("EF06 PASS (LOCAL SHARPENING): entire true original Kneg,e remains",
          "Loewner-below new cap and explicit 890-source Young upper.",
          "EF05 [0,1] conservative excess is substantially reduced.",flush=True)
    print("W-EVEN-FORM OPEN: remaining frequencies, full new cap vs A_e,",
          "finite supported inverse/Schur, whole Weil and RH not certified.",
          flush=True)


if __name__=="__main__":
    validate()
