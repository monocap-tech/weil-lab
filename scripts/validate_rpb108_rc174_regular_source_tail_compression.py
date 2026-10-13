"""RC174: seven-source regular input-tail compression and actual f0 budgets."""
from pathlib import Path
from fractions import Fraction as F
from math import ceil,sqrt
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,mul,div,bounds,up,down,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,cong,mm,transpose

def scale(t,A):return [[t*x for x in row] for row in A]

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];prior,native,moments,tail,regular,metric,joint=map(json.loads,raw)
    assert [d['milestone'] for d in (prior,native,moments,tail,regular,metric,joint)]==['RC173','RC169','RC168','RC159','RC170','RC121','RC129']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert prior['input_sha256'][2:]==hs[5:]
    assert native['input_sha256'][0]==hs[2] and native['input_sha256'][3]==hs[5]
    assert moments['input_sha256'][1]==hs[3] and moments['input_sha256'][7]==hs[6]
    assert regular['input_sha256']==[hs[1],hs[5]]
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    ep=F(regular['e_upper']);pi=F(regular['pi_upper']);I2=up(ep*pi*pi/3);r=F(789,125)
    assert ep<F(11,4) and 4*B*I2<r*r
    def smoothing(N):
        n=N+1;U=F(n)/(6*pi*B)
        # n! >= (n/e)^n; e<11/4 gives the exact real-axis Taylor bound.
        rem2=up(F(11,12)**(2*n),10**80)
        beta=up(min(r*r,4*B*I2*rem2+ep*ep/(U*U)))
        return U,rem2,beta
    O=tail['finite_Gram_prefix_degree'];first=tail['first_omitted_even_degree']
    assert O==16382 and first==O+2 and moments['finite_tail_first_degree']==first
    harmonic=[Z]
    for n in range(1,first+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
    Dfirst=F(plus(harmonic[first],rat(sl))[0])
    U,rem2,phi2=smoothing(O);factor=up(phi2/(sl*Dfirst))
    coeff=mat(tail,'conditioned_scaled_tail_polynomial_coefficients')
    nativeCoeff=mat(tail,'native_scaled_tail_polynomial_coefficients');T=mat(native,'conditioned_to_native_source_matrix');Ti=mat(native,'native_to_conditioned_coefficients')
    assert mm(transpose(nativeCoeff),T)==coeff
    assert mm(T,Ti)==[[F(i==j) for j in range(7)] for i in range(7)]
    polys=transpose(coeff);ml=[F(x['full_lower']) for x in moments['tail_moment_intervals']];mu=[F(x['full_upper']) for x in moments['tail_moment_intervals']]
    entryLo=[[F(0)]*7 for _ in range(7)];entryHi=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            conv=[F(0)]*(len(polys[i])+len(polys[j])-1)
            for k,x in enumerate(polys[i]):
                for l,y in enumerate(polys[j]):conv[k+l]+=x*y
            orders=list(range(len(conv)));orders=orders[::-1] if replay else orders
            lo=hi=F(0)
            for k in orders:
                c=conv[k];lo+=c*(ml[k] if c>=0 else mu[k]);hi+=c*(mu[k] if c>=0 else ml[k])
            entryLo[i][j]=entryLo[j][i]=down(lo);entryHi[i][j]=entryHi[j][i]=up(hi)
    Glo=mat(moments,'conditioned_source_Gram_lower');Ghi=mat(moments,'conditioned_source_Gram_upper')
    weights=[sqrtup(Ghi[i][i]) for i in range(7)]
    _,tailHi,_=loewner(entryLo,entryHi,weights);assert psd(tailHi)
    errorTail=scale(factor,tailHi);assert psd(errorTail)
    # NumPy supplies a hint only; exact rational PSD pays every reported bound.
    import numpy as np
    ds=[sqrt(float(Glo[i][i])) for i in range(7)]
    chol=np.linalg.cholesky([[float(Glo[i][j])/ds[i]/ds[j] for j in range(7)] for i in range(7)])
    grid=10**16
    def relative(A):
        yes=lambda k:psd(add(scale(F(k,grid),Glo),A,-1))
        Q=np.array([[float(A[i][j])/ds[i]/ds[j] for j in range(7)] for i in range(7)])
        H=np.linalg.solve(chol,np.linalg.solve(chol,Q).T).T
        k=max(1,ceil(float(np.linalg.eigvalsh((H+H.T)/2)[-1])*grid))
        for _ in range(8):
            if yes(k):
                if not yes(k-1):return F(k,grid)
                k-=1
            else:k+=1
        hi=1
        while not yes(hi):hi*=2
        lo=0
        while hi-lo>1:
            mid=(lo+hi)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(hi-1);return F(hi,grid)
    tailBeta=relative(errorTail);tailNorm=sqrtup(tailBeta)
    quadFactor=up(F(regular['supported_physical_L2_operator_error_norm_upper'])**2/(sl*sl))
    quadError=scale(quadFactor,Ghi)
    taus=[F(1,10),F(1,4),F(1,2),F(1),F(2),F(4),F(10)];taus=taus[::-1] if replay else taus
    candidates=[];best=None
    for tau in taus:
        E=add(scale(1+tau,errorTail),scale(1+1/tau,quadError));beta=relative(E)
        candidates.append(dict(tau=str(tau),relative_error_energy_upper=str(beta)))
        if best is None or (beta,tau)<best[0]:best=((beta,tau),E)
    (beta,tau),combined=best;norm=sqrtup(beta)
    candidates.sort(key=lambda d:F(d['tau']))
    nGlo=mat(native,'native_source_D_Gram_lower');assert cong(Ti,Glo)==nGlo
    nativeTail=cong(Ti,errorTail);nativeCombined=cong(Ti,combined)
    assert psd(add(scale(tailBeta,nGlo),nativeTail,-1)) and psd(add(scale(beta,nGlo),nativeCombined,-1))
    # Actual finite f0 contains eta coefficients at all even degrees 2..988.
    physicalE={};jobs=list(range(2,989,2));jobs=jobs[::-1] if replay else jobs
    for n in jobs:
        dn=plus(harmonic[n],rat(sl));d=(dn[0],plus(harmonic[n],rat(sh))[1])
        value=div(rat(F(2*n+1,n*(n+1))),d)
        energy=mul(rat(2*B/F(2*n+1)),mul(value,value));physicalE[n]=bounds(energy)[1]
    prefixTail={};total=F(0)
    for n in range(988,0,-2):prefixTail[n]=total;total+=physicalE[n]
    prefixTail[0]=total
    rows=[]
    for M in range(0,989,2):
        tailEnergy=prefixTail[M]
        u,rem,ph=smoothing(M)
        err2=up(ph*tailEnergy/sl);old2=up(r*r*tailEnergy/sl)
        rows.append(dict(degree=M,source_physical_tail_energy_upper=str(tailEnergy),smoothing_factor_squared_upper=str(ph),D_inverse_regular_input_tail_error_norm_upper=str(sqrtup(err2)),uniform_r_only_error_norm_upper=str(sqrtup(old2))))
    targets=[F(1,10**4),F(1,10**5),F(1,10**6)];budgets=[]
    for target in targets:
        selected=next(row for row in rows if F(row['D_inverse_regular_input_tail_error_norm_upper'])<=target)
        M=selected['degree'];assert M==0 or F(rows[M//2-1]['D_inverse_regular_input_tail_error_norm_upper'])>target
        budgets.append(dict(requested_component_D_error_norm=str(target),smallest_even_input_degree_for_this_bound=M,achieved_input_tail_error_norm_upper=selected['D_inverse_regular_input_tail_error_norm_upper']))
    displays=[rows[M//2] for M in [16,32,64,128,192,256,384,512,768,988]]
    return dict(milestone='RC174',status='PASS: full seven-source regular input-tail contract and f0 finite-input budgets',starting_commit='0f30fec20153a724c55b4b8d3c6555b448222c54',input_sha256=hs,aperture='11/10',
      regular_high_input_mode_bound='||R (I-Pi_N)||_physical^2 <= min(r^2,4*B*I2*(11/12)^(2*(N+1))+e_upper^2/U^2), U=(N+1)/(6*pi_upper*B)',
      finite_regular_input_last_degree=O,first_omitted_even_degree=first,low_frequency_half_bandwidth=str(U),Taylor_remainder_squared_upper=str(rem2),high_mode_regular_operator_norm_squared_upper=str(phi2),
      conditioned_source_tail_D_Gram_entry_lower=ser(entryLo),conditioned_source_tail_D_Gram_entry_upper=ser(entryHi),conditioned_source_tail_D_Gram_upper=ser(tailHi),
      tail_to_regular_D_action_squared_factor_upper=str(factor),conditioned_regular_input_tail_error_Gram_upper=ser(errorTail),native_regular_input_tail_error_Gram_upper=ser(nativeTail),
      seven_source_regular_input_tail_relative_error_energy_upper=str(tailBeta),seven_source_regular_input_tail_relative_error_norm_upper=str(tailNorm),
      seven_source_finite_Poisson_regular_map_error_Gram_upper=ser(combined),native_seven_source_finite_Poisson_regular_map_error_Gram_upper=ser(nativeCombined),
      combined_regular_map_relative_error_energy_upper=str(beta),combined_regular_map_relative_error_norm_upper=str(norm),selected_Young_tau=str(tau),combined_error_candidates=candidates,
      represented_regular_map='D^-1 Rhat Pi_16382 on the full seven-source family; source coefficients keep actual s',
      f0_finite_input_component_budgets=budgets,f0_input_cutoff_examples=displays,
      f0_budgets_include_only_regular_input_truncation=True,all_seven_source_real_and_complex_tail_mixtures_paid=True,
      compressed_action_map_selfadjointness_assumed=False,true_action_error_lower_bound_inferred=False,
      endpoint_or_minus_r_term_input_tails_dropped=False,finite_regular_output_coefficients_realized_on_seven_sources=False,
      new_regular_output_actions_evaluated=False,full_seven_source_canonical_inverse_certified=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='evaluate the compressed finite-polynomial regular source outputs with their arithmetic/carrier errors; use the paid correlated input-tail contracts and preserve endpoint and -r source tails')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=7)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC174 PASS: seven-source regular tail compression and finite f0 budgets')
