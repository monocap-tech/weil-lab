#!/usr/bin/env python3
"""NF48 independent original-entry expansion and rational inverse validation.

Gaussian Decimal arithmetic chooses a rational inverse only. All positivity,
inverse errors, source balls and signs are checked with outward rational boxes.
The NF48 producer is not imported.
"""
import argparse,base64,gzip,hashlib,json,sys
from decimal import Decimal as D,localcontext
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
import validate_native_floor_transport_nf47_106 as independent
import certify_native_remaining_background_nf31_106 as originals
import certify_native_second_high_direction_nf38_106 as physical
B=independent.Box;dot=independent.dot;mm=independent.mm;tr=independent.transpose


def read(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.b64'): raw=gzip.decompress(base64.b64decode(raw))
    return json.loads(raw)


def sqrt_upper(value):
    from math import isqrt
    value=F(value);assert value>=0
    grid=10**500;integer=isqrt((value*grid*grid).__floor__())
    if F(integer*integer,grid*grid)==value:return F(integer,grid)
    return F(integer+1,grid)


def independent_inverse(A):
    n=len(A)
    def dec(value):
        value=F(value);return D(value.numerator)/D(value.denominator)
    with localcontext() as context:
        context.prec=190
        M=[[dec(v.mid()) for v in row] for row in A]
        augmented=[row[:]+[D(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
        for k in range(n):
            p=max(range(k,n),key=lambda i:abs(augmented[i][k]));assert augmented[p][k]!=0
            augmented[k],augmented[p]=augmented[p],augmented[k]
            pivot=augmented[k][k];augmented[k]=[v/pivot for v in augmented[k]]
            for i in range(n):
                if i!=k:
                    factor=augmented[i][k];augmented[i]=[x-factor*y for x,y in zip(augmented[i],augmented[k])]
        approximate=[[F(v) for v in row[n:]] for row in augmented]
        # Independently select a congruence by forward unit-LDL then invert
        # its lower triangular factor by solving columns, not backward rows.
        L=[[D(int(i==j)) for j in range(n)] for i in range(n)];pivots=[]
        for k in range(n):
            value=M[k][k]-sum((L[k][j]**2*pivots[j] for j in range(k)),D(0));assert value>0
            pivots.append(value)
            for i in range(k+1,n):L[i][k]=(M[i][k]-sum((L[i][j]*L[k][j]*pivots[j] for j in range(k)),D(0)))/value
        J=[[D(0)]*n for _ in range(n)]
        for col in range(n):
            for i in range(n):J[i][col]=D(int(i==col))-sum((L[i][j]*J[j][col] for j in range(i)),D(0))
        rational_J=[[F(v) for v in row] for row in J]
    congruence=mm(mm(rational_J,A),tr(rational_J))
    gap=min(row[i].l-sum((v.abs() for j,v in enumerate(row) if j!=i),F(0)) for i,row in enumerate(congruence));assert gap>0
    product=mm(approximate,A)
    residual=[[B(int(i==j))-product[i][j] for j in range(n)] for i in range(n)]
    rho=max(sum((v.abs() for v in row),F(0)) for row in residual);assert rho<1
    error=max(sum(map(abs,row)) for row in approximate)*rho/(1-rho)
    return [[B(v-error,v+error) for v in row] for row in approximate],dict(
        method='partial-pivot Gaussian rational candidate; independent column-solved LDL congruence',
        congruence_Gershgorin_lower=str(gap),inverse_residual_upper=str(rho),inverse_entry_error_upper=str(error))


def overlap(a,b):
    assert max(a.l,b.l)<=min(a.h,b.h)


def row_check(saved,row,idx,data,source):
    independent.validate_frame(row,idx)
    target=data[0]['authenticated_compensated_targets'][idx]
    x=list(map(F,target['retained_coefficients']))
    w=list(map(F,data[2]['parity_certificates'][idx]['exact_rational_retained_response']))
    p,q=row['old_two_constraint_pivots'];free=row['old_free_coordinates'];det=x[p]*w[q]-x[q]*w[p]
    base=[]
    for j in free:
        col=[F(int(i==j)) for i in range(56)]
        col[p]=(x[q]*w[j]-w[q]*x[j])/det;col[q]=(w[p]*x[j]-x[p]*w[j])/det;base.append(col)
    ell=list(map(F,row['third_constraint_coordinates']));k=row['third_constraint_pivot_in_old_free_coordinates']
    cols=[[a-ell[j]/ell[k]*b for a,b in zip(col,base[k])] for j,col in enumerate(base) if j!=k]
    ids=target['retained_indices']
    native=lambda i,j:B(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    sparse=[[(ids[i],v) for i,v in enumerate(col) if v] for col in cols]
    # Reverse summation order and independent interval implementation.
    C=[[sum((native(j,i)*b*a for j,b in reversed(right) for i,a in reversed(left)),B(0)) for right in sparse] for left in sparse]
    stored=independent.boxmatrix(saved['original_remaining_native_Gram'])
    for ra,rb in zip(C,stored):
        for a,b in zip(ra,rb):overlap(a,b)
    print(['even','odd'][idx],'independent original native entries replayed',flush=True)
    inverse,proof=independent_inverse(C)
    print(['even','odd'][idx],'independent inverse certified',flush=True)
    mass=[[dot(a,b) for b in cols] for a in cols]
    assert saved['physical_constraint_Gram_reconstructed_exactly']
    assert all(mass[i][i]>0 for i in range(53))
    trace=sum((inverse[i][j]*mass[j][i] for j in range(53) for i in range(53)),B(0));assert trace.l>0
    overlap(trace,B(*map(F,saved['physical_inverse_trace'])))
    # Recover unchanged original physical source projections through the
    # historical definitions, rather than accepting new stored coordinates.
    parity=['even','odd'][idx];o=physical.objects(data,source,parity)
    assert o['columns']==[(d['indices'],list(map(F,d['coefficients']))) for d in row['unchanged_joined_columns']]
    low=[[B(F(z.l,physical.n.SCALE),F(z.h,physical.n.SCALE)) for z in r] for r in o['low']]
    assert [[z.ends() for z in r] for r in low]==saved['retained_source_approximant_coordinates']
    errors=o['retained_errors'];assert list(map(str,errors))==saved['retained_source_reconstruction_errors']
    raw=[[dot(list(reversed(col)),list(reversed(r))) for col in cols] for r in low]
    paid=[[v+B(-errors[i]*sqrt_upper(dot(col,col)),errors[i]*sqrt_upper(dot(col,col))) for v,col in zip(raw[i],cols)] for i in range(3)]
    for ra,rb in zip(paid,independent.boxmatrix(saved['original_remaining_native_couplings'])):
        for a,b in zip(ra,rb):overlap(a,b)
    radii=[errors[i]+8*max((z.h-z.l)/2 for z in low[i]) for i in range(3)]
    assert list(map(str,radii))==saved['physical_retained_source_ball_radii']
    centers=[[z.mid() for z in r] for r in low]
    coordinates=[[dot(col,center) for col in cols] for center in centers]
    hat=mm(mm(coordinates,inverse),tr(coordinates))
    error=[radius*sqrt_upper(trace.h) for radius in radii]
    norms=[sqrt_upper(hat[i][i].h) for i in range(3)]
    reaction=[[hat[i][j]+B(-error[i]*norms[j]-error[j]*norms[i]-error[i]*error[j],error[i]*norms[j]+error[j]*norms[i]+error[i]*error[j]) for j in range(3)] for i in range(3)]
    for ra,rb in zip(reaction,independent.boxmatrix(saved['original_finite_remaining_reaction_Gram'])):
        for a,b in zip(ra,rb):overlap(a,b)
    original=read(f'notes/data/RPB108_NF37_{parity.upper()}_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
    assert saved['joined_native_Gram']==original['original_selected_native_energy_Gram']
    Q=independent.boxmatrix(original['original_selected_native_energy_Gram'])
    finite=independent.add(Q,independent.scale(reaction,-1))
    for ra,rb in zip(finite,independent.boxmatrix(saved['finite_joined_after_remaining_elimination'])):
        for a,b in zip(ra,rb):overlap(a,b)
    first=finite[0][0];second=finite[1][1]-finite[1][0]*finite[0][1]/first
    last=finite[2][2]-finite[2][0]*finite[0][2]/first
    last-=(finite[2][1]-finite[2][0]*finite[0][1]/first)*(finite[1][2]-finite[1][0]*finite[0][2]/first)/second
    if saved['finite_full_retained_graph_status']=='CERTIFIED_POSITIVE':assert min(first.l,second.l,last.l)>0
    print(parity,'independent finite full-retained graph PASS',flush=True)
    return dict(parity=parity,status='PASS',original_signed_native_entries_checked=1431,
        original_signed_joined_couplings_checked=159,independent_inverse=proof,
        independent_physical_native_gap_lower=str(1/trace.h),independent_finite_last_pivot=last.ends(),
        finite_full_retained_graph_positive=min(first.l,second.l,last.l)>0,
        original_physical_source_errors_paid=True,high_condensed_remaining_block_certified=False)


def main(path):
    encoded=Path(path).read_bytes();raw=gzip.decompress(base64.b64decode(encoded));cert=json.loads(raw)
    oldraw=Path('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json').read_bytes();old=json.loads(oldraw)
    assert hashlib.sha256(oldraw).hexdigest()==cert['NF47_certificate_sha256']
    data,source,hashes=originals.inputs();assert hashes==cert['original_native_archive_uncompressed_sha256']
    assert not any(cert[k] for k in ['whole_aperture_positive','complete_high_transport_certified','original_frozen_vectors_changed','original_native_inputs_regenerated','RH','F4','Lean'])
    rows=[row_check(row,frame,i,data,source) for i,(row,frame) in enumerate(zip(cert['parity_certificates'],old['parity_frames']))]
    return dict(milestone='NF48',status='PASS',encoded_certificate_sha256=hashlib.sha256(encoded).hexdigest(),
        uncompressed_certificate_sha256=hashlib.sha256(raw).hexdigest(),original_native_archive_uncompressed_sha256=hashes,
        parity_checks=rows,controls=independent.controls(),complete_high_transport_certified=False,whole_aperture_positive=False)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--certificate',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    Path(a.output).write_text(json.dumps(main(a.certificate),indent=2,sort_keys=True)+'\n')
