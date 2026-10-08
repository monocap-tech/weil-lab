"""NF68 exact critical-output elimination; finite controls are not zeta bounds."""
from fractions import Fraction as F
import json
def tr(a): return [list(x) for x in zip(*a)]
def mm(a,b): return [[sum((x*y for x,y in zip(r,c)),F(0)) for c in zip(*b)] for r in a]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b,s=1): return [[x+s*y for x,y in zip(r,t)] for r,t in zip(a,b)]
def inv(a):
 n=len(a); z=[r[:]+e for r,e in zip(a,eye(n))]
 for j in range(n):
  k=next(k for k in range(j,n) if z[k][j]); z[j],z[k]=z[k],z[j]
  q=z[j][j]; z[j]=[x/q for x in z[j]]
  for k in range(n):
   if k!=j:
    q=z[k][j]; z[k]=[x-q*y for x,y in zip(z[k],z[j])]
 return [r[n:] for r in z]
def block(a,b,c,d): return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def inertia(a):
 a=[r[:] for r in a]; p=m=z=0
 while a:
  n=len(a); k=next((i for i in range(n) if a[i][i]),None)
  if k is not None:
   order=[k]+[i for i in range(n) if i!=k]
   a=[[a[i][j] for j in order] for i in order]; q=a[0][0]
   p+=q>0; m+=q<0
   a=[[a[i][j]-a[i][0]*a[0][j]/q for j in range(1,n)] for i in range(1,n)]
  else:
   pair=next(((i,j) for i in range(n) for j in range(i+1,n) if a[i][j]),None)
   if pair is None: z+=n; break
   order=list(pair)+[i for i in range(n) if i not in pair]
   a=[[a[i][j] for j in order] for i in order]
   b=[r[:2] for r in a[:2]]; cross=[r[2:] for r in a[:2]]
   low=[r[2:] for r in a[2:]]
   a=add(low,mm(mm(tr(cross),inv(b)),cross),-1); p+=1; m+=1
 return p,m,z
def run():
 checks=cases=0; counts={'positive':0,'negative':0,'unit':0}
 def check(v):
  nonlocal checks
  assert v
  checks+=1
 T=[[F(4,5),F(0),F(0)],[F(0),F(3,4),F(0)],[F(0),F(0),F(1,4)]]
 D=add(eye(3),mm(T,tr(T)),-1); G=[r[:2] for r in D[:2]]
 for u in [F(0),F(1,5),F(3,5),F(1)]:
  for v in [F(0),F(1,7),F(2,3)]:
   for r in [F(0),F(1,8)]:
    for q in [F(0),F(1,10)]:
     K=[[u,v],[v,F(1,5)],[r,q]]; L=K[:2]; low=[K[2]]
     B0=[[x/D[2][2] for x in row] for row in mm(tr(low),low)]
     C=add(eye(2),B0,-1)
     check(inertia(C)==(2,0,0))
     B=mm(mm(tr(K),inv(D)),K); J=add(eye(2),B,-1)
     H=add(G,mm(mm(L,inv(C)),tr(L)),-1)
     ij=inertia(J); ih=inertia(H)
     check(ij==ih)
     M=block(C,tr(L),L,G)
     # Each of the two exact square completions reconstructs the same block.
     E1=block(eye(2),mm(inv(C),tr(L)),[[F(0)]*2 for _ in range(2)],eye(2))
     diag1=block(C,[[F(0)]*2 for _ in range(2)],[[F(0)]*2 for _ in range(2)],H)
     check(mm(mm(tr(E1),diag1),E1)==M)
     E2=block(eye(2),[[F(0)]*2 for _ in range(2)],mm(inv(G),L),eye(2))
     diag2=block(J,[[F(0)]*2 for _ in range(2)],[[F(0)]*2 for _ in range(2)],G)
     check(mm(mm(tr(E2),diag2),E2)==M)
     Tall=[a+b for a,b in zip(T,K)]
     original=add(eye(5),mm(tr(Tall),Tall),-1)
     io=inertia(original)
     check(io==(ij[0]+3,ij[1],ij[2]))
     # All critical columns and their mixed complete residual are retained.
     U=[[F(1,3),F(1,9)],[F(1,7),F(1,4)]]
     Eres=add(tr(L),mm(C,U),-1)
     trial=add(add(mm(L,U),mm(tr(U),tr(L))),mm(mm(tr(U),C),U),-1)
     reaction=mm(mm(L,inv(C)),tr(L))
     residual=mm(mm(tr(Eres),inv(C)),Eres)
     check(add(reaction,trial,-1)==residual)
     check(inertia(add(C,[[F(7,8)*a for a in row] for row in eye(2)],-1))[1]==0)
     upper=[[F(8,7)*a for a in row] for row in mm(tr(Eres),Eres)]
     check(inertia(add(upper,residual,-1))[1]==0)
     # Actual old physical representers Z satisfy N Z=critical identity.
     Acrit=[[F(16,25),F(0)],[F(0),F(9,16)]]
     Z=mm(tr(T[:2]),inv(Acrit))
     check(mm(T,Z)==[[F(1),F(0)],[F(0),F(1)],[F(0),F(0)]])
     # Positive old/incoming ranges are orthogonal, so Q(Z,k)=-L.
     check(mm(tr(Z),mm(T,K))==L)
     counts['negative' if ih[1] else 'unit' if ih[2] else 'positive']+=1
     cases+=1
 # Exact original contact: T=4/5, incoming=3/5, equal nonzero energies.
 d=F(9,25); ell=F(3,5)
 check(d-ell*ell==0)
 h=[[F(4,3)],[F(1)]]; N=[[F(4,5),F(3,5)]]
 check(mm(add(eye(2),mm(tr(N),N),-1),h)==[[F(0)],[F(0)]])
 # Coupled low channel renormalizes reaction: raw L L*<G does NOT suffice.
 G1=F(1,2); L2=F(1,4); C1=F(1,4)
 check(L2<G1 and G1-L2/C1<0)
 # Positive physical eigenlevel 11/100, never relabeled unshifted nullity.
 N=[[F(4,5),F(1,2)]]; gram=mm(tr(N),N); Q=add(eye(2),gram,-1)
 h=tr(N); mu=F(11,100)
 check(mm(Q,h)==[[mu*x[0]] for x in h])
 check(mm(add(Q,[[mu*x for x in row] for row in eye(2)],-1),h)==[[F(0)],[F(0)]])
 check(counts['positive']>0 and counts['negative']>0)
 return {'passed':True,'exact_checks':checks,'coupled_cases':cases,'inertia_cases':counts,
 'criterion':'Gcrit-L (I-B_low)^(-1) L* > 0',
 'whole_incoming_range_retained':True,'actual_arithmetic_overlap_bound':False,
 'new_aperture_certificate':False,'arithmetic_nondivergence':False,'lean_certified':False}
if __name__=='__main__': print(json.dumps(run(),indent=2))
