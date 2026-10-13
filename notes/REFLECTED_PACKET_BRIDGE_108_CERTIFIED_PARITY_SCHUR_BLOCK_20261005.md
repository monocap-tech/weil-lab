# RPB108: certified actual two-dimensional corrected block

## Terminology and theorem

The **constant-linear corrected block** is the restriction of the exact 64-dimensional Schur form to span{1,2x} inside the low space E at a=1/2. A **parity split** is the even/odd decomposition under reflection x to -x; its mixed form entry vanishes by actual form invariance, not by multiplicity-copy counting.

For e=alpha+beta(2x) supported on [-1/2,1/2], the exact corrected Schur form satisfies

S(e,e) > (3/50)||e||_(physical L2)^2 for nonzero e.

Equivalently, the same-vector corrected source e-z_e has that positive actual energy. This certifies a complete two-dimensional mixed block including every infinite-complement correction. It does not decide the full 64-dimensional Schur form.

## Linear actual source and endpoint separation

Write p(x)=2x, d_-=x+1/2, d_+=1/2-x, and retain the actual K,J,H from the preceding constant-source certificate. Let U(d)=integral_0^d sK(s) ds. The actual source constructor gives

q_p(x)=c(x)(2x)+2[U(d_-)-U(d_+)]
 -(log 2/sqrt 2)[p(x-log 2)+p(x+log 2)]
 -2B sinh(x/2),

where the translated p uses its zero extension, and B=M_+(p)=-M_-(p). Separate its log part as (2x)L(x), with L(x)=-(1/2)[log d_-+log d_+]. The remainder, apart from a multiple of the low polynomial 2x, is

h_p(x)=(2x)[H(d_-)+H(d_+)-2H(1/2)]
 +2[U(d_-)-U(d_+)]-2B sinh(x/2).

The subtracted multiple of 2x has zero physical complement projection.

## Log and smooth tails

The established log coefficients are even, and the degree-below-64 part of L has degree at most 62. Multiplication by 2x takes this part to degree at most 63, annihilated by complement projection. Multiplication by 2x has physical norm at most one. Thus

||P_F^(physical)((2x)L)|| <= ||P_F^(physical)L|| <=1/64.

For the smooth remainder, |H'|<=1 gives
|H(d_-)+H(d_+)-2H(1/2)|<=1, and the derivative of that bracket has magnitude at most two. The derivative of its product with 2x is therefore at most four.

Since dK(d)=exp(d/2)d/(2sinh d)<1 for 0<=d<=1, the U contribution has derivative magnitude at most four. Also

|B|=|integral (2x)sinh(x/2)dx|<1/4,

because sinh(1/4)<1/2 and integral |2x|dx=1/2. Its pole derivative is bounded by |B|cosh(1/4)<1/2. Consequently |h_p'|<9. The same Legendre derivative-energy bound as before gives

||P_F^(physical)h_p||^2 <81/[6*64*65] <(3/50)^2.

No logarithmic/graph density or spectral operator domain is assumed.

## Exact shifted-linear prime tail

Put r=2log 2-1, ell=2log 2 and c=log 2/sqrt 2. In the physical coordinate u=2x, the prime source, up to its irrelevant overall minus sign, is

c[(u-ell)1_(u>=r)+(u+ell)1_(u<=-r)].

It is odd and its squared physical norm is c^2(1-r^3)/3. Set I_0=1-r and I_n=[P_(n-1)(r)-P_(n+1)(r)]/(2n+1) for n>=1. For odd n, its normalized physical Legendre coefficient is

c[(n+1)I_(n+1)+n I_(n-1)-ell(2n+1)I_n]/sqrt(2n+1),

and for even n it vanishes. This follows by integrating the Legendre recurrence for uP_n. Subtracting squares through n=63 from the full squared norm gives the exact tail. Rational log/sqrt enclosures and interval recurrence, through degree 65, certify tail squared below 1/900. Its display is about 0.001075872, but that display is not an input.

The linear source residual therefore satisfies

||P_F^(physical)q_p|| <1/64+1/30+3/50<11/100.

## Corrected linear sign and mixed entry

The established residual theorem bounds the entire complement correction by

Q(z_p)<5(11/100)^2=121/2000.

The prior rational raw certificate gives Q(p)>9/100. Its second pivot equals Q(p) because the raw mixed constant-linear entry is exactly zero. Thus

S(p,p)>9/100-121/2000=59/2000>1/40.

Reflection preserves the actual logarithmic inner product, arch multiplier, paired prime translates and pole cross form. It also preserves E and F. The restricted coercive operator C commutes with reflection, so its inverse preserves parity. Therefore the exact lifts of 1 and 2x are respectively even and odd. The exact Schur mixed entry S(1,2x) is zero.

The prior corrected constant lower bound is S(1,1)>194/3125. Since ||alpha+beta(2x)||_L2^2=|alpha|^2+|beta|^2/3, the two exact diagonal bounds imply the theorem with physical coercivity 3/50. This handles arbitrary complex coefficients and includes the mixed entry.

## Validation and frontier

`scripts/certify_native_parity_schur.py` recomputes the constant certificate and the prior raw finite certificate, then checks the exact rational prime projection, derivative-tail constants and diagonal inequalities. Output: `notes/data/RPB108_PARITY_SCHUR_CERTIFICATE_20261005.json`. No exploratory quadrature is used.

This certifies one even and one odd corrected direction. Within each parity block, the other low modes and their mixed couplings remain. The full Schur form has 32 even and 32 odd coordinates; symmetry reduces its mixed cross-parity entries to zero but does not certify either 32-dimensional block. No full-carrier WD-T10 contraction, actual negative/null witness, endpoint exclusion or RH conclusion is asserted. F4 entry and FULL TRANSPORT CLOSED remain open. Lean source/checkpoint and CI claims are unchanged.
