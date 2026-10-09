#!/usr/bin/env python3
"""Frozen rational coherent majorant, complete signed interval LDL payment."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json
SHA=['0cb636cdf03ad09f57cfce6d4bc67d0b7094dc1c154597cb0d1fe467590a2fd6','ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788','316ea81720e0992699ee8a37c5cc48b1170d811ef6d88bbdf19d46d03860c7a9','96a4f1448b0aa0d347ce79345e222d260c70af22cc86e7cd998626883e6fdb90','4004a41e1ff792ea667719ba889d5908b3098581fd0dfbf437e96fe0c6cf9f93']
def read(p):
    b=Path(p).read_bytes(); return json.loads(b),hashlib.sha256(b).hexdigest()
class Interval:
    digits=80
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi); assert self.lo<=self.hi
    def box(self):return [str(self.lo),str(self.hi)]
    @classmethod
    def rounded(cls,lo,hi):
        s=10**cls.digits; return cls(F((lo*s).__floor__(),s),F((hi*s).__ceil__(),s))
    def __add__(a,b):
        if not isinstance(b,Interval):b=Interval(b)
        return Interval.rounded(a.lo+b.lo,a.hi+b.hi)
    def __neg__(a):return Interval(-a.hi,-a.lo)
    def __sub__(a,b):return a+-b if isinstance(b,Interval) else a+(-F(b))
    def __mul__(a,b):
        if not isinstance(b,Interval):b=Interval(b)
        vals=[x*y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return Interval.rounded(min(vals),max(vals))
    def __truediv__(a,b):
        if not isinstance(b,Interval):b=Interval(b)
        assert b.lo>0 or b.hi<0
        return a*Interval.rounded(1/b.hi,1/b.lo)
def intersect(a,b):return Interval(max(a.lo,b.lo),min(a.hi,b.hi))
def ldl(A):
    n=len(A); L=[[Interval(int(i==j)) for j in range(n)] for i in range(n)];D=[]
    for i in range(n):
        p=A[i][i]
        for h in range(i):p=p-L[i][h]*L[i][h]*D[h]
        assert p.lo>0,('pivot',i,p.box()); D.append(p)
        for j in range(i+1,n):
            v=A[j][i]
            for h in range(i):v=v-L[j][h]*L[i][h]*D[h]
            L[j][i]=v/p
    return dict(pivots=[v.box() for v in D],unit_lower=[[v.box() for v in row] for row in L])
def matrices(r,l,s):
    scale=[F(1)]+list(map(F,r['congruence_scales']));n=4
    Q=[[Interval(0) for _ in range(n)] for _ in range(n)]
    G=[[Interval(0) for _ in range(n)] for _ in range(n)]
    Q[0][0]=Interval(*l['native_Q_diagonal']);G[0][0]=Interval(F(l['full_F112_source_square'][1]))
    for i,v in enumerate(r['original_low_lift_pairings']):Q[0][i+1]=Q[i+1][0]=Interval(*v)
    for i in range(3):
        for j in range(3):
            Q[i+1][j+1]=intersect(Interval(*s['original_native_energy_Gram'][i][j]),Interval(*s['original_native_energy_Gram'][j][i]))
            G[i+1][j+1]=intersect(Interval(*s['original_complete_source_Gram'][i][j]),Interval(*s['original_complete_source_Gram'][j][i]))
    Q=[[v*(scale[i]*scale[j]) for j,v in enumerate(row)] for i,row in enumerate(Q)]
    G=[[v*(scale[i]*scale[j]) for j,v in enumerate(row)] for i,row in enumerate(G)]
    return Q,G,scale
def run(paths,digits):
    Interval.digits=digits;data=[read(p) for p in paths];assert [h for _,h in data]==SHA;checks=1
    joint,low,even,odd,prior=[v for v,_ in data]; k=F(11,25);rows=[]
    for idx,(r,l,s,p) in enumerate(zip(joint['rows'],low['native_parity_gates'],(even,odd),prior['rows'])):
        assert r['parity']==l['parity']==s['parity']==p['parity'];checks+=1
        Q,G,scale=matrices(r,l,s)
        t=F(381,1000) if idx==0 else F(173,500)
        c=F(4,125) if idx==0 else F(41,500)
        q=F(1,25) if idx==0 else F(7,50)
        # G is only the block diagonal source majorant input, NOT Gamma4.
        major=[[v*((1+1/t) if i==j==0 else (1+t)) for j,v in enumerate(row)] for i,row in enumerate(G)]
        H=[[Q[i][j]*(k-c)-major[i][j] for j in range(4)] for i in range(4)]
        paid=ldl(H);checks+=4
        native=ldl([[Q[i][j]-Interval(q if i==j else 0) for j in range(4)] for i in range(4)]);checks+=4
        assert c>F(p['reported_complete_remainder_source_credit']);checks+=1
        ell=[F(1,10**6)]+[F(1,5) if idx==0 else F(7,100)]*3
        U=[[Q[i][j]-major[i][j]/k for j in range(4)] for i in range(4)]
        physical=ldl([[U[i][j]-Interval(ell[i] if i==j else 0) for j in range(4)] for i in range(4)]);checks+=4
        mass=list(map(F,p['high_completed_column_mass_upper']))
        gap=1/(sum((a*b)**2/e for a,b,e in zip(scale,mass,ell))+1/k)
        rows.append(dict(parity=r['parity'],young_source_parameter=str(t),complete_four_column_source_credit=str(c),
            prior_credit=p['reported_complete_remainder_source_credit'],native_scaled_identity_lower=str(q),
            scaled_coarse_diagonal_lower=list(map(str,ell)),column_scales=list(map(str,scale)),
            scaled_native_matrix=[[v.box() for v in row] for row in Q],
            scaled_block_source_input=[[v.box() for v in row] for row in G],
            scaled_coherent_source_majorant=[[v.box() for v in row] for row in major],
            signed_comparison_matrix=[[v.box() for v in row] for row in H],
            signed_comparison_LDL=paid,native_identity_comparison_LDL=native,
            physical_diagonal_comparison_LDL=physical,
            high_completed_column_mass_upper=list(map(str,mass)),physical_gap_strict_lower=str(gap),
            display_credit=float(c),display_gap=float(gap)))
    guard=F(19,10**36);assert min(F(r['physical_gap_strict_lower']) for r in rows)>guard;checks+=1
    return dict(stage='DNE28',aperture='53/50',high_floor=str(k),interval_digits=digits,input_sha256=SHA,
        rows=rows,exact_counted_assertions=checks,physical_gap_guard=str(guard),
        unknown_low_source_crosses_paid_by_coherent_Gram_Young=True,
        tested_DNE23_frame_unchanged=True,positive_retained_dimension=8,uncovered_retained_dimension=104,
        complete_remaining_source_Gram_certified=False,new_source_integrations=False,
        actual_infinite_inverse_evaluated=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for key in ['dne23','low','even','odd','dne27']:p.add_argument(key)
    p.add_argument('--digits',type=int,default=80);p.add_argument('--output',required=True)
    a=p.parse_args();r=run([getattr(a,k) for k in ['dne23','low','even','odd','dne27']],a.digits)
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({'checks':r['exact_counted_assertions'],'rows':[{k:v[k] for k in ['parity','display_credit','display_gap']} for v in r['rows']]}))
