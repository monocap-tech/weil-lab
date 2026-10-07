"""Finalize complete raw rows via outward 80-digit parity blocks."""
import gzip,hashlib,json
from pathlib import Path
from math import isqrt
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_matrix_checkpoint import load

def certificate(checkpoint):
    raw=Path(checkpoint).read_bytes();state=json.loads(gzip.decompress(raw))
    assert state['completed_rows']==84 and state['bindings']['aperture']=='97/100'
    assert state['bindings']['bernoulli_pairs']==260
    root=Path(__file__).resolve().parent
    for name,digest in state['bindings']['scripts'].items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
    old=I.grid;I.grid=10**400
    try:
        done,matrix=load(checkpoint,state['bindings']);assert done==84
        def precise_sqrt(x):
            n=isqrt((x*I.grid**2).__floor__())
            return I(F(n,I.grid),F(n+1,I.grid))
        Q=[[precise_sqrt(F((2*i+1)*(2*j+1)))*matrix[i][j]/F(97,50)
             for j in range(84)] for i in range(84)]
        width=max(x.hi-x.lo for row in Q for x in row);assert width<F(1,10**35)
        assert all(x.lo==x.hi==0 for i,row in enumerate(Q) for j,x in enumerate(row) if (i+j)%2)
        stored=[[[str(x.lo),str(x.hi)] for x in row] for row in Q]
        I.grid=10**80
        compact=[[I(x.lo,x.hi) for x in row] for row in Q]
        assert all(compact[i][j].lo<=Q[i][j].lo<=Q[i][j].hi<=compact[i][j].hi for i in range(84) for j in range(84))
        pivots=[];shifted_pivots=[];tau=F(1,10**18)
        for parity in (0,1):
            degrees=list(range(parity,84,2))
            pivots.extend(positive_pivots([[compact[i][j] for j in degrees] for i in degrees]))
        while True:
            try:
                shifted_pivots=[]
                for parity in (0,1):
                    degrees=list(range(parity,84,2))
                    block=[[compact[i][j]-(I(tau) if i==j else I(0)) for j in degrees] for i in degrees]
                    shifted_pivots.extend(positive_pivots(block))
                break
            except ArithmeticError:
                if tau<F(1,10**60):raise
                tau/=2
        broken=[[I(-1),I(0)],[I(0),I(1)]]
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative parity control accepted')
        return dict(status='certified full native finite restriction from complete raw rows via parity blocks',
            aperture='97/100',physical_degrees=list(range(84)),prime_terms=[2,3,4,5],
            physical_basis='sqrt((2n+1)/(2a)) P_n(x/a) on [-a,a]',matrix_intervals=stored,
            pivot_lower_bounds=[str(x.lo) for x in pivots],
            shifted_pivot_lower_bounds=[str(x.lo) for x in shifted_pivots],
            pivot_order='even degrees, then odd degrees; exact parity decomposition',
            raw_physical_coercivity_lower_bound=str(tau),maximum_entry_width=str(width),
            exact_reflection_parity=True,negative_control_rejected=True,
            exponential_order=260,bernoulli_pairs=260,gamma_order=20,
            interval_grid_digits=400,finite_sign_grid_digits=80,log_series_terms=220,
            complete_raw_checkpoint_sha256=hashlib.sha256(raw).hexdigest(),
            finalization_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            raw_constructor_bindings=state['bindings'],full_source_gram_certified=False,
            corrected_schur_sign_certified=False,whole_domain_positivity=False,
            f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
