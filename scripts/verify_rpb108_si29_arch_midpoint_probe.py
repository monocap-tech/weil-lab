#!/usr/bin/env python3
"""One complete raw-source arch shift node; NOT a quadrature certificate."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb,arb_mat,ctx
import verify_rpb108_si29_original_prime_mixed as p

NATIVE_SHA='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'

class RationalClipped(p.Clipped):
    def __init__(self,s):
        assert isinstance(s,F) and 0<s<2*p.m.B
        self.pi=arb.pi();self.b=p.m.a(p.m.B);self.shift=p.m.a(s)
        # Rational subtraction FIRST preserves the exact endpoint zero.
        self.right=p.m.a(p.m.B-s);self.tables={};self.negative={}
    def primitives(self,power,kind,f,x,which):
        # Every regularized primitive is normalized to vanish at zero.
        # Never evaluate the separate Ci/log or 1/x expressions there.
        if x==0:return acb(0)
        return super().primitives(power,kind,f,x,which)

def main():
    args=argparse.ArgumentParser();args.add_argument('--certificate',required=True)
    args.add_argument('--output',default='artifacts/si29_arch_midpoint_node_probe.json');a=args.parse_args()
    raw=Path(a.certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==NATIVE_SHA
    z=json.loads(raw);ctx.prec=z['working_precision_bits'];assert ctx.prec==4096
    assert p.m.flint.__version__=='0.8.0'
    nodes=[(F(c),n) for c,n in z['original_source_nodes']]
    features=[(F(c),F(r),d) for c,r,d in z['feature_definitions']]
    assert len(nodes)==107 and sum(n for c,n in nodes)==469 and len(features)==14
    terms=[p.m.source_terms(c,k) for c,n in nodes for k in range(n)]+[p.m.pole_terms()]+[p.m.feature_terms(f) for f in features]
    X=arb_mat([[p.ball(v) for v in row] for row in z['full_physical_projection_coefficient_balls']])
    C=arb_mat([[p.dy(v) for v in row] for row in z['exact_dyadic_feature_transform']])
    Q=arb_mat([[-X[i,j] for j in range(14)] for i in range(470)]+[[arb(int(i==j)) for j in range(14)] for i in range(14)])*C
    kernel=RationalClipped(p.m.B);assert kernel.right==0
    start=time.monotonic()
    p.primitive_series_check(kernel);p.translation_checks(terms,kernel)
    p.feature_series_check(features,terms,kernel)
    print('Exact zero-endpoint primitive and all continuous-feature Taylor checks PASS',flush=True)
    translated=[p.shifted(t,kernel) for t in terms[:470]]
    A=arb_mat(470,484)
    for i in range(470):
        for j in range(i,470):A[i,j]=A[j,i]=p.clipped_gram(terms[j],translated[i],kernel)
        for j in range(470,484):A[i,j]=p.clipped_gram(terms[j],translated[i],kernel)
        if i%100==0:print('Arch midpoint NODE raw row',i,'seconds',round(time.monotonic()-start,1),flush=True)
    k=2*(-kernel.shift/2).exp()/(1-(-2*kernel.shift).exp())
    mixed=-k*(A*Q)
    radius2=sum((p.rat(p.m.dyadic(mixed[i,j].rad()))**2 for i in range(470) for j in range(14)),F(0))
    assert 0<radius2<F(1,10**180)
    epsilon=F(1)
    while epsilon**2/4>=radius2:epsilon/=2
    result=dict(status='DIAGNOSTIC_COMPLETE_ARCH_SHIFT_NODE_NOT_INTEGRAL',native_input_sha256=NATIVE_SHA,
      working_precision_bits=4096,physical_shift=str(p.m.B),exact_right_endpoint='0',
      kernel_weight_ball=p.m.ball(k),raw_original_source_count=470,actual_feature_count=14,
      raw_arch_integrand_node_balls=p.m.balls(mixed),exact_raw_entry_radius_squared=str(radius2),
      coupled_raw_node_midpoint_operator_error_upper=str(epsilon),
      exact_zero_endpoint_regularized_limit_checked=True,independent_all_feature_Taylor_degree=255,
      native_node_elapsed_seconds=time.monotonic()-start,
      source_frame_D_applied=False,arch_integral_computed=False,quadrature_error_certified=False,
      matched_forcing_computed=False,inverse_response_value_certified=False,
      W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print('COMPLETE ARCH SHIFT NODE PROBE PASS; NOT an integral certificate; seconds',round(time.monotonic()-start,1),flush=True)
if __name__=='__main__':main()
