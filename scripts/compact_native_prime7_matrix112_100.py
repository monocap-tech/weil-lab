#!/usr/bin/env python3
"""Outward compact enclosure and fresh finite sign check at aperture 1."""
import argparse
import hashlib
import json
from pathlib import Path
from certify_native_legendre112_100 import F,I,positive_pivots


def certificate(path):
    raw=Path(path).read_bytes();original=json.loads(raw)
    assert original['aperture']=='1'
    assert original['physical_degrees']==list(range(112))
    assert original['prime_terms']==[2,3,4,5,7]
    assert original['whole_domain_positivity'] is False
    assert all(F(x)>0 for x in original['shifted_pivot_lower_bounds'])
    entries=original['matrix_intervals'];I.grid=10**80
    assert len(entries)==112 and all(len(row)==112 for row in entries)
    matrix=[];triangle=[]
    for i,row in enumerate(entries):
        target=[]
        for j,pair in enumerate(row):
            assert pair==entries[j][i]
            lo,hi=map(F,pair);assert lo<=hi
            if (i+j)%2:assert lo==hi==0
            x=I(lo,hi);assert x.lo<=lo<=hi<=x.hi
            target.append(x)
            if j<=i:triangle.append([str(int(x.lo*I.grid)),str(int(x.hi*I.grid))])
        matrix.append(target)
    tau=F(original['raw_physical_coercivity_lower_bound'])
    blocks=[]
    for parity in (0,1):
        degrees=list(range(parity,112,2))
        block=[[matrix[i][j]-(I(tau) if i==j else I(0)) for j in degrees] for i in degrees]
        pivots=positive_pivots(block)
        blocks.append({'degrees':degrees,'shifted_pivot_lower_bounds':[str(x.lo) for x in pivots]})
    broken=[[I(-1),I(0)],[I(0),I(1)]]
    try:positive_pivots(broken)
    except ArithmeticError:pass
    else:raise AssertionError('Negative control accepted')
    result={k:v for k,v in original.items() if k not in
            ('matrix_intervals','pivot_lower_bounds','shifted_pivot_lower_bounds','maximum_entry_width')}
    script_root=Path(__file__).resolve().parent
    result.update(status='certified native 112-vector finite restriction at 1; outward compact enclosure',
                  original_matrix_sha256=hashlib.sha256(raw).hexdigest(),
                  original_matrix_git_blob_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
                  original_interval_grid_digits=original['interval_grid_digits'],interval_grid_digits=80,
                  matrix_encoding='row-major lower triangle integer endpoints on grid 10^-80',
                  lower_triangle_row_major=triangle,outward_inclusions_checked=12544,
                  original_maximum_entry_width=original['maximum_entry_width'],
                  maximum_entry_width=str(max(x.hi-x.lo for row in matrix for x in row)),
                  parity_block_pivots=blocks,exponential_error_ceiling='55',kernel_error_ceiling='5',
                  construction_script_sha256=hashlib.sha256((script_root/'certify_native_prime7_matrix112_100.py').read_bytes()).hexdigest(),
                  base_constructor_sha256=hashlib.sha256((script_root/'certify_native_legendre112_100.py').read_bytes()).hexdigest(),
                  compact_checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  negative_control_rejected=True,compact_encoding_lossless=False,
                  full_source_gram_certified=False,corrected_schur_sign_certified=False,
                  whole_domain_positivity=False,whole_domain_positivity_frontier='399/400')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result=certificate(args.input)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'aperture':result['aperture'],'finite_margin':result['raw_physical_coercivity_lower_bound']}))

