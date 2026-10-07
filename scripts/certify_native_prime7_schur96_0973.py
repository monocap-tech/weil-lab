"""Fresh outward Schur sign using the pinned complete Gram and three-band complement."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots



EXPECTED_HASHES = {'gram': '0f83c73059a45bdf62552b11868ecde09a91bffb74985c6958e3296a2131374c', 'native': 'c773be2a97c524b533ced21c8805ec06746dcefb8c990269d09a74699f479b06', 'source': 'c6b3e9cd7eb9394fc0f28b6d18a31a6c56847099c0e301f4742eb23fad5e1d32'}


def certificate():
    old=I.grid;I.grid=10**160
    try:
        root=Path(__file__).resolve().parents[1]/'notes/data'
        names={'gram':'RPB108_PRIME7_GRAM96_0973_CERTIFICATE_20261007.json',
               'native':'RPB108_PRIME7_MATRIX96_0973_COMPACT80_20261007.json',
               'source':'RPB108_PRIME7_SOURCE96_0973_CERTIFICATE_20261007.json'}
        def read(name):
            p=root/name
            return p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
        raw={key:read(name) for key,name in names.items()}
        hashes={key:hashlib.sha256(value).hexdigest() for key,value in raw.items()}
        assert hashes==EXPECTED_HASHES
        data={key:json.loads(value) for key,value in raw.items()};g=data['gram'];native=data['native'];source=data['source']
        assert g['source_certificate_sha256']==hashes['source'] and g['native_certificate_sha256']==hashes['native']
        assert g['aperture']==native['aperture']==source['aperture']=='973/1000'
        assert g['physical_degrees']==g['projected_away_degrees']==list(range(96))
        assert g['native_source_pairing_count']==9216 and g['all_mixed_terms_retained']
        assert native['matrix_encoding']=='row-major lower triangle integer endpoints on grid 10^-80'
        triangle=native['lower_triangle_row_major'];assert len(triangle)==4656
        Q=[[None]*96 for _ in range(96)];index=0
        for i in range(96):
            for j in range(i+1):
                Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in triangle[index]));index+=1
        exactR=[[(F(lo),F(hi)) for lo,hi in row] for row in g['residual_gram_surrogate']]
        assert len(exactR)==96 and all(len(row)==96 for row in exactR)
        assert all(exactR[i][j]==exactR[j][i] and exactR[i][j][0]<=exactR[i][j][1] for i in range(96) for j in range(96))
        R=[[I(lo,hi) for lo,hi in row] for row in exactR]
        trace=sum((pair[1] for i,row in enumerate(exactR) for pair in [row[i]]),F(0))
        M=F(g['surrogate_residual_map_norm_upper']);assert M>0 and M*M>=trace
        eta=F(source['source_map_error_upper']);delta=eta*(2*M+eta)
        assert delta==F(g['actual_gram_operator_error_upper'])
        cp=root/'RPB108_PRIME7_96_PREFLIGHT_0973_CERTIFICATE_20261007.json'
        complement=json.loads(cp.read_bytes());c=F(complement['physical_lower']);beta=1/c
        assert c==F(423,500)<F(complement['physical_unrounded_lower'])
        assert c==F(423,500) and beta==1/F(423,500)
        G=[[Q[i][j]-beta*R[i][j] for j in range(96)] for i in range(96)]
        positive_pivots(G)
        tau=F(native["raw_physical_coercivity_lower_bound"])
        while True:
            lower=[row[:] for row in G]
            for i in range(96):lower[i][i]-=beta*delta+tau
            try:pivots=positive_pivots(lower);break
            except ArithmeticError:
                if tau<F(1,10**40):raise
                tau/=2
        lift2=beta*beta*(trace+delta);L=1
        while L*L<=lift2:L+=1
        mu=tau*c/(tau+c*(1+L*L));kappa=mu/(10*(mu+24))
        diagonal1=tau-mu*(1+L*L);diagonal2=c-mu
        determinant=diagonal1*diagonal2-(mu*L)**2
        assert diagonal1>=0 and diagonal2>=0 and determinant==mu*mu>0
        false_mu=2*mu
        false_det=(tau-false_mu*(1+L*L))*(c-false_mu)-(false_mu*L)**2
        assert false_det<0
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative control accepted')
        return dict(status='certified whole-domain actual positivity at 973/1000 with 96-vector matched weighted Schur complement',
            aperture='973/1000',interval_grid_digits=160,physical_degrees=list(range(96)),
            garding_constant=24,input_sha256=hashes,complement_certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),
            physical_complement_lower=str(c),complement_inverse_factor=str(beta),
            actual_gram_operator_error_upper=str(delta),all_mixed_terms_retained=True,
            source_pairing_count=9216,corrected_coercivity_lower_bound=str(tau),
            shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],lift_norm_squared_upper=str(lift2),
            lift_operator_norm_integer_upper=L,whole_domain_physical_coercivity_lower=str(mu),
            logarithmic_coercivity_lower=str(kappa),exact_conversion_determinant=str(determinant),
            oversized_conversion_control_rejected=True,negative_diagonal_control_rejected=True,
            original_complete_gram_preserved=True,whole_domain_positivity=True,
            fixed_aperture_weak_kernel_zero=True,fixed_aperture_unit_domination=True,
            global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    finally:I.grid=old


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
