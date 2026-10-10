"""NF62: append a high direction selected from the complete NF61 joint target.

Selection uses midpoint coordinates only. All conclusions use paid original
native pairings, complete physical source covariances and rational intervals.
"""
import argparse,base64,gzip,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import certify_native_complete_transport_nf49_106 as old
import native_precision_nf53 as precision
import native_precision_nf62 as enlarged_precision
import certify_native_joint_refinement_nf61_106 as predecessor
import validate_native_complete_transport_nf49_106 as context49
v=old.v;n=old.n;I=old.I;K=old.K;fast=old.fast;dot=old.dot;mv=old.mv

def functional(s,m,degree):
    out=n.add(fast.hankel(s[1],m.M,degree+1),fast.hankel(s[2],m.ML,degree+1))
    for cell,(mp,_) in zip(s[3],m.cm):out=n.add(out,fast.hankel(cell,mp,degree+1))
    return out

def combine(sources,weights):
    result=([],[I(0)],[I(0)],[[I(0)] for _ in range(13)])
    for s,w in zip(sources,weights):
        result=([],n.add(result[1],n.scale(s[1],w)),n.add(result[2],n.scale(s[2],w)),
                [n.add(a,n.scale(b,w)) for a,b in zip(result[3],s[3])])
    return result

def matrix(rows):return v.p.prev.matrix(rows)
def unpack(rows,size):
    out=[[None]*size for _ in range(size)];it=iter(rows)
    for i in range(size):
        for j in range(i,size):out[i][j]=out[j][i]=I(*map(F,next(it)))
    return out

def inherited(ctx,cert):
    idx=ctx['idx'];o=ctx['o'];packet=ctx['packet'];count=ctx['count']
    M,QH,GH,BH,SH=[matrix(packet[k]) for k in [count+'_high_physical_Gram',count+'_high_native_Gram',
        count+'_high_complete_source_Gram','joined_'+count+'_high_native_crosses','joined_'+count+'_high_source_crosses']]
    TT=unpack(cert['original_remaining_complete_source_Gram_upper'],53)
    TP=matrix(cert['original_remaining_joined_source_crosses']);TH=matrix(cert['original_remaining_high_source_crosses'])
    nativeTH=matrix(cert['original_remaining_high_native_crosses'])
    GP=matrix(o['parent37']['original_selected_complete_source_Gram'])
    oldnative=old.native.decode('notes/data/RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64')['parity_certificates'][idx]
    B0=v.c.tr(matrix(oldnative['original_remaining_native_couplings']))
    fullQ=v.block(matrix(o['parent37']['original_selected_native_energy_Gram']),v.c.tr(B0),B0,matrix(oldnative['original_remaining_native_Gram']))
    fullG=v.block(GP,v.c.tr(TP),TP,TT)
    return M,QH,GH,BH+nativeTH,SH+TH,fullQ,fullG

def parent_context(parity):
    ctx,previous,_,base=predecessor.parent_context(parity)
    path=Path(f'notes/data/RPB108_NF61_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')
    cert=context49.read(path)
    reportpath=f'notes/data/RPB108_NF61_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
    report=context49.read(reportpath)
    assert report['status']=='PASS' and report['certificate_sha256']==old.sha(path)
    assert report['validator_sha256']==old.sha('scripts/validate_native_joint_refinement_nf61_106.py')
    assert report['frozen_target_minorant_certified_negative']
    assert cert['fixed_high_selection']['normalized_frozen_joint_target']==context49.read(ctx['NF60_scalar_path'])['frozen_target']
    m=ctx['m'];ii=cert['fixed_high_selection']['selection_indices'];cc=list(map(F,cert['fixed_high_selection']['fixed_rational_high_coefficients']))
    key=hashlib.sha256(repr((parity,ii,cc,old.sha('scripts/certify_native_joint_refinement_nf61_106.py'))).encode()).hexdigest()
    sy=old.cached(Path('work/nf61')/parity/'new_source.pkl',key,lambda:m.source(ii,cc))
    ctx['sources'].append(v.r.projection(sy,matrix([cert['new_source_low_projection']])[0],ctx['ids']));ctx['H'].append((ii,cc))
    shadow=dict(cert)
    for name in ['joined_source_physical_errors','remaining_source_physical_errors','joined_source_approximant_norm_upper','remaining_source_approximant_norm_upper']:
        shadow[name]=previous[name]
    shadow['high_source_physical_errors']=previous['high_source_physical_errors']+[cert['new_projected_source_error_upper']]
    shadow['high_source_approximant_norm_upper']=previous['high_source_approximant_norm_upper']+[cert['new_source_approximant_norm_upper']]
    shadow['joint_lower_bound_sign']=previous['joint_lower_bound_sign']
    ctx['target_classification']='NF61_CERTIFIED_MINORANT_COUNTERDIRECTION';ctx['target_probe_sha256']=old.sha(reportpath)
    ctx['NF61_report_path']=reportpath
    upgrade=enlarged_precision.configure(1000,800)
    ctx['sources']=enlarged_precision.promote(ctx['sources'],1000,800)
    ctx['target_source']=enlarged_precision.promote(ctx['target_source'],1000,800)
    ctx['precision_metadata']=upgrade
    (Path('work/nf62')/(parity+'-proof-1000')).mkdir(parents=True,exist_ok=True)
    momentkey=parity+'-1700-1000-'+old.sha('scripts/native_precision_nf62.py')
    ctx['m']=old.cached(Path('work/nf62')/(parity+'-proof-1000')/'moments.pkl',momentkey,lambda:type(m)(1700,parity))
    base=base[:5]+enlarged_precision.promote(base[5:],1000,800)
    matrices=tuple(matrix(cert[k]) for k in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram',
        'enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses'])+base[5:]
    return ctx,shadow,path,matrices

def selection(ctx,cert,matrices):
    frozen=Path('work/nf62')/ctx['parity']/'selected_high.json' if 'parity' in ctx else Path('work/nf62')/(['even','odd'][ctx['idx']])/'selected_high.json'
    assert frozen.is_file(),'NF62 requires the already-frozen exterior selection'
    trial=json.loads(frozen.read_text());trial['selection_interval_grid_digits']=800
    return trial

def unused_original_selection(ctx,cert,matrices):
    M,QH,GH,B,S,Q,G=matrices
    # Selection needs only the denominator inverse and cross vector. The
    # complete 56-by-56 reaction matrix is certified separately in run().
    C=v.symmetry(v.c.add(QH,v.c.scale(M,-K)))
    U=v.symmetry(v.c.add(v.c.add(GH,v.c.scale(QH,-2*K)),v.c.scale(M,K*K)))
    W=v.c.add(S,v.c.scale(B,-K));N=v.symmetry(v.c.add(C,v.c.scale(U,1/K)))
    NI,_=v.mi.inverse(N)
    z=list(map(F,cert['joint_lower_bound_sign']['fixed_rational_lower_bound_witness']))
    mass=F(cert['joint_lower_bound_sign']['witness_original_physical_mass_squared'])
    normalization=v.ceilnorm([context49.root(mass)])
    z=[a/normalization for a in z]
    alpha=mv(NI,mv(v.c.tr(W),z));alpha=[a.mid() for a in alpha]
    sources=ctx['sources'];joint=sources[53:56]+sources[:53]
    response=combine([ctx['target_source']],[1/K])
    correction=combine(sources[56:],[-a/(K*K) for a in alpha])
    response=combine([response,correction],[F(1),F(1)])
    hp=n.physical(*v.p.c.merge(ctx['H'],[a/K for a in alpha]))
    response=([],n.add(response[1],hp),response[2],response[3])
    idx=ctx['idx'];shell=list(range(438-idx,501 if idx==0 else 500,2))
    assert all(max(ii)<min(shell) for ii,_ in ctx['H'])
    fun=functional(response,ctx['m'],max(shell));coords=[dot(n.basis(j),fun) for j in shell]
    raw=[F((a.mid()*10**100).__floor__(),10**100) for a in coords]
    H=[dict(zip(ii,cc)) for ii,cc in ctx['H']]
    projection=[F(0) for _ in H]
    orth=list(raw)  # Exterior support is exactly disjoint from every old column.
    norm=v.ceilnorm(orth);assert norm>0
    coeff=[c/norm for c in orth]
    assert all(sum(c*col.get(j,F(0)) for j,c in zip(shell,coeff))==0 for col in H)
    return dict(selection_indices=shell,fixed_rational_high_coefficients=list(map(str,coeff)),
        normalized_frozen_joint_target=list(map(str,z)),frozen_target_normalizing_upper=str(normalization),
        reconstructed_response_coordinates=[a.ends() for a in coords],raw_downrounded_coefficients=list(map(str,raw)),
        exact_old_high_projection_coefficients=list(map(str,projection)),new_direction_normalizing_upper=str(norm),
        exact_new_physical_mass_squared=str(sum(c*c for c in coeff)),
        selection_rule='NF60 direct combined target source; complete joint A0^-1(R alpha+G beta); midpoint down-round 10^100 on exterior degrees438..500/437..499; exact physical projection off all old high columns; rational upper-norm normalization',
        selection_is_not_a_sign_certificate=True)

def append_symmetric(a,cross,diagonal):return [row+[z] for row,z in zip(a,cross)]+[cross+[diagonal]]

def run(parity):
    ctx,cert,parent,matrices=parent_context(parity);idx=ctx['idx']
    precision_metadata=ctx['precision_metadata']
    work=Path('work/nf62')/(parity+'-proof-1000');work.mkdir(parents=True,exist_ok=True)
    m=ctx['m']
    ctx['m']=m
    trial=selection(ctx,cert,matrices)
    (Path('work/nf62')/parity/'selected_high.json').write_text(json.dumps(trial,sort_keys=True)+'\n')
    print(parity,'full joint inverse response selected and exactly orthogonalized',flush=True)
    ii=trial['selection_indices'];cc=list(map(F,trial['fixed_rational_high_coefficients']));mass=v.ceilnorm(cc)
    work=Path('work/nf62')/(parity+'-proof-1000');work.mkdir(parents=True,exist_ok=True)
    key=hashlib.sha256(repr((parity,ii,cc,old.sha(__file__))).encode()).hexdigest()
    sy=old.cached(work/'new_source.pkl',key,lambda:m.source(ii,cc))
    fun=functional(sy,m,max(ii));rawcoords={j:dot(n.basis(j),fun) for j in range(idx,max(ii)+1,2)}
    error=m.eta*mass;paidcoords={j:a+I(-error,error) for j,a in rawcoords.items()}
    low=[paidcoords[j] for j in ctx['ids']];ry=v.r.projection(sy,low,ctx['ids'])
    # sqrt(56)<8 suffices analytically;16 conservatively also covers the
    # independent cell-first interval accumulation about this frozen midpoint.
    ey=error+16*max(F(a.h-a.l,2*n.SCALE) for a in low)
    physical=ctx['P']+[(ctx['ids'],col) for col in ctx['T']]+ctx['H']+[(ii,cc)]
    native=[]
    for ids,col in physical:
        value=sum((a*rawcoords[j] for j,a in zip(ids,col)),I(0));e=error*v.ceilnorm(col)
        native.append(value+I(-e,e))
    sources=ctx['sources'][53:56]+ctx['sources'][:53]+ctx['sources'][56:]+[ry]
    assert 2*(max(len(s[1]) for s in sources)-1)<=1700
    adj=old.cached(work/'new_adjoint.pkl',key,lambda:fast.adjoint(ry,m,max(len(s[1]) for s in sources),
        max(len(s[2]) for s in sources),max(len(c) for s in sources for c in s[3])))
    raw=[fast.gram(s,adj) for s in sources];ny=v.r.normupper(raw[-1])
    errors=list(map(F,cert['joined_source_physical_errors']+cert['remaining_source_physical_errors']+cert['high_source_physical_errors']))+[ey]
    norms=list(map(F,cert['joined_source_approximant_norm_upper']+cert['remaining_source_approximant_norm_upper']+cert['high_source_approximant_norm_upper']))+[ny]
    paid=[]
    for a,e,nb in zip(raw,errors,norms):
        payment=e*ny+ey*nb+e*ey;paid.append(a+I(-payment,payment))
    print(parity,'all new native and complete source pairings paid',len(raw),flush=True)
    M,QH,GH,B,S,Q,G=matrices;hcount=len(ctx['H'])
    ydict=dict(zip(ii,cc));masscross=[sum(a*ydict.get(j,F(0)) for j,a in zip(ids,col)) for ids,col in ctx['H']]
    assert not any(masscross)
    newM=append_symmetric(M,list(map(I,masscross)),I(sum(a*a for a in cc)))
    newQH=append_symmetric(QH,native[56:-1],native[-1]);newGH=append_symmetric(GH,paid[56:-1],paid[-1])
    newB=[row+[a] for row,a in zip(B,native[:56])];newS=[row+[a] for row,a in zip(S,paid[:56])]
    _,_,_,_,_,reaction,cp,np=v.inverse_packet(newM,newQH,newGH,newB,newS,G)
    lower=v.symmetry(v.c.add(Q,v.c.scale(reaction,-1)))
    sign=old.lower_sign(lower,physical[:56])
    oldreaction=unpack(cert['complete_joint_high_inverse_upper_upper_triangle'],56)
    oldlower=unpack(cert['complete_joint_original_Schur_lower_upper_triangle'],56)
    z=list(map(F,trial['normalized_frozen_joint_target']))
    improvement=dot(z,mv(v.c.add(oldreaction,v.c.scale(reaction,-1)),z))
    oldvalue=dot(z,mv(oldlower,z));newvalue=dot(z,mv(lower,z))
    print(parity,sign['status'],'old witness refinement',float(improvement.mid()),flush=True)
    return dict(milestone='NF62',parity=parity,aperture='53/50',original_archive_uncompressed_sha256=ctx['hashes'],
        inherited_NF61_certificate_sha256=old.sha(parent),inherited_NF61_validation_sha256=old.sha(f'notes/data/RPB108_NF61_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'),
        old_target_classification=ctx['target_classification'],old_target_probe_sha256=ctx['target_probe_sha256'],precision_configuration=precision_metadata,precision_controls=precision.controls(),inherited_source_profile_grid_digits=[500,800],
        fixed_high_selection=trial,old_high_dimension=hcount,new_high_dimension=hcount+1,
        selection_exterior_to_all_old_high_support=True,source_square_moment_degree_required=2*(max(len(s[1]) for s in sources)-1),
        inherited_NF60_scalar_validation_sha256=old.sha(ctx['NF60_scalar_path']),inherited_NF60_combined_certificate_sha256=old.sha(ctx['NF60_combined_path']),
        regular_kernel_N=320,pole_degree=40,original_translation_cells=13,interval_grid_digits=1000,selection_interval_grid_digits=800,moment_degree=1700,
        analytic_unit_source_error=str(m.eta),retained_projection_halfwidth_multiplier=16,new_projected_source_error_upper=str(ey),new_source_approximant_norm_upper=str(ny),
        new_source_low_projection=[a.ends() for a in low],new_native_pairings=[a.ends() for a in native],
        reconstructed_new_complete_source_pairings=[a.ends() for a in raw],original_new_complete_source_pairings=[a.ends() for a in paid],
        all_new_native_pairings_certified=len(native),all_new_complete_source_pairings_certified=len(paid),
        enlarged_high_physical_Gram=old.ends(newM),enlarged_high_native_Gram=old.ends(newQH),enlarged_high_complete_source_Gram=old.ends(newGH),
        enlarged_joint_high_native_crosses=old.ends(newB),enlarged_joint_high_complete_source_crosses=old.ends(newS),
        enlarged_surplus_positive_proof=cp,enlarged_inverse_denominator_positive_proof=np,
        complete_joint_high_inverse_upper_upper_triangle=old.upper(reaction),complete_joint_original_Schur_lower_upper_triangle=old.upper(lower),
        normalized_NF61_witness_old_lower_value=oldvalue.ends(),normalized_NF61_witness_new_lower_value=newvalue.ends(),
        normalized_NF61_witness_inverse_reaction_improvement=improvement.ends(),joint_lower_bound_sign=sign,
        source_analytic_infinite_remainders_paid=True,original_joined_and_T53_columns_unchanged=True,old_high_columns_unchanged=True,
        original_inputs_regenerated=False,actual_negative_original_form_claimed=False,
        parity_whole_form_positive=sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND',whole_aperture_positive=False,
        highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--parity',choices=['even','odd'],required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();raw=(json.dumps(run(args.parity),indent=2,sort_keys=True)+'\n').encode()
    Path(args.output).write_bytes(base64.b64encode(gzip.compress(raw,mtime=0))+b'\n')
