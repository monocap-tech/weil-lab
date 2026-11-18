#!/usr/bin/env python3
"""Emit a bounded actual source-row widening trial, not a complete solve.

The source bank in this test is deliberately partial. It contains only
keys/degrees requested by H[0,0] and V[0,0..3]. The remaining H[0,j]
centers are genuine external entries but their lower-triangle enclosures
are NOT checked here. No analytic bank truth is asserted by this emitter.
"""
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F

from emit_nf627_original_moment_bank import emit_bank, filetext, MODULE, qlit
from verify_nf622_physical_entry_reassembly import (
    selected, critical, read_shards, entry, canonical, Q
)

def required_keys(a, bs):
    need={}
    for b in bs:
        for h,f,n,_,_ in a:
            for j,g,m,_,_ in b:
                k=canonical(h+j,f+g)
                if k!=(0,0):
                    need[k]=max(need.get(k,-1),n+m)
    return need

def emit_trial(root, shards, out):
    data=read_shards(root,shards)
    S,C=selected(root),critical(root)
    assert len(S)==242 and len(C)==4
    need=required_keys(S[0],[S[0],*C])
    subset={k:data[k][:n+1] for k,n in need.items()}
    assert all(len(subset[k])==n+1 for k,n in need.items())
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
            for p in shards.rglob('nf621-shard*.json.gz')}
    assert len(hashes)==8
    m=emit_bank(subset,out,32,hashes)
    H=[entry(data,S[0],b) for b in S]
    V=[entry(data,S[0],b) for b in C]
    # A deliberately wider pilot allowance for any reference rounding
    # differences. This is NOT the actual uniform payment radius.
    extra=10**50
    eH=F(max(r for _,r in H)+extra,Q)
    eV=F(max(r for _,r in V)+extra,Q)
    def vec(name,values):
        return 'def '+name+' : Array ℚ := #[\n  '+',\n  '.join(
            f'({v}:ℚ)/(neutralNF616Q:ℚ)' for v,_ in values)+'\n]\n\n'
    body=vec('nf629PilotH0',H)+vec('nf629PilotV0',V)
    body+='''def nf629PilotPayment : NF625PaymentData :=
  ⟨fun _ _ => 0,
   fun i j => if i.val=0 then nf629PilotH0[j.val]! else
     if j.val=0 then nf629PilotH0[i.val]! else 0,
   fun i j => if i.val=0 then nf629PilotV0[j.val]! else 0,
   fun _ => 0, '''+qlit(eH)+','+qlit(eV)+''',0⟩

def nf629PilotM : NF622Moments :=
  neutralNF624Lookup nf627Bank (neutralNF624Index nf627Bank)

def nf629PilotLookup (a b : Bool → NF622TermSpec) : Bool :=
  [true,false].all fun s => [true,false].all fun t =>
    neutralNF624LookupCheck nf627Bank (neutralNF624Index nf627Bank)
      ((a s).key.add (b t).key) ((a s).degree+(b t).degree)

def nf629PilotCoverage : Bool :=
  nf629PilotLookup (neutralNF624SelectedSpec 0) (neutralNF624SelectedSpec 0) &&
  (List.finRange 4).all (fun j =>
    (List.finRange 33).all (fun k =>
      nf629PilotLookup (neutralNF624SelectedSpec 0) (neutralNF624CriticalSpec j k)))

set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem nf629PilotCoverageCheck : nf629PilotCoverage = true := by
  decide +kernel

theorem nf629PilotEntryRow :
    neutralNF629EntryRow nf629PilotM nf629PilotPayment 0 = true := by
  decide +kernel

#print axioms nf629PilotCoverageCheck
#print axioms nf629PilotEntryRow'''
    path=out/'EntryRowPilot.lean'
    path.write_text(filetext([
        'WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTriangularEntries',
        MODULE+'.Bank'],body),encoding='utf-8')
    info={'schema':'NF629-original-entry-row-pilot-v1','keys':m['keys'],
          'rows':m['rows'],'input_sha256':hashes,
          'checked_entries':['H[0,0]']+[f'V[0,{j}]' for j in range(4)],
          'scope':'proposed widening and local lookup checks; not full bank truth or payment',
          'pilot_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    (out/'entry-row-pilot.json').write_text(json.dumps(info,indent=2)+'\n')
    print('NF629 actual first-row pilot proposals:',info['keys'],'keys,',info['rows'],'rows')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--shards',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    emit_trial(a.root,a.shards,a.output)

if __name__=='__main__':
    main()
