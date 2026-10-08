"""Three complete original odd sources; one mixed five-retained Schur test."""
from certify_native_odd_enlargement_cc10 import source_odd,read_interval
from certify_native_coupled_trial_cc3 import *
from certify_native_two_trial_solve_cc8 import midpoint
from validate_native_two_trial_solve_cc8 import solve
sys.set_int_max_str_digits(0)

def rational_ldl(A):
    n=len(A);L=[[F(i==j) for j in range(n)] for i in range(n)];p=[]
    for j in range(n):
        pivot=A[j][j]-sum((L[j][k]**2*p[k] for k in range(j)),F(0));p.append(pivot)
        if pivot<=0:return p,False
        for i in range(j+1,n):
            L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*p[k] for k in range(j)),F(0)))/pivot
    return p,True

def compute():
    oldpath=ROOT/'notes/data/RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json'
    old=json.loads(oldpath.read_bytes())
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
    degrees=[1,3,5];scales=[midpoint(norms[n]) for n in degrees]
    polys=[[s*x for x in P[n]] for s,n in zip(scales,degrees)]
    masses=[D*s*s/(2*n+1) for s,n in zip(scales,degrees)]
    regs=[];errors=[]
    for n,s,p in zip(degrees,scales,polys):
        print('CC11 source',n,file=sys.stderr,flush=True)
        r,e,pi,geom=source_odd(p,abs(s),n*(n+1)*abs(s));regs.append(r);errors.append(e)
    degree=max(len(row) for rows in regs for row in rows)*2-2
    print('CC11 primitives',degree,file=sys.stderr,flush=True)
    prim=[primitives(t,degree) for t in geom['cuts']]
    moments=[[I(0) for _ in range(112)] for _ in range(3)]
    gram=[[I(0) for _ in range(3)] for _ in range(3)]
    h1=[];h2=[];harm=F(0);harm2=F(0)
    for k in range(122):
        n=k+1;harm+=F(1,n);harm2+=F(1,n*n)
        h1.append(I((F(1,n*n)+harm/n)/2))
        h2.append(I((F(2,n**3)+(harm*harm+harm2)/n+2*harm/n**2+2*harm2/n)/4)-pi*pi/(12*n))
    for i in range(3):
        for j in range(i,3):gram[i][j]+=dot(mul(polys[i],polys[j]),h2)
    for panel,(a,b) in enumerate(zip(prim,prim[1:])):
        print('CC11 panel',panel,file=sys.stderr,flush=True)
        mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
        lm=[b[1][k]-a[1][k] for k in range(degree+1)]
        mm=[I(max(0,x.lo),x.hi) for x in mm];lm=[I(max(0,x.lo),x.hi) for x in lm]
        for i in range(3):
            for k in range(112):moments[i][k]+=dot(regs[i][panel],mm[k:])
            for j in range(i,3):
                gram[i][j]+=dot(mul(regs[i][panel],regs[j][panel]),mm)
                gram[i][j]+=dot(add(mul(polys[i],regs[j][panel]),mul(polys[j],regs[i][panel])),lm)
    for i in range(3):
        for k in range(112):moments[i][k]+=dot(polys[i],h1[k:])
    coarse=[F(10**8)*(1+abs(s)) for s in scales];projected=[];audits=0
    coeff=[s*sqrt_rational(D/F(2*n+1)) for s,n in zip(scales,degrees)]
    for i,n in enumerate(degrees):
        row=[]
        for k in range(1,112,2):
            x=D*norms[k]*dot(P[k],moments[i])+I(-errors[i],errors[i])
            audit=coeff[i]*Q[k][n]
            assert max(x.lo,audit.lo)<=min(x.hi,audit.hi),('odd native',n,k)
            row.append(x);audits+=1
        projected.append(row)
    for i in range(3):
        for j in range(i,3):
            budget=errors[i]*coarse[j]+errors[j]*coarse[i]+errors[i]*errors[j]
            x=D*gram[i][j]+I(-budget,budget)
            x-=sum((a*b for a,b in zip(projected[i],projected[j])),I(0))
            gram[i][j]=gram[j][i]=x
    nativeblock=[[None]*3 for _ in range(3)];symmetry=0
    for i,n in enumerate(degrees):
        for j in range(i,3):
            a=D*dot(polys[i],moments[j])+I(-errors[j]*sqrt_rational(masses[i]).hi,errors[j]*sqrt_rational(masses[i]).hi)
            b=D*dot(polys[j],moments[i])+I(-errors[i]*sqrt_rational(masses[j]).hi,errors[i]*sqrt_rational(masses[j]).hi)
            savedentry=coeff[i]*coeff[j]*Q[n][degrees[j]]
            assert max(a.lo,b.lo,savedentry.lo)<=min(a.hi,b.hi,savedentry.hi);symmetry+=1
            nativeblock[i][j]=nativeblock[j][i]=I(min(a.lo,b.lo,savedentry.lo),max(a.hi,b.hi,savedentry.hi))
    c=F(old['complement_lower']);oddmass=F(old['odd_original_witness_mass'])
    oddlower=[[nativeblock[i][j]-gram[i][j]/c for j in range(3)] for i in range(3)]
    cross=[];budgets=[]
    for i,n in enumerate(degrees):
        assert gram[i][i].hi>=0
        beta=8*sqrt_rational(oddmass*gram[i][i].hi).hi;budgets.append(beta)
        nativecross=coeff[i]*sum((v[j]*Q[j][n] for j in range(1,112,2)),I(0))
        cross.append(nativecross+I(-beta/c,beta/c))
    lower=[[I(0) for _ in range(5)] for _ in range(5)]
    for i in range(2):
        for j in range(2):lower[i][j]=read_interval(old['original_completed_schur_lower_block'][i][j])
    for i in range(3):
        lower[0][i+2]=lower[i+2][0]=cross[i]
        for j in range(3):lower[i+2][j+2]=oddlower[i][j]
    # Rescale the weak coordinate before paying a WHOLE row-radius allowance.
    # Undo the congruence for the physical metric; no entrywise-lower substitution.
    coordscale=[F(10**16),F(1),F(1),F(1),F(1)]
    scaled=[[lower[i][j]*coordscale[i]*coordscale[j] for j in range(5)] for i in range(5)]
    # A 100-digit rational centre keeps the finite inverse compact. Include
    # its rounding in each radius, then round the whole allowance UP.
    finitegrid=10**100
    centre=[[F((midpoint(x)*finitegrid).__floor__(),finitegrid) for x in row] for row in scaled]
    radius=max(sum((max(centre[i][j]-x.lo,x.hi-centre[i][j]) for j,x in enumerate(row)),F(0)) for i,row in enumerate(scaled))
    epsilon=F((radius*finitegrid).__ceil__(),finitegrid)
    G=[[centre[i][j]-(epsilon if i==j else 0) for j in range(5)] for i in range(5)]
    pivots,positive=rational_ldl(G)
    result={'stage':'CC11 complete mixed odd batch','aperture':'21/20','odd_degrees':degrees,
        'odd_rational_scales':list(map(str,scales)),'odd_masses':list(map(str,masses)),
        'odd_source_errors':list(map(str,errors)),'integration_degree':degree,
        'odd_native_pairing_audits':audits,'odd_native_symmetry_overlap_audits':symmetry,
        'odd_native_block':[[bracket(x) for x in row] for row in nativeblock],
        'complete_projected_odd_source_gram':[[bracket(x) for x in row] for row in gram],
        'odd_schur_lower_block':[[bracket(x) for x in row] for row in oddlower],
        'whole_witness_odd_source_cross_bounds':list(map(str,budgets)),
        'original_completed_schur_lower_block':[[bracket(x) for x in row] for row in lower],
        'coordinate_congruence_scales':list(map(str,coordscale)),
        'finite_matrix_grid_digits':100,'whole_scaled_row_radius':str(epsilon),'deterministic_scaled_lower_matrix':[[str(x) for x in row] for row in G],
        'exact_ldl_pivots':list(map(str,pivots)),'five_retained_plane_positive':positive,
        'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,'whole_complement_retained':True,
        'full_112_retained_sign':False,'whole_aperture_positive':False,'lean_certified':False,
        'input_sha256':{'cc9':hashlib.sha256(oldpath.read_bytes()).hexdigest(),
                        'saved_target':hashlib.sha256(savedpath.read_bytes()).hexdigest(),'native':hashlib.sha256(raw).hexdigest()},
        'displays':{'odd_lower_matrix':[[float(x.lo) for x in row] for row in oddlower],
                    'scaled_row_radius':float(epsilon),'ldl_pivots':list(map(float,pivots))}}
    if positive:
        inverse=[solve(G,[F(i==j) for i in range(5)]) for j in range(5)]
        traceinverse=sum((coordscale[i]**2*inverse[i][i] for i in range(5)),F(0))
        masstrace=sum(map(F,old['retained_masses']),F(0))+sum(masses,F(0))
        tau=1/(traceinverse*masstrace);mu=min(tau/266,c/2);canonical=mu/(10*(mu+26))
        O=[row[2:] for row in G[2:]];opiv,opos=rational_ldl(O);assert opos
        oi=[solve(O,[F(i==j) for i in range(3)]) for j in range(3)]
        otrace=sum((oi[i][i] for i in range(3)),F(0))
        ell=G[0][0]/coordscale[0]**2-(G[0][1]/coordscale[0])**2/G[1][1]
        crossnorm2=sum((max(abs(x.lo),abs(x.hi))**2 for x in cross),F(0))
        relativebudget=crossnorm2*otrace/ell
        # The SAME original parity also bounds the complete weak mixed row
        # on ALL 56 odd retained coordinates, without inventing their sign.
        nativeoddrow=[sum((v[j]*Q[k][j] for j in range(1,112,2)),I(0)) for k in range(1,112,2)]
        nativeoddnorm=sqrt_rational(sum((max(abs(x.lo),abs(x.hi))**2 for x in nativeoddrow),F(0))).hi
        wholesourcerow=64*sqrt_rational(oddmass).hi/c
        wholeoddrownorm=nativeoddnorm+wholesourcerow
        wholeoddplanereaction=wholeoddrownorm**2/ell
        result.update(protected_slice_codimension=107,slice_retained_physical_margin=str(tau),
            whole_infinite_slice_physical_margin=str(mu),whole_infinite_slice_canonical_margin=str(canonical),
            original_nonpositive_spectral_dimension_upper=107,odd_block_inverse_trace=str(otrace),
            weak_plane_lower_margin=str(ell),odd_batch_relative_weak_reaction_upper=str(relativebudget),
            entire_56_odd_native_weak_row=[bracket(x) for x in nativeoddrow],
            entire_56_odd_native_weak_row_norm_upper=str(nativeoddnorm),
            entire_56_odd_completed_weak_row_norm_upper=str(wholeoddrownorm),
            entire_56_odd_plane_inverse_reaction_allowance=str(wholeoddplanereaction),
            entire_56_odd_block_positive_claimed=False)
        result['displays'].update(physical_slice_margin=float(mu),canonical_slice_margin=float(canonical),
            odd_batch_relative_weak_reaction_upper=float(relativebudget),
            entire_56_odd_completed_weak_row_norm_upper=float(wholeoddrownorm),
            entire_56_odd_plane_inverse_reaction_allowance=float(wholeoddplanereaction))
    return result

if __name__=='__main__':
    result=compute()
    (ROOT/'notes/data/RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['displays'],indent=2));print('five_retained_plane_positive',result['five_retained_plane_positive'])
