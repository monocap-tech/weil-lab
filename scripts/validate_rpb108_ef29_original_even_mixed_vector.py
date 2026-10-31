#!/usr/bin/env python3
"""EF29 genuine original 471-vector mixed source, modulo the native c0 row.

EF28 real-even compact disjoint 471-bell basis phi_l, l=1..471,
x_l=l/512, radius r=1/8192. First native SI10 even source:
e=1_I cos(omega*x), omega=2*pi*(37/64), I=[-11/10,11/10].

Define Htilde: 469 true SI10 source moments + original cosh pole.
g_l=q0(e,phi_l), ORIGINAL signed 7-prime + digamma mixed.
The exact original k=0 source row is h0_l=<cos omega*x,phi_l>.
We calculate EXACTLY the equivalent projected vector

  gtilde = g - a_arch(c0)*h0
         = gprime_inside + garch_cut

because h0 is a row of Htilde, so for ANY real Htilde,
P_ker Htilde gtilde=P_ker Htilde g and residual δ is IDENTICAL.
The true original digamma arch kernel gives
 garch_cut,l = 2 Sum_{m>=0} Re[e^(i omega B)/(lambda_m-i omega)]
    e^(-lambda_m B) J_r(lambda_m) cosh(lambda_m x_l),
 lambda_m=2*m+1/2, original exact quarter-digamma, with
 J_r(lambda) the same physical cosine-six Laplace transform.
The true signed arithmetic prime inside is
 gprime_l=-Sum_{n=2,3,4,5,7,8,9} w_n bhat_r(c0)
   [Ipos*cos(omega*(ln n+x_l))+
    Ineg*cos(omega*(ln n-x_l))],
with exact original physical source cutoff flags and NO partial bells.

Outward 340-decimal integer interval evaluation uses SI06 exact ln,
sqrt and pi, EF24 Taylor trig, EF26 outward exp. The m=0..99 arch
tail is uniformly bounded by 10^-19 in EACH coordinate, rigorously
and independent of original Htilde matrix conditioning.

The script also encloses original SOURCE DIAGONAL PRIME PART A_prime
by an exact overlap elementary integral, and checks true k=0
sampled source frequency aliases modulo integer 512.

The actual 470x471 moment matrix, its rank/conditioning, δ and
arch diagonal A_arch are NOT COMPUTED; Schur/odd/Weil/RH OPEN.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import sys,json

from validate_rpb108_si06_negative_band import B, ACTIVE, ln_bounds
from validate_rpb108_ef28_pole_neutral_moment_kernel import (
    original_source_and_geometry,GRID,R,D,COUNT,TOTAL_ROWS
)
from validate_rpb108_ef24_original_even_edge_intervals import (
    I,S,PI,D as DIGITS,trig_pi,source_sqrt,as_i
)
from validate_rpb108_ef26_original_even_arch_laplace import (
    epos,eneg,sinh_i
)

ROOT=Path(__file__).resolve().parents[1]
C0=F(37,64)
OMEGA=2*PI*C0
LAMBDA_COUNT=100
TAIL=F(1,10**19)
assert COUNT==471 and TOTAL_ROWS==470
NS=tuple(sorted(ACTIVE))
assert NS==(2,3,4,5,7,8,9)

def exp_minus(t):
    """Safe EF26 high-precision exp for 0<=t<250 by exact 8th power."""
    t=as_i(t)
    assert 0<=t.lo<=t.hi<250*S
    z=eneg(t/8)
    for _ in range(3):
        z=z*z
    assert z.lo>=0
    return z

def bell_J(lam):
    lam=as_i(lam)
    y=lam*R/PI
    den=I(S)
    for k in (1,2,3):
        den=den*(y*y+k*k)
    out=F(45,2)*sinh_i(lam*R)/(lam*den)
    assert out.lo>0
    return out

def bell_hat_c0():
    # TRUE native EF28 b_r real Fourier, not EF24's smaller-r bell.
    q=2*R*C0
    _,sin=trig_pi(q)
    qi=I.rational(q)
    den=I(S)
    for k in (1,2,3):
        den=den*(qi*qi-k*k)
    out=-F(45,2)*R*sin/(PI*qi*den)
    assert out.lo>0
    return out

def exact_original_cutoff_flags():
    # Original T_{ln n}e(x)=e(x+ln n). For ALL original basis bells,
    # the LOWER source edge -B-ln(n) lies left of every lobe;
    # only upper edge U=B-ln(n) can matter.
    logs={n:ln_bounds(n,terms=450) for n in NS}
    xs=[F(j,512) for j in range(1,COUNT+1)]
    flags={}
    nearest={}
    for n in NS:
        lo,hi=logs[n]
        assert -B-lo < -xs[-1]-R
        upperlo,upperhi=B-hi,B-lo
        plus=[];minus=[]
        mindist=None
        for j,x in enumerate(xs,1):
            for sign,target in ((1,plus),(-1,minus)):
                center=sign*x
                if center+R<upperlo:
                    target.append(j)
                    gap=upperlo-(center+R)
                elif center-R>upperhi:
                    gap=(center-R)-upperhi
                else:
                    raise AssertionError(("partial original cutoff",n,j,sign))
                mindist=gap if mindist is None else min(mindist,gap)
        flags[n]=(set(plus),set(minus))
        nearest[n]=mindist
    counts={n:(len(p),len(q)) for n,(p,q) in flags.items()}
    assert counts=={
        2:(208,471),3:(0,471),4:(0,325),5:(0,211),
        7:(0,38),8:(0,0),9:(0,0)
    },counts
    assert all(margin>R/4 for margin in nearest.values())
    return flags,logs,nearest

def source_alias_scan(centers):
    # Exact frequency grid aliases of the k=0 cosine source rows:
    # cos[2*pi*c*j/512] identical for c'=±c (mod 512).
    aliases=[]
    for i,a in enumerate(centers):
        for j in range(i+1,len(centers)):
            b=centers[j]
            if ((a-b)/512).denominator==1:
                aliases.append((i,j,str(a),str(b),"difference"))
            if ((a+b)/512).denominator==1:
                aliases.append((i,j,str(a),str(b),"reflection"))
    return aliases

def source_weights_and_phases(logs):
    # Native original weights w_n=(ln p)/sqrt n, n=p^k.
    # They MUST NOT be mistaken for ln(n)/sqrt(n).
    lnprimes={p:ln_bounds(p,terms=450) for p in set(ACTIVE.values())}
    weights={}
    phases={}
    for n in NS:
        weights[n]=I.rational_bounds(*lnprimes[ACTIVE[n]])/source_sqrt(n)
        phases[n]=trig_pi(2*C0*I.rational_bounds(*logs[n]))
        assert weights[n].lo>0
    return weights,phases

def signed_original_prime_vector(flags,logs,hat):
    weights,phases=source_weights_and_phases(logs)
    step=(trig_pi(2*C0*GRID))
    z=(I(S),I(0))
    out=[I(0) for _ in range(COUNT)]
    source_row=[I(0) for _ in range(COUNT)]
    cstep,sstep=step
    for j in range(1,COUNT+1):
        c,s=z
        cnew=c*cstep-s*sstep
        snew=c*sstep+s*cstep
        z=(cnew,snew)
        c,s=z
        source_row[j-1]=hat*c
        value=I(0)
        for n in NS:
            p,nm=flags[n]
            if j not in p and j not in nm: continue
            cn,sn=phases[n]
            whole=I(0)
            if j in p:whole=whole+cn*c-sn*s
            if j in nm:whole=whole+cn*c+sn*s
            value=value-weights[n]*hat*whole
        out[j-1]=value
    assert len(out)==COUNT
    return out,source_row,weights

def signed_original_arch_mod_source():
    # Original EF26 digamma identity, but WITHOUT 469-FIR Lambda.
    # This garch_cut differs from the genuine q_arch(e,phi_l)
    # ONLY by a_arch(c0)*h0_l, an EXACT included SI10 source row.
    theta_c,theta_s=trig_pi(2*B*C0)
    phase=I(0)
    out=[I(0) for _ in range(COUNT)]
    for m in range(LAMBDA_COUNT):
        lam=F(2*m)+F(1,2)
        lam_i=I.rational(lam)
        real=(lam_i*theta_c-OMEGA*theta_s)/(lam_i*lam_i+OMEGA*OMEGA)
        # e^-lambda B is tiny but still representable in radix 10^340.
        amp=2*real*bell_J(lam_i)*exp_minus(lam_i*B)
        zp=epos(lam_i*GRID)
        zm=I(S)/zp
        xplus=I(S);xminus=I(S)
        for j in range(COUNT):
            xplus=xplus*zp
            xminus=xminus*zm
            out[j]=out[j]+amp*(xplus+xminus)/2
    # The original physical gap B-x_max-r is >17/100.
    gap=B-F(COUNT,512)-R
    assert gap>F(17,100)
    lam0=F(2*LAMBDA_COUNT)+F(1,2)
    assert lam0*F(17,100)>34
    # e^34>1e14 by a 70-term exact rational partial sum.
    exp34=sum((F(34)**k/factorial(k) for k in range(71)),F(0))
    assert exp34>10**14
    # For all x_l and each m>=100, terms <=(5r/4) exp(-lambda gap)/lambda.
    # exp(-2gap) <=1/(1+2gap)<1/(1+34/100).
    # Hence 1/(1-exp(-2gap))<4, and all 471 uniform tails:
    tail_ub=F(5,4)*R*F(1,10**14)*4/lam0
    assert tail_ub<TAIL
    signed=[I(x.lo-I.rational(TAIL).hi,x.hi+I.rational(TAIL).hi) for x in out]
    return signed,tail_ub

def source_diagonal_prime(weights,logs):
    # EXACT original physical same source e=1_I cos(omega x).
    # I_n=<e,T_ln n e> =
    # [(2B-ln n)/2]cos(omega ln n) +
    # sin[omega(2B-ln n)]/(2omega).
    # A_prime=-2 sum_n (ln p)/sqrt(n) I_n.
    a=I(0)
    for n in NS:
        L=I.rational_bounds(*logs[n])
        overlap=((2*B-L)*trig_pi(2*C0*L)[0])/2
        overlap=overlap+trig_pi(2*C0*(2*B-L))[1]/(2*OMEGA)
        assert (2*B-L).lo>0
        a=a-2*weights[n]*overlap
    return a

def run():
    m=json.loads((ROOT/"research/obligations.json").read_text())
    obs={v["id"]:v for v in m["obligations"]}
    assert m["active_obligation"]=="W-EVEN-FORM"
    assert all(obs[k]["status"]=="open" for k in ("W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert "EF29" in obs["W-EVEN-FORM"]["evidence"]
    centers,orders,xs=original_source_and_geometry()
    flags,logs,margin=exact_original_cutoff_flags()
    alias=source_alias_scan(centers)
    hat=bell_hat_c0()
    prime,h0,weights=signed_original_prime_vector(flags,logs,hat)
    arch,tail=signed_original_arch_mod_source()
    reduced=[x+y for x,y in zip(prime,arch)]
    aprime=source_diagonal_prime(weights,logs)
    assert len(reduced)==len(h0)==471
    print("EF29 genuine original 471 original signed mixed vector",
          "MODULO first source row h0, n_source 469, pole row 1;"
          " true δ=||Pker H gtilde|| exactly, NOT YET COMPUTED.",flush=True)
    print("EF29 EXACT native original prime cutoff counts:",
          {n:(len(flags[n][0]),len(flags[n][1])) for n in NS},
          "all 7 prime cutoffs have zero partially clipped bells;",
          "smallest exact source separation:",float(min(margin.values())),flush=True)
    print("EF29 original seven-prime source n8 and n9 vanish"
          " on ALL 471 bells; other n retained with exact"
          " full-bell signs and original w=(ln p)/sqrt(n).",flush=True)
    print("EF29 genuine original first-source A_prime interval:",
          aprime.scaled(),"A_arch and full A STILL UNCOMPUTED.",flush=True)
    print("EF29 exact native k0 source-grid frequency aliases:",
          len(alias),"examples:",alias[:12],
          "(an alias implies k0 row-dependence, NOT automatically"
          " full finite source rank deficiency).",flush=True)
    print("EF29 arch original Laplace cutoff vector 100 terms each,"
          " TRUE uniform all-471-coordinate absolute tail <",
          str(tail),"and",TAIL,"source row difference exactly"
          " a_arch(c0)*h0 in the true 470-row H.",flush=True)
    for j in (1,147,208,209,261,434,471):
        print("EF29 original source j",j,
              "gprime",prime[j-1].scaled(),
              "garch_cut",arch[j-1].scaled(),
              "gtilde",reduced[j-1].scaled(),flush=True)
    if "--output" in sys.argv:
        loc=Path(sys.argv[sys.argv.index("--output")+1])
        loc.parent.mkdir(parents=True,exist_ok=True)
        payload={
            "scope":"EF29 original signed q0 first source mixed MODULO h0; not finite Schur residual",
            "source":"SI06 seven primes plus original digamma EF26, SI10 native 107/469",
            "digits":DIGITS,
            "vector_count":COUNT,"rows":TOTAL_ROWS,
            "tail_abs_upper_rational":str(tail),
            "prime_diagonal_A_prime_interval":[str(aprime.lo),str(aprime.hi)],
            "scale":str(S),
            "aliases":alias,
            "cutoff_counts":{str(n):[len(flags[n][0]),len(flags[n][1])] for n in NS},
            "vector_original_projected_signed_intervals":[
                [str(z.lo),str(z.hi)] for z in reduced],
            "original_prime_intervals":[[str(z.lo),str(z.hi)] for z in prime],
            "original_arch_cutoff_intervals":[[str(z.lo),str(z.hi)] for z in arch],
            "original_h0_source_row":[[str(z.lo),str(z.hi)] for z in h0]
        }
        loc.write_text(json.dumps(payload,indent=1)+"\n")
        print("EF29 original signed source interval vector output:",loc,
              "not a computed δ or Schur sign.",flush=True)
    print("EF29 SCOPE STOP: original 470x471 SI10 moment matrix H"
          " not numerically constructed/enclosed; δ, σ_min,"
          " and A_arch not evaluated, no corrected even Schur sign,"
          " odd/whole Weil/RH OPEN.",flush=True)

if __name__=="__main__":
    run()
