#!/usr/bin/env python3
"""Persist exact source outputs and expensive, authenticated source profiles."""
from pathlib import Path
import argparse,json,gzip,base64,hashlib
def save(path,b):
 Path(path).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n');print(path,hashlib.sha256(b).hexdigest(),flush=True)
def run(profiles_only=False):
 for label in ['PRIMARY','REPLAY']:
  prefix=f'notes/data/RPB108_CC119_EVEN_SOURCE_{label}_20261010.json';directory=Path(prefix+'.profiles');files=[directory/f'{i}.json' for i in range(14)];raw=[json.loads(p.read_text()) for p in files];identity=raw[0]['identity'];assert all(p['identity']==identity for p in raw)
  packet=json.loads(Path('notes/data/RPB108_CC119_EVEN_PHYSICAL_PACKET_20261010.json').read_text())
  for i,x in enumerate(raw):assert x['column_sha256']==hashlib.sha256(json.dumps(packet['columns'][i],sort_keys=True).encode()).hexdigest()
  out=dict(milestone='CC119',run=label,identity=identity,profiles=raw,profile_stored_sha256=[hashlib.sha256(p.read_bytes()).hexdigest() for p in files]);save(f'notes/data/RPB108_CC119_EVEN_{label}_PROFILES_20261010.json.gz.b64',(json.dumps(out,separators=(',',':'))+'\n').encode())
  if not profiles_only:save(prefix+'.gz.b64',Path(prefix).read_bytes())
 if not profiles_only:
  for label in ['', '_REPLAY']:
   path=Path(f'notes/data/RPB108_CC119_JOINT_EVEN_RESPONSE{label}_20261010.json')
   if path.exists():save(str(path)+'.gz.b64',path.read_bytes())
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--profiles-only',action='store_true');run(a.parse_args().profiles_only)
