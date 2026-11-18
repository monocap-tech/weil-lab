#!/usr/bin/env python3
"""Emit untrusted original NF624 moment bank proposals in bounded Lean modules.

No proof is asserted by generation. The metadata uses only key/degree,
and its coverage is later transported by a separate exact shape check.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from tempfile import TemporaryDirectory

sys.set_int_max_str_digits(0)
MODULE = 'WeilDefect.Generated.NF627'
NS = 'WeilDefect'
BASE = 'WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentBank'
META = 'WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMetadataCoverage'

def qlit(x):
    x=F(x)
    return f'({x.numerator}/{x.denominator}:ℚ)'

def keylit(k):
    return '⟨'+','.join(qlit(x) for x in k)+'⟩'

def scaled(x):
    return f'({int(x)}:ℚ)/(neutralNF616Q:ℚ)'

def rowlit(row):
    assert len(row)==3 and row[2]>=0
    return '⟨'+','.join(scaled(x) for x in row)+'⟩'

def filetext(imports,body):
    return ''.join(f'import {m}\n' for m in imports)+f'\nnamespace {NS}\n\n'+body+'\n\nend '+NS+'\n'

def metadata_body(shapes, size=128):
    """Bound literal elaboration, preserving every ordered key/degree."""
    assert size>0 and shapes
    parts=[]
    body='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
    for start in range(0,len(shapes),size):
        name=f'nf627MetaPart{start//size:03d}'
        parts.append(name)
        body+=f'def {name} : Array NF624KeyTable := #[\n  '+',\n  '.join(shapes[start:start+size])+'\n]\n\n'
    body+='def nf627Meta : Array NF624KeyTable :=\n'
    body+='  (#['+', '.join(parts)+'] : Array (Array NF624KeyTable)).foldl (fun a b => a ++ b) #[]'
    return body

def emit_bank(data,out,chunk_size,source_hashes):
    assert chunk_size>0 and data
    out.mkdir(parents=True,exist_ok=True)
    ordered=sorted(data.items())
    assert all(k!=(0,0) and rows for k,rows in ordered)
    names=[]; records=[]
    def write(name,content):
        path=out/(name+'.lean')
        path.write_text(content,encoding='utf-8')
        records.append({'file':path.name,'bytes':path.stat().st_size,
                        'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    for i in range(0,len(ordered),chunk_size):
        name=f'Chunk{i//chunk_size:03d}'
        entries=[]
        for k,rows in ordered[i:i+chunk_size]:
            entries.append('⟨'+keylit(k)+', #[\n    '+',\n    '.join(map(rowlit,rows))+'\n  ]⟩')
        body=f'def nf627{name} : Array NF624KeyTable := #[\n  '+',\n  '.join(entries)+'\n]'
        write(name,filetext([BASE],body))
        names.append(name)
    parts=', '.join('nf627'+name for name in names)
    write('Bank',filetext([MODULE+'.'+name for name in names],
          f'def nf627Bank : Array NF624KeyTable :=\n  (#[{parts}] : Array (Array NF624KeyTable)).foldl (fun a b => a ++ b) #[]'))
    shapes=['⟨'+keylit(k)+f', Array.replicate {len(rows)} ⟨0,0,0⟩⟩' for k,rows in ordered]
    write('Metadata',filetext([META],metadata_body(shapes)))
    write('MetadataGate',filetext([MODULE+'.Metadata'],
          'set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
          'theorem nf627MetadataCoverage :\n'
          '    neutralNF624CoverageCheck nf627Meta (neutralNF624Index nf627Meta) = true := by\n'
          '  decide +kernel\n\n#print axioms nf627MetadataCoverage'))
    write('ShapeGate',filetext([MODULE+'.Metadata',MODULE+'.Bank'],
          'set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
          'theorem nf627BankMatchesMetadata : neutralNF627ShapeCheck nf627Bank nf627Meta = true := by\n'
          '  decide +kernel\n\n#print axioms nf627BankMatchesMetadata'))
    summary={'schema':'NF627-untrusted-lean-bank-v1','keys':len(ordered),
             'rows':sum(len(rows) for _,rows in ordered),'chunks':len(names),
             'input_sha256':source_hashes,'files':records,
             'scope':'untrusted proposals; no Lean truth or analytical soundness asserted'}
    (out/'manifest.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

def self_test():
    with TemporaryDirectory() as d:
        out=Path(d)
        data={(F(1,2),F(2,3)):[(10,-11,3),(2,4,5)],
              (F(-1,2),F(1,3)):[(-9,8,7)],
              (F(0),F(2)):[(5,6,7)]}
        m=emit_bank(data,out,2,{})
        assert (m['keys'],m['rows'],m['chunks'])==(3,4,2)
        a=(out/'Chunk000.lean').read_text()
        assert a.index('(-1/2:ℚ)')<a.index('(0/1:ℚ)')
        assert '(-9:ℚ)/(neutralNF616Q:ℚ)' in a
        assert 'Array.replicate 2' in (out/'Metadata.lean').read_text()
        for r in m['files']:
            assert hashlib.sha256((out/r['file']).read_bytes()).hexdigest()==r['sha256']
        print('NF627 emitter synthetic serialization PASS (not Lean acceptance)')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path)
    p.add_argument('--shards',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--chunk-size',type=int,default=32)
    p.add_argument('--self-test',action='store_true')
    a=p.parse_args()
    if a.self_test:
        self_test()
        return
    assert a.root and a.shards and a.output
    from verify_nf622_physical_entry_reassembly import read_shards
    data=read_shards(a.root,a.shards)
    assert len(data)==7835 and sum(map(len,data.values()))==37994
    sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in a.shards.rglob('nf621-shard*.json.gz')}
    assert len(sources)==8
    m=emit_bank(data,a.output,a.chunk_size,sources)
    print('NF627 emitted',m['keys'],'keys',m['rows'],'rows in',m['chunks'],'chunks; untrusted proposals')
if __name__=='__main__': main()
