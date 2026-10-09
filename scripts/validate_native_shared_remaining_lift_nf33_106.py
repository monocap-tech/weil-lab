#!/usr/bin/env python3
"""NF33 replay and independent exact witness/mass/payment checks."""
import json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
import certify_native_shared_remaining_lift_nf33_106 as c
n=c.n;I=c.I
ROOT='notes/data/RPB108_NF33_'
def read(name):
    raw=Path(ROOT+name+'_20261009.json').read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def interval(v):return I(*map(F,v))
def validate():
    data,source,hashes=c.prev.inputs()
    trial,th=read('FIXED_SHARED_REMAINING_LIFT');frame,fh=read('SHARED_REMAINING_FRAME_CERTIFICATE')
    assert c.choose(data,source)==trial
    replay=c.certify_frame(data,source,trial)
    replay.update(fixed_trial_sha256=th,authenticated_input_sha256=c.prev.SHA,native_archive_sha256=hashes)
    assert replay==frame
    rows=[]
    for idx,parity in enumerate(['even','odd']):
        cert,sh=read(parity.upper()+'_LIFTED_PROBE_CERTIFICATE');tr=trial['parities'][idx];fr=frame['parity_certificates'][idx]
        assert cert['fixed_trial_sha256']==frame['fixed_trial_sha256']==th
        assert cert['authenticated_input_sha256']==frame['authenticated_input_sha256']==c.prev.SHA
        assert cert['native_archive_sha256']==hashes
        ids=tr['retained_indices']+tr['high_indices'];v=list(map(F,tr['fixed_probe_coefficients']))
        x=list(map(F,data[0]['authenticated_compensated_targets'][idx]['retained_coefficients']))
        w=list(map(F,data[2]['parity_certificates'][idx]['exact_rational_retained_response']))
        assert sum(a*b for a,b in zip(v,x))==sum(a*b for a,b in zip(v,w))==0
        mass=sum(z*z for z in v);assert mass==F(cert['exact_lifted_probe_mass'])==F(fr['exact_lifted_probe_mass'])
        # A flat full quadratic sum differs from the producer's nested matrix
        # multiplication and the frame's T/H2 congruence.
        q=sum((v[i]*v[j]*c.native(source,a,b) for i,a in enumerate(ids) for j,b in enumerate(ids)),I(0))
        original=interval(cert['original_native_energy']);fq=interval(fr['lifted_probe_native_energy'])
        assert q.l>0 and max(q.l,original.l,fq.l)<=min(q.h,original.h,fq.h)
        sq=interval(cert['reconstructed_remaining_source_square']);eta=F(cert['physical_residual_error_upper'])
        root=F(n.sqrt_r(F(sq.h,n.SCALE)).h,n.SCALE);payment=2*eta*root+eta*eta
        assert str(payment)==cert['source_square_error_payment']
        gamma=sq+I(-payment,payment);assert gamma.ends()==cert['original_complete_remaining_source_square']
        score=original-gamma/F(207,1000);assert score.ends()==cert['floor_score']
        assert (gamma/original).ends()==cert['source_square_over_native_energy']
        assert cert['native_projection_check']['paid_overlap']
        check=cert['native_projection_check'];p=interval(check['reconstructed']);o=interval(check['original'])
        radius=eta # residual error is no smaller than unsquared source error.
        assert p.l-n.SCALE*radius<=o.h and p.h+n.SCALE*radius>=o.l
        expected='LIFTED_PROBE_DIAGONAL_PASSES' if score.l>0 else 'SHARED_LIFT_FLOOR_REJECTED' if score.h<0 else 'UNRESOLVED'
        assert cert['status']==expected
        assert not cert['remaining_complete_source_Gram_certified'] and not cert['actual_negative_vector_claimed'] and not cert['whole_aperture_positive']
        assert fr['certified_selected_shell_entry_count']==108
        assert F(fr['selected_shell_physical_operator_norm_upper'])==11*F(fr['selected_shell_max_entry_upper'])
        rows.append(dict(parity=parity,status=expected,certificate_sha256=sh,exact_membership_and_mass=True,three_way_native_energy_overlap=True,error_payment_checked=True,independent_native_projection_overlap_checked=True))
    return dict(milestone='NF33',status='PASS',fixed_trial_sha256=th,frame_certificate_sha256=fh,
        shared_frame_fresh_replay_identical=True,selection_fresh_replay_identical=True,parity_checks=rows,
        complete_collective_high_Gram_certified=False,whole_aperture_positive=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    Path(a.output).write_text(json.dumps(validate(),indent=2)+'\n')
