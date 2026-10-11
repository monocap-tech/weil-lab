"""RC63: actual 22-feature weak directions obstruct the RC57 uniform gate.

Fixed rational witnesses; no floating eigenvalue is accepted as evidence.
Bounds concern actual original Weil values and actual canonical norms.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import psd
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,serialize,root

DIM=22
WITNESSES=[
 (0,'weak_0',[240055290268,-482287602642,389870311391,-253644770281,132341598187,-55013389432,18028339291,-4574326831,867914768,-113866724,8197968]),
 (0,'weak_1',[213765909461,-281399395495,-131416625613,424995216563,-421273866871,254714387347,-105122162474,30312864712,-5923229471,692851884,-28931926]),
 (0,'positive_control',[217358535758,-110537363271,-425881284045,247166081547,276237182813,-433297199301,261088657740,-85638785357,13669463489,360282981,-518622083]),
 (1,'weak_0',[149267523357,-411363150617,477708927192,-365170357547,201655233261,-83047230859,25676433624,-5874155828,947807995,-94688511,3615950]),
 (1,'weak_1',[-222922467274,436630264788,-94740737708,-344130487055,439881477330,-276429905976,107376886919,-26228272616,3389960264,50082556,-83059073]),
 (1,'positive_control',[327703088304,-345467802402,-370810173193,311310484770,265873761130,-412716141754,207157048680,-41413012300,-4845665534,4623329622,-752359316])]

def quad(v,A):return sum((v[i]*v[j]*A[i][j] for i in range(DIM) for j in range(DIM)),F(0))
def up(x,den=10**30):
    a=x*den;return F(-(-a.numerator//a.denominator),den)
def down(x,den=10**30):
    a=x*den;return F(a.numerator//a.denominator,den)

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];native,residual,head,source,floor=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert [source['input_sha256'][k] for k in [1,2,3]]==hashes[:3]
    assert head['input_sha256'][1:3]==hashes[:2]
    assert floor['input_sha256'][6]==source['input_sha256'][4]
    P=matrix(native['physical_native_Gram']);T=matrix(native['physical_native_trial_Gram'])
    Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(residual['actual_canonical_Riesz_error_Gram_Loewner_upper'])
    U=matrix(source['nominal_complete_original_source_Gram_Loewner_upper']);QT=entries(head['actual_original_trial_Weil_head_entry_enclosures'])
    assert all(psd(A) for A in [P,T,Ep,Ec,U])
    alpha=F(native['actual_canonical_native_Gram_physical_lower_factor']);rho=F(native['actual_canonical_native_Gram_physical_upper_factor'])
    oldh=F(floor['original_Weil_uniform_low_eight_canonical_floor_lower']);assert oldh==F(1,2900000)
    gate=floor['conditional_1250_gate'];assert F(gate['required_actual_head_floor'])==oldh and gate['feature_count']==1250
    delta=F(source['actual_source_approximation_operator_error_upper']);k=list(map(F,source['complete_physical_operator_parity_norm_upper']))
    result=[]
    for parity,label,coeff in WITNESSES:
        v=[F(0)]*DIM
        for i,x in zip(range(parity,DIM,2),coeff):v[i]=F(x,10**12)
        pn=quad(v,P);tt=quad(v,T);ee=quad(v,Ep);ce=quad(v,Ec);uu=quad(v,U)
        assert pn>0 and min(tt,ee,ce,uu)>=0
        base=F(0);hr=F(0)
        for i in range(DIM):
            for j in range(DIM):
                a,b=QT[tuple(sorted((i,j)))];base+=v[i]*v[j]*(a+b)/2;hr+=abs(v[i]*v[j])*(b-a)/2
        rn=root(ee,10**30);un=root(uu,10**30);tn=root(tt,10**30)
        sn=up(un+delta*tn);linear=up(2*rn*sn);quadratic=up(k[parity]*ee)
        # Exact original-source cancellation; -E*E keeps its diagonal sign.
        lo=down(base-hr-linear-quadratic-ce);hi=up(base+hr+linear+quadratic)
        mlo=alpha*pn;mhi=rho*pn
        rlo=down(lo/(mhi if lo>=0 else mlo));rhi=up(hi/(mlo if hi>=0 else mhi))
        target=up(hi-oldh*mlo)
        if label.startswith('weak'):
            assert lo<0<hi and rhi<F(3,10**10) and target<0
        else:assert lo>0
        if replay:
            # Independent bilinear accumulation using only one triangle.
            def triangle(A):return sum((v[i]**2*A[i][i]+2*sum((v[i]*v[j]*A[i][j] for j in range(i+1,DIM)),F(0)) for i in range(DIM)),F(0))
            assert [triangle(A) for A in [P,T,Ep,Ec,U]]==[pn,tt,ee,ce,uu]
            assert rn**2>=ee and un**2>=uu and tn**2>=tt
            assert sn>=un+delta*tn and linear**2>=4*ee*sn**2
            assert lo<=base-hr-linear-quadratic-ce and hi>=base+hr+linear+quadratic
            assert target>=hi-oldh*mlo
        result.append(dict(parity='even' if parity==0 else 'odd',role=label,coefficients=list(map(str,v)),
            physical_native_squared_norm=str(pn),canonical_native_squared_norm_lower=str(mlo),canonical_native_squared_norm_upper=str(mhi),
            trial_physical_squared_norm=str(tt),actual_physical_Riesz_error_squared_upper=str(ee),
            actual_canonical_Riesz_error_squared_upper=str(ce),nominal_original_source_squared_upper=str(uu),
            actual_trial_original_source_norm_upper=str(sn),actual_trial_Weil_quadratic_center=str(base),
            actual_trial_Weil_quadratic_radius=str(hr),linear_original_source_error_allowance=str(linear),
            physical_quadratic_error_allowance=str(quadratic),actual_original_Weil_quadratic_lower=str(lo),actual_original_Weil_quadratic_upper=str(hi),
            actual_canonical_Rayleigh_lower=str(rlo),actual_canonical_Rayleigh_upper=str(rhi),
            old_gate_Q_minus_h_M_quadratic_upper=str(target),old_gate_floor_ruled_out=target<0,
            actual_Weil_direction_certified_positive=lo>0,actual_Weil_direction_certified_negative=hi<0))
    weak=[r for r in result if r['role'].startswith('weak')]
    best=min(weak,key=lambda r:F(r['actual_canonical_Rayleigh_upper']));bound=F(best['actual_canonical_Rayleigh_upper'])
    assert bound<F(18,10**11) and oldh/bound>1900
    tail=F(gate['inherited_actual_complement_floor']);budget=F(gate['required_actual_canonical_source_residual_relative_Gram_upper'])
    ceiling=tail*bound;assert budget/ceiling>900
    return dict(milestone='RC63',status='PASS',input_sha256=hashes,native_features_certified=list(range(DIM)),
        fixed_rational_direction_certificates=result,any_uniform_actual_twenty_two_canonical_head_floor_upper=str(bound),
        strongest_floor_ceiling_witness=dict(parity=best['parity'],role=best['role']),
        retained_actual_low_eight_uniform_floor=str(oldh),low_eight_floor_not_extendible_to_twenty_two=True,
        inherited_conditional_1250_head_floor_requirement_ruled_out=True,
        same_floor_ruled_out_on_every_native_superspace_containing_first_twenty_two=True,
        old_floor_to_new_certified_ceiling_ratio_lower=str(oldh/bound),
        inherited_1250_complement_floor=str(tail),old_conditional_squared_source_budget=str(budget),
        scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor=str(ceiling),
        old_source_budget_to_scalar_Schur_ceiling_ratio_lower=str(budget/ceiling),
        scalar_Schur_ceiling_is_a_requirement_of_this_sufficient_method_not_necessary_positivity=True,
        certified_positive_control_directions=[dict(parity=r['parity'],role=r['role']) for r in result if r['actual_Weil_direction_certified_positive']],
        all_individual_native_feature_signs_remain_positive=source['certified_positive_actual_original_head_diagonal_features']==list(range(DIM)),
        actual_head_indefiniteness_proved=False,uniform_twenty_two_positive_floor_certified=False,
        actual_twenty_two_projected_source_residual_evaluated=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc59_twenty_two_native_projection.json','rpb108_rc60_twenty_two_mixed_residuals.json','rpb108_rc61_twenty_two_signed_head.json','rpb108_rc62_twenty_two_original_source_covariance.json','rpb108_rc57_uniform_low_head_floor.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
        print('PASS: independent triangular quadratic sums, squared norm allowances, actual Rayleigh ceilings, four strict old-gate witnesses and two positive controls')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
