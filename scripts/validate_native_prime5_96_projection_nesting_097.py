"""Independent 84-to-96 residual projection identity on unchanged source rows."""
import gzip,hashlib,json
from math import lcm
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_endpoint_log_gram import shifted_legendre
from certify_native_exact_hankel import moment_apply,bilinear_bounds
from certify_native_prime3_matrix36 import precise_sqrt

def read(path):
    raw=Path(path).read_bytes()
    return gzip.decompress(raw) if str(path).endswith('.gz') else raw

def certificate(gram,checkpoint):
    root=Path(__file__).resolve().parents[1]/'notes/data'
    oldraw=read(root/'RPB108_PRIME5_GRAM84_097_CERTIFICATE_20261007.json.gz')
    old=json.loads(oldraw);newraw=read(gram);new=json.loads(newraw)
    checkpoint_raw=read(checkpoint);state=json.loads(checkpoint_raw);assert state['completed_panels']==9
    assert hashlib.sha256(checkpoint_raw).hexdigest()==new['complete_panel_checkpoint_sha256']
    assert state['bindings']['source']==new['source_certificate_sha256']
    assert state['bindings']['native']==new['native_certificate_sha256']
    oldsource=json.loads(read(root/'RPB108_PRIME5_SOURCE84_097_CERTIFICATE_20261007.json.gz'))
    newsource=json.loads(read(root/'RPB108_PRIME5_SOURCE96_097_CERTIFICATE_20261007.json.gz'))
    assert oldsource['rows']==newsource['rows'][:84]
    assert old['physical_degrees']==list(range(84)) and new['physical_degrees']==list(range(96))
    assert old['projected_away_degrees']==list(range(84)) and new['projected_away_degrees']==list(range(96))
    assert old['aperture']==new['aperture']=='97/100'
    saved=I.grid;I.grid=10**300
    try:
        polys=[[int(v) for v in row] for row in shifted_legendre(95)]
        harmonic=F(0);moments=[]
        for k in range(191):
            harmonic+=F(1,k+1)
            moments.append((F(1,(k+1)**2)+harmonic/F(k+1))/2)
        den=lcm(*(v.denominator for v in moments))
        fixed=[(int(v*den),int(v*den)) for v in moments]
        applied=[moment_apply(p,fixed,96) for p in polys[:84]]
        projection=[]
        for n in range(84,96):
            row=[]
            for i in range(84):
                exact=F(bilinear_bounds(polys[n],applied[i])[0],2*den)
                cs=I(*(F(int(x),I.grid) for x in state['matrices']['CS'][n][i]))
                row.append(cs+exact)
            projection.append(row)
        checks=0
        for i in range(84):
            for j in range(i,84):
                added=precise_sqrt(F((2*i+1)*(2*j+1)))*sum(((2*n+1)*projection[n-84][i]*projection[n-84][j] for n in range(84,96)),I(0))
                oldinterval=I(*map(F,old['residual_gram_surrogate'][i][j]))
                newinterval=I(*map(F,new['residual_gram_surrogate'][i][j]))
                difference=oldinterval-newinterval
                assert max(difference.lo,added.lo)<=min(difference.hi,added.hi)
                checks+=1 if i==j else 2
        assert checks==7056
        return dict(aperture='97/100',old_gram_sha256=hashlib.sha256(oldraw).hexdigest(),new_gram_sha256=hashlib.sha256(newraw).hexdigest(),unchanged_original_source_rows=84,added_projection_degrees=list(range(84,96)),residual_projection_identity_entries_verified=checks,identity='old residual Gram equals new restricted residual Gram plus the 12-coordinate projection Gram',surrogate_identity_only=True,whole_domain_positivity=False,f4_closed=False)
    finally:I.grid=saved

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
