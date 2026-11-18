#!/usr/bin/env python3
"""Prepare metadata-only retry from the actual NF627 archive, with no new moments.
Pass the original archive directory and a generated output directory.
This checks byte/shape custody, not kernel truth.
"""
import argparse,gzip,hashlib,json,re,zipfile
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import metadata_body,filetext,META

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--archives',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    sha=lambda b:hashlib.sha256(b).hexdigest()
    m=a.archives/'nf627-metadata.zip'
    assert sha(m.read_bytes())=='cd18543559e6ddacbd5439c3c15dd4c96698fae11903d8af794efce52e5ffbaa'
    b=a.archives/'nf635-endpoints.zip'
    assert sha(b.read_bytes())=='2b0e45897c28a1ed8d671b2958c8a51646e818e742ecbcf4ed6fcf02f31ed363'
    with zipfile.ZipFile(m) as z:
        old=z.read('Metadata.lean').decode()
        gate=z.read('MetadataGate.lean')
    with zipfile.ZipFile(b) as z:
        hashes=json.loads(z.read('manifest.json'))['input_sha256']
    pat=r'⟨⟨\((-?\d+/\d+):ℚ\),\((-?\d+/\d+):ℚ\)⟩, Array.replicate (\d+) ⟨0,0,0⟩⟩'
    shapes=re.findall(pat,old)
    keys=[(F(h),F(f),int(n)) for h,f,n in shapes]
    assert len(keys)==7835 and sum(n for h,f,n in keys)==37994
    expected={}
    for i in range(8):
        with zipfile.ZipFile(a.archives/f'nf621-shard{i}.zip') as z:
            name=f'nf621-shard{i}.json.gz'
            raw=z.read(name)
            assert sha(raw)==hashes[name]
            t=json.loads(gzip.decompress(raw))
        for row in t['tables']:
            k=(F(row['h']),F(row['f']))
            assert k not in expected
            expected[k]=len(row['rows'])
    assert keys==[(h,f,n) for (h,f),n in sorted(expected.items())]
    literals=[m.group(0) for m in re.finditer(pat,old)]
    body=metadata_body(literals)
    assert re.findall(pat,body)==shapes
    parts=re.findall(r'def (nf627MetaPart\d+) : Array NF624KeyTable := #\[\n(.*?)\n\]',body,re.S)
    sizes=[len(re.findall(pat,p)) for _,p in parts]
    assert sizes==[128]*61+[27]
    assert re.findall(r'nf627MetaPart\d+',body.split('def nf627Meta :',1)[1])==[n for n,_ in parts]
    a.output.mkdir(parents=True,exist_ok=True)
    v=a.output/'Metadata.lean'; v.write_text(filetext([META],body))
    g=a.output/'MetadataGate.lean'; g.write_bytes(gate)
    report={'schema':'NF652-metadata-rechunk-v1','keys':len(keys),'rows':sum(n for h,f,n in keys),
            'source_shards_checked':8,'parts':len(parts),'last_part':sizes[-1],
            'ordered_shapes_preserved':True,'files':{p.name:sha(p.read_bytes()) for p in (v,g)},
            'scope':'retained metadata shape and source shard reconciliation; no Lean execution'}
    (a.output/'nf652-rechunk-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
