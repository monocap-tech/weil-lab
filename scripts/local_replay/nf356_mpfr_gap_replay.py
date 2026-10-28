#!/usr/bin/env python3
"""Independent local directed-rounding MPFR replay of Weil-Lab #356 gap gate.

No python-flint, Arb, or mpmath.iv. Mathematical model:
  Re psi(1/4+i*pi*x) = Re psi(A+i*pi*x) - sum_{k<N} a_k/(a_k²+pi²x²)
  Re psi(A+iy) >= .5 log(A²+y²) - A/(2(A²+y²)) - 1/(2A)
for A=N+1/4. The final allowance dominates |Binet remainder|<=1/(12*A²).

All transcendental operations use MPFR directed rounding on intervals.
Upper bound of cos over a tiny argument interval is conservatively computed
using its 1-Lipschitz property; this remains rigorous across extrema.

The complete local gap scan covers [0,1300] outside retained #350
clusters using |m''|<2145. The >1300 tail and old-cover calculation
are separate inputs. This script makes no repository acceptance claim.
"""
import ctypes, hashlib, json, zipfile, sys, time
from ctypes import c_long,c_int,c_void_p,c_char_p,c_double,Structure,byref
from fractions import Fraction as F
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))

lib=ctypes.CDLL('libmpfr.so.6')
class rawmp(Structure):
    _fields_=[('_mpfr_prec',c_long),('_mpfr_sign',c_int),('_mpfr_exp',c_long),('_mpfr_d',c_void_p)]
RNDN=0; RNDU=2; RNDD=3; PREC=192
lib.mpfr_init2.argtypes=[ctypes.POINTER(rawmp),c_long]
lib.mpfr_clear.argtypes=[ctypes.POINTER(rawmp)]
lib.mpfr_set_str.argtypes=[ctypes.POINTER(rawmp),c_char_p,c_int,c_int]; lib.mpfr_set_str.restype=c_int
lib.mpfr_set.argtypes=[ctypes.POINTER(rawmp),ctypes.POINTER(rawmp),c_int]
lib.mpfr_const_pi.argtypes=[ctypes.POINTER(rawmp),c_int]
lib.mpfr_get_d.argtypes=[ctypes.POINTER(rawmp),c_int];lib.mpfr_get_d.restype=c_double
lib.mpfr_cmp.argtypes=[ctypes.POINTER(rawmp),ctypes.POINTER(rawmp)];lib.mpfr_cmp.restype=c_int
for k in ('add','sub','mul','div'):
    getattr(lib,'mpfr_'+k).argtypes=[ctypes.POINTER(rawmp)]*3+[c_int]
for k in ('log','sqrt','cos'):
    getattr(lib,'mpfr_'+k).argtypes=[ctypes.POINTER(rawmp)]*2+[c_int]

class N:
    __slots__=('v',)
    def __init__(self, s=None, rnd=RNDN):
        self.v=rawmp();lib.mpfr_init2(byref(self.v),PREC)
        if s is not None:
            r=lib.mpfr_set_str(byref(self.v),str(s).encode(),10,rnd)
            assert r==0 or r in (-1,1), (s,r)
    def __del__(self):
        if hasattr(self,'v'):lib.mpfr_clear(byref(self.v))
    def num(self,rnd=RNDN):return lib.mpfr_get_d(byref(self.v),rnd)
    @classmethod
    def one(cls):return cls(1)

def binop(a,b,k,rnd):
    o=N();getattr(lib,'mpfr_'+k)(byref(o.v),byref(a.v),byref(b.v),rnd);return o

def unary(a,k,rnd):
    o=N();getattr(lib,'mpfr_'+k)(byref(o.v),byref(a.v),rnd);return o

def cmp_mpfr(a,b):return lib.mpfr_cmp(byref(a.v),byref(b.v))
def exact_min(xs):
    ans=xs[0]
    for x in xs[1:]:
        if cmp_mpfr(x,ans)<0:ans=x
    return ans
def exact_max(xs):
    ans=xs[0]
    for x in xs[1:]:
        if cmp_mpfr(x,ans)>0:ans=x
    return ans

def fracn(x,rnd):
    assert isinstance(x,F)
    num=N(x.numerator,rnd)
    if x.denominator==1:return num
    den=N(x.denominator)
    return binop(num,den,'div',rnd)

class I:
    __slots__=('l','u')
    def __init__(self,l,u):self.l=l;self.u=u
    @staticmethod
    def f(x):
        if not isinstance(x,F):x=F(x)
        return I(fracn(x,RNDD),fracn(x,RNDU))
    @staticmethod
    def pi():
        lo=N();hi=N();lib.mpfr_const_pi(byref(lo.v),RNDD);lib.mpfr_const_pi(byref(hi.v),RNDU)
        return I(lo,hi)
    def __add__(self,o):
        if not isinstance(o,I):o=I.f(o)
        return I(binop(self.l,o.l,'add',RNDD),binop(self.u,o.u,'add',RNDU))
    __radd__=__add__
    def __sub__(self,o):
        if not isinstance(o,I):o=I.f(o)
        return I(binop(self.l,o.u,'sub',RNDD),binop(self.u,o.l,'sub',RNDU))
    def __rsub__(self,o):return I.f(o)-self
    def __mul__(self,o):
        if not isinstance(o,I):o=I.f(o)
        candidates_lo=[binop(a,b,'mul',RNDD) for a in (self.l,self.u) for b in (o.l,o.u)]
        candidates_hi=[binop(a,b,'mul',RNDU) for a in (self.l,self.u) for b in (o.l,o.u)]
        return I(exact_min(candidates_lo),exact_max(candidates_hi))
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,I):o=I.f(o)
        assert o.l.num(RNDD)>0, 'only positive denominators used'
        recip=I(binop(N(1),o.u,'div',RNDD),binop(N(1),o.l,'div',RNDU))
        return self*recip
    def __neg__(self):return I(binop(N(0),self.u,'sub',RNDD),binop(N(0),self.l,'sub',RNDU))
    def log(self):
        assert self.l.num(RNDD)>0
        return I(unary(self.l,'log',RNDD),unary(self.u,'log',RNDU))
    def sqrt(self):
        assert self.l.num(RNDD)>=0
        return I(unary(self.l,'sqrt',RNDD),unary(self.u,'sqrt',RNDU))
    def cos(self):
        # Lipschitz bound: cos(y) lies within [cos(x_l)-|u-l|,cos(x_l)+|u-l|]
        width=binop(self.u,self.l,'sub',RNDU)
        return I(binop(unary(self.l,'cos',RNDD),width,'sub',RNDD),
                 binop(unary(self.l,'cos',RNDU),width,'add',RNDU))
    def down(self):return F.from_float(self.l.num(RNDD))
    def up(self):return F.from_float(self.u.num(RNDU))

def main():
    t=time.monotonic()
    zip_path=str(CUSTODY_ROOT / 'pr350-certificate.zip');arc=Path(zip_path).read_bytes()
    assert hashlib.sha256(arc).hexdigest()=='3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09'
    with zipfile.ZipFile(zip_path) as z:raw=z.read('original_BS_pruned_rank_bound.json')
    assert hashlib.sha256(raw).hexdigest()=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
    data=json.loads(raw);clusters=data['cluster_witnesses']
    assert len(clusters)==107
    gaps=[(F(a['hi']),F(b['lo'])) for a,b in zip(clusters,clusters[1:])]
    gaps.append((F(clusters[-1]['hi']),F(1300)))
    assert len(gaps)==107 and all(a<b for a,b in gaps)

    PI=I.pi();A=I.f(F(65,4));TAU=I.f(F(1,2))*A
    LC=PI.log()+I.f(F(1,2))/A
    coefphase=[(I.f(2)*I.f(p).log()/I.f(n).sqrt(), I.f(2)*PI*I.f(n).log()) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]]
    # IMPORTANT: a_k=1/4+k as exact fractions, not binary floating.
    ak=[I.f(F(4*k+1,4)) for k in range(16)]
    ak2=[a*a for a in ak]
    Asq=A*A
    values={}
    def lower(q):
        if q in values:return values[q]
        X=I.f(q);Y=PI*X;Y2=Y*Y;Z=Asq+Y2
        V=Z.log()*I.f(F(1,2))-A/(I.f(2)*Z)-LC
        for a,a2 in zip(ak,ak2):V=V-a/(a2+Y2)
        for coef,phase in coefphase:V=V-coef*(phase*X).cos()
        ans=V.down();values[q]=ans
        return ans
    accepted=[]; stack=[(l,r,0,k) for k,(l,r) in enumerate(gaps)];minbound=None;worst=None;maxdepth=0
    H=F(2145);L=F(1,100)
    while stack:
        l,r,d,k=stack.pop()
        assert d<33,(l,r,k)
        bd=min(lower(l),lower(r))-H*(r-l)**2/8
        if bd>L:
            accepted.append((k,l,r,d,bd));maxdepth=max(maxdepth,d)
            if minbound is None or bd<minbound:minbound=bd;worst=(k,l,r,d)
        else:
            x=(l+r)/2;stack.append((x,r,d+1,k));stack.append((l,x,d+1,k))
    by_gap=[[] for _ in gaps]
    for k,l,r,d,bd in accepted:by_gap[k].append((l,r))
    for i,(a,b) in enumerate(gaps):
        rows=sorted(by_gap[i]);assert rows and rows[0][0]==a and rows[-1][1]==b
        assert all(x[1]==y[0] for x,y in zip(rows,rows[1:]))
    print('MPFR independent GAP PASS, lower=',float(minbound),'segment count',len(accepted),'unique endpoints',len(values),'max depth',maxdepth,'seconds',time.monotonic()-t)
    out={'status':'LOCAL_MPFR_DIRECTED_REPLAY_PASS','precision_bits':PREC,
       'backend':'ctypes libmpfr.so.6, no mpmath.iv or Arb','original_input_archive_sha256':hashlib.sha256(arc).hexdigest(),
       'gaps':len(gaps),'segments':len(accepted),'endpoints':len(values),'max_depth':maxdepth,
       'threshold':'1/100','lower_exact_float_fraction':str(minbound),'lower_approx':float(minbound),
       'worst_gap':worst[0], 'worst_interval':[str(worst[1]),str(worst[2])],
       'binet_remainder_proof':'|R(A+i*pi*x)|<=1/(12*A*A) <=1/(2*A); A=65/4',
       'original_W_odd_negative':'OPEN','native_arb_replay_done':False,'github_verified':False}
    out_path=Path(str(CUSTODY_ROOT / 'nf356_mpfr_gap_replay_report.json'));out_path.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
