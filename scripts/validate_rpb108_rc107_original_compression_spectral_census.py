"""RC107: exact spectral census of the original 22-feature compression.
Compression counts are not full-operator upper counts or spectral coverage.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd,inverse
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root,entries
from validate_rpb108_rc65_parity_projected_residual_refinement import cong,add,scale
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc92_signed_weak_head_reconstruction import bil
from validate_rpb108_rc99_signed_source_projection_bounds import upper
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down
FIXED=[{'parity': 'even', 'vectors': [['62216809122179/125000000000000', '0', '-1', '0', '808418863058781/1000000000000000', '0', '-262993318733053/500000000000000', '0', '274461750225521/1000000000000000', '0', '-57050450225737/500000000000000', '0', '37394322051949/1000000000000000', '0', '-9488477601933/1000000000000000', '0', '1800323616357/1000000000000000', '0', '-236182641949/1000000000000000', '0', '17000201977/1000000000000000', '0'], ['6947662894421/15625000000000', '0', '-111790418584781/200000000000000', '0', '-358630531469671/1000000000000000', '0', '1', '0', '-972354695215087/1000000000000000', '0', '583948920375881/1000000000000000', '0', '-15016123613019/62500000000000', '0', '6918148778867/100000000000000', '0', '-1689271020903/125000000000000', '0', '158274764611/100000000000000', '0', '-66636023367/1000000000000000', '0'], ['-433756364200327/1000000000000000', '0', '43684020182241/250000000000000', '0', '938067111124521/1000000000000000', '0', '-486226256514459/1000000000000000', '0', '-677219126074841/1000000000000000', '0', '1', '0', '-37187942545691/62500000000000', '0', '48629320316783/250000000000000', '0', '-15613826460117/500000000000000', '0', '-42750829531/62500000000000', '0', '1143252475463/1000000000000000', '0'], ['-271752964473333/500000000000000', '0', '-301109579776293/1000000000000000', '0', '1', '0', '886364256994233/1000000000000000', '0', '-25374841328937/40000000000000', '0', '-3169626987423/4000000000000', '0', '852933291372623/1000000000000000', '0', '-235128285832847/1000000000000000', '0', '-8116583771791/250000000000000', '0', '5718344740959/200000000000000', '0', '341602819331/100000000000000', '0'], ['7228051359213/500000000000000', '0', '36741901455223/500000000000000', '0', '41765551103617/250000000000000', '0', '96478383290923/500000000000000', '0', '10574837342921/500000000000000', '0', '-72151950869933/250000000000000', '0', '-301352543687113/1000000000000000', '0', '358617755806099/1000000000000000', '0', '711024984159599/1000000000000000', '0', '-1', '0', '138819647784167/200000000000000', '0'], ['564406838613539/1000000000000000', '0', '853642214673153/1000000000000000', '0', '133275807204511/1000000000000000', '0', '-42501277693027/62500000000000', '0', '-1', '0', '-12682800613123/31250000000000', '0', '259704900195011/500000000000000', '0', '25020281502319/62500000000000', '0', '-267252807092497/1000000000000000', '0', '-243615699843157/1000000000000000', '0', '102251374143149/1000000000000000', '0'], ['-528017290752347/1000000000000000', '0', '-1', '0', '-830627745784667/1000000000000000', '0', '-281415559665161/500000000000000', '0', '-32477775257573/125000000000000', '0', '3658727663709/250000000000000', '0', '34058451322307/100000000000000', '0', '299572637935173/500000000000000', '0', '-173508504240409/1000000000000000', '0', '-61241918421327/125000000000000', '0', '-502283475928067/1000000000000000', '0'], ['501996089306627/1000000000000000', '0', '1', '0', '247222525082701/250000000000000', '0', '97742643323771/100000000000000', '0', '981404066718291/1000000000000000', '0', '198772265618871/200000000000000', '0', '918070438046809/1000000000000000', '0', '17399973804883/25000000000000', '0', '607961941152213/1000000000000000', '0', '119213798962673/500000000000000', '0', '-6415602000213/500000000000000', '0'], ['-20490504129037/1000000000000000', '0', '-22909850605791/500000000000000', '0', '-15162264406973/250000000000000', '0', '-84317447444049/1000000000000000', '0', '-1163695807299/10000000000000', '0', '-95445342781387/500000000000000', '0', '-212586690692867/500000000000000', '0', '-167684992745889/200000000000000', '0', '-492511497872561/500000000000000', '0', '-1', '0', '-56653293609433/100000000000000', '0'], ['317770918711623/1000000000000000', '0', '86265679121033/125000000000000', '0', '41945625663857/50000000000000', '0', '1', '0', '979855761260187/1000000000000000', '0', '667765095918911/1000000000000000', '0', '128023325679381/250000000000000', '0', '749310272003783/1000000000000000', '0', '-54651831779491/125000000000000', '0', '90130794432799/250000000000000', '0', '896645843910371/1000000000000000', '0'], ['-26740892020197/100000000000000', '0', '-554726530735981/1000000000000000', '0', '-572105623369913/1000000000000000', '0', '-433917759499629/1000000000000000', '0', '24325300422177/250000000000000', '0', '937589039110537/1000000000000000', '0', '1', '0', '-43124019869667/125000000000000', '0', '206042588554713/1000000000000000', '0', '101737127311807/500000000000000', '0', '185711949419449/200000000000000', '0']]}, {'parity': 'odd', 'vectors': [['0', '156228102083443/500000000000000', '0', '-861099899178791/1000000000000000', '0', '1', '0', '-382219722128951/500000000000000', '0', '52768972282829/125000000000000', '0', '-173858027381887/1000000000000000', '0', '53754149224557/1000000000000000', '0', '-491910039219/40000000000000', '0', '1984243606043/1000000000000000', '0', '-198221625273/1000000000000000', '0', '1891975259/250000000000000'], ['0', '471268655618383/1000000000000000', '0', '-906218556747379/1000000000000000', '0', '70850884637621/500000000000000', '0', '16233466765043/20000000000000', '0', '-1', '0', '622229084347487/1000000000000000', '0', '-120382634355629/500000000000000', '0', '29377653894073/500000000000000', '0', '-7623281305929/1000000000000000', '0', '-47602744413/500000000000000', '0', '91093527023/500000000000000'], ['0', '2227659100377/3125000000000', '0', '-705577452760559/1000000000000000', '0', '-447002533595629/500000000000000', '0', '337217686042537/500000000000000', '0', '684340370604071/1000000000000000', '0', '-1', '0', '19882917624961/40000000000000', '0', '-100186377007271/1000000000000000', '0', '-2652202963749/250000000000000', '0', '10699125656037/1000000000000000', '0', '-1738827507099/1000000000000000'], ['0', '-41481735979/4000000000000', '0', '-39012218874799/500000000000000', '0', '-71374764451023/1000000000000000', '0', '8166008080259/62500000000000', '0', '355004774401607/1000000000000000', '0', '60493038669147/500000000000000', '0', '-16425266208161/31250000000000', '0', '-110097630064911/500000000000000', '0', '1', '0', '-168707357671779/200000000000000', '0', '14065151671873/40000000000000'], ['0', '-1', '0', '-45987292876657/500000000000000', '0', '919224895855749/1000000000000000', '0', '931938633296891/1000000000000000', '0', '-112304961174337/500000000000000', '0', '-5254444836859/6250000000000', '0', '241790760323311/1000000000000000', '0', '18775642984599/200000000000000', '0', '132087379464181/1000000000000000', '0', '-46952077553339/200000000000000', '0', '82083255302873/1000000000000000'], ['0', '-1', '0', '-194407056432019/250000000000000', '0', '-368327169900859/1000000000000000', '0', '33590565803547/250000000000000', '0', '577237851503169/1000000000000000', '0', '191611229079383/250000000000000', '0', '402572044730193/1000000000000000', '0', '-484648937294083/1000000000000000', '0', '-1021892187171/1000000000000000', '0', '445945807361559/1000000000000000', '0', '165966375243259/500000000000000'], ['0', '-385393931340631/500000000000000', '0', '-754075683245899/1000000000000000', '0', '-35303064173543/50000000000000', '0', '-299188623240197/500000000000000', '0', '-49150232942321/125000000000000', '0', '-29867814725133/500000000000000', '0', '381525338412203/1000000000000000', '0', '201673970061613/250000000000000', '0', '1', '0', '59412662054701/100000000000000', '0', '-51136101527707/500000000000000'], ['0', '-15045411905583/20000000000000', '0', '-45820586237697/62500000000000', '0', '-43181361344223/62500000000000', '0', '-155025126431521/250000000000000', '0', '-259113146159613/500000000000000', '0', '-404863882493403/1000000000000000', '0', '-375915585858583/1000000000000000', '0', '-559191229355671/1000000000000000', '0', '-76325156394683/100000000000000', '0', '-1', '0', '-108181135488751/125000000000000'], ['0', '215078540755459/250000000000000', '0', '872900735128943/1000000000000000', '0', '28044030537229/31250000000000', '0', '233017366963311/250000000000000', '0', '486020872103537/500000000000000', '0', '1', '0', '481603554198051/500000000000000', '0', '391813773574123/500000000000000', '0', '24426563241233/50000000000000', '0', '83474451037017/500000000000000', '0', '1916628686107/1000000000000000'], ['0', '-912629987795759/1000000000000000', '0', '-868157368995159/1000000000000000', '0', '-43181561247171/62500000000000', '0', '-299316913560119/1000000000000000', '0', '3130063628041/25000000000000', '0', '17865965590179/200000000000000', '0', '-10529377239989/200000000000000', '0', '1', '0', '-515704994990683/1000000000000000', '0', '-6643198187341/20000000000000', '0', '76759277005859/100000000000000'], ['0', '-2819584021301/250000000000000', '0', '107463688223221/1000000000000000', '0', '374922404827563/1000000000000000', '0', '45832148826883/62500000000000', '0', '399913292115373/500000000000000', '0', '-2668929349861/250000000000000', '0', '-1', '0', '59024313324347/1000000000000000', '0', '-955293707493/1000000000000000', '0', '59307781867201/200000000000000', '0', '-174815663944451/250000000000000']]}]
RHO=F(252,257)

def inertia(A,replay=False):
 # Nonzero unpivoted LDL pivots suffice for these fixed test matrices.
 # Replay uses leading principal determinant ratios (fraction-free Bareiss).
 if replay:
  def det(B):
   B=[r[:] for r in B];old=F(1)
   for k in range(len(B)-1):
    pivot=B[k][k];assert pivot!=0
    for i in range(k+1,len(B)):
     for j in range(k+1,len(B)):B[i][j]=(pivot*B[i][j]-B[i][k]*B[k][j])/old
    old=pivot
   return B[-1][-1]
  ds=[F(1)]+[det([r[:k] for r in A[:k]]) for k in range(1,len(A)+1)]
  pivots=[ds[k+1]/ds[k] for k in range(len(A))]
 else:
  B=[r[:] for r in A];pivots=[]
  for k in range(len(B)):
   pivot=B[k][k];assert pivot!=0;pivots.append(pivot)
   for i in range(k+1,len(B)):
    for j in range(k+1,len(B)):B[i][j]-=B[i][k]*B[k][j]/pivot
 return dict(negative=sum(x<0 for x in pivots),zero=0,positive=sum(x>0 for x in pivots))

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,old,enriched,native,source,residual,norm,compact,tail,response,response_residual=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC106' and old['milestone']=='RC104'
 assert old['input_sha256'][6:11]==h[2:7] and old['input_sha256'][11]==h[7] and old['input_sha256'][4]==h[8]
 assert compact['canonical_embedding_and_adjoint_compactness_analytic_proof_supplied']
 assert F(tail['inherited_1250_complement_floor'])==F(247,2500)>F(1,100)
 assert response_residual['input_sha256'][:4]==[h[x] for x in [9,4,2,3]]
 assert response['input_sha256'][1:3]==h[2:4] and response['input_sha256'][6]==h[4]
 Z=matrix(response['nominal_source_canonical_trial_response_coefficients']);RE=entries(response_residual['nominal_complete_physical_response_residual_Gram_entries']);deltaResp=F(response_residual['actual_canonical_operator_correction_norm_upper'])
 V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);G0=matrix(enriched['recentered_nominal_metric_center']);mass=list(map(F,enriched['physical_mass']));T=cong(V,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)])
 X=[[mass[i]*C[i][j] if i<22 else F(0) for j in range(22)] for i in range(64)];J=mm(tr(X),V);GT=cong(V,G0)
 H=matrix(source['nominal_original_trial_source_pairing_center']);Rh=matrix(source['nominal_original_trial_source_pairing_halfwidths']);Q0=add(add(GT,H),tr(J),-1)
 Q0=[[(Q0[i][j]+Q0[j][i])/2 for j in range(22)] for i in range(22)];Rh=[[(Rh[i][j]+Rh[j][i])/2 for j in range(22)] for i in range(22)]
 ER=entries(residual['nominal_Legendre_residual_Gram_entry_enclosures']);U=entries(source['nominal_complete_original_source_Gram_entries']);delta=F(source['actual_source_approximation_operator_error_upper']);deltaL=F(residual['actual_operator_correction_norm_upper']);dg=F(enriched['actual_recentered_metric_mass_error_upper']);nu=F(1,65536);blocks=[]
 for p,name in enumerate(['even','odd']):
  vs=[list(map(F,x)) for x in FIXED[p]['vectors']];assert len(vs)==11 and all(v[k]==0 for v in vs for k in range(22) if k%2!=p)
  zs=tr(mm(C,tr(vs)));tw=[[dot(v,T,w,replay) for w in vs] for v in vs];jt=[[bil(v,J,w,replay) for w in vs] for v in vs];gt=[[bil(v,GT,w,replay) for w in vs] for v in vs]
  ec=[[F(0)]*11 for _ in range(11)];er=[[F(0)]*11 for _ in range(11)]
  for i in range(11):
   for j in range(i,11):ec[i][j],er[i][j]=contract_interval(zs[i],ER,zs[j],replay);ec[j][i]=ec[i][j];er[j][i]=er[i][j]
  Ep=scale(add(scale(upper(ec,er,[F(1)]*11,replay),1+nu),tw,(1+1/nu)*deltaL**2),RHO**2);Ec=scale(Ep,1/RHO)
  Ep=rounded_bound(Ep,1,10**40)[0];Ec=scale(Ep,1/RHO)
  # M=J+J* - V*G_actual V + Gram_canonical(Riesz error).
  ml=add(add(add(jt,tr(jt)),gt,-1),tw,-dg);mu=add(add(ml,tw,2*dg),Ec);ml=rounded_bound(ml,-1,10**40)[0];mu=rounded_bound(mu,1,10**40)[0];assert pd(ml) and psd(add(mu,ml,-1))
  epd=[up(RHO**2*((1+nu)*(ec[i][i]+er[i][i])+(1+1/nu)*deltaL**2*tw[i][i]),10**60) for i in range(11)];ecd=[x/RHO for x in epd]
  vz=mm(V,tr(vs));zz=mm(Z,tr(vs));tz=cong(zz,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]);ez=[]
  for i in range(11):
   u,r=contract_interval(vs[i],RE,vs[i],replay)
   ez.append(up(RHO*(root(u+r,10**40)+deltaResp*root(tz[i][i],10**40)+delta*root(tw[i][i],10**40))**2,10**50))
  # Exact nominal <Riesz_i-V_i,Z_j>; actual metric correction paid separately.
  target_z=[[sum((mass[n]*zs[i][n]*zz[n][j] for n in range(22)),F(0)) for j in range(11)] for i in range(11)]
  ezcenter=add(target_z,mm(mm(tr(vz),G0),zz),-1)
  k=F(norm['complete_physical_operator_parity_norm_upper'][p]);qc=[[F(0)]*11 for _ in range(11)];qr=[[F(0)]*11 for _ in range(11)];signed=[]
  for i in range(11):
   for j in range(i,11):
    center=bil(vs[i],Q0,vs[j],replay)+ezcenter[i][j]+ezcenter[j][i];trial=bil(list(map(abs,vs[i])),Rh,list(map(abs,vs[j])),replay)+(delta+dg)*root(tw[i][i]*tw[j][j],10**40)
    linear=root(ecd[i]*ez[j],10**40)+root(ecd[j]*ez[i],10**40)+dg*(root(tw[i][i]*tz[j][j],10**40)+root(tw[j][j]*tz[i][i],10**40));physical=k*root(epd[i]*epd[j],10**40);can=ecd[i] if i==j else root(ecd[i]*ecd[j],10**40)
    lo=down(center-trial-linear-physical-can,10**40);hi=up(center+trial+linear+physical+(can if i!=j else 0),10**40)
    qc[i][j]=qc[j][i]=(lo+hi)/2;qr[i][j]=qr[j][i]=(hi-lo)/2;signed.append(dict(i=i,j=j,actual_original_Weil_entry_enclosure=[str(lo),str(hi)]))
  radii=[sum(row,F(0)) for row in qr];qu=[[qc[i][j]+F(i==j)*radii[i] for j in range(11)] for i in range(11)];ql=[[qc[i][j]-F(i==j)*radii[i] for j in range(11)] for i in range(11)]
  assert psd(add(qu,qc,-1)) and psd(add(qc,ql,-1))
  census=[]
  for beta in [F(1,1000),F(1,100),F(1,10),F(1,2),F(1),F(3,2),F(2)]:
   lower=inertia(add(ql,mu,-beta),replay);higher=inertia(add(qu,ml,-beta),replay)
   assert higher['negative']<=lower['negative']
   census.append(dict(threshold=str(beta),compression_eigenvalues_strictly_below_threshold_count_lower=higher['negative'],compression_eigenvalues_strictly_below_threshold_count_upper=lower['negative'],exact_count_certified=higher==lower,lower_endpoint_inertia=lower,upper_endpoint_inertia=higher,full_operator_below_threshold_count_lower=higher['negative'],full_operator_upper_count_inferred=False))
  assert census[1]['exact_count_certified'] and census[1]['compression_eigenvalues_strictly_below_threshold_count_lower']==5
  response_rows=[]
  for i in range(11):
   theta=up(qc[i][i]/((ml[i][i]+mu[i][i])/2),10**25)
   f=[zz[n][i]-theta*vz[n][i] for n in range(64)]
   tf=sum((mass[n]*f[n]**2 for n in range(64)),F(0));trial_norm=bil(f,G0,f,replay)+dg*tf;assert trial_norm>=0
   # A_Q Riesz_i = Z_i + e_response_i + i* K physical_Riesz_error_i.
   bound=up(root(trial_norm,10**40)+root(ez[i],10**40)+root(RHO,10**40)*k*root(epd[i],10**40)+abs(theta)*root(ecd[i],10**40),10**40)
   radius=up(root(bound*bound/ml[i][i],10**40),10**40)
   response_rows.append(dict(candidate_index=i,exact_rational_Ritz_center=str(theta),original_operator_action_residual_norm_upper=str(bound),original_operator_spectral_distance_upper=str(radius),original_spectral_inclusion_interval=[str(theta-radius),str(theta+radius)],source_response_error_canonical_squared_upper=str(ez[i]),actual_physical_Riesz_error_squared_upper=str(epd[i]),actual_canonical_Riesz_error_squared_upper=str(ecd[i]),outside_native_22_coupling_column_squared_upper=str(bound*bound),spectral_inclusion_interval_strictly_below_essential_spectrum=theta+radius<1))
  coupled_Gram=[[F(i==j)*5*F(response_rows[i]['outside_native_22_coupling_column_squared_upper']) for j in range(5)] for i in range(5)]
  # Balanced exact interval lower preserves weak/strong correlations.
  balance=[1/root(abs(qc[i][i]),10**40) for i in range(11)]
  br=[sum((qr[i][j]*balance[j]/balance[i] for j in range(11)),F(0)) for i in range(11)]
  balanced=[[qc[i][j]-F(i==j)*br[i] for j in range(11)] for i in range(11)];balanced=rounded_bound(balanced,-1,10**60)[0]
  assert psd(add(qc,balanced,-1))
  assert pd(balanced) and inertia(balanced,replay)==dict(negative=0,zero=0,positive=11)
  def certified_floor(A,M):
   for power in range(10,41):
    beta=F(1,10**power)
    if pd(add(A,M,-beta)):
     assert inertia(add(A,M,-beta),replay)['positive']==len(A)
     return beta
   raise AssertionError('no positive tested floor')
  native_floor=certified_floor(balanced,mu)
  def sub(A,ix):return [[A[i][j] for j in ix] for i in ix]
  iw=list(range(5));is_=list(range(5,11));m0=add(add(jt,tr(jt)),gt,-1)
  assert pd(add(sub(ml,iw),[[F(i==j) for j in range(5)] for i in range(5)],-1))
  assert pd(add(sub(ml,is_),[[F(i==j,5) for j in range(6)] for i in range(6)],-1))
  crossFrob=sum(((abs(m0[i][j])+dg*root(tw[i][i]*tw[j][j],10**40)+root(ecd[i]*ecd[j],10**40))**2 for i in iw for j in is_),F(0))
  crossFrob=up(crossFrob,10**50)
  projdelta=root(5*crossFrob,10**40);trialbeta=F(3,200) if p==0 else F(1,10)
  assert pd(add(sub(ql,is_),sub(mu,is_),-trialbeta))
  projection_floor=trialbeta-(1+RHO*k)*(2*projdelta+projdelta*projdelta)
  explicit_floor=down(projection_floor,10**6);assert explicit_floor>0
  projection_cert=dict(exceptional_candidate_dimension=5,remaining_native_orthogonal_dimension=6,weak_coordinate_metric_lower='1',strong_coordinate_metric_lower='1/5',canonical_metric_cross_Frobenius_squared_upper=str(up(crossFrob,10**50)),canonical_projection_relative_norm_upper=str(projdelta),fixed_high_candidate_span_original_floor=str(trialbeta),actual_native_canonical_orthogonal_complement_original_floor=str(explicit_floor),floor_is_full_operator_outside_candidate_span=False,original_operator_norm_upper=str(1+RHO*k),actual_orthogonal_projection_not_numerically_substituted=True)
  strong=sub(balanced,is_);mix=[[balanced[i][j] for j in is_] for i in iw];strong_inverse=inverse(strong)
  assert mm(strong,strong_inverse)==[[F(i==j) for j in range(6)] for i in range(6)]
  schur=add(sub(balanced,iw),mm(mm(mix,strong_inverse),tr(mix)),-1);schur=rounded_bound(schur,-1,10**60)[0]
  assert pd(schur) and inertia(schur,replay)['positive']==5
  schur_floor=certified_floor(schur,sub(mu,iw))
  native_positive=dict(balance_scales=list(map(str,balance)),balanced_original_Weil_Loewner_lower=serialize(balanced),full_parity_compression_original_positive_floor=str(native_floor),five_candidate_after_six_native_directions_Schur_Loewner_lower=serialize(schur),five_candidate_native_Schur_margin_relative_canonical_metric_lower=str(schur_floor),exceptional_block_and_all_native_couplings_certified_positive=True,scope='Original parity native eleven-space only; omitted original operator and the 1250-head complement have not been eliminated.')
  beta_max=F(1,10) if p==0 else F(1,2);idx=2 if p==0 else 3
  assert census[idx]['compression_eigenvalues_strictly_below_threshold_count_lower']>=6
  method=[]
  for i in range(5):
   hi=next(F(x['actual_original_Weil_entry_enclosure'][1]) for x in signed if x['i']==i and x['j']==i);u=F(response_rows[i]['outside_native_22_coupling_column_squared_upper']);ratio=u/(beta_max*hi);assert hi>0 and ratio>1
   method.append(dict(candidate_index=i,actual_exceptional_diagonal_upper=str(hi),individual_action_residual_squared_allowance=str(u),allowance_over_maximum_five_mode_Schur_diagonal_budget=str(ratio),inherited_allowance_cannot_pass_five_mode_scalar_floor_Schur=True))
  blocks.append(dict(parity=name,actual_native_Riesz_span_dimension=11,fixed_rational_native_coordinates=FIXED[p]['vectors'],actual_canonical_Gram_Loewner_lower=serialize(ml),actual_canonical_Gram_Loewner_upper=serialize(mu),targeted_actual_physical_Riesz_error_Gram_upper=serialize(Ep),signed_original_Weil_entry_enclosures=signed,actual_original_Weil_Loewner_lower=serialize(ql),actual_original_Weil_Loewner_upper=serialize(qu),spectral_census=census,original_native_positivity_and_exceptional_Schur_certificate=native_positive,explicit_native_orthogonal_floor_certificate=projection_cert,original_operator_action_and_spectral_inclusion_certificates=response_rows,first_five_outside_native_22_coupling_Gram_Loewner_upper=serialize(coupled_Gram),coupled_Gram_scope='Actual P_(native22 perpendicular) A_Q and also P_(candidate five-span perpendicular) A_Q on the five fixed rational columns; not exact compression spectral eigenvectors or complement-eliminated F responses.',any_five_dimensional_parity_exception_strong_floor_upper=str(beta_max),individual_norm_coupling_budget_rejections=method,compression_exceptional_dimension_below_one_hundredth=5,compression_spectral_floor_on_remaining_six_modes='1/100',compression_spectral_subspace_is_not_an_original_operator_invariant_subspace=True))
 out=dict(milestone='RC107',status='PASS',input_sha256=h,arithmetic='exact Fraction; rational candidates; floating search not acceptance',aperture='11/10',original_compression_dimension=22,parity_spectral_compression_certificates=blocks,
 compression_exceptional_dimension_below_one_hundredth=10,compression_floor_on_remaining_twelve_modes='1/100',original_operator_eigenvalues_below_one_hundredth_count_lower=10,
 original_operator_eigenvalues_below_one_hundredth_count_upper=1250,full_operator_upper_count_basis='The inherited complete 1250-feature complement has floor alpha=247/2500>1/100; dimension intersection bounds the low spectral subspace.',
 actual_original_candidate_coupled_action_norm_enclosures_supplied=True,inherited_individual_norm_allowance_cannot_close_fixed_ten_candidate_Schur=True,original_coupling_is_too_large_proved=False,exceptional_compression_block_positive_certified=True,entire_original_native_twenty_two_compression_positive_certified=True,original_native_positive_span_dimension=22,full_requested_spectral_certificate_completed=False,original_response_alignment_analytic_proof_supplied=True,
 original_compression_metric_identity_analytic_proof_supplied=True,Loewner_inertia_and_compact_minmax_proofs_supplied=True,known_corrected_positive_span_dimension=6,original_operator_nonpositive_spectral_dimension_upper=1244,
 actual_original_exceptional_spectral_subspace_identified=False,positive_floor_outside_original_ten_mode_structure_certified=False,original_ten_mode_structure_complete=False,compression_low_modes_are_certified_nonpositive=False,complete_nonpositive_mode_coverage_certified=False,actual_lifted_response_Gram_certified=False,strong_head_block_lower_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False,new_source_integrals_evaluated=0)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc106_correlated_effective_head_sandwich.json','rpb108_rc104_eight_mode_strong_floor_ceiling.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc66_arch_multiplier_transport.json','rpb108_rc77_canonical_adjoint_tail.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc84_direct_nominal_response_residual.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: reversed signed contractions, determinant-ratio inertia replay and original compression census')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
