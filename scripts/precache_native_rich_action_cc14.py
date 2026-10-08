"""Parallel exact source construction for the fixed CC14 trial batch."""
import json,gzip,hashlib,os
from concurrent.futures import ProcessPoolExecutor
from certify_native_rich_action_cc14 import ROOT,F,I,D,shifted_legendre,sqrt_rational,mid,fast_source,bracket,original_source_function_sha256
def worker(n):
 P=shifted_legendre(n)[n];nz=mid(sqrt_rational(F(2*n+1)/D));p=[nz*x for x in P]
 m0=abs(nz);m1=m0*n*(n+1);i=(n-112)//2+2
 bind=hashlib.sha256(json.dumps([original_source_function_sha256,hashlib.sha256((ROOT/'scripts/native_rich_action_fast_source_cc14.py').read_bytes()).hexdigest(),list(map(str,p)),str(m0),str(m1),str(I.grid)]).encode()).hexdigest()
 cache=ROOT/'notes/data'/f'RPB108_RICH_ACTION_CC14_SOURCE_CACHE_{i}.json.gz'
 if cache.exists():
  assert json.loads(gzip.decompress(cache.read_bytes()))['binding']==bind
  return {'degree':n,'already_complete':True}
 r,e,pi,geom=fast_source(p,m0,m1)
 value={'binding':bind,'regular_polynomials':[[str(x) for x in row] for row in r],'source_error':str(e),'pi':bracket(pi),'cuts':[bracket(x) for x in geom['cuts']],'active':geom['active']}
 temp=cache.with_suffix(f'.tmp{os.getpid()}');temp.write_bytes(gzip.compress(json.dumps(value).encode(),mtime=0));temp.replace(cache)
 return {'degree':n,'fresh_complete':True}
if __name__=='__main__':
 with ProcessPoolExecutor(max_workers=4) as pool:
  for result in pool.map(worker,range(112,144,2)):print(json.dumps(result),flush=True)
