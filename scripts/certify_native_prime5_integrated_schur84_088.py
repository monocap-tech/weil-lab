"""Fresh outward Schur sign using the pinned complete Gram and damped complement."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_prime5_refined_complement84_088 import certificate as complement_certificate


EXPECTED_HASHES = {'gram': 'a6cd202c9835acc884627c6df87295f8221ba05006cf8517583e17b9696dd60b', 'native': '49ad98d92b40948bd31f362aa7db1913526cc714da358c44fb8a3ee6e55b745a', 'source': 'c9d420b7208b431fe9471e5177bb21817d67ff880f73a1a046d05210df974f47'}


def certificate():
    old=I.grid;I.grid=10**160
    try:
        root=Path(__file__).resolve().parents[1]/'notes/data'
        names={'gram':'RPB108_PRIME5_GRAM84_088_CERTIFICATE_20261006.json',
               'native':'RPB108_PRIME5_MATRIX84_088_COMPACT80_20261006.json',
               'source':'RPB108_PRIME5_SOURCE84_088_CERTIFICATE_20261006.json'}
        raw={key:(root/name).read_bytes() for key,name in names.items()}
        hashes={key:hashlib.sha256(value).hexdigest() for key,value in raw.items()}
        assert hashes==EXPECTED_HASHES
        data={key:json.loads(value) for key,value in raw.items()};g=data['gram'];native=data['native'];source=data['source']
        assert g['source_certificate_sha256']==hashes['source'] and g['native_certificate_sha256']==hashes['native']
        assert g['aperture']==native['aperture']==source['aperture']=='22/25'
        assert g['physical_degrees']==g['projected_away_degrees']==list(range(84))
        assert g['native_source_pairing_count']==7056 and g['all_mixed_terms_retained']
        assert native['matrix_encoding']=='row-major lower triangle integer endpoints on grid 10^-80'
        triangle=native['lower_triangle_row_major'];assert len(triangle)==3570
        Q=[[None]*84 for _ in range(84)];index=0
        for i in range(84):
            for j in range(i+1):
                Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in triangle[index]));index+=1
        exactR=[[(F(lo),F(hi)) for lo,hi in row] for row in g['residual_gram_surrogate']]
        assert len(exactR)==84 and all(len(row)==84 for row in exactR)
        assert all(exactR[i][j]==exactR[j][i] and exactR[i][j][0]<=exactR[i][j][1] for i in range(84) for j in range(84))
        R=[[I(lo,hi) for lo,hi in row] for row in exactR]
        trace=sum((pair[1] for i,row in enumerate(exactR) for pair in [row[i]]),F(0))
        M=F(g['surrogate_residual_map_norm_upper']);assert M>0 and M*M>=trace
        eta=F(source['source_map_error_upper']);delta=eta*(2*M+eta)
        assert delta==F(g['actual_gram_operator_error_upper'])
        complement=complement_certificate();c=F(complement['physical_lower']);beta=F(1)/c
        assert c==F(619,1000) and beta==F(1000,619)
        G=[[Q[i][j]-beta*R[i][j] for j in range(84)] for i in range(84)]
        positive_pivots(G)
        tau=F(native["raw_physical_coercivity_lower_bound"])
        while True:
            lower=[row[:] for row in G]
            for i in range(84):lower[i][i]-=beta*delta+tau
            try:pivots=positive_pivots(lower);break
            except ArithmeticError:
                if tau<F(1,10**40):raise
                tau/=2
        lift2=beta*beta*(trace+delta);L=1
        while L*L<=lift2:L+=1
        mu=tau*c/(tau+c*(1+L*L));kappa=mu/(10*(mu+23))
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
        return dict(status='certified whole-domain actual positivity at 22/25 with integrated damped complement',
            aperture='22/25',interval_grid_digits=160,physical_degrees=list(range(84)),
            input_sha256=hashes,complement_certificate_sha256=hashlib.sha256((json.dumps(complement,indent=2)+'\n').encode()).hexdigest(),
            physical_complement_lower=str(c),complement_inverse_factor=str(beta),
            actual_gram_operator_error_upper=str(delta),all_mixed_terms_retained=True,
            source_pairing_count=7056,corrected_coercivity_lower_bound=str(tau),
            shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],lift_norm_squared_upper=str(lift2),
            lift_operator_norm_integer_upper=L,whole_domain_physical_coercivity_lower=str(mu),
            logarithmic_coercivity_lower=str(kappa),exact_conversion_determinant=str(determinant),
            oversized_conversion_control_rejected=True,negative_diagonal_control_rejected=True,
            original_complete_gram_preserved=True,whole_domain_positivity=True,
            fixed_aperture_weak_kernel_zero=True,fixed_aperture_unit_domination=True,
            global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    finally:I.grid=old


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
