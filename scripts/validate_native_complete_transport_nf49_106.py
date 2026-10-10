"""NF49 independent cell-first signed moments and joint lower-bound checks.

Does not import the NF49 certifier. Reconstructs the original sources at a
different moment cutoff, integrates combined polynomial sources cell first,
and checks all entries and the final sign with independent rational boxes.
"""
import argparse,base64,gzip,hashlib,json,pickle,sys
from pathlib import Path
from fractions import Fraction as F
from math import factorial,isqrt
sys.set_int_max_str_digits(0)
import validate_native_remaining_native_nf48_106 as oldcheck
import certify_native_next_shell_nf46_106 as historic
from native_transport_nf49_moments import convolution
originals=oldcheck.originals;physical=oldcheck.physical
ind=oldcheck.independent;Box=ind.Box;K=F(207,1000);GRID=10**500


def read(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.b64'):raw=gzip.decompress(base64.b64decode(raw))
    return json.loads(raw)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def root(q):return F(isqrt((F(q)*GRID*GRID).__floor__())+1,GRID)
def overlap(a,b):assert max(a.l,b.l)<=min(a.h,b.h)


class CellBox:
    def __init__(self,lo=0,hi=None):self.l=lo;self.h=lo if hi is None else hi;assert self.l<=self.h
    def __add__(self,other):return CellBox(self.l+other.l,self.h+other.h)
    def __mul__(self,other):
        values=[self.l*other.l,self.l*other.h,self.h*other.l,self.h*other.h]
        return CellBox(min(values)//GRID,-((-max(values))//GRID))
    def box(self):return Box(F(self.l,GRID),F(self.h,GRID))


def add(a,b):
    return [CellBox((a[i].l if i<len(a) else 0)+(b[i].l if i<len(b) else 0),
                    (a[i].h if i<len(a) else 0)+(b[i].h if i<len(b) else 0)) for i in range(max(len(a),len(b)))]


def weighted(poly,moments,count):
    # Ceiling centers differ from the producer's floor centers. The four
    # integer convolutions independently pay every coefficient uncertainty.
    p=list(reversed(poly));m=moments[:len(poly)+count-1];assert len(m)==len(poly)+count-1
    pc=[(v.l+v.h+1)//2 for v in p];mc=[(v.l+v.h+1)//2 for v in m]
    pr=[max(c-v.l,v.h-c) for c,v in zip(pc,p)];mr=[max(c-v.l,v.h-c) for c,v in zip(mc,m)]
    c=convolution(pc,mc)
    errorparts=[convolution(pr,list(map(abs,mc))),convolution(list(map(abs,pc)),mr),convolution(pr,mr)]
    return [CellBox((c[k]-sum(e[k] for e in errorparts))//GRID,-((-(c[k]+sum(e[k] for e in errorparts)))//GRID))
            for k in range(len(poly)-1,len(poly)-1+count)]


def cell_action(source,m,bcount,lcount):
    _,b,l,cells=source;out=[];logs=weighted(l,m.ML2,lcount)
    for c,(mp,ml) in zip(cells,m.cm):
        combined=add(b,c)
        out.append(add(weighted(combined,mp,bcount),weighted(l,ml,bcount)))
        logs=add(logs,weighted(combined,ml,lcount))
    return out,logs


def pair(source,action):
    _,b,l,cells=source;vectors,logs=action
    lower=upper=0
    for c,vector in zip(cells,vectors):
        for i,z in enumerate(vector[:max(len(b),len(c))]):
            lo=(b[i].l if i<len(b) else 0)+(c[i].l if i<len(c) else 0)
            hi=(b[i].h if i<len(b) else 0)+(c[i].h if i<len(c) else 0)
            if lo or hi:
                values=[lo*z.l,lo*z.h,hi*z.l,hi*z.h]
                lower+=min(values);upper+=max(values)
    for a,z in zip(l,logs):
        if a.l or a.h:
            values=[a.l*z.l,a.l*z.h,a.h*z.l,a.h*z.h]
            lower+=min(values);upper+=max(values)
    return CellBox(lower//GRID,-((-upper)//GRID)).box()


def arithmetic_controls():
    from types import SimpleNamespace
    p=[CellBox(-2*GRID,-GRID),CellBox(0,GRID),CellBox(3*GRID,4*GRID)]
    moments=[CellBox((i-1)*GRID,(i+1)*GRID) for i in range(9)]
    for i,z in enumerate(weighted(p,moments,7)):
        terms=[[a.l*moments[i+j].l,a.l*moments[i+j].h,a.h*moments[i+j].l,a.h*moments[i+j].h] for j,a in enumerate(p)]
        assert z.l<=sum(min(t) for t in terms)//GRID
        assert z.h>=-((-sum(max(t) for t in terms))//GRID)
    m=SimpleNamespace(ML2=[CellBox(13*GRID//4)],cm=[([CellBox(GRID)],[CellBox(GRID//2)]) for _ in range(13)])
    a=([],[CellBox(GRID)],[CellBox(-2*GRID)],[[CellBox((i-6)*GRID)] for i in range(13)])
    b=([],[CellBox(-3*GRID)],[CellBox(2*GRID)],[[CellBox((i%3-1)*GRID)] for i in range(13)])
    result=pair(a,cell_action(b,m,1,1));expected=F(sum((i-6)*(-2+i%3-1) for i in range(13)))
    assert result.l==result.h==expected
    return dict(ceiling_center_Hankel_corner_controls='PASS',signed_thirteen_cell_mixed_log_identity='PASS')


def cached(path,key,builder):
    if path.is_file():
        record=pickle.loads(path.read_bytes())
        if record['key']==key:return record['value']
    value=builder();path.write_bytes(pickle.dumps(dict(key=key,value=value),protocol=5));return value


def context(parity):
    idx=['even','odd'].index(parity);data,source,hashes=originals.inputs()
    nf47=read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json');frame=nf47['parity_frames'][idx]
    ind.validate_frame(frame,idx)
    o=physical.objects(data,source,parity);P=o['columns'];ids=o['ids']
    assert P==[(v['indices'],list(map(F,v['coefficients']))) for v in frame['unchanged_joined_columns']]
    x=list(map(F,data[0]['authenticated_compensated_targets'][idx]['retained_coefficients']))
    w=list(map(F,data[2]['parity_certificates'][idx]['exact_rational_retained_response']))
    u=[dict(zip(*P[2])).get(j,F(0)) for j in ids]
    p,q=frame['old_two_constraint_pivots'];free=frame['old_free_coordinates'];det=x[p]*w[q]-x[q]*w[p]
    base=[]
    for j in free:
        col=[F(int(i==j)) for i in range(56)]
        col[p]=(x[q]*w[j]-w[q]*x[j])/det;col[q]=(w[p]*x[j]-x[p]*w[j])/det;base.append(col)
    ell=[sum(a*b for a,b in zip(u,col)) for col in base];assert list(map(str,ell))==frame['third_constraint_coordinates']
    pivot=frame['third_constraint_pivot_in_old_free_coordinates']
    T=[[a-ell[j]/ell[pivot]*b for a,b in zip(col,base[pivot])] for j,col in enumerate(base) if j!=pivot]
    assert len(T)==53 and all(sum(a*b for a,b in zip(col,r))==0 for col in T for r in [x,w,u])
    if idx==0:
        trial=read('notes/data/RPB108_NF46_EVEN_FIXED_NEXT_SHELL_20261009.json');label='eighth';count='eight'
        H=[(row['indices'],list(map(F,row['coefficients']))) for row in trial['seven_high_columns']]
        loH,eH=historic.high_projection_data(0,o,historic.parents()[2])
        packet=read('notes/data/RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json')
    else:
        trial=read('notes/data/RPB108_NF45_ODD_FIXED_INVERSE_WITNESS_20261009.json');label='seventh';count='seven'
        H=[(row['indices'],list(map(F,row['coefficients']))) for row in trial['six_high_columns']]
        loH,eH=historic.prior.high_projection_data(1,o,historic.prior.parents()[3])
        packet=read('notes/data/RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json')
    H.append((trial['selection_indices'],list(map(F,trial['fixed_rational_'+label+'_high_coefficients']))))
    co=dict(zip(packet['reconstructed_'+label+'_source_coordinates_indices'],map(physical.iv,packet['reconstructed_'+label+'_source_coordinates'])))
    loH.append([co[j] for j in ids]);eH.append(F(packet[label+'_projected_source_error_upper']))
    def Q(i,j):return physical.I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    lowT=[[sum((v*Q(i,j) for i,v in zip(ids,col) if v),physical.I(0)) for j in ids] for col in T]
    columns=[(ids,col) for col in T]+P+H;low=lowT+o['low']+loH
    key=hashlib.sha256(repr((parity,columns,[[z.ends() for z in row] for row in low],1200,GRID,
        [sha('scripts/'+p) for p in ['certify_native_correlated_sources_nf25_106.py','certify_native_high_correction_nf26_106.py',
         'certify_native_expanded_response_nf30_106.py','certify_native_remaining_source_probe_nf32_106.py']])).encode()).hexdigest()
    work=Path('work/nf49')/(parity+'-independent');work.mkdir(parents=True,exist_ok=True)
    m=cached(work/'moments.pkl',key,lambda:historic.p.p.old.probe.Moments(1200,parity))
    sources=[]
    for j,((ii,cc),projection) in enumerate(zip(columns,low)):
        s=cached(work/f'source_{j:02d}.pkl',key,lambda ii=ii,cc=cc,projection=projection:
            historic.r.projection(m.source(ii,cc),projection,ids))
        sources.append(s);print(parity,'independent source',j+1,'/',len(columns),flush=True)
    return dict(idx=idx,data=data,hashes=hashes,ids=ids,T=T,P=P,H=H,lowT=lowT,loH=loH,eH=eH,o=o,
                packet=packet,count=count,m=m,sources=sources,work=work,key=key)


def unpack(entries,size):
    assert len(entries)==size*(size+1)//2
    matrix=[[None]*size for _ in range(size)];k=0
    for i in range(size):
        for j in range(i,size):matrix[i][j]=matrix[j][i]=Box(*map(F,entries[k]));k+=1
    return matrix


def compare(a,b):
    assert len(a)==len(b) and all(len(x)==len(y) for x,y in zip(a,b))
    for x,y in zip(a,b):
        for v,w in zip(x,y):overlap(v,w)


def run(path,ctx):
    cert=read(path);parity=cert['parity'];idx=ctx['idx'];m=ctx['m'];sources=ctx['sources'];T=ctx['T'];H=ctx['H'];o=ctx['o']
    assert cert['milestone']=='NF49' and cert['aperture']=='53/50' and idx==['even','odd'].index(parity)
    assert cert['original_archive_uncompressed_sha256']==ctx['hashes']
    for p,h in cert['frozen_input_sha256'].items():assert sha(p)==h
    floor=read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_VALIDATION_20261009.json')
    assert floor['status']=='PASS' and floor['certificate_sha256']==sha('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
    assert F(floor['original_F112_floor']['independent_original_F112_lower'])>K
    replay=read('notes/data/RPB108_NF48_ORIGINAL_NF46_REPLAY_20261009.json');assert replay['status']=='PASS'
    assert all(r['status']=='PASS_BYTE_IDENTICAL' for r in replay['unchanged_historical_runner_report']['fresh_NF46_replay'])
    assert cert['regular_kernel_N']==320 and cert['pole_degree']==40 and cert['original_translation_cells']==13 and cert['interval_grid_digits']==500
    unit=2*F(53,50)*4*F(106,125)**320/(1-F(106,125))+16*(F(53,100))**41/F(factorial(41))
    assert unit==m.eta==F(cert['source_analytic_unit_error'])
    masses=[root(sum(v*v for v in col)) for col in T]
    errorT=[unit*mass+8*max(F(z.h-z.l,2*GRID) for z in low) for mass,low in zip(masses,ctx['lowT'])]
    assert list(map(str,errorT))==cert['remaining_source_physical_errors']
    assert list(map(str,ctx['eH']))==cert['high_source_physical_errors']
    for (_,col),low,err in zip(H,ctx['loH'],ctx['eH']):
        # Unit boundary columns have exact physical norm one; retain that
        # exact square rather than adding an unnecessary grid unit to it.
        needed=unit*oldcheck.sqrt_upper(sum(v*v for v in col))+8*max(F(z.h-z.l,2*GRID) for z in low)
        assert err>=needed
    assert list(map(str,o['physical_source_errors']))==cert['joined_source_physical_errors']
    bcount=max(len(s[1]) for s in sources);lcount=max(len(s[2]) for s in sources)
    rawTT=[[None]*53 for _ in range(53)];rawTP=[[None]*3 for _ in range(53)];rawTH=[[None]*len(H) for _ in range(53)]
    for j in range(53):
        action=cached(ctx['work']/f'action_{j:02d}.pkl',ctx['key']+'-'+sha(__file__),lambda j=j:cell_action(sources[j],m,bcount,lcount))
        for i in range(j+1):rawTT[i][j]=rawTT[j][i]=pair(sources[i],action)
        for k in range(3):rawTP[j][k]=pair(sources[53+k],action)
        for k in range(len(H)):rawTH[j][k]=pair(sources[56+k],action)
        print(parity,'independent cell-first covariances',j+1,'/ 53',flush=True)
    compare(rawTT,unpack(cert['reconstructed_remaining_source_Gram_upper'],53))
    compare(rawTP,ind.boxmatrix(cert['reconstructed_remaining_joined_source_crosses']))
    compare(rawTH,ind.boxmatrix(cert['reconstructed_remaining_high_source_crosses']))
    packet=ctx['packet'];count=ctx['count'];GH=ind.boxmatrix(packet[count+'_high_complete_source_Gram'])
    GP=ind.boxmatrix(o['parent37']['original_selected_complete_source_Gram'])
    normT=[root(rawTT[j][j].h) for j in range(53)]
    errorP=o['physical_source_errors'];errorH=ctx['eH']
    normP=[root(GP[j][j].h)+errorP[j] for j in range(3)];normH=[root(GH[j][j].h)+errorH[j] for j in range(len(H))]
    def pay(raw,ea,eb,na,nb):return [[v+Box(-(ea[i]*nb[j]+eb[j]*na[i]+ea[i]*eb[j]),ea[i]*nb[j]+eb[j]*na[i]+ea[i]*eb[j]) for j,v in enumerate(row)] for i,row in enumerate(raw)]
    TT=pay(rawTT,errorT,errorT,normT,normT);TP=pay(rawTP,errorT,errorP,normT,normP);TH=pay(rawTH,errorT,errorH,normT,normH)
    compare(TT,unpack(cert['original_remaining_complete_source_Gram_upper'],53));compare(TP,ind.boxmatrix(cert['original_remaining_joined_source_crosses']))
    compare(TH,ind.boxmatrix(cert['original_remaining_high_source_crosses']))
    nativeTH=[[sum((v*Box(F(z.l,GRID),F(z.h,GRID)) for v,z in zip(col,ctx['loH'][j])),Box(0))+Box(-errorH[j]*masses[i],errorH[j]*masses[i])
               for j in range(len(H))] for i,col in enumerate(T)]
    compare(nativeTH,ind.boxmatrix(cert['original_remaining_high_native_crosses']))
    compare(ind.add(TH,ind.scale(nativeTH,-K)),ind.boxmatrix(cert['original_remaining_surplus_source_crosses']))
    QH=ind.boxmatrix(packet[count+'_high_native_Gram']);MH=ind.boxmatrix(packet[count+'_high_physical_Gram'])
    C=ind.add(QH,ind.scale(MH,-K));surplus_inverse,surplus_proof=oldcheck.independent_inverse(C)
    UGram=ind.add(ind.add(GH,ind.scale(QH,-2*K)),ind.scale(MH,K*K));N=ind.add(C,ind.scale(UGram,1/K))
    inverse,denominator_proof=oldcheck.independent_inverse(N)
    joinedNative=ind.boxmatrix(packet['joined_'+count+'_high_native_crosses']);joinedSource=ind.boxmatrix(packet['joined_'+count+'_high_source_crosses'])
    W=ind.add(joinedSource+TH,ind.scale(joinedNative+nativeTH,-K))
    fullG=[a+b for a,b in zip(GP,ind.transpose(TP))]+[a+b for a,b in zip(TP,TT)]
    response=ind.add(ind.scale(fullG,1/K),ind.scale(ind.mm(ind.mm(W,inverse),ind.transpose(W)),-1/(K*K)))
    oldnative=read('notes/data/RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64')['parity_certificates'][idx]
    B0=ind.transpose(ind.boxmatrix(oldnative['original_remaining_native_couplings']));Q=ind.boxmatrix(o['parent37']['original_selected_native_energy_Gram'])
    finiteC=ind.boxmatrix(oldnative['original_remaining_native_Gram'])
    fullQ=[a+b for a,b in zip(Q,ind.transpose(B0))]+[a+b for a,b in zip(B0,finiteC)]
    lower=ind.add(fullQ,ind.scale(response,-1))
    compare(response,unpack(cert['complete_joint_high_inverse_upper_upper_triangle'],56));compare(lower,unpack(cert['complete_joint_original_Schur_lower_upper_triangle'],56))
    sign=cert['joint_lower_bound_sign'];check=dict(status=sign['status'])
    if sign['status']=='JOINT_LOWER_BOUND_REJECTED':
        witness=list(map(F,sign['fixed_rational_lower_bound_witness']));assert len(witness)==56
        value=ind.dot(witness,[ind.dot(row,witness) for row in lower]);assert value.h<0
        coefficients={}
        for scalar,(ids,col) in zip(witness,ctx['P']+[(ctx['ids'],col) for col in T]):
            for j,c in zip(ids,col):coefficients[j]=coefficients.get(j,F(0))+scalar*c
        mass=sum(v*v for v in coefficients.values());assert str(mass)==sign['witness_original_physical_mass_squared']
        overlap(value,Box(*map(F,sign['witness_lower_matrix_value'])))
        check.update(independent_witness_lower_matrix_value=value.ends(),independent_physical_quotient=(value/mass).ends(),
                     actual_negative_original_vector_claimed=False)
    elif sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND':
        _,proof=oldcheck.independent_inverse(lower);check['independent_positive_congruence_proof']=proof
    else:assert sign['status']=='UNRESOLVED'
    assert cert['all_remaining_source_Gram_entries_certified']==1431 and cert['all_signed_joined_source_crosses_certified']==159
    assert cert['all_signed_existing_high_source_crosses_certified']==53*len(H)
    assert cert['complete_remaining_source_transport_data_certified'] and cert['source_analytic_infinite_remainders_paid']
    assert cert['parity_whole_form_positive']==(sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND')
    assert not cert['whole_aperture_positive']
    assert not any(cert[k] for k in ['actual_negative_original_form_claimed','original_frozen_vectors_changed','original_inputs_regenerated','RH','F4','Lean'])
    print(parity,'independent complete transport PASS',check['status'],flush=True)
    return dict(milestone='NF49',parity=parity,status='PASS',encoded_certificate_sha256=sha(path),
        original_archive_uncompressed_sha256=ctx['hashes'],independent_source_reconstruction_count=len(sources),
        independent_moment_degree=1200,method='cell-first combined polynomial moments; ceiling-center integer Hankel; rational Gaussian inverse proof',
        all_remaining_source_Gram_entries_checked=1431,all_signed_joined_source_crosses_checked=159,
        all_signed_high_source_crosses_checked=53*len(H),all_original_source_infinite_remainders_paid=True,
        independent_surplus_proof=surplus_proof,independent_denominator_proof=denominator_proof,
        original_F112_floor_inherited_from_passed_NF47=True,joint_lower_bound_check=check,
        parity_whole_form_positive=sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND',whole_aperture_positive=False,
        actual_negative_original_form_claimed=False,controls=ind.controls(),arithmetic_controls=arithmetic_controls())


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--parity',choices=['even','odd'],required=True)
    p.add_argument('--prepare',action='store_true');p.add_argument('--certificate');p.add_argument('--output');a=p.parse_args()
    ctx=context(a.parity)
    if not a.prepare:
        assert a.certificate and a.output
        Path(a.output).write_text(json.dumps(run(a.certificate,ctx),indent=2,sort_keys=True)+'\n')
