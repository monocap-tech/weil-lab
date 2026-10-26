"""Full original 484D trial physical preconditioner and energy enclosure.

No original Astar matrix entries, energy projection, forcing, or response are
computed. All analytic transfers remain conditional on the inherited domain.
"""
import argparse, hashlib, json, time
from fractions import Fraction as F
from pathlib import Path
from flint import arb, arb_mat, ctx
import verify_rpb108_si29_full_J_L2_normalization as m

SHA = 'c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
def dy(x): return arb((int(x[0]), int(x[1])))
def ball(x): return arb(dy(x[0]), dy(x[1]))
def rat(x):
    n,e = int(x[0]),int(x[1])
    return F(n*2**max(e,0), 2**max(-e,0))
def upper(x): return rat(m.dyadic(x.upper()))
def derivative(terms, kernel):
    out=[]
    for p,t,f,c in terms:
        if p: out.append((p-1,t,f,c*p))
        out.append((p,'c' if t=='s' else 's',f,c*kernel.w(f)*(1 if t=='s' else -1)))
    return out
def endpoint(terms,kernel):
    from flint import acb
    z=acb(0)
    for p,t,f,c in terms:
        w=kernel.w(f)*kernel.b
        z+=c*kernel.b**p*(w.sin() if t=='s' else w.cos())
    assert z.imag.contains(0)
    return z.real

class Kernel(m.Integrals):
    def _get(self,p,kind,f):
        if p>=-4 or f==(0,0):return super()._get(p,kind,f)
        assert p in (-5,-6)
        w=self.w(f); b=self.b; n=-p; t=w*b
        reg=t.sin() if kind=='s' else t.cos()
        for k in range(1 if kind=='s' else 0,n-1,2):
            reg-=(-1)**(k//2)*t**k/m.factorial(k)
        return -reg/((n-1)*b**(n-1))+(w if kind=='s' else -w)/(n-1)*self._get(p+1,'c' if kind=='s' else 's',f)

def candidate(H):
    # Rounding EACH candidate operation prevents interval Cholesky dependency
    # growth. No enclosure assertion is made until D^t ORIGINAL H D is checked.
    n=H.nrows(); L=arb_mat(n,n)
    for i in range(n):
        for j in range(i+1):
            x=(H[i,j].mid()-sum((L[i,k]*L[j,k] for k in range(j)),arb(0))).mid()
            if i==j:
                assert x>0, ('candidate pivot',i)
                L[i,j]=x.sqrt().mid()
            else:L[i,j]=(x/L[j,j]).mid()
        if i%100==0: print('candidate Cholesky row',i,flush=True)
    identity=arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
    # The rounded triangular candidate is nonsingular. A verified solve builds
    # a candidate only; the final original-Gram check carries correctness.
    print('Candidate triangular factor complete',flush=True)
    D=L.transpose().solve(identity,algorithm='lu').mid()
    print('Candidate triangular inverse complete',flush=True)
    return D

def derivative_series_check(nodes,features,terms,ds,kernel):
    # Entire Taylor differentiation is independent of Laurent/Si primitives.
    # Include all 15 first-cluster original generators, pole, actual features.
    K=255;powers=list(range(1,K+1,2)); count=nodes[0][1]
    indices=list(range(count))+[469]+list(range(470,484))
    V=arb_mat(len(powers),len(indices)); eps=[];amps=[]
    for j,index in enumerate(indices):
        if index>=470:
            f=features[index-470];c,r,d=f;mu=m.band_moments(f,K)
            for i,n in enumerate(powers):
                V[i,j]=(-1)**((n-1)//2)*m.a(mu[n])*(2*kernel.pi)**n*kernel.b**(n-1)/m.factorial(n-1)
            t=F(44,7)*m.B*(c+r);amp=F(44,7)*(c+r)*(F(3,2) if d else 1)
            eps.append(m.a(amp*t**255/m.factorial(255)));amps.append(m.a(amp))
        elif index==469:
            for i,n in enumerate(powers): V[i,j]=kernel.b**(n-1)/(2**n*m.factorial(n-1))
            t=m.B/2;eps.append(m.a(F(1,2)*t**255/m.factorial(255)/(1-t/256)));amps.append(arb(1))
        else:
            c=nodes[0][0];k=index
            for i,n in enumerate(powers):
                degree=n-k
                if degree>=0:
                    V[i,j]=(-1)**((degree-(1-k%2))//2)*(2*kernel.pi*m.a(c))**degree*kernel.b**(n-1)*n/m.factorial(degree)
            omega=F(44,7)*c;t=omega*m.B;degree=K-k
            error=k*m.B**(k-1)*t**(degree+1)/m.factorial(degree+1)+omega*m.B**k*t**degree/m.factorial(degree)
            eps.append(m.a(error));amps.append(m.a(k*m.B**(k-1)+omega*m.B**k))
    M=arb_mat([[2*kernel.b/(i+j-1) for j in powers] for i in powers]);poly=V.transpose()*M*V
    for i,ii in enumerate(indices):
        for j,jj in enumerate(indices[:i+1]):
            fee=2*kernel.b*(eps[i]*amps[j]+eps[j]*amps[i]+eps[i]*eps[j])
            assert abs(m.gram(ds[ii],ds[jj],kernel)-poly[i,j])<fee,('independent derivative series',ii,jj)
    print('Independent full first-cluster/pole/14-feature derivative series PASS',flush=True)

def main():
    p=argparse.ArgumentParser();p.add_argument('--certificate',required=True)
    p.add_argument('--output',default='artifacts/si29_full_trial_preconditioner.json')
    args=p.parse_args();start=time.monotonic()
    raw=Path(args.certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
    z=json.loads(raw);ctx.prec=z['working_precision_bits'];assert ctx.prec==4096
    assert m.flint.__version__=='0.8.0'
    nodes=[(F(c),p) for c,p in z['original_source_nodes']]
    features=[(F(c),F(r),d) for c,r,d in z['feature_definitions']]
    assert len(nodes)==107 and sum(p for c,p in nodes)==469 and len(features)==14
    terms=[m.source_terms(c,k) for c,p in nodes for k in range(p)]+[m.pole_terms()]+[m.feature_terms(f) for f in features]
    kernel=Kernel();m.independent_series_check(nodes,features,kernel)
    H=arb_mat(470,470)
    for i in range(470):
        for j in range(i+1): H[i,j]=H[j,i]=m.gram(terms[i],terms[j],kernel)
    print('Full original physical H built',round(time.monotonic()-start,2),flush=True)
    D=candidate(H);N=D.transpose()*H*D
    errors=[]
    for i in range(470):
        e=sum((abs(N[i,j]-int(i==j)) for j in range(470)),arb(0))
        assert e<arb('0.01'),('original H normalized row',i,e.str(10))
        errors.append(upper(e))
    print('Full J470 physical normalization verified',float(max(errors)),flush=True)
    X=arb_mat([[ball(v) for v in row] for row in z['full_physical_projection_coefficient_balls']])
    C=arb_mat([[dy(v) for v in row] for row in z['exact_dyadic_feature_transform']])
    Q=arb_mat([[-X[i,j] for j in range(14)] for i in range(470)]+[[arb(int(i==j)) for j in range(14)] for i in range(14)])*C
    # Verify all original cross terms anew. This is a full 484D Gram check,
    # not merely an assertion that the inherited X is the exact projection.
    Bm=arb_mat([[m.gram(terms[i],terms[470+j],kernel) for j in range(14)] for i in range(470)])
    Fm=arb_mat([[m.gram(terms[470+i],terms[470+j],kernel) for j in range(14)] for i in range(14)])
    cross=D.transpose()*(Bm-H*X)*C
    S=C.transpose()*(Fm-Bm.transpose()*X-X.transpose()*Bm+X.transpose()*H*X)*C
    full_errors=[]
    for i in range(470):
        full_errors.append(upper(sum((abs(N[i,j]-int(i==j)) for j in range(470)),arb(0))+sum((abs(cross[i,j]) for j in range(14)),arb(0))))
    for i in range(14):
        full_errors.append(upper(sum((abs(S[i,j]-int(i==j)) for j in range(14)),arb(0))+sum((abs(cross[j,i]) for j in range(470)),arb(0))))
    assert max(full_errors)<F(1,100)
    print('Full 484D physical Gram normalized',float(max(full_errors)),flush=True)
    # P maps exact coordinates to [JD, (F-JX)C]. All its coefficients are
    # exact reals; native X balls enclose the exact defining projection solve.
    P=arb_mat(484,484)
    for i in range(470):
        for j in range(470):P[i,j]=D[i,j]
    for i in range(484):
        for j in range(14):P[i,470+j]=Q[i,j]
    ds=[derivative(t,kernel) for t in terms]
    derivative_series_check(nodes,features,terms,ds,kernel)
    G=arb_mat(484,484)
    for i in range(484):
        for j in range(i+1):G[i,j]=G[j,i]=m.gram(ds[i],ds[j],kernel)
    DP=P.transpose()*G*P
    endpoints=arb_mat([[endpoint(t,kernel) for t in terms]])*P
    trace=upper(sum((DP[i,i] for i in range(484)),arb(0)))
    endpoint2=upper(sum((endpoints[0,j]**2 for j in range(484)),arb(0)))
    assert trace>0 and endpoint2>0
    variation=8*endpoint2+4*m.B*trace
    # exp(7/10)>2 follows already from 1+x+x²/2+x³/6+x⁴/24>2.
    x=F(7,10);assert sum((x**k/m.factorial(k) for k in range(5)),F(0))>2
    choices=[]
    for k in range(0,100):
        R=2**k;t=F(7,10)*k
        # two-sided IBP, (2pi)^2>36, low Fourier Parseval on full trial.
        U=F(101,100)*max(F(36),17+t)+variation*(18+t)/(18*R)
        choices.append((U,k))
    bound,k=min(choices)
    clean=(bound.numerator+bound.denominator-1)//bound.denominator
    assert clean<=128,('energy upper',clean)
    lower=F(33621,10**9)*F(99,100)
    condition=F(clean)/lower
    # Compact deterministic candidate fingerprint; replay recomputes D from
    # the original sources, not from unchecked serialized normalized Grams.
    digest=hashlib.sha256()
    for i in range(470):
        for j in range(470):
            digest.update((json.dumps(m.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
    result=dict(status='CONDITIONAL_ORIGINAL_FULL_484_TRIAL_PHYSICAL_PRECONDITIONER',native_input_sha256=SHA,working_precision_bits=ctx.prec,
      original_source_count=470,actual_continuous_feature_count=14,full_trial_dimension=484,
      independent_derivative_Taylor_degree=255,independent_derivative_checks='all first-cluster generators, pole, all 14 actual continuous features',
      basis='[J D, (F-J X) C], with exact dyadic D,C and exact real X=(J*J)^-1 J*F',
      exact_dyadic_J_transform_sha256=digest.hexdigest(),full_physical_Gram_row_error_uppers=[str(e) for e in full_errors],
      physical_Gram_lower='99/100',physical_Gram_upper='101/100',
      full_trial_derivative_Gram_trace_upper=str(trace),full_trial_endpoint_vector_squared_upper=str(endpoint2),
      full_trial_variation_squared_upper=str(variation),chosen_log_split_dyadic_exponent=k,
      exact_energy_upper=str(bound),rational_Astar_trial_energy_upper=clean,
      conditional_Astar_trial_energy_lower=str(lower),conditional_full_trial_energy_condition_upper=str(condition),
      actual_Astar_matrix_entries_computed=False,actual_Astar_projection_computed=False,
      matched_forcing_computed=False,inverse_response_value_certified=False,
      energy_projected_negative_action_computed=False,negative_action_transfer_claimed=False,
      W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('FULL TRIAL PRECONDITIONER PASS',clean,'condition',float(condition),'seconds',round(time.monotonic()-start,2),flush=True)
if __name__=='__main__':main()
