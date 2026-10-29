#!/usr/bin/env python3
"""NF387: construct a NONZERO original J242 dyadic trial with certified Fourier tail.

No signed lowband mismatch integral or original lowband upper is computed.
The source-moment-based scale is a reproducible heuristic, not an optimizer.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
from nf386_original_fourier_primal_lowband_entry import tail_upper
sys.set_int_max_str_digits(0)

RANK_SHA256 = '9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
NF375_GIT_BLOB_SHA1 = '03c709571046d3f09307614aaded9749f5a15ba1'
NF375_SOURCE_SHA256 = 'abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
NF375_NATIVE_SHA256 = 'a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'
B = F(11,10)
C = F(37,64)
KAPPA_UPPER = F(44,7) * C  # pi < 22/7; angular frequency 2*pi*C
DYAD_BITS = 48
SOURCE_A1 = F(-40060235101,1048576000000000000)
CUT = 2**24

def read_rank(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==RANK_SHA256, 'original selected rank mismatch'
    r=json.loads(raw)
    assert r['retained_physical_rank_upper']==242
    assert r['retained_original_pole'] is True
    assert r['original_nodes'][0][0]=='37/64'
    assert int(r['selected_multiplicities'][0])>=3
    assert sum(int(q) for q in r['selected_multiplicities'])+1==242
    return r

def read_nf375(path):
    raw=Path(path).read_bytes()
    git_blob_sha1=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
    assert git_blob_sha1==NF375_GIT_BLOB_SHA1
    j=json.loads(raw)
    assert j['source_sha256']==NF375_SOURCE_SHA256
    assert j['native_report_sha256']==NF375_NATIVE_SHA256
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    assert j['measured_original_lowband'] is False
    assert len(j['directions'])==4
    d=j['directions'][3]
    assert d['direction']==4
    assert F(d['signed_original_first_sine_moment'])==SOURCE_A1
    q=[v for v in d['dyadic_cutoff_options'] if v['log2_cutoff']==24]
    assert len(q)==1 and q[0]['cutoff']==CUT
    assert q[0]['exact_squared_original_individual_gate'] is True
    return F(q[0]['chosen_future_lowband_target'])

def nearest_int(q):
    q=F(q)
    return (2*q.numerator+q.denominator)//(2*q.denominator)

def produce(rank,nf375,output=None):
    read_rank(rank)
    tau=read_nf375(nf375)
    assert tau==F(28,10**14)
    # Scale chosen to match central polynomial sine coefficient 121*alpha
    # with NF375's actual fourth original signed first endpoint sine moment
    # A1; this is merely a deterministic source-informed candidate choice.
    n=nearest_int((SOURCE_A1/F(121))*2**DYAD_BITS)
    assert n==-88873
    alpha=F(n,2**DYAD_BITS)
    j0=121*alpha
    j2=-100*alpha
    assert j0==F(-10753633,2**48)
    assert j2==F(8887300,2**48)
    assert j0+j2*B*B==0, 'exact original boundary zero failed'
    # Original J242 first selected node has the two basis functions
    # sin(2*pi*37/64*x) and x² sin(2*pi*37/64*x).
    # Thus j=(121-100x²)*alpha*sin(...) on I, identically zero outside I.
    # At x=B: |j'(B)| <= 200*B*|alpha|.
    # On [-B,B], |p|<=121, |p'|<=200*B, |p''|=200,
    # |j''| <= |alpha|*(200+2*(200B)*Kappa+121*Kappa²).
    abs_alpha=abs(alpha)
    endpoint_derivative_abs_upper=200*B*abs_alpha
    second_deriv_L1_upper=2*B*abs_alpha*(
        200+2*(200*B)*KAPPA_UPPER+121*KAPPA_UPPER*KAPPA_UPPER)
    combined=2*endpoint_derivative_abs_upper+second_deriv_L1_upper
    assert F(0)<combined<F(1,400000)<F(1,10)
    freq_tail2=tail_upper(0,combined,CUT)
    assert F(0)<freq_tail2<tau*tau/64
    # Full original 242-coordinate dyadic vector in RAW SOURCE coordinates,
    # not normalized/physical orthonormal frame coordinates.
    nums=[0]*242
    nums[0]=-10753633
    nums[2]=8887300
    assert sum(bool(k) for k in nums)==2
    out={
      'standing':'NF387 ACTUAL NONZERO ORIGINAL J242 DYADIC TRIAL AND FOURIER TAIL UPPER; SIGNED MISMATCH OPEN',
      'original_rank_sha256':RANK_SHA256,
      'nf375_git_blob_sha1':NF375_GIT_BLOB_SHA1,
      'original_nf375_source_sha256':NF375_SOURCE_SHA256,
      'original_nf374_native_sha256':NF375_NATIVE_SHA256,
      'original_selected_frame':'RAW original J242 selected source coordinates, 241 original nodes plus retained pole; NOT orthonormal frame',
      'original_support_half_width':str(B),
      'original_first_retained_center':str(C),
      'first_retained_multiplicity_at_least_three':True,
      'construction':'alpha*(121-100*x^2)*sin(2*pi*(37/64)*x) supported on [-11/10,11/10]; alpha nearest dyadic to NF375 direction4 signed first sine moment /121',
      'dyadic_denominator_power':48,
      'dyadic_raw_selected_coordinate_numerators':nums,
      'nonzero_raw_source_coordinate_indices':[0,2],
      'nonzero_raw_source_coefficient_fractions':[str(j0),str(j2)],
      'source_signed_first_sine_moment_fourth_direction':str(SOURCE_A1),
      'scale_alpha':str(alpha),
      'actual_j_is_nonzero':True,
      'actual_original_j_endpoint_value_at_B':'0',
      'actual_j_endpoint_derivative_abs_upper':str(endpoint_derivative_abs_upper),
      'actual_j_second_derivative_L1_upper':str(second_deriv_L1_upper),
      'actual_j_two_endpoint_derivative_plus_curvature_upper':str(combined),
      'actual_j_endpoint_and_curvature_cap_lt_one_tenth':True,
      'cutoff':CUT,
      'original_nf375_direction4_future_lowband_norm_upper_target':str(tau),
      'actual_j_high_frequency_squared_tail_strict_upper':str(freq_tail2),
      'actual_j_squared_tail_strictly_less_than_tau2_over_64':True,
      'actual_original_source_matched_signed_Fourier_mismatch_integrated':False,
      'actual_original_lowband_norm_upper_certified':False,
      'candidate_spectral_optimality':'UNTESTED; no signed source adaptation is claimed by heuristic scale',
      'original_operator_domain_review':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    if output:
        p=Path(output)
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(out,indent=2)+'\n')
    print('NF387 original dyadic j !=0 (raw indices 0,2) PASS; exact boundary value zero')
    print('NF387 endpoint-derivative+curvature cap:',str(combined))
    print('NF387 strict original selected j Fourier squared tail upper:',str(freq_tail2))
    print('NF387 actual signed Fourier mismatch not measured; W-ODD-NEG/RH OPEN')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--rank',required=True)
    p.add_argument('--nf375',required=True)
    p.add_argument('--output')
    a=p.parse_args()
    produce(a.rank,a.nf375,a.output)
