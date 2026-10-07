"""Independent endpoint Hankel evaluation and complete residual contraction audit."""
import gzip,hashlib,json,sys
from pathlib import Path
from math import comb,lcm
from certify_native_legendre_small_window import F,I,atan
from certify_native_exact_hankel import moment_apply,bilinear_bounds
from certify_native_prime3_matrix36 import precise_sqrt

def read(path):
    raw=Path(path).read_bytes()
    return gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw

def certificate(gram,checkpoint):
    gr=read(gram);cr=read(checkpoint);g=json.loads(gr);cp=json.loads(cr)
    assert g['aperture']==cp['bindings']['aperture']=='49/50'
    assert cp['completed_panels']==g['panel_count']==11
    assert g['complete_panel_checkpoint_sha256']==hashlib.sha256(cr).hexdigest()
    # Closed binomial coefficients, independent of the recurrence constructor.
    p=[[(-1)**(n-k)*comb(n,k)*comb(n+k,k) for k in range(n+1)] for n in range(112)]
    h=h2=F(0);lm=[];l2m=[];zm=[]
    for n in range(1,224):
        h+=F(1,n);h2+=F(1,n*n)
        lm.append((F(1,n*n)+h/n)/2)
        l2m.append((F(2,n**3)+(h*h+h2)/n+2*h/n**2+2*h2/n)/4)
        zm.append(-F(1,2*n))
    def action(moments):
        d=lcm(*(x.denominator for x in moments))
        a=[moment_apply(row,[(int(x*d),int(x*d)) for x in moments],112) for row in p]
        return [[F(bilinear_bounds(row,a[j])[0],2*d) for j in range(112)] for row in p]
    cl=action(lm);fullr=action(l2m);fullz=[[-x for x in row] for row in action([-x for x in zm])]
    old=I.grid;I.grid=10**400
    try:
        pi=16*atan(F(1,5),320)-4*atan(F(1,239),320);zeta=pi*pi/6
        grid=10**300
        rawcs=cp['matrices']['CS']
        denominator=lcm(*(x.denominator for row in cl for x in row))
        den=grid*denominator
        cs=[[(int(pair[0])*denominator,int(pair[1])*denominator) for pair in row] for row in rawcs]
        cli=[[int(x*den) for x in row] for row in cl]
        def product(a,b):
            values=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
            return min(values),max(values)
        def linear(x,a):
            lo,hi=x*a[0],x*a[1]
            return min(lo,hi),max(lo,hi)
        checks=0;controls=0;maxgap=F(0)
        for i in range(112):
            for j in range(i,112):
                root=precise_sqrt(F((2*i+1)*(2*j+1)))
                endpoint=I(0) if (i+j)%2 else I(fullr[i][j])+fullz[i][j]*zeta-sum(((2*n+1)*cl[n][i]*cl[n][j] for n in range(112)),F(0))
                terms=[cp['matrices']['smooth'][i][j],cp['matrices']['cross'][i][j],cp['matrices']['cross'][j][i]]
                smoothlo=sum(int(pair[0]) for pair in terms);smoothhi=sum(int(pair[1]) for pair in terms)
                projectionlo=projectionhi=0
                for n in range(112):
                    terms=[product(cs[n][i],cs[n][j]),linear(cli[n][i],cs[n][j]),linear(cli[n][j],cs[n][i])]
                    projectionlo+=(2*n+1)*sum(a for a,b in terms)
                    projectionhi+=(2*n+1)*sum(b for a,b in terms)
                corrected=endpoint+I(F(smoothlo,grid),F(smoothhi,grid))-I(F(projectionlo,den*den),F(projectionhi,den*den))
                reconstructed=root*corrected
                lo,hi=map(F,g['residual_gram_surrogate'][i][j])
                assert lo<=reconstructed.lo<=reconstructed.hi<=hi
                gap=max(F(0),lo-reconstructed.hi,reconstructed.lo-hi);maxgap=max(maxgap,gap)
                assert reconstructed.lo+1>hi
                count=1 if i==j else 2;checks+=count;controls+=count
        assert checks==controls==12544
        return dict(aperture='49/50',gram_sha256=hashlib.sha256(gr).hexdigest(),checkpoint_sha256=hashlib.sha256(cr).hexdigest(),
            independent_closed_binomial_legendre_coefficients=True,independent_endpoint_log_squared_hankel_moments=True,
            endpoint_pi_alternating_terms=320,interval_grid_digits=400,residual_entries_reconstructed=checks,
            all_finer_reconstructed_intervals_inside_saved_enclosures=True,all_endpoint_smooth_mixed_projection_terms_retained=True,
            displaced_residual_controls_rejected=controls,maximum_interval_gap=str(maxgap),whole_domain_positivity=False,f4_entry_closed=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(*sys.argv[1:]),indent=2))
