import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
NATIVE_COMMIT='fd077f602b7e5762e85660e66fcc8d69e7a3b210'
NATIVE_RUN=40391210597
NATIVE_ARTIFACT=12684320650
ARCHIVE_SHA256='06c23a32846c1d3decd1538d7d0ae8aa8ebd1775c748295184225892daeec732'
JSON_SHA256='4a230980bd536e400f168e6f9b4855f53eb3962ab47c7a79dfdf5499f5798b6c'
def dy(x):
 n,e=int(x[0]),int(x[1]);return F(n*2**max(e,0),2**max(-e,0))
def run(path):
 raw=Path(path).read_bytes();assert hashlib.sha256(raw).hexdigest()==JSON_SHA256
 z=json.loads(raw);assert z['status']=='CONDITIONAL_ACTUAL_NORMALIZED_FULL_J_ENERGY_UPPER'
 D=z['normalized_derivative_Gram_balls'];v=z['normalized_endpoint_balls']
 assert len(D)==len(v)==14 and all(len(r)==14 for r in D)
 assert all(dy(x[1])>=0 for row in D for x in row) and all(dy(x[1])>=0 for x in v)
 trace=sum((dy(D[i][i][0])+dy(D[i][i][1]) for i in range(14)),F(0))
 endpoint=sum(((abs(dy(x[0]))+dy(x[1]))**2 for x in v),F(0))
 V2=8*endpoint+F(44,10)*trace
 assert V2>0
 assert 36*F(101,100)+V2==F(z['exact_variation_energy_upper'])
 assert z['rational_energy_operator_upper']==2**33
 # exp(7/10)>2 by four positive Taylor terms, hence log(2)<7/10.
 t=F(7,10);assert 1+t+t*t/2+t**3/6>2
 candidates=[]
 for k in range(81):
  logR=k*t;R=2**k
  low=max(F(36),17+logR)
  high=V2*(18+logR)/(18*R)
  bound=F(101,100)*low+high
  rounded=F((bound*10**9).__ceil__(),10**9)
  candidates.append((bound,k,rounded))
 bound,k,rounded=min(candidates)
 U=1
 while U<bound:U*=2
 floor=F(z['conditional_energy_lower']);assert floor==F(3328479,10**11)
 assert U<2**33
 return dict(status='EXACT_RATIONAL_ORIGINAL_NORMALIZED_LOG_SPLIT_ENERGY_BOUND',
  accepted_input_commit=NATIVE_COMMIT,accepted_input_run=NATIVE_RUN,accepted_input_artifact=NATIVE_ARTIFACT,
  accepted_input_json_sha256=JSON_SHA256,exact_variation_squared_upper=str(V2),
  selected_cutoff_power=k,selected_cutoff=2**k,log2_upper='7/10',
  selected_exact_energy_upper=str(bound),rational_energy_operator_upper=U,
  conditional_energy_lower=str(floor),conditional_energy_condition_number_upper=str(F(U)/floor),
  previous_energy_upper=2**33,energy_upper_improvement_factor=str(F(2**33,U)),
  candidate_energy_uppers=[dict(k=i,upper=str(r)) for b,i,r in candidates],
  new_frequency_integration_performed=False,actual_Astar_projection_computed=False,
  matched_forcing_computed=False,inverse_response_certified=False,
  W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--certificate',required=True);p.add_argument('--output',default='artifacts/si29_log_split_energy.json');a=p.parse_args()
 z=run(a.certificate);o=Path(a.output);o.parent.mkdir(parents=True,exist_ok=True);o.write_text(json.dumps(z,indent=2)+'\n')
 print('EXACT LOG-SPLIT ENERGY PASS: upper',z['rational_energy_operator_upper'],'cutoff 2^',z['selected_cutoff_power'])
 print('Condition ceiling',float(F(z['conditional_energy_condition_number_upper'])))
