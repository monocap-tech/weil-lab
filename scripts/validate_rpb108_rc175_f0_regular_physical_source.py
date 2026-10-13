"""RC175: actual compressed f0 regular source and signed canonical mixed rows."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math
from validate_rpb108_rc127_enriched_even_endpoint_action import B,up,down,sqrtup
from validate_rpb108_rc171_regular_legendre_projection import ZERO,rat,add,sub,mul,scale,divide,div_int,endpoints,pi_bounds,atan,log_point,double_factorial

def root_lower(x):
    v=sqrtup(x)-F(1,10**40);assert v>0 and v*v<=x
    return v

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];prior,p2,p0,regular,audit,metric,joint=map(json.loads,raw)
    assert [d['milestone'] for d in (prior,p2,p0,regular,audit,metric,joint)]==['RC174','RC172','RC171','RC170','RC169','RC121','RC129']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert prior['input_sha256'][1]==hs[4] and prior['input_sha256'][4:]==hs[3:4]+hs[5:]
    assert p2['input_sha256']==hs[2:] and p0['input_sha256']==hs[3:]
    assert regular['input_sha256']==[hs[4],hs[5]]
    budget=prior['f0_finite_input_component_budgets'][0];assert budget['requested_component_D_error_norm']=='1/10000'
    M=budget['smallest_even_input_degree_for_this_bound'];assert M==172
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    harmonic=F(0);actual={};centers={};inputRows=[];prefixEnergy=F(0);centerEnergy=F(0);tailEnergy=F(0)
    for n in range(1,989):
        harmonic+=F(1,n)
        if n%2:continue
        a=divide(rat(F(2*n+1,n*(n+1))),(rat(sl+harmonic)[0],rat(sh+harmonic)[1]));lo,hi=endpoints(a);actual[n]=a
        mass=2*B/F(2*n+1)
        if n<=M:
            c=(lo+hi)/2;radius=(hi-lo)/2;centers[n]=c;prefixEnergy+=mass*c*c;centerEnergy+=mass*radius*radius
            inputRows.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(radius)))
        else:tailEnergy+=up(mass*hi*hi)
    inputSup=sum(abs(c) for c in centers.values())
    digest=hashlib.sha256(json.dumps(inputRows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    source=Path(__file__).with_name('validate_rpb108_rc170_poisson_regular_action.py')
    src=source.read_text().split("\nif __name__=='__main__':")[0]
    target='    pi=pi_bounds();pl,ph=bounds(pi);assert F(3)<pl<ph<F(22,7)';assert src.count(target)==1
    src=src.replace(target,'    return locals()',1);ns={};exec(compile(src,'RC170 node reconstruction','exec'),ns)
    d=ns['run']([paths[4],paths[5]]);nodes=d['nodes'];delta=d['delta']
    assert d['coefficientHash'].hexdigest()==regular['node_coefficient_center_sha256']
    p=(F(regular['pi_lower'])+F(regular['pi_upper']))/2
    piError=max(p-F(regular['pi_lower']),F(regular['pi_upper'])-p);pi=pi_bounds()
    # Exact input moments through degree 62 suffice for all far-node terms.
    inputMom=[]
    for j in range(0,63,2):
        moment=F(0)
        for n in range(2,min(M,j)+1,2):
            factor=F(2*math.factorial(j),double_factorial(j-n)*double_factorial(j+n+1))
            moment+=centers[n]*factor
        inputMom.append(moment)
    xs=[F(0),F(1,2),F(1)];values={u:ZERO for u in xs};farMom=[ZERO for _ in range(32)]
    weights=F(0);farRemainder=F(0);nearCount=farCount=0;ar={n:rat(c) for n,c in centers.items()}
    order=nodes[::-1] if replay else nodes
    for tc,ac in order:
        weight=delta*ac;weights+=weight;c=2*p*B/tc
        if c<F(1,4):
            power=rat(c);square=rat(c*c)
            for k in range(32):farMom[k]=add(farMom[k],scale(weight,power));power=mul(power,square)
            farRemainder+=up(weight*(2*c)**65/p);farCount+=1;continue
        h=1/c;hr=rat(h);wr=rat(-2*weight/p)
        for u in xs:
            real=ZERO if u==0 else scale(F(1,4),log_point(((u+1)**2+h*h)/((u-1)**2+h*h)))
            imag=scale(F(-1,2),add(atan((1-u)/h,pi),atan((1+u)/h,pi)))
            qprev=(real,imag)
            q=(sub(sub(scale(u,real),mul(hr,imag)),rat(1)),add(scale(u,imag),mul(hr,real)))
            total=ZERO
            for n in range(1,M):
                zq=(sub(scale(u,q[0]),mul(hr,q[1])),add(scale(u,q[1]),mul(hr,q[0])))
                qnext=tuple(div_int(sub(scale(2*n+1,zq[i]),scale(n,qprev[i])),n+1) for i in range(2))
                if (n+1)%2==0:total=add(total,mul(ar[n+1],qnext[1]))
                qprev,q=q,qnext
            values[u]=add(values[u],mul(wr,total))
        nearCount+=1
        if nearCount%512==0:print('RC175 signed f0 physical-source node block',nearCount,flush=True)
    # Far operator is the same symmetric degree-62 kernel polynomial used
    # for the historical P0/P2 columns. Its rational output is explicit.
    poly=[ZERO for _ in range(63)]
    for k,g in enumerate(farMom):
        for j in range(0,2*k+1,2):
            factor=F((-1)**k*math.comb(2*k,j),p)*inputMom[(2*k-j)//2]
            poly[j]=add(poly[j],scale(factor,g))
    farRows=[];farPoly={};farRound=F(0)
    for j in range(0,63,2):
        lo,hi=endpoints(poly[j]);c=(lo+hi)/2;radius=(hi-lo)/2;farPoly[j]=c;farRound+=radius
        farRows.append(dict(power=j,coefficient_center=str(c),coefficient_radius=str(radius)))
    for u in xs:
        for j,c in farPoly.items():values[u]=add(values[u],rat(c*u**j))
    ep=F(regular['e_upper']);pu=F(regular['pi_upper']);I2=up(ep*pu*pu/3);r=F(789,125);assert 4*B*I2<r*r
    band=F(M+1)/(6*pu*B);rem2=up(F(11,12)**(2*(M+1)),10**80)
    smoothing=up(min(r*r,4*B*I2*rem2+ep*ep/(band*band)))
    tailPhysical=sqrtup(smoothing*tailEnergy);centerPhysical=up(r*sqrtup(centerEnergy))
    phase=up(4*piError/F(regular['pi_lower'])*weights)
    quad=F(regular['supported_physical_L2_operator_error_norm_upper']);quadSup=F(regular['supported_physical_Linfinity_operator_error_norm_upper'])
    farError=up(inputSup*farRemainder+farRound)
    physicalError=up(tailPhysical+centerPhysical+(quad+phase)*sqrtup(prefixEnergy)+sqrtup(2*B)*farError)
    Derror=up(physicalError/root_lower(sl));assert Derror<F(12,10**5)
    uniformError=up(sqrtup(2*I2)*(sqrtup(tailEnergy)+sqrtup(centerEnergy))+(quadSup+phase)*inputSup+farError)
    samples=[]
    for u in xs:
        lo,hi=endpoints(values[u]);assert hi-lo<F(1,10**30)
        samples.append(dict(x=str(B*u),represented_value_lower=str(lo),represented_value_upper=str(hi),actual_Rf0_value_lower=str(down(lo-uniformError)),actual_Rf0_value_upper=str(up(hi+uniformError))))
    # Self-adjointness yields retained output coefficients from the two
    # independently paid physical action columns, with identical kernels.
    oldRows=[{r['degree']:r for r in old['physical_regular_coefficient_enclosures']} for old in (p0,p2)]
    output=[];canonicalPairs=[]
    ln2=log_point(F(2));d2=sub(rat(F(41,30)),ln2)
    for i,mode in enumerate([0,2]):
        value=ZERO
        for n in sorted(centers,reverse=replay):
            row=oldRows[i][n];interval=(rat(F(row['represented_regular_source_coefficient_lower']))[0],rat(F(row['represented_regular_source_coefficient_upper']))[1])
            value=add(value,scale(centers[n]*F(2*mode+1,2*n+1),interval))
        lo,hi=endpoints(value);mass=2*B/F(2*mode+1);err=up(physicalError/root_lower(mass))
        trueLo,trueHi=down(lo-err),up(hi+err)
        output.append(dict(degree=mode,represented_regular_coefficient_lower=str(lo),represented_regular_coefficient_upper=str(hi),actual_regular_coefficient_lower=str(trueLo),actual_regular_coefficient_upper=str(trueHi)))
        endpoint=ZERO
        for n in sorted(actual,reverse=replay):
            if mode==0:entry=rat(2*B/F(n*(n+1)))
            elif n==2:entry=scale(2*B/5,d2)
            else:entry=rat(2*B/F(n*(n+1)-6))
            endpoint=add(endpoint,mul(entry,actual[n]))
        pair=add(endpoint,scale(mass,(rat(trueLo)[0],rat(trueHi)[1])))
        if mode==2:pair=add(pair,sub(rat(2*B/6),scale(r*mass,actual[2])))
        pl,ph=endpoints(pair);canonicalPairs.append(dict(source_mode=mode,canonical_mixed_pairing_lower=str(pl),canonical_mixed_pairing_upper=str(ph)))
    formError=up(Derror+F(joint['RC128_Cf0_w_error_paid']))
    return dict(milestone='RC175',status='PASS: represented actual f0 regular physical source and canonical mixed rows',starting_commit='d771d3d3e19cf3604d6fdf27984299c8e0f2f637',input_sha256=hs,aperture='11/10',
      actual_source_definition='f0_n=eta_n for even 2<=n<=988; zero otherwise',retained_input_degree=M,input_coefficient_intervals=inputRows,input_center_sha256=digest,
      physical_input_tail_energy_upper=str(up(tailEnergy)),physical_input_center_error_energy_upper=str(centerEnergy),
      near_Poisson_node_count=nearCount,far_Poisson_node_count=farCount,near_input_profile_definition='-2/pi_kernel*Im sum_even_2<=n<=172 alpha_n Q_n(u+i*t/(2*pi_kernel*B)); Q_n by its exact Cauchy-moment recurrence',
      source_profile_definition='sum_near_nodes delta*a_j*near_input_profile + stored rational far polynomial in u=x/B',far_source_polynomial=farRows,
      far_kernel_and_polynomial_rounding_uniform_error_upper=str(farError),kernel_pi_replacement_operator_error_upper=str(phase),
      complete_physical_Rf0_source_error_norm_upper=str(physicalError),complete_uniform_Rf0_source_error_upper=str(uniformError),
      induced_D_inverse_regular_f0_error_norm_upper=str(Derror),physical_source_samples=samples,retained_regular_output_coefficient_intervals=output,
      actual_canonical_P0_P2_f0_mixed_pairings=canonicalPairs,
      canonical_f0_source_form_trial_definition='f0+w14-r*D^-1*f0+D^-1*(stored represented regular physical source)',canonical_f0_source_form_trial_D_error_norm_upper=str(formError),
      full_regular_physical_source_function_represented=True,actual_native_f0_regular_source_evaluated=True,
      complete_regular_output_Legendre_carrier_realized=False,only_output_modes_zero_and_two_evaluated=True,full_three_source_canonical_Gram_evaluated=False,
      full_seven_source_canonical_inverse_certified=False,canonical_Riesz_iteration_performed=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='project the represented f0 regular source into an actionable finite/analytic carrier with paid output tail, or pay its remaining correlated diagonal/action data before adding f0 to canonical inversion')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=7)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC175 PASS: actual f0 regular physical source and signed canonical mixed rows')
