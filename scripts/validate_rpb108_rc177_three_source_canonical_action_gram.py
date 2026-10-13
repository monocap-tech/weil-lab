"""RC177: full correlated canonical source/first-action Gram on P0,P2,f0."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add
from validate_rpb108_rc134_correlated_six_input_covariance import smul

def scale(c,A):return [[c*x for x in row] for row in A]
def mat(d,k):return [[F(x) for x in row] for row in d[k]]
def width(gap,G):
    yes=lambda k:psd(add(scale(F(k,10**6),G),gap,-1))
    hi=1
    while not yes(hi):hi*=2
    lo=0
    while hi-lo>1:
        mid=(lo+hi)//2
        if yes(mid):hi=mid
        else:lo=mid
    assert yes(hi) and not yes(hi-1)
    return F(hi,10**6)

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];fnew,p2,p0,joint,wold,old,metric,physical=map(json.loads,raw)
    assert [x['milestone'] for x in (fnew,p2,p0,joint,wold,old,metric,physical)]==['RC176','RC172','RC171','RC129','RC128','RC127','RC121','RC175']
    hs=[hashlib.sha256(x).hexdigest() for x in raw]
    assert fnew['input_sha256'][0]==hs[7] and fnew['input_sha256'][-1]==hs[3]
    assert p2['input_sha256'][0]==hs[2] and p2['input_sha256'][-2:]==[hs[6],hs[3]]
    assert p0['input_sha256'][-2:]==[hs[6],hs[3]]
    assert joint['input_sha256'][:2]==[hs[4],hs[5]] and wold['input_sha256'][0]==hs[5]
    sl=F(old['D_Gram_Loewner_lower'][0][0])/(2*B);sh=F(old['D_Gram_Loewner_upper'][0][0])/(2*B)
    s=(rat(sl)[0],rat(sh)[1]);O=4094;r=F(789,125)
    log=(rat(1-F(old['endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(old['endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
    harmonic=[Z]
    for n in range(1,2*O+3):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
    dn={n:plus(s,harmonic[n]) for n in range(0,O+3,2)}
    diagonal={n:minus(plus(minus(mul(rat(2),harmonic[2*n]),mul(rat(2),harmonic[n])),rat(F(1,2*n+1))),log) for n in range(0,O+1,2)}
    f={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(2,989,2)}
    assert F(joint['actual_D_Gram_entry_lower'][0][0])==2*B*sl
    assert F(joint['actual_D_Gram_entry_upper'][0][0])==2*B*sh
    g={};coeff=[];jobs=list(f);jobs=jobs[::-1] if replay else jobs
    for n in range(0,O+1,2):
        value=Z
        for m in jobs:
            entry=diagonal[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,f[m]))
        lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
        g[n]=center;coeff.append(dict(degree=n,center=str(center),radius=str(radius)))
        if n%1024==0:print('RC177 native w14 reconstruction block',n,flush=True)
    digest=hashlib.sha256(json.dumps(coeff,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest==wold['finite_output_polynomial_coefficient_sha256']
    budget=wold['collective_response_enrichment_budgets'][2];mu=list(map(F,budget['analytic_moment_center_coefficients']))
    lam=F(wold['tail_lambda']);assert lam==977132
    assert len(mu)==15 and min(mu)>0
    r0={x['degree']:F(x['D_inverse_trial_coefficient']) for x in p0['physical_regular_coefficient_enclosures']}
    r2={x['degree']:F(x['D_inverse_trial_coefficient']) for x in p2['physical_regular_coefficient_enclosures']}
    rf={x['degree']:F(x['coefficient_center']) for x in fnew['D_inverse_regular_polynomial']}
    neg={x['degree']:F(x['coefficient_center']) for x in fnew['negative_r_D_inverse_f0_polynomial']}
    eps=[F(p0['canonical_constant_action_D_error_norm_upper']),F(p2['canonical_P2_action_D_error_norm_upper']),F(fnew['canonical_f0_trial_D_error_norm_upper'])]
    Glo=[[2*B*sl,F(0),F(0)],[F(0),2*B*(sl+F(3,2))/5,2*B/6],[F(0),2*B/6,F(joint['actual_D_Gram_entry_lower'][2][2])]]
    Ghi=[[2*B*sh,F(0),F(0)],[F(0),2*B*(sh+F(3,2))/5,2*B/6],[F(0),2*B/6,F(joint['actual_D_Gram_entry_upper'][2][2])]]
    assert psd(Glo) and psd(add(Ghi,Glo,-1))
    nominal=[[Z for _ in range(3)] for _ in range(3)];mixed=[[Z for _ in range(3)] for _ in range(3)]
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        v=[rat(r0.get(n,F(0))),rat(r2.get(n,F(0))),plus(rat(g[n]+rf.get(n,F(0))+neg.get(n,F(0))),f.get(n,Z))]
        if n==0:
            v[0]=plus(v[0],rat(1+F(p0['canonical_constant_action_P0_correction_center'])))
            v[1]=plus(v[1],rat(F(p2['endpoint_P0_coefficient_center'])))
        if n>=2:v[0]=plus(v[0],div(rat(F(2*n+1,n*(n+1))),dn[n]))
        if n==2:v[1]=plus(v[1],rat(1+F(p2['endpoint_P2_correction_center'])))
        if n>=4:v[1]=plus(v[1],div(rat(F(2*n+1,n*(n+1)-6)),dn[n]))
        u=[rat(F(n==0)),rat(F(n==2)),f.get(n,Z)]
        mass=mul(rat(2*B/F(2*n+1)),dn[n])
        for i in range(3):
            for j in range(i,3):nominal[i][j]=plus(nominal[i][j],smul(mass,smul(v[i],v[j])))
            for j in range(3):mixed[i][j]=plus(mixed[i][j],smul(mass,smul(u[i],v[j])))
    # Beyond 4094 every stored finite term vanishes. The three action
    # tails are eta, eta/(1-6/z), eta*sum(mu_k*(lambda/z)^k).
    first=O+2;z=first*(first+1)
    tailD=up(B/(F(dn[O][0])*(O-1)*O))
    amps=[F(1),1/(1-F(6,z)),sum(mu[k]*(lam/z)**k for k in range(15))]
    assert amps[2]<=F(joint['analytic_tail_coefficient_domination_constant'])
    qLo=[[F(0)]*3 for _ in range(3)];qHi=[[F(0)]*3 for _ in range(3)]
    finiteLo=[[F(0)]*3 for _ in range(3)];finiteHi=[[F(0)]*3 for _ in range(3)]
    tailEntry=[[up(amps[i]*amps[j]*tailD) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(i,3):
            lo,hi=bounds(nominal[i][j]);finiteLo[i][j]=finiteLo[j][i]=lo;finiteHi[i][j]=finiteHi[j][i]=hi
            qLo[i][j]=qLo[j][i]=lo;qHi[i][j]=qHi[j][i]=up(hi+tailEntry[i][j])
    sourceWeights=[sqrtup(Ghi[i][i]) for i in range(3)]
    nominalLo,nominalHi,_=loewner(qLo,qHi,sourceWeights)
    assert psd(nominalLo) and psd(add(nominalHi,nominalLo,-1))
    normalizedSum=sum(eps[i]/sourceWeights[i] for i in range(3))
    E=[[up(eps[i]*sourceWeights[i]*normalizedSum) if i==j else F(0) for j in range(3)] for i in range(3)]
    assert psd(E) and psd(add(E,[[eps[i]*eps[j] for j in range(3)] for i in range(3)],-1))
    # Actual symmetric first moment: intersect both independently paid
    # action rows using self-adjointness; retain prior two-source controls.
    kLo=[[F(0)]*3 for _ in range(3)];kHi=[[F(0)]*3 for _ in range(3)]
    directional=[]
    for i in range(3):
        for j in range(i,3):
            enclosures=[]
            for a,b in [(i,j),(j,i)]:
                lo,hi=bounds(mixed[a][b]);err=up(sourceWeights[a]*eps[b])
                enclosures.append((down(lo-err),up(hi+err)))
            if i<2 and j<2:enclosures.append((F(p2['two_source_canonical_Gram_entry_lower'][i][j]),F(p2['two_source_canonical_Gram_entry_upper'][i][j])))
            if j==2 and i<2:
                prior=physical['actual_canonical_P0_P2_f0_mixed_pairings'][i]
                enclosures.append((F(prior['canonical_mixed_pairing_lower']),F(prior['canonical_mixed_pairing_upper'])))
            lo=max(a for a,b in enclosures);hi=min(b for a,b in enclosures);assert lo<=hi
            kLo[i][j]=kLo[j][i]=lo;kHi[i][j]=kHi[j][i]=hi
            directional.append(dict(row=i,column=j,independent_lower_bounds=[str(a) for a,b in enclosures],independent_upper_bounds=[str(b) for a,b in enclosures]))
    Klo,Khi,_=loewner(kLo,kHi,sourceWeights)
    a=F(metric['actual_canonical_diagonal_metric_lower']);assert a==F(32125,230953)
    assert psd(add(Klo,scale(a,Ghi),-1)) and psd(add(scale(2,Glo),Khi,-1))
    # Every mixed action error is paid; no orthogonality is assigned to
    # old and new errors or to the input-induced output error.
    actionWeights=[sqrtup(qHi[i][i]) for i in range(3)]
    actualLo=[[F(0)]*3 for _ in range(3)];actualHi=[[F(0)]*3 for _ in range(3)];errorEntry=[[F(0)]*3 for _ in range(3)]
    for i in range(3):
        for j in range(i,3):
            err=up(actionWeights[i]*eps[j]+actionWeights[j]*eps[i]+eps[i]*eps[j])
            errorEntry[i][j]=errorEntry[j][i]=err
            actualLo[i][j]=actualLo[j][i]=down(qLo[i][j]-err)
            actualHi[i][j]=actualHi[j][i]=up(qHi[i][j]+err)
    Qlo,Qhi,_=loewner(actualLo,actualHi,sourceWeights)
    assert psd(Qlo) and psd(add(Qhi,Qlo,-1))
    assert psd(add(Qlo,scale(a,Khi),-1)) and psd(add(scale(2,Klo),Qhi,-1))
    assert psd(add(Qlo,scale(a*a,Ghi),-1)) and psd(add(scale(4,Glo),Qhi,-1))
    kWidth=width(add(Khi,Klo,-1),Glo);qWidth=width(add(Qhi,Qlo,-1),Glo);eWidth=width(E,Glo)
    assert kWidth<F(1,20) and qWidth<F(1,20)
    return dict(milestone='RC177',status='PASS: full correlated three-source canonical first and action Gram',starting_commit='cd81bb3848963aed70020e84205a29658ba538a8',input_sha256=hs,aperture='11/10',source_order=['P0','P2','f0'],
      source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),exact_P2_f0_D_pairing=str(2*B/6),
      action_operator='M=D^-1 L, self-adjoint in D energy; L=D+h+R-rI',
      action_carriers='RC171 P0, RC172 P2, RC176 f0; native w14 reconstructed with RC128 coefficient hash',
      native_w14_finite_coefficient_sha256=digest,finite_prefix_last_degree=O,first_omitted_even_degree=first,
      full_tail_action_definitions=['eta_n','eta_n/(1-6/(n(n+1)))','eta_n*sum_k=0..14 mu_k*(lambda/(n(n+1)))^k'],native_w14_tail_lambda=str(lam),
      common_eta_tail_D_energy_upper=str(tailD),tail_coefficient_amplitude_upper=list(map(str,amps)),full_tail_action_Gram_entry_upper=ser(tailEntry),
      individual_full_action_D_error_norm_upper=list(map(str,eps)),full_correlated_action_error_Gram_upper=ser(E),action_error_relative_to_three_source_D_Gram_squared_upper=str(eWidth),
      nominal_action_Gram_finite_entry_lower=ser(finiteLo),nominal_action_Gram_finite_entry_upper=ser(finiteHi),nominal_full_action_Gram_entry_lower=ser(qLo),nominal_full_action_Gram_entry_upper=ser(qHi),
      nominal_full_action_Gram_Loewner_lower=ser(nominalLo),nominal_full_action_Gram_Loewner_upper=ser(nominalHi),
      selfadjoint_first_moment_intersection_controls=directional,actual_canonical_Gram_entry_lower=ser(kLo),actual_canonical_Gram_entry_upper=ser(kHi),
      actual_canonical_Gram_Loewner_lower=ser(Klo),actual_canonical_Gram_Loewner_upper=ser(Khi),relative_first_moment_width_upper=str(kWidth),
      mixed_action_Gram_error_entry_radius=ser(errorEntry),actual_full_action_Gram_entry_lower=ser(actualLo),actual_full_action_Gram_entry_upper=ser(actualHi),
      actual_full_action_Gram_Loewner_lower=ser(Qlo),actual_full_action_Gram_Loewner_upper=ser(Qhi),relative_action_Gram_width_upper=str(qWidth),
      structural_a_G_le_K_le_2_G_verified=True,structural_a_K_le_Q_le_2_K_verified=True,structural_a_squared_G_le_Q_le_4_G_verified=True,
      all_real_and_complex_three_source_mixtures_paid=True,finite_compression_invariance_assumed=False,action_error_orthogonality_assumed=False,
      full_three_source_canonical_Gram_evaluated=True,full_three_source_canonical_action_Gram_evaluated=True,native_seven_source_frame_changed=False,
      actual_three_source_canonical_inverse_response_certified=False,full_seven_source_canonical_inverse_certified=False,canonical_Riesz_iteration_performed=False,
      original_augmentation_adjoint_range_identified=False,required_Stage_I_matrix_tolerance_specified=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='extend RC173 actual canonical inverse response to P0/P2/f0, paying full correlated inverse-trial residuals with these complete action carriers')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=8)
    args=p.parse_args();r=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==r
    else:Path(args.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC177 PASS: complete correlated P0/P2/f0 canonical first and action Gram')
