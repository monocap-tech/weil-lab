"""NF60: reconstruct the complete source of each frozen NF59 physical target.

Combine exact physical coefficients before source integration. The original
archives, high minorant, target and all historical entry payments stay fixed.
This is a scalar enclosure refinement, not a full matrix sign certificate.
"""
import argparse,json
from fractions import Fraction as F
from pathlib import Path
import certify_native_joint_refinement_nf59_106 as p

def run(parity):
    ctx,_,_,_=p.parent_context(parity)
    cp=f'notes/data/RPB108_NF59_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
    vp=f'notes/data/RPB108_NF59_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
    c=p.context49.read(cp);v=p.context49.read(vp)
    assert v['status']=='PASS' and v['certificate_sha256']==p.old.sha(cp)
    z=list(map(F,c['fixed_high_selection']['normalized_NF58_joint_witness']))
    physical=ctx['P']+[(ctx['ids'],col) for col in ctx['T']]
    merged={}
    for (ii,cc),w in zip(physical,z):
        for j,a in zip(ii,cc):merged[j]=merged.get(j,F(0))+w*a
    ii=sorted(merged);cc=[merged[j] for j in ii]
    mass=sum(a*a for a in cc);assert 0<mass<=1
    expected=F(c['inherited_joint_lower_bound_sign']['witness_original_physical_mass_squared']) if 'inherited_joint_lower_bound_sign' in c else None
    work=Path('work/nf60')/parity;work.mkdir(parents=True,exist_ok=True)
    key=p.old.sha(__file__)+'-'+p.old.sha(cp)
    m=ctx['m'];norm=p.v.ceilnorm(cc)
    print(parity,'exact combined physical target frozen',flush=True)
    sy=p.old.cached(work/'combined_source.pkl',key,lambda:m.source(ii,cc))
    fun=p.functional(sy,m,max(ii));e=m.eta*norm
    low=[p.dot(p.n.basis(j),fun)+p.I(-e,e) for j in ctx['ids']]
    r=p.v.r.projection(sy,low,ctx['ids'])
    error=e+16*max(F(a.h-a.l,2*p.n.SCALE) for a in low)
    adj=p.fast.adjoint(r,m,len(r[1]),len(r[2]),max(map(len,r[3])))
    raw=p.fast.gram(r,adj);nr=p.v.r.normupper(raw)
    payment=2*error*nr+error*error
    paid=raw+p.I(-payment,payment)
    result=dict(milestone='NF60',parity=parity,aperture='53/50',producer_sha256=p.old.sha(__file__),
        inherited_NF59_certificate_sha256=p.old.sha(cp),inherited_NF59_validation_sha256=p.old.sha(vp),
        frozen_normalized_target=list(map(str,z)),combined_physical_indices=ii,combined_physical_coefficients=list(map(str,cc)),
        exact_combined_physical_mass_squared=str(mass),physical_norm_upper=str(norm),
        source_low_projection=[a.ends() for a in low],regular_and_signed_pole_tail_operator_upper=str(m.eta),
        unprojected_source_error_upper=str(e),projected_source_error_upper=str(error),
        raw_combined_projected_source_norm_squared=raw.ends(),approximant_norm_upper=str(nr),
        source_norm_squared_error_payment=str(payment),paid_combined_complete_source_norm_squared=paid.ends(),
        moment_degree=1700,interval_grid_digits=800,all_thirteen_prime_cells_retained=True,
        signed_pole_and_endpoint_log_retained=True,original_inputs_regenerated=False,
        original_frozen_vectors_changed=False,whole_matrix_sign_certified=False,whole_aperture_positive=False)
    print(parity,'complete combined source norm paid',flush=True)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--parity',choices=['even','odd'],required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();Path(args.output).write_text(json.dumps(run(args.parity),indent=2,sort_keys=True)+'\n')
