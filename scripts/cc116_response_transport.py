"""Rebuild signed response rows at their actual floor by exact physical transport."""
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import validate_cc105_selected_response as data
from certify_cc112_physical_response_transport import sparse,solve,pivots
from certify_cc108_dne41_integration import rank

def transport(parity,packet=None):
 idx=int(parity=='odd');tr,th,_=data.read('notes/data/RPB108_CC112_PHYSICAL_RESPONSE_TRANSPORT_20261010.json.gz.b64');old=tr['parity_checks'][idx];standing,_,_=data.read('notes/data/RPB108_CC113_RESPONSE_AT_603_20261010.json');assert standing['status']=='PASS' and th==standing['parity_checks'][idx]['CC112_transport_sha256']
 if packet is None:return old,th
 frame,fh,_=data.read('notes/cc104-source/notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json');assert fh==old['NF47_frame_sha256'];fr=frame['parity_frames'][idx];joined=[sparse(x) for x in fr['unchanged_joined_columns']];low=fr['retained_indices'];mass=[sum(x.get(i,F(0))**2 for i in low) for x in joined];pv=fr['old_two_constraint_pivots']+[fr['old_free_coordinates'][fr['third_constraint_pivot_in_old_free_coordinates']]];free=[i for i in fr['old_free_coordinates'] if i!=pv[2]];A=[[x.get(low[i],F(0)) for i in pv] for x in joined];R=[[-x.get(low[i],F(0)) for i in free] for x in joined];sol=solve(A,R);remaining=[]
 for j,i in enumerate(free):
  col={low[i]:F(1)}
  for k,q in enumerate(pv):col[low[q]]=sol[k][j]
  remaining.append(col)
 native=joined+remaining;hp,hph,_=data.read(f'notes/data/RPB108_CC105_{parity.upper()}_PHYSICAL_PACKET_20261010.json');assert hph==old['CC105_high_packet_sha256'];Y=[sparse(x) for x in hp['columns'][1:]];ids=old['high_residual_indices'];v=list(map(F,old['exact_missing_high_coefficients']));basis=[[x.get(i,F(0)) for i in ids] for x in Y]+[v];C=[];res=[]
 for raw in packet['columns']:
  col=sparse(raw);assert all(i in low or i in ids for i in col);alpha=[sum(col.get(i,F(0))*x.get(i,F(0)) for i in low)/m for x,m in zip(joined,mass)];beta=[col.get(low[i],F(0))-sum(a*x.get(low[i],F(0)) for a,x in zip(alpha,joined)) for i in free];cc=alpha+beta;C.append(cc)
  assert all(sum(a*x.get(i,F(0)) for a,x in zip(cc,native))==col.get(i,F(0)) for i in low)
  res.append([col.get(i,F(0))-sum(a*x.get(i,F(0)) for a,x in zip(alpha,joined)) for i in ids])
 pp=pivots(basis);coef=solve([[x[i] for x in basis] for i in pp],[[x[i] for x in res] for i in pp]);assert all(sum(basis[k][i]*coef[k][j] for k in range(len(basis)))==res[j][i] for j in range(len(res)) for i in range(len(ids)));assert [list(map(str,row[:44])) for row in zip(*C)]==old['Native_trial_transport_C'];assert [list(map(str,row[:44])) for row in coef[:-1]]==old['paid_high_transport_D'];assert list(map(str,coef[-1][:44]))==old['missing_high_transport_row_t'];assert rank(C)==len(packet['columns'])
 out=dict(old,Native_trial_transport_C=[list(map(str,row)) for row in zip(*C)],paid_high_transport_D=[list(map(str,row)) for row in coef[:-1]],missing_high_transport_row_t=list(map(str,coef[-1])),fresh_retained_rank=len(packet['columns']),exact_prefix_preserved=True);return out,th

def signed_rows(parity,K,high,old):
 QY,GY,BN,SN=[c.matrix(high[key]) for key in ['enlarged_high_native_Gram','enlarged_high_complete_source_Gram','enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']]
 C=c.transpose(c.matrix(old['Native_trial_transport_C']));D=c.transpose(c.matrix(old['paid_high_transport_D']));t=list(map(F,old['missing_high_transport_row_t']));star,sh,_=data.read(f'notes/data/RPB108_CC113_{parity.upper()}_SOURCE_REPLAY_20261010.json');audit,_,_=data.read('notes/data/RPB108_CC113_RESPONSE_AT_603_20261010.json');assert sh==audit['parity_checks'][int(parity=='odd')]['source_replay_sha256'];qv=list(map(c.iv,old['recovered_native_residual_high_row']));gv=list(map(c.iv,star['original_projected_source_Gram'][0][1:]));WK=r.sub(SN,r.scale(BN,K));HY=r.sub(GY,r.scale(QY,K));a=r.mm(C,WK);b=r.mm(D,HY)
 return [[r.compact(c.add(c.add(x,y),c.mul(c.iv(t[i]),c.sub(gv[j],c.mul(c.iv(K),qv[j]))))) for j,(x,y) in enumerate(zip(ar,br))] for i,(ar,br) in enumerate(zip(a,b))]
