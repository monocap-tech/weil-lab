#!/usr/bin/env python3
"""Complete original joint tested/remainder projected source Gram.

All source correlations, whole-source analytic integrals, paid common-grid
coefficient rounding, and complete E112 projection. No quadrature.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,base64,gzip,hashlib,json,sys,time
from materialize_dne50_complete_sources import run as materialize
from dne44_integer_moment_dot import outward_moments,integer_dot

PARENT='7d0d03400f78a3bf0d91d01c52a1b6d6a33e4bd4'
def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def packed_conv(a,b):
 """Exact signed Kronecker substitution with an explicit no-carry bound."""
 am=max(map(abs,a),default=0);bm=max(map(abs,b),default=0)
 if not am or not bm:return [0]*(len(a)+len(b)-1)
 bits=am.bit_length()+bm.bit_length()+min(len(a),len(b)).bit_length()+2
 base=1<<bits;half=base>>1;mask=base-1
 assert min(len(a),len(b))*am*bm<half
 def pack(v):
  out=0
  for x in reversed(v):out=(out<<bits)+x
  return out
 value=pack(a)*pack(b);out=[]
 for k in range(len(a)+len(b)-1):
  digit=value&mask
  if digit>=half:digit-=base
  out.append(digit);value=(value-digit)>>bits
 assert value==0
 return out

def root(x):
 scale=10**160;v=F(isqrt(x.numerator*scale*scale//x.denominator)+1,scale);assert v*v>x;return v

def run(parity,count,output,finalize_checkpoint=False):
 start=time.time();assert parity=='even' and count==62
 gp='notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64';g,gh=read(gp);z=g['rows'][0]
 oldcols=z['columns'][:44]+z['high_trial_columns']+z['columns'][44:]
 ext,eh=read('notes/data/RPB108_DNE51_RESPONSE_EXTENSION_20261010.json.gz.b64');newcols=ext['proposed_source_extensions'][0]['new_trial_columns']
 cols=oldcols+[{**c,'norm_upper':str(F(1)+F(1,10**100))} for c in newcols];reused_count=59
 packet=dict(columns=cols,column_labels=z['source_column_labels']+['e112','e114','e116'],native_matrix=z['native_matrix'],native_to_source=z['native_to_source'],trial_source_indices=[44,45,46,59,60,61]);ph=hashlib.sha256((json.dumps(packet,sort_keys=True)+'\n').encode()).hexdigest()
 bridge,bhash=read('notes/data/RPB108_DNE52_CC117_INGESTION_20261010.json');bv,bvh=read('notes/data/RPB108_DNE52_CC117_INGESTION_VALIDATION_20261010.json');assert bv['status']=='PASS' and bv['certificate_sha256']==bhash
 required=set(map(tuple,bridge['new_even_source_upper_triangle']));controls={(59,59),(59,60),(60,60)};pairs=required|controls;assert len(required)==68 and len(pairs)==71
 hp='scripts/dne23_dne16_source_input.py';helper=Path(hp).read_bytes();hh=hashlib.sha256(helper).hexdigest();assert hh=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8'
 target='notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64';prefix=helper.decode().split('\nps=[p]+')[0];assert prefix.count('range(116)')==1;prefix=prefix.replace('range(116)','range(181)')
 old=sys.argv;sys.argv=[hp,parity,target];d={}
 try:exec(compile(prefix,hp,'exec'),d)
 finally:sys.argv=old
 suffix='_REPLAY' if d['N']==400 else '';assert (d['N'],d['P']) in [(360,600),(400,620)];reuse_path=f'notes/data/RPB108_DNE50_EVEN_COMPLETE_SOURCE{suffix}_20261010.json.gz.b64';reuse,rh=read(reuse_path);assert reuse['helper_sha256']==hh and reuse['column_labels']==packet['column_labels'][:59] and reuse['joint_packet_input_sha256'][0]==gh
 I,Z,A,bases=d['I'],d['Z'],d['A'],d['bases'];plus=d['plus'];low=0 if parity=='even' else 1;ps=[];us=[]
 for col in cols:
  p=[Z]*(max(col['indices'])+1);dp=[Z]*len(p)
  for n,c in zip(col['indices'],map(F,col['coefficients'])):
   p=plus(p,bases[n],I(c));dp=plus(dp,bases[n],I(c)*I(sum((F(1,k) for k in range(1,n+1)),F(0))))
  ps.append(p)
  if not finalize_checkpoint:us.append(d['make_u'](p,dp));print('block source',parity,len(ps),round(time.time()-start,1),flush=True)
 gridpoly=10**250;moment_grid=10**d['P']
 def exact_dot(coeff,moments,denominator):
  lo,hi=integer_dot(coeff,moments);return I(I(F(lo,denominator*moment_grid)).lo,I(F(hi,denominator*moment_grid)).hi)
 def roundpoly(poly):
  ints=[];delta=Z
  for k,v in enumerate(poly):
   z=round((F(v.lo)+F(v.hi))/2*gridpoly);ints.append(z);delta=delta+I(max(abs(F(v.lo)-F(z,gridpoly)),abs(F(v.hi)-F(z,gridpoly))))*A**k
  return ints,delta
 log2=I(2).log();loga=A.log();L2=[]
 for k in range(0,2*max(map(len,ps))-1,2):
  m=k//2;dd=-d['pi']*d['pi']/3+4*I(sum((F(1,(2*j+1)**2) for j in range(m+1)),F(0)));psi=2*log2-2*I(sum((F(1,2*j+1) for j in range(m+1)),F(0)));L2.append(A**(k+1)/I(k+1)*((2*loga+psi)**2+dd))
 l2mom=outward_moments([x/4 for x in L2],moment_grid)
 rounded=[roundpoly(p) for p in ps];rps=[x[0] for x in rounded];delta_ps=[x[1] for x in rounded];rpis=[[I(F(x,gridpoly)) for x in p] for p in rps]
 if finalize_checkpoint:
  saved=json.loads(Path(output+'.checkpoint.json').read_text());identity=saved['identity'];expected=dict(parity=parity,count=count,order=d['N'],precision=d['P'],packet_sha256=ph,reuse_sha256=rh)
  assert {k:v for k,v in identity.items() if k!='producer_sha256'}==expected and identity['producer_sha256'] in ('fafceb81ecfddb3ded981131f74d07612e21d5d1b1dafb5ad0f051c530f6d179',hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
  assert saved['completed_panel']==6
  gram=[[I(*x) for x in row] for row in saved['gram']];moments=[[I(*x) for x in row] for row in saved['moments']];panel_errors=saved['panel_errors'];assert len(gram)==count and all(len(r)==count for r in gram) and len(moments)==count and all(len(r)==181 for r in moments) and len(panel_errors)==count and all(len(r)==7 for r in panel_errors)
  maxn=180;print('finalizing complete authenticated seven-panel checkpoint',flush=True)
 else:
  active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active};cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active};cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active];cuts.sort(key=lambda x:x.lo);assert all(l.hi<h.lo for l,h in zip(cuts,cuts[1:]))
  maxn=180;maxdeg=max(max(map(len,ps))-1+maxn,max(map(len,us))+max(map(len,ps))-2);logs={}
  for j,x in enumerate(cuts):
   xp=[x**k for k in range(maxdeg+2)];vals=[Z]*(maxdeg+1)
   for sign in (-1,1):
    b=-sign*A;bp=[b**k for k in range(maxdeg+2)];y=A+sign*x;endpoint=y.lo<=0<=y.hi
    if endpoint:assert abs(y.lo)<d['D']('1e-170') and abs(y.hi)<d['D']('1e-170')
    ly=Z if endpoint else y.log();S=Z
    for k in range(maxdeg+1):
     S=b*S+xp[k+1]/(k+1);vals[k]=vals[k]+((Z if endpoint else (xp[k+1]-bp[k+1])*ly)-S)/(k+1)
   for k,v in enumerate(vals):logs[k,j]=v
  gram=[[Z for _ in cols] for _ in cols];moments=[[Z]*(maxn+1) for _ in cols];panel_errors=[[] for _ in cols]
  for i in range(count):
   for j in range(i,count):
    if (i,j) not in pairs:continue
    pp=packed_conv(rps[i],rps[j]);gram[i][j]=exact_dot(pp[::2],l2mom[:len(pp[::2])],gridpoly**2)
  shifts=[{(n,s):d['shift'](p,s*ells[n]) for n in active for s in (-1,1)} for p in ps]
  checkpoint_path=Path(output+'.checkpoint.json');checkpoint_identity=dict(parity=parity,count=count,order=d['N'],precision=d['P'],packet_sha256=ph,reuse_sha256=rh,producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());completed=-1
  if checkpoint_path.exists():
   saved=json.loads(checkpoint_path.read_text());assert saved['identity']==checkpoint_identity;completed=saved['completed_panel'];assert 0<=completed<7
   gram=[[I(*x) for x in row] for row in saved['gram']];moments=[[I(*x) for x in row] for row in saved['moments']];panel_errors=saved['panel_errors'];assert len(gram)==count and all(len(row)==count for row in gram);assert len(moments)==count and all(len(row)==maxn+1 for row in moments);assert len(panel_errors)==count and all(len(row)==completed+1 for row in panel_errors)
   print('resumed completed panel',parity,completed,flush=True)
  def save_checkpoint(panel):
   def pairs(rows):return [[[str(x.lo),str(x.hi)] for x in row] for row in rows]
   payload=dict(identity=checkpoint_identity,completed_panel=panel,gram=pairs(gram),moments=pairs(moments),panel_errors=panel_errors)
   temp=checkpoint_path.with_suffix('.tmp');temp.write_text(json.dumps(payload));temp.replace(checkpoint_path)
  for panel,(l,h) in enumerate(zip(cuts,cuts[1:])):
   if panel<=completed:continue
   mid=(l+h)/2;pm=[(h**(k+1)-l**(k+1))/(k+1) for k in range(max(2*max(map(len,us))-1,max(map(len,us))+maxn))];rus=[];pmi=outward_moments(pm,moment_grid);lmi=outward_moments([logs[k,panel+1]-logs[k,panel] for k in range(maxdeg+1)],moment_grid)
   for i,(p,u) in enumerate(zip(ps,us)):
    uj=list(u)
    for n in active:
     for s in (-1,1):
      pos=mid+s*ells[n]
      if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shifts[i][n,s],-cs[n])
      else:assert pos.hi<=-A.hi or pos.lo>=A.hi
    ru,de=roundpoly(uj);rus.append(ru);panel_errors[i].append(str(de.hi));ui=[I(F(x,gridpoly)) for x in ru]
    for k in (range(low,maxn+1,2) if i>=reused_count else []):moments[i][k]=moments[i][k]+exact_dot(ru,pmi[k:k+len(ru)],gridpoly)-exact_dot(rps[i],lmi[k:k+len(rps[i])],2*gridpoly)
   for i in range(count):
    for j in range(i,count):
     if (i,j) not in pairs:continue
     uu=packed_conv(rus[i],rus[j]);up=packed_conv(rus[i],rps[j]);pu=packed_conv(rus[j],rps[i]);assert len(up)==len(pu);mixed=[x+y for x,y in zip(up,pu)]
     gram[i][j]=gram[i][j]+exact_dot(uu,pmi[:len(uu)],gridpoly**2)-exact_dot(mixed,lmi[:len(mixed)],2*gridpoly**2)
   save_checkpoint(panel)
   print('block panel',parity,panel,round(time.time()-start,1),'checkpoint saved',flush=True)
 coords=[[2*sum((x*moments[i][k] for k,x in enumerate(bases[n])),Z) for n in range(low,112,2)] for i in range(count)]
 grid=10**100
 def floor(x):return F((F(x)*grid).__floor__(),grid)
 def ceil(x):return -floor(-F(x))
 def box(v):return [str(floor(v.lo)),str(ceil(v.hi))]
 whole=[[None]*count for _ in cols]
 for i in range(count):
  for j in range(i,count):whole[i][j]=whole[j][i]=reuse['complete_rounded_source_Gram'][i][j] if j<reused_count else (box(2*gram[i][j]) if (i,j) in pairs else None)
 actioncoords=[[box(2*sum((x*moments[i][k] for k,x in enumerate(bases[n])),Z)) for n in range(0,181,2)] for i in range(59,62)]
 cboxes=reuse['retained_rounded_source_coordinates']+[row[:56] for row in actioncoords]
 assert panel_errors[:reused_count]==reuse['panel_regular_polynomial_sup_error_upper'];assert [str(x.hi) for x in delta_ps[:reused_count]]==reuse['logarithmic_polynomial_sup_error_upper']
 # All load-bearing projection arithmetic and source payments are rational.
 projected=[[None]*count for _ in cols]
 for i in range(count):
  for j in range(i,count):
   if whole[i][j] is None:continue
   lo,hi=map(F,whole[i][j])
   for a,b in zip(cboxes[i],cboxes[j]):
    al,ah=map(F,a);bl,bh=map(F,b);v=[al*bl,al*bh,ah*bl,ah*bh];lo-=max(v);hi-=min(v)
   projected[i][j]=projected[j][i]=[str(lo),str(hi)]
 eta=ceil((2*A*I(F(550,19))*I(F(106,125))**d['N']+I('3e-99')).hi);sqrta=ceil((2*A).sqrt().hi);lognorm=ceil((2*L2[0]).sqrt().hi)
 rounding=[ceil(sqrta*max(map(F,row))+F(de.hi)*lognorm/2) for row,de in zip(panel_errors,delta_ps)];errors=[ceil(eta*F(c['norm_upper'])+e) for c,e in zip(cols,rounding)];roots=[root(F(projected[i][i][1])) for i in range(count)];original=[[None]*count for _ in cols];payments=[[None]*count for _ in cols]
 for i in range(count):
  for j in range(count):
   if projected[i][j] is None:continue
   e=ceil(errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);lo,hi=map(F,projected[i][j]);original[i][j]=[str(lo-e),str(hi+e)];payments[i][j]=str(e)
 for i in range(59):
  for j in range(59):assert original[i][j]==reuse['original_projected_source_Gram'][i][j]
 fresh={f'{i},{j}':original[i][j] for i,j in sorted(pairs)}
 for ii,i in enumerate(packet['native_to_source']):
  for u,j in enumerate((59,60)):original[i][j]=original[j][i]=bridge['reused_projected_source_pairings_Z_to_e112_e114'][ii][u]
 for u,i in enumerate((59,60)):
  for v,j in enumerate((59,60)):original[i][j]=bridge['reused_projected_source_self_Gram'][u][v]
 assert all(x is not None for row in original for x in row)
 out=dict(stage='DNE53',parent=PARENT,parity='even',packet_definition_sha256=ph,input_paths=[gp,'notes/data/RPB108_DNE51_RESPONSE_EXTENSION_20261010.json.gz.b64','notes/data/RPB108_DNE52_CC117_INGESTION_20261010.json','notes/data/RPB108_DNE52_CC117_INGESTION_VALIDATION_20261010.json',reuse_path],input_sha256=[gh,eh,bhash,bvh,rh],reused_source_path=reuse_path,reused_source_sha256=rh,reused_joint_dimension=59,columns=cols,column_labels=packet['column_labels'],precision=d['P'],regular_order=d['N'],helper_sha256=hh,exact_masses=[c['exact_mass_squared'] for c in cols],physical_norm_upper=[c['norm_upper'] for c in cols],polynomial_rounding_grid_digits=250,logarithmic_polynomial_sup_error_upper=[str(x.hi) for x in delta_ps],panel_regular_polynomial_sup_error_upper=panel_errors,physical_interval_sqrt_upper=str(sqrta),complete_log_squared_norm=box(2*L2[0]),complete_log_norm_upper=str(lognorm),uniform_original_source_operator_error_upper=str(eta),polynomial_rounding_source_L2_error_upper=list(map(str,rounding)),source_L2_error_upper=list(map(str,errors)),complete_rounded_source_Gram=whole,retained_projection_indices=list(range(0,112,2)),retained_rounded_source_coordinates=cboxes,new_action_coordinate_indices=list(range(0,181,2)),new_rounded_action_coordinates=actioncoords,projected_rounded_source_Gram=projected,projected_source_norm_upper=list(map(str,roots)),source_Gram_error_payments=payments,original_projected_source_Gram=original,fresh_original_projected_source_pairings=fresh,new_source_upper_triangle=sorted(required),source_control_upper_triangle=sorted(controls),native_block=packet['native_matrix'],native_to_source=packet['native_to_source'],trial_source_indices=packet['trial_source_indices'],complete_original_source_action=True,exact_endpoint_logs=True,all_six_primes_both_orientations=True,half_translation_panels=7,sampled_quadrature=False,complete_remaining_source_Gram_certified=True,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(parity,count,'complete coherent source block',round(time.time()-start,1),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('parity',choices=['even','odd']);p.add_argument('--count',type=int,default=62);p.add_argument('--output',required=True);p.add_argument('--finalize-checkpoint',action='store_true');a=p.parse_args();run(a.parity,a.count or {'even':59,'odd':56}[a.parity],a.output,a.finalize_checkpoint)
