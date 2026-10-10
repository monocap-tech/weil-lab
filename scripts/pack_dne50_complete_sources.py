#!/usr/bin/env python3
"""Lossless deterministic packing of complete source primary/replay archives."""
from pathlib import Path
import argparse,json,gzip,base64,hashlib

def run():
 a=argparse.ArgumentParser();a.add_argument('--raw-dir',default='/tmp');args=a.parse_args()
 for par in ('even','odd'):
  for N in (360,400):
   p=Path(args.raw_dir)/f'dne50_{par}_{N}.json';b=p.read_bytes();d=json.loads(b);assert d['stage']=='DNE50' and d['parity']==par and d['regular_order']==N and len(d['columns'])==({'even':59,'odd':56}[par]);suffix='_REPLAY' if N==400 else '';out=Path(f'notes/data/RPB108_DNE50_{par.upper()}_COMPLETE_SOURCE{suffix}_20261010.json.gz.b64');out.write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n');print(out,len(b),hashlib.sha256(b).hexdigest(),flush=True)
if __name__=='__main__':run()
