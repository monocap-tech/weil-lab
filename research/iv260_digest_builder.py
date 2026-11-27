"""IV260 outward digest export. Run python iv260_digest_builder.py /tmp/iv260_joint.json."""
import json, hashlib, sys
from fractions import Fraction as F
p=sys.argv[1]
raw=open(p,'rb').read()
assert hashlib.sha1(('blob '+str(len(raw))+'\0').encode()+raw).hexdigest()=='93ded854f86f6d4067be11083bc7c14a2b6cf908'
r=json.loads(raw);V=int(r['scale']);U=int(r['energy_scale']);ED=int(r['inverse_variational_center_denominator']);D=10**18
fl=lambda x:x.numerator//x.denominator
ce=lambda x:-fl(-x)
def interval(k):return [[[str(fl(F(int(x[0])*D,V**2))),str(ce(F(int(x[1])*D,V**2)))] for x in row] for row in r[k]]
def upper(mat,den,loss=F(0)):
 A=[[fl(F(int(x)*D,den)) for x in row] for row in mat]
 for i in range(4):A[i][i]+=4+ce(loss*D)
 return [list(map(str,row)) for row in A]
out={'scale':str(D),'prefix_gram':interval('original_prefix_gram_interval_scaled_squared'),'projected_prefix_gram':interval('orthogonalized_prefix_gram_interval_scaled_squared'),'projected_energy_upper':upper(r['orthogonalized_energy_upper_scaled'],U),'projected_factor_inverse_upper':upper(r['inverse_variational_center'],ED,F(r['inverse_upper_uniform_loss'])),'extra_correlation_radius':[str(ce(F(int(x)*D,U))) for x in r['correlation_extra_error_scaled']],'prefix_projection_column_square_upper':[str(ce(F(int(x)*D,int(r['prefix_projection_coeff_scale'])**2))) for x in r['prefix_projection_column_square_numerators']],'source_receipt_sha':'93ded854f86f6d4067be11083bc7c14a2b6cf908'}
data=(json.dumps(out,indent=2)+'\n').encode()
assert hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest()=='ec811065bb376e7f7fe3ceeaa4077f95e6be1a5c'
sys.stdout.buffer.write(data)
