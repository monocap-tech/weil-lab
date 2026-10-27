#!/usr/bin/env python3
"""Independent scalar physical and Cauchy-coefficient validations of local jets."""
import argparse,json,time,hashlib
from math import factorial
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb,acb_series,ctx
from verify_rpb108_original_signed_frequency_kernel import Kernel
import verify_rpb108_original_two_ray_signed_physical as reference
def dy(x):
    n,e=x.man_exp();return [str(n),int(e)]
def ball(x):return [dy(x.mid()),dy(x.rad())]
def cb(x):return [ball(x.real),ball(x.imag)]
def main():
    p=argparse.ArgumentParser();p.add_argument('--column',required=True);p.add_argument('--output',default='artifacts/original_signed_kernel_validation.json');args=p.parse_args();start=time.monotonic()
    z=json.load(open(args.column));k=Kernel();v0=acb(2*k.pi*37/64)
    ss=k.diagonal(v0);pp=tuple(-x for x in k.diagonal(k.pole))
    A0,I0=k.point(v0);Ap,Ip=k.point(k.pole);ctx.cap=1
    sp=tuple(-k.I*x[0] for x in k.mixed(acb_series([v0]),acb_series([A0]),acb_series([I0]),k.pole,Ap,Ip))
    cases=[]
    for a,b in [(1,0),(0,1),(1,1)]:
        direct=reference.signed_form(a,b)
        pieces=[a*a*ss[j]+2*a*b*sp[j]+b*b*pp[j] for j in range(3)]
        original=[direct['arch'],direct['prime'],-2*direct['pole']**2]
        assert all((x.real-y).contains(0) and x.imag.contains(0) for x,y in zip(pieces,original))
        cases.append(dict(sine=a,pole=b,kernel_components=[ball(x.real) for x in pieces],direct_physical_components=[ball(x) for x in original]))
    # A priori analytic disk majorant for F(nu)=Q(sin(nu*x),fixed_probe).
    B=F(11,10);a=list(map(F,z['target_probe']['sine_coefficients']));b=F(z['target_probe']['sinh_coefficient']);cs=list(map(F,z['target_sine_frequencies']))
    S=sum(map(abs,a),F(0))+F(3,5)*abs(b);D=F(44,7)*sum((abs(x)*c for x,c in zip(a,cs)),F(0))+F(3,5)*abs(b)
    Nf=2*B*S*S;Vf=8*S*S+8*B*B*D*D;Aof=36*Nf+Vf
    Nu=2*B*F(3,2)**2;Vu=8*F(3,2)**2+8*B*B*6**2;Aou=36*Nu+Vu
    assert F(44,7)*F(37,64)+F(1,4)<4 and 1/(1-B/4)<F(3,2)
    majorant=(Aof+Aou)/2+F(39,2)*(Nf+Nu);M=F(10**8);assert majorant<M
    # For a fixed small complex-frequency disk the COMPLETE physical form is
    # entire. Cauchy aliasing gives a rigorous 256-point coefficient error.
    target=[]
    for c,coef in zip(cs,a):
        mu=acb(2*k.pi*arb(str(c)));Am,Im=k.point(mu);target.append((mu,acb(str(coef)),Am,Im))
    Am,Im=k.point(k.pole);target.append((k.pole,-k.I*acb(str(b)),Am,Im))
    N=256;r=F(1,8);R=F(1,4);order=13;values=[];total=acb(0)
    for j in range(N):
        angle=2*k.I*k.pi*j/N;omega=angle.exp();phase=(-order*angle).exp();nu=v0+acb(str(r))*omega
        An,In=k.point(nu);ctx.cap=1;value=acb(0)
        for mu,coef,Am,Im in target:
            pieces=k.mixed(acb_series([nu]),acb_series([An]),acb_series([In]),mu,Am,Im)
            value+=coef*sum((x[0] for x in pieces),acb(0))
        assert abs(value)<arb(str(M));total+=value*phase
        values.append(dict(index=j,omega_native=cb(omega),inverse_phase_native=cb(phase),mixed_value_native=cb(value)))
        assert time.monotonic()-start<60,'bounded 60-second independent Cauchy validation guard'
    estimate=total/(N*acb(str(r))**order)*factorial(order)*(-1)**(order//2)
    alias=M/R**order*(r/R)**N/(1-(r/R)**N)*factorial(order)
    row=next(x for x in z['rows'] if x['original_source_index']==13)
    interval=list(map(F,row['entries'][0]['signed_interval']))
    assert (estimate.real+arb(0,arb(str(alias)))-arb(str((interval[0]+interval[1])/2),arb(str((interval[1]-interval[0])/2)))).contains(0)
    out=dict(status='CONDITIONAL_SIGNED_KERNEL_PHYSICAL_AND_CAUCHY_VALIDATION',column_sha256=hashlib.sha256(Path(args.column).read_bytes()).hexdigest(),working_precision_bits=512,anchor_cases=cases,Cauchy_order=order,Cauchy_nodes=N,Cauchy_radius=str(r),analytic_radius=str(R),analytic_majorant=str(M),analytic_majorant_composed_upper=str(majorant),
      source_probe_amplitude_upper=str(S),source_probe_derivative_amplitude_upper=str(D),source_probe_norm_upper=str(Nf),source_probe_Ao_upper=str(Aof),circle_sine_norm_upper=str(Nu),circle_sine_Ao_upper=str(Aou),
      Cauchy_points=values,Cauchy_derivative_estimate_native=cb(estimate),Cauchy_derivative_alias_error_upper=str(alias),compared_column_original_source_index=13,
      compared_column_target_index=0,global_mixed_or_inverse_bound_certified=False,W_ODD_NEG='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('INDEPENDENT PHYSICAL/Cauchy VALIDATION PASS: three full original anchor combinations, native 256-point order13 coefficient check; seconds',round(out['elapsed_seconds'],2))
if __name__=='__main__':main()
