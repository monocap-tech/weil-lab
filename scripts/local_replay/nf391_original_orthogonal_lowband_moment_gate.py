#!/usr/bin/env python3
"""NF391: combine two ORTHOGONAL original lowband observations exactly.

The n512 exterior-original shadow and the candidate-selected j387 shadow
are physically orthogonal; the squared Bessel lower is strictly stronger
than either isolated scalar lowband criterion. Source-only exact Fraction
tests prove a threshold below 1.81e-20 but DO NOT assert native j387 STOP.

When --native390 is supplied, recompute the exact interval decision on the
genuine original pole-corrected selected moment. If omitted, report UNTESTED.
No new signed kernel cells, no Fourier integral, no infinite upper or RH.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)

SHA512='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
GIT_NF375='03c709571046d3f09307614aaded9749f5a15ba1'
GIT_J387='d705ae312be5324bff64f3a9540e30e8b8bd34dc'
SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
B=F(11,10)
EXTERIOR_MIN=F(834,10**16)   # > 8.34e-14 in verified original NF384
SELECTED_NORM_BUDGET=F(2673,10**16)  # > sqrt(tau^2-EXTERIOR_MIN^2)
MOMENT_CEILING=F(181,10**22) # 1.81e-20; a sufficient (not necessary) stop gate
ALPHA=F(-88873,2**48)
JNORM_CAP=F(363,2)*abs(ALPHA)
D=F(2401,2*10**28)

def read(path,sha=None,git_sha=None):
    raw=Path(path).read_bytes()
    if sha: assert hashlib.sha256(raw).hexdigest()==sha,('original SHA mismatch',path)
    if git_sha:
        g=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
        assert g==git_sha,('original Git blob mismatch',path)
    return json.loads(raw)

def run(p512,nf375,j387,native390=None,output=None):
    a=read(p512,sha=SHA512)
    t=read(nf375,git_sha=GIT_NF375)
    j=read(j387,git_sha=GIT_J387)
    assert a['unfitted_n']==512 and a['selected_rank']==242 and a['critical_count']==4
    assert a['original_physical_16_Gram_overlaps'] is True
    assert a['original_signed_32_CE_BP_overlaps'] is True
    assert a['original_WJJ_WJF_archived_cells_reused']==30371
    assert a['original_source_sha256']==SOURCE_SHA and a['original_rank_sha256']==RANK_SHA
    assert a['W_ODD_NEG']==a['RH']=='OPEN'
    assert F(a['original_direction_four_squared_residual_budget'])==D
    assert t['source_sha256']==SOURCE_SHA and t['measured_original_lowband'] is False
    assert t['W_ODD_NEG']==t['RH']=='OPEN'
    assert j['original_rank_sha256']==RANK_SHA and j['original_nf375_source_sha256']==SOURCE_SHA
    assert j['original_nf375_git_blob_sha1']==GIT_NF375
    assert j['scale_alpha']==str(ALPHA)
    assert len(j['coefficients_raw_source_numerators'])==242
    assert j['nonzero_raw_source_indices']==[0,2]
    assert j['endpoint_value_exact']=='0'
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    q=[r for r in t['directions'][3]['dyadic_cutoff_options'] if r['log2_cutoff']==24]
    assert len(q)==1 and q[0]['cutoff']==2**24
    assert q[0]['exact_squared_original_individual_gate'] is True
    H=F(q[0]['highband_upper'])
    tau=F(q[0]['chosen_future_lowband_target'])
    assert tau==F(7,25*10**12) and H>0
    g0,g1=map(F,a['outside_E4_norm2_interval'])
    b0,b1=map(F,a['complete_original_signed_u4_qperp_interval'])
    assert 0<g0<=g1<B and 0<b0<=b1
    # Direct original signed b512 and NF375 highband tail imply for
    # q512 orthogonal to J242:
    # ||P_(span q512)(t_L - j)|| > EXTERIOR_MIN for every j in J242.
    assert b0*b0 > g1*(H+EXTERIOR_MIN)**2
    # Since the original j387 belongs to J242, j387 ⟂ q512:
    # ||t_L-j387||² >= |<t_L-j387,q512>|²/g512
    #                    +|<t_L-j387,j387>|²/||j387||².
    assert EXTERIOR_MIN**2 + SELECTED_NORM_BUDGET**2 > tau**2
    assert F(2)*B < F(9,4)
    assert F(121)*abs(ALPHA)*F(3,2)==JNORM_CAP
    threshold=(H+SELECTED_NORM_BUDGET)*JNORM_CAP
    assert threshold<MOMENT_CEILING
    assert threshold<(H+tau)*JNORM_CAP, 'new joint gate is not stronger'
    out={
       'standing':'NF391 SOURCE-NATIVE ORIGINAL TWO ORTHOGONAL SHADOWS EXACT LOWBAND NECESSARY GATE; SELECTED NATIVE MOMENT PENDING',
       'original_n512_SHA256':SHA512,
       'original_nf375_git_blob_sha1':GIT_NF375,
       'original_j387_git_blob_sha1':GIT_J387,
       'original_nf370_direction_four_budget':str(D),
       'cutoff':2**24,
       'original_nf375_fourth_lowband_target':str(tau),
       'original_nf375_fourth_highband_upper':str(H),
       'certified_n512_orthogonal_lowband_norm_strictly_greater_than':str(EXTERIOR_MIN),
       'remaining_selected_shadow_norm_upper_sufficient_for_stop':str(SELECTED_NORM_BUDGET),
       'exact_squared_combined_gate':'e²+r²>tau² TRUE',
       'original_j387_physical_norm_strict_upper':str(JNORM_CAP),
       'native_selected_pole_corrected_moment_discrepancy_stop_threshold_strictly_below':str(threshold),
       'source_only_rational_moment_discrepancy_ceiling':str(MOMENT_CEILING),
       'original_nf390_selected_native_result_supplied':native390 is not None,
       'nf390_native_selected_moment_result':'NOT PROVIDED',
       'nf387_specific_candidate_joint_method_stopped':False,
       'original_signed_lowband_integral_computed':False,
       'original_full_lowband_upper_computed':False,
       'whole_original_exterior_inverse_computed':False,
       'original_strong_domain_audit':'OPEN',
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    if native390 is not None:
        n=read(native390)
        assert n['original_rank_sha256']==RANK_SHA and n['original_source_sha256']==SOURCE_SHA
        assert n['original_signed_archive_zip_sha256']=='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
        assert n['nf387_selected_raw_candidate_git_blob_sha1']==GIT_J387
        assert n['pole_restored_for_selected_test'] is True
        assert n['fresh_original_signed_kernel_cells']==0
        assert n['original_physical_16_Gram_overlaps'] is True
        assert n['W_ODD_NEG']==n['RH']=='OPEN'
        assert n['actual_original_signed_lowband_integral_computed'] is False
        discrepancy=list(map(F,n['actual_selected_moment_discrepancy_interval']))
        jnorm2=list(map(F,n['original_j387_physical_norm_squared_interval']))
        assert len(discrepancy)==2 and len(jnorm2)==2
        assert 0<jnorm2[0]<=jnorm2[1]<JNORM_CAP**2
        dlo=(F(0) if discrepancy[0]<=0<=discrepancy[1]
             else min(abs(discrepancy[0]),abs(discrepancy[1])))
        # The native physical norm2 interval is genuine; all exact comparisons
        # remain rational, avoid rounding an irrational sqrt.
        stopped=dlo*dlo > (H+SELECTED_NORM_BUDGET)**2*jnorm2[1]
        old_stopped=bool(n['actual_original_j387_specific_NF375_lowband_candidate_stopped'])
        if old_stopped: assert stopped, 'new stronger criterion cannot lose old stop'
        out['nf390_native_selected_moment_result']='SHA-PINNED SOURCE-MATCHED INTERVAL CONSUMED'
        out['nf390_pole_restored']=True
        out['native_moment_abs_interval_outward_lower']=str(dlo)
        out['native_j387_physical_norm2_outward_upper']=str(jnorm2[1])
        out['nf387_specific_candidate_joint_method_stopped']=bool(stopped)
        out['prior_nf390_isolated_candidate_method_stopped']=old_stopped
        out['standing']=('NF391 ORIGINAL FROZEN J387 STRICT METHOD STOP; INFINITE COMPLEMENT OPEN'
                         if stopped else
                         'NF391 ORIGINAL J387 COMBINED SELECTED MOMENT GATE INCONCLUSIVE')
    if output:
        p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(out,indent=2)+'\n')
    print('NF391 original exact n512 exterior and original j387 selected orthogonality PASS')
    print('NF391 original necessary moment mismatch ceiling:',str(MOMENT_CEILING))
    print('NF391 original selected native outcome:',out['nf390_native_selected_moment_result'])
    print('NF391 complete original lowband upper / W-ODD-NEG / RH OPEN')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--original-512',required=True)
    p.add_argument('--nf375',required=True)
    p.add_argument('--j387',required=True)
    p.add_argument('--native390')
    p.add_argument('--output')
    a=p.parse_args()
    run(a.original_512,a.nf375,a.j387,a.native390,a.output)
