"""RC179: paid finite focus residual and its complete actual canonical action."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math
from validate_rpb108_rc127_enriched_even_endpoint_action import B,up,down,psd,ser,loewner
from validate_rpb108_rc171_regular_legendre_projection import ZERO,rat,add,sub,mul,scale,divide,div_int,endpoints,log_point
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root,centered

def regular_action(alpha,regular,joint,replay=False):
    # RC176's analytic kernel/Beta/log-moment method, now for an exact
    # finite rational polynomial; there is no regular input-tail error.
    M=max(alpha);K=192;N=768;J=M+K+1;r=F(789,125)
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    harmonic=[F(0)]
    for n in range(1,N+J+2):harmonic.append(harmonic[-1]+F(1,n))
    prefix=sum(2*B*alpha[n]**2/F(2*n+1) for n in alpha)
    a=[sum(alpha[n]*(-1)**l*math.comb(n,l)*math.comb(n+l,l) for n in alpha if n>=l) for l in range(M+1)]
    # Exact parity check: q(1-v)=q(v).
    assert all(a[l]==(-1)**l*sum(a[j]*math.comb(j,l) for j in range(l,M+1)) for l in range(M+1))
    el,eh=F(regular['e_lower']),F(regular['e_upper']);pl,ph=F(regular['pi_lower']),F(regular['pi_upper'])
    ec=(el+eh)/2;pc=(pl+ph)/2;sc=(sl+sh)/2
    lc,lr=centered(log_point(F(2)),10**80);C=1-sc+lc+r;c=4*pc*B*ec
    de=max(ec-el,eh-ec);dp=max(pc-pl,ph-pc);dC=(sh-sl)/2+lr+de/el+dp/pl
    # Row norm integral: split at t=4B, using min(1,4B/t).
    rowbound=4*B*eh+1
    # Replacing the universal pi/2 in the odd series by pc/2 costs
    # at most dp*c/pc, using 1-cos(w)<=w for w>=0.
    parameter=up(de/el+4*rowbound*dp/pl+4*B*ec*dC+dp*c/pc,10**80)
    T=[rat(1)]
    for j in range(1,K+3):T.append(div_int(scale(c,T[-1]),j))
    kernel=[]
    for j in range(K+1):
        if j%2==0:
            f=scale(4*B*ec*F((-1)**(j//2),j+1),T[j])
            kernel.append((scale(harmonic[j+1]-C,f),scale(-1,f)))
        else:kernel.append((scale(F((-1)**((j+3)//2),2),T[j+1]),ZERO))
    trunc=up((4*B*ec+(c/2+4*B*ec*(abs(C)+1))/F(K+2))*F(T[K+1][1])/(1-c/F(K+2)),10**80)
    assert c<K+2 and trunc<F(1,10**50)
    w=[ZERO for _ in range(J+1)];b=[ZERO for _ in range(J+1)]
    # Beta integrals of v^l times the two power/log kernel components.
    for j in (range(K,-1,-1) if replay else range(K+1)):
        A,Q=kernel[j];beta=F(1,j+1)
        for l in range(M+1):
            k=j+l+1;z=a[l]*beta
            w[k]=add(w[k],scale(z,add(A,scale(harmonic[j]-harmonic[k],Q))))
            b[k]=add(b[k],scale(z,Q));beta*=F(l+1,j+l+2)
        if j%48==0:print('RC179 analytic kernel block',j,flush=True)
    rows=[];wc=[F(0)]*(J+1);bc=wc.copy();rounding=F(0)
    for k in range(1,J+1):
        wc[k],wr=centered(w[k],10**80);bc[k],br=centered(b[k],10**80)
        rounding+=2*wr+2*br/F(k)
        rows.append(dict(power=k,polynomial_center=str(wc[k]),polynomial_radius=str(wr),log_center=str(bc[k]),log_radius=str(br)))
    assert rounding<F(1,10**60)
    I2=up(eh*ph*ph/3);band=F(M+1)/(6*ph*B)
    smoothing=up(min(r*r,4*B*I2*up(F(11,12)**(2*(M+1)),10**80)+eh*eh/(band*band)))
    inputTail=F(0)
    center=F(0)
    phys=up(inputTail+r*center+(parameter+trunc)*root(prefix)+root(2*B)*rounding)
    globalD=up(phys/lower_root(sl))
    uniform=up(root(2*I2)*(F(0)+center)+(parameter+trunc)*sum(abs(x) for x in alpha.values())+rounding)
    lowEnergy=F(0);projection=[];sourceRows=[]
    # Exact differentiated beta moments; odd coefficients vanish by parity.
    for n in range(0,N+1,2):
        value=ZERO
        if n:
            lm=F(-2,n*(n+1));jm=F(0)
        else:
            jm=F(2);lm=F(-2)
        for k in range(J+1):
            if k>=n:
                if k==n:jm=F(2*math.factorial(n)**2,math.factorial(2*n+1))
                lm=jm*(2*harmonic[k]-harmonic[k-n]-harmonic[k+n+1])
            if k:
                value=add(value,scale(wc[k]*jm+bc[k]*lm,rat(2*n+1)))
            if k<n-1:lm*=F(-(k+1)**2,(n-k-1)*(n+k+2))
            elif k>=n:jm*=F((k+1)**2,(k+1-n)*(k+n+2))
        slo,shi=endpoints(value);assert shi-slo<F(1,10**30)
        Dn=(rat(sl+harmonic[n])[0],rat(sh+harmonic[n])[1])
        trial=divide(value,Dn);lo,hi=endpoints(trial);cc=(lo+hi)/2;rad=(hi-lo)/2
        lowEnergy+=up(2*B/F(2*n+1)*(sh+harmonic[n])*rad*rad)
        projection.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)))
        mass=2*B/F(2*n+1);err=up(phys/lower_root(mass))
        sourceRows.append(dict(degree=n,represented_source_coefficient_lower=str(slo),represented_source_coefficient_upper=str(shi),actual_source_coefficient_lower=str(down(slo-err)),actual_source_coefficient_upper=str(up(shi+err))))
        if n%128==0:print('RC179 exact Legendre block',n,flush=True)
    # All n>N: polynomial part zero. Bound every endpoint-log basis tail,
    # then use the triangle inequality across the stored signed coefficients.
    Dfirst=sl+harmonic[N+2];tailNorm=F(0);components=[]
    for k in range(1,J+1):
        Ak=2+F(2*k+1,N+2-k)
        e2=4*B*Ak*math.factorial(k)**4/(Dfirst*(4*k+2)*(N-k)**(4*k+2))
        contribution=abs(bc[k])*root(e2);tailNorm+=contribution
        components.append(dict(power=k,weighted_D_inverse_tail_norm_upper=str(up(contribution,10**80))))
    tailNorm=up(tailNorm,10**80);assert tailNorm<F(1,10**6)
    projectedError=up(root(lowEnergy+tailNorm*tailNorm))
    complete=up(globalD+projectedError);assert complete<F(101,10**6)
    digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return dict(input_degree=M,kernel_degree=K,output_degree=N,analytic_source_max_power=J,analytic_source_coefficient_sha256=digest,
      D_inverse_regular_polynomial=projection,analytic_log_tail_components=components,
      parameter_operator_error_upper=str(parameter),kernel_series_uniform_error_upper=str(trunc),source_rounding_uniform_error_upper=str(up(rounding,10**80)),
      represented_output_tail_D_inverse_norm_upper=str(tailNorm),complete_D_inverse_regular_action_error_norm_upper=str(complete))

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];focus,prior,*data,regular=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert focus['milestone']=='RC178' and prior['milestone']=='RC177' and regular['milestone']=='RC170'
    assert focus['input_sha256'][0]==hs[1] and focus['input_sha256'][2:]==hs[2:10] and prior['input_sha256']==hs[2:10]
    fnew,p2,p0,joint,wold,old,metric,physical=data
    assert fnew['input_sha256'][2]==hs[-1]
    src=Path(__file__).with_name('validate_rpb108_rc177_three_source_canonical_action_gram.py').read_text().split("\nif __name__=='__main__':")[0]
    marker='    nominal=[[Z for _ in range(3)] for _ in range(3)];mixed=[[Z for _ in range(3)] for _ in range(3)]'
    assert src.count(marker)==1
    ns={};exec(compile(src.replace(marker,'    return locals()',1),'RC177 immutable carrier reconstruction','exec'),ns)
    d=ns['run'](paths[2:10],replay);assert d['digest']==prior['native_w14_finite_coefficient_sha256']
    dn,f,g,r0,r2,rf,neg=[d[k] for k in ['dn','f','g','r0','r2','rf','neg']]
    selected=focus['selected_enclosure'];Y=[[F(x) for x in row] for row in selected['trial_source_coefficients']]
    probe=list(map(F,focus['half_Gram_gate_failure_witness_source_coefficients']))
    y=[sum(Y[i][j]*probe[j] for j in range(3)) for i in range(3)]
    quadratic=lambda A:sum(probe[i]*F(A[i][j])*probe[j] for i in range(3) for j in range(3))
    M=256;O=prior['finite_prefix_last_degree'];q={};qrows=[];roundEnergy=F(0);finiteTail=F(0)
    order=list(range(0,O+1,2));order=order[::-1] if replay else order
    for n in order:
        v=[rat(r0.get(n,F(0))),rat(r2.get(n,F(0))),add(rat(g[n]+rf.get(n,F(0))+neg.get(n,F(0))),f.get(n,ZERO))]
        if n==0:
            v[0]=add(v[0],rat(1+F(p0['canonical_constant_action_P0_correction_center'])))
            v[1]=add(v[1],rat(F(p2['endpoint_P0_coefficient_center'])))
        if n>=2:v[0]=add(v[0],divide(rat(F(2*n+1,n*(n+1))),dn[n]))
        if n==2:v[1]=add(v[1],rat(1+F(p2['endpoint_P2_correction_center'])))
        if n>=4:v[1]=add(v[1],divide(rat(F(2*n+1,n*(n+1)-6)),dn[n]))
        value=add(rat(probe[0]*F(n==0)+probe[1]*F(n==2)),scale(probe[2],f.get(n,ZERO)))
        for i in range(3):value=sub(value,scale(y[i],v[i]))
        lo,hi=endpoints(value);mass=2*B/F(2*n+1)*F(dn[n][1])
        if n<=M:
            c=(lo+hi)/2;rad=(hi-lo)/2;q[n]=c;roundEnergy+=up(mass*rad*rad)
            qrows.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
        else:finiteTail+=up(mass*max(abs(lo),abs(hi))**2)
    qrows.sort(key=lambda x:x['degree'])
    analyticTail=quadratic(selected['full_inverse_trial_tail_Gram_upper'])
    nominalError=root(roundEnergy+finiteTail+analyticTail)
    actualResidualError=F(focus['residual_focus_nominal_to_actual_D_error_norm_upper'])
    inputError=up(nominalError+actualResidualError)
    relativeInput=up(inputError/F(focus['residual_focus_actual_D_norm_lower']))
    assert relativeInput<F(1,10)
    qEnergyLo=qEnergyHi=F(0)
    for n,c in q.items():
        qEnergyLo+=down(2*B/F(2*n+1)*F(dn[n][0])*c*c)
        qEnergyHi+=up(2*B/F(2*n+1)*F(dn[n][1])*c*c)
    assert qEnergyLo>0 and qEnergyHi<F(1,100)
    print('RC179 focus input complete; D approximation error',float(inputError),flush=True)
    reg=regular_action(q,regular,joint,replay)
    sl,sh=d['sl'],d['sh'];A=sum(abs(c) for c in q.values());log2=log_point(F(2));r=F(789,125)
    H=[F(0)]
    for n in range(1,2*O+1):H.append(H[-1]+F(1,n))
    endpoint=[];endpointEnergy=F(0);negative=[];negativeEnergy=F(0)
    jobs=sorted(q,reverse=replay)
    for n in range(0,O+1,2):
        value=ZERO
        for m in jobs:
            if n==m:entry=sub(rat(2*H[2*n]-2*H[n]+F(1,2*n+1)),log2)
            else:entry=rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=add(value,scale(q[m],entry))
        value=divide(value,dn[n]);lo,hi=endpoints(value);c=(lo+hi)/2;rad=(hi-lo)/2
        endpointEnergy+=up(2*B/F(2*n+1)*(sh+H[n])*rad*rad)
        endpoint.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
        if n<=M:
            value=divide(rat(-r*q[n]),dn[n]);lo,hi=endpoints(value);c=(lo+hi)/2;rad=(hi-lo)/2
            negativeEnergy+=up(2*B/F(2*n+1)*(sh+H[n])*rad*rad)
            negative.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
        if n%1024==0:print('RC179 signed endpoint block',n,flush=True)
    first=O+2;rho=F(M*(M+1),first*(first+1));T=F(prior['common_eta_tail_D_energy_upper'])
    endpointTail=up(root(T)*A/(1-rho));endpointError=up(root(endpointEnergy+endpointTail**2))
    actionError=up(endpointError+root(negativeEnergy)+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    focusActionError=up(actionError+2*inputError)
    assert actionError<F(1,10000) and focusActionError<F(1,100)
    # Exact rational finite source and its represented complete action.
    cq={x['degree']:F(x['coefficient_center']) for x in endpoint};nq={x['degree']:F(x['coefficient_center']) for x in negative};rq={x['degree']:F(x['coefficient_center']) for x in reg['D_inverse_regular_polynomial']}
    trial={n:q.get(n,F(0))+cq.get(n,F(0))+nq.get(n,F(0))+rq.get(n,F(0)) for n in range(0,O+1,2)}
    pair=ZERO
    for n in jobs:pair=add(pair,mul(rat(2*B/F(2*n+1)*q[n]*trial[n]),dn[n]))
    lo,hi=endpoints(pair);pairError=up(root(qEnergyHi)*actionError)
    actualPairLo=down(lo-pairError);actualPairHi=up(hi+pairError)
    assert actualPairLo>F(metric['actual_canonical_diagonal_metric_lower'])*qEnergyHi and actualPairHi<2*qEnergyLo
    return dict(milestone='RC179',status='PASS: paid focus residual approximation and complete actual canonical action',starting_commit='251f9280cecb8f77da488062fd841ce768fedee1',input_sha256=hs,aperture='11/10',
      residual_source_focus=focus['residual_focus_source'],selected_inverse_trial=focus['selected_trial'],inverse_trial_focus_coefficients=list(map(str,y)),
      finite_focus_direction_definition='q=rounded degree-256 prefix of (S-VY)*probe; q is an exact rational polynomial',finite_focus_direction=qrows,
      finite_input_degree=M,nominal_focus_input_rounding_D_energy_upper=str(up(roundEnergy)),omitted_finite_focus_D_energy_upper=str(up(finiteTail)),omitted_analytic_focus_D_energy_upper=str(up(analyticTail)),
      nominal_focus_to_q_D_error_norm_upper=str(up(nominalError)),actual_focus_to_q_D_error_norm_upper=str(inputError),
      actual_focus_to_q_relative_D_norm_error_upper=str(relativeInput),
      finite_focus_D_energy_lower=str(qEnergyLo),finite_focus_D_energy_upper=str(qEnergyHi),regular_action=reg,
      endpoint_action_polynomial=endpoint,endpoint_action_full_output_tail_D_norm_upper=str(endpointTail),endpoint_action_full_D_error_norm_upper=str(endpointError),
      negative_r_D_inverse_direction_polynomial=negative,complete_canonical_q_action_definition='q + stored endpoint polynomial + stored negative-r D^-1 q polynomial + stored D^-1 Rq polynomial',
      complete_actual_canonical_q_action_D_error_norm_upper=str(actionError),complete_actual_focus_residual_action_D_error_norm_upper=str(focusActionError),
      actual_q_canonical_pairing_lower=str(actualPairLo),actual_q_canonical_pairing_upper=str(actualPairHi),canonical_q_pairing_structural_a_D_to_2_D_verified=True,
      canonical_action_on_new_finite_direction_evaluated=True,full_input_and_output_tails_paid=True,actual_focus_action_transfer_uses_M_norm_at_most_two=True,
      enriched_inverse_response_evaluated=False,canonical_half_Gram_gate_closed=False,canonical_Riesz_iteration_performed=False,native_seven_source_frame_changed=False,
      original_Weil_or_augmented_actions_performed=False,full_seven_source_canonical_inverse_certified=False,Stage_I_closed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='add exact finite direction q to the canonical inverse trial space, certify its correlated mixed Gram/action rows, and re-evaluate the three-source half-Gram gate')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=11)
    args=p.parse_args();result=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC179 PASS: finite focus residual direction and complete actual canonical action')
