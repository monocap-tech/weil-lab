"""V10B31: replay the authenticated V10B19 generator with reflected moments.
Usage: python v10b31_reflected_replay.py ORIGINAL_GENERATOR FROZEN_JSON OUTPUT_DIR
No changes to trial data, constants, pole load, action coefficients or LDL.
The original script is required because it is held in the V10B19 archive.
"""
import hashlib, subprocess, sys
from pathlib import Path
src, frozen, out=map(Path,sys.argv[1:])
assert hashlib.sha256(src.read_bytes()).hexdigest()=="18dd4d727007ce8ccb3f45643c41273a1441c521c29d384ff0a0c4dea0e9cb01"
assert hashlib.sha256(frozen.read_bytes()).hexdigest()=="bccbd53fd2e02cb887868f588ef7f8765e780086f7fabe748518d5685d7c7616"
old="mom=[[Q(1,j),-Q(1,j*j)-harm[j]/j, Q(2,j**3)+(harm[j]**2+h2[j])/j+2*(harm[j]/j**2-(zeta-h2[j])/j)] for j in range(1,K+1)]"
new="""mom=[]
for j in range(1,K+1):
 k=j-1
 a=sum((Q((-1)**i*comb(k,i),(i+1)**2) for i in range(j)),Q(0))
 b=sum((Q(2*(-1)**i*comb(k,i),(i+1)**3) for i in range(j)),Q(0))
 assert a==harm[j]/j and b==(harm[j]**2+h2[j])/j
 mom.append([Q(1,j),-Q(1,j*j)-a,Q(2,j**3)+b+2*(harm[j]/j**2-(zeta-h2[j])/j)])
print('REFLECTED_MOMENT_EXACT',K,2*K,flush=True)"""
s=src.read_text()
assert s.count(old)==1
out.mkdir(parents=True,exist_ok=True)
p=out/"reflected_replay.py"
p.write_text(s.replace(old,new))
assert hashlib.sha256(p.read_bytes()).hexdigest()=="49edda13e81a945f9c7bd47b87fb2a8f0d15356351ba901983a4d93a28255ddf"
subprocess.run([sys.executable,str(p),str(frozen.resolve())],check=True)
assert hashlib.sha256((out/"exact_result.json").read_bytes()).hexdigest()=="afb474cb569b08dff1782e5a19430b0436a3a77bfcb7b2211547017e7a460903"
print("V10B31 reflected full replay: identical V10B19 exact result SHA256 PASS")
