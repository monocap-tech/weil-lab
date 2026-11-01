#!/usr/bin/env python3
"""EF39 source-original signed 40-mode arch/primes/pole L2 Gram.
Original SI10 first row only; entire infinite arch tail paid.
No 469D projection, full Schur sign, or RH theorem.
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
from validate_rpb108_si06_negative_band import B

ROOT=Path(__file__).resolve().parents[1]
N=40
MU=F(17,25000)

def endpoint_mode(x,c,s,ep,em,lam):
    li=I.rational(lam)
    plus=exp_minus(li*(I.rational(B)-x))
    minus=exp_minus(li*(I.rational(B)+x))
    sh=(plus-minus)/2
    ch=(plus+minus)/2
    den=li*li+OMEGA*OMEGA
    jc=(li*sh*c+OMEGA*ch*s)/den
    js=(li*sh*s-OMEGA*ch*c)/den
    t1=(plus*ep-minus*em)/(li+F(1,2))
    if lam==F(1,2):
        t2=2*x*exp_minus(li*B)
    else:
        t2=(plus*em-minus*ep)/(li-F(1,2))
    return jc,js,(t1+t2)/4

def run_source():
    zsq,s0,ze,_,_,_=original_source_project_one_exact_row()
    cells,_=full_original_prime_cells()
    _,u=original_even_pole_diagonal()
    k=2*u
    epnts=[cells[0][0]]+[v[1] for v in cells]
    assert len(epnts)==9 and epnts[-1].lo==B*S
    pt=[]
    for x in epnts:
        c,s=trig_pi(2*C0*x)
        ep=epos(x/2)
        pt.append((x,c,s,ep,I(S)/ep))
    pc,ps=trig_pi(2*B*C0)
    lams=[];coeff=[];E=[]
    cross=I(0);he=I(0)
    for m in range(N):
        lam=F(2*m)+F(1,2)
        li=I.rational(lam)
        a=2*(li*pc-OMEGA*ps)/(li*li+OMEGA*OMEGA)
        lams.append(lam);coeff.append(a)
        E.append(exp_minus(I.rational(2*lam*B)))
        prim=[endpoint_mode(*point,lam) for point in pt]
        he+=2*a*(prim[-1][0]-prim[0][0])
        mixed=I(0)
        for j,(_,__,p,q,flags) in enumerate(cells):
            a0,a1=prim[j],prim[j+1]
            mixed+=p*(a1[0]-a0[0])+q*(a1[1]-a0[1])+k*(a1[2]-a0[2])
        cross+=2*a*mixed
    hsq=I(0)
    for i in range(N):
        li,ai,Ei=lams[i],coeff[i],E[i]
        for j in range(i,N):
            lj,aj,Ej=lams[j],coeff[j],E[j]
            if i==j:
                G=(I(S)-Ei*Ei)/(4*li)+B*Ei
                mult=1
            else:
                G=(I(S)-Ei*Ej)/(2*(li+lj))+(Ej-Ei)/(2*(li-lj))
                mult=2
            hsq+=mult*ai*aj*G
    assert hsq.lo>0
    full=zsq+2*cross+hsq
    projected=full-(ze+he)*(ze+he)/s0
    assert projected.lo>0
    assert F(projected.hi,S)<F(1,15), projected.scaled()
    return projected,full,cross,he,hsq

def original_tail():
    lam=F(2*N)+F(1,2)
    power=F(57,500)
    assert F(1,2*N-F(3,2))<power*power
    en=exp_minus(I.rational(lam*B))
    assert en.hi<S//10**20
    exp_upper=F(11,5)*F(1,10**20)*F(1,lam)*F(16,11)
    assert exp_upper<F(1,10000)
    assert F(259,1000)**2>F(1,15)
    assert F(259,1000)+power+exp_upper<F(3,8)
    assert (F(3,8)**2)/MU==F(28125,136)
    return power+exp_upper

def main():
    data=json.loads((ROOT/'research/obligations.json').read_text())
    obs={x['id']:x for x in data['obligations']}
    assert data['active_obligation']=='W-EVEN-FORM'
    assert 'EF38' in obs['W-EVEN-FORM']['evidence']
    assert all(obs[x]['status']=='open' for x in ('W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    proj,full,cross,he,hsq=run_source()
    tail=original_tail()
    print('EF39 original signed <z,h40>:',cross.scaled(),flush=True)
    print('EF39 original arch <h40,e>:',he.scaled(),
          'true 40x40 arch L2 Gram:',hsq.scaled(),flush=True)
    print('EF39 original full signed z+h40 L2 squared:',full.scaled(),
          'one genuine protected SI10 row projected squared:',proj.scaled(),
          '<1/15',flush=True)
    print('EF39 complete original remaining infinite arch L2 tail <',
          float(tail),'true cofinite source projection norm <3/8,'
          'energy dual eta <28125/136 =',float(F(28125,136)),flush=True)
    print('EF39 original 469-source full projected residual and'
          ' full even Schur, odd, Weil, RH OPEN; original Fourier'
          ' and form-domain audit independent.',flush=True)

if __name__=='__main__':
    main()
