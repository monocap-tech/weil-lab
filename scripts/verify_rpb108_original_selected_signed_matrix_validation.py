#!/usr/bin/env python3
"""Independent one-variable Cauchy validation of the coincident mixed (13,13) jet."""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from flint import arb,acb,ctx
from verify_rpb108_original_signed_bivariate_kernel import TwoKernel

def dy(x):
 n,e=x.man_exp();return [str(n),int(e)]
def ball(x):return [dy(x.mid()),dy(x.rad())]
def cb(x):return [ball(x.real),ball(x.imag)]
def main():
 p=argparse.ArgumentParser();p.add_argument('--matrix',required=True);p.add_argument('--output',required=True);a=p.parse_args();raw=Path(a.matrix).read_bytes();z=json.loads(raw);assert z['selected_rank']==242 and z['maximum_required_I_jet_order']==27
 start=time.monotonic();t=TwoKernel(3072,384);k=t.k;c=F(37,64);v0=t.frequency(c);v,A,I=k.functions(v0,14);grids=t.block(c,c,14,14);wanted=sum((g[13][13] for g in grids),acb(0))*factorial(13)**2
 # The COMPLETE physical form is analytic in both compactly supported
 # frequency parameters. On each radius1/4 disk, |u|<3/2, |u'|<6.
 B=F(11,10);Nu=2*B*F(3,2)**2;Aou=36*Nu+8*F(3,2)**2+8*B*B*6**2
 M=10**8;majorant=Aou+39*Nu;assert majorant<M
 N=256;r=F(1,8);R=F(1,4);total=acb(0);points=[]
 for j in range(N):
  angle=2*k.I*k.pi*j/N;omega=angle.exp();phase=(-13*angle).exp();mu=v0+acb(str(r))*omega;Am,Im=k.point(mu);parts=k.mixed(v,A,I,mu,Am,Im)
  val=sum((x[13] for x in parts),acb(0))*factorial(13);total+=val*phase
  points.append(dict(index=j,omega=cb(omega),phase=cb(phase),value=cb(val)))
  assert time.monotonic()-start<90,'bounded independent mixed Cauchy guard'
 estimate=total/N/acb(str(r))**13*factorial(13)
 alias=F(M)*R**-26*factorial(13)**2*(r/R)**N/(1-(r/R)**N)
 assert (estimate-wanted+acb(arb(0,arb(str(alias))),arb(0,arb(str(alias))))).contains(0)
 out=dict(status='CONDITIONAL_COINCIDENT_MIXED_ORDER13_CAUCHY_VALIDATION',matrix_sha256=hashlib.sha256(raw).hexdigest(),working_precision_bits=3072,Laplace_terms=384,source_center='37/64',source_order=13,target_order=13,Cauchy_nodes=N,Cauchy_radius=str(r),analytic_radius=str(R),analytic_bivariate_majorant=M,analytic_bivariate_composed_upper=str(majorant),circle_sine_norm_upper=str(Nu),circle_sine_Ao_upper=str(Aou),derivative_alias_upper=str(alias),points=points,Cauchy_estimate=cb(estimate),coincident_mixed_jet=cb(wanted),global_domain_proved=False,W_ODD_NEG='OPEN',elapsed_seconds=time.monotonic()-start)
 Path(a.output).write_text(json.dumps(out,separators=(',',':'))+'\n');print('INDEPENDENT mixed (13,13) Cauchy PASS; alias',float(alias),'seconds',round(time.monotonic()-start,2),flush=True)
if __name__=='__main__':main()
