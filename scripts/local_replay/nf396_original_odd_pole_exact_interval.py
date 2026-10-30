#!/usr/bin/env python3
"""NF396 source-pinned *rigorous* exact rational odd pole-correction intervals.

On original unchanged B=11/10, 32 sine frequencies 5n/11 and true sinh pole,
the pole pairing is closed form. Original j387 contains only the first
selected sin and x²sin. This pays rational Machin-pi, Taylor-tail and interval
errors without Arb/FFT/J242 Gram reconstruction. It is NOT original signed
Wodd(u4,j), lowband upper, full inverse, positivity, or RH.
"""
import argparse, hashlib, json, math, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)

SOURCE_GIT='d87cf3cb9972bed42db4c54e89a05d742499d2d0'
SELECTED_GIT='d705ae312be5324bff64f3a9540e30e8b8bd34dc'
ORIGINAL_SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
B=F(11,10)
A=F(1,2)
C=F(37,64)
ALPHA=F(-88873,2**48)
T=[F(n,2**20) for n in (-2271087,-1621433,1115405,1048576)]

def read(path,expected):
    buf=Path(path).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(buf)).encode()+b'\x00'+buf).hexdigest()==expected
    return json.loads(buf)

class IV:
    def __init__(self,lo,hi=None):
        self.lo=F(lo)
        self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,other):
        x=iv(other)
        return IV(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,x): return self+-iv(x)
    def __rsub__(self,x): return iv(x)+-self
    def __mul__(self,other):
        x=iv(other)
        v=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return IV(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,other):
        x=iv(other)
        assert x.lo*x.hi>0
        return self*IV(F(1,x.hi),F(1,x.lo))
    def __rtruediv__(self,other): return iv(other)/self
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        if k==0:return IV(1)
        if k%2==0:
            if self.lo<=0<=self.hi:
                return IV(0,max(abs(self.lo),abs(self.hi))**k)
            return IV(min(self.lo**k,self.hi**k),max(self.lo**k,self.hi**k))
        return IV(self.lo**k,self.hi**k)
    def assert_inside(self,lo,hi):
        assert F(lo)<self.lo<=self.hi<F(hi),'rigorous interval does not meet claimed bound'
    def approx(self):
        return [float(self.lo),float(self.hi)]
def iv(x):return x if isinstance(x,IV) else IV(x)

def pi_bound(N=60):
    # Machin: pi=16 atan(1/5)-4 atan(1/239).
    # Alternating arctan series; exactly pay first omitted term.
    assert N>0 and N%2==0
    def atan_inv(d):
        x=F(1,d)
        s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
        omitted=x**(2*N+1)/F(2*N+1)
        return IV(s,s+omitted)
    return 16*atan_inv(5)-4*atan_inv(239)

def taylor_interval(x,kind,N=40):
    # True sin/cos/sinh/cosh enclosed via a signed rational partial sum
    # and twice the next term: all omitted ratios <1/2 for |x|<5,N>=40.
    x=iv(x)
    w=max(abs(x.lo),abs(x.hi))
    assert N>=40 and w<5
    b=1 if kind in ('sin','sinh') else 0
    total=IV(0)
    for k in range(N):
        exponent=2*k+b
        sign=(-1)**k if kind in ('sin','cos') else 1
        total+=sign*x**exponent/F(math.factorial(exponent))
    first=2*N+b
    err=2*w**first/F(math.factorial(first))
    return total+IV(-err,err)

def produce(source_path,jpath,output=None):
    source=read(source_path,SOURCE_GIT)
    selected=read(jpath,SELECTED_GIT)
    obj=source['data']
    assert source['custody'] and len(obj['target_sine_frequencies'])==32
    assert [F(x) for x in obj['target_sine_frequencies']]==[F(5*n,11) for n in range(1,33)]
    assert len(obj['target_probes'])==4
    assert selected['original_rank_sha256']==RANK_SHA
    assert selected['original_nf375_source_sha256']==ORIGINAL_SOURCE_SHA
    assert selected['scalar_alpha']==str(ALPHA)
    assert selected['nonzero_raw_source_indices']==[0,2]
    assert selected['coefficients_dyadic_denominator_power']==48
    assert selected['endpoint_value_exact']=='0'
    assert selected['W_ODD_NEG']==selected['RH']=='OPEN'
    g=[]
    for n in range(33):
        val=sum((T[k]*F(obj['target_probes'][k]['sine_coefficients'][n]
                        if n<32 else obj['target_probes'][k]['sinh_coefficient'])
                 for k in range(4)),F(0))
        g.append(val)
    # The 32 source frequencies satisfy omega_n*B=n*pi EXACTLY.
    # Hence integral_{-B}^B sin(omega_n x)sinh(x/2) dx
    # = (-1)^(n+1) 2*omega_n*sinh(B/2)/(omega_n²+1/4).
    PI=pi_bound()
    PI.assert_inside(F(314159265358979323846264338327950288419716939937510,10**50),
                     F(314159265358979323846264338327950288419716939937512,10**50))
    S=taylor_interval(IV(B*A),'sinh')
    SB=taylor_interval(IV(B),'sinh')
    CH=taylor_interval(IV(B*A),'cosh')
    original_FT_pole=IV(0)
    for n,v in enumerate(g[:32],1):
        omega=2*PI*F(5*n,11)
        scalar=(-1)**(n+1)*2*omega*S/(omega**2+A*A)
        original_FT_pole+=v*scalar
    original_FT_pole+=g[32]*(SB-B)
    # I(w)=int_-B^B sin(w*x)sinh(x/2)dx=2U/(a²+w²).
    # Since I''(w)=-int x²sin(w*x)sinh(x/2)dx,
    # <j387,s>=alpha*(121*I+100*I'').
    w=2*PI*C
    x=w*B
    D=A*A+w**2
    sinx=taylor_interval(x,'sin')
    cosx=taylor_interval(x,'cos')
    U=A*CH*sinx-w*S*cosx
    U1=(A*B*CH-S)*cosx+w*B*S*sinx
    U2=(-A*B*B*CH+2*B*S)*sinx+w*B*B*S*cosx
    I=2*U/D
    I2=2*(U2/D-4*w*U1/(D**2)-2*U/(D**2)+8*w**2*U/(D**3))
    selected_pole=ALPHA*(121*I+100*I2)
    correction=2*original_FT_pole*selected_pole
    original_FT_pole.assert_inside(F(723,1000),F(725,1000))
    selected_pole.assert_inside(F(-65,10**10),F(-64,10**10))
    correction.assert_inside(F(-95,10**10),F(-92,10**10))
    # The conservative accepted candidate-stop scale was <1.31e-20.
    # Magnitude of the mandatory pole correction exceeds 7e11 times that
    # scale, but this DOES NOT bound Wodd or prove failure.
    assert F(92,10**10)>7*10**11*F(131,10**22)
    result={
       'standing':'NF396 SOURCE-PINNED RIGOROUS ORIGINAL SELECTED ODD POLE CORRECTION; COMPLETE SIGNED MOMENT OPEN',
       'original_pr355_source_git_blob_sha1':SOURCE_GIT,
       'original_selected_j387_git_blob_sha1':SELECTED_GIT,
       'original_rank_sha256':RANK_SHA,
       'original_source_sha256':ORIGINAL_SOURCE_SHA,
       'original_selected_rank':242,
       'original_source_fourth_T_exact_numerators':[-2271087,-1621433,1115405,1048576],
       'source_T_denominator_power':20,
       'original_32_sine_pole_overlaps_used_exact_endpoint_phase':True,
       'original_sinh_pole_norm_identity':'<s,s>=sinh(B)-B',
       'original_j387_pole_identity':'alpha*(121*I(w)+100*I_second_derivative(w)), w=2*pi*37/64',
       'pi_proof':'Machin exact alternating arctan 60 terms + omitted term bound',
       'trig_hyperbolic_proof':'40 terms rational interval Taylor, each tail bounded by twice first omitted term for |argument|<5',
       'original_FTe4_pole_overlap_lower':'723/1000',
       'original_FTe4_pole_overlap_upper':'725/1000',
       'original_j387_pole_overlap_lower':'-65/10000000000',
       'original_j387_pole_overlap_upper':'-64/10000000000',
       'original_complete_pole_correction_lower':'-95/10000000000',
       'original_complete_pole_correction_upper':'-92/10000000000',
       'original_FTe4_pole_overlap_diagnostic_approx':original_FT_pole.approx(),
       'original_j387_pole_overlap_diagnostic_approx':selected_pole.approx(),
       'original_pole_correction_diagnostic_approx':correction.approx(),
       'lower_bound_pole_correction_magnitude_more_than_7e11_times_1p31e_minus20':True,
       'original_Wodd_u4_j387_signed_selected_remainder_measured':False,
       'original_full_multiplier_selected_moment_measured':False,
       'original_j387_candidate_method_verdict':'UNDECIDED',
       'original_lowband_upper_computed':False,
       'whole_original_exterior_inverse_computed':False,
       'original_operator_domain':'OPEN',
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    if output:
        p=Path(output)
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(result,indent=2)+'\n')
    print('NF396 original source four-source pole overlap:',original_FT_pole.approx())
    print('NF396 original j387 selected pole overlap:',selected_pole.approx())
    print('NF396 original pole correction:',correction.approx())
    print('NF396 all strict exact rational interval checks PASS; Wodd, j387 verdict, RH OPEN')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--source',required=True)
    p.add_argument('--j387',required=True)
    p.add_argument('--output')
    args=p.parse_args()
    produce(args.source,args.j387,args.output)
