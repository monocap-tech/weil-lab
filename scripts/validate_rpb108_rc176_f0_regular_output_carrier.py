"""RC176: analytic regular f0 output projection with full endpoint-log tail."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math
from validate_rpb108_rc127_enriched_even_endpoint_action import B,up,down,sqrtup
from validate_rpb108_rc171_regular_legendre_projection import ZERO,rat,add,sub,mul,scale,divide,div_int,endpoints,log_point

def root(x,grid=10**300):
    assert x>=0
    z=math.isqrt(x.numerator*grid*grid//x.denominator)
    if z*z*x.denominator<x.numerator*grid*grid:z+=1
    return F(z,grid)
def lower_root(x):
    z=root(x)-F(1,10**300);assert z>0 and z*z<=x
    return z
def centered(a,grid):
    lo,hi=down(F(a[0]),grid),up(F(a[1]),grid)
    return (lo+hi)/2,(hi-lo)/2

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];old,tail,regular,joint=map(json.loads,raw)
    assert [d['milestone'] for d in (old,tail,regular,joint)]==['RC175','RC174','RC170','RC129']
    hashes=[hashlib.sha256(b).hexdigest() for b in raw]
    assert old['input_sha256'][0]==hashes[1] and old['input_sha256'][3]==hashes[2] and old['input_sha256'][-1]==hashes[3]
    M=old['retained_input_degree'];assert M==172
    K=192;N=512;J=M+K+1;r=F(789,125)
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    harmonic=[F(0)]
    for n in range(1,N+J+2):harmonic.append(harmonic[-1]+F(1,n))
    alpha={x['degree']:F(x['coefficient_center']) for x in old['input_coefficient_intervals']}
    assert hashlib.sha256(json.dumps(old['input_coefficient_intervals'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==old['input_center_sha256']
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
        if j%48==0:print('RC176 analytic kernel block',j,flush=True)
    rows=[];wc=[F(0)]*(J+1);bc=wc.copy();rounding=F(0)
    for k in range(1,J+1):
        wc[k],wr=centered(w[k],10**80);bc[k],br=centered(b[k],10**80)
        rounding+=2*wr+2*br/F(k)
        rows.append(dict(power=k,polynomial_center=str(wc[k]),polynomial_radius=str(wr),log_center=str(bc[k]),log_radius=str(br)))
    assert rounding<F(1,10**60)
    I2=up(eh*ph*ph/3);band=F(M+1)/(6*ph*B)
    smoothing=up(min(r*r,4*B*I2*up(F(11,12)**(2*(M+1)),10**80)+eh*eh/(band*band)))
    inputTail=root(smoothing*F(old['physical_input_tail_energy_upper']))
    center=root(F(old['physical_input_center_error_energy_upper']))
    phys=up(inputTail+r*center+(parameter+trunc)*root(prefix)+root(2*B)*rounding)
    globalD=up(phys/lower_root(sl))
    uniform=up(root(2*I2)*(root(F(old['physical_input_tail_energy_upper']))+center)+(parameter+trunc)*sum(abs(x) for x in alpha.values())+rounding)
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
        if n%128==0:print('RC176 exact Legendre block',n,flush=True)
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
    # Realize the finite -r D^-1 f0 correction through degree 988.
    correction=[];correctionEnergy=F(0)
    for n in range(2,989,2):
        Hn=harmonic[n] if n<len(harmonic) else sum(F(1,j) for j in range(1,n+1))
        dn=(rat(sl+Hn)[0],rat(sh+Hn)[1])
        z=scale(-r,divide(divide(rat(F(2*n+1,n*(n+1))),dn),dn));lo,hi=endpoints(z)
        cc=(lo+hi)/2;rad=(hi-lo)/2;correctionEnergy+=up(2*B/F(2*n+1)*(sh+Hn)*rad*rad)
        correction.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)))
    formError=up(complete+root(correctionEnergy)+F(joint['RC128_Cf0_w_error_paid']))
    samples=[]
    for t in [F(1,2),F(1,4),F(0)]:
        value=ZERO;lt=log_point(t) if t else ZERO;l1=log_point(1-t)
        for k in range(1,J+1):
            value=add(value,add(rat(wc[k]*(t**k+(1-t)**k)),scale(bc[k],add(scale(t**k,lt),scale((1-t)**k,l1)))))
        lo,hi=endpoints(value);assert hi-lo<F(1,10**30)
        oldSample=next(z for z in old['physical_source_samples'] if F(z['x'])==B*(1-2*t))
        tl,th=down(lo-uniform),up(hi+uniform)
        assert max(tl,F(oldSample['actual_Rf0_value_lower']))<=min(th,F(oldSample['actual_Rf0_value_upper']))
        samples.append(dict(x=str(B*(1-2*t)),represented_lower=str(lo),represented_upper=str(hi),actual_Rf0_lower=str(tl),actual_Rf0_upper=str(th)))
    for oldrow in old['retained_regular_output_coefficient_intervals']:
        row=next(x for x in sourceRows if x['degree']==oldrow['degree'])
        assert max(F(row['actual_source_coefficient_lower']),F(oldrow['actual_regular_coefficient_lower']))<=min(F(row['actual_source_coefficient_upper']),F(oldrow['actual_regular_coefficient_upper']))
    return dict(milestone='RC176',status='PASS: full actual f0 regular output carrier and paid canonical first action',starting_commit='93fd7326ce1f8f942369aa38c980336ec7d0c709',input_sha256=hashes,
      input_degree=M,kernel_degree=K,output_degree=N,source_basis_max_power=J,aperture=str(B),
      actual_operator='L=D+h+R-rI; canonical source action D^-1 L',native_source_frame_unchanged=True,
      input_center_sha256=old['input_center_sha256'],kernel_e_center=str(ec),kernel_pi_center=str(pc),kernel_C_center=str(C),
      source_basis='t=(B-x)/(2B); sum_k w_k[t^k+(1-t)^k]+b_k[t^k log(t)+(1-t)^k log(1-t)]; endpoint limits used',
      analytic_source_coefficients=rows,parameter_replacement_operator_error_upper=str(parameter),kernel_series_uniform_error_upper=str(trunc),source_coefficient_rounding_uniform_error_upper=str(up(rounding,10**80)),
      physical_input_tail_error_norm_upper=str(up(inputTail)),complete_physical_source_error_norm_upper=str(phys),complete_uniform_source_error_upper=str(uniform),
      global_source_error_in_D_inverse_norm_upper=str(globalD),physical_source_samples=samples,regular_source_coefficient_enclosures=sourceRows,
      D_inverse_regular_polynomial=projection,retained_D_coefficient_error_energy_upper=str(up(lowEnergy)),
      endpoint_log_tail_components=components,complete_represented_output_tail_D_inverse_norm_upper=str(tailNorm),represented_source_projection_D_error_norm_upper=str(projectedError),
      complete_actual_D_inverse_Rf0_carrier_error_norm_upper=str(complete),negative_r_D_inverse_f0_polynomial=correction,
      canonical_f0_trial='native f0 + native w14 + stored negative_r_D_inverse_f0_polynomial + stored D_inverse_regular_polynomial',
      canonical_f0_trial_D_error_norm_upper=str(formError),RC175_sample_and_zero_two_coefficient_controls_overlap=True,
      full_regular_output_Legendre_carrier_realized=True,full_canonical_f0_first_action_carrier_realized=True,
      full_three_source_canonical_Gram_evaluated=False,full_seven_source_canonical_inverse_certified=False,canonical_Riesz_iteration_performed=False,
      Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='pay the correlated f0 canonical action diagonal and mixed action Gram; then extend canonical inversion from P0/P2 to P0/P2/f0')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=4)
    args=p.parse_args();result=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC176 PASS: full actual f0 regular output carrier and paid canonical first action')
