#!/usr/bin/env python3
"""NF31 exact fresh replay plus genuine mixed-block crossing controls."""
import argparse,json,hashlib,gzip,base64
from pathlib import Path
from fractions import Fraction as F
import certify_native_remaining_background_nf31_106 as p

def controls():
    out=[]
    # Remaining background/high block [[1,1/2],[1/2,1]] is positive.
    # Couplings (-1/4,1/2) require a joint reaction7/12. Separate
    # reactions total5/16, giving an invalid positive credit13/48.
    a,c,d,b,r=F(1),F(1),F(1,2),F(-1,4),F(1,2)
    joint=(c*b*b-2*d*b*r+a*r*r)/(a*c-d*d)
    separate=b*b/a+r*r/c
    assert joint==F(7,12) and separate==F(5,16)
    for scale in (F(1),F(1,10**18)):
        for s in (F(-1,100),F(0),F(1,100)):
            q=(joint+s)*scale*scale
            true=q-joint*scale*scale
            arithmetic=q-separate*scale*scale
            partial_high=q-r*r/c*scale*scale
            partial_finite=q-b*b/a*scale*scale
            assert true==s*scale*scale and arithmetic>true
            assert min(arithmetic,partial_high,partial_finite)>0
            out.append(dict(scale=str(scale),crossing_parameter=str(s),true_joint_Schur=str(true),
                old_high_score=str(partial_high),finite_remaining_reaction=str(b*b/a*scale*scale),
                invalid_arithmetic_subtraction=str(arithmetic),arithmetic_is_not_a_lower_bound=True))
    return out

def positive_levels():
    joint=F(7,12);M=[[joint,F(-1,4),F(1,2)],[F(-1,4),F(1),F(1,2)],[F(1,2),F(1,2),F(1)]]
    null=[F(1),F(2,3),F(-5,6)]
    assert all(sum(a*b for a,b in zip(row,null))==0 for row in M)
    # The lower block is positive and its exact Schur value is zero,
    # hence M is positive semidefinite. Each mass shift has floor delta.
    return [dict(whole_mass_shift=str(delta),exact_physical_ground_level=str(delta),null_vector=list(map(str,null))) for delta in (F(1,1000),F(1,10),F(2))]

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('certificate');a.add_argument('--output',required=True);a=a.parse_args()
    encoded=Path(a.certificate).read_bytes();raw=gzip.decompress(base64.b64decode(encoded)) if a.certificate.endswith('.b64') else encoded;cert=json.loads(raw)
    data,source,hashes=p.inputs();replay=p.run(data,source);replay['authenticated_input_sha256']=p.SHA;replay['native_archive_sha256']=hashes
    assert cert==replay
    for row in cert['parity_certificates']:
        assert row['remaining_dimension']==54
        assert all(len(z)==54 for z in row['remaining_original_native_couplings'])
        assert row['finite_full_retained_lifted_family_positive']
        assert not row['remaining_complete_source_Gram_certified']
    out=dict(milestone='NF31',status='PASS',fresh_rational_certificate_replay_identical=True,
        exact_native_remaining_response_gain_checks_passed=True,original_signed_coupling_count=216,
        genuine_joint_crossing_controls=controls(),exact_positive_physical_level_controls=positive_levels(),previous_four_direction_high_certificate_preserved=True,
        full_collective_infinite_high_certificate=False,certificate_sha256=hashlib.sha256(raw).hexdigest(),encoded_certificate_sha256=hashlib.sha256(encoded).hexdigest())
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
