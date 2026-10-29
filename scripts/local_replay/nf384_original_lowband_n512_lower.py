#!/usr/bin/env python3
"""NF384: SHA-pinned original n512 signed witness -> nonzero low-band norm.
A lower-bound diagnostic only; never an upper, n513, Weil sign, or RH result.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
N512_SHA256='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
NF375_GIT_BLOB_SHA1='03c709571046d3f09307614aaded9749f5a15ba1'
NF375_SRC_SHA256='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
NF375_NATIVE_SHA256='a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'
B=F(11,10)
D=F(2401,2*10**28)
# Strictly certified lower bounds at k>20; k=20 has no positive result.
LOWER={20:F(0),21:F(21,10**16),22:F(385,10**16),
       23:F(646,10**16),24:F(834,10**16)}

def read_pinned(path, sha256=None, git_blob_sha1=None):
    raw=Path(path).read_bytes()
    if sha256 is not None:
        assert hashlib.sha256(raw).hexdigest()==sha256, 'native SHA mismatch'
    if git_blob_sha1 is not None:
        hdr=b'blob '+str(len(raw)).encode()+b'\x00'
        assert hashlib.sha1(hdr+raw).hexdigest()==git_blob_sha1, 'NF375 Git blob SHA mismatch'
    return json.loads(raw)

def run(original_512,nf375,output=None):
    a=read_pinned(original_512,sha256=N512_SHA256)
    t=read_pinned(nf375,git_blob_sha1=NF375_GIT_BLOB_SHA1)
    assert a['unfitted_n']==512 and a['selected_rank']==242 and a['critical_count']==4
    assert a['original_physical_16_Gram_overlaps'] is True
    assert a['original_signed_32_CE_BP_overlaps'] is True
    assert a['original_WJJ_WJF_archived_cells_reused']==30371
    assert a['original_lowband_integral_computed'] is False
    assert a['entire_exterior_inverse_computed'] is False
    assert a['W_ODD_NEG']==a['RH']=='OPEN'
    assert F(a['original_direction_four_squared_residual_budget'])==D
    assert t['source_sha256']==NF375_SRC_SHA256
    assert t['native_report_sha256']==NF375_NATIVE_SHA256
    assert t['measured_original_lowband'] is False
    assert t['original_whole_residual_certified'] is False
    assert len(t['directions'])==4
    g_lo,g_hi=map(F,a['outside_E4_norm2_interval'])
    b_lo,b_hi=map(F,a['complete_original_signed_u4_qperp_interval'])
    assert 0<g_lo<=g_hi<B and 0<b_lo<=b_hi
    row=t['directions'][3]
    assert row['direction']==4 and len(row['dyadic_cutoff_options'])==5
    report=[]
    for v in row['dyadic_cutoff_options']:
        k=v['log2_cutoff']
        assert k in LOWER and v['cutoff']==2**k
        h=F(v['highband_upper']); target=F(v['chosen_future_lowband_target'])
        assert h>0 and target>0 and v['exact_squared_original_individual_gate'] is True
        lower=LOWER[k]
        # EXACT inequality proving ||low-j|| > lower, independent of j in J242:
        #   |b| <= ||q|| ( ||low-j|| + ||high|| ).
        strict_positive=(b_lo*b_lo > g_hi*(h+lower)**2)
        if k>20:
            assert strict_positive,('low-band lower not certified',k)
        else:
            assert lower==0
            assert b_hi*b_hi<g_lo*h*h, 'at k20 high-band envelope not dominant'
        # This particular witness does not force failure of the old future target.
        assert b_hi*b_hi<g_lo*(h+target)**2
        report.append(dict(log2_cutoff=k,cutoff=2**k,
            original_NF375_highband_upper=str(h),
            original_NF375_unmeasured_lowband_upper_target=str(target),
            strict_universal_lowband_norm_lower=str(lower) if k>20 else '0',
            positive_lower_certified=(k>20),
            this_one_witness_does_not_exclude_original_NF375_target=True))
    out=dict(
        standing='NF384 ORIGINAL N512 SIGNED LOWBAND LOWER AT FOUR CUTS; ORIGINAL UPPER UNMEASURED',
        original_n512_sha256=N512_SHA256,original_nf375_git_blob_sha1=NF375_GIT_BLOB_SHA1,
        original_family='unchanged J242, four PR355 sources, NF369 Y0, NF370 T',
        conditional_inequality='H4(L;j)>=max(0,abs(Wodd(u4,qperp))/||qperp||-high4(L)) for any j in J242, inherited signed strong-domain hypothesis',
        cutoff_results=report,original_n513_measured=False,
        original_lowband_upper_computed=False,whole_strong_residual_upper=False,
        strong_operator_domain_audit='OPEN',W_ODD_NEG='OPEN',RH='OPEN')
    if output:
        p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(out,indent=2)+'\n')
    for r in report:
        print('NF384 cutoff 2^%d lower=%s (target not excluded)'%(
            r['log2_cutoff'],r['strict_universal_lowband_norm_lower']))
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--original-512',required=True)
    ap.add_argument('--nf375',required=True)
    ap.add_argument('--output')
    a=ap.parse_args()
    run(a.original_512,a.nf375,a.output)
