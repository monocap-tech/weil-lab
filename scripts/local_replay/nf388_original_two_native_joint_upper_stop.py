#!/usr/bin/env python3
"""NF388: complete original n512,n513 TWO-RAY strong dual UPPER.

The original signed native n513 is fetched from preserved GitHub Actions
artifact #12882010193 / run 40820718599 by the workflow, SHA-pinned here.
NO inference of infinite exterior upper, full Weil sign or RH.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)

SHA512='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
SHA513='e0aaa0abb29c8ec75b3524ec6197c12235a7fc7fa66d76c77c4643c2ff27bffe'
ARTIFACT_ZIP_SHA='193483b0c757f88f836479e5d50261b629439ed8534875feeeee66008bb121ad'
ARTIFACT_ID=12882010193
ARTIFACT_RUN=40820718599
ORIGINAL_SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
ORIGINAL_RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
B=F(11,10)
D=F(2401,2*10**28)
# Conservative *outward* rational bracketing of original signed physical native:
G1_FLOOR=F(10855,10000)
G2_FLOOR=F(10856,10000)
ABS_B1_CEILING=F(137528,10**18)
ABS_B2_CEILING=F(3110,10**17)
RHO_CEILING=F(1,75)
JOINT_DUAL_FRACTION_CEILING=F(31,200)
UNSEEN_REQUIRED_FRACTION_FLOOR=F(169,200)

def load_native(path,sha,expected_n):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha,(expected_n,'original SHA mismatch')
    j=json.loads(raw)
    assert j['unfitted_n']==expected_n
    assert j['selected_rank']==242 and j['critical_count']==4
    assert j['original_physical_16_Gram_overlaps'] is True
    assert j['original_signed_32_CE_BP_overlaps'] is True
    assert j['original_WJJ_WJF_archived_cells_reused']==30371
    assert j['original_lowband_integral_computed'] is False
    assert j['entire_exterior_inverse_computed'] is False
    assert j['original_source_sha256']==ORIGINAL_SOURCE_SHA
    assert j['original_rank_sha256']==ORIGINAL_RANK_SHA
    assert F(j['original_direction_four_squared_residual_budget'])==D
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    g=tuple(map(F,j['outside_E4_norm2_interval']))
    b=tuple(map(F,j['complete_original_signed_u4_qperp_interval']))
    assert len(g)==len(b)==2 and 0<g[0]<=g[1]<B and b[0]<=b[1]
    return j,g,b

def evaluate(p512,p513,output=None):
    a,g1,b1=load_native(p512,SHA512,512)
    b,g2,b2=load_native(p513,SHA513,513)
    assert a['parent_original_archive_sha256']==b['parent_original_archive_sha256']
    assert a['original_frame_sha256']==b['original_frame_sha256']
    assert b['original_512_native_source_sha256']==SHA512
    assert 0<b1[0] and 0<b2[0], 'original certified signed responses not strictly positive'
    assert g1[0]>G1_FLOOR and g2[0]>G2_FLOOR
    assert b1[1]<ABS_B1_CEILING and b2[1]<ABS_B2_CEILING
    # Exact original physical v512,v513 are orthogonal on I, with
    # ||v512||²=||v513||²=B; q_i=(I-P_(J242+F4)) v_i.
    # Therefore |<q512,q513>|² <= (B-g1)*(B-g2).
    # The following exact inequality strictly caps the NORMALIZED
    # original off-diagonal Gram by rho<1/75.
    assert (B-G1_FLOOR)*(B-G2_FLOOR)*75**2 < G1_FLOOR*G2_FLOOR
    assert RHO_CEILING*75==1
    # For normalized 2x2 Gram N=[[1,rho],[rho,1]] with |rho|<1/75,
    # N^-1 < (75/74)*I in Loewner order.
    # Thus exact two-ray b*G^-1*b is strictly LESS THAN:
    cap=F(75,74)*(ABS_B1_CEILING**2/G1_FLOOR+
                   ABS_B2_CEILING**2/G2_FLOOR)
    cap_fraction=cap/D
    assert cap_fraction < JOINT_DUAL_FRACTION_CEILING < F(1)
    assert F(1)-JOINT_DUAL_FRACTION_CEILING==UNSEEN_REQUIRED_FRACTION_FLOOR
    # More than 84.5% D must be in the physical complement of the
    # actual two-ray span if full strong residual squared >=D.
    result={
      'standing':'NF388 ORIGINAL N512,N513 NATIVE-REPLAY TWO-RAY EXACT UPPER: METHOD STOP ONLY',
      'source_native_512_sha256':SHA512,
      'source_native_513_sha256':SHA513,
      'original_n513_artifact_zip_sha256':ARTIFACT_ZIP_SHA,
      'original_n513_actions_artifact_id':ARTIFACT_ID,
      'original_n513_actions_run_id':ARTIFACT_RUN,
      'original_complete_signed_32_overlaps_checked':True,
      'original_physical_16_overlap_checked':True,
      'original_fixed_selected_rank':242,
      'original_fixed_critical_count':4,
      'source_frame_hashes_consistent':True,
      'certified_normalized_physical_Gram_cross_abs_strictly_less_than':str(RHO_CEILING),
      'original_512_lower_physical_norm_squared_bound':str(G1_FLOOR),
      'original_513_lower_physical_norm_squared_bound':str(G2_FLOOR),
      'original_512_signed_abs_upper_bound':str(ABS_B1_CEILING),
      'original_513_signed_abs_upper_bound':str(ABS_B2_CEILING),
      'original_nf370_direction_four_squared_residual_budget':str(D),
      'complete_original_two_ray_dual_squared_strict_upper_fraction_of_D':str(JOINT_DUAL_FRACTION_CEILING),
      'exact_sharper_rational_intermediate_upper_fraction_of_D':str(cap_fraction),
      'one_frozen_two_ray_method_can_exhaust_direction_four_budget':False,
      'if_actual_full_squared_residual_ge_D_unseen_physical_orthogonal_response_strictly_gt_fraction_of_D':str(UNSEEN_REQUIRED_FRACTION_FLOOR),
      'actual_cross_Gram_computed':False,
      'actual_whole_original_exterior_residual_upper_computed':False,
      'actual_original_lowband_upper_computed':False,
      'actual_original_full_energy_inverse_computed':False,
      'analytic_domain_audit':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    if output:
        target=Path(output);target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(json.dumps(result,indent=2)+'\n')
    print('NF388 pinned native original n513 accepted SHA:',SHA513)
    print('NF388 original normalized cross <1/75; complete two-ray dual² <31/200 * D')
    print('NF388 one two-ray obstruction STOP; original infinite complement, W-ODD-NEG, RH OPEN')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--original-512',required=True)
    p.add_argument('--native-513',required=True)
    p.add_argument('--output')
    a=p.parse_args()
    evaluate(a.original_512,a.native_513,a.output)
