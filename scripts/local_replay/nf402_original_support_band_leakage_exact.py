#!/usr/bin/env python3
"""NF402 original physical-support versus Fourier-band information gate.

Original data supply localization radius only; the original selected
Fourier tail and lowband exterior leakage remain UNMEASURED.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,argparse

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--localization',default='notes/data/provisional/NF401_original_projection_localization_exact.json')
    p.add_argument('--receipt',default='notes/data/provisional/NF401_original_242D_execution_receipt.json')
    p.add_argument('--acceptance',default='notes/data/provisional/NF401_original_242D_selected_column_independent_acceptance.json')
    p.add_argument('--nf398',default='notes/data/provisional/NF398_original_j387_selected_signed_native.json')
    p.add_argument('--output',default=None)
    args=p.parse_args()
    loc,locsha=load(args.localization)
    rec,_=load(args.receipt)
    acc,accsha=load(args.acceptance)
    n,nsha=load(args.nf398)
    original_sha='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
    parent_sha='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
    assert loc['original_native_sha256']==acc['native_sha256']==rec['original_native_json_sha256']==original_sha
    assert loc['original_nf398_native_sha256']==nsha==parent_sha
    assert rec['native_column_accepted'] and loc['strict_original_rational_comparisons_pass']
    assert n['original_NF375_fourth_cutoff']==2**24
    assert loc['W_ODD_NEG']==loc['RH']==rec['W_ODD_NEG']==rec['RH']=='OPEN'
    assert loc['complete_original_lowband_upper'] is False
    assert loc['candidate_fourier_tail_certified'] is False
    H=F(loc['source_highband_bound'])
    tau=F(loc['source_lowband_target'])
    rho=H+tau
    cap=F(329,10**15)
    assert tau==F(7,25*10**12) and 0<H<tau and rho<cap

    # Exact-rational finite Hilbert witness (NOT original source).
    # Fourier low projection E=diag(1,0), support S=1/2 [[1,1],[1,1]].
    S=lambda v:((v[0]+v[1])/2,(v[0]+v[1])/2)
    E=lambda v:(v[0],F(0))
    sq=lambda v:sum((z*z for z in v),F(0))
    U=(F(1),F(0))
    t=S(U)
    j=t
    assert sq((t[0]-j[0],t[1]-j[1]))==0
    assert sq((j[0]-E(j)[0],j[1]-E(j)[1]))==F(1,4)>0
    assert sq((U[0]-S(U)[0],U[1]-S(U)[1]))==F(1,2)
    assert E(S((F(0),F(1))))!=S(E((F(0),F(1))))

    # Conditional inequality uses exact rational numbers and pays exterior
    # low-band leakage L. For any actual j within tau on I and j_*=Pw,
    # T=||high j_*|| <= rho + sqrt(tau^2+L^2).
    # A STOP requires T_lower>rho and (T_lower-rho)^2>tau^2+L_upper^2.
    test_tail=F(1,10**12)
    test_leak=F(1,10**13)
    assert test_tail>rho
    assert (test_tail-rho)**2>tau**2+test_leak**2

    out={
       'pass':'NF402',
       'standing':'SOURCE-PINNED SUPPORT/BAND NONCOMMUTATION AND CONDITIONAL LEAKAGE GATE ONLY',
       'source_original_nf401_native_sha256':original_sha,
       'source_original_nf398_native_sha256':parent_sha,
       'original_nf401_localization_sha256':locsha,
       'original_nf401_acceptance_sha256':accsha,
       'original_cutoff':2**24,
       'original_physical_support_half_width':'11/10',
       'source_target_tau':str(tau),
       'source_highband_H':str(H),
       'source_localization_radius_rho':str(rho),
       'radius_upper_exact':str(cap),
       'exact_synthetic_commutator_nonzero':True,
       'exact_synthetic_zero_support_error_positive_Fourier_tail':True,
       'coupled_tail_leakage_method_stop_condition':
         'Tlo>rho AND (Tlo-rho)^2>tau^2+Lupper^2, Tlo<=||high(j*)||, Lupper>=||U_L||_(I^c)',
       'coupled_condition_exact_arithmetic_example_pass':True,
       'original_candidate_tail_lower_measured':False,
       'original_lowband_outside_support_leakage_upper_measured':False,
       'original_complement_lowband_upper_measured':False,
       'full_lowband_upper':False,
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    data=json.dumps(out,indent=2)+'\n'
    if args.output:
        Path(args.output).parent.mkdir(parents=True,exist_ok=True)
        Path(args.output).write_text(data)
    print(data,end='')

if __name__=='__main__':main()
