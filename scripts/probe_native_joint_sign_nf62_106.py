"""Freeze unresolved NF62 sign candidates for each parity for the next exact gate.

Midpoint LDL supplies candidates only. Every reported quadratic enclosure is
computed from the certified lower matrix with exact rational interval algebra.
A span-zero enclosure neither rejects the bound nor proves its positivity.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import validate_native_complete_transport_nf49_106 as prior
import certify_native_remaining_native_nf48_106 as frame
Box=prior.Box;ind=prior.ind

def run(parity):
    cp=f'notes/data/RPB108_NF62_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
    vp=f'notes/data/RPB108_NF62_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
    cert=prior.read(cp);report=prior.read(vp)
    assert report['status']=='PASS' and report['certificate_sha256']==prior.sha(cp)
    assert report['validator_sha256']==prior.sha('scripts/validate_native_joint_refinement_nf62_106.py')
    assert cert['joint_lower_bound_sign']['status']==report['joint_lower_bound_sign']['status']=='UNRESOLVED'
    size=56;M=[[None]*size for _ in range(size)];values=iter(cert['complete_joint_original_Schur_lower_upper_triangle'])
    for i in range(size):
        for j in range(i,size):M[i][j]=M[j][i]=tuple(map(F,next(values)))
    floor=prior.read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
    ids,T,retained,P=frame.constraint_frame(floor['parity_frames'][['even','odd'].index(parity)])
    physical=P+[(ids,col) for col in zip(*T)]
    rows=[]
    with localcontext() as context:
        context.prec=220
        def dec(z):z=F(z);return D(z.numerator)/D(z.denominator)
        a=[[dec((x[0]+x[1])/2) for x in row] for row in M]
        L=[[D(int(i==j)) for j in range(size)] for i in range(size)];piv=[]
        for k in range(size):
            d=a[k][k]-sum((L[k][j]**2*piv[j] for j in range(k)),D(0))
            if d<=0:
                w=[D(0)]*size;w[k]=D(1)
                for j in reversed(range(k)):w[j]=-sum((L[i][j]*w[i] for i in range(j+1,k+1)),D(0))
                rational=[F((x*D(10)**120).to_integral_value(rounding='ROUND_FLOOR'))/10**120 for x in w]
                lo=F(0);hi=F(0)
                for i in range(size):
                    for j in range(size):
                        w=rational[i]*rational[j];l,h=M[i][j]
                        lo+=w*(l if w>=0 else h);hi+=w*(h if w>=0 else l)
                coeff={}
                for scalar,(ii,cc) in zip(rational,physical):
                    for j,c in zip(ii,cc):coeff[j]=coeff.get(j,F(0))+scalar*c
                mass=sum(c*c for c in coeff.values());assert mass>0
                # This milestone records unresolved candidates, not a signed
                # obstruction. A later sign requires a fresh explicit proof.
                classification='CERTIFIED_NEGATIVE_LOWER_MATRIX_PROBE' if hi<0 else 'SPAN_ZERO' if lo<=0<=hi else 'CERTIFIED_POSITIVE_LOWER_MATRIX_PROBE'
                rows.append(dict(midpoint_nonpositive_pivot=k,fixed_rational_sign_probe=list(map(str,rational)),
                    original_physical_mass_squared=str(mass),certified_matrix_probe_value=list(map(str,[lo,hi])),
                    certified_matrix_probe_physical_quotient=list(map(str,[lo/mass,hi/mass])),
                    enclosure_spans_zero=lo<=0<=hi,lower_matrix_probe_classification=classification,actual_original_form_sign_certified=False))
            assert d!=0
            piv.append(d)
            for i in range(k+1,size):
                L[i][k]=(a[i][k]-sum((L[i][j]*L[k][j]*piv[j] for j in range(k)),D(0)))/d
    assert rows and rows[0]['midpoint_nonpositive_pivot']==cert['joint_lower_bound_sign']['first_nonpositive_midpoint_LDL_pivot']
    return dict(milestone='NF62',status='PASS',parity=parity,certificate_sha256=prior.sha(cp),validation_sha256=prior.sha(vp),
        probe_script_sha256=prior.sha(__file__),physical_frame_certificate_sha256=prior.sha('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json'),
        candidate_selection_decimal_digits=220,candidate_denominator='10^120',all_56_midpoint_pivots_examined=True,
        arithmetic='Exact Fraction interval quadratic evaluation of the certified producer lower matrix',
        independently_reconstructed_source_and_inverse_status=report['status'],
        sign_probe_candidates=rows,all_selected_negative_midpoint_candidates_have_span_zero_enclosures=all(r['enclosure_spans_zero'] for r in rows),
        entire_matrix_sign_certified=False,actual_negative_original_form_claimed=False,whole_aperture_positive=False,
        next_gate='Refine any certified negative lower-matrix residual first; otherwise resolve the first span-zero residual with complete direct-source/inverse enclosures, then certify the entire original Schur gate.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--parity',choices=['even','odd'],required=True)
    args=parser.parse_args();result=run(args.parity)
    Path(f'notes/data/RPB108_NF62_{args.parity.upper()}_UNRESOLVED_JOINT_SIGN_PROBES_20261010.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('NF62',args.parity,'remaining sign probes frozen with exact rational enclosures')
