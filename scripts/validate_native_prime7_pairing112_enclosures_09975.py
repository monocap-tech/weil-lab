"""Independent native/source enclosure audit from complete saved contractions."""
import hashlib,json,sys
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_endpoint_log_gram import shifted_legendre
from certify_native_prime3_matrix36 import precise_sqrt
from certify_native_exact_hankel import moment_apply,bilinear_bounds

def certificate(checkpoint):
    root=Path(__file__).resolve().parents[1]/'notes/data'
    sp=root/'RPB108_PRIME7_SOURCE112_09975_CERTIFICATE_20261007.json'
    np=root/'RPB108_PRIME7_MATRIX112_09975_COMPACT80_20261007.json'
    source_raw=sp.read_bytes() if sp.exists() else __import__('gzip').decompress(sp.with_suffix('.json.gz').read_bytes())
    source=json.loads(source_raw);native=json.loads(np.read_bytes())
    raw=Path(checkpoint).read_bytes()
    if raw[:2]==b'\x1f\x8b':raw=__import__('gzip').decompress(raw)
    state=json.loads(raw)
    assert state['completed_panels']==11 and state['bindings']['aperture']=='399/400'
    assert state['bindings']['source']==hashlib.sha256(source_raw).hexdigest()
    assert state['bindings']['native']==hashlib.sha256(np.read_bytes()).hexdigest()
    assert source['aperture']==native['aperture']=='399/400'
    old=I.grid;I.grid=10**300
    try:
        assert state['grid']==str(I.grid)
        p=shifted_legendre(111)
        harmonic=F(0);moments=[]
        for k in range(223):
            harmonic+=F(1,k+1)
            moments.append((F(1,(k+1)**2)+harmonic/F(k+1))/2)
        # Independent exact integer Hankel action for rational logarithmic moments.
        from math import lcm
        denominator=lcm(*(x.denominator for x in moments))
        fixed=[(int(x*denominator),int(x*denominator)) for x in moments]
        polynomials=[[int(x) for x in row] for row in p]
        applied=[moment_apply(row,fixed,112) for row in polynomials]
        cl=[[F(bilinear_bounds(row,applied[i])[0],2*denominator)
             for i in range(112)] for row in polynomials]
        cs=[[I(*(F(int(x),I.grid) for x in pair)) for pair in row]
            for row in state['matrices']['CS']]
        triangle=native['lower_triangle_row_major'];q=[[None]*112 for _ in range(112)];index=0
        for i in range(112):
            for j in range(i+1):
                q[i][j]=q[j][i]=I(*(F(int(x),10**80) for x in triangle[index]));index+=1
        old_failures=[];max_gap=F(0);max_excess=F(0);checks=0
        for i in range(112):
            eta=F(source['rows'][i]['normalized_uniform_error'])
            for j in range(112):
                pair=precise_sqrt(F((2*i+1)*(2*j+1)))*(cl[j][i]+cs[j][i])
                native_entry=q[i][j];difference=pair-native_entry
                error=max(abs(difference.lo),abs(difference.hi))
                gap=max(F(0),pair.lo-native_entry.hi,native_entry.lo-pair.hi)
                budget=eta+(pair.hi-pair.lo)+(native_entry.hi-native_entry.lo)
                assert gap<eta and error<budget
                if error>=eta:old_failures.append([i,j])
                max_gap=max(max_gap,gap);max_excess=max(max_excess,error-eta)
                displaced=pair+I(2*budget+1)
                broken=displaced-native_entry
                assert max(abs(broken.lo),abs(broken.hi))>budget
                checks+=1
        assert checks==12544
        return dict(aperture='399/400',checkpoint_sha256=hashlib.sha256(raw).hexdigest(),
            source_sha256=hashlib.sha256(source_raw).hexdigest(),native_sha256=hashlib.sha256(np.read_bytes()).hexdigest(),
            independently_recomputed_rational_endpoint_projections=True,pairing_checks=checks,
            enclosure_widths_accounted_for=True,strict_interval_gap_below_source_allowance=True,
            original_source_only_gate_failures=old_failures,maximum_interval_gap=str(max_gap),
            maximum_source_only_allowance_excess=str(max_excess),displaced_pair_controls_rejected=checks,
            actual_source_map_error_unchanged=True,complete_residual_gram_accepted=False,
            corrected_sign_accepted=False,whole_domain_positivity=False,f4_entry_closed=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(sys.argv[1]),indent=2))
