"""RC25 exact polynomial components of the physical logarithmic metric.

These are trial-basis components, NOT the RC22 Riesz-head Gram matrices.
The scalar c_R and compact kernel matrix still require certified evaluation.
"""
from fractions import Fraction as F
import json
from validate_rpb108_rc23_canonical_matrix_gate import psd

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c
def scale(a,s): return [s*v for v in a]
def product(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return c
def harmonic(n): return sum((F(1,k) for k in range(1,n+1)),F(0))
def legendre(count):
    if count==1: return [[F(1)]]
    p=[[F(1)],[F(0),F(1)]]
    for n in range(1,count-1):
        p.append(scale(add(scale([F(0)]+p[-1],2*n+1),scale(p[-2],-n)),F(1,n+1)))
    return p
def singular_action(p):
    """(1/2) integral_( -1)^1 [p(t)-p(s)]/abs(t-s) ds."""
    out=[F(0)]*len(p)
    for k,a in enumerate(p):
        out[k]+=a*harmonic(k)
        for j in range(k):
            out[k-1-j]-=a*F(1+(-1)**(j+1),2*(j+1))
    return out
def endpoint_moment(power):
    """Integral_0^1 t^power log(2/sqrt(1-t^2)) dt, even powers."""
    if power%2: raise ValueError('Even power required.')
    m=power//2
    return sum((F(1,2*j+1) for j in range(m+1)),F(0))/F(2*m+1)
def exact_components(count,B=F(11,10)):
    p=legendre(count)
    mass=[[F(0) for _ in p] for _ in p]
    singular=[[F(0) for _ in p] for _ in p]
    endpoint=[]
    for i in range(count):
        mass[i][i]=2*B/F(2*i+1)
        singular[i][i]=harmonic(i)*mass[i][i]
        row=[]
        for j in range(count):
            q=product(p[i],p[j])
            row.append(2*B*sum((a*endpoint_moment(k) for k,a in enumerate(q) if k%2==0),F(0)))
        endpoint.append(row)
    return {'physical_mass':mass,'singular_metric':singular,'endpoint_metric':endpoint}

def controls():
    checks=0
    def check(v):
        nonlocal checks
        assert v, checks+1
        checks+=1
    p=legendre(16)
    for n,q in enumerate(p):
        check(singular_action(q)==scale(q,harmonic(n)))
    check(endpoint_moment(0)==1)
    check(endpoint_moment(2)==F(4,9))
    check(endpoint_moment(4)==F(23,75))
    components=exact_components(8)
    D,W=components['physical_mass'],components['endpoint_metric']
    check(W[0][0]==F(11,5))
    check(W[1][1]==F(44,45))
    check(W[0][2]==F(11,30))
    check(all(W[i][j]==W[j][i] for i in range(8) for j in range(8)))
    check(all(W[i][j]==0 for i in range(8) for j in range(8) if (i+j)%2))
    check(psd([[W[i][j]-D[i][j]/2 for j in range(8)] for i in range(8)]))
    R=F(11,5); a=F(11,4)
    row_half_bound=a*R+6
    hs_sq=2*R*(a*a*R+12*a+72)
    check(row_half_bound==F(241,20))
    check(hs_sq==F(107041,200)<24**2)
    check(1+2/(4*R)==F(27,22))
    check(1-2*row_half_bound==-F(231,10))
    return {'milestone':'RC25','status':'PASS','exact_rational_checks':checks,
            'metric_singular_legendre_eigenvalues':'H_n',
            'endpoint_polynomial_matrix_entries':'exact rational',
            'regular_kernel_Hilbert_Schmidt_norm_upper':24,
            'actual_trial_component_dimension':8,
            'complete_metric_matrix_evaluated':False,
            'actual_Riesz_head_matrix_evaluated':False,
            'actual_head_certified':False,'whole_centered_aperture_extended':False,
            'RH':False,'F4':False,'Lean':False}

if __name__=='__main__': print(json.dumps(controls(),indent=2))
