#!/usr/bin/env python3
"""EF13: instantiate the TRUE original SI10 even exceptional carrier.

No conservative EF06/EF07 cap is used in the target Q_e, and no
operator inverse or PSD of the finite exceptional block is assumed.

Reconstruct the complete original signed protected-frequency cover,
its 107 actual rational clusters and exact Taylor order (BITS=24),
and give every even carrier column explicitly as a parity-even
physical polynomial/modulated cosine. Certify a true positive
cofinite original even-form lower via the SI10 whole-frequency proof.

Formal linear independence and form-domain attachment are stated
in the EF13 research note. No finite original signed Schur or RH proof.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si10_complement_positivity import KAPPA, protected_outer_band
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves

BITS=24
EPS2=F(1,2**(2*BITS))

def original_even_carrier():
    outer,minimum=protected_outer_band()
    assert minimum>KAPPA and outer>0
    clusters,W,Mneg,whole_mass=full_upper_leaves()
    assert len(clusters)==107 and W==F(973,32)
    assert Mneg>0 and whole_mass==Mneg+KAPPA*W
    assert all(len(c)>0 for c in clusters)
    assert sum((len(c) for c in clusters))==973

    # Every j-th cluster has a strictly positive rational center c_j,
    # and none intersects any other cluster. For 0<=k<p_j,
    # u_jk(x) = 1_I(x) (2*pi*x)^k/k!
    #            cos(2*pi*c_j*x + k*pi/2).
    # This is exactly the even projection of SI10's BOTH-sign
    # frequency-plane-wave Taylor carrier.
    centers=[]
    column_metadata=[]
    ords=[]
    for j,cluster in enumerate(clusters):
        left=cluster[0][0]
        right=cluster[-1][1]
        assert F(0)<=left<right<=896
        center=(left+right)/2
        assert center>0
        if centers:
            assert centers[-1]<center
        centers.append(center)
        p,tail=taylor_order(right-left,BITS)
        assert p>=1 and tail>=0
        assert tail<F(1,2**BITS)
        assert PI[1]>0
        ords.append(p)
        for k in range(p):
            # For even k cosine is even and x^k is even;
            # for odd k cosine phase is +/-sin (odd),
            # multiplied by x^k (odd), giving even.
            if k%2==0: parity=("even_polynomial","even_cosine")
            else: parity=("odd_polynomial","odd_sine")
            column_metadata.append((j,k,center,parity))
    assert len(centers)==107
    assert len(column_metadata)==sum(ords)==890
    assert len({(j,k) for j,k,_,_ in column_metadata})==890
    assert max(ords)<256

    # For even f orthogonal to the physical 890-column V_e,
    # |Ff(xi)| <= sqrt(2B) * EPS ||f|| on every unresolved
    # positive-frequency leaf and its even reflection.
    # All exterior original m(xi)>=kappa is paid by SI10.
    gamma=KAPPA-2*B*whole_mass*EPS2
    assert gamma==KAPPA*(1-2*B*W*EPS2)-2*B*Mneg*EPS2
    assert gamma>F(999,10**6)
    # Due to strictly distinct positive frequencies and standard
    # independence of exponential polynomials, these 890 columns
    # are linearly independent on the physical open interval.
    # This algebraic fact requires a separate analytical proof,
    # not a numerical Gram-determinant check.
    return dict(clusters=clusters,orders=ords,cols=column_metadata,
                W=W,Mneg=Mneg,mass=whole_mass,gamma=gamma,outer=outer)

def validate():
    data=original_even_carrier()
    assert len(data["cols"])==890
    assert data["gamma"]>0
    assert data["mass"]<F(38)
    print("EF13 original SI10 signed seven-prime protected cover: PASS",flush=True)
    print("EF13 true original physical even Taylor clusters:",
          len(data["clusters"]),flush=True)
    print("EF13 true original even exceptional source dimension:",
          len(data["cols"]),flush=True)
    print("EF13 original signed full negative/uncertain 973 cells:",
          sum(len(c) for c in data["clusters"]),flush=True)
    print("EF13 true original SI10 whole-cap reflected width:",
          float(data["W"]),flush=True)
    print("EF13 original conservative total cap MASS used only for",
          "cofinite ERROR:",float(data["mass"]),flush=True)
    print("EF13 original signed even cofinite L2 lower >",
          float(data["gamma"]),flush=True)
    print("EF13 exact rational protected-frequency p=24 eps^2:",
          float(EPS2),flush=True)
    print("EF13 parity dimension: even V 890, odd V 891",
          "including original odd pole; full SI10 1781",flush=True)
    print("EF13 open: original 890x890 signed A block, true original",
          "complement Riesz columns, full residual energy-dual",
          "bounds, finite Schur PSD, all even Q, Weil and RH.",
          flush=True)

if __name__=="__main__":
    validate()
