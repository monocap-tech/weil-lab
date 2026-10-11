"""RC85: source response attached to the actual rank-38 Riesz projection.

Sharpen the head Gram with RC81's low-22 errors and direct diagonal errors
for the added sixteen Legendre targets. No new source inputs or floors.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
from concurrent.futures import ProcessPoolExecutor
import json,sys,hashlib
from validate_rpb108_rc35_enriched_residuals import I,PI,N,transformed,reflect,polyadd,scalar
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc60_twenty_two_mixed_residuals import init_worker,gram_worker
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,relative
DIM=64;HEAD=38;OLD=22;HIGH=16;RHO=F(252,257)
def diag(v):return [[x*F(i==j) for j in range(len(v))] for i,x in enumerate(v)]
def cong(C,A):return mm(mm(tr(C),A),C)
def progress(s):print(s,file=sys.stderr,flush=True)
def build_forms(V,cmid):
    ntrial=len(V); ntarget=len(V[0]);assert (ntrial,ntarget)==(64,16)
    assert all(V[i][j]==0 for i in range(ntrial) for j in range(ntarget) if (i-j)%2)
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(2*(N+ntrial+1)+1)]
    H2=[sum((F(1,k*k) for k in range(1,n+1)),F(0)) for n in range(len(H))]
    R=F(11,5);Z=I(1).exp()*2*PI*I(R);assert Z.h<42
    q=[I(0)]*N;l=[I(0)]*N;power=I(1)
    for n in range(1,N+1):
        power=power*Z/n
        if n%2==0:q[n-1]=(-1)**(n//2+1)*power/2
        else:
            sign=(-1)**((n-1)//2)
            q[n-1]=sign*power*I(H[n]+cmid-1)/PI
            l[n-1]=-sign*power/PI
    eps=F(4,3)*(N+ntrial)*F(42)**(N+1)/factorial(N+1);assert eps<F(1,10**40)
    moments=[[],[],[],[],[],[]];zeta=PI*PI/6
    for k in range(2*(N+ntrial)+1):
        a=k+1;ha=H[a];hb=H2[a]
        for value,arr in zip([I(F(1,a)),I(-F(1,a*a)),I(-ha/a),I(F(2,a**3)),I((ha*ha+hb)/a),I(ha/F(a*a)+hb/a)-zeta/a],moments):arr.append(value)
    P=[transformed(legendre(i)) for i in range(ntrial)];forms=[]
    for j in range(ntarget):
        v=[F(0)]*ntrial;tv=[F(0)]*ntrial
        for i in range(ntrial):
            for m,x in enumerate(P[i]):v[m]+=V[i][j]*x;tv[m]+=H[i]*V[i][j]*x
        al=[I(0)]*(N+ntrial);bl=[I(0)]*(N+ntrial)
        for p in range(N):
            for m,vm in enumerate(v):
                if vm==0:continue
                d=p+m+1;beta=F(factorial(p)*factorial(m),factorial(d))
                bl[d]=bl[d]+l[p]*I(vm*beta)
                al[d]=al[d]+(q[p]+l[p]*I(H[p]-H[d]))*I(vm*beta)
        ka=polyadd(al,reflect(al),(-1)**j)
        base=polyadd([I(x) for x in P[j+22]],[I(tv[m]+cmid*v[m]) for m in range(ntrial)],-1)
        forms.append((polyadd(base,ka,-1),polyadd([I(x/2) for x in v],bl,-1),polyadd([I(x/2) for x in v],scalar(reflect(bl),(-1)**j),-1)))
        print('additional head form',j+22,'built',file=sys.stderr,flush=True)
    return forms,moments,R,eps

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths]
 residual,response,previous,direct,head,enriched,native,precision,source=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [residual['input_sha256'][i] for i in [0,1,2,3,4]]==[hashes[i] for i in [1,8,5,6,7]]
 assert [response['input_sha256'][i] for i in [0,1,2,3,6,9]]==[hashes[i] for i in [4,5,6,7,8,2]]
 assert [previous['input_sha256'][i] for i in [0,2,3,5,6]]==[hashes[i] for i in [3,5,8,6,4]]
 assert direct['input_sha256'][2:]==[hashes[i] for i in [5,6,7]]
 assert head['input_sha256'][:2]==[hashes[i] for i in [5,6]]
 assert head['actual_orthogonal_projection_rank_certified']==HEAD and residual['source_input_features']==list(range(OLD))
 C38=matrix(head['chebyshev_to_legendre']);Ci38=inverse(C38)
 C22=matrix(native['chebyshev_to_legendre']);Ci22=inverse(C22)
 Vh=mm(matrix(head['native_trial_coefficients']),Ci38)
 Vlow=mm(matrix(enriched['enriched_native_trial_coefficients']),Ci22)
 assert [row[:OLD] for row in Vh]==Vlow
 forms,mom,R,eps=build_forms([row[OLD:] for row in Vh],F(precision['constant_midpoint']))
 intervals=[]
 with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(forms,mom,R,replay)) as pool:
  for i,j,value in pool.map(gram_worker,[(j,j) for j in range(HIGH)]):
   a,b=outward(value,10**20)
   if saved is not None:
    x,y=map(F,saved['additional_head_Legendre_operator_residual_squared_norm_enclosures'][i]['enclosure']);assert x<=a<=b<=y,(i,a,b);a,b=x,y
   intervals.append(dict(Legendre_target=i+OLD,enclosure=[str(a),str(b)]));progress('additional target '+str(i+OLD)+' residual diagonal checked')
 mass=list(map(F,enriched['physical_mass']));D=diag(mass);G=matrix(enriched['recentered_nominal_metric_center']);delta=F(enriched['actual_recentered_metric_mass_error_upper'])
 Gl=add(G,D,-delta);Gu=add(G,D,delta)
 Th=cong(Vh,D);deltaL=2*F(precision['constant_radius'])+eps;t0=F(1,65536)
 ehi=[]
 for j,row in enumerate(intervals):
  value=RHO*((1+t0)*F(row['enclosure'][1])+(1+1/t0)*deltaL**2*Th[j+OLD][j+OLD]);den=10**30
  ehi.append(F(-(-(value*den).numerator//(value*den).denominator),den))
 Elo=cong(Ci22,matrix(direct['actual_canonical_Riesz_error_Gram_Loewner_upper']));assert psd(Elo)
 X=[[mass[i]*F(i==j) for j in range(HEAD)] for i in range(DIM)]
 J=mm(tr(X),Vh);base=add(add(J,tr(J)),cong(Vh,Gl),-1)
 Z=matrix(response['nominal_source_canonical_trial_response_coefficients']);Y=mm(tr(X),Z);energy=cong(Z,Gu)
 Mlo38=cong(Ci38,matrix(head['actual_canonical_native_Gram_Loewner_lower']))
 Mlo22=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 tau=F(previous['canonical_complement_embedding_norm_upper']);assert 0<tau**2<RHO
 Er=scale(matrix(residual['actual_physical_nominal_source_response_operator_residual_Gram_Loewner_upper']),tau**2)
 Et=matrix(previous['projected_canonical_source_transfer_Gram_Loewner_upper']);assert psd(Er) and psd(Et)
 oldA=matrix(previous['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper'])
 def head_upper(nus):
  E=[[F(0)]*HEAD for _ in range(HEAD)]
  for i in range(HEAD):
   for j in range(HEAD):
    if i<OLD and j<OLD:E[i][j]=(1+nus[i%2])*Elo[i][j]
    elif i==j and i>=OLD:E[i][i]=(1+1/nus[i%2])*8*ehi[i-OLD]
  # Eight high-target errors in each parity block; Gram <= 8 diag.
  assert psd(E)
  Mu=rounded_bound(add(base,E),1,10**24)[0]
  assert psd(Mu) and psd(add(Mu,Mlo38,-1))
  return E,Mu
 def response_upper(Mu):
  inverseMu=inverse(Mu)
  if replay:
   A=mm(inverseMu,Y);capture=cong(A,Mu);assert mm(Mu,A)==Y and capture==mm(tr(Y),A)
  else:capture=cong(Y,inverseMu)
  Q=rounded_bound(add(energy,capture,-1),1,10**24)[0];assert psd(Q)
  return Q
 grid=[F(1,16),F(1,8),F(1,4),F(1,2),F(1),F(2),F(4),F(8),F(16)]
 best=[None,None];records=[]
 er=[relative(block(Er,p),block(Mlo22,p)) for p in range(2)];et=[relative(block(Et,p),block(Mlo22,p)) for p in range(2)]
 for nu in grid:
  E,Mu=head_upper([nu,nu]);Q=response_upper(Mu)
  row=dict(head_error_block_Young_parameter=str(nu),parity_candidates=[])
  for p in range(2):
   q=relative(block(Q,p),block(Mlo22,p));tbal=root(er[p]/q,10**12)
   nb=(1+tbal)*q+(1+1/tbal)*er[p];ubal=root(et[p]/nb,10**12)
   chosen=None
   for tm in [F(3,4),F(1),F(4,3)]:
    t=tbal*tm;nom=add(scale(block(Q,p),1+t),block(Er,p),1+1/t)
    for um in [F(3,4),F(1),F(4,3)]:
     u=ubal*um;candidate=rounded_bound(add(scale(nom,1+u),block(Et,p),1+1/u),1,10**24)[0]
     lam=relative(candidate,block(Mlo22,p));data=(lam,nu,t,u)
     if chosen is None or data<chosen:chosen=data
   lam,_,t,u=chosen
   row['parity_candidates'].append(dict(parity='even' if p==0 else 'odd',projected_response_component_relative_upper=str(q),response_error_component_relative_upper=str(er[p]),original_source_transfer_component_relative_upper=str(et[p]),response_Young_parameter=str(t),source_transfer_Young_parameter=str(u),actual_projected_original_source_relative_upper=str(lam)))
   if best[p] is None or chosen<best[p]:best[p]=chosen
  records.append(row);progress('head error block parameter '+str(nu)+' checked')
 # Preserve the conservative uncorrelated attachment as a diagnostic.
 uncorr=[dict(parity='even' if p==0 else 'odd',relative_upper=str(best[p][0]),head_error_block_Young_parameter=str(best[p][1]),response_Young_parameter=str(best[p][2]),source_transfer_Young_parameter=str(best[p][3])) for p in range(2)]
 H=[[F(a)+F(b) for a,b in row] for row in response['nominal_physical_Legendre_source_pairing_enclosures']];H=scale(H,F(1,2))
 Rh=[[(F(b)-F(a))/2 for a,b in row] for row in response['nominal_physical_Legendre_source_pairing_enclosures']]
 defect=add(H,mm(G,Z),-1);Di=diag([1/x for x in mass]);Kh=cong(Rh,Di)
 box=diag([sum(row,F(0)) for row in Kh])
 # Projection of the response error onto the physical polynomial trial
 # space has covariance <= Omega, since G_actual >= D.
 Omega=rounded_bound(scale(add(add(cong(defect,Di),box),cong(Z,D),delta**2),3),1,10**60)[0];assert psd(Omega)
 Eglobal=matrix(residual['actual_canonical_nominal_source_response_error_Gram_Loewner_upper'])
 sigma=F(1,10**20)
 def hblock(A,p):return [[A[i][j] for j in range(p,HEAD,2)] for i in range(p,HEAD,2)]
 def true_coefficient_error(E,Mu):
  A0=mm(inverse(Mu),Y);cap=cong(A0,Mu);F0=cong(A0,E)
  eta=[];kappa=[]
  for p in range(2):
   eta.append(relative(hblock(add(Mu,Mlo38,-1),p),hblock(Mu,p)))
   kappa.append(relative(hblock(E,p),hblock(Mu,p)))
   assert 0<eta[p]<1 and 0<kappa[p]
  coeff=[kappa[p]*(eta[p]/(1-eta[p]))**2 for p in range(2)]
  pert=[[coeff[i%2]*cap[i][j] for j in range(OLD)] for i in range(OLD)]
  v=[root(relative(block(pert,p),block(Mlo22,p))/relative(block(F0,p),block(Mlo22,p)),10**12) for p in range(2)]
  FF=rounded_bound([[(1+v[i%2])*F0[i][j]+(1+1/v[i%2])*pert[i][j] for j in range(OLD)] for i in range(OLD)],1,10**24)[0];assert psd(FF)
  return FF,eta,kappa,v
 def nominal_correlated(Q,FF,ws):
  # For A_true=M_actual^-1 Y, R A_true=Pi38 Z.
  # Z-V A_true lies in the 64-mode trial space, while
  # (R-V) A_true has Gram <= FF. Keep the near-orthogonality
  # of e=i*F_nom-Z to that space rather than a triangle bound.
  return [[Q[i][j]+Er[i][j]+sigma*(6*energy[i][j]+4*FF[i][j])+Omega[i][j]/sigma+ws[i%2]*FF[i][j]+Eglobal[i][j]/ws[i%2] for j in range(OLD)] for i in range(OLD)]
 corrbest=[None,None];corrrecords=[]
 for nu in [F(1,8),F(1,4),F(1,2),F(1)]:
  EE,MM=head_upper([nu,nu]);QQ=response_upper(MM);FF,etas,kappas,vs=true_coefficient_error(EE,MM)
  row=dict(head_error_block_Young_parameter=str(nu),parity_candidates=[])
  for p in range(2):
   fbeta=relative(block(FF,p),block(Mlo22,p));ebeta=relative(block(Eglobal,p),block(Mlo22,p));wbal=root(ebeta/fbeta,10**12);chosen=None
   for wm in [F(3,4),F(1),F(4,3)]:
    w=wbal*wm;nom=block(nominal_correlated(QQ,FF,[w,w]),p);nb=relative(nom,block(Mlo22,p));ubal=root(et[p]/nb,10**12)
    for um in [F(3,4),F(1),F(4,3)]:
     u=ubal*um;candidate=rounded_bound(add(scale(nom,1+u),block(Et,p),1+1/u),1,10**24)[0];lam=relative(candidate,block(Mlo22,p));data=(lam,nu,w,u)
     if chosen is None or data<chosen:chosen=data
   lam,_,w,u=chosen
   row['parity_candidates'].append(dict(parity='even' if p==0 else 'odd',head_inverse_relative_uncertainty_upper=str(etas[p]),head_error_relative_head_Gram_upper=str(kappas[p]),coefficient_error_Young_parameter=str(vs[p]),actual_projection_coefficient_Riesz_error_relative_input_upper=str(fbeta),cross_error_Young_parameter=str(w),source_transfer_Young_parameter=str(u),actual_projected_original_source_relative_upper=str(lam)))
   if corrbest[p] is None or chosen<corrbest[p]:corrbest[p]=chosen
  corrrecords.append(row);progress('correlated head error block parameter '+str(nu)+' checked')
 nus=[x[1] for x in corrbest];Ehead,Mu=head_upper(nus);Q=response_upper(Mu);FF,etas,kappas,vs=true_coefficient_error(Ehead,Mu)
 ws=[x[2] for x in corrbest];us=[x[3] for x in corrbest];nominal=nominal_correlated(Q,FF,ws)
 if replay:
  raw=add([[nominal[i][j]*(1+us[i%2]) for j in range(OLD)] for i in range(OLD)],[[Et[i][j]*(1+1/us[i%2]) for j in range(OLD)] for i in range(OLD)])
 else:raw=[[(1+us[i%2])*nominal[i][j]+(1+1/us[i%2])*Et[i][j] for j in range(OLD)] for i in range(OLD)]
 A=rounded_bound(raw,1,10**24)[0];assert psd(A)
 parity=[];use=[]
 for p in range(2):
  lam=relative(block(A,p),block(Mlo22,p));old=F(previous['parity_residual_certificates'][p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper'])
  keep=min(lam,old);use.append(lam<old)
  parity.append(dict(parity='even' if p==0 else 'odd',head_error_block_Young_parameter=str(nus[p]),head_inverse_relative_uncertainty_upper=str(etas[p]),head_error_relative_head_Gram_upper=str(kappas[p]),coefficient_error_Young_parameter=str(vs[p]),cross_error_Young_parameter=str(ws[p]),source_transfer_Young_parameter=str(us[p]),new_response_attachment_relative_upper=str(lam),RC82_relative_upper=str(old),retained_relative_upper=str(keep),new_response_attachment_selected=lam<old))
 retained=[[A[i][j] if use[i%2] else oldA[i][j] for j in range(OLD)] for i in range(OLD)]
 for p in range(2):assert psd(add(scale(block(Mlo22,p),F(parity[p]['retained_relative_upper'])),block(retained,p),-1))
 sharp_whole=psd(add(scale(diag(mass[:HEAD]),RHO),Mu,-1))
 oldbound=F(previous['actual_rank_38_relative_bound_for_existing_22_source_inputs']);bound=max(F(x['retained_relative_upper']) for x in parity)
 result=dict(milestone='RC85',status='PASS',input_sha256=hashes,actual_Riesz_projection_head_rank=HEAD,canonical_trial_dimension=DIM,source_input_features=list(range(OLD)),
  original_source_definition=source['original_source_definition'],additional_head_Legendre_operator_residual_squared_norm_enclosures=intervals,
  additional_head_canonical_Riesz_error_squared_norm_uppers=list(map(str,ehi)),canonical_operator_correction_norm_upper=str(deltaL),additional_error_Young_parameter=str(t0),
  head_Riesz_error_block_Loewner_upper_in_Legendre_targets=serialize(Ehead),actual_head_Gram_Loewner_upper_in_Legendre_targets=serialize(Mu),
  head_Gram_upper_whole_Loewner_improves_RC70=sharp_whole,actual_projection_pairings_with_response_in_Legendre_targets=serialize(Y),
  actual_rank_38_projected_response_Gram_Loewner_upper=serialize(Q),projected_nominal_response_error_Gram_Loewner_upper=serialize(Er),projected_original_source_transfer_Gram_Loewner_upper=serialize(Et),
  uncorrelated_parameter_candidates=records,uncorrelated_parity_certificates=uncorr,correlated_parameter_candidates=corrrecords,parity_residual_certificates=parity,
  canonical_trial_space_response_error_projection_Gram_Loewner_upper=serialize(Omega),trial_space_cross_Young_parameter=str(sigma),actual_projection_coefficient_Riesz_error_Gram_Loewner_upper=serialize(FF),correlated_nominal_projected_source_Gram_Loewner_upper=serialize(rounded_bound(nominal,1,10**24)[0]),response_attachment_actual_projected_original_source_Gram_Loewner_upper=serialize(A),
  retained_actual_rank_38_projected_original_source_Gram_Loewner_upper=serialize(retained),actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),
  prior_RC82_relative_bound=str(oldbound),certified_fractional_upper_bound_reduction=str(1-bound/oldbound),
  actual_rank_38_projected_response_evaluated_by_enclosure=True,actual_original_source_uncertainty_attached=True,
  original_Riesz_trials_unchanged=True,RC83_response_coefficients_unchanged=True,new_response_attachment_whole_Loewner_improves_RC82=psd(add(oldA,A,-1)),
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,
  enlarged_Weil_floor_certified=False,enlarged_complement_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc84_direct_nominal_response_residual.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc82_direct_error_source_attachment.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc68_enriched_original_source_covariance.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
  print('PASS: reflected additional head residual diagonals, exact variational projection capture, independent source attachment and retained Gram comparisons')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
