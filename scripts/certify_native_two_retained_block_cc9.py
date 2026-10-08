"""Four actual original sources and a mixed two-retained completed-Schur block."""
import sys,json,gzip,hashlib
from certify_native_coupled_trial_cc3 import (F,I,D,ROOT,source,shifted_legendre,
    sqrt_rational,primitives,dot,mul,add,bracket)
from certify_native_two_trial_solve_cc8 import midpoint,solve_midpoint

def attach_slice(result):
    if result['two_retained_plane_positive']:
        d=F(result['lower_block_determinant'][0])
        lower=result['original_completed_schur_lower_block']
        trace=F(lower[0][0][1])+F(lower[1][1][1])
        mass_trace=sum(map(F,result['retained_masses']),F(0))
        tau=d/(trace*mass_trace)
        c=F(result['complement_lower']);mu=min(tau/F(266),c/2)
        kap=mu/(10*(mu+26))
        result['protected_slice_codimension']=110
        result['slice_retained_physical_margin']=str(tau)
        result['whole_infinite_slice_physical_margin']=str(mu)
        result['whole_infinite_slice_canonical_margin']=str(kap)
        result['original_nonpositive_spectral_dimension_upper']=110
        result['displays']['retained_plane_physical_margin']=float(tau)
        result['displays']['infinite_slice_physical_margin']=float(mu)
        result['displays']['infinite_slice_canonical_margin']=float(kap)
    return result

def compute():
    savedpath=ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'
    saved=json.loads(savedpath.read_bytes());v=list(map(F,saved['rational_coefficient_witness']))
    rawbytes=gzip.decompress((ROOT/'notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
    assert hashlib.sha256(rawbytes).hexdigest()==saved['input_sha256']['native']
    raw=json.loads(rawbytes);native=[[None]*112 for _ in range(112)];index=0
    for i in range(112):
        for j in range(i+1):
            l,r=raw['lower_triangle_row_major'][index];index+=1
            native[i][j]=native[j][i]=I(F(int(l),10**80),F(int(r),10**80))
    P=shifted_legendre(114);norms=[sqrt_rational(F(2*j+1)/D) for j in range(115)]
    weights=[v[j]*midpoint(norms[j]) if j%2==0 else F(0) for j in range(112)]
    ph=[sum((weights[j]*(P[j][k] if k<=j else 0) for j in range(112)),F(0)) for k in range(111)]
    nu=midpoint(norms[0]);nz=[midpoint(norms[n]) for n in (112,114)]
    polys=[ph,[nu]]+[[nz[i]*x for x in P[n]] for i,n in enumerate((112,114))]
    M0=[sum(map(abs,weights),F(0)),abs(nu)]+list(map(abs,nz))
    M1=[sum((abs(weights[j])*j*(j+1) for j in range(112)),F(0)),F(0)]+[abs(nz[i])*n*(n+1) for i,n in enumerate((112,114))]
    regs=[];errors=[]
    for i,p in enumerate(polys):
        print('CC9 source',i,file=sys.stderr,flush=True)
        r,e,pi,geom=source(p,M0[i],M1[i]);regs.append(r);errors.append(e)
    errors[0]+=2*F(10**7)*sum((abs(v[j])*sqrt_rational(D/F(2*j+1)).hi/(2*I.grid) for j in range(0,112,2)),F(0))
    assert max(errors)<F(1,10**44)
    degree=max(len(row) for rows in regs for row in rows)*2-2
    print('CC9 primitives',degree,file=sys.stderr,flush=True)
    prim=[primitives(t,degree) for t in geom['cuts']]
    moments=[[I(0) for _ in range(115)] for _ in range(4)]
    gram=[[I(0) for _ in range(4)] for _ in range(4)]
    h1=[];h2=[];harm=F(0);harm2=F(0)
    for k in range(229):
        n=k+1;harm+=F(1,n);harm2+=F(1,n*n)
        h1.append(I((F(1,n*n)+harm/n)/2))
        h2.append(I((F(2,n**3)+(harm*harm+harm2)/n+2*harm/n**2+2*harm2/n)/4)-pi*pi/(12*n))
    for i in range(4):
        for j in range(i,4):gram[i][j]+=dot(mul(polys[i],polys[j]),h2)
    for panel,(a,b) in enumerate(zip(prim,prim[1:])):
        print('CC9 panel',panel,file=sys.stderr,flush=True)
        mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
        lm=[b[1][k]-a[1][k] for k in range(degree+1)]
        mm=[I(max(0,x.lo),x.hi) for x in mm];lm=[I(max(0,x.lo),x.hi) for x in lm]
        for i in range(4):
            for k in range(115):moments[i][k]+=dot(regs[i][panel],mm[k:])
            for j in range(i,4):
                gram[i][j]+=dot(mul(regs[i][panel],regs[j][panel]),mm)
                gram[i][j]+=dot(add(mul(polys[i],regs[j][panel]),mul(polys[j],regs[i][panel])),lm)
    for i in range(4):
        for k in range(115):moments[i][k]+=dot(polys[i],h1[k:])
    coarse=[F(10**8)*(1+x) for x in M0]
    for i in range(4):
        for j in range(i,4):
            err=errors[i]*coarse[j]+errors[j]*coarse[i]+errors[i]*errors[j]
            gram[i][j]=gram[j][i]=D*gram[i][j]+I(-err,err)
    projected=[];native_audits=0
    ucoeff=nu*sqrt_rational(D)
    for i in range(4):
        row=[]
        for k in range(0,112,2):
            x=D*norms[k]*dot(P[k],moments[i])+I(-errors[i],errors[i])
            if i<2:
                audit=sum((v[j]*native[k][j] for j in range(0,112,2)),I(0)) if i==0 else ucoeff*native[k][0]
                assert max(x.lo,audit.lo)<=min(x.hi,audit.hi),('native',i,k)
                native_audits+=1
            row.append(x)
        projected.append(row)
    for i in range(4):
        for j in range(i,4):
            gram[i][j]=gram[j][i]=gram[i][j]-sum((a*b for a,b in zip(projected[i],projected[j])),I(0))
    # Only the h diagonal needs its actual odd source energy, orthogonal to all even columns.
    M=F(saved['surrogate_map_norm_upper'])+F(saved['complete_source_map_allowance'])
    assert M<8
    oddmass=sum((v[j]*v[j] for j in range(1,112,2)),F(0))
    gram[0][0]+=I(0,64*oddmass)
    massh=F(saved['witness_mass_squared']);massu=D*nu*nu
    massz=[D*nz[i]*nz[i]/(2*n+1) for i,n in enumerate((112,114))]
    QZ=[[I(0) for _ in range(2)] for _ in range(2)];BZ=[[I(0) for _ in range(2)] for _ in range(2)]
    symmetry=0
    for i,n in enumerate((112,114)):
        for j in range(2):
            x=D*nz[i]*dot(P[n],moments[j])+I(-errors[j]*sqrt_rational(massz[i]).hi,errors[j]*sqrt_rational(massz[i]).hi)
            y=D*dot(polys[j],moments[i+2])+I(-errors[i+2]*sqrt_rational((massh,massu)[j]).hi,errors[i+2]*sqrt_rational((massh,massu)[j]).hi)
            assert max(x.lo,y.lo)<=min(x.hi,y.hi);symmetry+=1
            BZ[i][j]=I(min(x.lo,y.lo),max(x.hi,y.hi))
        for j,m in enumerate((112,114)):
            QZ[i][j]=D*nz[i]*dot(P[n],moments[j+2])+I(-errors[j+2]*sqrt_rational(massz[i]).hi,errors[j+2]*sqrt_rational(massz[i]).hi)
    assert max(QZ[0][1].lo,QZ[1][0].lo)<=min(QZ[0][1].hi,QZ[1][0].hi);symmetry+=1
    QZ[0][1]=QZ[1][0]=I(min(QZ[0][1].lo,QZ[1][0].lo),max(QZ[0][1].hi,QZ[1][0].hi))
    A00=I(*map(F,saved['native_weil_witness_interval']))
    A01=D*nu*moments[0][0]+I(-errors[0]*sqrt_rational(massu).hi,errors[0]*sqrt_rational(massu).hi)
    A01b=D*dot(ph,moments[1])+I(-errors[1]*sqrt_rational(massh).hi,errors[1]*sqrt_rational(massh).hi)
    native_cross=ucoeff*sum((v[j]*native[j][0] for j in range(112)),I(0))
    assert max(A01.lo,A01b.lo,native_cross.lo)<=min(A01.hi,A01b.hi,native_cross.hi);symmetry+=1
    A01=I(min(A01.lo,A01b.lo,native_cross.lo),max(A01.hi,A01b.hi,native_cross.hi))
    A11=D*nu*moments[1][0]+I(-errors[1]*sqrt_rational(massu).hi,errors[1]*sqrt_rational(massu).hi)
    assert max(A11.lo,(ucoeff*ucoeff*native[0][0]).lo)<=min(A11.hi,(ucoeff*ucoeff*native[0][0]).hi)
    AR=[[A00,A01],[A01,A11]];GR=[row[:2] for row in gram[:2]]
    GZ=[row[2:] for row in gram[2:]];VZ=[row[:2] for row in gram[2:]]
    c=F(699,1000)
    J=[[GZ[i][j]/c-QZ[i][j] for j in range(2)] for i in range(2)]
    AA=[[VZ[i][j]/c-BZ[i][j] for j in range(2)] for i in range(2)]
    assert J[0][0].lo>0 and (J[0][0]*J[1][1]-J[0][1]*J[1][0]).lo>0
    columns=[solve_midpoint(J,[AA[i][j] for i in range(2)]) for j in range(2)]
    T=[[columns[j][i] for j in range(2)] for i in range(2)]
    credit=[[sum((AA[k][i]*T[k][j]+T[k][i]*AA[k][j] for k in range(2)),I(0))-
             sum((T[k][i]*J[k][l]*T[l][j] for k in range(2) for l in range(2)),I(0)) for j in range(2)] for i in range(2)]
    lower=[[AR[i][j]-GR[i][j]/c+credit[i][j] for j in range(2)] for i in range(2)]
    determinant=lower[0][0]*lower[1][1]-lower[0][1]*lower[1][0]
    positive=lower[0][0].lo>0 and determinant.lo>0
    result={'stage':'CC9 actual mixed two-retained Schur lower block','aperture':'21/20',
        'retained_directions':['saved original coefficient witness','defined rational constant'],
        'constant_rational_scale':str(nu),'trial_degrees':[112,114],'complement_lower':str(c),
        'retained_masses':[str(massh),str(massu)],'odd_original_witness_mass':str(oddmass),
        'retained_native_block':[[bracket(x) for x in row] for row in AR],
        'actual_retained_source_gram':[[bracket(x) for x in row] for row in GR],
        'trial_native_gram':[[bracket(x) for x in row] for row in QZ],
        'trial_action_gram':[[bracket(x) for x in row] for row in GZ],
        'mixed_trial_native':[[bracket(x) for x in row] for row in BZ],
        'mixed_trial_action':[[bracket(x) for x in row] for row in VZ],
        'rational_linear_lift':[[str(x) for x in row] for row in T],
        'matrix_credit':[[bracket(x) for x in row] for row in credit],
        'original_completed_schur_lower_block':[[bracket(x) for x in row] for row in lower],
        'lower_block_determinant':bracket(determinant),'two_retained_plane_positive':positive,
        'source_errors':list(map(str,errors)),'native_pairing_audits':native_audits,
        'cross_source_symmetry_audits':symmetry,'integration_degree':degree,
        'full_112_retained_schur_sign':False,'whole_domain_positivity':False,'lean_certified':False,
        'full_source_gram_archives_replayed':False,
        'input_sha256':{'saved_target':hashlib.sha256(savedpath.read_bytes()).hexdigest(),'native':hashlib.sha256(rawbytes).hexdigest()},
        'displays':{'lower_block':[[[float(x.lo),float(x.hi)] for x in row] for row in lower],
                    'determinant':[float(determinant.lo),float(determinant.hi)]}}
    return attach_slice(result)

if __name__=='__main__':
    result=compute()
    (ROOT/'notes/data/RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['displays'],indent=2))
    print('two_retained_plane_positive',result['two_retained_plane_positive'])
