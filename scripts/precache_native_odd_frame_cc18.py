"""Reconstruct the fixed55 retained +16 complementary original odd sources."""
import json,gzip,hashlib,os,time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from native_odd_frame_source_cc18 import frame_source,frame_error,I,F,D,original,mid,sqrt_rational
from native_rich_action_source_error_cc14 import constant_radius
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'notes/data';DEGREES=list(range(3,144,2))
I.grid=10**400

def binding(n):
 return {'degree':n,'source_factory_sha256':hashlib.sha256((ROOT/'scripts/native_odd_frame_source_cc18.py').read_bytes()).hexdigest(),'odd_factory_sha256':hashlib.sha256((ROOT/'scripts/native_terminal_odd_source_cc17.py').read_bytes()).hexdigest(),'base_source_sha256':hashlib.sha256((ROOT/'scripts/certify_native_coupled_trial_cc3.py').read_bytes()).hexdigest(),'interval_grid_digits':400,'coefficient_grid_digits':150}

def worker(n):
 start=time.monotonic();I.grid=10**400;path=BASE/f'RPB108_ODD_FRAME_CC18_SOURCE_CACHE_{n}.json.gz';bind=binding(n)
 if path.exists():
  s=json.loads(gzip.decompress(path.read_bytes()));assert s['binding']==bind
  return {'degree':n,'already_complete':True}
 nz=mid(sqrt_rational(F(2*n+1)/D));p=[nz*x for x in original.shifted_legendre(n)[n]];M0=nz;M1=nz*n*(n+1)
 regs,unfactored,pi,geom=frame_source(p,M0,M1)
 error=frame_error(p,M0,M1,regs,constant_radius(pi))
 # Target is the EXACT physically normalized Legendre source. This pays
 # the midpoint normalization separately from all analytic/decimal errors.
 norm=sqrt_rational(F(2*n+1)/D);error+=F(10**8)*(1+M0)*(norm.hi-norm.lo)/(2*nz)
 value={'binding':bind,'degree':n,'polynomial':list(map(str,p)),'M0':str(M0),'M1':str(M1),'regular_polynomials':[[str(x) for x in row] for row in regs],'source_error':str(error),'unfactored_error':str(unfactored),'pi':[str(pi.lo),str(pi.hi)],'cuts':[[str(x.lo),str(x.hi)] for x in geom['cuts']],'active':geom['active']}
 temporary=path.with_suffix(f'.tmp{os.getpid()}');temporary.write_bytes(gzip.compress(json.dumps(value).encode(),mtime=0));temporary.replace(path)
 return {'degree':n,'fresh_complete':True,'seconds':round(time.monotonic()-start,2)}

if __name__=='__main__':
 with ProcessPoolExecutor(max_workers=4) as pool:
  for result in pool.map(worker,DEGREES):print(json.dumps(result),flush=True)
