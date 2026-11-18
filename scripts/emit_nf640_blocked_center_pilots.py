#!/usr/bin/env python3
"""Literal dot and mass custody pilots from retained NF631 widened data.
Recompute every mass, every vector product and four actual matrix products.
The generated Lean files are local proof proposals, with global attachment
to the full input matrices still separate.
"""
import argparse
import gzip
import json
from pathlib import Path
from emit_nf630_original_literal_payments import historical, payment_receipt, sha, rat, array, filetext
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA

BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBlockedCenterReceipts'
MODULE='WeilDefect.Generated.NF640'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def dot(x,y): return sum(a*b for a,b in zip(x,y))

def main():
    p=argparse.ArgumentParser()
    for k in ('root','historical','entries','payments','cache','output'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    dh=sha(a.historical); eh=sha(a.entries)
    payment=payment_receipt(a.payments,eh,frame)
    selected=(0,N-1)
    cols=[sum(abs(row[i]) for row in D) for i in range(N)]
    masses=[sum(map(abs,row)) for row in D]
    total=sum(cols); wm=sum(map(abs,w)); ym=dot([abs(v) for v in y],cols)
    files=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(filetext(imports,OPT+body))
        files.append({'file':path.name,'sha256':sha(path)})
    # Store only the two needed H rows, all V rows, and the two HD columns.
    H={i:[0]*N for i in selected}; V=[]
    with gzip.open(a.entries,'rt') as f:
        head=json.loads(next(f))
        assert head['schema']=='NF622-original-physical-entry-balls-v1'
        assert head['scale']=='10^2600'
        for i,line in enumerate(f):
            q=json.loads(line); assert q['row']==i<N
            assert len(q['H_lower'])==i+1 and len(q['V'])==4
            v=[int(x[0]) for x in q['H_lower']]
            for j in selected:
                if i==j: H[j][:i+1]=v
                elif i>j: H[j][i]=v[j]
            V.append([int(x[0]) for x in q['V']])
    assert len(V)==N
    HD={j:[] for j in selected}; HDrow={}; Arow={}; vectors=[]
    with gzip.open(a.cache,'rt') as f:
        head=json.loads(next(f))
        assert head['schema']=='NF626-integer-center-cache-v1'
        assert head['entry_sha256']==eh and head['historical_sha256']==dh
        assert head['frame_sha256']==frame and head['frozen_sha256']==FROZEN_SHA
        assert {k:int(v) for k,v in head['scales'].items()}==dict(S=S,Q=Q,U=U,T=T)
        assert list(map(int,head['y']))==y and list(map(int,head['w']))==w
        assert [rat(head[k]) for k in ('eH','eV','r')]==[rat(payment[k]) for k in ('uniform_H_radius','uniform_V_radius','r')]
        for i,line in enumerate(f):
            q=json.loads(line); assert q['i']==i<N
            hd,ar=list(map(int,q['HD'])),list(map(int,q['A']))
            assert len(hd)==len(ar)==N
            for j in selected: HD[j].append(hd[j])
            if i in selected: HDrow[i]=hd; Arow[i]=ar
            vv={k:int(q[k]) for k in ('Vw','b','Ay','Dy')}
            assert vv['Vw']==dot(V[i],w)
            assert vv['Ay']==dot(ar,y) and vv['Dy']==dot(D[i],y)
            vectors.append(vv)
    assert len(vectors)==N
    vw=[v['Vw'] for v in vectors]
    assert all(v['b']==dot([row[i] for row in D],vw) for i,v in enumerate(vectors))
    # Entire mass vector generated; local proofs of two row/column pairs and totals.
    body=''
    for label,vs in [('Cols',cols),('Y',y),('W',w)]:
        body+=f'def nf640{label} : Array ℤ := {array(vs)}\n\n'
    body+=f'theorem nf640Totals : neutralNF640TotalsGate (fun i => nf640Cols[i.val]!) (fun i => nf640Y[i.val]!) (fun i => nf640W[i.val]!) ({total}:ℤ) ({wm}:ℤ) ({ym}:ℤ)=true := by\n  decide +kernel\n\n'
    for i in selected:
        for label,vs,value in [('Row',D[i],masses[i]),('Col',[row[i] for row in D],cols[i])]:
            name=f'nf640{label}{i:03d}'
            body+=f'def {name} : Array ℤ := {array(vs)}\n\n'
            body+=f'theorem {name}Mass : neutralNF640AbsGate (fun j : Fin 242 => {name}[j.val]!) ({value}:ℤ)=true := by\n  decide +kernel\n\n'
            body+=f'#print axioms {name}Mass\n'
    body+='#print axioms nf640Totals\n'
    write('MassPilot',[BASE],body)
    blocks=[list(range(i,min(i+32,N))) for i in range(0,N,32)]
    body=''
    bn=[]
    for k,is_ in enumerate(blocks):
        name=f'nf640Block{k:02d}'; bn.append(name)
        body+=f'def {name} : List (Fin 242) := ['+', '.join(map(str,is_))+']\n'
    body+='\ndef nf640Blocks : List (List (Fin 242)) := ['+', '.join(bn)+']\n'
    body+='theorem nf640Partition : nf640Blocks.flatten=List.finRange 242 := by\n  decide +kernel\n'
    write('Blocks',[BASE],body)
    count=0
    for i in selected:
        j=i; dc=[row[i] for row in D]
        for label,x,z,expected in [('HD',H[i],dc,HDrow[i][j]),('A',dc,HD[j],Arow[i][j])]:
            assert dot(x,z)==expected
            name=f'{label}{i:03d}'; v='nf640'+name
            values=[sum(x[k]*z[k] for k in b) for b in blocks]
            assert sum(values)==expected
            body=f'def {v}X : Array ℤ := {array(x)}\ndef {v}Y : Array ℤ := {array(z)}\n'
            body+=f'def {v}x (i : Fin 242) : ℤ := {v}X[i.val]!\ndef {v}y (i : Fin 242) : ℤ := {v}Y[i.val]!\n'
            body+=f'def {v}Values : List ℤ := ['+', '.join(f'({a}:ℤ)' for a in values)+']\n\n'
            proofs=[]
            for k,val in enumerate(values):
                th=f'{v}Check{k:02d}'; eq=f'{v}Eq{k:02d}'; proofs.append(eq)
                body+=f'theorem {th} : neutralNF640DotGate {v}x {v}y {bn[k]} ({val}:ℤ)=true := by\n  decide +kernel\n'
                body+=f'theorem {eq} : neutralNF640DotBlock {v}x {v}y {bn[k]}=({val}:ℤ) := of_decide_eq_true {th}\n\n'
            body+=f'theorem {v}Map : nf640Blocks.map (neutralNF640DotBlock {v}x {v}y)={v}Values := by\n'
            body+='  simp only [nf640Blocks,List.map_cons,List.map_nil,'+', '.join(proofs)+f',{v}Values]\n'
            body+=f'theorem {v}Sum : {v}Values.sum=({expected}:ℤ) := by\n  decide +kernel\n'
            body+=f'theorem {v}Dot : neutralNF626Dot {v}x {v}y=({expected}:ℤ) :=\n  neutralNF640Dot_of_blocks {v}x {v}y nf640Blocks {v}Values ({expected}:ℤ) nf640Partition {v}Map {v}Sum\n'
            body+=f'#print axioms {v}Dot\n'
            write(name,[MODULE+'.Blocks'],body); count+=1
    manifest={'schema':'NF640-blocked-center-pilots-v1','entry_sha256':eh,'historical_sha256':dh,
        'cache_sha256':sha(a.cache),'payment_sha256':sha(a.payments),'mass_rows_external':N,
        'mass_columns_external':N,'vector_products_external':4*N,'matrix_products_external':count,
        'kernel_proposals':{'mass_gates':5,'dot_blocks':count*len(blocks),'dot_identities':count},'files':files,
        'scope':'literal local proposals; full matrix identity attachment remains open'}
    (a.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print('NF640 external checks: 242 row masses, 242 column masses, 968 vector products, 4 matrix products; emitted 32 exact dot blocks')
if __name__=='__main__': main()
