#!/usr/bin/env python3
"""Lossless deterministic packing of primary/replay original source archives."""
from pathlib import Path
import argparse,base64,gzip,hashlib,json

def run(paths):
 for path,order,suffix in zip(paths,(360,400),('','_REPLAY')):
  b=Path(path).read_bytes();d=json.loads(b);assert d['stage']=='DNE48' and d['regular_order']==order and d['columns']==list(range(47))
  packed=base64.b64encode(gzip.compress(b,mtime=0))+b'\n';assert gzip.decompress(base64.b64decode(packed))==b
  target=Path(f'notes/data/RPB108_DNE48_TRIAL_SOURCE{suffix}_20261010.json.gz.b64');target.write_bytes(packed);print(target,'decoded sha256',hashlib.sha256(b).hexdigest(),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('inputs',nargs=2);run(ap.parse_args().inputs)
