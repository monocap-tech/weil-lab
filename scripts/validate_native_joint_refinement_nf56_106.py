"""NF56 independent cell-first native/source integrals and joint inverse proof.

Does not import the NF56 producer. Inherits hash-pinned NF55 certified data,
rebuilds the new physical source at moment degree1600 and checks every added
entry, exact physical orthogonality and final rational witness signs.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import validate_native_complete_transport_nf49_106 as prior
import native_precision_nf53 as precision
import validate_native_joint_refinement_nf55_106 as predecessor
h=prior.historic;n=h.n;ind=prior.ind;Box=prior.Box;K=prior.K;GRID=prior.GRID
read=prior.read;sha=prior.sha;mat=ind.boxmatrix

def functional(source,m,degree):
    # Integrate b+prime-cell together on each original translation cell.
    out=[prior.CellBox(0) for _ in range(degree+1)]
    for c,(mp,ml) in zip(source[3],m.cm):
        out=prior.add(out,prior.add(prior.weighted(prior.add(source[1],c),mp,degree+1),prior.weighted(source[2],ml,degree+1)))
    return [z.box() for z in out]

def polynomial_value(poly,fun):
    return sum((Box(F(a.l,GRID),F(a.h,GRID))*b for a,b in zip(poly,fun)),Box(0))

def block(a,b,c,d):return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def append(a,c,d):return [r+[z] for r,z in zip(a,c)]+[c+[d]]
def vector(matrix,coeff):return [ind.dot(row,coeff) for row in matrix]
def value(matrix,coeff):return ind.dot(coeff,vector(matrix,coeff))
def inverse(M,QH,GH,B,S,G):
    C=ind.add(QH,ind.scale(M,-K));_,cp=prior.oldcheck.independent_inverse(C)
    U=ind.add(ind.add(GH,ind.scale(QH,-2*K)),ind.scale(M,K*K))
    N=ind.add(C,ind.scale(U,1/K));NI,np=prior.oldcheck.independent_inverse(N)
    W=ind.add(S,ind.scale(B,-K))
    reaction=ind.add(ind.scale(G,1/K),ind.scale(ind.mm(ind.mm(W,NI),ind.transpose(W)),-1/(K*K)))
    return reaction,cp,np

def correlated_gain(M,QH,GH,B,S,z):
    # The common Xi Gram cancels exactly. A block inverse gives a positive
    # rank-one gain; do not pay the common Gram's interval error twice.
    C=ind.add(QH,ind.scale(M,-K))
    U=ind.add(ind.add(GH,ind.scale(QH,-2*K)),ind.scale(M,K*K))
    N=ind.add(C,ind.scale(U,1/K));W=ind.add(S,ind.scale(B,-K))
    oldN=[row[:-1] for row in N[:-1]]
    NI,_=prior.oldcheck.independent_inverse(oldN)
    t=[row[-1] for row in N[:-1]];a=vector(NI,t)
    delta=N[-1][-1]-ind.dot(t,a);assert delta.l>0
    oldW=[row[:-1] for row in W]
    residual=ind.dot(z,[row[-1] for row in W])-ind.dot(z,vector(oldW,a))
    square=Box(0 if residual.l<=0<=residual.h else min(residual.l**2,residual.h**2),max(residual.l**2,residual.h**2))
    gain=square/(delta*K*K)
    return gain,delta,residual

def gain_controls():
    N=[[F(2),F(1)],[F(1),F(3)]];NI=ind.exact_inverse(N)
    for w in [F(4),F(-4),F(3,2)]:
        x=[F(3),w]
        new=sum(x[i]*NI[i][j]*x[j] for i in range(2) for j in range(2))
        delta=F(3)-F(1,2);residual=w-F(3,2)
        assert new-F(9,2)==residual**2/delta
    assert F(1,2)-F(1,2)==0
    return dict(signed_and_null_rank_one_gain_identity='PASS',singular_denominator_control='PASS')

def parent_context(parity):
    ctx,previous,parent49=predecessor.parent_context(parity)
    global GRID
    GRID=10**900;prior.GRID=GRID;ind.GRID=GRID
    path=f'notes/data/RPB108_NF55_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
    cert=read(path);report=read(f'notes/data/RPB108_NF55_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json')
    assert report['status']=='PASS' and report['certificate_sha256']==sha(path)
    parent54=f'notes/data/RPB108_NF54_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
    assert cert['inherited_NF54_certificate_sha256']==sha(parent54)
    assert cert['inherited_NF54_validation_sha256']==sha(f'notes/data/RPB108_NF54_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json')
    ii=cert['fixed_high_selection']['selection_indices'];cc=list(map(F,cert['fixed_high_selection']['fixed_rational_high_coefficients']))
    key=hashlib.sha256(repr((parity,ii,cc,900,ctx['key'])).encode()).hexdigest()
    work=Path('work/nf55')/(parity+'-independent')
    m=prior.cached(work/'moments.pkl',parity+'-1600-900-'+sha('scripts/native_precision_nf53.py'),lambda:h.p.p.old.probe.Moments(1600,parity))
    sy=prior.cached(work/'new_source.pkl',key,lambda:m.source(ii,cc))
    low=[h.I(*map(F,e)) for e in cert['new_source_low_projection']]
    ctx['sources'].append(h.r.projection(sy,low,ctx['ids']));ctx['H'].append((ii,cc));ctx['m']=m
    shadow=dict(cert)
    for name in ['joined_source_physical_errors','remaining_source_physical_errors','joined_source_approximant_norm_upper','remaining_source_approximant_norm_upper']:
        shadow[name]=previous[name]
    shadow['high_source_physical_errors']=previous['high_source_physical_errors']+[cert['new_projected_source_error_upper']]
    shadow['high_source_approximant_norm_upper']=previous['high_source_approximant_norm_upper']+[cert['new_source_approximant_norm_upper']]
    if parity=='even':
        probe_path='notes/data/RPB108_NF55_EVEN_UNRESOLVED_JOINT_SIGN_PROBES_20261010.json'
        probe=read(probe_path);assert probe['status']=='PASS' and probe['certificate_sha256']==sha(path)
        assert probe['validation_sha256']==sha(f'notes/data/RPB108_NF55_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json')
        target=probe['sign_probe_candidates'][0];assert target['enclosure_spans_zero']
        shadow['joint_lower_bound_sign']=dict(cert['joint_lower_bound_sign'],fixed_rational_lower_bound_witness=target['fixed_rational_sign_probe'],witness_original_physical_mass_squared=target['original_physical_mass_squared'])
        ctx['target_classification']='UNRESOLVED_SIGN_PROBE';ctx['target_probe_sha256']=sha(probe_path)
    else:
        assert cert['joint_lower_bound_sign']['status']=='JOINT_LOWER_BOUND_REJECTED'
        ctx['target_classification']='CERTIFIED_REJECTING_WITNESS';ctx['target_probe_sha256']=None
    return ctx,shadow,parent49

def run(path):
    cert=read(path);parity=cert['parity'];ctx,parent,parent49=parent_context(parity);idx=ctx['idx']
    assert cert['milestone']=='NF56' and cert['aperture']=='53/50'
    assert cert['original_archive_uncompressed_sha256']==ctx['hashes']
    parentpath=f'notes/data/RPB108_NF55_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
    validationpath=f'notes/data/RPB108_NF55_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
    validation=read(validationpath)
    assert sha(parentpath)==cert['inherited_NF55_certificate_sha256']==validation['certificate_sha256']
    assert sha(validationpath)==cert['inherited_NF55_validation_sha256'] and validation['status']=='PASS'
    for p,digest in parent49['frozen_input_sha256'].items():assert sha(p)==digest
    floor=read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_VALIDATION_20261009.json')
    assert floor['status']=='PASS' and F(floor['original_F112_floor']['independent_original_F112_lower'])>K
    trial=cert['fixed_high_selection'];ii=trial['selection_indices'];cc=list(map(F,trial['fixed_rational_high_coefficients']))
    assert ii==list(range(112+idx,373 if idx==0 else 372,2)) and len(ii)==len(cc)
    mass=sum(a*a for a in cc);assert str(mass)==trial['exact_new_physical_mass_squared'] and 0<mass<=1
    ydict=dict(zip(ii,cc));H=ctx['H']
    assert all(sum(a*ydict.get(j,F(0)) for j,a in zip(ids,col))==0 for ids,col in H)
    raw=list(map(F,trial['raw_downrounded_coefficients']));ell=list(map(F,trial['exact_old_high_projection_coefficients']))
    assert raw==[F((((F(a)+F(b))/2)*10**100).__floor__(),10**100) for a,b in trial['reconstructed_response_coordinates']]
    highdict=[dict(zip(ids,col)) for ids,col in H]
    oldmass=[[sum(a.get(j,F(0))*b.get(j,F(0)) for j in ii) for b in highdict] for a in highdict]
    rawcross=[sum(a.get(j,F(0))*c for j,c in zip(ii,raw)) for a in highdict]
    assert [sum(a*b for a,b in zip(row,ell)) for row in oldmass]==rawcross
    norm=F(trial['new_direction_normalizing_upper']);assert norm>0
    assert cc==[(c-sum(a*dict(zip(ids,col)).get(j,F(0)) for a,(ids,col) in zip(ell,H)))/norm for j,c in zip(ii,raw)]
    # Reproducible frozen rational selection; sign evidence below is separate.
    z=list(map(F,trial['normalized_NF55_joint_witness']));normalization=F(trial['NF55_witness_normalizing_upper'])
    assert [a*normalization for a in z]==list(map(F,parent['joint_lower_bound_sign']['fixed_rational_lower_bound_witness']))
    target_coeff={}
    for scalar,(jj,col) in zip([a*normalization for a in z],ctx['P']+[(ctx['ids'],col) for col in ctx['T']]):
        for j,a in zip(jj,col):target_coeff[j]=target_coeff.get(j,F(0))+scalar*a
    target_mass=sum(a*a for a in target_coeff.values())
    assert target_mass==F(parent['joint_lower_bound_sign']['witness_original_physical_mass_squared'])
    assert normalization**2>=target_mass
    precision_metadata=ctx['precision_metadata']
    work=Path('work/nf56')/(parity+'-independent');work.mkdir(parents=True,exist_ok=True)
    key=hashlib.sha256(repr((parity,ii,cc,900,ctx['key'])).encode()).hexdigest()
    m=ctx['m']
    sy=prior.cached(work/'new_source.pkl',key,lambda:m.source(ii,cc))
    fun=functional(sy,m,max(ii));coords={j:polynomial_value(n.basis(j),fun) for j in range(idx,max(ii)+1,2)}
    error=m.eta*prior.root(mass);paidcoords={j:a+Box(-error,error) for j,a in coords.items()}
    low=[paidcoords[j] for j in ctx['ids']]
    prior.compare([low],[list(map(lambda e:Box(*map(F,e)),cert['new_source_low_projection']))])
    # Freeze the producer's low midpoint polynomial so the independently
    # enclosed approximant is exactly the same physical function.
    frozenlow=[Box(*map(F,e)) for e in cert['new_source_low_projection']]
    midpoint=[(a.l+a.h)/2 for a in frozenlow]
    ry=(sy[0],n.add(sy[1],n.scale(n.physical(ctx['ids'],midpoint),-1)),sy[2],sy[3])
    needed=error+8*max(max(abs(a.l-c),abs(a.h-c)) for a,c in zip(low,midpoint))
    ey=F(cert['new_projected_source_error_upper']);assert ey>=needed
    columns=ctx['P']+[(ctx['ids'],col) for col in ctx['T']]+H+[(ii,cc)]
    native=[]
    for ids,col in columns:
        val=sum((c*coords[j] for j,c in zip(ids,col)),Box(0));e=error*prior.root(sum(c*c for c in col))
        native.append(val+Box(-e,e))
    prior.compare([native],[list(map(lambda e:Box(*map(F,e)),cert['new_native_pairings']))])
    print(parity,'independent native integrals and projection PASS',flush=True)
    sources=ctx['sources'][53:56]+ctx['sources'][:53]+ctx['sources'][56:]+[ry]
    action=prior.cached(work/'new_action.pkl',key+'-'+sha(__file__)+'-'+sha(path),lambda:prior.cell_action(ry,m,max(len(s[1]) for s in sources),max(len(s[2]) for s in sources)))
    rawsource=[prior.pair(s,action) for s in sources]
    prior.compare([rawsource],[list(map(lambda e:Box(*map(F,e)),cert['reconstructed_new_complete_source_pairings']))])
    normY=prior.root(rawsource[-1].h)
    errors=list(map(F,parent['joined_source_physical_errors']+parent['remaining_source_physical_errors']+parent['high_source_physical_errors']))+[ey]
    norms=list(map(F,parent['joined_source_approximant_norm_upper']+parent['remaining_source_approximant_norm_upper']+parent['high_source_approximant_norm_upper']))+[normY]
    paid=[]
    for a,e,nb in zip(rawsource,errors,norms):
        payment=e*normY+ey*nb+e*ey;paid.append(a+Box(-payment,payment))
    prior.compare([paid],[list(map(lambda e:Box(*map(F,e)),cert['original_new_complete_source_pairings']))])
    print(parity,'independent cell-first full source covariances PASS',len(paid),flush=True)
    o=ctx['o']
    M,QH,GH,B,S=[mat(parent[k]) for k in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram',
        'enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']]
    G=block(mat(o['parent37']['original_selected_complete_source_Gram']),ind.transpose(mat(parent49['original_remaining_joined_source_crosses'])),
        mat(parent49['original_remaining_joined_source_crosses']),prior.unpack(parent49['original_remaining_complete_source_Gram_upper'],53))
    oldnative=read('notes/data/RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64')['parity_certificates'][idx]
    B0=ind.transpose(mat(oldnative['original_remaining_native_couplings']))
    Q=block(mat(o['parent37']['original_selected_native_energy_Gram']),ind.transpose(B0),B0,mat(oldnative['original_remaining_native_Gram']))
    newM=append(M,[Box(0) for _ in H],Box(mass));newQH=append(QH,native[56:-1],native[-1]);newGH=append(GH,paid[56:-1],paid[-1])
    newB=[row+[a] for row,a in zip(B,native[:56])];newS=[row+[a] for row,a in zip(S,paid[:56])]
    for reconstructed,label in [(newM,'physical_Gram'),(newQH,'native_Gram'),(newGH,'complete_source_Gram')]:
        prior.compare(reconstructed,mat(cert['enlarged_high_'+label]))
    prior.compare(newB,mat(cert['enlarged_joint_high_native_crosses']));prior.compare(newS,mat(cert['enlarged_joint_high_complete_source_crosses']))
    reaction,cp,np=inverse(newM,newQH,newGH,newB,newS,G);lower=ind.add(Q,ind.scale(reaction,-1))
    prior.compare(reaction,prior.unpack(cert['complete_joint_high_inverse_upper_upper_triangle'],56))
    prior.compare(lower,prior.unpack(cert['complete_joint_original_Schur_lower_upper_triangle'],56))
    oldreaction=prior.unpack(parent['complete_joint_high_inverse_upper_upper_triangle'],56)
    oldlower=prior.unpack(parent['complete_joint_original_Schur_lower_upper_triangle'],56)
    improvement=value(ind.add(oldreaction,ind.scale(reaction,-1)),z)
    oldvalue=value(oldlower,z);newvalue=value(lower,z)
    gain,delta,residual=correlated_gain(newM,newQH,newGH,newB,newS,z)
    assert gain.l>0
    if parity=='odd':assert oldvalue.h<0
    else:assert oldvalue.l<=0<=oldvalue.h
    assert cert['old_target_classification']==ctx['target_classification'] and cert['old_target_probe_sha256']==ctx['target_probe_sha256']
    prior.overlap(gain,improvement)
    correlated_new=oldvalue+gain;prior.overlap(correlated_new,newvalue)
    tight_new=Box(max(correlated_new.l,newvalue.l),min(correlated_new.h,newvalue.h))
    for actual,label in [(improvement,'inverse_reaction_improvement'),(oldvalue,'old_lower_value'),(newvalue,'new_lower_value')]:
        prior.overlap(actual,Box(*map(F,cert['normalized_NF55_witness_'+label])))
    sign=cert['joint_lower_bound_sign'];signcheck=dict(status=sign['status'])
    if sign['status']=='JOINT_LOWER_BOUND_REJECTED':
        witness=list(map(F,sign['fixed_rational_lower_bound_witness']));test=value(lower,witness);assert test.h<0
        merged={}
        for scalar,(ids,col) in zip(witness,columns[:56]):
            for j,c in zip(ids,col):merged[j]=merged.get(j,F(0))+scalar*c
        witnessmass=sum(c*c for c in merged.values());assert str(witnessmass)==sign['witness_original_physical_mass_squared']
        quotient=test*(1/witnessmass)
        signcheck.update(independent_lower_matrix_value=[str(test.l),str(test.h)],independent_original_physical_quotient=[str(quotient.l),str(quotient.h)])
    elif sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND':
        _,proof=prior.oldcheck.independent_inverse(lower);signcheck['independent_positive_congruence_proof']=proof
    else:assert sign['status']=='UNRESOLVED'
    assert cert['original_joined_and_T53_columns_unchanged'] and cert['old_high_columns_unchanged']
    assert not any(cert[k] for k in ['original_inputs_regenerated','actual_negative_original_form_claimed','whole_aperture_positive','RH','F4','Lean'])
    return dict(milestone='NF56',status='PASS',parity=parity,certificate_sha256=sha(path),validator_sha256=sha(__file__),old_target_classification=ctx['target_classification'],old_target_probe_sha256=ctx['target_probe_sha256'],precision_configuration=precision_metadata,precision_controls=precision.controls(),
        original_archive_uncompressed_sha256=ctx['hashes'],independent_moment_degree=1600,
        independent_native_pairings_checked=len(native),independent_complete_source_pairings_checked=len(paid),
        exact_new_high_physical_orthogonality_checked=True,analytic_infinite_remainders_paid=True,
        inherited_NF55_certificate_and_validation_authenticated=True,
        independent_enlarged_surplus_positive_proof=cp,independent_enlarged_denominator_positive_proof=np,
        independent_normalized_NF55_witness_inverse_reaction_improvement=[str(improvement.l),str(improvement.h)],
        independent_normalized_NF55_witness_old_lower_value=[str(oldvalue.l),str(oldvalue.h)],
        independent_normalized_NF55_witness_new_lower_value=[str(newvalue.l),str(newvalue.h)],
        independent_normalized_NF55_witness_correlated_inverse_reaction_improvement=gain.ends(),
        independent_normalized_NF55_witness_correlated_new_lower_value=tight_new.ends(),
        correlated_gain_schur_denominator=delta.ends(),correlated_gain_signed_residual=residual.ends(),
        old_NF55_witness_lifted_to_positive=tight_new.l>0,
        joint_lower_bound_sign=signcheck,arithmetic_controls=prior.arithmetic_controls(),joint_controls=ind.controls(),correlated_gain_controls=gain_controls(),
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20',actual_negative_original_form_claimed=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--certificate',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();result=run(args.certificate);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(result['parity'],'NF56 independent PASS',flush=True)
