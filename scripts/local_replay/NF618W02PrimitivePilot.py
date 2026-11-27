#!/usr/bin/env python3
"""External directed fixed-point pilot; no new native admissions."""
import hashlib,json,re,sys,zipfile
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from time import perf_counter
sys.set_int_max_str_digits(0)
Q=10**2600; N=1200; M=2000
Z=(0,0); O=(Q,0); CZ=(Z,Z); CO=(O,Z)
def ceil(a,b): assert b>0; return -((-a)//b)
def exact(a):
 a=F(a); m,r=divmod(a.numerator*Q,a.denominator); return m,int(bool(r))
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[0],a[1]
def mul(a,b):
 m,r=a;n,s=b;return m*n//Q,ceil(abs(m)*s+abs(n)*r+r*s,Q)+1
def div(a,k): return a[0]//k,ceil(a[1],k)+1
def za(a,b): return add(a[0],b[0]),add(a[1],b[1])
def zn(a): return neg(a[0]),neg(a[1])
def zm(a,b): return add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))
def real(a): return exact(a),Z
def cj(a): return a[0],neg(a[1])
def upper(a): return abs(a[0])+a[1]
def inv(a):
 m,r=a;assert m-r>0;L=Q*Q//(m+r);U=ceil(Q*Q,m-r);c=(L+U)//2;return c,max(U-c,c-L)
def zi(a):
 d=add(mul(a[0],a[0]),mul(a[1],a[1]));b=inv(d);return mul(a[0],b),mul(neg(a[1]),b)
def atan(p):
 s=Z;power=p
 for n in range(M): s=add(s,exact(F((-1)**n,power*(2*n+1))));power*=p*p
 assert Q<=power*(2*M+1);return s[0],s[1]+1
assert 2*Q<=factorial(N)
pi=add(mul(exact(16),atan(5)),neg(mul(exact(4),atan(239))))
def small(z):
 assert sum(map(upper,z))<=Q;s=CZ;t=CO
 for n in range(N):
  s=za(s,t)
  if n+1<N: t=tuple(div(a,n+1) for a in zm(t,z))
 return tuple((m,r+1) for m,r in s)
root=small((Z,mul(pi,exact(F(1,640)))));powers=[CO,root]
for k in range(2,161):powers.append(zm(powers[-1],root))
def phase(p):
 p%=1280;j=(p+160)//320;r=p-320*j;v=powers[abs(r)]
 if r<0:v=cj(v)
 for _ in range(j%4):v=neg(v[1]),v[0]
 return v
E=small(real(F(11,20)))[0];Ei=inv(E);amps={-2:mul(Ei,Ei),-1:Ei,0:O,1:E,2:mul(E,E)}
def endpoint(h,f):
 H=2*h;p=1408*f;assert H.denominator==p.denominator==1;return zm((amps[int(H)],Z),phase(int(p)))
def direct_endpoint(h,f):
 u=f*F(11,10);u-=(u+F(1,2))//1
 a=small((Z,mul(pi,exact(u/2))));a=zm(a,a);a=zm(a,a)
 b=small(real(h*F(11,20)));return zm(a,zm(b,b))
def exponent(h,f):return exact(h),mul(pi,exact(2*f))
def primitive(n,x,recip):
 # Horner form in 1/z: sum_j (-1)^j n!/(n-j)! x^(n-j) / z^(j+1)
 p=CZ
 for j in range(n,-1,-1):
  c=(-1)**j*factorial(n)//factorial(n-j);p=zm(za(p,real(c*x**(n-j))),recip)
 return p
def direct(h,f,k):
 if h==f==0:return [real(F(0) if n%2 else 2*F(11,10)**(n+1)/(n+1)) for n in range(k+1)]
 u=zi(exponent(h,f));a=endpoint(h,f);b=endpoint(-h,-f);B=F(11,10)
 return [za(zm(a,primitive(n,B,u)),zn(zm(b,primitive(n,-B,u)))) for n in range(k+1)]
def recurrence(h,f,k):
 if h==f==0:return direct(h,f,k)
 u=zi(exponent(h,f));a=direct_endpoint(h,f);b=direct_endpoint(-h,-f);B=F(11,10);prev=CZ;out=[]
 for n in range(k+1):
  bd=za(zm(real(B**n),a),zn(zm(real((-B)**n),b)));prev=zm(za(bd,zn(zm(real(n),prev))),u);out.append(prev)
 return out
def overlap(a,b):return all(abs(x[0]-y[0])<=x[1]+y[1] for x,y in zip(a,b))
def radius_exp(v):return max((len(str(r))-2600 for _,r in v if r),default=None)
def verify_zip(p,d):
 b=Path(p).read_bytes();assert hashlib.sha256(b).hexdigest()==d;z=zipfile.ZipFile(p);assert z.testzip() is None;return z
def main():
 s=verify_zip(sys.argv[1],'72b366246a55f5e2bc4defca1441623075dc651d7b6c20d718ae97b0c27fdba3');e=verify_zip(sys.argv[2],'18bc48a722598212a9fe1090bc728efa5e15baf06985c1499efe637f7b1c88ce')
 manifest=s.read('manifest.json');assert manifest==e.read('nf618-session/Batch24/source/manifest.json');m=json.loads(manifest)
 phase_checks=[]
 for p in m['phases']:
  f=F(p['phase']);k=f*1280;assert k.denominator==1
  txt=s.read(p['module']+'.lean').decode();line=next(x for x in txt.splitlines() if re.match(r'def \S+Value : NF591Rect :=',x));v=list(map(int,re.findall(r'\((-?\d+):ℚ\)/neutralNF616Q',line)));assert len(v)==4
  old=(tuple(v[:2]),tuple(v[2:]));new=phase(int(k));assert overlap(old,new);phase_checks.append(p['module'])
 tables=m['tables'];assert len(tables)==111 and sum(t['rows'] for t in tables)==584
 # Select smallest/largest f, largest degree, both mixed signs, and first slot of each of 16 phase leaves as represented by the source table metadata.
 picked={}
 for sign in ['-1/2','0','1/2']:
  ts=[t for t in tables if t['key'][0]==sign]
  for t in [min(ts,key=lambda t:F(t['key'][1])),max(ts,key=lambda t:F(t['key'][1])),max(ts,key=lambda t:t['rows'])]:picked[t['slot']]=t
 for t in tables:
  # Additional first table for every distinct phase class.
  p=abs((F(t['key'][1])*F(11,10)+F(1,2))%1-F(1,2))
  if not any(abs((F(x['key'][1])*F(11,10)+F(1,2))%1-F(1,2))==p for x in picked.values()):picked[t['slot']]=t
 cases=[(t['slot'],F(t['key'][0]),F(t['key'][1]),t['rows']-1) for t in sorted(picked.values(),key=lambda t:t['slot'])]
 # Historical NF620 named sample keys (not claimed to have literal archive rows here).
 cases += [('NF620-degree26',F(0),F(37,32),26),('NF620-mixed13',F(1,2),F(37,64),13),('NF620-small-frequency',F(0),F(7,704),3),('zero-polynomial',F(0),F(0),26)]
 results=[]
 for slot,h,f,k in cases:
  t=perf_counter();a=direct(h,f,k);td=perf_counter()-t;t=perf_counter();b=recurrence(h,f,k);tr=perf_counter()-t
  assert all(overlap(x,y) for x,y in zip(a,b)),slot
  def mx(v):return max((p for x in v if (p:=radius_exp(x)) is not None),default=None)
  results.append(dict(slot=slot,h=str(h),f=str(f),rows=k+1,direct_radius_exponent=mx(a),recurrence_radius_exponent=mx(b),direct_seconds=round(td,4),recurrence_seconds=round(tr,4)))
 print(json.dumps(dict(manifest_sha256=hashlib.sha256(manifest).hexdigest(),source_phase_overlap=phase_checks,archive_tables=len(tables),archive_rows=584,sample_tables=len(results),sample_rows=sum(t['rows'] for t in results),cases=results),indent=2))
if __name__=='__main__':main()
