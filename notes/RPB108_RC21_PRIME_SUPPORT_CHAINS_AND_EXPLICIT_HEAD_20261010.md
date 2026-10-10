# RPB108 RC21 — prime support-chain bounds and a 23000-feature head

2026-10-10. Independent route consolidation.
Parent: a974b2925b3775587151e87b71f8de3c5233537b (RC20).
Only research/rpb108-route-consolidation is written.

## Result and scope

The finite interval geometry sharpens the norm bound for every actual
prime translation pair. Their complete summed physical norm allowance
at B=11/10 is

    11029/2640,

and the complete prime-plus-negative-pole allowance is <5.
The native archimedean argument from RC19 then works with cutoff exp(7).

RC20's explicit canonical moment construction now needs only 23000
features and has WHOLE original-form complementary floor

    247/2500 >1/11.

If this actual head has floor >=1/4000 and actual canonical source cross
norm <=1/300, its Schur reserve is >=1223/8892000.
Neither bound is certified. No canonical projection, actual head matrix
or actual source columns are computed in this step.

This is a factor-20 reduction in the sufficient moment count from RC20,
using a new bound on the actual prime operators. The count is an upper
bound from a conservative construction; it is not a necessary rank.
No new whole aperture positivity is claimed.

## Native definitions and attachments

Use the canonical supported logarithmic carrier D_B with physical
inclusion i, Fourier convention exp(-2pi i xi x), and weight
w(xi)=log(e+|xi|). The original canonical operator is A_Q=I+i^*R_B i.
The physical archimedean multiplier is
a_arch(xi)=Re psi(1/4+i*pi*xi)-log pi.
The full Q retains its unbounded physical logarithmic principal part.

CC27 blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482 at CC119
5df347d3808ac3282864a657b7380e0f54bf4daa pins the full native form.
At B=11/10 its active prime powers are 2,3,4,5,7,8,9.
For d=log n, let S_d be the compressed physical translation on
L2(-B,B), extending functions by zero. The prime term is
-c_n(S_d+S_d^*), c_n=Lambda(n)/sqrt(n).
Both orientations and the cross-paired pole moments remain included.

## Exact finite-chain translation norm

Translate the physical interval to (0,L), L=2B. For any displacement d>0,
write each point as x=r+k d with 0<=r<d.
Integration splits into a direct integral over r of finite fibers.
On each fiber S_d+S_d^* is the adjacency matrix of a path:
its entries immediately above and below the diagonal are one.
The number of vertices on any fiber is at most

    m=floor(L/d)+1.

Endpoint fibers of measure zero do not affect the operator estimate.
The direct-integral change of coordinates is unitary, since
integral_0^L |h(x)|^2 dx equals the integral over r of the fiber squared
norm sum. It retains arbitrary complex L2 profiles, not selected packets.

For a path with q vertices, the vectors with entries
sin(j k pi/(q+1)), j=1,...,q, have eigenvalues
2cos(k pi/(q+1)), k=1,...,q; the sine addition identity proves this.
Their distinct eigenvalues provide a complete basis.
Thus the norm is 2cos(pi/(q+1)), increasing in q.
Consequently

    ||S_d+S_d^*||<=2cos(pi/(m+1)).

For m=2,3,4 these norms are respectively 1, sqrt2, and
phi=(1+sqrt5)/2. This improves the uncompressed bound 2.

Fresh 9<exp(L)<10 determines the fiber counts without floating
thresholds: for n=2, 2^3<exp(L)<2^4; for n=3,
3^2<exp(L)<3^3; for each remaining active n,
n<exp(L)<n^2.

| Prime power n | Maximum fiber vertices | Pair norm upper | c_n upper |
| --- | ---: | ---: | ---: |
| 2 | 4 | 13/8 > phi | 1/2 |
| 3 | 3 | 17/12 > sqrt2 | 11/17 |
| 4 | 2 | 1 | 7/20 |
| 5 | 2 | 1 | 161/220 |
| 7 | 2 | 1 | 3/4 |
| 8 | 2 | 1 | 1/4 |
| 9 | 2 | 1 | 11/30 |

The coefficient bounds use fresh log2<7/10, log3<11/10,
log5<161/100, log7<39/20, and rational lower bounds
sqrt2>7/5, sqrt3>17/10, sqrt5>11/5, sqrt7>13/5,
sqrt8>14/5. The coefficient at 8 uses Lambda(8)=log2,
and at 9 uses Lambda(9)=log3.

The triangle inequality across the seven ACTUAL pair operators gives

    prime norm <
      (13/8)(1/2)+(17/12)(11/17)+7/20
      +161/220+3/4+1/4+11/30
      =11029/2640.

This is a lawful upper bound for their joint sum; it does not claim to
compute the joint spectrum or exploit cancellation between different
prime displacements.

## Full signed physical costs

RC17's exact pole decomposition has negative norm
2sinh(B)-2B<179/310 and full norm
2sinh(B)+2B<1543/310.
Therefore the complete nonarchimedean negative allowance is

    11029/2640+179/310=77831/16368<5.

The positive pole component may be discarded in this lower estimate.
Both pole components are retained in the actual operator and source
response. With the inherited archimedean remainder norm <8,
the same improved prime bound additionally gives

    R_B>=-13I,    ||R_B||<18.

These are entire physical remainder bounds, not bounds on just the
chosen finite head. The original signed form has not been altered.

## Native archimedean floor at the reduced cutoff

RC19 proves analytically from the digamma Euler series that

    a_arch(xi)>=-31/5 for all xi,
    a_arch(xi)>=log x-1/x for x=|xi| sufficiently large,

with the latter valid when pi*x>=1/4.
Set T=exp(7), alpha=1/10.
For x>=T, log(e+x)<=log x+3/x, so

    a_arch(xi)-5-alpha*w(xi)
      >=(9/10)log x-5-(13/10)/x>0.

Indeed log x>=7 and x>2 make this larger than
63/10-5-13/20>0.
For x<=T, e+exp(7)<exp(8), giving w(xi)<8.
The global multiplier floor then gives

    a_arch(xi)-5-alpha*w(xi)>=-31/5-5-8/10=-12.

Including the entire nonarchimedean lower budget proves

    A_Q >=(1/10)I_D -12 J_T^*J_T,                  (1)

where J_T restricts Fourier(i h) to (-T,T).
This original-form inequality holds on the smooth core and extends by
bounded canonical form continuity. No original positivity is assumed.

## Explicit 23000-feature canonical head

Define physical moment functionals
ell_k(h)=integral x^k (i h)(x)dx and their CANONICAL Riesz
representatives r_k. They are bounded since ||i||<=1.
Let n=23000 and let P project canonically onto
span{r_0,...,r_(n-1)}. Put H=I-P.
This is an explicit mathematical feature space, not a physical
polynomial projection and not a computed canonical basis.

As in RC20, the n-term Fourier--Taylor map X_n satisfies

    ||J_T-X_n||<=2sqrt(BT)(2pi BT)^n/n!,
    X_n H=0.

Fresh rational bounds exp(7)<1100 and e<11/4 give
BT<1210 and

    3(2pi BT)<(132/7)*1210<23000=n.

The factorial estimate n!>=(n/e)^n yields

    (2pi BT)^n/n! <(11/12)^n
                  <=(11/12)^128<1/40000.

Also 2sqrt(BT)<70. Thus the ENTIRE low-band residual is

    ||J_T H||<70/40000<1/100.

Applying (1) proves

    D:=H A_Q H >=[1/10-12/10000]I_H
                 =(247/2500)I_H.                 (2)

No finite complementary sampling replaces this bound.
The head rank is at most n=23000. No Riesz vectors, canonical projection,
Gram matrix, finite head entries or source columns are instantiated.

## Actual head and source-residual obligations

Let G=P A_Q P and Z=H A_Q P=H i^*R_B i P.
The actual residual includes all archimedean remainder, prime and signed
pole channels. The lower envelope (1) is not used as their substitute.

For certified G>=m I_P and ||Z||<=beta, (2) gives

    G-Z^*D^(-1)Z >=[m-beta^2/(247/2500)]I_P.

At m=1/4000, beta=1/300,

    beta^2/(247/2500)=1/8892,
    m-1/8892=1223/8892000>0.

The exact bounded Schur factorization would then certify original
whole positivity at B=11/10. These actual head and source bounds remain
open. RC18's column-error certificate is available only after constructing
a canonical orthonormal basis for THIS head and its actual sources.
Bounds for different heads require a rigorous metric/projection conversion.

## Computational boundary and validation

The complete support-chain bound resolves a genuine loss in the
unsigned prime allowance. The analytic Fourier cutoff falls from exp(10)
to exp(7), and the sufficient moment count from 460000 to 23000.
No claim is made that any actual matrix spectrum improves by those ratios.

This size is substantially smaller but still requires considerable
computation and certified canonical metric construction.
High-degree raw moments can be badly conditioned. A stable equivalent
basis and rigorous whole-source errors remain necessary; no stable
implementation or actual certificate is supplied here.

scripts/validate_rpb108_rc21_prime_chain_head.py passes 30 exact rational
checks: cap thresholds, coefficient and radical enclosures, path norm
bounds, complete signed physical budgets, reduced cutoff, explicit
rank and low-band residual, whole-tail floor, conditional Schur reserve
and unsafe block control. The direct-integral, path-spectrum and
whole-complement proofs are analytic arguments above, not sampled
operator spectra.

No actual head or source residual is evaluated. No original negative
vector, new whole aperture positivity, RH/F4 theorem or Lean closure
is claimed. Existing 1.06 positivity and prior restricted theorems
remain intact. Other branches and historical files are unchanged.
