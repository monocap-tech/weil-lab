#!/usr/bin/env python3
"""All 104 frozen remainder native energies, with a paid rational congruence."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import argparse,base64,gzip,hashlib,json

PARENT='cb92d7361a067506ee2a87d4cec9467beaff553d'
ARCHIVE='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    elif p.endswith('.gz'):b=gzip.decompress(b)
    return json.loads(b),hashlib.sha256(b).hexdigest()
class I:
    digits=120
    def __init__(self,a=0,b=None):
        if isinstance(a,I):self.l,self.h=a.l,a.h;return
        scale=10**self.digits;a=F(a);b=a if b is None else F(b)
        self.l=F((a*scale).__floor__(),scale);self.h=F((b*scale).__ceil__(),scale);assert self.l<=self.h
    def __add__(a,b):b=I(b);return I(a.l+b.l,a.h+b.h)
    __radd__=__add__
    def __neg__(a):return I(-a.h,-a.l)
    def __sub__(a,b):return a+-I(b)
    def __rsub__(a,b):return I(b)+-a
    def __mul__(a,b):
        b=I(b);v=[x*y for x in (a.l,a.h) for y in (b.l,b.h)];return I(min(v),max(v))
    __rmul__=__mul__
    def box(a):return [str(a.l),str(a.h)]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def mm(A,B):return [[dot(row,col) for col in zip(*B)] for row in A]
def tr(A):return [list(row) for row in zip(*A)]
def midpoint(v):return (v.l+v.h)/2
def precondition(B):
    # Decimal arithmetic only chooses the rational matrix. No sign conclusion.
    with localcontext() as ctx:
        ctx.prec=160
        M=[[D(midpoint(v).numerator)/D(midpoint(v).denominator) for v in row] for row in B];n=len(M)
        L=[[D(i==j) for j in range(n)] for i in range(n)];piv=[]
        for i in range(n):
            z=M[i][i]-sum((L[i][k]**2*piv[k] for k in range(i)),D(0));assert z>0;piv.append(z)
            for j in range(i+1,n):L[j][i]=(M[j][i]-sum((L[j][k]*L[i][k]*piv[k] for k in range(i)),D(0)))/z
        LT=tr(L);U=[[D(0)]*n for _ in range(n)]
        for j in range(n):
            for i in reversed(range(j+1)):
                U[i][j]=((D(1)/piv[j].sqrt()) if i==j else D(0))-sum((LT[i][k]*U[k][j] for k in range(i+1,j+1)),D(0))
        return [[F(round(F(v)*10**80),10**80) for v in row] for row in U]
def compact_archive(path,out):
    d,sha=read(path);assert sha==ARCHIVE and d['aperture']=='53/50' and d['dim']==112
    grid=10**100;data={}
    for i in range(112):
        for j in range(i,112,2):
            lo,hi=map(F,d['complete_form'][f'{i},{j}']['full'])
            data[f'{i},{j}']=[str(F((lo*grid).__floor__(),grid)),str(F((hi*grid).__ceil__(),grid))]
    b=(json.dumps(dict(stage='DNE32',aperture='53/50',original_decoded_archive_sha256=sha,original_N=d['N'],original_K=d['K'],outward_grid_digits=100,complete_original_retained_native=data),indent=2)+'\n').encode()
    Path(out).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n');print('authenticated native export',len(data),'entries')
def run(parity,archive,primary_path,replay_path,output):
    ix=0 if parity=='even' else 1;upper=parity.upper();raw,rh=read(archive);assert raw['original_decoded_archive_sha256']==ARCHIVE
    native_path=f'notes/data/RPB108_DNE31_{upper}_NATIVE_BORDER_20261009.json.gz.b64'
    frame_path=f'notes/data/RPB108_DNE31_{upper}_REMAINDER_FRAME_20261009.json.gz.b64'
    native,nh=read(native_path);frame,fh=read(frame_path);primary,ph=read(primary_path);replay,sh=read(replay_path)
    assert native['parity']==frame['parity']==primary['parity']==replay['parity']==parity
    assert primary['regular_order']==900 and replay['regular_order']==940
    assert primary['input_sha256']==replay['input_sha256']==native['input_sha256'] and primary['exact_W_columns']==replay['exact_W_columns']==native['exact_W_columns']
    W=tr([list(map(F,row)) for row in native['exact_W_columns']]);ids=native['retained_indices'];J=[list(map(F,row)) for row in frame['frozen_scaled_projection_J']];scale=list(map(F,frame['column_scales']))
    Q=[[I(*raw['complete_original_retained_native'][f'{min(i,j)},{max(i,j)}']) for j in ids] for i in ids]
    sparse=[[(i,v) for i,v in enumerate(col) if v] for col in zip(*W)]
    Braw=[[sum((Q[i][j]*x*y for i,x in c for j,y in d),I(0)) for d in sparse] for c in sparse]
    A=[];P=[];nested=0
    for i in range(4):
        row=[]
        for j in range(4):
            a=list(map(F,primary['fresh_original_T4_native_matrix'][i][j]));b=list(map(F,replay['fresh_original_T4_native_matrix'][i][j]));assert a[0]<=b[0]<=b[1]<=a[1];nested+=1
            lo,hi=map(F,frame['tightened_scaled_T4_native_matrix'][i][j]);s=scale[i]*scale[j]
            for x,y in [(i,j),(j,i)]:
                v=list(map(F,replay['fresh_original_T4_native_matrix'][x][y]));lo=max(lo,v[0]*s);hi=min(hi,v[1]*s)
            assert lo<=hi;row.append(I(lo,hi))
        A.append(row);row=[]
        for j in range(52):
            a=list(map(F,primary['original_native_T4_W52_border'][i][j]));b=list(map(F,replay['original_native_T4_W52_border'][i][j]));assert a[0]<=b[0]<=b[1]<=a[1];nested+=1
            old=list(map(F,native['original_native_T4_W52_border'][i][j]));assert old[0]<=b[0]<=b[1]<=old[1]
            row.append(I(b[0]*scale[i],b[1]*scale[i]))
        P.append(row)
    cross=mm(tr(P),J);correction=mm(tr(J),mm(A,J));B=[[Braw[i][j]-cross[i][j]-cross[j][i]+correction[i][j] for j in range(52)] for i in range(52)]
    # Intersect both orientations: all describe the same original symmetric form.
    B=[[I(max(B[i][j].l,B[j][i].l),min(B[i][j].h,B[j][i].h)) for j in range(52)] for i in range(52)]
    print(parity,'full native remainder assembled',flush=True)
    U=precondition(B);C=mm(tr(U),mm(B,U));margins=[]
    for i in range(52):margins.append(C[i][i].l-sum(max(abs(C[i][j].l),abs(C[i][j].h)) for j in range(52) if j!=i))
    margin=min(margins);assert margin>0
    # Physical raw-W mass, not the much larger physical mass of hatY.
    # B^-1 <= U U*/margin, so tr(G_W B^-1)<=||W U||_F^2/margin.
    mass_matrix=[[sum(x*y for x,y in zip(a,b)) for b in zip(*W)] for a in zip(*W)]
    # W is sparse; form WU in exact rational arithmetic without interval grids.
    WU=[[sum(x*y for x,y in zip(row,col)) for col in zip(*U)] for row in W]
    mass=sum(x*x for row in WU for x in row);bound=margin/mass
    required=F(frame['required_hatY_native_floor_relative_W_mass']);assert bound>required
    guard=F(1,10**100);assert guard<bound
    while guard*10<bound:guard*=10
    f2=F(frame['scaled_border_Frobenius_squared_upper']);q=F(frame['native_scaled_identity_lower']);credit=F(frame['optimized_T4_source_credit']);kappa=F(frame['original_high_floor'])
    dual2=f2/(q*guard);allocation=(credit/(4*kappa))**2;assert dual2<allocation
    eps=credit/(4*kappa);assert eps<1
    y_mass=sum(F(v['exact_mass_squared']) for v in frame['exact_frozen_remainder_column_records'])
    selected,_=read(native['input_paths'][2]);t_mass=[F(1)]+[F(v['exact_mass_squared']) for v in selected['columns']]
    scaled_t_mass=sum(s*s*m for s,m in zip(scale,t_mass))
    physical_y_guard=guard/y_mass
    physical_full_guard=(1-eps)/(2*(scaled_t_mass/q+y_mass/guard))
    out=dict(stage='DNE32',parent=PARENT,parity=parity,input_paths=[archive,native_path,frame_path,primary_path,replay_path],input_sha256=[rh,nh,fh,ph,sh],original_decoded_archive_sha256=ARCHIVE,
        nested_source_checks=nested,remaining_dimension=52,native_matrix_formula='Q(hatY)=W*Q_E*W-P_s*J-J*P_s+J*A_s*J',
        complete_original_native_remainder_matrix=[[v.box() for v in row] for row in B],tightened_scaled_T4_native_matrix=[[v.box() for v in row] for row in A],tightened_scaled_T4_W52_border=[[v.box() for v in row] for row in P],
        exact_rational_congruence_U=[[str(x) for x in row] for row in U],congruence_matrix=[[v.box() for v in row] for row in C],congruence_Gershgorin_margins=list(map(str,margins)),congruence_margin_lower=str(margin),
        exact_raw_W_mass_matrix=[[str(x) for x in row] for row in mass_matrix],exact_WU_Frobenius_squared=str(mass),native_floor_relative_raw_W_mass_lower=str(bound),native_floor_guard=str(guard),display_native_floor_lower=float(bound),
        DNE31_required_native_floor=str(required),DNE31_mixed_native_border_hypothesis_discharged=True,native_mixed_dual_border_squared_upper=str(dual2),native_mixed_dual_allocation_squared=str(allocation),
        exact_total_frozen_remainder_physical_mass=str(y_mass),exact_total_scaled_tested_physical_mass=str(scaled_t_mass),remaining_native_physical_gap_guard=str(physical_y_guard),full_finite_lifted_native_physical_gap_guard=str(physical_full_guard),full_finite_lifted_native_family_positive=True,
        remaining_native_energy_certified=True,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
    b=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n' if output.endswith('.gz.b64') else b)
    print(json.dumps({'parity':parity,'native_floor':float(bound),'guard':str(guard),'congruence_margin':float(margin),'source_Gram_certified':False}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--export-archive');p.add_argument('--archive');p.add_argument('--parity');p.add_argument('--primary');p.add_argument('--replay');p.add_argument('--output',required=True);a=p.parse_args()
    if a.export_archive:compact_archive(a.export_archive,a.output)
    else:run(a.parity,a.archive,a.primary,a.replay,a.output)
