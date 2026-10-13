"""RC172: actual P2 regular carrier and correlated P0/P2 canonical interface."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,up,down,sqrtup,psd,ser,loewner

def replace_once(src,old,new):
    assert src.count(old)==1
    return src.replace(old,new,1)

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];prior,regular,audit,metric,joint=map(json.loads,raw)
    assert [d['milestone'] for d in (prior,regular,audit,metric,joint)]==['RC171','RC170','RC169','RC121','RC129']
    hs=[hashlib.sha256(b).hexdigest() for b in raw];assert prior['input_sha256']==hs[1:]
    source=Path(__file__).with_name('validate_rpb108_rc171_regular_legendre_projection.py')
    src=source.read_text().split("\nif __name__=='__main__':")[0]
    src=replace_once(src,"    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)","    return locals()")
    src=replace_once(src,'for n in range(1,N+1):','for n in range(1,N+3):')
    old="""        a0=scale(1/p,sub(scale(-4,q0[1]),scale(2*h,q0[0])))
        low[0]=add(low[0],mul(wr,a0))
        for n in range(2,N+1,2):low[n]=add(low[n],mul(minusWeight,sub(qs[n+1][1],qs[n-1][1])))"""
    new="""        f=[ZERO for _ in range(N+3)];ell=[ZERO for _ in range(N+2)]
        f[0]=scale(1/p,sub(scale(-4,q0[1]),scale(2*h,q0[0])))
        for n in range(2,N+3,2):f[n]=scale(-2/p,sub(qs[n+1][1],qs[n-1][1]))
        for n in range(1,N+2,2):ell[n]=scale(4,sub(qs[n+1][0],qs[n-1][0]))
        for n in range(0,N+1,2):
            middle=F((n+1)**2,(2*n+1)*(2*n+3))+(F(n*n,(2*n+1)*(2*n-1)) if n else 0)
            u2=add(scale(middle,f[n]),scale(F((n+2)*(n+1),(2*n+5)*(2*n+3)),f[n+2]))
            if n>=2:u2=add(u2,scale(F(n*(n-1),(2*n-1)*(2*n-3)),f[n-2]))
            uell=scale(F(n+1,2*n+3),ell[n+1])
            if n>=2:uell=add(uell,scale(F(n,2*n-1),ell[n-1]))
            g=add(sub(scale(F(3,2),u2),scale(F(1,2)+F(3,2)*h*h,f[n])),scale(3*h/(2*p),uell))
            if n==0:g=add(g,rat(3*h/p))
            low[n]=add(low[n],mul(wr,g))"""
    src=replace_once(src,old,new)
    src=replace_once(src,'farRemainder+=up(weight*2*(2*c)**65/(65*p))','farRemainder+=up(weight*(2*c)**65/p)')
    old='        for j in range(0,2*k+2,2):poly[j]=add(poly[j],scale(F(2*(-1)**k*math.comb(2*k+1,j),(2*k+1)*p),moment))'
    new="""        for j in range(0,2*k+1,2):
            degree=2*k-j;inputMoment=F(3,degree+3)-F(1,degree+1)
            poly[j]=add(poly[j],scale(F((-1)**k*math.comb(2*k,j),p)*inputMoment,moment))"""
    src=replace_once(src,old,new)
    ns={'__file__':str(source)};exec(compile(src,'RC172 paid P2 Poisson reconstruction','exec'),ns)
    d=ns['run'](paths[1:],replay);endpoints=ns['endpoints'];rat=ns['rat'];divide=ns['divide'];sub=ns['sub']
    N=d['N'];low=d['low'];p=d['p'];weights=d['weights']
    assert d['d']['coefficientHash'].hexdigest()==regular['node_coefficient_center_sha256']
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    entries=[];Hn=F(0);roundSquared=F(0);physicalRound=F(0)
    for n in range(N+1):
        if n:Hn+=F(1,n)
        if n%2:continue
        lo,hi=endpoints(low[n]);assert hi-lo<F(1,10**30)
        center=(lo+hi)/2;radius=(hi-lo)/2;dl,dh=sl+Hn,sh+Hn
        al,ah=endpoints(divide(rat(center),(rat(dl)[0],rat(dh)[1])));trial=(al+ah)/2;ar=(ah-al)/2;m=2*B/F(2*n+1)
        roundSquared+=m*dh*ar*ar;physicalRound+=m*radius*radius
        entries.append(dict(degree=n,represented_regular_source_coefficient_lower=str(lo),represented_regular_source_coefficient_upper=str(hi),D_inverse_trial_coefficient=str(trial)))
    phase=up(4*d['piError']/F(regular['pi_lower'])*weights);far=up(d['farRemainder']);epsilon=F(regular['supported_physical_L2_operator_error_norm_upper'])
    m0=2*B;m2=2*B/5
    physicalError=up(sqrtup(m2)*(epsilon+phase)+sqrtup(m0)*far+sqrtup(physicalRound))
    rootSl=sqrtup(sl)-F(1,10**40);assert rootSl>0 and rootSl*rootSl<=sl
    projectedError=up(physicalError/rootSl+sqrtup(roundSquared))
    I2=up(F(regular['e_upper'])*F(regular['pi_upper'])**2/3);r=F(789,125);assert 4*B*I2<r*r
    derivativeNorm=up(r*sqrtup(6/B)+sqrtup(2*I2))
    differentialNorm=up(2*B*derivativeNorm+3*r*sqrtup(2*B)+6*B*sqrtup(I2)+4*F(regular['e_upper'])*B*sqrtup(2*B))
    Hnext=Hn+F(1,N+1)+F(1,N+2);z=(N+2)*(N+3)
    tailSquared=up(differentialNorm**2/(z*z*(sl+Hnext)));regularSquared=up(projectedError**2+tailSquared);regularError=sqrtup(regularSquared)
    log2=ns['log_point'](F(2));ll,lh=endpoints(log2)
    ep0=endpoints(divide(rat(F(1,6)),(rat(sl)[0],rat(sh)[1])))
    ep2=endpoints(divide(sub(rat(F(41,30)-r),log2),(rat(sl+F(3,2))[0],rat(sh+F(3,2))[1])))
    c0,c2=(ep0[0]+ep0[1])/2,(ep2[0]+ep2[1])/2
    endpointError=up(sqrtup(m0*sh)*(ep0[1]-ep0[0])/2+sqrtup(m2*(sh+F(3,2)))*(ep2[1]-ep2[0])/2)
    actionError=up(regularError+endpointError);assert actionError<F(1,1500)
    # Independent self-adjoint cross check, in two different action columns.
    old2=prior['physical_regular_coefficient_enclosures'][1];assert old2['degree']==2
    a,b=F(old2['represented_regular_source_coefficient_lower'])/5,F(old2['represented_regular_source_coefficient_upper'])/5
    c,e=endpoints(low[0]);crossLo,crossHi=max(a,c),min(b,e);assert crossLo<=crossHi
    crossRadius=up(sqrtup(m0*m2)*(epsilon+phase)+m0*far)
    q22lo,q22hi=endpoints(low[2]);diagRadius=up(m2*(epsilon+phase)+sqrtup(m0*m2)*far)
    entryLo=[[F(prior['actual_canonical_constant_direction_Gram_lower']),down(m0*F(1,6)+m0*crossLo-crossRadius)],
      [down(m0*F(1,6)+m0*crossLo-crossRadius),down(m2*(sl+F(3,2)+F(41,30)-lh-r+q22lo)-diagRadius)]]
    entryHi=[[F(prior['actual_canonical_constant_direction_Gram_upper']),up(m0*F(1,6)+m0*crossHi+crossRadius)],
      [up(m0*F(1,6)+m0*crossHi+crossRadius),up(m2*(sh+F(3,2)+F(41,30)-ll-r+q22hi)+diagRadius)]]
    w=[sqrtup(entryHi[i][i]) for i in range(2)];Glo,Ghi,_=loewner(entryLo,entryHi,w)
    floor=[[m0*F(257,252),F(0)],[F(0),m2*F(257,252)]]
    assert psd(Glo) and psd([[Ghi[i][j]-Glo[i][j] for j in range(2)] for i in range(2)])
    assert psd([[Glo[i][j]-floor[i][j] for j in range(2)] for i in range(2)])
    eps0=F(prior['canonical_constant_action_D_error_norm_upper']);errorUpper=[[2*eps0**2,F(0)],[F(0),2*actionError**2]]
    Dlo=[[m0*sl,F(0)],[F(0),m2*(sl+F(3,2))]]
    beta=up(max(errorUpper[i][i]/Dlo[i][i] for i in range(2)))
    assert psd([[beta*Dlo[i][j]-errorUpper[i][j] for j in range(2)] for i in range(2)])
    return dict(milestone='RC172',status='PASS: P2 regular carrier and full correlated P0/P2 canonical action interface',starting_commit='413d3701d582271bd3e318790b1be58e985f8047',input_sha256=hs,aperture='11/10',
      physical_input='P2(x/B)=(3*(x/B)^2-1)/2',maximum_even_trial_degree=N,first_omitted_even_degree=N+2,
      physical_regular_coefficient_enclosures=entries,near_Poisson_node_count=d['nearCount'],far_Poisson_node_count=d['farCount'],
      far_kernel_source_uniform_error_upper=str(far),Poisson_pi_replacement_operator_error_upper=str(phase),
      regular_source_derivative_norm_upper=str(derivativeNorm),regular_source_Legendre_differential_norm_upper=str(differentialNorm),
      projected_regular_action_D_error_norm_upper=str(projectedError),full_omitted_D_inverse_regular_source_energy_upper=str(tailSquared),
      full_D_inverse_regular_P2_error_norm_upper=str(regularError),canonical_P2_action_D_error_norm_upper=str(actionError),
      endpoint_P0_coefficient_center=str(c0),endpoint_P2_correction_center=str(c2),endpoint_finite_coefficient_error_norm_upper=str(endpointError),
      endpoint_P2_tail_definition='xi2_n=(2*n+1)/[(H_n+s)*(n*(n+1)-6)] for even n>=4; zero otherwise',
      canonical_P2_action_representation='(1+endpoint_P2_correction_center)*P2+endpoint_P0_coefficient_center*P0+xi2+regular_D_inverse_P2_polynomial',
      independent_selfadjoint_cross_pairing_intersection_lower=str(crossLo),independent_selfadjoint_cross_pairing_intersection_upper=str(crossHi),
      two_source_canonical_Gram_entry_lower=ser(entryLo),two_source_canonical_Gram_entry_upper=ser(entryHi),two_source_canonical_Gram_Loewner_lower=ser(Glo),two_source_canonical_Gram_Loewner_upper=ser(Ghi),
      two_source_canonical_action_error_Gram_upper=ser(errorUpper),two_source_D_Gram_lower=ser(Dlo),two_source_action_error_relative_squared_factor_upper=str(beta),
      all_real_and_complex_two_source_mixtures_paid=True,mixed_action_error_orthogonality_assumed=False,
      native_seven_source_frame_changed=False,full_seven_source_canonical_action_realized=False,canonical_Riesz_iteration_performed=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='use the polynomial-source Poisson projection construction on the required finite source family, retaining full correlated errors and every endpoint/regular carrier tail')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=5)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC172 PASS: P2 regular carrier and correlated canonical action')
