#!/usr/bin/env python3
"""Test larger corrected Schur shifts against the pinned complete actual Gram."""
import argparse
import hashlib
import json
from pathlib import Path
from certify_native_legendre_small_window import F, I, positive_pivots

GRAM_SHA256 = '32f664f3e4a686dd220755c18f8aa38b790955b9c6b1a08e99fb8c5ac3a1615c'
COMPACT_SHA256 = 'd7c50dd7e784300ddedb2d2d020d21f427ebd2254ca841b7b35888cb532dec96'
NATIVE_BLOB = '513b970b3d7d521c6d9f8b8f6551d550c99584d7'
SOURCE_BLOB = 'cbdd89a810bf400bf39988a56319ac8c217eb1b7'


def read_pinned(path, blob=None, sha256=None):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    git = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if (blob is not None and git != blob) or (sha256 is not None and digest != sha256):
        raise ValueError('Pinned certificate mismatch: '+str(path))
    return json.loads(raw), digest, git


def certificate(gram_path, native_path, source_path):
    gram, gram_hash, gram_blob = read_pinned(gram_path)
    compact = gram.get('compact_enclosure', False)
    if compact:
        if COMPACT_SHA256 is None or gram_hash != COMPACT_SHA256:
            raise ValueError('Compact Gram hash mismatch')
        assert gram['original_complete_gram_sha256'] == GRAM_SHA256
    elif gram_hash != GRAM_SHA256:
        raise ValueError('Original Gram hash mismatch')
    native, native_hash, _ = read_pinned(native_path, blob=NATIVE_BLOB)
    source, source_hash, _ = read_pinned(source_path, blob=SOURCE_BLOB)
    assert gram['native_certificate_sha256'] == native_hash
    assert gram['source_certificate_sha256'] == source_hash
    assert gram['physical_degrees'] == gram['projected_away_degrees'] == list(range(84))
    assert gram['native_source_pairing_count'] == 7056
    assert gram['all_mixed_terms_retained'] and gram['whole_domain_positivity']
    assert gram['complement_inverse_factor'] == '100/51'
    assert gram['physical_complement_lower'] == '51/100'
    beta, comp = F(100,51), F(51,100)
    delta = F(gram['actual_gram_operator_error_upper'])
    eta = F(source['source_map_error_upper'])
    norm = F(gram['surrogate_residual_map_norm_upper'])
    assert delta == eta*(2*norm+eta) and delta < F(1,10**45)
    if compact:
        assert gram['compact_grid_digits'] == 80
        triangle = gram['lower_triangle_row_major']
        assert len(triangle) == 3570
        original = [[None for _ in range(84)] for _ in range(84)]
        k = 0
        for i in range(84):
            for j in range(i+1):
                pair = tuple(F(int(x),10**80) for x in triangle[k])
                original[i][j] = original[j][i] = pair
                k += 1
    else:
        original = [[tuple(map(F, pair)) for pair in row] for row in gram['residual_gram_surrogate']]
    assert len(original) == 84 and all(len(row) == 84 for row in original)
    assert all(original[i][j] == original[j][i] and original[i][j][0] <= original[i][j][1]
               for i in range(84) for j in range(84))
    trace = sum((original[i][i][1] for i in range(84)), F(0))
    if compact:
        source_trace = F(gram['original_surrogate_trace_upper'])
        assert trace >= source_trace and norm*norm >= source_trace
    else:
        assert norm*norm >= trace
    lift2 = beta*beta*(trace+delta)
    if not compact:
        assert lift2 == F(gram['lift_norm_squared_upper'])
    assert gram['lift_operator_norm_integer_upper'] == 10
    lift = F(47,5)
    assert lift*lift > lift2
    I.grid = 10**80
    r = [[I(lo,hi) for lo,hi in row] for row in original]
    q = [[I(*pair) for pair in row] for row in native['matrix_intervals']]
    # Keep the complete 84x84 matrix, including enclosed mixed parity entries.
    lower = [[q[i][j]-beta*r[i][j]-(I(beta*delta) if i == j else I(0))
              for j in range(84)] for i in range(84)]
    assert all(r[i][j].lo <= original[i][j][0] <= original[i][j][1] <= r[i][j].hi
               for i in range(84) for j in range(84))
    attempts = []
    for exponent in range(18,30):
        tau = F(1,10**exponent)
        shifted = [[lower[i][j]-(I(tau) if i == j else I(0)) for j in range(84)] for i in range(84)]
        try:
            pivots = positive_pivots(shifted)
        except ArithmeticError:
            attempts.append({'shift':str(tau),'certified':False})
            continue
        attempts.append({'shift':str(tau),'certified':True})
        break
    else:
        raise ArithmeticError('No positive corrected shift certified')
    assert tau >= F(1,10**29)
    mu = tau*comp/(tau+comp*(1+lift*lift))
    kappa = mu/(10*(mu+23))
    simple_mu, simple_kappa = F(1,10**20), F(4,10**23)
    assert mu > simple_mu and kappa > simple_kappa
    control = [row[:] for row in shifted]
    control[0][0] = I(-1)
    try:
        positive_pivots(control)
    except ArithmeticError:
        pass
    else:
        raise AssertionError('Indefinite matrix control accepted')
    return {
        'status':'certified complete actual corrected Schur shift',
        'aperture':'81/100','gram_input_sha256':gram_hash,'gram_input_git_blob_sha':gram_blob,
        'original_complete_gram_sha256':GRAM_SHA256,'compact_enclosure_used':compact,
        'source_sha256':source_hash,'native_sha256':native_hash,
        'complete_matrix_dimension':84,'all_mixed_terms_retained':True,
        'interval_grid_digits':80,'residual_outward_inclusions_checked':7056,
        'actual_gram_operator_error_upper':str(delta),
        'complement_inverse_factor':str(beta),'physical_complement_lower':str(comp),
        'shift_attempts':attempts,'failed_attempts_imply_negativity':False,
        'corrected_coercivity_lower_bound':str(tau),
        'previous_corrected_coercivity_lower_bound':str(F(1,10**29)),
        'corrected_margin_improvement_factor':str(tau/F(1,10**29)),
        'shifted_pivot_lower_bounds':[str(p.lo) for p in pivots],
        'lift_norm_squared_upper':str(lift2),'lift_operator_norm_upper':str(lift),
        'whole_domain_physical_coercivity_lower':str(mu),
        'logarithmic_coercivity_lower':str(kappa),
        'simple_physical_coercivity_lower':str(simple_mu),
        'simple_logarithmic_coercivity_lower':str(simple_kappa),
        'negative_control_rejected':True,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'whole_domain_positivity':True,'fixed_aperture_weak_kernel_zero':True,
        'global_endpoint_excluded':False,'f4_entry_closed':False,
        'full_transport_closed':False,'lean_formalized':False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    root = Path(__file__).resolve().parents[1]/'notes/data'
    parser.add_argument('--gram',default=root/'RPB108_PRIME5_GRAM84_081_COMPACT80_20261006.json')
    parser.add_argument('--native',default=root/'RPB108_PRIME5_MATRIX84_081_CERTIFICATE_20261005.json')
    parser.add_argument('--source',default=root/'RPB108_PRIME5_SOURCE84_081_CERTIFICATE_20261005.json')
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    result = certificate(args.gram,args.native,args.source)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('corrected_coercivity_lower_bound',
                                         'whole_domain_physical_coercivity_lower')}))
