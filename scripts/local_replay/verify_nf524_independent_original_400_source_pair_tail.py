#!/usr/bin/env python3
"""NF524 independent ORIGINAL source 400-jet and two-divisor-tail audit.

Recompute original NF494 |U|,|U'| on complete B-d terminal collar by
reverse dual Horner, pay source 400-jet analytic Cauchy tails, verify the
complex strip Fourier constant and independent dyadic sum identity.
No numerical zero enumeration, new Lean build, signed Weil/RH claims.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SHA='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
B=F(11,10);D=F(1,500);RAD=F(1,25)
def read(p):
    data=Path(p).read_bytes()
    return json.loads(data),hashlib.sha256(data).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for name in ('nf494','primary','output'):p.add_argument('--'+name,required=True)
    a=p.parse_args()
    source,sh=read(a.nf494);first,ph=read(a.primary)
    assert sh==SHA and source['pass']=='NF494-native'
    assert source['original_nf407_source_sha256']==SRC
    assert source['original_nf406_seams_sha256']==SEAM
    assert F(source['original_B'])==B
    assert F(source['original_true_terminal_delta'])==D
    assert F(source['original_source_analytic_Cauchy_radius'])==RAD
    assert source['original_source_400_jet_order']==400
    assert first['pass']=='NF524-original-endpoint-full-two-source-divisor-graph-analytic-envelope-exact'
    assert first['original_NF494_full_source_SHA256']==sh
    raw=source['original_U_400_native_outward']
    assert len(raw)==400
    vals=[]
    for low,high in raw:
        low,high=F(low),F(high)
        assert low<=high
        vals.append(max(abs(low),abs(high)))
    lower,upper=map(F,raw[0])
    assert upper< -F(1,10**11)
    # Algebraically independent reverse Horner and derivative recursion.
    poly=vals[-1];dpoly=F(0)
    for coefficient in vals[-2::-1]:
        dpoly=poly+D*dpoly
        poly=coefficient+D*poly
    ratio=D/RAD;C=F(10)**400
    tail0=C*ratio**400/(1-ratio)
    tail1=C/RAD*ratio**399*(F(400)/(1-ratio)+ratio/(1-ratio)**2)
    assert tail0==F(source['original_original_U400_analytic_tail'])
    sup=poly+tail0;supder=dpoly+tail1
    assert 0<sup<F(2,10**7)
    assert 0<supder<F(7,10**4)
    # The true c(d)=U(B-d)/2 is half the independently certified U.
    m0=sup/2;m1=supder/2;Q=F(1,10000)
    low=4*m0*D*8
    log_coefficient=4*F(501,500)*3*m0
    constant=4*F(501,500)*(11*m0+8*m1*D)
    assert low<Q/501 and max(log_coefficient,constant)<Q
    # Alternate exact derivation of geometric cubic tail:
    # E[j^0]=2,E[j^1]=2,E[j^2]=6,E[j^3]=26 for weights 2^-j.
    for N in (0,4,16,32,64):
        t=F(2,2**N)*((N+2)**3+3*(N+2)**2+9*(N+2)+13)
        tnext=F(2,2**(N+1))*((N+3)**3+3*(N+3)**2+9*(N+3)+13)
        assert t-tnext==F((N+2)**3,2**N)
    result={
      'pass':'NF524-independent-original-NF494-400-source-Fourier-and-two-divisor-pair-tail',
      'original_nf494_source_SHA256':sh,'original_nf407_source_SHA256':SRC,
      'original_nf406_source_SHA256':SEAM,
      'primary_NF524_receipt_SHA256':ph,
      'independent_full_original_U_sup_reverse_Horner':str(sup),
      'independent_full_original_Uprime_sup_reverse_dual_Horner':str(supder),
      'source_original_U_B_signed_interval':[str(lower),str(upper)],
      'actual_half_U_low_height_envelope':str(low),
      'actual_half_U_high_log_coefficient':str(log_coefficient),
      'actual_half_U_high_constant':str(constant),
      'source_original_uniform_complex_strip_decay_1e_minus_4':'PASS',
      'independent_actual_divisor_dyadic_cubic_tail':'PASS',
      'multiplicity_count_constant_A':'UNSPECIFIED_EXISTENCE_FROM_LEAN',
      'original_ell_U_actual_two_source_graph_membership':'ANALYTIC_THEOREM',
      'NF523_exact_242_moment_sequence_source_graph_convergence':'ANALYTIC_THEOREM',
      'Green_closed_subspace':'OPEN','full_source_Weil_sign_diagonal':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN','new_Lean_build':False}
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF524 independent SHA-pinned original NF494 source 400-coefficient and dyadic two-source graph bound PASS')
    print('Green closure and signed Weil/RH OPEN')
if __name__=='__main__':main()
