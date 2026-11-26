#!/usr/bin/env python3
"""Generate disjoint importable row sectors, using unchanged IV159 predicates.
This creates source only; it does not certify it. No external receipt
or numerical result enters a Lean theorem as a premise."""
from pathlib import Path
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--sector',type=int,choices=range(8))
p.add_argument('--assemble',action='store_true')
p.add_argument('--root',type=Path,default=Path('WeilDefect/Arithmetic/IV160Bank'))
a=p.parse_args()
root=a.root
root.mkdir(parents=True,exist_ok=True)
ns='WeilDefect.Arithmetic.IV160Bank.'
header='namespace WeilDefect\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
def write(stem,imports,body,name):
    path=root/(stem+'.lean')
    text=''.join('import '+i+'\n' for i in imports)+header+body+f'\n#print axioms {name}\nend WeilDefect\n'
    if path.exists() and path.read_text()!=text:
        raise RuntimeError('refusing to overwrite existing proof source: '+str(path))
    path.write_text(text)
def dispatch(i,groups):
    # Nested bounded cases, all arithmetic side conditions are checked.
    lines=[]
    indent='  '
    for lo,hi,name in groups[:-1]:
        lines.append(indent+f'by_cases h{i}_{hi} : {i} < {hi}')
        lines.append(indent+f'· exact {name} {i} (by omega) (by omega)')
        lines.append(indent+'·')
        indent+='  '
    lo,hi,name=groups[-1]
    lines.append(indent+f'exact {name} {i} (by omega) (by omega)')
    return '\n'.join(lines)
sectors=[(32,128)]+[(128*k,128*(k+1)) for k in range(1,8)]
assert [i for lo,hi in sectors for i in range(lo,hi)]==list(range(32,1024))
if a.sector is not None:
    lo,hi=sectors[a.sector]
    stems=[]
    for b in range(lo,hi,2):
        stem=f'Row{b:04}'
        # Match IV160 leaf source byte-for-byte, retaining global names.
        path=root/(stem+'.lean')
        text='import WeilDefect.Arithmetic.ActualZetaIV159AMRowReceiver\n'+header
        for j in (b,b+1):
            n=f'neutralIV159Row_{j:04}'
            text+=f'theorem {n} : neutralIV159RowBlock {j} = true := by decide\n#print axioms {n}\n'
        text+='end WeilDefect\n'
        if path.exists() and path.read_text()!=text: raise RuntimeError(str(path))
        path.write_text(text)
        stems.append(stem)
    groups=[]
    for b in range(lo,hi,8):
        stem=f'RowGroup{b:04}'
        name=f'neutralIV160RowGroup_{b:04}'
        body=f'theorem {name} (i : ℕ) (hl : {b} ≤ i) (hu : i < {b+8}) : neutralIV159RowBlock i = true := by\n  interval_cases i\n'
        body+='\n'.join(f'  · exact neutralIV159Row_{j:04}' for j in range(b,b+8))
        write(stem,[ns+f'Row{j:04}' for j in range(b,b+8,2)],body,name)
        groups.append((b,b+8,name))
        stems.append(stem)
    stem=f'RowSector{a.sector:02}'
    name=f'neutralIV165{stem}'
    body=f'theorem {name} (i : ℕ) (hl : {lo} ≤ i) (hu : i < {hi}) : neutralIV159RowBlock i = true := by\n'+dispatch('i',groups)
    write(stem,[ns+f'RowGroup{b:04}' for b in range(lo,hi,8)],body,name)
    stems.append(stem)
    (root/f'{stem}.json').write_text(json.dumps({'block_interval':[lo,hi],'row_interval':[8*lo,8*hi],'modules':stems},indent=2))
if a.assemble:
    # Prefix has its own receiver signature; wrap it into a sector signature.
    imports=[ns+'RowPrefix0032']+[ns+f'RowSector{k:02}' for k in range(8)]
    for stem in [x.split('.')[-1] for x in imports]:
        assert (root/(stem+'.lean')).is_file(),stem
    groups=[(0,32,'neutralIV165Prefix')]+[(lo,hi,f'neutralIV165RowSector{k:02}') for k,(lo,hi) in enumerate(sectors)]
    body='theorem neutralIV165Prefix (i : ℕ) (_hl : 0 ≤ i) (hu : i < 32) : neutralIV159RowBlock i = true := neutralIV160RowPrefix0032 i hu\n\n'
    body+='theorem neutralIV160RowBank (i : ℕ) (hi : i < 1024) : neutralIV159RowBlock i = true := by\n'+dispatch('i',groups)
    write('RowBank',imports,body,'neutralIV160RowBank')
