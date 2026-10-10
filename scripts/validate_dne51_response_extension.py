#!/usr/bin/env python3
"""Independent unrounded rational optimal-response and new-frame audit."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import argparse,json,gzip,base64,hashlib

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def div(a,b):
 assert b[0]>0;return mul(a,(1/b[1],1/b[0]))
def total(v):
 r=(F(0),F(0))
 for x in v:r=add(r,x)
 return r
def boxes(M):return [[tuple(map(F,v)) for v in row] for row in M]
def tr(M):return list(map(list,zip(*M)))
def mm(A,B):return [[total(mul(x,y) for x,y in zip(row,col) if x!=(0,0) and y!=(0,0)) for col in zip(*B)] for row in A]
def quadratic(A,v):return total(mul((x*y,x*y),A[i][j]) for i,x in enumerate(v) for j,y in enumerate(v) if x and y)
def raw(c):return {n:F(v) for n,v in zip(c['indices'],c['coefficients']) if F(v)}
def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def encloses(a,b):check(F(a[0])<=b[0]<=b[1]<=F(a[1]))
 def positive(pc,M):
  O=boxes(pc['original_matrix']);U=[list(map(F,row)) for row in pc['exact_congruence_U']];n=len(M);check(len(O)==len(U)==n and all(len(row)==n for row in O+U))
  for i in range(n):
   check(U[i][i]!=0)
   for j in range(n):check(i<=j or U[i][j]==0);encloses(O[i][j],M[i][j])
  UI=[[(x,x) for x in row] for row in U];K=mm(tr(UI),mm(O,UI));S=boxes(pc['congruence_matrix']);margins=[]
  for i in range(n):
   for j in range(n):encloses(S[i][j],K[i][j])
   d=S[i][i][0]-sum(max(abs(a),abs(b)) for j,(a,b) in enumerate(S[i]) if j!=i);check(d==F(pc['Gershgorin_margins'][i]) and d>0);margins.append(d)
  check(F(pc['coefficient_floor_lower'])==min(margins)/sum(x*x for row in U for x in row))
 c,ch=read(path);check(c['stage']=='DNE51' and c['parent']=='3c61708f807b42ddffcff7d0a8516ea6a9e45cf1');inp=[read(p) for p in c['input_paths']];check([h for x,h in inp]==c['input_sha256']);r,rv,subspaces,sv,packet,old,srcv=[x for x,h in inp];check(rv['status']==sv['status']==srcv['status']=='PASS');check(rv['certificate_sha256']==inp[0][1] and sv['certificate_sha256']==inp[2][1]);check(sv['actual_certified_all_high_retained_dimension']==109 and sv['uncovered_retained_dimension']==3)
 z=r['rows'][0];check(z['parity']=='even');source,sh=read(z['source_path']);check(sh==z['source_sha256']==srcv['rows'][0]['replay_sha256']);check(source['joint_packet_input_sha256'][0]==inp[4][1]);N=boxes(z['original_native_matrix']);G=boxes(z['projected_native_source_Gram']);M=boxes(z['original_native_M']);A=boxes(z['original_native_A']);S=boxes(source['original_projected_source_Gram']);mapn=source['native_to_source'];ys=source['trial_source_indices'];check(len(mapn)==56 and ys==[44,45,46]);B=[[S[i][j] for j in ys] for i in mapn];D=[[S[i][j] for j in ys] for i in ys]
 for i in range(56):
  for j in range(56):encloses(N[i][j],tuple(map(F,source['native_block'][i][j])));encloses(G[i][j],S[mapn[i]][mapn[j]])
 def fields(t):
  E=[[sub(b,mul((t,t),m)) for b,m in zip(br,mr)] for br,mr in zip(B,M)];W=[[sub(d,mul((t,t),a)) for d,a in zip(dr,ar)] for dr,ar in zip(D,A)];H=[[sub(mul((t,t),n),g) for n,g in zip(nr,gr)] for nr,gr in zip(N,G)];return E,W,H
 def inverse_quadratic_ldl(W,e):
  d0=W[0][0];l10=div(W[1][0],d0);l20=div(W[2][0],d0);d1=sub(W[1][1],mul(mul(l10,l10),d0));l21=div(sub(W[2][1],mul(mul(l20,l10),d0)),d1);d2=sub(sub(W[2][2],mul(mul(l20,l20),d0)),mul(mul(l21,l21),d1));check(min(d0[0],d1[0],d2[0])>0);u0=e[0];u1=sub(e[1],mul(l10,u0));u2=sub(sub(e[2],mul(l20,u0)),mul(l21,u1));return total(div(mul(u,u),d) for u,d in zip((u0,u1,u2),(d0,d1,d2)))
 def inverse_quadratic_adjugate(W,e):
  # Determinant expanded by all six permutations; no producer inverse helper.
  det=(F(0),F(0))
  for p in permutations(range(3)):
   sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3));term=(F(sign),F(sign))
   for i in range(3):term=mul(term,W[i][p[i]])
   det=add(det,term)
  check(det[0]>0)
  # Check the stored enclosure with the same cofactor grouping, using
  # independently evaluated unrounded rationals. The permutation determinant
  # above and the LDL sign check are separate controls of the inverse.
  cof=[]
  for j in range(3):
   cols=[a for a in range(3) if a!=j]
   v=sub(mul(W[1][cols[0]],W[2][cols[1]]),mul(W[1][cols[1]],W[2][cols[0]]))
   cof.append(mul((F((-1)**j),)*2,v))
  det=total(mul(W[0][j],cof[j]) for j in range(3));check(det[0]>0);out=(F(0),F(0))
  for i in range(3):
   for j in range(3):
    rows=[a for a in range(3) if a!=j];cols=[a for a in range(3) if a!=i];co=sub(mul(W[rows[0]][cols[0]],W[rows[1]][cols[1]]),mul(W[rows[0]][cols[1]],W[rows[1]][cols[0]]));co=mul((F((-1)**(i+j)),)*2,co);out=add(out,mul(mul(e[i],e[j]),div(co,det)))
  return out
 audited=[]
 for index,a in enumerate(c['fixed_even_trial_obstructions']):
  t=F(a['hypothetical_high_floor']);check(t==[F(647,1000),F(669,1000),F(69,100)][index]);E,W,H=fields(t);positive(a['W_positive_certificate'],W)
  for i in range(3):
   for j in range(3):encloses(a['residual_W'][i][j],W[i][j])
  v=list(map(F,a['exact_failure_trial']));check(len(v)==56 and any(v));base=quadratic(H,v);e=[total(mul((v[i],v[i]),E[i][j]) for i in range(56)) for j in range(3)];credit=inverse_quadratic_adjugate(W,e);q=add(base,credit);ldlq=add(base,inverse_quadratic_ldl(W,e));encloses(a['base_trial_budget'],base);encloses(a['optimal_credit_trial'],credit);encloses(a['optimal_trial_budget'],q);check(q[1]<0 and ldlq[1]<0 and a['no_coefficient_matrix_J_closes_full_even_budget']);audited.append(dict(hypothetical_high_floor=str(t),independent_optimal_budget_upper=str(q[1]),independent_LDL_budget_upper=str(F((ldlq[1]*10**80).__ceil__(),10**80))))
 u=c['hypothetical_even_sufficient_upper'];t=F(u['hypothetical_high_floor']);check(t==F(691,1000) and u['actual_high_floor_established'] is False);E,W,H=fields(t);J=[list(map(F,row)) for row in u['exact_trial_coefficients_J']];check(len(J)==3 and all(len(row)==56 for row in J));JI=[[(x,x) for x in row] for row in J];EJ=mm(E,JI);JWJ=mm(tr(JI),mm(W,JI));paid=[[sub(add(add(H[i][j],EJ[i][j]),EJ[j][i]),JWJ[i][j]) for j in range(56)] for i in range(56)];positive(u['full_budget_positive_certificate'],paid)
 ceiling=F(old['positive_region_shell_route_ceiling_upper']);check(F(c['positive_region_shell_route_ceiling_upper'])==ceiling<F(669,1000)<F(69,100));check(c['fixed_even_trial_required_floor_lower']=='69/100' and c['fixed_even_trial_sufficient_floor_upper']=='691/1000')
 Y=old['physical_high_trial_columns'];Yraw=[raw(a) for a in Y];chart=c['even_packet_tail_recycling'];co=chart['exact_packet_tail_coefficients'];check(len(co)==56 and all(len(row)==3 for row in co))
 for a,abc in zip(packet['rows'][0]['columns'],co):
  high={n:v for n,v in raw(a).items() if n>=112};abc=list(map(F,abc));ids=set(high).union(*[set(v) for v in Yraw])
  for n in ids:check(high.get(n,F(0))==sum(abc[i]*Yraw[i].get(n,F(0)) for i in range(3)))
 check(chart['all_56_packet_high_tails_in_old_trial_span'] and c['old_even_trial_space_exhausted'])
 frames=[]
 for f in c['proposed_source_extensions']:
  par=f['parity'];check(par in ('even','odd'));oldcols=Y if par=='even' else [];new=f['new_trial_columns'];allcols=f['all_trial_columns'];check(allcols==oldcols+new and len(new)==3);size=59 if par=='even' else 56;check(f['reused_source_dimension']==size and f['reused_trial_count']==len(oldcols));source2,sh2=read(r['rows'][0 if par=='even' else 1]['source_path']);check(source2['joint_packet_input_sha256'][0]==inp[4][1] and sh2==srcv['rows'][0 if par=='even' else 1]['replay_sha256'])
  for i,a in enumerate(new):
   h=raw(a);check(all(n>=112 and n%2==(0 if par=='even' else 1) for n in h));mass=sum(v*v for v in h.values());check(F(a['exact_mass_squared'])==mass>0)
   if par=='even':check(a['indices']==[112+2*i] and a['coefficients']==['1'])
   else:
    col=packet['rows'][1]['columns'][i+1];original={n:v for n,v in raw(col).items() if n>=112};scale=F(a['rational_normalization']);om=sum(v*v for v in original.values());check(a['parent_packet_column']==i+1 and F(a['original_high_mass_squared'])==om and scale*scale>om>0)
    check(set(original)==set(h))
    for n,v in original.items():check(h[n]*scale==v)
  vals=[raw(a) for a in allcols];GG=[[(sum(v*b.get(n,F(0)) for n,v in a.items()),)*2 for b in vals] for a in vals];positive(f['physical_Gram_positive_certificate'],GG)
  for i in range(len(GG)):
   for j in range(len(GG)):encloses(f['physical_Gram'][i][j],GG[i][j])
  expected=[[i,j] for j in range(size,size+3) for i in range(j+1)];check(f['new_source_upper_triangle']==expected and f['new_source_correlation_count']==len(expected));check(f['physical_trial_dimension']==len(allcols) and f['original_new_trial_sources_certified'] is False and f['new_response_credit_established'] is False);frames.append(dict(parity=par,physical_trial_dimension=len(allcols),new_source_correlation_count=len(expected)))
 check([a['parity'] for a in frames]==['even','odd']);check(c['new_source_correlations_required']==sum(a['new_source_correlation_count'] for a in frames)==357);check(c['actual_certified_all_high_retained_dimension']==109 and c['uncovered_retained_dimension']==3 and c['actual_original_high_floor']=='647/1000' and c['original_aperture']=='53/50')
 for k in ('source_integrals_recomputed','new_original_positivity_established','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(c[k] is False)
 # Crossing and mixed controls: optimal comparison failure is not original negativity.
 # L=diag(2,5), k=1, Y=e2, f=I gives upper diag(1,1/5).
 check(F(1,5)>0 and F(1,2)-F(1,5)>0)
 check((2-1)*(F(7,10)-F(1,5))-1<0) # positive diagonals do not pay mixed coupling
 check(F(3,4)-1<0<F(3,4)-F(1,2)) # failed bound with positive true Schur
 out=dict(stage='DNE51',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],fixed_even_trial_obstructions=audited,hypothetical_even_floor_bracket=['69/100','691/1000'],old_even_packet_tail_space_exhausted=True,proposed_source_extensions=frames,new_source_correlations_required=357,actual_certified_all_high_retained_dimension=109,uncovered_retained_dimension=3,new_original_positivity_established=False,whole_aperture_positive=False,RH=False,Lean=False);Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'checks; original rank unchanged at 109',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--output',required=True);a=p.parse_args();run(a.input,a.output)
