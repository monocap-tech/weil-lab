"""CC10: one complete odd source enlarges CC9's exact original retained plane."""
from certify_native_coupled_trial_cc3 import *
from certify_native_two_trial_solve_cc8 import midpoint

def source_odd(p,M0,M1):
    # Parity -1: right kernel difference is -reflect(left);
    # signed pole moments obey M_minus=-M_plus, not M_minus=M_plus.
    assert exact_reflect(p)==[-c for c in p]
    N,K=140,180
    B=bernoulli(2*K+2)
    bp=[F(0)]*(2*K+1);bp[0],bp[1]=F(1),D
    for k in range(1,K+1):bp[2*k]=B[2*k]*(2*D)**(2*k)/factorial(2*k)
    A=[c/2 for c in mul(bp,[(-D/2)**k/factorial(k) for k in range(N+1)])]
    ce=F(23,10)*(D/2)**(N+1)/factorial(N+1)
    cb=4*(D/3)**(2*K+2)/(1-(D/3)**2)
    he=ce/(N+1)+cb/(2*K+2);ae=ce/(N+2)+cb/(2*K+3)
    H=[F(0)]+[-A[k]/k for k in range(1,len(A))]
    smooth=mul(p,add(H,exact_reflect(H)))
    left=[F(0)]*(len(p)+len(A)-1)
    for j,c in enumerate(p):
        for k,a in enumerate(A):left[j+k]+=c*a*regular_difference_factor(j,k)
    smooth=add(smooth,[-c for c in add(left,[-c for c in exact_reflect(left)])])
    pi=16*atan(F(1,5),500)-4*atan(F(1,239),500)
    gamma=I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-log(F(100))
    gamma+=sum((B[2*k]/F(2*k*100**(2*k)) for k in range(1,57)),F(0))
    ge=abs(B[114])/F(114*100**114);gamma+=I(-ge,ge)
    constant=-gamma-log(F(2))-I(log(pi.lo).lo,log(pi.hi).hi)-log(D)
    ep=compose([(D/2)**k/factorial(k) for k in range(N+1)],F(-1,2))
    em=exact_reflect(ep)
    mp=D*sum((c/F(k+1) for k,c in enumerate(mul(p,ep))),F(0))
    core=[I(c)+constant*(p[k] if k<len(p) else 0) for k,c in enumerate(smooth)]
    core=add(core,[mp*(-ep[k]+em[k]) for k in range(N+1)])
    ns=[2,3,4,5,7,8]
    amplitudes=[log(F(2))/sqrt_rational(F(2)),log(F(3))/sqrt_rational(F(3)),
                log(F(2))/2,log(F(5))/sqrt_rational(F(5)),
                log(F(7))/sqrt_rational(F(7)),log(F(2))/sqrt_rational(F(8))]
    geom=translation_panels(F(21,20),logarithm=log)
    shifts={(i,s):[-amplitudes[i]*c for c in compose(p,s*log(F(n))/D)] for i,n in enumerate(ns) for s in (1,-1)}
    panels=[];radius=F(0);grid=10**250
    for active in geom['active']:
        row=core[:]
        for i,s in active:row=add(row,shifts[i,s])
        mids=[];err=F(0)
        for x in row:
            x=x if isinstance(x,I) else I(x)
            mid=F((((x.lo+x.hi)/2)*grid).__floor__(),grid)
            mids.append(mid);err+=max(abs(x.lo-mid),abs(x.hi-mid))
        panels.append(mids);radius=max(radius,err)
    exp_error=2*(D/4)**(N+1)/factorial(N+1)
    uniform=2*M0*he+2*M1*ae+100*D*M0*exp_error+radius
    return panels,sqrt_rational(D).hi*uniform,pi,geom

def read_interval(x):return I(*map(F,x))

def compute():
    cc9path=ROOT/'notes/data/RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json'
    old=json.loads(cc9path.read_bytes())
    savedpath=ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'
    saved=json.loads(savedpath.read_bytes());v=list(map(F,saved['rational_coefficient_witness']))
    assert v[2]!=0 and saved['physical_complement_lower']==old['complement_lower']=='699/1000'
    assert F(saved['surrogate_map_norm_upper'])+F(saved['complete_source_map_allowance'])<8
    raw=gzip.decompress((ROOT/'notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()==saved['input_sha256']['native']
    native=json.loads(raw);Q=[[None]*112 for _ in range(112)];index=0
    for i in range(112):
        for j in range(i+1):
            lo,hi=native['lower_triangle_row_major'][index];index+=1
            Q[i][j]=Q[j][i]=I(F(int(lo),10**80),F(int(hi),10**80))
    P=shifted_legendre(111);norms=[sqrt_rational(F(2*j+1)/D) for j in range(112)]
    no=midpoint(norms[1]);p=[no*x for x in P[1]];mass=D*no*no/3
    print('CC10 odd source',file=sys.stderr,flush=True)
    regs,error,pi,geom=source_odd(p,abs(no),2*abs(no))
    degree=max(len(r) for r in regs)*2-2
    print('CC10 primitives',degree,file=sys.stderr,flush=True)
    prim=[primitives(t,degree) for t in geom['cuts']]
    moments=[I(0) for _ in range(112)];gram=I(0)
    h1=[];h2=[];harm=F(0);harm2=F(0)
    for k in range(114):
        n=k+1;harm+=F(1,n);harm2+=F(1,n*n)
        h1.append(I((F(1,n*n)+harm/n)/2))
        h2.append(I((F(2,n**3)+(harm*harm+harm2)/n+2*harm/n**2+2*harm2/n)/4)-pi*pi/(12*n))
    gram+=dot(mul(p,p),h2)
    for panel,(a,b) in enumerate(zip(prim,prim[1:])):
        print('CC10 panel',panel,file=sys.stderr,flush=True)
        mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
        lm=[b[1][k]-a[1][k] for k in range(degree+1)]
        mm=[I(max(0,x.lo),x.hi) for x in mm];lm=[I(max(0,x.lo),x.hi) for x in lm]
        for k in range(112):moments[k]+=dot(regs[panel],mm[k:])
        gram+=dot(mul(regs[panel],regs[panel]),mm)+2*dot(mul(p,regs[panel]),lm)
    for k in range(112):moments[k]+=dot(p,h1[k:])
    coarse=F(10**8)*(1+abs(no));budget=2*error*coarse+error*error
    gram=D*gram+I(-budget,budget);projections=[];audits=0
    coeff=no*sqrt_rational(D/3)
    for k in range(1,112,2):
        x=D*norms[k]*dot(P[k],moments)+I(-error,error)
        audit=coeff*Q[k][1]
        assert max(x.lo,audit.lo)<=min(x.hi,audit.hi),('odd native',k)
        projections.append(x);audits+=1
    for x in projections:gram-=x*x
    native_self=coeff*coeff*Q[1][1]
    own=D*dot(p,moments)+I(-error*sqrt_rational(mass).hi,error*sqrt_rational(mass).hi)
    assert max(own.lo,native_self.lo)<=min(own.hi,native_self.hi)
    own=I(min(own.lo,native_self.lo),max(own.hi,native_self.hi))
    c=F(old['complement_lower']);last=own-gram/c
    oddmass=F(old['odd_original_witness_mass'])
    assert gram.hi>=0
    crossbudget=8*sqrt_rational(oddmass*gram.hi).hi
    native_cross=coeff*sum((v[j]*Q[j][1] for j in range(1,112,2)),I(0))
    cross=native_cross+I(-crossbudget/c,crossbudget/c)
    lower=[[read_interval(x) for x in row]+[I(0)] for row in old['original_completed_schur_lower_block']]
    lower.append([cross,I(0),last]);lower[0][2]=cross
    # Entire mixed lower form: old two-column lift extended by ZERO odd trial.
    a,b,d=lower[0][0],lower[0][1],lower[1][1]
    det2=a*d-b*b;det3=last*det2-d*cross*cross
    positive=a.lo>0 and det2.lo>0 and det3.lo>0
    result={'stage':'CC10 original parity enlargement','aperture':'21/20',
        'retained_directions':old['retained_directions']+['defined rational odd degree-one Legendre'],
        'odd_rational_scale':str(no),'odd_mass':str(mass),'odd_source_error':str(error),
        'odd_projected_source_norm_squared':bracket(gram),'odd_native_energy':bracket(own),
        'odd_scalar_schur_lower':bracket(last),'native_odd_witness_cross':bracket(native_cross),
        'whole_mixed_source_cross_bound':str(crossbudget),'odd_native_pairing_audits':audits,
        'odd_native_self_overlap_audit':True,'integration_degree':degree,
        'original_completed_schur_lower_block':[[bracket(x) for x in row] for row in lower],
        'lower_determinant':bracket(det3),'three_retained_plane_positive':positive,
        'all_original_prime_powers':[2,3,4,5,7,8],'both_signed_pole_slots':True,
        'source_reflection_parity':-1,'whole_complement_retained':True,
        'full_112_retained_sign':False,'whole_aperture_positive':False,'lean_certified':False,
        'input_sha256':{'cc9':hashlib.sha256(cc9path.read_bytes()).hexdigest(),
                        'saved_target':hashlib.sha256(savedpath.read_bytes()).hexdigest(),
                        'native':hashlib.sha256(raw).hexdigest()},
        'displays':{'odd_native':float(own.lo),'odd_source_norm_squared_upper':float(gram.hi),
                    'odd_schur_lower':float(last.lo),'mixed_determinant_lower':float(det3.lo)}}
    if positive:
        # lambda_min >= det / sum of the three principal order-two minors.
        minors=det2+a*last-cross*cross+d*last
        coord=det3.lo/minors.hi
        masses=sum(map(F,old['retained_masses']),F(0))+mass
        tau=coord/masses;mu=min(tau/266,c/2);canonical=mu/(10*(mu+26))
        result.update(protected_slice_codimension=109,slice_retained_physical_margin=str(tau),
            whole_infinite_slice_physical_margin=str(mu),whole_infinite_slice_canonical_margin=str(canonical),
            original_nonpositive_spectral_dimension_upper=109)
        result['displays'].update(physical_slice_margin=float(mu),canonical_slice_margin=float(canonical))
    return result

if __name__=='__main__':
    result=compute()
    (ROOT/'notes/data/RPB108_ODD_ENLARGEMENT_CC10_CERTIFICATE_20261008.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['displays'],indent=2));print('three_retained_plane_positive',result['three_retained_plane_positive'])
