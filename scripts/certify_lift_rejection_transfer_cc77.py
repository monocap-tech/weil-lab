#!/usr/bin/env python3
"""Transfer the complete-source witness rejection to CC76's frozen lift."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_remaining_background_nf31_106 as p

def run(transfer,trial,certs,highgram):
    data,source,hashes=p.inputs();rows=[];k=F(207,1000)
    for idx,(old,tr,c,hg) in enumerate(zip(transfer['parity_certificates'],trial['parities'],certs,highgram['parity_certificates'])):
        assert old['parity']==tr['parity']==c['parity']==hg['parity']
        a=list(map(F,tr['inherited_constraint_coordinates']));T=[list(map(F,row)) for row in old['exact_remaining_basis']]
        u=[sum(v*z for v,z in zip(row,a)) for row in T]
        original=list(map(F,tr['fixed_probe_coefficients']));assert u==original[:56]
        hs=tr['high_indices'];assert hs==old['high_indices']
        Z=[list(map(F,row)) for row in old['fixed_shared_remaining_high_lift']]
        newhigh=[-sum(v*z for v,z in zip(row,a)) for row in Z]
        delta=[v-z for v,z in zip(newhigh,original[56:])]
        # NF25's final paid Gram contains P_F L e_h as columns 1 and 2.
        for i in range(2):assert F(hg['original_complete_three_source_Gram'][i+1][i+1][1])<16
        norm_error=4*sum(map(abs,delta));assert norm_error<F(1,10**65)
        ids=tr['retained_indices']+hs
        def Q(i,j):return p.I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
        cross=[sum((z*Q(i,h) for i,z in zip(ids,original)),p.I(0)) for h in hs]
        energy_error=2*sum(abs(d)*v.absupper() for d,v in zip(delta,cross))
        energy_error+=sum(abs(delta[i]*delta[j])*Q(hs[i],hs[j]).absupper() for i in range(2) for j in range(2))
        qlo,qhi=map(F,c['original_native_energy']);glo,ghi=map(F,c['original_complete_remaining_source_square'])
        root=F(p.n.sqrt_r(glo).l,p.n.SCALE);assert root>norm_error
        new_gamma_lower=(root-norm_error)**2;new_energy_upper=qhi+energy_error
        score_upper=new_energy_upper-new_gamma_lower/k;assert score_upper<0
        shell_square_upper=F(old['measured_high_source_operator_norm_upper'])**2*sum(z*z for z in u)
        shell_fraction_upper=shell_square_upper/new_gamma_lower
        assert shell_fraction_upper<F(1,10**113)
        rows.append(dict(parity=c['parity'],exact_same_retained_probe=True,
            changed_high_coefficients=list(map(str,delta)),complete_source_norm_perturbation_upper=str(norm_error),
            original_energy_perturbation_upper=str(energy_error),
            CC76_complete_source_square_lower=str(new_gamma_lower),CC76_probe_energy_upper=str(new_energy_upper),
            CC76_floor_score_upper=str(score_upper),CC76_shared_family_floor_estimator_rejected=True,
            CC76_selected_shell_fraction_upper=str(shell_fraction_upper),
            CC76_outside_selected_shell_fraction_lower=str(1-shell_fraction_upper),
            NF33_necessary_fraction_of_floor_response_credit_lower=str(1-k*qhi/glo),
            arbitrary_H2_retuning_rejected=False,actual_negative_vector_claimed=False))
        print(c['parity'],'source norm perturbation',float(norm_error),'CC76 score upper',float(score_upper),flush=True)
    return dict(milestone='CC77',parity_certificates=rows,native_archive_sha256=hashes,
        complete_remaining_54_source_Gram_certified=False,whole_aperture_positive=False,
        full_Weil_nonimplication_claimed=False)

if __name__=='__main__':
    a=argparse.ArgumentParser()
    for name in ['transfer','trial','even','odd','highgram']:a.add_argument(name)
    a.add_argument('--output',required=True);a=a.parse_args()
    raw=[Path(getattr(a,name)).read_bytes() for name in ['transfer','trial','even','odd','highgram']]
    expected=['7fdc6cd93c62e4964efd3d6b7b7a9cf058b8605cf2fbf44bab420ca7dc0dba98',
        '89683af32013c4bfc3ed3bd66d90ff889131a4ccdd03dd769523a7dfbbcd9cff',
        '9bdf992dda4aca110f2c776183ce9e6f614623fdc373389485cf25e06711a9dd',
        'ce8c97c61db0ade92d2b10d2bed56775eb07d0bb66ae956654c94716a4febac5',
        '7f0fa640a873ba4746d326a0898a5869887e6c23ddafb1ee8ff2a10e5c9c80da']
    assert [hashlib.sha256(v).hexdigest() for v in raw]==expected
    d=list(map(json.loads,raw));r=run(d[0],d[1],d[2:4],d[4]);r['input_sha256']=[hashlib.sha256(v).hexdigest() for v in raw]
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
