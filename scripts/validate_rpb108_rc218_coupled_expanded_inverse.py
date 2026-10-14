"""RC218: full prefix Gram interface and coupled ten-trial/eight-source inverse."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math
import validate_rpb108_rc217_expanded_mixed_inverse as prev
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc129_four_vector_joint_moment import inv,add,cong,mm
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS['certificates/rpb108_rc217_expanded_mixed_inverse.json']='5f0f64ccb9af714b86a90e76d3be9dccbca5b69f'
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc217_expanded_mixed_inverse.py']='00ec74eb1f550858ba59416581350e7f315f7632'
def outer(v):return [[a*b for b in v] for a in v]
def trans(A):return list(map(list,zip(*A)))
def zeros(n):return [[F(0)]*n for _ in range(n)]
def isum(terms):
    value=Z
    for t in terms:value=plus(value,t)
    return value
def interval_matrix(rows,symmetric=False):
    lo=[];hi=[]
    for row in rows:
        b=[bounds(x) for x in row];lo.append([x[0] for x in b]);hi.append([x[1] for x in b])
    if symmetric:
        for i in range(len(rows)):
            for j in range(i):lo[i][j]=lo[j][i];hi[i][j]=hi[j][i]
    return lo,hi
def imat(L,H):return [[(rat(L[i][j])[0],rat(H[i][j])[1]) for j in range(len(L[0]))] for i in range(len(L))]
def iprod(A,B):
    return [[isum([smul(A[i][k],B[k][j]) for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]
def iconst(A):return [[rat(x) for x in r] for r in A]
def isym(A):
    return [[smul(rat(F(1,2)),plus(A[i][j],A[j][i])) for j in range(len(A))] for i in range(len(A))]
def iadd(A,B,sign=1):return [[plus(A[i][j],B[i][j]) if sign==1 else minus(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def envelope(vectors,radii,G):
    Gi=inv(G);norm=[sqrtup(sum(v[i]*Gi[i][j]*v[j] for i in range(len(G)) for j in range(len(G)))) for v in vectors]
    weights=[1/n if n else F(1) for n in norm]
    factor=sum(r/weights[k] for k,r in enumerate(radii))
    E=zeros(len(G))
    for k,v in enumerate(vectors):E=add(E,scale(factor*radii[k]*weights[k],outer(v)))
    return E,weights
def error_matrix(Y,eps,w):
    factor=sum(eps[k]/w[k] for k in range(10))
    D=[[factor*eps[i]*w[i] if i==j else F(0) for j in range(10)] for i in range(10)]
    assert min(w)>0 and psd(add(D,outer(eps),-1))
    return cong(Y,D)
def certified_width(gap,G):
    # Floating eigenvalues only propose a narrow integer bracket. Exact PSD
    # decisions prove both ends and the final minimal 1e-6 grid bound.
    import numpy as np
    from scipy.linalg import eigh
    ar=lambda M:np.array([[float(x) for x in row] for row in M])
    yes=lambda k:psd(add(scale(F(k,10**6),G),gap,-1))
    try:guess=max(0.,float(eigh(ar(gap),ar(G),eigvals_only=True)[-1]))
    except Exception:return width(gap,G)
    hi=max(1,math.ceil(guess*10**6)+10);step=1000
    while not yes(hi):hi+=step;step*=2
    lo=max(0,hi-step)
    while lo and yes(lo):step*=2;lo=max(0,hi-step)
    if lo==0 and yes(0):return F(0)
    while hi-lo>1:
        mid=(hi+lo)//2
        if yes(mid):hi=mid
        else:lo=mid
    assert yes(hi) and not yes(hi-1)
    return F(hi,10**6)
def transport(ctx,Y,eps,G,GH,Gcmp,a,ps,inheritedL,inheritedH,reverse=False):
    candidates=[];seen=set();cache={}
    def cw(gap,gram):
        key=(tuple(map(tuple,gap)),tuple(map(tuple,gram)))
        if key not in cache:cache[key]=certified_width(gap,gram)
        return cache[key]
    for p in ps[::-1] if reverse else ps:
        w=list(map(F,p['weights']));E=error_matrix(Y,eps,w)
        l,u,tC,tW=[F(p[k]) for k in ['lower_theta','upper_theta','variational_tail_theta','cross_tail_theta']]
        assert 0<l<=F(1,2) and min(u,tC,tW)>0
        C=add(scale(tC,ctx['Utail']),scale(1/(4*tC),ctx['Rtail']))
        V=add(scale(tW,ctx['Utail']),scale(1/(4*tW),ctx['Rtail']))
        W=lambda c:add(add(add(ctx['UGhi'],scale(c*c,ctx['Nhi'])),scale(2*c,ctx['Xhi'])),scale(2*c,V))
        WL=W(F(1));WH=W(2/a);assert psd(WL) and psd(WH)
        L=add(add(add(ctx['baseLo'],scale(F(1,2),ctx['Nlo'])),C,-1),add(scale(l,WL),scale(1/(4*l)-F(1,2),E)),-1)
        H=add(add(add(ctx['baseHi'],scale(1/a,ctx['Nhi'])),C),add(scale(u,WH),scale(1/a+1/(4*u),E)))
        for ln,lo in [('coupled',L),('inherited_RC217',inheritedL),('refined_structural',scale(F(1,2),G))]:
            for hn,hi in [('coupled',H),('inherited_RC217',inheritedH),('refined_structural',scale(1/a,GH))]:
                key=(ln,hn,tuple(map(tuple,lo)),tuple(map(tuple,hi)),p['label'] if ln=='coupled' or hn=='coupled' else '')
                if key in seen:continue
                # Keep the label tie-breaking independent of replay order.
                if ln!='coupled' and hn!='coupled' and p['label']!=min(q['label'] for q in ps):continue
                seen.add(key);gap=add(hi,lo,-1)
                if not psd(lo) or not psd(gap):continue
                if candidates:
                    best=min(F(c['relative_inverse_width_upper']) for c in candidates)
                    if not psd(add(scale(best,G),gap,-1)):continue
                beta=cw(gap,G);common=cw(gap,Gcmp);gate=add(scale(F(1,2),G),gap,-1)
                assert psd(add(scale(beta,G),gap,-1))
                candidates.append(dict(proposal=p,lower_type=ln,upper_type=hn,inverse_response_lower=ser(lo),inverse_response_upper=ser(hi),relative_inverse_width_upper=str(beta),relative_width_on_RC217_Gram_floor=str(common),half_Gram_gate_passed=psd(gate),half_Gram_gate_matrix=ser(gate),action_error_Gram_upper=ser(E)))
    return min(candidates,key=lambda c:(F(c['relative_inverse_width_upper']),c['lower_type'],c['upper_type'],c['proposal']['label']))
def optimize(ctx,Y,eps,G,a,weights):
    import numpy as np
    from scipy.optimize import minimize
    ar=lambda M:np.array([[float(x) for x in row] for row in M])
    g=ar(G);s=np.diag(1/np.sqrt(np.diag(g)));L=np.linalg.cholesky(s@g@s);W=s@np.linalg.inv(L).T
    wh=lambda M:W.T@ar(M)@W
    UG,N,X,UT,RT,gap=map(wh,[ctx['UGhi'],ctx['Nhi'],ctx['Xhi'],ctx['Utail'],ctx['Rtail'],add(ctx['baseHi'],ctx['baseLo'],-1)])
    NL=wh(ctx['Nlo']);y=ar(Y)@W;es=np.array(list(map(float,eps)));ws=np.array(list(map(float,weights)))
    def objective(z):
        w=ws*np.exp(z[:10]);l,u,tC,tW=map(math.exp,z[10:])
        E=(es/w).sum()*((y.T*(es*w))@y)
        C=tC*UT+RT/(4*tC);V=tW*UT+RT/(4*tW)
        lowW=UG+N+2*X+2*V;co=2/float(a);highW=UG+co*co*N+2*co*X+2*co*V
        full=gap+N/float(a)-NL/2+2*C+l*lowW+u*highW+(1/float(a)+1/(4*u)+1/(4*l)-.5)*E
        return float(np.linalg.eigvalsh((full+full.T)/2)[-1])
    bounds=[(-4,4)]*10+[(-14,math.log(.5)),(-14,3),(-7,7),(-7,7)]
    z=np.array([0.]*10+[math.log(.004),math.log(.003),0.,0.]);proposals=[]
    def record(z,label):
        w=[max(F(1,10**24),down(F(float(ws[k]*math.exp(z[k]))),10**24)) for k in range(10)]
        pars=[max(F(1,10**12),down(F(math.exp(v)),10**12)) for v in z[10:]]
        pars[0]=min(F(1,2),pars[0])
        proposals.append(dict(label=label,weights=list(map(str,w)),lower_theta=str(pars[0]),upper_theta=str(pars[1]),variational_tail_theta=str(pars[2]),cross_tail_theta=str(pars[3])))
    record(z,'initial')
    for method in ['Powell','SLSQP']:
        result=minimize(objective,z,method=method,bounds=bounds,options={'maxiter':600,'ftol':1e-10})
        record(result.x,method);print('RC218 proposal',method,objective(result.x),flush=True);z=result.x
    return proposals
def run(reverse=False,proposals=None):
    data={}
    for p,sha in HELPER_PINS.items():assert prev.blob((ROOT/p).read_bytes())==sha,(p,'helper Git blob mismatch')
    for p,sha in PINS.items():
        b=(ROOT/p).read_bytes();assert prev.blob(b)==sha,(p,'input Git blob mismatch');data[p]=json.loads(b)
    get=lambda n:data['certificates/rpb108_rc'+n+'.json']
    base=get('217_expanded_mixed_inverse')
    path=ROOT/'scripts/validate_rpb108_rc217_expanded_mixed_inverse.py'
    src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker="    dm=list(map(F,get('134_correlated_six_input_covariance')"
    assert src.count(marker)==1;src=src.replace(marker,'    return locals()\n'+marker)
    ns={'__file__':str(path)};exec(compile(src,'RC218 immutable source and legacy carrier recovery','exec'),ns)
    state=ns['run'](reverse);d=state['d'];old=state['old'];delta=state['delta'];t=state['t']
    dc=get('214_correlated_difference_canonical_action');tc=get('216_refined_t10_canonical_action');capture=get('135_common_response_capture')
    dm=list(map(F,get('134_correlated_six_input_covariance')['z_minus_v_combined_tail_polynomial']));tm=list(map(F,capture['collective_capture_budgets'][1]['analytic_moment_centers']))
    dlambda=F(4094*4095);tlambda=F(capture['tail_Lambda'])
    carrier=dict(milestone='RC218-native-carriers',delta_finite_rows=[dict(degree=n,center=str(delta[n])) for n in sorted(delta)],t10_finite_center_radius_rows=state['payload'],
        delta_historical_sha256=state['deltaHash'],t10_historical_sha256=state['digest'],delta_analytic_lambda=str(dlambda),delta_analytic_moments=list(map(str,dm)),t10_analytic_lambda=str(tlambda),t10_analytic_moments=list(map(str,tm)),source_definitions_unchanged=True)
    cp=[{r['degree']:F(r['coefficient_center']) for r in c['endpoint_action_polynomial']} for c in [dc,tc]]
    rp=[{r['degree']:F(r['coefficient_center']) for r in c['regular_action']['D_inverse_regular_polynomial']} for c in [dc,tc]]
    ep=[list(map(F,c['endpoint_signed_moment_coefficients'])) for c in [dc,tc]];el=[F(c['endpoint_analytic_lambda']) for c in [dc,tc]]
    gg=[[Z]*10 for _ in range(10)];bb=[[Z]*10 for _ in range(10)];aa=[[Z]*10 for _ in range(10)]
    degrees=old['degrees'][::-1] if reverse else old['degrees']
    for n in degrees:
        u,v,mass=d['expandedCache'][n];D=old['D'][n];eta=div(rat(F(2*n+1,n*(n+1))),D) if n else Z
        du=rat(delta[n]) if n<=8190 else smul(eta,rat(sum(dm[k]*F(dlambda,n*(n+1))**k for k in range(len(dm)))))
        tu=rat(t[n]) if n<=16382 else smul(eta,rat(sum(tm[k]*F(tlambda,n*(n+1))**k for k in range(len(tm)))))
        us=[du,tu];vs=[]
        for k in range(2):
            av=plus(us[k],rat(cp[k].get(n,F(0))+rp[k].get(n,F(0))))
            av=minus(av,smul(div(rat(old['r']),D),us[k]))
            if n>=4096:av=plus(av,smul(rat(F(1,2)),us[k]))
            if n>=8192:av=plus(av,smul(eta,rat(sum(ep[k][j]*F(el[k],n*(n+1))**j for j in range(25)))))
            vs.append(av)
        u=u+us;v=v+vs
        for i in range(10):
            for j in range(i,10):
                gg[i][j]=plus(gg[i][j],smul(mass,smul(u[i],u[j])))
                aa[i][j]=plus(aa[i][j],smul(mass,smul(v[i],v[j])))
            for j in range(10):bb[i][j]=plus(bb[i][j],smul(mass,smul(u[i],v[j])))
        if n%8192==0:print('RC218 full joint prefix',n,flush=True)
    gl,gh=interval_matrix(gg,True);bl,bh=interval_matrix(bb);al,ah=interval_matrix(aa,True)
    norms=[sqrtup(F(base['raw_source_D_Gram_entry_upper'][i][i])) for i in range(10)]
    GTlo,prefixHi,_=loewner(gl,gh,norms)
    O=d['O'];z=F((O+2)*(O+3));T=d['T'];r=old['r'];Dlow=F(old['D'][O][0])
    wmu=old['mu'];vmu=d['mu'];vmom=d['mom'];q185=old['qmom'];q202=list(map(F,get('202_six_source_residual_action')['endpoint_exact_signed_moments']))
    sd=[F(0)]*10;sd[4]=old['df'];sd[6]=sum(abs(vmu[k])*F(d['lam'],z)**k for k in range(1,11));sd[8]=sum(abs(dm[k])*F(dlambda,z)**k for k in range(1,len(dm)));sd[9]=sum(abs(tm[k])*F(tlambda,z)**k for k in range(1,len(tm)))
    sl=[F(0),F(0),F(0),F(1),wmu[0],F(0),vmu[0],F(0),dm[0],tm[0]]
    vl=[F(1),F(1),wmu[0],F(3,2)+old['nu'][0]-r/(2*Dlow),old['cw0']*wmu[0]+old['omega'][0],q185[0],(F(3,2)-r/(2*Dlow))*vmu[0]+vmom[0],q202[0]]
    vd=[F(0),old['d2'],old['df'],old['dp'],old['dw'],sum(abs(q185[k])*F(old['qlam'],z)**k for k in range(1,25)),F(3,2)*sd[6]+r*abs(vmu[0])/(2*Dlow)+sum(abs(vmom[k])*F(d['epLam'],z)**k for k in range(1,25)),sum(abs(q202[k])*F(F(get('202_six_source_residual_action')['endpoint_analytic_lambda']),z)**k for k in range(1,25))]
    for k,mu in enumerate([dm,tm]):
        vl.append((F(3,2)-r/(2*Dlow))*mu[0]+ep[k][0])
        vd.append(F(3,2)*sd[8+k]+r*abs(mu[0])/(2*Dlow)+sum(abs(ep[k][j])*F(el[k],z)**j for j in range(1,25)))
    sourceTail=add(scale(2*T,outer(sl)),[[8*T*sd[i]**2 if i==j else F(0) for j in range(10)] for i in range(10)])
    GThi=add(prefixHi,sourceTail);keep=[0,1,2,3,4,6,8,9];Fmap=[[F(i==keep[j]) for j in range(8)] for i in range(10)]
    G=cong(Fmap,GTlo);GH=cong(Fmap,GThi);assert psd(G);inv(G)
    Gcmp=mat(base,'conditioned_source_D_Gram_lower')
    mid=lambda L,H:scale(F(1,2),add(L,H))
    AM=mid(al,ah);BM=mid(bl,bh);pickB=mm(trans(BM),Fmap)
    full=mm(inv(AM),pickB)
    subAM=[[AM[i][j] for j in keep] for i in keep];subB=[[pickB[i][j] for j in range(8)] for i in keep]
    sub=mm(inv(subAM),subB);sourceOnly=zeros(10)
    sourceOnly=[[F(0)]*8 for _ in range(10)]
    for i,k in enumerate(keep):sourceOnly[k]=sub[i]
    trials={'least_residual_10':full,'source_only_8':sourceOnly}
    trials={name:[[down(x,10**30) for x in row] for row in Y] for name,Y in trials.items()}
    eps=list(map(F,base['complete_column_action_D_error_norm_upper']));a=F(base['spectral_metric_lower']);results=[];proposalMap={}
    iGG=imat(gl,gh);iBB=imat(bl,bh);iAA=imat(al,ah);iF=iconst(Fmap);iFt=iconst(trans(Fmap))
    inherited=base['selected_inverse_enclosure'];inheritedL=mat(inherited,'inverse_response_lower');inheritedH=mat(inherited,'inverse_response_upper')
    for name in sorted(trials,reverse=reverse):
        Y=trials[name];iy=iconst(Y);iyt=iconst(trans(Y));j=[[Fmap[i][j]-Y[i][j] for j in range(8)] for i in range(10)]
        cross=iprod(iprod(iFt,iBB),iy)
        N=iadd(iadd(iprod(iprod(iFt,iGG),iF),iadd(cross,trans(cross)),-1),iprod(iprod(iyt,iAA),iy))
        UR=iadd(iprod(iprod(iyt,iGG),iF),iprod(iprod(iyt,iBB),iy),-1)
        nl,nh=interval_matrix(N);xl,xh=interval_matrix(isym(UR))
        sw=[sqrtup(GH[i][i]) for i in range(8)]
        Nlo,NprefixHi,_=loewner(nl,nh,sw);Xlo,Xhi,_=loewner(xl,xh,sw)
        if not psd(Nlo):Nlo=zeros(8)
        lead=[sl[keep[j]]-sum(vl[k]*Y[k][j] for k in range(10)) for j in range(8)]
        vec=[];rad=[]
        for i in range(8):
            if sd[keep[i]]:vec.append([F(j==i) for j in range(8)]);rad.append(sd[keep[i]])
        for k in range(10):
            if vd[k]:vec.append(Y[k]);rad.append(vd[k])
        Qrem,_=envelope(vec,rad,G)
        Rtail=add(scale(F(3,2)*T,outer(lead)),scale(3*T,Qrem))
        Utail=cong(Y,sourceTail);Nhi=add(NprefixHi,Rtail);assert psd(Nhi)
        UGlo=cong(Y,GTlo);UGhi=cong(Y,GThi)
        SUlo=scale(F(1,2),add(add(G,UGlo),cong(j,GThi),-1));SUhi=scale(F(1,2),add(add(GH,UGhi),cong(j,GTlo),-1))
        ctx=dict(UGhi=UGhi,Nlo=Nlo,Nhi=Nhi,Xlo=Xlo,Xhi=Xhi,Utail=Utail,Rtail=Rtail,baseLo=add(SUlo,Xlo),baseHi=add(SUhi,Xhi))
        _,weights=envelope(Y,eps,G)
        ps=proposals[name] if proposals is not None else optimize(ctx,Y,eps,G,a,weights);proposalMap[name]=ps
        chosen=transport(ctx,Y,eps,G,GH,Gcmp,a,ps,inheritedL,inheritedH,reverse)
        results.append(dict(trial=name,trial_coefficients=ser(Y),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),nominal_residual_tail_Gram_upper=ser(Rtail),trial_source_tail_Gram_upper=ser(Utail),trial_source_Gram_upper=ser(UGhi),finite_trial_residual_cross_lower=ser(Xlo),finite_trial_residual_cross_upper=ser(Xhi),base_variational_lower=ser(ctx['baseLo']),base_variational_upper=ser(ctx['baseHi']),selected_enclosure=chosen))
        print('RC218 trial / inverse width / gate',name,chosen['relative_inverse_width_upper'],chosen['half_Gram_gate_passed'],flush=True)
    results.sort(key=lambda c:c['trial']);best=min(results,key=lambda c:(F(c['selected_enclosure']['relative_inverse_width_upper']),c['trial']));chosen=best['selected_enclosure']
    interface=dict(milestone='RC218-prefix-interface',raw_trial_order=base['raw_trial_order'],finite_prefix_degree=O,
        source_Gram_entry_lower=ser(gl),source_Gram_entry_upper=ser(gh),nominal_source_action_entry_lower=ser(bl),nominal_source_action_entry_upper=ser(bh),nominal_action_Gram_entry_lower=ser(al),nominal_action_Gram_entry_upper=ser(ah),
        source_tail_signed_leading_coefficients=list(map(str,sl)),source_tail_nonleading_absolute_bounds=list(map(str,sd)),action_tail_signed_leading_coefficients=list(map(str,vl)),action_tail_nonleading_absolute_bounds=list(map(str,vd)),common_eta_tail_D_energy_upper=str(T),source_tail_Gram_upper=ser(sourceTail),full_source_Gram_lower=ser(GTlo),full_source_Gram_upper=ser(GThi),complete_column_error_norm_upper=list(map(str,eps)),source_action_definitions_unchanged=True)
    result=dict(milestone='RC218',starting_commit='fa20e123c4d0711e7dbb18c8bfdbca8b4c25d97e',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,conditioned_response_source_order=base['conditioned_response_source_order'],raw_trial_order=base['raw_trial_order'],conditioned_to_original_source_matrix=base['conditioned_to_original_source_matrix'],
        source_D_Gram_lower=ser(G),source_D_Gram_upper=ser(GH),RC217_comparison_Gram_floor=ser(Gcmp),finite_prefix_degree=O,rational_parameter_proposals=proposalMap,evaluated_trials=results,selected_trial=best['trial'],selected_enclosure=chosen,relative_inverse_width_upper=chosen['relative_inverse_width_upper'],relative_width_on_RC217_Gram_floor=chosen['relative_width_on_RC217_Gram_floor'],canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],
        previous_eight_source_width_upper=base['relative_inverse_width_upper'],full_nominal_prefix_and_analytic_residual_Gram_assembled=True,same_action_error_combined_before_Young=True,complete_action_and_source_tails_paid=True,new_sources_operator_and_domain_unchanged=True,source_Gram_normalization_refined_not_silently_identified_with_RC217=True,complex_mixtures_paid=True,numerical_optimization_used_only_for_rational_proposals=True,accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC219: inspect and refine the dominant coupled residual/error payment using the materialized prefix interface; preserve both passed earlier gates')
    return result,carrier,interface
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--carriers',type=Path,required=True);p.add_argument('--interface',type=Path,required=True);p.add_argument('--replay',action='store_true');a=p.parse_args()
    expected=json.loads(a.output.read_text()) if a.replay else None
    result,carrier,interface=run(a.replay,expected['rational_parameter_proposals'] if expected else None)
    if a.replay:
        assert result==expected and carrier==json.loads(a.carriers.read_text()) and interface==json.loads(a.interface.read_text())
    else:
        for path,value in [(a.output,result),(a.carriers,carrier),(a.interface,interface)]:path.write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')
    print('RC218 PASS: coupled inverse width',result['relative_inverse_width_upper'],'gate',result['canonical_half_Gram_inverse_width_gate_passed'])
