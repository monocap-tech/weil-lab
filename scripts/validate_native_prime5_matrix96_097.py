"""Independent exact persisted raw-to-physical enclosure and compact custody audit."""
import gzip,hashlib,json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

def certificate(primary,repeat,checkpoint,compact,compact_repeat):
    raw=Path(primary).read_bytes();assert raw==Path(repeat).read_bytes()
    r=json.loads(raw);s=json.loads(gzip.decompress(Path(checkpoint).read_bytes()))
    assert r['aperture']==s['bindings']['aperture']=='97/100'
    assert r['complete_raw_checkpoint_sha256']==hashlib.sha256(Path(checkpoint).read_bytes()).hexdigest()
    assert r['finalization_script_sha256']==hashlib.sha256((Path(__file__).parent/'finalize_native_prime5_matrix96_097.py').read_bytes()).hexdigest()
    assert r['raw_constructor_bindings']==s['bindings']
    assert r['finite_sign_grid_digits']==160 and r['pivot_order']=='even degrees, then odd degrees; exact parity decomposition'
    assert s['completed_rows']==96 and s['grid_digits']==400
    assert r['bernoulli_pairs']==s['bindings']['bernoulli_pairs']==300
    root=Path(__file__).resolve().parent
    for name,digest in s['bindings']['scripts'].items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
    assert r['physical_degrees']==list(range(96)) and r['prime_terms']==[2,3,4,5]
    assert all(F(x)>0 for x in r['pivot_lower_bounds']+r['shifted_pivot_lower_bounds'])
    g=10**400
    def quantize(lo,hi):return F((lo*g).__floor__(),g),F((hi*g).__ceil__(),g)
    def mul(x,y):
        values=[a*b for a in x for b in y];return quantize(min(values),max(values))
    inverse=quantize(F(50,97),F(50,97));checked=0;k=0
    for i in range(96):
        for j in range(i+1):
            x=[F(int(v),g) for v in s['lower_triangle'][k]];k+=1
            n=isqrt((2*i+1)*(2*j+1)*g*g)
            q=mul(mul((F(n,g),F(n+1,g)),x),inverse)
            stored=tuple(map(F,r['matrix_intervals'][i][j]));assert q==stored
            assert r['matrix_intervals'][i][j]==r['matrix_intervals'][j][i]
            if (i+j)%2:assert stored==(F(0),F(0))
            checked+=1 if i==j else 2
    assert checked==9216
    width=max(F(p[1])-F(p[0]) for row in r['matrix_intervals'] for p in row)
    assert width==F(r['maximum_entry_width']) and width<F(1,10**35)
    cr=Path(compact).read_bytes();assert cr==Path(compact_repeat).read_bytes();c=json.loads(cr)
    assert c['original_matrix_sha256']==hashlib.sha256(raw).hexdigest()
    assert c['base_constructor_sha256']==hashlib.sha256((root/'certify_native_legendre96_097.py').read_bytes()).hexdigest()
    assert c['construction_script_sha256']==hashlib.sha256((root/'certify_native_prime5_matrix96_097.py').read_bytes()).hexdigest()
    assert c['compact_checker_sha256']==hashlib.sha256((root/'compact_native_prime5_matrix96_097.py').read_bytes()).hexdigest()
    assert c['bernoulli_pairs']==300 and c['outward_inclusions_checked']==9216
    k=0
    for i in range(96):
        for j in range(i+1):
            lo,hi=[F(int(v),10**80) for v in c['lower_triangle_row_major'][k]];k+=1
            a,b=map(F,r['matrix_intervals'][i][j]);assert lo<=a<=b<=hi
    assert len(c['parity_block_pivots'])==2
    for block in c['parity_block_pivots']:assert len(block['degrees'])==48 and all(F(v)>0 for v in block['shifted_pivot_lower_bounds'])
    assert c['raw_physical_coercivity_lower_bound']==r['raw_physical_coercivity_lower_bound']
    assert c['negative_control_rejected'] and r['negative_control_rejected']
    assert c['whole_domain_positivity'] is False and r['whole_domain_positivity'] is False
    previous=json.loads((root.parent/'notes/data/RPB108_PRIME5_MATRIX84_097_COMPACT80_20261007.json').read_bytes())
    assert previous['aperture']=='97/100' and previous['physical_degrees']==list(range(84))
    overlap=0;index=0
    for i in range(84):
        for j in range(i+1):
            a,b=[F(int(v),10**80) for v in previous['lower_triangle_row_major'][index]];index+=1
            lo,hi=map(F,r['matrix_intervals'][i][j])
            assert max(lo,a)<=min(hi,b)
            overlap+=1 if i==j else 2
    assert overlap==7056
    return dict(aperture='97/100',native_reproduced_byte_for_byte=True,compact_reproduced_byte_for_byte=True,
        old_84_block_overlap_entries_verified=overlap,native_sha256=hashlib.sha256(raw).hexdigest(),compact_sha256=hashlib.sha256(cr).hexdigest(),
        raw_checkpoint_constructor_bindings_verified=True,independent_raw_to_physical_entries_checked=checked,
        compact_outward_inclusions_checked=9216,shifted_parity_block_pivots=96,
        maximum_native_width_display=float(width),finite_physical_margin=r['raw_physical_coercivity_lower_bound'],
        finite_restriction_only=True,complete_residual_gram_pending=True,whole_domain_positivity=False,
        f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
