# RPB108: actual coercive complement and exact finite obstruction

## Terminology and result

The **physical Legendre complement** F is the closed subspace of the logarithmic form carrier H=D_(1/2) whose physical L2 moments against P_0(x/a),...,P_63(x/a) vanish. The **coupling correction** is the nonnegative finite form removed when this coercive complement is eliminated by the exact Schur formula below.

For the actual native Weil form, unconditionally,

Q(f) > (1/5)||f||_(L2)^2 and Q(f) > (9/100)||f||_H^2

for every nonzero f in F. Here ||f||_H^2=integral log(e+|xi|)|Fourier(f)(xi)|^2 dxi, with support in [-1/2,1/2]. These bounds sharpen an initial 96-moment sufficient choice to 64 moments by evaluating the factorial bound rationally.

Consequently all negative and weak-null directions reduce exactly to a 64-dimensional Schur form. This form is not the raw 64-vector restriction: it subtracts the coupling correction. Its sign remains uncomputed. This locates the independent input still required at this aperture.

## Actual symbol bounds

The established actual form is integral m(xi)|Fourier(f)(xi)|^2 plus the exact pole cross-moment form. At a=1/2 only prime 2 contributes and its amplitude S=sqrt(2)log 2<1. The rational script checks log 2<7/10 and sqrt(2)<10/7, as well as log 3>1 for the cutoff.

Prior actual Euler bounds give, with t=|xi|>0,

m(xi) >= log t - 1/(2t) - S,
and m(xi) >= w(xi)-10-S > -10,

where w=log(e+t)>=1. For t>=4, log t>=log 4>=4/3 and 1/(2t)<=1/8, so m>=5/24. Also

w<=log t+e/t<log t+3/4,
m>log t-9/8 >= (1/10)(log t+3/4) >= (1/10)w.

The middle inequality is equivalent to log t>=4/3. On t<=4, w<=log(e+4)<log 7<2; the last inequality follows from e>8/3 and hence e^2>7. These are actual native multiplier bounds, not background positivity assumptions.

## Low-frequency observation and pole bounds

Physical moment vanishing through degree 63 annihilates the degree-63 Taylor polynomial of exp(-2pi i x xi). The rectangle remainder on |xi|<=T=4, |x|<=a=1/2 gives

||1_[-4,4] Fourier(f)||_(L2)^2 <= rho^2 ||f||_(L2)^2,
rho^2 <= 8*3^32*16^128/(64!)^2.

Indeed the Taylor norm bound is sqrt(4aT)exp(2pi aT)(2pi aT)^64/64!, and 2pi aT=4pi<16 and exp(16)<3^16. The same physical moments annihilate the degree-63 Taylor polynomials of exp(plus or minus x/2). For each actual pole moment,

|M_+(f)|, |M_-(f)| <= eta ||f||_(L2),
eta <= 2*(1/4)^64/64!.

This uses exp(1/4)<2 and 2a=1. The absolute pole cross-form is therefore at most 2eta^2||f||_(L2)^2, with bound p=8/[4^128(64!)^2]. All estimates use the same supported f and require no spectral operator-domain membership.

## Coercivity proof

Splitting at T=4 gives

Q(f) >= [5/24-(245/24)rho^2-p]||f||_(L2)^2,
Q(f) >= [1/10-(51/5)rho^2-p]||f||_H^2.

For the second estimate, the loss on the low band is at most (10+w/10) times its physical Fourier mass, hence less than (51/5) times that mass. Also ||f||_(L2)<=||f||_H. The pole loss is handled with that same inequality.

`scripts/certify_native_legendre_complement.py` checks exactly, with rational integers and factorials,

(245/24)rho^2+p < 1/120,
(51/5)rho^2+p < 1/100.

The displayed rho^2 is approximately 1.234509*10^(-8). The first loss is below 1.27*10^(-7). This proves both stated complement bounds. Exact rational constants are recorded in `notes/data/RPB108_LEGENDRE_COMPLEMENT_CERTIFICATE_20261005.json`. The script certifies the constants in this analytic proof, not a numerically discretized infinite operator.

## Exact finite obstruction with same-vector custody

Let E be the 64-dimensional span of these supported Legendre polynomials. They belong to H. The physical projection onto E is bounded on H: each physical moment is continuous on H and the image is finite dimensional. Thus H=E direct-sum F topologically; this need not be an orthogonal sum in H.

Represent the form restricted to F by C on the Hilbert space F. The proved bound gives C>=9/100 I, so C is boundedly invertible and ||C^(-1)||<=100/9. For e in E let b_e in F be the Riesz representer defined by Q(e,v)=<b_e,v>_H for v in F, with the inner product linear in its second slot. Define z_e=C^(-1)b_e and

S(e,e')=Q(e,e')-Q(z_e,z_e').

For h=e+v the exact square completion is

Q(h)=S(e,e)+Q(v+z_e).

This yields the following equivalences and constructors:

- Q>=0 on H if and only if S>=0 on E.
- Every strict negative vector for S gives the actual supported negative vector h=e-z_e for Q; no raw divisor preimage or retained membership is asserted.
- ker Q (the weak form kernel) consists exactly of e-z_e for e in ker S.
- The negative indices of Q and S agree, and their weak nullities agree. Every negative subspace projects injectively to E and has negative S-form; the reverse inequality uses e to e-z_e.

The coupling correction is Q(z_e,z_e)=<b_e,C^(-1)b_e>_H. It is nonnegative and at most (100/9)||b_e||_H^2. Thus a rigorous bound on this actual coupling, or a certified evaluation of the actual Schur form, would complete the fixed-aperture sign decision. Raw finite restriction positivity alone does not supply it: for any positive scalars a,c, the block matrix [[a,b],[b,c]] has positive diagonal restrictions but becomes indefinite when b^2>ac.

## Carrier consequence and cursor

Using the existing same-vector identity Q(f)=||S_+f||^2-||S_Bf||^2, the global WD-T10 contraction at this aperture is equivalent to S>=0. If that finite Schur sign holds, the norm inequality implies ker S_+ subset ker S_B and induces T(S_+f)=S_Bf; its continuous extension to the positive completion is a contraction. This is the previously established factorization criterion applied to an actual, explicitly coercive complement. The quotient alone does not establish the missing Schur sign.

The earlier eight-vector positivity and finite-range contraction are compatible with this reduction but do not certify S, which includes additional coordinates and the complement correction. No complement density, zero simplicity, full-domain positivity, endpoint existence or endpoint exclusion is assumed. No full Schur entries, actual negative witness, exact null or signed endpoint-null Gaussian upper estimate are produced here. Even a fixed a=1/2 sign decision would not alone decide every aperture. F4 entry and FULL TRANSPORT CLOSED remain open.

Lean source and the prior certified checkpoint are unchanged. This is an actual analytic complement theorem with exact rational constant checks.
