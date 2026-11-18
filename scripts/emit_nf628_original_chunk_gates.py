#!/usr/bin/env python3
"""Generate independent kernel gates for NF627 literal chunks.

Full mode reproduces the sorted complete bank; pilot mode intentionally
uses only a few original keys and must not claim source-wide coverage.
"""
import argparse
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from fractions import Fraction as F

from emit_nf627_original_moment_bank import emit_bank, filetext, MODULE

CHECK = 'WeilDefect.Arithmetic.ActualZetaOriginalPhysicalChunkedBank'
OPTIONS = 'set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'

def emit_gates(out, manifest, pilot=False):
    names = [f'Chunk{i:03d}' for i in range(manifest['chunks'])]
    records = []
    def write(name, imports, body):
        path = out / (name + '.lean')
        path.write_text(filetext(imports, body), encoding='utf-8')
        records.append({'file':path.name,
                        'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    for name in names:
        write('Gate'+name, [CHECK, MODULE+'.'+name],
              OPTIONS+f'theorem nf628{name}Check :\n'
              f'    neutralNF628ChunkCheck nf627{name} = true := by\n'
              '  decide +kernel\n\n'
              f'#print axioms nf628{name}Check')
    joined = ', '.join('nf627'+n for n in names)
    checks = ', '.join('nf628'+n+'Check' for n in names)
    write('ChunkJoin', [MODULE+'.Gate'+n for n in names],
          OPTIONS+f'def nf628Chunks : List (Array NF624KeyTable) := [{joined}]\n\n'
          'def nf628Bank : Array NF624KeyTable := neutralNF628Join nf628Chunks\n\n'
          'theorem nf628ChunksCheck : nf628Chunks.all neutralNF628ChunkCheck = true := by\n'
          f'  simp only [nf628Chunks, List.all_cons, List.all_nil, {checks}, Bool.true_and]\n\n'
          'theorem nf628BankCheck : neutralNF624BankCheck nf628Bank = true :=\n'
          '  neutralNF628Bank_of_chunks nf628Chunks nf628ChunksCheck\n\n'
          '#print axioms nf628BankCheck')
    if not pilot:
        write('JoinedShapeGate', [MODULE+'.ChunkJoin', MODULE+'.Metadata'],
              OPTIONS+'theorem nf628JoinedShape :\n'
              '    neutralNF627ShapeCheck nf628Bank nf627Meta = true := by\n'
              '  decide +kernel\n\n#print axioms nf628JoinedShape')
    (out/'chunk-gates.json').write_text(json.dumps({
        'schema':'NF628-local-kernel-proposals-v1','pilot':pilot,
        'keys':manifest['keys'],'rows':manifest['rows'],
        'chunks':manifest['chunks'],'files':records},indent=2)+'\n')

def self_test():
    with TemporaryDirectory() as d:
        out=Path(d)
        m=emit_bank({(F(0),F(1)):[(1,2,3)],
                     (F(1,2),F(2)):[(4,5,6),(7,8,9)]},out,1,{})
        emit_gates(out,m,True)
        j=(out/'ChunkJoin.lean').read_text()
        assert 'nf628Chunk000Check, nf628Chunk001Check' in j
        assert 'neutralNF628Bank_of_chunks' in j
        assert not (out/'JoinedShapeGate.lean').exists()
        emit_gates(out,m)
        assert (out/'JoinedShapeGate.lean').exists()
        for rec in json.loads((out/'chunk-gates.json').read_text())['files']:
            assert hashlib.sha256((out/rec['file']).read_bytes()).hexdigest()==rec['sha256']
        print('NF628 synthetic gate emission PASS; no Lean truth asserted')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path)
    p.add_argument('--shards',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--chunk-size',type=int,default=32)
    p.add_argument('--pilot-keys',type=int,default=0)
    p.add_argument('--self-test',action='store_true')
    a=p.parse_args()
    if a.self_test:
        self_test()
        return
    assert a.root and a.shards and a.output and a.chunk_size>0
    from verify_nf622_physical_entry_reassembly import read_shards
    data=read_shards(a.root,a.shards)
    assert len(data)==7835 and sum(map(len,data.values()))==37994
    sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
             for p in a.shards.rglob('nf621-shard*.json.gz')}
    assert len(sources)==8
    if a.pilot_keys:
        assert 0<a.pilot_keys<len(data)
        # Take low-frequency real-pole and oscillatory keys if available,
        # otherwise use the first original keys in exact sorted order.
        data=dict(sorted(data.items())[:a.pilot_keys])
    m=emit_bank(data,a.output,a.chunk_size,sources)
    emit_gates(a.output,m,bool(a.pilot_keys))
    print('NF628 emitted',m['chunks'],'local gates; pilot=',bool(a.pilot_keys))

if __name__=='__main__': main()
