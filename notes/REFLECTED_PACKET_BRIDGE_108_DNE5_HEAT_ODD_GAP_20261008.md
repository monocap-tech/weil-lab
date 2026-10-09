# RPB108 DNE5 — Quantitative native odd gap, heat regularization and exact reflected cut

Date: 2026-10-08 America/Los_Angeles (UTC publication may be October 9). Previous DNE head `fc5aafef1fce971fde89a75634681dab07cea83e`. [Definitions](../docs/TERMINOLOGY_RPB108_DNE5_ODD_GAP.md). Read-only CC51 and NF17 developed concurrently; do not merge or promote finite E112 positivity to whole-aperture positivity.

**Classification:** analytically proved boundedness of the actual pole-free ground state, a full-domain positive odd spectral-gap lower bound, a numerically explicit but insufficient rational bound at a=53/50, an exact reflected-cut **upper** test, and proof that the simplest diameter certificate fails the needed RH-strength comparison. There is NO original Weil first-null exclusion, all-aperture sign, RH/F4/Lean result.

## 1. Actual unshifted pure-jump operator and free semigroup

Fix finite a>0 and keep the original prime powers n with ell_n=log n<=2a, c_n=Lambda(n)/sqrt(n). DNE3 proves on the ENTIRE canonical supported D_a that

    H_a=J_a-kappa_a I,
    kappa_a=log pi-psi(1/4)+2 sum_n c_n,

where the positive Dirichlet jump J_a has continuous density

    j(d)=exp(-|d|/2)/(1-exp(-2|d|)),

all finite active prime translations, BOTH orientations, and full exterior killing by zero extension. This is pole-FREE only; the original Q retains its signed even and odd pole terms. Let a0=psi(1/4)-log pi, and let Phi_a(xi) be the Fourier multiplier of the same jump operator on the UNRESTRICTED real line:

    Phi_a(xi) = a_arch(xi)-a0
         +2 sum_n c_n[1-cos(2pi xi ell_n)] >=0,       (1)
    a_arch(xi)=Re psi(1/4+i*pi*xi)-log pi.

CC37's global actual estimate r_arch=a_arch-log(e+|xi|), |r_arch|<8, gives

    Phi_a(xi)>=log(e+|xi|)-8-a0.                     (2)

The full-line semigroup e^{-t J_free} is convolution with its symmetric Levy transition measure. For t=1, e^{-Phi_a} belongs to L2 by (2) and its convolution kernel p_1 is a nonnegative L2 probability density. Plancherel in the inherited unitary Fourier convention gives

    ||p_1||_2 = ||exp(-Phi_a)||_2
      <= exp(8+a0) sqrt(2/e)
      < exp(3) sqrt(2/e).                           (3)

The last strict bound uses a0<-5, following from the exact digamma evaluation

    -a0=gamma_E+pi/2+3log2+log pi>5.

(The right side is not a physical-space bound for the full unbounded Weil form; it is a positive jump heat-semigroup estimate.)

The regular supported D_a is the part/killed form of that full-line jump process. Standard Dirichlet-form part semigroup domination gives for t>0 and f>=0,

    0<=e^{-tJ_a}f<=e^{-tJ_free} f_extended     (inside I). (4)

It can also be obtained by repeated positive semigroup truncation at the interval, retaining all exterior jumps, and a strong semigroup limit; no assumption that the killed generator is the free multiplier of the zero extension is made. At t=1, Cauchy-Schwarz for convolution yields

    ||e^{-J_a}f||_infty
      <= exp(3) sqrt(2/e) ||f||_2.                  (5)

This is the native log-order heat smoothing: the Fourier symbol grows like log|xi|, so t=1 is sufficiently large for L2-to-L-infinity regularization. It applies to all L2 vectors, not only positive f, by semigroup positivity and |Tf|<=T|f|.

Let phi>=0 be CC43/DNE2's normalized ground state of J_a, ||phi||_2=1, J_a phi=mu_a phi, mu_a=kappa_a+lambda0(H_a)>=0. From phi=e^{mu_a}e^{-J_a}phi, (5) gives the actual bound

    M_a=||phi||_infty <=exp(mu_a+3) sqrt(2/e)<infinity. (6)

This upgrades DNE2's a.e. positivity by an essential upper bound; it DOES NOT give continuity, pointwise positive boundary traces or a positive essential lower bound.

References for the abstract killed-process domination used in (4): Grzywny, *Intrinsic ultracontractivity for Levy processes*, https://arxiv.org/abs/math/0606659, section 2 (killed heat kernel dominated by the full transition kernel); Li--Ying, *On domination for (non-symmetric) Dirichlet forms*, https://arxiv.org/abs/2412.08886 (dominated semigroup/part-form characterization). DNE3's specific native jump density establishes the relevant Levy-measure hypotheses directly; no full intrinsic ultracontractivity theorem is imported.

## 2. Complete-domain quantitative odd gap

DNE4 certifies the weighted ground-state representation on ALL `L2((-a,a),phi² dx)` form-domain vectors:

    W_phi(u)= (1/2) int_I int_I j(x-y)phi(x)phi(y)(u(x)-u(y))² dxdy
       +sum_n c_n int_(x,x+ell_n in I)
                       phi(x)phi(x+ell_n)(u(x)-u(x+ell_n))²dx.

For any real odd u, the weighted mean int_I phi² u vanishes by even phi. The basic diameter inequality j(|x-y|)>=j(2a) and the variance identity give

    W_phi(u)
      >=j(2a)[S_a^phi int_I phi u² -(int_I phi u)²]
      =j(2a) S_a^phi min_c int_I phi(x)(u(x)-c)² dx
      >=j(2a) S_a^phi/M_a * int_I phi²u².       (7)

The middle minimum formula is exact; for odd u the minimizer c=0, since int phi u=0 as phi is even. Here S_a^phi=int_I phi>0. Because phi is L2 normalized and 0<=phi<=M_a, one has 1=int phi²<=M_a S_a^phi, so

    gamma_odd(a):=inf_(odd u !=0) W_phi(u)/||u||²_(phi²)
        >=j(2a) S_a^phi/M_a
        >=j(2a)/M_a²
        >=(e/2) j(2a) exp[-2(mu_a+3)]>0.      (8)

This is a genuine effective (if crude) positive odd spectral separation on the FULL supported domain and works even if original Q_a is indefinite. It excludes equality with the GROUND transformed eigenvalue zero, not the higher original H eigenvalue zero.

## 3. Rigorous rational cap test: a=53/50

Use only *prior authenticated* native data, not a newly assumed full-aperture sign.

- The CC40 pinned NF12 original degree0 arch and prime outward rational intervals add to a value strictly below -4. Thus lambda0(H_a)<=H_a(Legendre0)<-4. No NF17/E112 finite sign is needed.
- CC37 gives the cap prime coefficient sum S_a=sum c_n<12093/3740<4.
- The exact special-value identity for -a0 and elementary gamma_E<1, pi/2<2, 3log2<21/10, log pi<6/5 imply -a0<7. Thus kappa_a=-a0+2S_a<15.
- Hence mu_a=kappa_a+lambda0(H_a)<15-4=11.
- Since 1<a=53/50<2 and 2a<9/4, one has j(2a)=e^{-a}/(1-e^{-4a})>e^{-2}>1/9. Also e^{-a}<3/8 and 1-e^{-4a}>15/16, so j(2a)<2/5.

Equation (6) yields M_a<e^{14}sqrt(2/e). Combining with (8) and 2<e<3 gives

    gamma_odd(53/50)
      > (e/2)(1/9)e^(-28)
      > 3^(-30).                                      (9)

The second comparison follows from e/2>1 and e^-28>3^-28. All inequalities are conservative; no full mixed-Schur matrix or actual eigenvector values have been evaluated.

The specific diameter certificate on the right side of (7) also obeys

    Gamma_diam=j(2a)S_a^phi/M_a
       <=2a j(2a)<(9/4)(2/5)=9/10<1.             (10)

But DNE's desired zero-moment exclusion would need gamma_odd> -lambda0(H_a)>4. Therefore this exact *diameter-only sufficient lower bound* cannot possibly certify that conclusion at the target cap. This does NOT prove gamma_odd<1, cannot disprove actual odd positivity, and is not an original negative vector.

## 4. A prime-sensitive mirrored-cut upper diagnostic (not a lower bound)

Because phi is bounded by (6), u(x)=sgn(x) is in the FULL weighted DNE4 form domain: its continuous cross-origin jump integral is finite since j(x+y)=O(1/(x+y)) and int_(0,a)^2 (x+y)^-1 dxdy<infinity; all finite prime-cross terms are bounded. Its weighted norm is ||u||²_(phi²)=||phi||²_2=1.

The jump differences vanish whenever x,y have the same sign. Consequently DNE4 gives the EXACT quotient

    C_cut(phi)= W_phi(sgn x)
       =4 int_0^a int_0^a
                      j(x+y)phi(x)phi(y)dxdy
         +4 sum_(ell_n<=2a)c_n int_(max(0,ell_n-a))^(min(a,ell_n))
                      phi(z)phi(ell_n-z)dz.            (11)

The second integral counts each ORIGINAL prime shift crossing the origin once; the factor 4 comes solely from (sgn+ - sgn-)². It retains ALL prime power bridges 2,3,4,5,7,8 at a=53/50. Therefore

    gamma_odd(a) <= C_cut(phi).                        (12)

This is a useful **upper** test of proposed gap claims, and a natural response-coordinate for numerical future work. No actual Weil phi has been computed, so it has not been evaluated or used to assert a sign for H or Q. In particular lower and upper bounds on gamma are not interchangeable.

## 5. Adversarial controls and decision

A finite attractive connected graph can have a bounded strictly positive ground state and a positive odd Doob gap equal to -lambda0, leaving a higher original odd H zero (DNE2--4 exact three-site control). Thus heat smoothing, positive diameter conductance, nonzero odd gap, and reflected-cut finiteness are all consistent with an actual first crossing in other operators. Positive physical level shifts provide the same warning. The coefficients in (11) are actual von Mangoldt coefficients, but only evaluated on the unknown actual ground state would they constrain zeta specifically.

**DNE5 achieved:** essential boundedness of the actual ground state by native heat smoothing; complete-domain quantitative positive odd ground-gap (8), with conservative rational >3^-30 at53/50; strict disqualification of the coarse diameter certificate; exact prime-sensitive sign-cut upper formula (11).

**DNE5 not achieved:** the strict arithmetic surplus gamma_odd> -lambda0, a lower bound for the actual odd form at level kappa_a, even zero-moment or moment-carrying contact exclusion, whole-a=53/50 sign, RH/F4 or Lean closure.

**DNE6 natural follow-up:** identify a sharper eigenfunction-adapted lower bound for the reflected half-interval weighted form, retaining j(|x-y|)-j(x+y), the full prime bridge, and true phi. Audit its strict surplus against the graph contact control and NF17's separate original E112 finite certificate before promotion. Do not repeat the diameter minorant or infer full sign from E112 and F112 without the mixed native Schur.

## 6. Custody and verification

The corresponding exact rational validator reads the already pinned CC40/NF12 degree0 input and checks H00<-4, S_a<4, all elementary rational comparisons required for (9) and (10). The native semigroup, Fourier, and DNE4 domain steps are analytic deductions, NOT inferred from finite rational samples. Only additive DNE files are published; CC51 and NF17 remain read-only. 
