"""Exact eight-moment reconstruction and canonical projector-gap budget."""
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys

def run(path):
    raw=Path(path).read_bytes(); data=json.loads(raw)
    assert data['actual_low_native_Gram_certified']
    assert data['native_features_certified']==list(range(8))
    V=[[F(x) for x in row] for row in data['native_trial_coefficients']]
    C=[[F(x) for x in row] for row in data['chebyshev_to_legendre']]
    P=[[F(x) for x in row] for row in data['physical_native_Gram']]
    assert len(V)==32 and all(len(row)==8 for row in V)
    mass=[F(11,5*(2*i+1)) for i in range(32)]
    D=[[mass[i]*(i==j) for j in range(8)] for i in range(8)]
    assert mm(mm(tr(C),D),C)==P
    # J = R_native^* V_native exactly: ell_i(v_j) is a physical integral,
    # even though R_native itself is not a physical polynomial.
    J=mm(tr(C),[[mass[i]*V[i][j] for j in range(8)] for i in range(8)])
    sym=[[ (J[i][j]+J[j][i])/2 for j in range(8)] for i in range(8)]
    assert psd([[sym[i][j]-F(1,2)*P[i][j] for j in range(8)] for i in range(8)])
    B=inverse(J); identity=[[F(i==j) for j in range(8)] for i in range(8)]
    assert mm(J,B)==mm(B,J)==identity
    W=mm(V,B)
    moments=mm(tr(C),[[mass[i]*W[i][j] for j in range(8)] for i in range(8)])
    assert moments==identity
    assert mm(W,J)==V
    assert all(W[i][j]==0 for i in range(32) for j in range(8) if (i-j)%2)
    # O h = W ell(h), where W's rows are Legendre polynomial coefficients.
    # The exact moment identity proves O^2=O, ker O=ker ell, and ell(I-O)=0.
    q2=F(data['canonical_trial_error_actual_native_metric_squared_upper'])
    assert 0<q2<1
    tan2=q2/(1-q2); norm2=F(1)/(1-q2)
    gap=F(523,10000); norm=F(100137,100000)
    assert tan2<gap*gap and norm2<norm*norm
    # Concrete nonorthogonal control: zero oblique residual is NOT zero
    # canonical orthogonal residual. This prevents unsafe source attachment.
    t=F(1,20); O=[[F(1),F(0)],[t,F(0)]]
    orth=[[F(1),F(0)],[F(0),F(0)]]
    source=[[F(1)],[t]]
    assert mm(O,O)==O and O!=tr(O)
    ob=[[source[i][0]-mm(O,source)[i][0]] for i in range(2)]
    exact=[[source[i][0]-mm(orth,source)[i][0]] for i in range(2)]
    assert mm(tr(ob),ob)==[[F(0)]] and mm(tr(exact),exact)==[[t*t]]
    # Young's inequality at s=1 yields a rigorous whole-source transfer.
    # No source columns or source Gram are supplied by this certificate.
    return dict(milestone='RC41',status='PASS',
        source_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        native_features_certified=list(range(8)),trial_dimension=32,
        exact_native_moment_trial_pairing=[[str(x) for x in row] for row in J],
        exact_moment_pairing_inverse=[[str(x) for x in row] for row in B],
        reconstruction_legendre_coefficients=[[str(x) for x in row] for row in W],
        exact_reconstruction_moment_matrix=[[str(x) for x in row] for row in moments],
        native_to_trial_subspace_gap_squared_upper=str(q2),
        oblique_to_canonical_projector_gap_squared_upper=str(tan2),
        oblique_to_canonical_projector_gap_upper=str(gap),
        reconstruction_canonical_operator_norm_squared_upper=str(norm2),
        reconstruction_canonical_operator_norm_upper=str(norm),
        source_transfer_oblique_Gram_multiplier='2',
        source_transfer_full_source_Gram_multiplier=str(2*tan2),
        unsafe_zero_oblique_source_control_actual_residual_squared=str(t*t),
        exact_native_moment_reconstruction_certified=True,
        exact_canonical_projector_evaluated=False,
        complete_native_projector_certified=False,
        native_remainder_sources_certified=False,
        original_Weil_head_floor_certified=False,aperture_extended=False)

def replay(certificate_path,source_path):
    """Replay emitted coefficients using direct power-basis physical integrals."""
    from validate_rpb108_rc29_atom_reduction import legendre
    raw=Path(source_path).read_bytes(); source=json.loads(raw)
    cert=json.loads(Path(certificate_path).read_text())
    assert cert['source_certificate_sha256']==hashlib.sha256(raw).hexdigest()
    W=[[F(x) for x in row] for row in cert['reconstruction_legendre_coefficients']]
    V=[[F(x) for x in row] for row in source['native_trial_coefficients']]
    J=[[F(x) for x in row] for row in cert['exact_native_moment_trial_pairing']]
    B=[[F(x) for x in row] for row in cert['exact_moment_pairing_inverse']]
    cheb=[[F(1)],[F(0),F(1)]]
    for n in range(1,7):
        row=[F(0)]*(n+2)
        for k,x in enumerate(cheb[n]): row[k+1]+=2*x
        for k,x in enumerate(cheb[n-1]): row[k]-=x
        cheb.append(row)
    # B dx substitution and exact integral of every power on [-1,1].
    K=[[sum((F(11,10)*a*b*F(2,k+l+1)
             for k,a in enumerate(cheb[i]) for l,b in enumerate(legendre(j))
             if (k+l)%2==0),F(0)) for j in range(32)] for i in range(8)]
    identity=[[F(i==j) for j in range(8)] for i in range(8)]
    assert mm(K,W)==identity and mm(K,V)==J and mm(W,J)==V
    assert mm(J,B)==mm(B,J)==identity
    q2=F(source['canonical_trial_error_actual_native_metric_squared_upper'])
    assert F(cert['native_to_trial_subspace_gap_squared_upper'])==q2
    tan2=q2/(1-q2)
    assert F(cert['oblique_to_canonical_projector_gap_squared_upper'])==tan2
    assert F(cert['reconstruction_canonical_operator_norm_squared_upper'])==1+tan2
    assert tan2<F(cert['oblique_to_canonical_projector_gap_upper'])**2
    assert 1+tan2<F(cert['reconstruction_canonical_operator_norm_upper'])**2
    assert F(cert['source_transfer_full_source_Gram_multiplier'])==2*tan2
    print('PASS: direct power-basis moment replay, inverse products, reconstruction, and budgets')

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        replay(sys.argv[2],sys.argv[3] if len(sys.argv)>3 else root/'rpb108_rc39_native_low_chebyshev_gram.json')
    else:
        path=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc39_native_low_chebyshev_gram.json'
        print(json.dumps(run(path),indent=2))
