"""NF50 independent cell-first native/source integrals and joint inverse proof.

Does not import the NF50 producer. Inherits hash-pinned NF49 certified data,
rebuilds the new physical source at moment degree1300 and checks every added
entry, exact physical orthogonality and final rational witness signs.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import validate_native_complete_transport_nf49_106 as prior
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

def run(path):
    cert=read(path);parity=cert['parity'];ctx=prior.context(parity);idx=ctx['idx']
    assert cert['milestone']=='NF50' and cert['aperture']=='53/50'
    assert cert['original_archive_uncompressed_sha256']==ctx['hashes']
    parentpath=f'notes/data/RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64'
    validationpath=f'notes/data/RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_VALIDATION_20261010.json'
    parent=read(parentpath);validation=read(validationpath)
    assert sha(parentpath)==cert['inherited_NF49_certificate_sha256']==validation['encoded_certificate_sha256']
    assert sha(validationpath)==cert['inherited_NF49_validation_sha256'] and validation['status']=='PASS'
    for p,digest in parent['frozen_input_sha256'].items():assert sha(p)==digest
    floor=read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_VALIDATION_20261009.json')
    assert floor['status']=='PASS' and F(floor['original_F112_floor']['independent_original_F112_lower'])>K
    trial=cert['fixed_high_selection'];ii=trial['selection_indices'];cc=list(map(F,trial['fixed_rational_high_coefficients']))
    assert ii==list(range(112+idx,245 if idx==0 else 244,2)) and len(ii)==len(cc)
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
    z=list(map(F,trial['normalized_NF49_joint_witness']));normalization=F(trial['NF49_witness_normalizing_upper'])
    assert [a*normalization for a in z]==list(map(F,parent['joint_lower_bound_sign']['fixed_rational_lower_bound_witness']))
    assert normalization**2>=F(parent['joint_lower_bound_sign']['witness_original_physical_mass_squared'])
    work=Path('work/nf50')/(parity+'-independent');work.mkdir(parents=True,exist_ok=True)
    key=hashlib.sha256(repr((parity,ii,cc,1300,ctx['key'])).encode()).hexdigest()
    m=prior.cached(work/'moments.pkl',key,lambda:h.p.p.old.probe.Moments(1300,parity))
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
    action=prior.cached(work/'new_action.pkl',key+'-'+sha(__file__),lambda:prior.cell_action(ry,m,max(len(s[1]) for s in sources),max(len(s[2]) for s in sources)))
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
    packet=ctx['packet'];count=ctx['count'];o=ctx['o']
    M,QH,GH,BH,SH=[mat(packet[k]) for k in [count+'_high_physical_Gram',count+'_high_native_Gram',count+'_high_complete_source_Gram',
        'joined_'+count+'_high_native_crosses','joined_'+count+'_high_source_crosses']]
    B=BH+mat(parent['original_remaining_high_native_crosses']);S=SH+mat(parent['original_remaining_high_source_crosses'])
    G=block(mat(o['parent37']['original_selected_complete_source_Gram']),ind.transpose(mat(parent['original_remaining_joined_source_crosses'])),
        mat(parent['original_remaining_joined_source_crosses']),prior.unpack(parent['original_remaining_complete_source_Gram_upper'],53))
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
    assert oldvalue.h<0 and improvement.l>0 and newvalue.l>0
    for actual,label in [(improvement,'inverse_reaction_improvement'),(oldvalue,'old_lower_value'),(newvalue,'new_lower_value')]:
        prior.overlap(actual,Box(*map(F,cert['normalized_NF49_witness_'+label])))
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
    return dict(milestone='NF50',status='PASS',parity=parity,certificate_sha256=sha(path),validator_sha256=sha(__file__),
        original_archive_uncompressed_sha256=ctx['hashes'],independent_moment_degree=1300,
        independent_native_pairings_checked=len(native),independent_complete_source_pairings_checked=len(paid),
        exact_new_high_physical_orthogonality_checked=True,analytic_infinite_remainders_paid=True,
        inherited_NF49_certificate_and_validation_authenticated=True,
        independent_enlarged_surplus_positive_proof=cp,independent_enlarged_denominator_positive_proof=np,
        independent_normalized_NF49_witness_inverse_reaction_improvement=[str(improvement.l),str(improvement.h)],
        independent_normalized_NF49_witness_old_lower_value=[str(oldvalue.l),str(oldvalue.h)],
        independent_normalized_NF49_witness_new_lower_value=[str(newvalue.l),str(newvalue.h)],
        joint_lower_bound_sign=signcheck,arithmetic_controls=prior.arithmetic_controls(),joint_controls=ind.controls(),
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20',actual_negative_original_form_claimed=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--certificate',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();result=run(args.certificate);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(result['parity'],'NF50 independent PASS',flush=True)
