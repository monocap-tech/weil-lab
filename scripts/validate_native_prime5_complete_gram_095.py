"""Complete fresh Gram custody, entry widths and actual source-error conversion."""
import gzip,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def read(path):
    raw=Path(path).read_bytes()
    return gzip.decompress(raw) if str(path).endswith('.gz') else raw

def certificate(primary,repeat,checkpoint,checkpoint_repeat):
    raw=read(primary);assert raw==read(repeat);g=json.loads(raw)
    cp=read(checkpoint);assert cp==read(checkpoint_repeat);state=json.loads(cp)
    assert state['completed_panels']==g['panel_count']==9
    root=Path(__file__).resolve().parents[1]
    names={'source':'notes/data/RPB108_PRIME5_SOURCE84_095_CERTIFICATE_20261007.json.gz',
        'native':'notes/data/RPB108_PRIME5_MATRIX84_095_COMPACT80_20261007.json'}
    data={k:json.loads(read(root/p)) for k,p in names.items()}
    hashes={k:hashlib.sha256(read(root/p)).hexdigest() for k,p in names.items()}
    source,native=data['source'],data['native']
    assert g['aperture']==source['aperture']==native['aperture']==state['bindings']['aperture']=='19/20'
    assert g['source_certificate_sha256']==state['bindings']['source']==hashes['source']
    assert g['native_certificate_sha256']==state['bindings']['native']==hashes['native']
    scripts={'constructor':'certify_native_prime5_gram84_095.py',
        'geometry':'certify_native_translation_panel_order.py','hankel':'certify_native_exact_hankel.py',
        'checkpoint_codec':'certify_native_gram_checkpoint.py'}
    for key,name in scripts.items():
        assert state['bindings'][key]==hashlib.sha256((root/'scripts'/name).read_bytes()).hexdigest()
    assert g['gram_constructor_sha256']==state['bindings']['constructor']
    assert g['complete_panel_checkpoint_sha256']==hashlib.sha256(cp).hexdigest()
    assert state['grid']==str(10**300) and g['interval_grid_digits']==300
    assert set(state['matrices'])=={'CS','smooth','cross'}
    count=0
    for matrix in state['matrices'].values():
        assert len(matrix)==84 and all(len(row)==84 for row in matrix)
        for row in matrix:
            for pair in row:
                assert len(pair)==2 and int(pair[0])<=int(pair[1]);count+=1
    assert count==21168
    assert g['physical_degrees']==g['projected_away_degrees']==list(range(84))
    assert g['native_source_pairing_count']==7056 and g['all_mixed_terms_retained']
    assert g['pairing_audit_includes_both_enclosure_widths'] and g['pairing_interval_gap_below_actual_source_allowance']
    r=g['residual_gram_surrogate'];assert len(r)==84 and all(len(row)==84 for row in r)
    width=F(0);trace=F(0)
    for i,row in enumerate(r):
        for j,pair in enumerate(row):
            lo,hi=map(F,pair);assert lo<=hi and pair==r[j][i]
            width=max(width,hi-lo)
            if i==j:trace+=hi
    assert width==F(g['maximum_entry_width'])<F(1,10**55)
    eta=F(source['source_map_error_upper']);error2=F(0)
    for n,row in enumerate(source['rows']):
        e,en=F(row['unnormalized_uniform_error']),F(row['normalized_uniform_error'])
        assert row['degree']==n and en*en>=(2*n+1)*e*e
        error2+=en*en
    assert 0<eta<F(5,10**36) and eta*eta>=error2
    M=F(g['surrogate_residual_map_norm_upper']);assert M>0 and M*M>=trace>0
    delta=eta*(2*M+eta)
    assert delta==F(g['actual_gram_operator_error_upper'])<F(1,10**30)
    assert g['full_source_gram_certified'] is True
    assert g['corrected_schur_sign_certified'] is g['whole_domain_positivity'] is False
    return dict(aperture='19/20',gram_sha256=hashlib.sha256(raw).hexdigest(),
        complete_checkpoint_sha256=hashlib.sha256(cp).hexdigest(),input_sha256=hashes,
        complete_nine_panel_gram_repeated_byte_for_byte=True,
        complete_nine_panel_checkpoint_repeated_byte_for_byte=True,
        cumulative_matrix_entries_checked=count,residual_entries_checked=7056,
        all_mixed_terms_retained=True,maximum_entry_width_display=float(width),
        trace_upper=str(trace),surrogate_map_norm_upper=str(M),source_map_error_upper=str(eta),
        actual_gram_operator_error_upper=str(delta),actual_gram_error_display=float(delta),
        complete_source_error_aggregation_verified=True,
        whole_domain_positivity=False,whole_domain_positivity_frontier='47/50',
        corrected_sign_pending=True,f4_entry_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
