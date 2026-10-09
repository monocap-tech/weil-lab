#!/usr/bin/env python3
"""Independent exact vertex/Sylvester verification; no producer import."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product, permutations
import argparse,json,hashlib
SHA=['0cb636cdf03ad09f57cfce6d4bc67d0b7094dc1c154597cb0d1fe467590a2fd6','ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788','316ea81720e0992699ee8a37c5cc48b1170d811ef6d88bbdf19d46d03860c7a9','96a4f1448b0aa0d347ce79345e222d260c70af22cc86e7cd998626883e6fdb90','4004a41e1ff792ea667719ba889d5908b3098581fd0dfbf437e96fe0c6cf9f93']
def box(v):return tuple(map(F,v))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):
    vs=[x*y for x in a for y in b];return min(vs),max(vs)
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,v):return mul(a,(v,v))
def inside(a,b):return b[0]<=a[0]<=a[1]<=b[1]
def determinant(A):
    n=len(A);out=F(0)
    for p in permutations(range(n)):
        v=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):v*=A[i][p[i]]
        out+=v
    return out
def vertex_sylvester(A):
    n=len(A);positions=[(i,j) for i in range(n) for j in range(i,n)]
    assert all(A[i][j]==A[j][i] for i,j in positions)
    choices=[sorted(set(A[i][j])) for i,j in positions];vertices=0;checks=0;minors=[None]*n
    for values in product(*choices):
        M=[[F(0)]*n for _ in range(n)]
        for (i,j),v in zip(positions,values):M[i][j]=M[j][i]=v
        for k in range(1,n+1):
            d=determinant([row[:k] for row in M[:k]]);assert d>0
            minors[k-1]=d if minors[k-1] is None else min(d,minors[k-1]);checks+=1
        vertices+=1
    return vertices,checks,list(map(str,minors))
def validate(paths,primary,replay):
    data=[Path(p).read_bytes() for p in paths];assert [hashlib.sha256(v).hexdigest() for v in data]==SHA;checks=1
    joint,low,even,odd,old=[json.loads(v) for v in data]
    a=json.loads(Path(primary).read_bytes());b=json.loads(Path(replay).read_bytes());records=[];k=F(11,25)
    assert a['input_sha256']==b['input_sha256']==SHA;checks+=1
    for idx,(r,rp,j,l,s,o) in enumerate(zip(a['rows'],b['rows'],joint['rows'],low['native_parity_gates'],(even,odd),old['rows'])):
        t=F(r['young_source_parameter']);credit=F(r['complete_four_column_source_credit']);sc=[F(1)]+list(map(F,j['congruence_scales']))
        assert r['parity']==rp['parity']==j['parity']==l['parity']==s['parity']==o['parity'];checks+=1
        assert 0<t and 0<credit<k and credit>8*F(o['reported_complete_remainder_source_credit']);checks+=1
        Q=[[box(v) for v in row] for row in r['scaled_native_matrix']]
        G=[[box(v) for v in row] for row in r['scaled_block_source_input']]
        D=[[box(v) for v in row] for row in r['scaled_coherent_source_majorant']]
        H=[[box(v) for v in row] for row in r['signed_comparison_matrix']]
        Q0=[[(F(0),F(0)) for _ in range(4)] for _ in range(4)];G0=[[(F(0),F(0)) for _ in range(4)] for _ in range(4)]
        Q0[0][0]=box(l['native_Q_diagonal']);P0=F(l['full_F112_source_square'][1]);G0[0][0]=(P0,P0)
        for i,v in enumerate(j['original_low_lift_pairings']):Q0[0][i+1]=Q0[i+1][0]=box(v)
        for i in range(3):
            for h in range(3):
                for field,A in [('original_native_energy_Gram',Q0),('original_complete_source_Gram',G0)]:
                    x=box(s[field][i][h]);y=box(s[field][h][i]);A[i+1][h+1]=(max(x[0],y[0]),min(x[1],y[1]));assert A[i+1][h+1][0]<=A[i+1][h+1][1];checks+=1
        for i in range(4):
            for h in range(4):
                assert inside(scale(Q0[i][h],sc[i]*sc[h]),Q[i][h]);checks+=1
                assert inside(scale(G0[i][h],sc[i]*sc[h]),G[i][h]);checks+=1
                fac=1+1/t if i==h==0 else 1+t
                assert inside(scale(G[i][h],fac),D[i][h]);checks+=1
                assert inside(minus(scale(Q[i][h],k-credit),D[i][h]),H[i][h]);checks+=1
                for key in ['scaled_native_matrix','scaled_block_source_input','scaled_coherent_source_majorant','signed_comparison_matrix']:
                    assert inside(box(rp[key][i][h]),box(r[key][i][h]));checks+=1
        q=F(r['native_scaled_identity_lower']);ell=list(map(F,r['scaled_coarse_diagonal_lower']))
        N=[[minus(Q[i][h],(q,q) if i==h else (F(0),F(0))) for h in range(4)] for i in range(4)]
        U=[[minus(minus(Q[i][h],scale(D[i][h],1/k)),(ell[i],ell[i]) if i==h else (F(0),F(0))) for h in range(4)] for i in range(4)]
        for name,M in [('source_credit',H),('native_identity',N),('physical_diagonal',U)]:
            vs,cs,mins=vertex_sylvester(M);checks+=cs;records.append(dict(parity=r['parity'],matrix=name,vertices=vs,positive_leading_minors=cs,minimal_leading_determinants=mins))
        masses=list(map(F,o['high_completed_column_mass_upper']));gap=1/(sum((ss*m)**2/e for ss,m,e in zip(sc,masses,ell))+1/k)
        assert gap==F(r['physical_gap_strict_lower'])==F(rp['physical_gap_strict_lower'])>F(a['physical_gap_guard'])>F(old['eight_direction_physical_gap_guard']) and gap>F(o['whole_high_physical_gap_strict_lower']);checks+=1
        assert r['complete_four_column_source_credit']==rp['complete_four_column_source_credit'] and r['young_source_parameter']==rp['young_source_parameter'] and r['column_scales']==rp['column_scales']==list(map(str,sc)) and r['scaled_coarse_diagonal_lower']==rp['scaled_coarse_diagonal_lower'] and r['high_completed_column_mass_upper']==rp['high_completed_column_mass_upper']==o['high_completed_column_mass_upper'];checks+=1
        # Nonzero, signed low/source crosses: coherent Young is an exact square.
        sources=[[F(1),F(-2),F(3)],[F(2),F(1),F(-1)],[F(-1),F(3),F(2)],[F(3),F(-1),F(1)]]
        for z in product(range(-1,2),repeat=4):
            x=[z[0]*v for v in sources[0]];y=[sum(z[i]*sources[i][h] for i in range(1,4)) for h in range(3)]
            lhs=(1+1/t)*sum(v*v for v in x)+(1+t)*sum(v*v for v in y)-sum((v+w)**2 for v,w in zip(x,y))
            assert lhs==sum((v-t*w)**2 for v,w in zip(x,y))/t>=0;checks+=1
        for z in product(range(-1,2),repeat=5):
            mass=sum(abs(v)*ss*m for v,ss,m in zip(z[:4],sc,masses))+abs(z[4]);energy=sum(e*v*v for e,v in zip(ell,z[:4]))+k*z[4]**2
            assert energy>=gap*mass*mass;checks+=1
    # Genuine full-block crossings and whole-physical-mass positive levels.
    controls=[]
    for border in [F(99,100),F(1),F(101,100)]:
        d=determinant([[F(1),border],[border,F(1)]]);assert (d>0)==(border<1) and (d==0)==(border==1);checks+=1
        controls.append(dict(border=str(border),determinant=str(d)))
    for lam in [F(1,10),F(1),F(2)]:
        A=[[1+lam,F(1)],[F(1),1+lam]];assert determinant(A)>0 and (A[0][0]+A[1][1]-2)/2==lam;checks+=1
    return dict(stage='DNE28',status='PASS',independent_rational_checks=checks,
        complete_symmetric_box_vertex_checks=records,
        certificate_sha256=hashlib.sha256(Path(primary).read_bytes()).hexdigest(),
        replay_sha256=hashlib.sha256(Path(replay).read_bytes()).hexdigest(),
        coherent_source_Young_controls=162,physical_completion_controls=486,
        crossing_controls=controls,complete_remaining_Gram_certified=False,whole_aperture_positive=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for key in ['dne23','low','even','odd','dne27','certificate','replay','output']:p.add_argument(key)
    a=p.parse_args();r=validate([getattr(a,k) for k in ['dne23','low','even','odd','dne27']],a.certificate,a.replay)
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'checks':r['independent_rational_checks'],'vertices':sum(v['vertices'] for v in r['complete_symmetric_box_vertex_checks'])}))
