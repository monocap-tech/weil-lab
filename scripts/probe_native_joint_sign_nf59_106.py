"""Freeze unresolved even NF59 sign candidates for the next exact gate.

Midpoint LDL supplies candidates only. Every reported quadratic enclosure is
computed from the certified lower matrix with exact rational interval algebra.
A span-zero enclosure neither rejects the bound nor proves its positivity.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import validate_native_complete_transport_nf49_106 as prior
import certify_native_remaining_native_nf48_106 as frame
Box=prior.Box;ind=prior.ind

def run():
    cp='notes/data/RPB108_NF59_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
    vp='notes/data/RPB108_NF59_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json'
    cert=prior.read(cp);report=prior.read(vp)
    assert report['status']=='PASS' and report['certificate_sha256']==prior.sha(cp)
    assert cert['joint_lower_bound_sign']['status']==report['joint_lower_bound_sign']['status']=='UNRESOLVED'
    size=56;M=prior.unpack(cert['complete_joint_original_Schur_lower_upper_triangle'],size)
    floor=prior.read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
    ids,T,retained,P=frame.constraint_frame(floor['parity_frames'][0])
    physical=P+[(ids,col) for col in zip(*T)]
    rows=[]
    with localcontext() as context:
        context.prec=220
        def dec(z):z=F(z);return D(z.numerator)/D(z.denominator)
        a=[[dec((x.l+x.h)/2) for x in row] for row in M]
        L=[[D(int(i==j)) for j in range(size)] for i in range(size)];piv=[]
        for k in range(size):
            d=a[k][k]-sum((L[k][j]**2*piv[j] for j in range(k)),D(0))
            if d<=0:
                w=[D(0)]*size;w[k]=D(1)
                for j in reversed(range(k)):w[j]=-sum((L[i][j]*w[i] for i in range(j+1,k+1)),D(0))
                rational=[F((x*D(10)**120).to_integral_value(rounding='ROUND_FLOOR'))/10**120 for x in w]
                value=ind.dot(rational,[ind.dot(row,rational) for row in M])
                coeff={}
                for scalar,(ii,cc) in zip(rational,physical):
                    for j,c in zip(ii,cc):coeff[j]=coeff.get(j,F(0))+scalar*c
                mass=sum(c*c for c in coeff.values());assert mass>0
                # This milestone records unresolved candidates, not a signed
                # obstruction. A later sign requires a fresh explicit proof.
                classification='CERTIFIED_NEGATIVE_LOWER_MATRIX_PROBE' if value.h<0 else 'SPAN_ZERO' if value.l<=0<=value.h else 'CERTIFIED_POSITIVE_LOWER_MATRIX_PROBE'
                rows.append(dict(midpoint_nonpositive_pivot=k,fixed_rational_sign_probe=list(map(str,rational)),
                    original_physical_mass_squared=str(mass),certified_matrix_probe_value=value.ends(),
                    certified_matrix_probe_physical_quotient=(value*(1/mass)).ends(),
                    enclosure_spans_zero=value.l<=0<=value.h,lower_matrix_probe_classification=classification,actual_original_form_sign_certified=False))
            assert d!=0
            piv.append(d)
            for i in range(k+1,size):
                L[i][k]=(a[i][k]-sum((L[i][j]*L[k][j]*piv[j] for j in range(k)),D(0)))/d
    assert rows and rows[0]['midpoint_nonpositive_pivot']==cert['joint_lower_bound_sign']['first_nonpositive_midpoint_LDL_pivot']
    return dict(milestone='NF59',status='PASS',parity='even',certificate_sha256=prior.sha(cp),validation_sha256=prior.sha(vp),
        probe_script_sha256=prior.sha(__file__),physical_frame_certificate_sha256=prior.sha('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json'),
        candidate_selection_decimal_digits=220,candidate_denominator='10^120',all_56_midpoint_pivots_examined=True,
        arithmetic='Exact Fraction interval quadratic evaluation of the certified producer lower matrix',
        independently_reconstructed_source_and_inverse_status=report['status'],
        sign_probe_candidates=rows,all_selected_negative_midpoint_candidates_have_span_zero_enclosures=all(r['enclosure_spans_zero'] for r in rows),
        entire_matrix_sign_certified=False,actual_negative_original_form_claimed=False,whole_aperture_positive=False,
        next_gate='Resolve the first frozen even sign-probe direction and the odd rejecting witness using tighter complete inverse/source enclosures; then certify the entire original Schur gate.')

if __name__=='__main__':
    result=run();Path('notes/data/RPB108_NF59_EVEN_UNRESOLVED_JOINT_SIGN_PROBES_20261010.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('NF59 even sign probes frozen; exact interval signs recorded for all selected nonpositive midpoint candidates')
