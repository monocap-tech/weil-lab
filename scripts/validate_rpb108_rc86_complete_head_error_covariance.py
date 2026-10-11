"""RC86: complete correlated Riesz errors for the actual rank-38 head.

Replace the RC85 diagonal/block envelope by a complete direct Gram. No new source inputs or floors.
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
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root,entries,rows
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc60_twenty_two_mixed_residuals import init_worker,gram_worker
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,relative
DIM=64;HEAD=38;OLD=22;HIGH=16;RHO=F(252,257)
def diag(v):return [[x*F(i==j) for j in range(len(v))] for i,x in enumerate(v)]
def cong(C,A):return mm(mm(tr(C),A),C)
def progress(s):print(s,file=sys.stderr,flush=True)
def build_forms(V,cmid):
    ntrial=len(V); ntarget=len(V[0]);assert (ntrial,ntarget)==(64,38)
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
        base=polyadd([I(x) for x in P[j]],[I(tv[m]+cmid*v[m]) for m in range(ntrial)],-1)
        forms.append((polyadd(base,ka,-1),polyadd([I(x/2) for x in v],bl,-1),polyadd([I(x/2) for x in v],scalar(reflect(bl),(-1)**j),-1)))
        print('head form',j,'built',file=sys.stderr,flush=True)
    return forms,moments,R,eps

def fine_relative(A,B):
 high=F(1)
 while not psd(add(scale(B,high),A,-1)):high*=2
 low=F(0) if high==1 else high/2
 for _ in range(32):
  mid=(low+high)/2
  if psd(add(scale(B,mid),A,-1)):high=mid
  else:low=mid
 assert psd(add(scale(B,high),A,-1))
 return high

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths]
 residual,response,previous,direct,head,enriched,native,precision,source,prior=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['input_sha256']==hashes[:9] and prior['milestone']=='RC85'
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
 forms,mom,R,eps=build_forms(Vh,F(precision['constant_midpoint']))
 intervals=entries(direct['nominal_Legendre_residual_Gram_entry_enclosures'])
 assert len(intervals)==OLD*(OLD+1)//2
 for row in prior['additional_head_Legendre_operator_residual_squared_norm_enclosures']:
  j=row['Legendre_target'];intervals[j,j]=tuple(map(F,row['enclosure']))
 for i in range(HEAD):
  for j in range(i,HEAD):
   if (i-j)%2:intervals[i,j]=(F(0),F(0))
 saved_entries={} if saved is None else entries(saved['nominal_head_Legendre_operator_residual_Gram_entry_enclosures'])
 alljobs=[(i,j) for i in range(HEAD) for j in range(i,HEAD) if (i-j)%2==0]
 jobs=alljobs if replay else [(i,j) for i,j in alljobs if (i,j) not in intervals]
 assert len(alljobs)==380 and (replay or len(jobs)==232)
 with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(forms,mom,R,replay)) as pool:
  for i,j,value in pool.map(gram_worker,jobs):
   a,b=outward(value,10**20)
   if (i,j) in intervals:
    x,y=intervals[i,j];assert x<=a<=b<=y,(i,j);a,b=x,y
   if saved is not None:
    x,y=saved_entries[i,j];assert x<=a<=b<=y,(i,j);a,b=x,y
   intervals[i,j]=(a,b);progress('head residual Gram '+str((i,j))+' checked')
 assert len(intervals)==HEAD*(HEAD+1)//2
 Qcenter=[[F(0)]*HEAD for _ in range(HEAD)];allow=[F(0)]*HEAD
 for (i,j),(a,b) in intervals.items():
  Qcenter[i][j]=Qcenter[j][i]=(a+b)/2;half=(b-a)/2;allow[i]+=half
  if i!=j:allow[j]+=half
 Qu=[[Qcenter[i][j]+F(i==j)*allow[i] for j in range(HEAD)] for i in range(HEAD)];assert psd(Qu)
 mass=list(map(F,enriched['physical_mass']));D=diag(mass);G=matrix(enriched['recentered_nominal_metric_center']);delta=F(enriched['actual_recentered_metric_mass_error_upper'])
 Gl=add(G,D,-delta);Gu=add(G,D,delta)
 if replay:Th=[[sum((mass[k]*Vh[k][i]*Vh[k][j] for k in range(DIM)),F(0)) for j in range(HEAD)] for i in range(HEAD)]
 else:Th=cong(Vh,D)
 deltaL=2*F(precision['constant_radius'])+eps;t0=F(1,65536)
 Bhead,bround=rounded_bound(add(scale(Qu,1+t0),Th,(1+1/t0)*deltaL**2),1,10**30)
 Ehead=scale(Bhead,RHO);assert psd(Ehead)
 oldE=matrix(prior['head_Riesz_error_block_Loewner_upper_in_Legendre_targets'])
 error_improvement=psd(add(oldE,Ehead,-1))
 X=[[mass[i]*F(i==j) for j in range(HEAD)] for i in range(DIM)]
 J=mm(tr(X),Vh);base=add(add(J,tr(J)),cong(Vh,Gl),-1)
 Z=matrix(response['nominal_source_canonical_trial_response_coefficients']);Y=mm(tr(X),Z);energy=cong(Z,Gu)
 Mlo38=cong(Ci38,matrix(head['actual_canonical_native_Gram_Loewner_lower']))
 Mlo22=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 tau=F(previous['canonical_complement_embedding_norm_upper']);assert 0<tau**2<RHO
 Er=scale(matrix(residual['actual_physical_nominal_source_response_operator_residual_Gram_Loewner_upper']),tau**2)
 Et=matrix(previous['projected_canonical_source_transfer_Gram_Loewner_upper']);assert psd(Er) and psd(Et)
 oldA=matrix(prior['retained_actual_rank_38_projected_original_source_Gram_Loewner_upper'])
 def response_upper(Mu):
  inverseMu=inverse(Mu)
  if replay:
   A=mm(inverseMu,Y);capture=cong(A,Mu);assert mm(Mu,A)==Y and capture==mm(tr(Y),A)
  else:capture=cong(Y,inverseMu)
  Q=rounded_bound(add(energy,capture,-1),1,10**24)[0];assert psd(Q)
  return Q
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
   eta.append(fine_relative(hblock(add(Mu,Mlo38,-1),p),hblock(Mu,p)))
   kappa.append(fine_relative(hblock(E,p),hblock(Mu,p)))
   assert 0<eta[p]<1 and 0<kappa[p]
  coeff=[kappa[p]*(eta[p]/(1-eta[p]))**2 for p in range(2)]
  pert=[[coeff[i%2]*cap[i][j] for j in range(OLD)] for i in range(OLD)]
  v=[root(fine_relative(block(pert,p),block(Mlo22,p))/fine_relative(block(F0,p),block(Mlo22,p)),10**12) for p in range(2)]
  FF=rounded_bound([[(1+v[i%2])*F0[i][j]+(1+1/v[i%2])*pert[i][j] for j in range(OLD)] for i in range(OLD)],1,10**24)[0];assert psd(FF)
  return FF,eta,kappa,v
 def nominal_correlated(Q,FF,ws):
  # For A_true=M_actual^-1 Y, R A_true=Pi38 Z.
  # Z-V A_true lies in the 64-mode trial space, while
  # (R-V) A_true has Gram <= FF. Keep the near-orthogonality
  # of e=i*F_nom-Z to that space rather than a triangle bound.
  return [[Q[i][j]+Er[i][j]+sigma*(6*energy[i][j]+4*FF[i][j])+Omega[i][j]/sigma+ws[i%2]*FF[i][j]+Eglobal[i][j]/ws[i%2] for j in range(OLD)] for i in range(OLD)]
 Mu,mround=rounded_bound(add(base,Ehead),1,10**24)
 assert psd(Mu) and psd(add(Mu,Mlo38,-1))
 Q=response_upper(Mu);FF,etas,kappas,vs=true_coefficient_error(Ehead,Mu)
 assert Omega==matrix(prior['canonical_trial_space_response_error_projection_Gram_Loewner_upper'])
 assert Er==matrix(prior['projected_nominal_response_error_Gram_Loewner_upper']) and Et==matrix(prior['projected_original_source_transfer_Gram_Loewner_upper'])
 et=[fine_relative(block(Et,p),block(Mlo22,p)) for p in range(2)]
 best=[];candidate_records=[]
 for p in range(2):
  fbeta=fine_relative(block(FF,p),block(Mlo22,p));ebeta=fine_relative(block(Eglobal,p),block(Mlo22,p));wbal=root(ebeta/fbeta,10**12);chosen=None;records=[]
  for wm in [F(1,2),F(3,4),F(1),F(4,3),F(2)]:
   w=wbal*wm;nom=block(nominal_correlated(Q,FF,[w,w]),p);nb=fine_relative(nom,block(Mlo22,p));ubal=root(et[p]/nb,10**12)
   for um in [F(3,4),F(1),F(4,3)]:
    u=ubal*um;candidate=rounded_bound(add(scale(nom,1+u),block(Et,p),1+1/u),1,10**24)[0];lam=relative(candidate,block(Mlo22,p));data=(lam,w,u)
    records.append(dict(cross_error_Young_parameter=str(w),source_transfer_Young_parameter=str(u),actual_projected_original_source_relative_upper=str(lam)))
    if chosen is None or data<chosen:chosen=data
  best.append(chosen);candidate_records.append(dict(parity='even' if p==0 else 'odd',head_inverse_relative_uncertainty_upper=str(etas[p]),head_error_relative_head_Gram_upper=str(kappas[p]),coefficient_error_Young_parameter=str(vs[p]),actual_projection_coefficient_Riesz_error_relative_input_upper=str(fbeta),candidates=records));progress('correlated source attachment parity '+str(p)+' checked')
 ws=[x[1] for x in best];us=[x[2] for x in best];nominal=nominal_correlated(Q,FF,ws)
 if replay:raw=add([[nominal[i][j]*(1+us[i%2]) for j in range(OLD)] for i in range(OLD)],[[Et[i][j]*(1+1/us[i%2]) for j in range(OLD)] for i in range(OLD)])
 else:raw=[[(1+us[i%2])*nominal[i][j]+(1+1/us[i%2])*Et[i][j] for j in range(OLD)] for i in range(OLD)]
 A,arounding=rounded_bound(raw,1,10**24);assert psd(A)
 parity=[];use=[]
 for p in range(2):
  lam=relative(block(A,p),block(Mlo22,p));old=F(prior['parity_residual_certificates'][p]['retained_relative_upper']);keep=min(lam,old);use.append(lam<old)
  parity.append(dict(parity='even' if p==0 else 'odd',head_inverse_relative_uncertainty_upper=str(etas[p]),head_error_relative_head_Gram_upper=str(kappas[p]),coefficient_error_Young_parameter=str(vs[p]),cross_error_Young_parameter=str(ws[p]),source_transfer_Young_parameter=str(us[p]),new_response_attachment_relative_upper=str(lam),prior_retained_relative_upper=str(old),retained_relative_upper=str(keep),new_response_attachment_selected=lam<old))
 retained=[[A[i][j] if use[i%2] else oldA[i][j] for j in range(OLD)] for i in range(OLD)]
 for p in range(2):assert psd(add(scale(block(Mlo22,p),F(parity[p]['retained_relative_upper'])),block(retained,p),-1))
 bound=max(F(x['retained_relative_upper']) for x in parity);oldbound=F(prior['actual_rank_38_relative_bound_for_existing_22_source_inputs'])
 oldMu=matrix(prior['actual_head_Gram_Loewner_upper_in_Legendre_targets']);oldQ=matrix(prior['actual_rank_38_projected_response_Gram_Loewner_upper']);oldFF=matrix(prior['actual_projection_coefficient_Riesz_error_Gram_Loewner_upper'])
 diagcomparisons=[dict(Legendre_target=j,RC85_head_Riesz_error_squared_upper=str(oldE[j][j]),direct_head_Riesz_error_squared_upper=str(Ehead[j][j]),diagonal_upper_bound_improvement_factor=str(oldE[j][j]/Ehead[j][j])) for j in range(HEAD)]
 result=dict(milestone='RC86',status='PASS',input_sha256=hashes,actual_Riesz_projection_head_rank=HEAD,canonical_trial_dimension=DIM,source_input_features=list(range(OLD)),
  head_Riesz_error_target_features=list(range(HEAD)),nominal_head_Legendre_operator_residual_Gram_entry_enclosures=rows(intervals),nominal_head_operator_residual_Gram_Loewner_upper=serialize(Qu),nominal_interval_row_allowances=list(map(str,allow)),
  cached_RC81_low_head_entries_preserved_exactly=True,cached_RC85_additional_head_diagonals_preserved_exactly=True,new_same_parity_entries_evaluated=232,all_same_parity_entries_replayed=380,
  canonical_operator_correction_norm_upper=str(deltaL),operator_correction_Young_parameter=str(t0),physical_head_trial_Gram=serialize(Th),actual_physical_head_operator_residual_Gram_Loewner_upper=serialize(Bhead),operator_transport_rounding_row_allowances=list(map(str,bround)),
  actual_head_canonical_Riesz_error_Gram_Loewner_upper_in_Legendre_targets=serialize(Ehead),head_Riesz_error_whole_Loewner_improves_RC85=error_improvement,head_Riesz_error_diagonal_comparisons=diagcomparisons,
  actual_head_Gram_Loewner_upper_in_Legendre_targets=serialize(Mu),head_Gram_rounding_row_allowances=list(map(str,mround)),head_Gram_upper_whole_Loewner_improves_RC85=psd(add(oldMu,Mu,-1)),
  actual_projection_pairings_with_response_in_Legendre_targets=serialize(Y),actual_rank_38_projected_response_Gram_Loewner_upper=serialize(Q),projected_response_upper_whole_Loewner_improves_RC85=psd(add(oldQ,Q,-1)),
  canonical_trial_space_response_error_projection_Gram_Loewner_upper=serialize(Omega),trial_space_cross_Young_parameter=str(sigma),actual_projection_coefficient_Riesz_error_Gram_Loewner_upper=serialize(FF),coefficient_error_upper_whole_Loewner_improves_RC85=psd(add(oldFF,FF,-1)),
  projected_nominal_response_error_Gram_Loewner_upper=serialize(Er),projected_original_source_transfer_Gram_Loewner_upper=serialize(Et),response_error_and_original_source_transfer_uppers_unchanged=True,
  parameter_candidates=candidate_records,parity_residual_certificates=parity,correlated_nominal_projected_source_Gram_Loewner_upper=serialize(rounded_bound(nominal,1,10**24)[0]),response_attachment_actual_projected_original_source_Gram_Loewner_upper=serialize(A),source_attachment_rounding_row_allowances=list(map(str,arounding)),
  retained_actual_rank_38_projected_original_source_Gram_Loewner_upper=serialize(retained),actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_retained_relative_bound=str(oldbound),certified_fractional_upper_bound_reduction=str(1-bound/oldbound),
  new_response_attachment_whole_Loewner_improves_prior_retained=psd(add(oldA,A,-1)),actual_original_source_uncertainty_attached=True,actual_rank_38_projection_used=True,
  original_Riesz_trials_unchanged=True,RC83_response_coefficients_unchanged=True,required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,
  enlarged_Weil_floor_certified=False,enlarged_complement_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc84_direct_nominal_response_residual.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc82_direct_error_source_attachment.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc85_actual_response_projection_attachment.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
  print('PASS: all 380 same-parity head residual entries through reflected moments, exact projection capture, complete correlated source attachment and retained Gram checks')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
