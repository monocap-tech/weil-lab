# RPB108: concrete actual sources and a posteriori Schur enclosures

## Terminology

A **physical residual certificate** is an L2 enclosure of the actual interior action after removing its physical Legendre degrees 0..63. An **approximate lift** is a specified linear map Z:E to F, replacing the exact complement solution C^(-1)b_e. It does not change the source vector or assert exact nullity.

This chunk uses the actual coercive complement at a=1/2 from `REFLECTED_PACKET_BRIDGE_108_ACTUAL_LEGENDRE_COMPLEMENT_20261005.md`. It constructs concrete polynomial source actions and proves a rigorous residual-to-Schur error bound. Full Schur sign remains unevaluated.

## Explicit actual interior source constructor

Let p be any polynomial on [-a,a], extended by zero, with a=1/2. Put d_-=x+a, d_+=a-x and

K(s)=exp(-s/2)/(1-exp(-2s)),
J(d)=atanh(exp(-d/2))+atan(exp(-d/2)),
c(x)=psi(1/4)-log pi+J(d_-)+J(d_+).

For -a<x<a, the actual archimedean action is

Ap(x)=c(x)p(x)
 - integral_0^(d_-) K(s)[p(x-s)-p(x)] ds
 - integral_0^(d_+) K(s)[p(x+s)-p(x)] ds.

The actual whole interior source is

q_p(x)=Ap(x)
 -(log 2/sqrt 2)[p(x-log 2)+p(x+log 2)]
 +M_-(p)exp(x/2)+M_+(p)exp(-x/2),

where the translated p is its zero extension and the moments are the same supported p. Thus prime cutoff, pole custody and correlations all use the unchanged polynomial source.

To derive the formula, the Euler digamma integral gives

Ap=( -gamma-log pi)p + integral_0^infinity
 [2exp(-2s)p(x)-exp(-s/2)(p(x-s)+p(x+s))]/(1-exp(-2s)) ds.

Subtract p(x) inside the two integrals up to d_- and d_+. Each remaining coefficient equals half of psi(1/4)+gamma plus the tail integral of K beyond its corresponding d. Substitution u=exp(-s/2) shows integral_d^infinity K(s)ds=J(d). This proves the displayed c. The classical duplication/reflection identities give psi(1/4)=-gamma-pi/2-3log 2; equivalently this value follows from the quarter-argument Euler series.

The formula is not an assumed operator-domain attachment. Integration by parts gives Fourier(p)=O(1/|xi|) for the zero-extended polynomial. The actual multiplier is O(log(e+|xi|)), so multiplier times Fourier(p) belongs to L2. The pole is locally L2. Hence the actual interior action is an L2 function and its mixed pairing agrees with Q(p,v) for every v in H. Endpoint jumps are permitted; H1 membership is unnecessary. One may first justify the integral with truncated Euler kernels and then pass by the removable difference at zero and logarithmic endpoint domination.

## Explicit integrability and source bound

For 0<d<=1, 1-exp(-d/2)>=d/4 gives
0<J(d)<=3+(1/2)|log d|. Also |psi(1/4)-log pi|<8. Since the L2 norm of log d on (0,1) is sqrt 2, ||c||_L2<16.

On 0<s<=1, K(s)<=9/(2s), and each polynomial difference is at most s M1, where M1=max |p'|. Their combined integration length is d_-+d_+=1. Thus the archimedean difference contribution has norm at most (9/2)M1. Put M0=max |p|. The prime contribution has norm below M0, since 2log 2/sqrt 2<1. The pole contribution has norm below 8M0, since exp(1/4)<2 and both moments have magnitude below 2M0. Therefore the simple explicit bound

||q_p||_L2 <= 25M0+(9/2)M1 < 26M0+5M1

holds for nonzero p. This supplies concrete residual inputs without invoking a spectral domain or a raw divisor synthesis preimage.

## Rigorous Schur error bound

Use the previous H=E direct-sum F and exact lift z_e=C^(-1)b_e. Let Z:E to F be any specified linear approximate lift for which g_e=e-Ze has an interior physical source q_(g_e) in L2. Polynomial approximate lifts with degrees 64 and above satisfy this by the constructor. Define

r_e=P_F^(physical) q_(g_e),
R(e,e')=<r_e,r_(e')>_(L2),
S_Z(e,e')=Q(g_e,g_(e')).

The physical projection subtracts the first 64 supported Legendre components from the source on [-a,a]. It need not produce a vector in H; it is an L2 source representing a bounded functional on F. For every v in F, Q(g_e,v)=<r_e,v>_(L2).

Set u_e=z_e-Ze. The exact corrected vector e-z_e is Q-orthogonal to F, so Q(u_e,v)=<r_e,v>_(L2). Applying the proved physical complement bound Q(u)>=(1/5)||u||_L2^2 and Cauchy--Schwarz gives

Q(u_e)<=5||r_e||_L2^2.

The exact square completion gives S_Z-S=Q(u_e,u_(e')). Applying the diagonal bound to every linear combination of sources proves the matrix/form enclosure

S_Z-5R <= S <= S_Z.

This is an exact same-vector theorem, not a numerical condition estimate. It also yields ||u_e||_H^2 <= (500/9)||r_e||_L2^2. No density of polynomial trial lifts is assumed.

Consequently a certified nonnegative matrix S_Z-5R establishes Q>=0 on the entire fixed-aperture H, and then the WD-T10 contraction follows by the existing factorization criterion. A strict negative S_Z vector gives the concrete negative source g_e directly. Exact nullity cannot be inferred from a numerical zero band.

If Z is obtained by Galerkin solution in a chosen finite polynomial subspace of F, then Q(e,Ze)=Q(Ze,Ze) and S_Z=Q(e,e')-Q(Ze,Ze'). The residual norm enclosure accounts for all uncomputed complement directions. A projected residual is necessary: counting multiplicity copies does not generate these observations.

## Exploratory constant-source check and remaining input

For p=1, the difference integrals vanish and

q_1(x)=c(x)+8sinh(1/4)cosh(x/2)
 -(log 2/sqrt 2)[1_(x>=log 2-1/2)+1_(x<=1/2-log 2)].

`scripts/explore_native_constant_coupling.py` splits at the two prime discontinuities and uses 512/1024 Gauss nodes per panel. At 1024 nodes, the projected residual squared is approximately 0.001236624 and its fivefold coupling majorant approximately 0.006183120. At 512 nodes the squared residual is approximately 0.001233490. These are uncertified displays with endpoint logarithms; repeated quadrature is not an enclosure. The Q00 display approaches the previously certified finite entry. No Schur sign, even for this scalar direction, is promoted from this pilot.

The actual missing fixed-aperture input is now an explicit arithmetic task: enclose S_Z and the residual Gram R for all 64 sources tightly enough to decide S_Z-5R, or improve the approximate lift. The integrable endpoint logarithms and finite prime jumps must receive rigorous quadrature/error control. This theorem supplies a concrete physical source constructor and error mechanism; it does not claim that those 64 coupled enclosures have been completed.

The global signed endpoint-null Gaussian upper estimate/endpoint exclusion remains independent. Even complete fixed-aperture positivity would not settle every aperture. No retained membership, full graph density, zero simplicity or background positivity is assumed. F4 entry and FULL TRANSPORT CLOSED remain open. Lean source/checkpoint and CI claims are unchanged.
