"""RC210: correlated omitted-input regular action on four native tails.
Retains signed collective leading moments before taking tail norms.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,mul,div,bounds,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import cong,inv
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale
import validate_rpb108_rc206_directional_error_inverse as prev
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
EXTRA={'174_regular_source_tail_compression':'f0e3837e3dc0a6dc03cfa0d9195fa632348313bd','129_four_vector_joint_moment':'33e681e688450c987993603354544fe3919b435f','170_poisson_regular_action':'690b571c35d3f49302223b306488008c9b907272','183_materialized_w14_canonical_carrier':'4469fa1b92e6e1e9f08598ce707cfb43b240784a','181_psi_action_completion_dashboard':'ceed57e11d269b11b1aee30cfe215efab5c37ff0','188_extended_psi_endpoint_action':'91a4bf81150ecf6be696b1004b79a67c2bdbec50','190_extended_w14_endpoint_action':'aa139a1ddbb285b4c8fc20f5b8b90b910eeae529','193_extended_f0_regular_action':'299fc1207f0e90478e0bebd0e082e2981a8c514e','197_native_v10_canonical_action':'6e759211fbc8de8e4b6c4ed5fd4c62a5e5241455','200_extended_v10_endpoint_action':'3e0a948321e87b840dae6a83319a2d06dfc8eede'}
PINS.update({'certificates/rpb108_rc'+n+'.json':sha for n,sha in EXTRA.items()})
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc206_directional_error_inverse.py']='7ada815599b8d2b607aed030e38b8daa01801496'
O=32766

def run(reverse=False):
    for path,sha in HELPER_PINS.items():assert prev.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        b=(ROOT/path).read_bytes();assert prev.prev.blob(b)==sha,(path,'input Git blob mismatch');data[path]=json.loads(b)
    get=lambda n:data['certificates/rpb108_rc'+n+'.json']
    base=get('203_residual_enriched_six_source_inverse');joint=get('129_four_vector_joint_moment');regular=get('170_poisson_regular_action');source=get('183_materialized_w14_canonical_carrier');psi=get('181_psi_action_completion_dashboard');psiFull=get('188_extended_psi_endpoint_action');wfull=get('190_extended_w14_endpoint_action');ffull=get('193_extended_f0_regular_action');native=get('197_native_v10_canonical_action');vfull=get('200_extended_v10_endpoint_action')
    assert ffull['regular_input_degree']==wfull['retained_regular_input_degree']==native['finite_action_input_degree']==512
    assert psi['first_actual_psi_degree']==990 and psi['regular_psi_trial'].startswith('zero')
    assert regular['aperture']=='11/10'
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B);assert 0<sl<=sh
    g={2*i:F(x) for i,x in enumerate(source['native_w14_finite_coefficient_centers'])};v={2*i:F(x) for i,x in enumerate(source['Cg_finite_coefficient_centers'])}
    mu=list(map(F,source['analytic_moment_centers']));nu=list(map(F,native['native_analytic_moments']));lw=F(source['analytic_lambda']);lv=F(native['native_analytic_lambda'])
    assert len(g)==2048 and len(v)==4096 and len(mu)==15 and len(nu)==11 and lw==977132 and lv==4094*4095
    assert min(list(g.values())+list(v.values())+mu+nu)>=0
    H=[Z]
    for n in range(1,O+3):H.append(plus(H[-1],rat(F(1,n))))
    D={n:plus(H[n],(rat(sl)[0],rat(sh)[1])) for n in range(0,O+3,2)}
    def moment(ms,lam,z):
        out=Z;ids=list(range(len(ms)))
        if reverse:ids.reverse()
        for k in ids:out=plus(out,rat(ms[k]*F(lam,z)**k))
        return out
    gg=[[Z]*4 for _ in range(4)];degrees=list(range(514,O+1,2))
    if reverse:degrees.reverse()
    for n in degrees:
        eta=div(rat(F(2*n+1,n*(n+1))),D[n]);z=n*(n+1)
        us=[eta if n<=988 else Z,eta if n>=990 else Z,rat(g[n]) if n<=4094 else mul(eta,moment(mu,lw,z)),rat(v[n]) if n<=8190 else mul(eta,moment(nu,lv,z))]
        mass=rat(2*B/F(2*n+1))
        for i in range(4):
            for j in range(i,4):gg[i][j]=plus(gg[i][j],mul(mass,mul(us[i],us[j])))
        if n%8192==8190:print('RC210 collective regular-input prefix',n,flush=True)
    L=[[F(0)]*4 for _ in range(4)];U=[[F(0)]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i,4):lo,hi=bounds(gg[i][j]);L[i][j]=L[j][i]=lo;U[i][j]=U[j][i]=hi
    # Directed intervals are rounded outward onto the same rational grid;
    # reverse replay must reproduce every final certified matrix exactly.
    finiteLo,finiteHi,_=loewner(L,U,[F(1)]*4)
    z=(O+2)*(O+3);dl=F(D[O][0]);T=up(B/(dl*dl*(O-1)*O))
    dw=sum(mu[k]*F(lw,z)**k for k in range(1,len(mu)));dv=sum(nu[k]*F(lv,z)**k for k in range(1,len(nu)))
    leading=[F(0),F(1),mu[0],nu[0]]
    tail=scale(F(3,2)*T,prev.outer(leading));tail=prev.add(tail,[[6*T*(dw*dw if i==2 else dv*dv if i==3 else F(0)) if i==j else F(0) for j in range(4)] for i in range(4)])
    Gtail=prev.add(finiteHi,tail);assert psd(Gtail) and psd(tail)
    phi=F(ffull['regular_input_tail_smoothing_squared_factor_upper'])
    assert phi==F(wfull['regular_input_tail_smoothing_squared_factor_upper'])==F(native['regular_input_smoothing_squared_upper'])
    action=scale(phi/sl,Gtail)
    selected=base['selected_enclosure'];Y=mat(selected,'trial_basis_coefficients');indices=[2,3,4,6];EY=cong([Y[i] for i in indices],action);assert psd(EY)
    eps=list(map(F,base['individual_raw_trial_action_error_norm_upper']));removed=[F(ffull['regular_input_tail_D_action_error_norm_upper']),F(psi['complete_actual_D_inverse_Rpsi_error_norm_upper']),F(wfull['regular_input_tail_action_D_error_norm_upper']),F(native['regular_input_tail_D_error_norm_upper'])]
    assert eps[2]==F(ffull['canonical_f0_trial_D_error_norm_upper']) and eps[3]==F(psiFull['canonical_psi_source_form_full_D_error_norm_upper']) and eps[4]==F(wfull['complete_canonical_w14_action_D_error_norm_upper']) and eps[6]==F(vfull['complete_canonical_v10_action_D_error_norm_upper'])
    remainder=eps[:]
    for i,e in zip(indices,removed):remainder[i]-=e;assert remainder[i]>=0
    e=F(regular['e_upper']);pi=F(regular['pi_upper']);I2=up(e*pi*pi/3);band=F(513)/(6*pi*B);rr=F(789,125)
    assert phi==up(min(rr*rr,4*B*I2*up(F(11,12)**1026,10**80)+e*e/(band*band)))
    assert phi>0
    # The remainder bounds retain all other norm terms and outward rounding;
    # the additive decompositions are certified in the pinned source records.
    G=mat(base,'source_D_Gram_lower');Gi=inv(G)
    dual=[sum(Y[k][i]*Gi[i][j]*Y[k][j] for i in range(6) for j in range(6)) for k in range(8)]
    weights=[1/sqrtup(q) if q else F(1) for q in dual];Erem=prev.error_gram(Y,remainder,weights)
    tau=F(1,3);Etotal=prev.add(scale(1+tau,EY),scale(1+1/tau,Erem));assert psd(Etotal)
    x=list(map(F,['427/125000','-15419/1000000','84697/500000','-1','-600677/1000000','315051/500000']));q=lambda A:sum(x[i]*A[i][j]*x[j] for i in range(6) for j in range(6))
    oldProbe=sum(eps[k]*abs(sum(Y[k][j]*x[j] for j in range(6))) for k in range(8))**2
    return dict(milestone='RC210',starting_commit='2733eb54d1a7858f3d1d1c59be33df19e7207adf',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,regular_tail_source_order=['f0','psi0','w14','v10'],high_input_first_degree=514,finite_prefix_last_degree=O,actual_psi_first_degree=990,physical_input_tail_Gram_upper=ser(Gtail),physical_infinite_tail_Gram_upper=ser(tail),physical_eta_tail_energy_upper=str(T),common_leading_tail_moments=list(map(str,leading)),nonleading_w14_tail_amplitude_upper=str(dw),nonleading_v10_tail_amplitude_upper=str(dv),high_input_smoothing_squared_factor_upper=str(phi),D_metric_floor_lower=str(sl),collective_regular_tail_action_Gram_upper=ser(action),fixed_trial_collective_regular_tail_error_Gram_upper=ser(EY),removed_individual_regular_tail_norm_bounds=list(map(str,removed)),remaining_individual_action_error_norm_upper=list(map(str,remainder)),remaining_error_triangle_weights=list(map(str,weights)),remaining_action_error_Gram_upper=ser(Erem),selected_component_Young_tau=str(tau),complete_fixed_trial_action_error_Gram_upper=ser(Etotal),probe_coefficients=list(map(str,x)),old_individual_triangle_probe_squared_error=str(oldProbe),new_collective_probe_squared_error_upper=str(q(Etotal)),collective_probe_error_improved=q(Etotal)<oldProbe,operator_and_source_trial_carriers_unchanged=True,finite_regular_projection_and_nonregular_errors_retained=True,common_regular_operator_applied_after_signed_tail_combination=True,complex_response_mixtures_paid=True,all_physical_input_and_output_tails_paid=True,new_inverse_enclosure_evaluated=False,latest_certified_inverse_width_upper_unchanged='74677/125000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC211: transport the collective regular-tail error Gram through the coupled inverse and optimize component payments only with exact all-mixture verification')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(a.replay)
    if a.replay:assert json.loads(a.output.read_text())==r,'replay differs'
    else:a.output.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC210 PASS: collective probe error improved',r['collective_probe_error_improved'])
