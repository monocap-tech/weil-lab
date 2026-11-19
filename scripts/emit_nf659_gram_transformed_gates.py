#!/usr/bin/env python3
"""NF659 exact 15x15 transformed-center/radius Lean gates from pinned witness."""
import argparse,hashlib,json,sys
from pathlib import Path
sys.set_int_max_str_digits(0)
N=15
sha=lambda x:hashlib.sha256(x).hexdigest()
def matrix(name,m):
    return f'def {name} : Array (Array ℤ) := #[\n'+',\n'.join(
        '  #['+','.join(f'({v}:ℤ)' for v in row)+']' for row in m)+'\n]\n\n'
def wrap(imports,body):
    return ''.join('import '+x+'\n' for x in imports)+'''
namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

'''+body+'\nend WeilDefect\n'
def produce(witness,out):
    raw=witness.read_bytes();w=json.loads(raw)
    assert w['schema']=='NF657-original-15-source-compact-congruence-v1'
    assert w['indices']==list(range(14))+[241] and w['S']=='10^64' and w['Q']=='10^2600'
    K=[[int(x) for x in row] for row in w['K_scaled']]
    C=[[int(x) for x in row] for row in w['H_center_scaled']]
    E=[[int(x) for x in row] for row in w['H_radius_scaled']]
    assert all(len(a)==N and all(len(row)==N for row in a) for a in (K,C,E))
    assert all(C[i][j]==C[j][i] and E[i][j]==E[j][i]>=0 for i in range(N) for j in range(N))
    T=[[sum(K[i][p]*K[j][q]*C[p][q] for p in range(N) for q in range(N))
        for j in range(N)] for i in range(N)]
    U=[[sum(abs(K[i][p]*K[j][q])*E[p][q] for p in range(N) for q in range(N))
        for j in range(N)] for i in range(N)]
    assert all(T[i][j]==T[j][i] and U[i][j]==U[j][i]>=0 for i in range(N) for j in range(N))
    M=[T[i][i]-U[i][i]-sum(abs(T[i][j])+U[i][j] for j in range(N) if i!=j)
        for i in range(N)]
    assert M==list(map(int,w['dominance_margin_scaled_numerator'])) and min(M)>0
    kn=sum(k*k for row in K for k in row)
    assert kn==int(w['K_norm_sq_scaled_numerator']) and min(M)*10**60>10**64*kn
    out.mkdir(parents=True,exist_ok=True);files=[]
    def write(name,imports,body):
        p=out/(name+'.lean');p.write_text(wrap(imports,body))
        files.append({'file':p.name,'sha256':sha(p.read_bytes())})
    body=matrix('nf659ComputedCenters',T)+matrix('nf659ComputedRadii',U)
    body+='''def nf659CenterAt (i j : Fin 15) : ℤ :=
  (nf659ComputedCenters[i.val]!).getD j.val 0

def nf659RadiusAt (i j : Fin 15) : ℤ :=
  (nf659ComputedRadii[i.val]!).getD j.val 0

def nf659MarginAt (i : Fin 15) : ℤ :=
  nf659CenterAt i i - nf659RadiusAt i i -
    ∑ j : Fin 15, if j=i then 0 else
      |nf659CenterAt i j| + nf659RadiusAt i j

theorem nf659MarginOfArray : ∀ i : Fin 15,
    nf659MarginAt i = nf658Margins[i.val]! := by
  decide +kernel

theorem nf659MarginPositive (i : Fin 15) : 0 < nf659MarginAt i := by
  rw [nf659MarginOfArray]
  exact nf658MarginPos i

theorem nf659MarginUniform (i : Fin 15) :
    nf658MinMargin ≤ nf659MarginAt i := by
  rw [nf659MarginOfArray]
  exact nf658MinMarginLe i

def nf659KNormSq : ℤ :=
  ∑ i : Fin 15, ∑ j : Fin 15, (nf658Get nf658Kints i j)^2

theorem nf659KNormSq_eq : nf659KNormSq = nf658Ksq := by
  decide +kernel

theorem nf659ExactCoercivityGate :
    nf658MinMargin * (10^60:ℤ) > (10^64:ℤ) * nf659KNormSq := by
  rw [nf659KNormSq_eq]
  exact nf658CoercivityIntegerGate

theorem nf659CentersSymm : ∀ i j : Fin 15,
    nf659CenterAt i j = nf659CenterAt j i := by
  decide +kernel

theorem nf659RadiiSymm : ∀ i j : Fin 15,
    nf659RadiusAt i j = nf659RadiusAt j i := by
  decide +kernel

#print axioms nf659MarginOfArray
'''
    write('ComputedData',['WeilDefect.Generated.NF658.TransformPilot'],body)
    for i in range(N):
        body=''
        for j in range(N):
            body+=f'theorem nf659C{i:02d}_{j:02d} : nf658TransformedCenter {i} {j} = nf659CenterAt {i} {j} := by\n  decide +kernel\n'
            body+=f'theorem nf659R{i:02d}_{j:02d} : nf658TransformedRadius {i} {j} = nf659RadiusAt {i} {j} := by\n  decide +kernel\n'
        body+=f'#print axioms nf659C{i:02d}_00\n#print axioms nf659R{i:02d}_14\n'
        write(f'Row{i:02d}',['WeilDefect.Generated.NF659.ComputedData'],body)
    write('Complete',[f'WeilDefect.Generated.NF659.Row{i:02d}' for i in range(N)],
          '-- All 225 exact transformed centers and 225 exact radii.\n'
          '#print axioms nf659C00_00\n#print axioms nf659R14_14')
    report={'schema':'NF659-transformed-physical-gram-exact-integer-v1',
        'input_sha256':sha(raw),'source_archive_sha256':w['source_archive_sha256'],
        'center_checks':N*N,'radius_checks':N*N,'positive_margins':N,
        'minimal_margin_integer':str(min(M)),
        'integer_coercivity_gate':str(min(M)*10**60-10**64*kn),
        'files':files,'scope':'exact emitted proof targets, not Lean acceptance'}
    (out/'manifest.json').write_text(json.dumps(report,indent=2)+'\n')
    print('NF659 450 transformed integer identities, 15 margins, exact preflight PASS')
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('witness',type=Path)
    a.add_argument('output',type=Path);x=a.parse_args()
    produce(x.witness,x.output)
