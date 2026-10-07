"""Saved-column custody and independent floor-cell audit of final source coefficients."""
import gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F

def certificate(primary,repeat,columns):
    raw=Path(primary).read_bytes();repeated=Path(repeat).read_bytes();c=json.loads(raw)
    other=json.loads(repeated);assert c==other
    canonical=json.dumps(c,sort_keys=True,separators=(',',':')).encode()
    assert canonical==json.dumps(other,sort_keys=True,separators=(',',':')).encode()
    folder=Path(columns);bindings=json.loads((folder/'bindings.json').read_bytes())
    assert bindings==c['constructor_sha256']
    for name,digest in bindings.items():assert hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest()==digest
    unit=F(1,10**40);checked=0;hashes=[]
    for n,row in enumerate(c['rows']):
        saved=(folder/f'row{n:03}.json.gz').read_bytes();r=json.loads(gzip.decompress(saved))
        hashes.append(hashlib.sha256(saved).hexdigest())
        assert r['degree']==row['degree']==n and len(r['panels'])==len(row['panels'])==11
        for old,new in zip(r['panels'],row['panels']):
            q=[F(x,10**40) for x in new['low_degree_numerators']+row['common_high_degree_numerators']]
            p=list(map(F,old['coefficients']));assert len(p)==len(q)
            differences=[x-y for x,y in zip(p,q)]
            assert all(0<=x<unit for x in differences)
            assert F(new['coefficient_radius'])==F(old['coefficient_radius'])+sum(differences,F(0))
            assert not 0<=p[0]-(q[0]+1)<unit  # displaced coefficient fails its floor cell
            checked+=len(q)
        previous_radius=max(F(p['coefficient_radius']) for p in r['panels'])
        final_radius=max(F(p['coefficient_radius']) for p in row['panels'])
        assert F(row['unnormalized_uniform_error'])==F(r['unnormalized_uniform_error'])-previous_radius+final_radius
    assert len(hashes)==112 and checked==461384
    return dict(aperture='399/400',source_sha256=hashlib.sha256(raw).hexdigest(),
        source_repeat_scope='assembly and quantization from the same complete saved unquantized columns',
        exact_decoded_source_data_repeated=True,canonical_sorted_encoding_repeated_byte_for_byte=True,
        canonical_sorted_sha256=hashlib.sha256(canonical).hexdigest(),
        original_serialized_sha256=hashlib.sha256(raw).hexdigest(),repeat_serialized_sha256=hashlib.sha256(repeated).hexdigest(),
        saved_column_bindings_verified=True,
        column_record_sha256=hashes,independent_floor_cells_checked=checked,
        all_quantization_radius_increments_verified=True,displaced_floor_controls_rejected=1232,
        full_residual_gram_certified=False,whole_domain_positivity=False,
        whole_domain_frontier='199/200',f4_entry_closed=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
