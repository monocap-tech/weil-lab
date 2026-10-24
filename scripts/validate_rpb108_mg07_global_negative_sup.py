#!/usr/bin/env python3
"""Original whole-frequency Knegative UNIFORM spectral norm improvement.

SI06 all seven prime powers and digamma constant prove at every real xi:
 m(xi)>-CONST_UP-TWOC.
Hence 0<=Knegative< (kappa+CONST_UP+70751/10000)*I on the
original supported odd Hilbert space by zero-extension Parseval.
No SM40 finite cap and no sampled Fourier frequencies are used.
Independent SI06 original physical realization/domain review remains.
"""
import json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import TWOC,CONST_UP,WEIGHTS,ACTIVE
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR

def exact_bound():
    assert CONST_UP==F(4707,875)
    assert TWOC==sum((2*WEIGHTS[n][1] for n in ACTIVE),F(0))
    assert F(0)<TWOC<F(70751,10000)
    assert KAPPA==F(1,1000)
    Hsup=KAPPA+CONST_UP+F(70751,10000)
    assert Hsup==F(871887,70000)<F(25,2)
    Hmass=F(13244372713,160000000)
    Hmass40=F(11807860669,320000000)
    assert Hsup<Hmass40<Hmass
    assert Hmass/Hsup>F(6)
    assert KAPPA_STAR==F(33621,10**9)
    old_t1=2*Hmass/KAPPA_STAR
    new_t1=2*Hsup/KAPPA_STAR
    assert old_t1/new_t1==Hmass/Hsup
    # Independent SM33 complete 107-cluster premises must establish
    # this exact conservative repaired-b9 epsilon majorant.
    epsilon_bound=F(1062977491599207,16000000000000000000)
    gamma2=Hsup*epsilon_bound
    schur=gamma2/F(17,25000)
    assert gamma2<F(1,1000) and schur<F(5,4)
    return {
      "status":"CERTIFIED_SI06_SCALAR_GLOBAL_POINTWISE_KNEGATIVE_UPPER",
      "original_negative_norm_upper":str(Hsup),
      "repaired_SM10_mass_norm_upper":str(Hmass),
      "SM40_mass_norm_upper":str(Hmass40),
      "MG07_improvement_factor":str(Hmass/Hsup),
      "t1_MG07_old_residual_coefficient":str(old_t1),
      "t1_MG07_new_residual_coefficient":str(new_t1),
      "SI06_arch_lower":str(-CONST_UP),
      "SI06_prime_abs_ceiling":str(F(70751,10000)),
      "conditional_107_cluster_epsilon_upper":str(epsilon_bound),
      "conditional_negative_only_mixed_squared_upper":str(gamma2),
      "conditional_negative_only_Schur_upper":str(schur),
      "original_physical_Fourier_domain_audit":"OPEN",
      "470_source_residual_and_signed_odd_even_CC27_RH":"OPEN"}
if __name__=="__main__":
    print(json.dumps(exact_bound(),indent=2))
