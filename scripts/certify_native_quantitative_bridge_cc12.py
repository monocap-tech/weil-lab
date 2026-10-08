"""Actual three-plane metric, correlated entire native row and residual obstruction."""
from certify_native_coupled_trial_cc3 import *
from certify_native_two_trial_solve_cc8 import midpoint,solve_midpoint
from validate_native_two_trial_solve_cc8 import solve
sys.set_int_max_str_digits(0)

def read(x):return I(*map(F,x))
def compact(x):
    g=10**100
    return I(F((x.lo*g).__floor__(),g),F((x.hi*g).__ceil__(),g))
def normupper(row):return sqrt_rational(sum((max(abs(x.lo),abs(x.hi))**2 for x in row),F(0))).hi
def quad(A,t):return sum((t[i]*A[i][j]*t[j] for i in range(len(t)) for j in range(len(t))),I(0))

def compute():
    paths={k:ROOT/'notes/data'/p for k,p in {
        'cc3':'RPB108_COUPLED_TRIAL_CC3_CERTIFICATE_20261008.json',
        'cc9':'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json',
        'cc10':'RPB108_ODD_ENLARGEMENT_CC10_CERTIFICATE_20261008.json',
        'cc11':'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json',
        'saved':'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'}.items()}
    data={k:json.loads(p.read_bytes()) for k,p in paths.items()};old=data['cc9'];three=data['cc10'];saved=data['saved']
    raw=gzip.decompress((ROOT/'notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()==saved['input_sha256']['native']==old['input_sha256']['native']
    native=json.loads(raw);Q=[[None]*112 for _ in range(112)];idx=0
    for i in range(112):
        for j in range(i+1):
            lo,hi=native['lower_triangle_row_major'][idx];idx+=1
            Q[i][j]=Q[j][i]=I(F(int(lo),10**80),F(int(hi),10**80))
    v=list(map(F,saved['rational_coefficient_witness']));c=F(old['complement_lower'])
    M=F(saved['surrogate_map_norm_upper'])+F(saved['complete_source_map_allowance'])
    assert c==F(699,1000) and M<8 and v[2]!=0
    block=[[read(x) for x in row] for row in three['original_completed_schur_lower_block']]
    scales=[F(10**16),F(1),F(1)];grid=10**100
    scaled=[[block[i][j]*scales[i]*scales[j] for j in range(3)] for i in range(3)]
    centre=[[F((midpoint(x)*grid).__floor__(),grid) for x in row] for row in scaled]
    radius=max(sum((max(centre[i][j]-x.lo,x.hi-centre[i][j]) for j,x in enumerate(row)),F(0)) for i,row in enumerate(scaled))
    pad=F((radius*grid).__ceil__(),grid)
    G=[[centre[i][j]-(pad if i==j else 0) for j in range(3)] for i in range(3)]
    G=[[G[i][j]/(scales[i]*scales[j]) for j in range(3)] for i in range(3)]
    K=[row[1:] for row in G[1:]];rho=solve(K,G[0][1:])
    ell=G[0][0]-sum((G[0][j+1]*rho[j] for j in range(2)),F(0))
    assert ell>0 and K[0][1]==K[1][0]==0 and K[0][0]>0 and K[1][1]>0
    nu=F(old['constant_rational_scale']);no=F(three['odd_rational_scale'])
    coeff=[I(x) for x in v];coeff[0]-=rho[0]*nu*sqrt_rational(D);coeff[1]-=rho[1]*no*sqrt_rational(D/3)
    nativeweak=[sum((Q[i][j]*coeff[j] for j in range(112)),I(0)) for i in range(112)]
    GR=[[I(0) for _ in range(3)] for _ in range(3)]
    for i in range(2):
        for j in range(2):GR[i][j]=read(old['actual_retained_source_gram'][i][j])
    GR[2][2]=read(three['odd_projected_source_norm_squared'])
    beta=F(three['whole_mixed_source_cross_bound']);GR[0][2]=GR[2][0]=I(-beta,beta)
    weak=[F(1),-rho[0],-rho[1]];sourceweak=quad(GR,weak)
    GZ=[[read(x) for x in row] for row in old['trial_action_gram']]
    V=[read(row[0])-rho[0]*read(row[1]) for row in old['mixed_trial_action']]
    # Odd trial/source action pairings vanish under the ORIGINAL reflection.
    t=solve_midpoint(GZ,V)
    det=GZ[0][0]*GZ[1][1]-GZ[0][1]*GZ[1][0];assert det.lo>0
    maxcredit=(GZ[1][1]*V[0]*V[0]-2*GZ[0][1]*V[0]*V[1]+GZ[0][0]*V[1]*V[1])/det
    minimum_residual=sourceweak-maxcredit
    residual=sourceweak-2*sum((t[i]*V[i] for i in range(2)),I(0))+quad(GZ,t)
    assert minimum_residual.lo>0 and residual.hi>=minimum_residual.lo
    # Complete source-native trial rows, freshly repeated independently.
    P=shifted_legendre(114);norms=[sqrt_rational(F(2*j+1)/D) for j in range(115)]
    rows=[];errors=[];audits=0
    for trial,n in enumerate((112,114)):
        nz=midpoint(norms[n]);p=[nz*x for x in P[n]]
        print('CC12 full trial row source',n,file=sys.stderr,flush=True)
        regs,e,pi,geom=source(p,abs(nz),n*(n+1)*abs(nz));errors.append(e)
        degree=max(len(r) for r in regs)-1+114
        prim=[primitives(x,degree) for x in geom['cuts']];mom=[I(0) for _ in range(115)]
        h1=[];harm=F(0)
        for k in range(229):
            a=k+1;harm+=F(1,a);h1.append(I((F(1,a*a)+harm/a)/2))
        for panel,(a,b) in enumerate(zip(prim,prim[1:])):
            print('CC12 trial panel',n,panel,file=sys.stderr,flush=True)
            mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
            mm=[I(max(0,x.lo),x.hi) for x in mm]
            for k in range(115):mom[k]+=dot(regs[panel],mm[k:])
        for k in range(115):mom[k]+=dot(p,h1[k:])
        row=[I(0) for _ in range(112)]
        for k in range(0,112,2):
            row[k]=D*norms[k]*dot(P[k],mom)+I(-e,e)
            if trial==0:
                previous=data['cc3']['even_projection_pairings'][k//2]['trial']
                assert max(row[k].lo,F(previous[0]))<=min(row[k].hi,F(previous[1]));audits+=1
        hpair=sum((v[k]*row[k] for k in range(0,112,2)),I(0))
        upair=nu*sqrt_rational(D)*row[0]
        for got,savedpair in ((hpair,old['mixed_trial_native'][trial][0]),(upair,old['mixed_trial_native'][trial][1])):
            prev=read(savedpair);assert max(got.lo,prev.lo)<=min(got.hi,prev.hi);audits+=1
        for j,m in enumerate((112,114)):
            mass=D*midpoint(norms[m])**2/(2*m+1)
            got=D*midpoint(norms[m])*dot(P[m],mom)+I(-e*sqrt_rational(mass).hi,e*sqrt_rational(mass).hi)
            prev=read(old['trial_native_gram'][j][trial])
            assert max(got.lo,prev.lo)<=min(got.hi,prev.hi);audits+=1
        rows.append(row)
    correlated=[compact(nativeweak[k]-sum((t[i]*rows[i][k] for i in range(2)),I(0))) for k in range(112)]
    old_allowance=normupper(nativeweak)+M*sqrt_rational(sourceweak.hi).hi/c
    residual_allowance=normupper(correlated)+M*sqrt_rational(residual.hi).hi/c
    old_budget=old_allowance**2/ell;new_budget=residual_allowance**2/ell
    templatefloor=M*M*minimum_residual.lo/(c*c*ell)
    # A definite physical remainder vector orthogonal to h,u,o1, not a trial
    # source-prefix or an assumed lower bound on the entire remainder.
    hm=sum((v[j]**2 for j in range(2,112)),F(0));assert hm>v[2]**2
    r=[F(0),F(0)]+[F(j==2)-v[2]*v[j]/hm for j in range(2,112)]
    rm=sum((x*x for x in r),F(0));assert rm>0 and sum((r[j]*v[j] for j in range(112)),F(0))==0
    qr=sum((r[i]*Q[i][j]*r[j] for i in range(112) for j in range(112)),I(0))/rm
    assert qr.lo>0 and templatefloor>qr.hi
    return {'stage':'CC12 quantitative critical-reaction integration','classification':'C',
        'aperture':'21/20','plane_used':'CC10 original h,u,odd1; CC11 preserved',
        'three_plane_deterministic_lower':[[str(x) for x in row] for row in G],
        'scaled_whole_row_radius':str(pad),'three_plane_strong_metric':[[str(x) for x in row] for row in K],
        'recomputed_weak_shear':list(map(str,rho)),'recomputed_weak_margin':str(ell),
        'weak_source_norm_squared':bracket(sourceweak),
        'original_trial_action_gram':old['trial_action_gram'],'weak_trial_action_cross':list(map(bracket,V)),
        'original_trial_coefficients':list(map(str,t)),
        'minimum_residual_in_two_trial_action_span':bracket(minimum_residual),
        'actual_trial_residual_norm_squared':bracket(residual),
        'native_row_storage_grid_digits':100,
        'whole_112_trial_native_rows':[[bracket(compact(x)) for x in row] for row in rows],
        'whole_112_correlated_trial_native_weak_row':list(map(bracket,correlated)),
        'correlated_trial_native_weak_row_norm_upper':str(normupper(correlated)),
        'complete_retained_source_map_upper':str(M),'original_complement_lower':str(c),
        'recomputed_absolute_weak_row_allowance':str(old_allowance),
        'correlated_residual_weak_row_allowance':str(residual_allowance),
        'recomputed_absolute_weak_reaction_budget':str(old_budget),
        'correlated_residual_weak_reaction_budget':str(new_budget),
        'any_two_trial_absolute_residual_template_budget_floor':str(templatefloor),
        'physical_109_quotient_test_vector':list(map(str,r)),'quotient_test_mass':str(rm),
        'quotient_native_rayleigh_upper_for_exact_schur':bracket(qr),
        'two_trial_absolute_residual_template_cannot_close_quotient':True,
        'new_whole_matrix_sign':False,'nonpositive_dimension_upper_preserved':107,
        'whole_domain_aperture_preserved':'1','arithmetic_nondivergence':False,
        'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,'source_row_errors':list(map(str,errors)),
        'independent_trial_row_overlap_audits':audits,'full_binary_source_gram_replayed':False,'lean_certified':False,
        'input_sha256':{**{k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()},'native':hashlib.sha256(raw).hexdigest()},
        'displays':{'recomputed_three_plane_weak_margin':float(ell),'recomputed_shears':list(map(float,rho)),
            'minimum_residual_lower':float(minimum_residual.lo),'actual_residual_source_fraction_upper':float(residual.hi/sourceweak.lo),
            'correlated_native_row_norm_upper':float(normupper(correlated)),
            'old_absolute_weak_budget':float(old_budget),'new_correlated_residual_weak_budget':float(new_budget),
            'any_two_trial_template_budget_floor':float(templatefloor),'quotient_native_rayleigh_upper':float(qr.hi)}}

if __name__=='__main__':
    result=compute()
    (ROOT/'notes/data/RPB108_QUANTITATIVE_BRIDGE_CC12_CERTIFICATE_20261008.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['displays'],indent=2));print('classification',result['classification'])
