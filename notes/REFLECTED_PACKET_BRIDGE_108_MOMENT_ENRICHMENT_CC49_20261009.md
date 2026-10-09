# RPB108 CC49 — Exact moment enrichment removes the tiny-beta division

Date: 2026-10-09 UTC. Publication base b420910c5edcdccbe637edbfde83f487447d2254.
Fresh integration base88611389e831d808c2b7df11d6581d0beefb7303 preserves NF16's concurrent E96/complement handoff.
[Definitions](../docs/TERMINOLOGY_RPB108_MOMENT_ENRICHMENT_CC49.md).
This reformulates CC47's invisible-null gate using the actual pole profiles.
It does not evaluate its native sign or strengthen the whole-positive anchor.

## 1. A complementary split with identically zero high moments

At B=53/50 let E=E112. In each real parity sector set

    Eplus=E+span{w}, Fplus=D intersect Eplus-perp,
    Z=Eplus intersect ker m, m(h)=<w,h>_physical,             (1)

where w is the supported cosh or sinh profile. These profiles are in D:
they are smooth on the cap, and their zero extensions are bounded variation
with O(1/|xi|) Fourier tails, integrable in logarithmic energy. CC48 proves
their physical F112 projections are nonzero. Thus Eplus has57 dimensions
per parity (114 overall), and Z has56 dimensions per parity.

Importantly Fplus is a SUBSPACE of F112. The established original bound

    Q(y)>=17/100 ||y||_2^2, y in F112,

therefore holds on Fplus without a perturbation argument. Physical
proximity of projections is not invoked for an unbounded logarithmic form.
The fresh NF16 handoff strengthens the same original F112 bound to207/1000;
this stronger value transfers identically to Fplus and may be used in (3).
By construction m|Fplus=0 exactly; this is CC47's legitimate beta=0 case,
not a numerical approximation to CC48's strictly positive old beta.

Every original moment-zero h decomposes physically as h=z+y, z in Z,
y in Fplus. Neither its finite nor high part carries a pole moment.
Hence Q=H on the entire constrained carrier and in every mixed pairing
used for its gate. The poles have not been omitted from a general vector;
their vanishing follows from the EXACT moment constraint.

## 2. Ordinary signed form Schur gate on Z

Put Cplus=Q|Fplus=H|Fplus. By CC47's norm equivalence this is a complete
coercive form Hilbert space. Define Wplus by

    Cplus(Wplus z,y)=H(z,y) for every y in Fplus.

Then

    Q(z+y)=K_Z(z)+Cplus(y+Wplus z),
    K_Z(z)=H(z,z)-Cplus(Wplus z,Wplus z).                    (2)

Strict finite positivity of K_Z is equivalent to a physical coercive
floor on the full moment-zero sector, with the known high lower17/100.
For example if K_Z>=sigma||z||_2^2 and ||Wplus||_physical<=M,
the complete square gives the conservative bound

    Q(h)>=min[sigma/(2(1+M)^2),17/200] ||h||_2^2.           (3)

No division by the tiny old beta appears. All archimedean and prime
coupling remains inside the signed Wplus Gram. Positivity on Z alone
does not imply positivity of K_Z, and this theorem supplies no such sign.
One must certify the complete response and its errors as before.

## 3. The compensated tail cannot be discarded

Write w=e+f with e=Ew, f=Fw, physical norms p=||e||>0, q=||f||>0,
and b=e/p.

Here p>0 because the even moment has nonzero pairing with the constant
Legendre mode, and the odd moment with the linear mode.
A basis decomposition of the actual retained constrained space is

    Z=(E intersect ker m) plus span{t},
    t=f/q-(q/p)b,  m(t)=0.                                  (4)

The sum is physically orthogonal because every old low moment-zero vector
is orthogonal to both e and f. The compensated tail norm is sqrt(1+q^2/p^2).
Although q is tiny, t has physical norm at least1. Omitting t leaves only
55 directions per parity and misses valid constrained vectors.

Computationally, normalizing f by q may still require careful stable
moment-tail evaluation. Enrichment removes the beta division from the
gate; it does not assert that tiny tails are easy to calculate or bound
in the logarithmic norm. Eplus is NOT identical to the first114 Legendre
modes, and no preexisting native E114 certificate is borrowed.

## 4. Exact coordinate and level controls

Consider physical Q on one old low and two high coordinates, with
Q_low=1, C=I, mixed row B=(2,1/3), and moment m=x+epsilon*y1.
Old CC47 data are G=37/9, beta=epsilon^2, a=1-2epsilon.
Enrichment retains e1,e2 and leaves e3 high. Z is spanned by
t=e2-epsilon e1. Its ordinary Schur gate is

    K_Z(t)=1-4epsilon+(8/9)epsilon^2
           =epsilon^2 [1-37/9+(1-2epsilon)^2/epsilon^2].     (5)

The tiny-beta gate and enriched gate are congruent, not numerically equal
under different physical low coordinates. At epsilon=1/10 the gate is
positive, at epsilon=1/2 it is negative. The omitted compensated direction
is precisely where this control can fail; old E intersect ker m is {0}.

Genuine positive-level control: Q_low=2,C=I,B=(1,0), high moment profile
epsilon*e3. Enrichment retains e1,e3, Z=span e1 and high=e2. Its gate is1.
After shifting the WHOLE physical mass by mu=1/2, high C=1/2 and the
gate is3/2-1/(1/2)=-1/2. The original positive eigenlevel
(3-sqrt5)/2 becomes the constrained contact; enrichment does not exclude
genuine crossing or misidentify shifted positivity as original positivity.

The local differential crossing likewise is not ruled out by an exact
coordinate change. Original moment-carrying contacts lie outside ker m
and remain separate arithmetic thresholds.

All19 new exact checks pass: compensated moments, omitted-direction
controls, congruence of gates at rational tail sizes, and the complete
mass-shift algebra. These are not actual native source-response measurements.

## 5. Current frontier

This gives a denominator-free formulation using the actual pole profiles
and preserves NF10's entire high bound by subspace containment. It moves
the missing target to the signed native response Gram on56 constrained
directions per parity, including the compensated tail. NF16 advances the
finite Legendre sign to E96 but leaves16 retained modes before E112 and
does not supply the enriched moment-tail rows or complete response Gram. No target gate
is certified, no moment-zero null is excluded at an unproved cap, and no
uniform defect-relative source-shell estimate follows. Whole-domain
positivity remains21/20; RH/F4, contact exclusion and Lean remain open.
