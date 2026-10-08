"""Actual original degree-112/114 complement action integrations and shifted solve.

Reconstructs three complete sources; does not use the blocked full archives.
All polynomial and endpoint-log products are enclosed with exact rationals.
"""
import sys,json,hashlib,gzip
from pathlib import Path
from certify_native_coupled_trial_cc3 import (F,I,D,ROOT,source,shifted_legendre,
    sqrt_rational,primitives,dot,mul,add,bracket,log)

def midpoint(x):return (x.lo+x.hi)/2
def quadratic(M,t):return sum((t[i]*M[i][j]*t[j] for i in range(2) for j in range(2)),I(0))
def dot2(t,v):return sum((t[i]*v[i] for i in range(2)),I(0))
def solve_midpoint(M,b):
    a,d,f=midpoint(M[0][0]),midpoint(M[0][1]),midpoint(M[1][1])
    v,w=map(midpoint,b);det=a*f-d*d
    assert det>0
    values=((f*v-d*w)/det,(a*w-d*v)/det)
    grid=10**100
    return [F((x*grid).__floor__(),grid) for x in values]

def attach_head_tail(result):
    saved=json.loads((ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json').read_bytes())
    c=F(result['complement_lower'])
    tail=F(result['actual_source_norm_squared'][1])/(2*c)
    lower=F(saved['native_weil_witness_interval'][0])-F(result['actual_first_shifted_head_quadratic'][1])-tail
    result['whole_original_inverse_tail_after_first_head_upper']=str(tail)
    result['original_completed_direction_first_head_plus_whole_tail_lower']=str(lower)
    result['first_head_plus_whole_tail_direction_positive']=lower>0
    result['displays']['first_head_plus_whole_tail_direction_lower']=float(lower)
    return result

def compute():
    savedpath=ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'
    saved=json.loads(savedpath.read_bytes());vcoeff=list(map(F,saved['rational_coefficient_witness']))
    native_raw=gzip.decompress((ROOT/'notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
    assert hashlib.sha256(native_raw).hexdigest()==saved['input_sha256']['native']
    raw=json.loads(native_raw);native=[[None]*112 for _ in range(112)];index=0
    for i in range(112):
        for j in range(i+1):
            l,u=raw['lower_triangle_row_major'][index];index+=1
            native[i][j]=native[j][i]=I(F(int(l),10**80),F(int(u),10**80))
    P=shifted_legendre(114);norms=[sqrt_rational(F(2*j+1)/D) for j in range(115)]
    weights=[vcoeff[j]*midpoint(norms[j]) if j%2==0 else F(0) for j in range(112)]
    ph=[sum((weights[j]*(P[j][k] if k<=j else 0) for j in range(112)),F(0)) for k in range(111)]
    nz=[midpoint(norms[n]) for n in (112,114)]
    polynomials=[ph]+[[nz[i]*x for x in P[n]] for i,n in enumerate((112,114))]
    M0=[sum(map(abs,weights),F(0))]+list(map(abs,nz))
    M1=[sum((abs(weights[j])*j*(j+1) for j in range(112)),F(0))]+[abs(nz[i])*n*(n+1) for i,n in enumerate((112,114))]
    regular=[];errors=[]
    for k,p in enumerate(polynomials):
        print('CC8 source',k,file=sys.stderr,flush=True)
        r,e,pi,geom=source(p,M0[k],M1[k]);regular.append(r);errors.append(e)
    errors[0]+=2*F(10**7)*sum((abs(vcoeff[j])*sqrt_rational(D/F(2*j+1)).hi/(2*I.grid) for j in range(0,112,2)),F(0))
    assert max(errors)<F(1,10**44)
    degree=max(len(row) for rows in regular for row in rows)*2-2
    print('CC8 primitives degree',degree,file=sys.stderr,flush=True)
    prim=[primitives(t,degree) for t in geom['cuts']]
    projections=[[I(0) for _ in range(115)] for _ in range(3)]
    gram=[[I(0) for _ in range(3)] for _ in range(3)]
    h1=[];h2=[];harm=F(0);harm2=F(0)
    for k in range(229):
        n=k+1;harm+=F(1,n);harm2+=F(1,n*n)
        h1.append(I((F(1,n*n)+harm/n)/2))
        h2.append(I((F(2,n**3)+(harm*harm+harm2)/n+2*harm/n**2+2*harm2/n)/4)-pi*pi/(12*n))
    for i in range(3):
        for j in range(i,3):gram[i][j]+=dot(mul(polynomials[i],polynomials[j]),h2)
    for panel,(left,right) in enumerate(zip(prim,prim[1:])):
        print('CC8 integrate panel',panel,file=sys.stderr,flush=True)
        moments=[(right[0][k+1]-left[0][k+1])/(k+1) for k in range(degree+1)]
        logs=[right[1][k]-left[1][k] for k in range(degree+1)]
        moments=[I(max(0,x.lo),x.hi) for x in moments];logs=[I(max(0,x.lo),x.hi) for x in logs]
        for i in range(3):
            for k in range(115):projections[i][k]+=dot(regular[i][panel],moments[k:])
            for j in range(i,3):
                gram[i][j]+=dot(mul(regular[i][panel],regular[j][panel]),moments)
                gram[i][j]+=dot(add(mul(polynomials[i],regular[j][panel]),mul(polynomials[j],regular[i][panel])),logs)
    for i in range(3):
        for k in range(115):projections[i][k]+=dot(polynomials[i],h1[k:])
    coarse=[F(10**8)*(1+x) for x in M0]
    for i in range(3):
        for j in range(i,3):
            err=errors[i]*coarse[j]+errors[j]*coarse[i]+errors[i]*errors[j]
            gram[i][j]=gram[j][i]=D*gram[i][j]+I(-err,err)
    physical=[];audit_count=0
    for i in range(3):
        row=[]
        for k in range(0,112,2):
            value=D*norms[k]*dot(P[k],projections[i])+I(-errors[i],errors[i])
            if i==0:
                audit=sum((vcoeff[j]*native[k][j] for j in range(0,112,2)),I(0))
                assert max(value.lo,audit.lo)<=min(value.hi,audit.hi)
                audit_count+=1
            row.append(value)
        physical.append(row)
    for i in range(3):
        for j in range(i,3):
            gram[i][j]=gram[j][i]=gram[i][j]-sum((a*b for a,b in zip(physical[i],physical[j])),I(0))
    Q=[[I(0) for _ in range(2)] for _ in range(2)];b=[];mass=[];symmetry_audits=0
    for i,n in enumerate((112,114)):
        mass.append(D*nz[i]*nz[i]/(2*n+1))
        bp=D*nz[i]*dot(P[n],projections[0])+I(-errors[0]*sqrt_rational(mass[i]).hi,errors[0]*sqrt_rational(mass[i]).hi)
        symmetric=D*dot(ph,projections[i+1])+I(-errors[i+1]*sqrt_rational(F(saved['witness_mass_squared'])).hi,errors[i+1]*sqrt_rational(F(saved['witness_mass_squared'])).hi)
        assert max(bp.lo,symmetric.lo)<=min(bp.hi,symmetric.hi);b.append(bp);symmetry_audits+=1
        for j,m in enumerate((112,114)):
            Q[i][j]=D*nz[i]*dot(P[n],projections[j+1])+I(-errors[j+1]*sqrt_rational(mass[i]).hi,errors[j+1]*sqrt_rational(mass[i]).hi)
    assert max(Q[0][1].lo,Q[1][0].lo)<=min(Q[0][1].hi,Q[1][0].hi);symmetry_audits+=1
    # Preserve both independent outward bounds; use their hull symmetrically.
    Q[0][1]=Q[1][0]=I(min(Q[0][1].lo,Q[1][0].lo),max(Q[0][1].hi,Q[1][0].hi))
    G=[[gram[i+1][j+1] for j in range(2)] for i in range(2)];cross=[gram[0][j+1] for j in range(2)]
    c=F(699,1000);J=[[G[i][j]/c-Q[i][j] for j in range(2)] for i in range(2)]
    a=[cross[i]/c-b[i] for i in range(2)]
    assert J[0][0].lo>0 and (J[0][0]*J[1][1]-J[0][1]*J[1][0]).lo>0
    t=solve_midpoint(J,a)
    credit=2*dot2(t,a)-quadratic(J,t)
    baseline=I(*map(F,saved['corrected_witness_interval']));schur=baseline+credit
    tau=c
    QL=[[Q[i][j]+(I(tau*mass[i]) if i==j else I(0)) for j in range(2)] for i in range(2)]
    GL=[[G[i][j]+2*tau*Q[i][j]+(I(tau*tau*mass[i]) if i==j else I(0)) for j in range(2)] for i in range(2)]
    vL=[cross[i]+tau*b[i] for i in range(2)]
    ts=solve_midpoint(GL,vL)
    # Source norm from complete saved corrected estimator, with native/baseline intervals outward.
    qnative=I(*map(F,saved['native_weil_witness_interval']));wmass=F(saved['witness_mass_squared'])
    norm2=c*(qnative-baseline)+I(-2*F(saved['actual_gram_operator_error_upper'])*wmass,0)
    assert norm2.lo>0
    residual2=norm2-2*dot2(ts,vL)+quadratic(GL,ts)
    assert residual2.hi>0
    residual2=I(max(0,residual2.lo),residual2.hi)
    head_lower=2*dot2(ts,b)-quadratic(QL,ts)
    head=I(head_lower.lo,(head_lower+residual2/(c+tau)).hi)
    result={'stage':'CC8 actual two-trial original solve','aperture':'21/20',
        'trial_degrees':[112,114],'complement_lower':str(c),'trial_masses':list(map(str,mass)),
        'original_native_trial_gram':[[bracket(x) for x in row] for row in Q],
        'actual_action_gram':[[bracket(x) for x in row] for row in G],
        'source_cross_action':list(map(bracket,cross)),'source_native_cross':list(map(bracket,b)),
        'unshifted_inverse_trial_coefficients':list(map(str,t)),
        'inverse_estimator_credit':bracket(credit),'original_completed_direction_lower':bracket(schur),
        'shift':str(tau),'actual_shifted_solve_coefficients':list(map(str,ts)),
        'actual_source_norm_squared':bracket(norm2),'actual_shifted_residual_norm_squared':bracket(residual2),
        'actual_first_shifted_head_quadratic':bracket(head),
        'shifted_solve_mass_error_squared_upper':str(residual2.hi/(c+tau)**2),
        'residual_relative_squared_upper':str(residual2.hi/norm2.lo),
        'source_errors':list(map(str,errors)),'native_pairing_audits':audit_count,
        'cross_source_symmetry_audits':symmetry_audits,'integration_degree':degree,
        'source_and_gram_archives_replayed':False,'full_112_column_solve':False,
        'whole_domain_positivity':False,'new_aperture_certificate':False,'lean_certified':False,
        'input_sha256':{'saved_target':hashlib.sha256(savedpath.read_bytes()).hexdigest(),'native':hashlib.sha256(native_raw).hexdigest()},
        'displays':{'credit_lower':float(credit.lo),'completed_lower':float(schur.lo),
                    'shifted_head_lower':float(head.lo),'shifted_head_upper':float(head.hi),
                    'residual_relative_squared_upper':float(residual2.hi/norm2.lo)}}
    return attach_head_tail(result)

if __name__=='__main__':
    result=compute()
    path=ROOT/'notes/data/RPB108_TWO_TRIAL_SOLVE_CC8_CERTIFICATE_20261008.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['displays'],indent=2))
