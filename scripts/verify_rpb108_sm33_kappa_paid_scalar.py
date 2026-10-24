#!/usr/bin/env python3
"""Fast stdlib-only SM33 full-kappa scalar regression.

Conditional on original 107-cluster signed-real premises (not replayed):
 h-only mass 37.59565259375, epsilon_h<66247/1e9,
 max b9 Taylor remainder <16813/1e7, reflected width 973/32.
The full-cluster validator must separately establish those.
"""
from fractions import Fraction as F
import json
B=F(11,10); KAPPA=F(1,1000); W=F(973,32)
MASS_H=F('37.59565259375')
EPS_H_UP=F(66247,10**9); EMAX=F(16813,10**7)
MU_OLD=F(17,25000); THETA_OLD=F(51,56)

def exact_audit():
    # Explicit counterexample to SM33's old missing-kappa estimate.
    m=KAPPA/2; h=F(0)
    assert max(F(0),KAPPA-m)>h
    assert max(F(0),KAPPA-m)<=h+KAPPA
    mass=MASS_H+KAPPA*W
    H=2*B*mass
    assert mass==F(1204033883,32000000)
    assert H==F(13244372713,160000000)<83
    # Original SM40 source certificate previously verified exact
    # signed negative envelope mass across 3,892 original real cells.
    # This stdlib scalar regression does not replay that certificate.
    mass_SM40=F('16.772529359375')
    H_SM40=2*B*mass_SM40
    assert mass_SM40==F(1073441879,64000000)
    assert H_SM40==F(11807860669,320000000)
    # Additional certified SI06 all-real SUP norm, conditional on
    # the original signed Fourier/domain realization.
    const_arch=F(29,50)+F(11,7)+3*F(347,500)+F(573,500)
    Hsup=KAPPA+const_arch+F(70751,10000)
    assert const_arch==F(4707,875)
    assert Hsup==F(871887,70000)
    assert Hsup<H_SM40 and H/Hsup>6
    d_coarse=2*B*KAPPA*W/2**18
    assert d_coarse==F(10703,41943040000)
    e_coarse=EPS_H_UP+d_coarse
    assert e_coarse==F(8716573659,131072000000000)<F(1,15000)
    t_coarse=1-e_coarse/KAPPA
    assert t_coarse==F(122355426341,131072000000)>F(14,15)>THETA_OLD
    d_sharp=2*B*KAPPA*W*EMAX**2
    e_sharp=EPS_H_UP+d_sharp
    assert e_sharp==F(1062977491599207,16000000000000000000)
    assert e_sharp<e_coarse
    theta=1-e_sharp/KAPPA
    assert theta==F(14937022508400793,16000000000000000)
    assert theta>t_coarse
    cross=H*e_sharp; correction=cross/MU_OLD
    assert cross<F(11,2000) and correction<F(81,10)
    new_cross=Hsup*e_sharp
    new_schur=new_cross/MU_OLD
    assert new_cross<F(1,1000) and new_schur<F(5,4)
    return {
     "status":"SCALAR_EXACT_ONLY_CONDITIONAL_ON_ORIGINAL_CLUSTER_PREMISES",
     "H_repaired":str(H),"H_SM40":str(H_SM40),
     "H_uniform_SI06":str(Hsup),
     "SI06_mixed_squared_conditional_upper":str(new_cross),
     "SI06_negative_only_Schur_conditional_upper":str(new_schur),
     "uniform_gain_over_repaired_mass":str(H/Hsup),
     "repaired_H_over_SM40_factor":str(H/H_SM40),
     "SM40_exact_mass_premise_not_replayed":True,
     "epsilon_coarse_upper":str(e_coarse),
     "epsilon_sharp_upper":str(e_sharp),
     "squared_mixed_upper":str(cross),
     "negative_only_schur_upper":str(correction),
     "new_470_source_theta_lower":str(theta),
     "theta_decimal":float(theta),
     "all_107_original_cluster_replay":False,
     "complete_470_G_N_and_signed_odd_RH":"OPEN"}
if __name__=="__main__":
    print(json.dumps(exact_audit(),indent=2))
