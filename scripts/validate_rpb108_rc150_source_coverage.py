"""RC150: exact seven-carrier completion of the five-source response frame."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv
from validate_rpb108_rc149_combined_five_matrix import run as rc149_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc149_run(paths[1:],replay)
    frame=json.loads(raw[11]);joint=json.loads(raw[13])
    assert [x['milestone'] for x in (prior,frame,joint)]==['RC149','RC138','RC136']
    S=[[F(x) for x in row] for row in frame['trial_source_matrix']]
    GLo=[[F(x) for x in row] for row in joint['actual_D_Gram_Loewner_lower']]
    GHi=[[F(x) for x in row] for row in joint['actual_D_Gram_Loewner_upper']]
    # Native seven-vector order: P0, psi0, f0, w14, v10, z_b6, t10.
    # The existing five include B=w14-alpha*psi0 and u=(v10+z_b6)/2.
    psi=[F(i==1) for i in range(7)]
    delta=[F(i==5)-F(i==4) for i in range(7)]
    W=[S[i]+[psi[i],delta[i]] for i in range(7)]
    # The inherited exact inversion helper has no row pivoting; choose the
    # native row order that exposes the seven nonzero source pivots.
    order=[0,2,3,4,6,1,5]
    P=[[F(j==i) for j in range(7)] for i in order]
    Wi=mm(inv(mm(P,W)),P);I=mm(W,Wi)
    assert I==[[F(i==j) for j in range(7)] for i in range(7)]
    assert mm(Wi,W)==I
    fullLo,fullHi=cong(W,GLo),cong(W,GHi)
    assert psd(fullLo) and psd(add(fullHi,fullLo,-1))
    A=[row[:5] for row in fullLo[:5]]
    B=[row[5:] for row in fullLo[:5]]
    C=[row[5:] for row in fullLo[5:]]
    schur=add(C,mm(transpose(B),mm(inv(A),B)),-1)
    assert psd(schur)
    floor=min(schur[0][0],schur[1][1])/10**8
    assert floor>0 and psd(add(schur,[[floor if i==j else F(0) for j in range(2)] for i in range(2)],-1))
    # These two independent columns cannot be represented by the five-source
    # response certificate. The positive Schur complement is a quantitative
    # actual-D-Gram separation, not an inverse-response estimate.
    assert prior['all_five_source_mixtures_certified'] and F(prior['relative_source_Gram_matrix_width_upper'])<F(1,2)
    assert prior['original_Weil_or_augmented_actions_performed'] is False
    return dict(milestone='RC150',status='PASS: seven-carrier source completion and positive two-dimensional Gram complement',
        starting_commit='45f627eaf76efd5025c18bd6290ae046643aabd2',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',
        carrier_family=['P0','psi0','f0','w14','v10','z_b6','t10'],
        RC149_paid_response_sources=['P0','f0','w14-alpha*psi0','(v10+z_b6)/2','t10'],
        missing_complement_sources=['psi0','z_b6-v10'],
        augmented_source_frame=ser(W),augmented_frame_inverse=ser(Wi),
        actual_D_Gram_complement_Schur=ser(schur),
        complement_positive_diagonal_floor=str(floor),
        source_frame_rank=7,paid_response_rank=5,unpaid_response_complement_rank=2,
        five_source_half_Gram_matrix_width_inherited=prior['relative_source_Gram_matrix_width_upper'],
        seven_source_half_Gram_matrix_width_certified=False,
        complement_inverse_response_matrix_evaluated=False,
        required_Stage_I_matrix_tolerance_specified_in_RC149=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
        next_cursor='pay the psi0 and z_b6-v10 response columns and their mixed rows, or prove a native-source reduction eliminating them; then compare with explicit Stage I tolerance and original Weil transport')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=18)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC150 PASS: exact seven-carrier source coverage audit')
