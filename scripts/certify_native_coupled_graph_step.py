"""CC2: exact input audit and graph-step budgets; analytic implications in note."""
from pathlib import Path
from fractions import Fraction as F
import base64,gzip,hashlib,json

def run(root=None):
    root=Path(root) if root else Path(__file__).resolve().parents[1]
    data=root/'notes/data'
    c=json.loads((data/'RPB108_PRIME7_SCHUR112_100_CERTIFICATE_20261007.json').read_text())
    parts=sorted(data.glob('RPB108_PRIME7_MATRIX112_100_COMPACT80_20261007.json.transport.b64.part*'))
    assert len(parts)==5
    raw=gzip.decompress(base64.b64decode(b''.join(p.read_bytes().strip() for p in parts),validate=True))
    digest=hashlib.sha256(raw).hexdigest()
    assert digest==c['input_sha256']['native']
    native=json.loads(raw)
    rows=[[F(0)]*112 for _ in range(112)];index=0
    for i in range(112):
        for j in range(i+1):
            lo,hi=[F(int(x),10**80) for x in native['lower_triangle_row_major'][index]]
            assert lo<=hi
            index+=1
            rows[i][j]=rows[j][i]=max(abs(lo),abs(hi))
    assert index==6328
    finite_norm=max(sum(row) for row in rows)
    assert finite_norm<11
    tau=F(c['corrected_coercivity_lower_bound'])
    cp=F(c['physical_complement_lower'])
    lift=c['lift_operator_norm_integer_upper']
    assert tau==F(1,320*10**27) and cp==F(93,100) and lift==8
    # Saved exact lift-squared bound also gives ||B||^2 < 49 because
    # it is c_p^(-2) times the actual residual Gram norm upper.
    actual_residual_squared=F(c['lift_norm_squared_upper'])*cp*cp
    assert actual_residual_squared<49
    assert 11**2+7**2<14**2
    assert 1+lift**2<9**2
    # Existing C0<10, active-prime <6, pole <12, exterior arch <4.
    mass=F(9);forcing=F(14)
    moment=(10+4+6+12+forcing)*mass
    assert moment==414
    # Representation epsilon=2^-N, R=2^(N/2). No enormous integer built.
    N=10**21
    assert N%2==0 and N>=16
    assert 2**8==16**2 and 2*16**2>18**2
    # Analytic induction proves 2^-N and 2^(-N/2)<=1/N^2.
    # The full PS1 norm modulus protects only the O(1) complement.
    omega=F(48,N)+F(121,N*N)
    c0=cp/(10*(cp+24))
    cc=c0-omega
    assert c0==F(93,24930) and cc>c0/2
    # Diagonal graph estimate uses the SQUARED logarithmic moment tail;
    # mixed coupling uses its square root. Keep their constants separate.
    alpha=(25*mass**2+6*16*mass**2+6*32*moment**2)/N**2
    eta=6*8*moment/N+(25*mass+6*16*mass)/N**2
    t=tau-alpha-eta*eta/cc
    assert alpha+eta*eta/cc<tau/2 and t>tau/2
    ell=F(lift)+eta/cc
    assert ell<F(81,10)
    mu=t*cc/(t+cc*(1+ell*ell))
    published_mu=F(2,10**32)
    assert mu>published_mu
    # Uniform pulled Garding: q_b >= E_H/10 -26 mass.
    canonical=mu/(10*(mu+26))
    published_canonical=F(7,10**35)
    assert canonical>published_canonical
    # The PS2 constant-finite-block crossing remains a real loss on W.
    zstar=tau*cp*cp/(49+tau*cp)
    T=F(7)/cp
    for scale in [F(1,2),F(1),F(3,2)]:
        z=scale*zstar
        completed=tau-z*T*T-(z*T)**2/(cp-z)
        assert completed==tau-49*z/(cp*(cp-z))
        assert (completed>0)==(scale<1)
    # Bad tail or erased mass controls fail: the rate is not an H1 bound.
    failed_N=10**19
    bad_eta=6*8*moment/failed_N+(25*mass+6*16*mass)/failed_N**2
    assert bad_eta*bad_eta/c0>tau
    assert F(3,2)*2!=0
    # Ratio of represented exponents measures improvement; neither width
    # is usable. No floating value for epsilon is ever substituted.
    assert 10**36//N==10**15
    def logs(n):
        z=F(n-1,n+1)
        lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(100)),F(0))
        hi=lo+2*z**201/(F(201)*(1-z*z))
        return lo,hi
    assert logs(8)[0]>F(202,100)>2+F(2,N*N)
    assert logs(3)[0]>F(21,20)
    assert 4*F(21,20)*3<F(13)
    assert 6+6+4*F(21,20)*3+F(1,10)*F(1,20)<26
    return dict(status='analytic coupled interval with exact finite budgets; impractical radius',
      starting_head='bbb2175f460bcc314a80468d1c5dfa6dacb6d9a0',
      native_sha256=digest,native_interval_entries_audited=6328,
      native_operator_norm_upper=str(finite_norm),native_operator_norm_integer_upper=11,
      actual_residual_squared_upper=str(actual_residual_squared),
      full_retained_source_operator_norm_upper=14,completed_graph_physical_norm_upper=9,
      completed_graph_X1_norm_upper=414,canonical_anchor_complement=str(c0),
      aperture_interval='1 <= b <= 1 + 2^(-10^21)',radius_exponent=N,
      full_norm_budget=str(omega),complement_lower=str(cc),
      completed_graph_diagonal_budget=str(alpha),completed_graph_mixed_budget=str(eta),
      completed_graph_Schur_lower=str(t),completed_graph_lift_upper=str(ell),
      physical_lower=str(mu),published_physical_lower=str(published_mu),
      canonical_lower=str(canonical),published_canonical_lower=str(published_canonical),
      native_logarithmic_lower=str(published_canonical),
      original_source_gain_squared_upper='1 - (7e-35)/C_(21/20)^2',
      source_upper_constant_numerically_evaluated=False,
      graph_equation_is_forced=True,homogeneous_eigenvector_premise=False,
      fresh_source_gram_constructed=False,gram_archive_replayed=False,
      native_compact_archive_replayed=True,prime8_crossed=False,
      practically_useful_radius=False,nonstalling_proved=False,
      analytic_proof_written=True,analytic_proof_mechanically_certified=False,
      lean_certified=False,outcome='B strengthened: actual graph budgets, impractical interval',
      all_finite_checks_passed=True)

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
