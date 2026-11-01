#!/usr/bin/env python3
"""EF40 source-native two-row SI10 projection: e and x*sin(omega*x).

These are actual even frequency-jet source rows of original first
SI10 cluster, with order >=2. EF39 provides all 7 real prime/power
signed translated terms, genuine cosh even pole, and original first
40 half-integer arch cutoff terms and their complete signed Gram.
Here exact original 8-cell physical primitives and an exact 2x2
positive Gram certify an additional genuine source projection.
The complete untruncated original arch tail is still paid; this is
NOT the other 467 source directions or an actual cofinite inverse.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_ef24_original_even_edge_intervals import I,S,trig_pi
from validate_rpb108_ef29_original_even_mixed_vector import C0,OMEGA,exp_minus
from validate_rpb108_ef26_original_even_arch_laplace import epos
from validate_rpb108_ef32_even_471_bell_negative_gate_stop import original_even_pole_diagonal
from validate_rpb108_ef37_original_even_correlated_prime_pole import full_original_prime_cells
from validate_rpb108_ef38_original_even_first_protected_row_projection import original_source_project_one_exact_row
from validate_rpb108_ef39_original_even_full_arch_cross_first_row import run_source,original_tail,N
from validate_rpb108_ef28_pole_neutral_moment_kernel import original_source_and_geometry
from validate_rpb108_si06_negative_band import B

ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)
RESID2_CAP=F(29,500)
FULL_CAP=F(9,25)
ETA_CAP=F(3240,17)

def endpoint(x):
    c,s=trig_pi(2*C0*x)
    c2,s2=trig_pi(4*C0*x)
    ep=epos(x/2)
    em=I(S)/ep
    return x,c,s,c2,s2,(ep+em)/2,(ep-em)/2

def z_v_ant(t):
    x,c,s,c2,s2,ch,sh=t
    d=OMEGA*OMEGA+F(1,4)
    jcs=-x*c2/(4*OMEGA)+s2/(8*OMEGA*OMEGA)
    jss=x*x/4-x*s2/(4*OMEGA)-c2/(8*OMEGA*OMEGA)
    fs=(sh*s/2-OMEGA*ch*c)/d
    integ=((F(1,4)-OMEGA*OMEGA)*ch*s-OMEGA*sh*c)/(d*d)
    return jcs,jss,x*fs-integ

def arch_v_ant(t,lam):
    x,c,s,c2,s2,ch,sh=t
    l=I.rational(lam)
    a=exp_minus(l*(I.rational(B)-x))
    b=exp_minus(l*(I.rational(B)+x))
    cc=(a+b)/2
    ss=(a-b)/2
    den=l*l+OMEGA*OMEGA
    fs=(l*ss*s-OMEGA*cc*c)/den
    integ=((l*l-OMEGA*OMEGA)*cc*s-2*l*OMEGA*ss*c)/(den*den)
    return x*fs-integ

def compute():
    centers,orders,_=original_source_and_geometry()
    assert len(centers)==107 and sum(orders)==469
    assert centers[0]==C0 and orders[0]>=2
    # Original k=1 EVEN real Fourier jet: -x*sin(omega*x).
    # Its sign is irrelevant to the span; use +x*sin.
    d1,full,cross,he,hsq=run_source()
    z2,s0,ze,alpha,_,_=original_source_project_one_exact_row()
    cells,_=full_original_prime_cells()
    endpts=[cells[0][0]]+[t[1] for t in cells]
    pts=[endpoint(x) for x in endpts]
    assert len(pts)==9
    _,u=original_even_pole_diagonal()
    k=2*u
    az=[z_v_ant(x) for x in pts]
    zv=I(0)
    for j,(_,__,p,q,flags) in enumerate(cells):
        left,right=az[j],az[j+1]
        zv+=2*(p*(right[0]-left[0])+q*(right[1]-left[1])
               +k*(right[2]-left[2]))
    pc,ps=trig_pi(2*B*C0)
    hv=I(0)
    for m in range(N):
        lam=F(2*m)+F(1,2)
        li=I.rational(lam)
        coeff=2*(li*pc-OMEGA*ps)/(li*li+OMEGA*OMEGA)
        hv+=2*coeff*(arch_v_ant(pts[-1],lam)-arch_v_ant(pts[0],lam))
    cos2B,sin2B=trig_pi(4*C0*B)
    ev=-B*cos2B/(2*OMEGA)+sin2B/(4*OMEGA*OMEGA)
    vv=B**3/3-B*B*sin2B/(2*OMEGA)-B*cos2B/(2*OMEGA*OMEGA)+sin2B/(4*OMEGA**3)
    schur=vv-ev*ev/s0
    assert schur.lo>F(1,4)*S,schur.scaled()
    assert F(schur.hi,S)<F(1,3),schur.scaled()
    b1=ze+he
    b2=zv+hv
    d2c=b2-b1*ev/s0
    gain=d2c*d2c/schur
    residual=d1-gain
    assert residual.lo>0,residual.scaled()
    assert F(residual.hi,S)<RESID2_CAP,(
        'EF40 actual two-row projected source residual',
        residual.scaled(),gain.scaled(),zv.scaled(),hv.scaled())
    tail=original_tail()
    assert RESID2_CAP<F(241,1000)**2
    assert F(241,1000)+F(57,500)+F(1,10000)<FULL_CAP
    assert FULL_CAP**2/MU==ETA_CAP
    return orders[0],zv,hv,ev,vv,schur,gain,residual,tail

def main():
    data=json.loads((ROOT/'research/obligations.json').read_text())
    obs={x['id']:x for x in data['obligations']}
    assert data['active_obligation']=='W-EVEN-FORM'
    assert 'EF39' in obs['W-EVEN-FORM']['evidence']
    assert all(obs[t]['status']=='open' for t in ('W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    order,zv,hv,ev,vv,schur,gain,residual,tail=compute()
    print('EF40 ORIGINAL first SI10 cluster exact source Taylor order',order,
          'includes e=cos and companion x*sin even source jet.',flush=True)
    print('EF40 original full seven-prime plus genuine even pole <z,xsin>:',
          zv.scaled(), 'true 40 arch cutoff cross <h40,xsin>:',
          hv.scaled(),flush=True)
    print('EF40 true original 2x2 physical protected source Gram:'
          ' <e,xsin>=',ev.scaled(),' ||xsin||²=',vv.scaled(),
          ' Schur >1/4:',schur.scaled(),flush=True)
    print('EF40 true second protected row squared projection gain:',
          gain.scaled(),'original 2-row signed response residual squared:',
          residual.scaled(),'<29/500',flush=True)
    print('EF40 full original untruncated arch tail L2 <',float(tail),
          ' original full cofinite projected gradient norm <9/25,'
          ' original unseen eta <3240/17=',float(ETA_CAP),flush=True)
    print('EF40 only 2 of genuine 469 protected source rows projected;'
          ' 467 remain; complete 469D Schur, actual energy inverse,'
          ' full even sign, paused odd, Weil/RH OPEN.'
          ' Independent Fourier/arch source-core audit OPEN.',flush=True)

if __name__=='__main__':
    main()
