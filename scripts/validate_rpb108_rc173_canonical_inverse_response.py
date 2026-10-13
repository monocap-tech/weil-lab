"""RC173: actual two-source canonical inverse response with full residuals."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,cong,add
from validate_rpb108_rc134_correlated_six_input_covariance import smul

def scale(c,A):return [[c*x for x in row] for row in A]
def outer(x):return [[a*b for b in x] for a in x]

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];actions,constant,metric,joint=map(json.loads,raw)
    assert [d['milestone'] for d in (actions,constant,metric,joint)]==['RC172','RC171','RC121','RC129']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert actions['input_sha256'][0]==hs[1] and actions['input_sha256'][3:]==hs[2:]
    assert constant['input_sha256'][2:]==hs[2:]
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    Glo=[[2*B*sl,F(0)],[F(0),2*B*(sl+F(3,2))/5]];Ghi=[[2*B*sh,F(0)],[F(0),2*B*(sh+F(3,2))/5]]
    assert Glo==mat(actions,'two_source_D_Gram_lower')
    Klo=mat(actions,'two_source_canonical_Gram_Loewner_lower');Khi=mat(actions,'two_source_canonical_Gram_Loewner_upper')
    Gmid=scale(F(1,2),add(Glo,Ghi));Kmid=scale(F(1,2),add(Klo,Khi))
    Y=[[down(x,10**30) for x in row] for row in mm(inv(Kmid),Gmid)]
    I=[[F(i==j) for j in range(2)] for i in range(2)];Iminus=add(I,Y,-1)
    # 2 sym(GY)-Y*KY = G-(I-Y)*G*(I-Y)+Y*(G-K)*Y.
    Clo=add(add(Glo,cong(Iminus,Ghi),-1),cong(Y,add(Glo,Khi,-1)))
    Chi=add(add(Ghi,cong(Iminus,Glo),-1),cong(Y,add(Ghi,Klo,-1)))
    assert psd(Clo) and psd(add(Chi,Clo,-1))
    s=(rat(sl)[0],rat(sh)[1]);harmonic=[Z]
    O=4094
    for n in range(1,O+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
    dn={n:plus(s,harmonic[n]) for n in range(0,O+1,2)}
    r0={r['degree']:F(r['D_inverse_trial_coefficient']) for r in constant['physical_regular_coefficient_enclosures']}
    r2={r['degree']:F(r['D_inverse_trial_coefficient']) for r in actions['physical_regular_coefficient_enclosures']}
    finite=[[Z for _ in range(2)] for _ in range(2)]
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        v=[rat(r0.get(n,F(0))),rat(r2.get(n,F(0)))]
        if n==0:
            v[0]=plus(v[0],rat(1+F(constant['canonical_constant_action_P0_correction_center'])))
            v[1]=plus(v[1],rat(F(actions['endpoint_P0_coefficient_center'])))
        if n>=2:v[0]=plus(v[0],div(rat(F(2*n+1,n*(n+1))),dn[n]))
        if n==2:v[1]=plus(v[1],rat(1+F(actions['endpoint_P2_correction_center'])))
        if n>=4:v[1]=plus(v[1],div(rat(F(2*n+1,n*(n+1)-6)),dn[n]))
        residual=[]
        for i in range(2):
            t=plus(smul(rat(Y[0][i]),v[0]),smul(rat(Y[1][i]),v[1]))
            residual.append(minus(rat(F(n==[0,2][i])),t))
        mass=mul(rat(2*B/F(2*n+1)),dn[n])
        for i in range(2):
            for j in range(i,2):finite[i][j]=plus(finite[i][j],smul(mass,smul(residual[i],residual[j])))
    fLo=[[F(0)]*2 for _ in range(2)];fHi=[[F(0)]*2 for _ in range(2)]
    for i in range(2):
        for j in range(i,2):
            lo,hi=bounds(finite[i][j]);fLo[i][j]=fLo[j][i]=lo;fHi[i][j]=fHi[j][i]=hi
    weights=[sqrtup(Ghi[i][i]) for i in range(2)]
    Nlo,prefixHi,_=loewner(fLo,fHi,weights);assert psd(Nlo) and psd(prefixHi)
    first=O+2;delta=F(6,first*(first+1)-6)
    T=up(B/(F(dn[O][0])*(O-1)*O));tailTau=F(1,1000)
    b=[Y[0][i]+Y[1][i] for i in range(2)];c=Y[1]
    tailHi=add(scale((1+tailTau)*T,outer(b)),scale((1+1/tailTau)*T*delta**2,outer(c)))
    assert psd(tailHi)
    Nhi=add(prefixHi,tailHi);assert psd(Nhi) and psd(add(Nhi,Nlo,-1))
    E=cong(Y,mat(actions,'two_source_canonical_action_error_Gram_upper'));assert psd(E)
    a=F(metric['actual_canonical_diagonal_metric_lower']);assert a==F(32125,230953) and metric['actual_canonical_diagonal_metric_upper']=='2'
    def width(gap,denominator=None):
        denominator=Glo if denominator is None else denominator
        yes=lambda k:psd(add(scale(F(k,10**6),denominator),gap,-1))
        hi=1
        while not yes(hi):hi*=2
        lo=0
        while hi-lo>1:
            mid=(lo+hi)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(hi-1)
        return F(hi,10**6)
    candidates=[];best=None
    uppers=[F(1,1000),F(1,300),F(1,100),F(1,30),F(1,10),F(1,3),F(1)]
    lowers=[F(0),F(1,100),F(1,30),F(1,10),F(1,3),F(1,2)]
    if replay:uppers.reverse();lowers.reverse()
    for tau in uppers:
        Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E))
        upper=add(Chi,scale(1/a,Rhi))
        for sigma in lowers:
            Rlo=[[F(0)]*2 for _ in range(2)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
            if not psd(Rlo):continue
            lower=add(Clo,scale(F(1,2),Rlo));gap=add(upper,lower,-1);assert psd(lower) and psd(gap)
            beta=width(gap);key=(beta,tau,sigma);candidates.append(dict(upper_tau=str(tau),lower_tau=str(sigma),relative_inverse_width_upper=str(beta)))
            if best is None or key<best[0]:best=(key,lower,upper,Rlo,Rhi)
    (beta,tau,sigma),lower,upper,Rlo,Rhi=best
    assert psd(add(lower,scale(F(1,2),Glo),-1))
    assert psd(add(scale(1/a,Ghi),upper,-1))
    gate=add(scale(F(1,2),Glo),add(upper,lower,-1),-1);passed=psd(gate)
    candidates.sort(key=lambda d:(F(d['upper_tau']),F(d['lower_tau'])))
    # The represented vector trial S Y has D-error Gram <=Rhi/a^2;
    # its actual canonical-energy error Gram is <=Rhi/a.
    vectorError=scale(1/(a*a),Rhi)
    canonicalError=scale(1/a,Rhi)
    warmstartSquared=width(canonicalError,lower);warmstartNorm=sqrtup(warmstartSquared)
    assert warmstartNorm<F(3,10)
    return dict(milestone='RC173',status='PASS: actual two-source canonical inverse with paid full residuals',starting_commit='f5ed7ad1a9144577e96ee76cb1b6161da9d989c3',input_sha256=hs,aperture='11/10',
      source_order=['P0','P2'],inverse_response_definition='Sigma=(D S)^* L^-1 (D S)=S^* D (D^-1 L)^-1 S',
      actual_canonical_metric_operator_used=True,original_augmentation_adjoint_range_identified=False,
      source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),trial_source_coefficients=ser(Y),
      variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),
      nominal_residual_finite_entry_lower=ser(fLo),nominal_residual_finite_entry_upper=ser(fHi),
      nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),
      finite_prefix_last_degree=O,first_omitted_even_degree=first,common_eta_tail_D_energy_upper=str(T),tail_rank_one_remainder_upper=ser(tailHi),
      inverse_trial_action_error_Gram_upper=ser(E),selected_actual_residual_Gram_lower=ser(Rlo),selected_actual_residual_Gram_upper=ser(Rhi),
      candidate_enclosures=candidates,selected_upper_tau=str(tau),selected_lower_tau=str(sigma),
      canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),
      canonical_half_Gram_gate_matrix=ser(gate),canonical_half_Gram_inverse_width_gate_passed=passed,
      selected_enclosure_improves_fullspace_structural_bounds=True,true_inverse_uncertainty_lower_bound_inferred=False,
      canonical_Riesz_trial_D_error_Gram_upper=ser(vectorError),canonical_Riesz_trial_D_error_relative_squared_upper=str(width(vectorError)),
      canonical_Riesz_trial_canonical_error_Gram_upper=ser(canonicalError),canonical_Riesz_trial_canonical_error_relative_source_D_squared_upper=str(width(canonicalError)),
      canonical_Riesz_warmstart_relative_to_true_image_energy_squared_upper=str(warmstartSquared),canonical_Riesz_warmstart_relative_to_true_image_norm_upper=str(warmstartNorm),
      actual_canonical_inverse_response_certified_on_two_sources=True,all_real_and_complex_two_source_mixtures_paid=True,
      source_interpretation='physical dual sources s*P0 and (s+3/2)*P2; actual constants retained',
      both_infinite_endpoint_tails_retained=True,new_regular_or_endpoint_actions_performed=False,
      full_seven_source_canonical_inverse_certified=False,required_Stage_I_matrix_tolerance_specified=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='extend the paid physical source/action family or enrich the canonical inverse trials in the residual directions; preserve the distinction between this two-source canonical gate and full Stage I coverage')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=4)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC173 PASS: actual canonical inverse and full two-source residual')
