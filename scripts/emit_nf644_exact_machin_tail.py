#!/usr/bin/env python3
"""Exact compressed reference Machin prefix chains, bound to retained NF635 pi."""
import argparse,gzip,hashlib,json
from pathlib import Path
from emit_nf632_segmented_pi import Q,N,ball,segment
from emit_nf627_original_moment_bank import filetext
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalExactMachinTail'
MODULE='WeilDefect.Generated.NF644'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((a.bank/'manifest.json').read_text())
    assert manifest['full_values'] and manifest['real_count']==5 and manifest['phase_count']==1276
    for x in manifest['files']:
        assert hashlib.sha256((a.bank/x['file']).read_bytes()).hexdigest()==x['sha256']
    with gzip.open(a.bank/'endpoints.json.gz','rt') as f: retained=json.load(f)
    files=[]; results=[]; ends=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(filetext(imports,OPT+body))
        files.append({'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    for p,cut in ((5,1858),(239,546)):
        assert p**(2*cut+1)*(2*cut+1)>Q
        assert p**(2*(cut-2)+1)*(2*(cut-2)+1)<=Q
        prev=None; total=(0,0)
        for start in range(0,cut,32):
            length=min(32,cut-start)
            m,r=segment(p,start,length)
            total=(total[0]+m,total[1]+r)
            name=f'Atan{p}_{start:04d}'; v='nf644'+name
            pv='nf644'+prev+'Prefix' if prev else '⟨0,0⟩'
            ph='nf644'+prev+'PrefixEq' if prev else '(by rfl)'
            body=f'def {v}Segment : NF591Ball := {ball(m,r)}\ndef {v}Prefix : NF591Ball := {ball(*total)}\n\n'
            body+=f'theorem {v}SegmentCheck : neutralNF632BallEq (neutralNF632AtanSegment (1/{p}) neutralNF616Q {start} {length}) {v}Segment=true := by\n  decide +kernel\n'
            body+=f'theorem {v}AddCheck : neutralNF632BallEq (NF591Ball.add {pv} {v}Segment) {v}Prefix=true := by\n  decide +kernel\n'
            body+=f'theorem {v}PrefixEq : neutralNF592AtanPartial (1/{p}) neutralNF616Q {start+length}={v}Prefix :=\n  neutralNF632AtanPrefix_extend (1/{p}) neutralNF616Q {start} {length} {pv} {v}Segment {v}Prefix {ph} {v}SegmentCheck {v}AddCheck\n'
            write(name,[MODULE+'.'+prev] if prev else [BASE],body); prev=name
        pairs=(N-cut)//2
        result=(total[0]-pairs,total[1]+2*pairs)
        assert result==segment(p,0,N)
        v='nf644Tail'+str(p); pv='nf644'+prev+'Prefix'
        body=f'def {v} : NF591Ball := {ball(*result)}\n'
        body+=f'theorem {v}Bound : decide (neutralNF616Q < neutralNF644Denom {p} (2*{cut//2}))=true := by\n  decide +kernel\n'
        body+=f'theorem {v}Check : neutralNF632BallEq ({pv}.add (neutralNF644Tail neutralNF616Q {pairs})) {v}=true := by\n  decide +kernel\n'
        body+=f'theorem {v}Eq : neutralNF592AtanPartial (1/{p}) neutralNF616Q neutralNF616AtanN={v} :=\n  neutralNF644AtanTail_of_prefix {p} neutralNF616Q {cut//2} {pairs} {pv} {v} (by decide) neutralNF616Q_pos {v}Bound nf644{prev}PrefixEq {v}Check\n'
        body+=f'#print axioms {v}Eq'
        write('Tail'+str(p),[MODULE+'.'+prev],body)
        results.append(result); ends.append({'p':p,'cutoff':cut,'pairs':pairs,'prefix_segments':(cut+31)//32})
    (m,r),(n,s)=results
    pp=(16*m-4*n,16*(r+1)+4*(s+1)+2)
    assert pp==tuple(map(int,retained['pi'])) and pp[1]==39942
    body=f'def nf644Pi : NF591Ball := {ball(*pp)}\n'
    body+='theorem nf644PiCheck : neutralNF632BallEq (neutralNF632PiFromPartials nf644Tail5 nf644Tail239 neutralNF616Q) nf644Pi=true := by\n  decide +kernel\n'
    body+='theorem nf644PiEq : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=nf644Pi :=\n  neutralNF632Pi_of_partials _ _ _ _ _ nf644Tail5Eq nf644Tail239Eq nf644PiCheck\n'
    body+='theorem nf644PiSound : nf644Pi.Contains Real.pi := neutralNF632HighPrecisionPi_sound _ nf644PiEq\n\n#print axioms nf644PiEq\n#print axioms nf644PiSound'
    write('Pi',[MODULE+'.Tail5',MODULE+'.Tail239'],body)
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF644-exact-Machin-tail-proposals-v1','slots':ends,'files':files,'retained_bank_manifest_sha256':hashlib.sha256((a.bank/'manifest.json').read_bytes()).hexdigest(),'scope':'untrusted kernel proof proposals'},indent=2)+'\n')
    print('NF644 retained pi exactly reproduced; 2404 prefix terms, 1596 compressed; 80 modules')
if __name__=='__main__': main()
