#!/usr/bin/env python3
"""NF378: exact-rational complete-signed-action dual obstruction gate.

It does NOT compute an original signed pairing. It certifies the necessary
thresholds from the original NF375 source report and tests the algebra of the
multi-witness Gram lower bound. W-ODD-NEG, lowband H and RH remain OPEN.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

NF375_SHA='f0067870a77f3825005395ac0f6f3e928521796ef3251c04463ba402c40cb5ec'
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
NATIVE_SHA='a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'


def checked(path,sha):
    data=Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest()==sha, ('parent SHA mismatch',path)
    return json.loads(data)


def run(rank_path,nf375_path):
    rank=checked(rank_path,RANK_SHA)
    nf375=checked(nf375_path,NF375_SHA)
    assert rank['retained_original_pole']
    assert sum(rank['selected_multiplicities'])==241
    assert nf375['source_sha256']==SOURCE_SHA
    assert nf375['native_report_sha256']==NATIVE_SHA
    assert nf375['accepted_cutoffs']==[2**k for k in range(20,25)]
    assert len(nf375['directions'])==4
    original=[]
    for i,row in enumerate(nf375['directions'],1):
        assert row['direction']==i
        budget=F(row['original_residual_squared_budget'])
        assert budget>0
        options=[]
        for p in row['dyadic_cutoff_options']:
            k=int(p['log2_cutoff'])
            assert 20<=k<=24 and p['cutoff']==2**k
            hi=F(p['highband_upper']);tau=F(p['chosen_future_lowband_target'])
            assert hi>0 and tau>0 and (hi+tau)**2<budget
            options.append(dict(log2_cutoff=k,highband_upper=str(hi),
               future_lowband_target=str(tau),
               exact_whole_signed_dual_obstruction_threshold=str(hi+tau),
               squared_gate_below_original_budget=True))
        assert len(options)==5
        smallest=min(options,key=lambda x:F(x['exact_whole_signed_dual_obstruction_threshold']))
        original.append(dict(direction=i,original_residual_squared_budget=str(budget),
          direct_whole_action_obstruction_iff_normalized_coupling_squared_exceeds=str(budget),
          cutoffs=options,best_cutoff_for_signed_form_obstruction=smallest['log2_cutoff'],
          best_full_signed_coupling_threshold=str(F(smallest['exact_whole_signed_dual_obstruction_threshold']))))
    # Fixed exact toy: single signed dual witnesses cannot obstruct the 4.5
    # threshold, but the original whole Gram joint dual does. No claims about
    # the actual Weil source or complete exterior are made by this toy.
    G=((F(1),F(0)),(F(0),F(1)))
    b=(F(3),F(4))
    assert G[0][0]*G[1][1]-G[0][1]**2==1
    single=max(v*v for v in b)
    joint=b[0]**2+b[1]**2
    assert single==16 and joint==25 and single<F(9,2)**2<joint
    # PS3 orientation-failure countercontrol, original mathematical type.
    A=F(1,2);B=(F(1),F(0));
    H1=B[0]*B[0]/F(1)+B[1]*B[1]/F(100)
    H2=B[0]*B[0]/F(100)+B[1]*B[1]/F(1)
    assert H1==1 and H2==F(1,100)
    assert A-H1==-F(1,2) and A-H2==F(49,100)
    out=dict(status='EXACT_ORIGINAL_NF375_ANCHORED_FULL_SIGNED_DUAL_GATE_ONLY',
       source_sha256=NF375_SHA,rank_sha256=RANK_SHA,
       inherited_signed_multiplier_identification='CONDITIONAL_ON_ORIGINAL_FORM_AND_DOMAIN',
       exact_pole_annihilation='s in J242 and q in J242 physical orthogonal complement',
       original_selected_rank=242,critical_directions=4,
       original_cutoff_thresholds=original,
       matrix_dual_lemma='b*G^-1 b <= ||Q_J m(D)u||_2^2 for any independent exterior witness family with physical Gram G',
       directional_whole_obstruction='b*G^-1 b > original_residual_squared_budget implies NO J242 subtraction passes the fixed sufficient strong-residual gate',
       directional_lowband_obstruction='b*G^-1 b > (highband_upper + future_lowband_target)^2 implies NO J242 subtraction passes THAT fixed cutoff lowband sufficient gate',
       toy_single_squared=16,toy_joint_squared=25,toy_budget_squared=str(F(9,2)**2),
       ps3_abstract_signs=[str(A-H1),str(A-H2)],
       actual_Weil_signed_B_vector_computed=False,
       actual_Weil_exterior_witness_Gram_computed_here=False,
       actual_lowband_integral_computed=False,
       actual_full_residual_obstructed=False,
       actual_inverse_Schur_response_computed=False,
       original_operator_domain_audit='OPEN',W_ODD_NEG='OPEN',RH='OPEN')
    print('NF378 exact whole signed-action exterior dual gate: PASS (thresholds only)',flush=True)
    for o in original:
        print('direction',o['direction'],'best cutoff',o['best_cutoff_for_signed_form_obstruction'],
         'best threshold',float(F(o['best_full_signed_coupling_threshold'])),flush=True)
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--rank',required=True);p.add_argument('--nf375',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    out=run(a.rank,a.nf375)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
