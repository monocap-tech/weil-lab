# RPB108 DNE6 — Exact odd reflected excess and low-potential-set obstruction

Date: 2026-10-08 America/Los_Angeles (GitHub UTC date may be October 9). Parent DNE5 `a771c93c69fbdfc65858d0497aa525f86201b44d`. [Definitions](../docs/TERMINOLOGY_RPB108_DNE6_REFLECTED_EXCESS.md). Read-only contemporaneous: CC52 and NF18; no source branch is reset, merged or rewritten. **Classification:** exact original-coefficient reflected HALF-INTERVAL form and conditional NON-STRICT contact exclusion, plus an interior localization inequality and sharp attractive-graph controls. No actual Weil first-null exclusion, no full a=53/50 sign, RH/F4 or Lean theorem.

## 1. Use the complete weighted ground-state domain, not a guessed smooth quotient

DNE4 established on the full closed transformed domain the exact pole-free Weil ground-state formula

    W_phi(u)=1/2 int_I² j(x-y)phi(x)phi(y)(u(x)-u(y))² dxdy
      +sum_(ell_n<=2a)c_n int_(x,x+ell_n in I)
                       phi(x)phi(x+ell_n)(u(x)-u(x+ell_n))² dx,       (1)

with I=(-a,a), phi=phi_a>0 a.e. even and normalized physical L2, and j(d)=exp(-|d|/2)/(1-exp(-2|d|)); c_n=Lambda(n)/sqrt(n)>0 for EVERY active original prime power, ell_n=log n. The signed original pole terms have been removed ONLY in the definition of H_a and have not been reclassified. DNE2–5 justify the full domain and boundedness of phi; no pointwise trace or smooth eigenfunction is assumed.

Assume a hypothetical nonzero real ODD eigenvector h of H_a at eigenvalue zero (the zero-moment pole-free channel of the original contact classification). CC43's simple even ground state then necessarily has lambda0(H_a)<0. Put d=-lambda0>0 and u=h/phi, odd, in the ENTIRE transformed form domain. The exact energy level is

    W_phi(u)=d ||h||²_2.                                (2)

We do not assume Q_a>=0 to deduce the necessary condition (2); an odd H-null automatically satisfies it. An original odd Q-contact additionally needs its sinh pole moment zero.

## 2. Exact half-interval decomposition retaining all prime bridges

Write u(x) for the restriction of odd u to 0<x<a. Even phi and odd u allow folding the complete continuous part of (1):

    W_cont(u)=int_0^a int_0^a phi(x)phi(y) [
       j(|x-y|)(u(x)-u(y))²+j(x+y)(u(x)+u(y))²]dxdy.      (3)

Define for a.e. x>0

    V_a(x)=2/phi(x) int_0^a j(x+y)phi(y)dy.              (4)

Because j is strictly decreasing and 0<|x-y|<x+y for x,y>0 apart from the diagonal,

    W_cont(u)=4 int_0^a phi(x)u(x)²
                         [int_0^a j(x+y)phi(y)dy]dx
        +int_0^a int_0^a phi(x)phi(y)
             [j(|x-y|)-j(x+y)](u(x)-u(y))²dxdy.          (5)

The first term is EXACTLY the full weighted physical potential integral `int_I V_a(|x|)phi²u²`.

Each original undirected prime edge splits into two copies of a same-sign, same-half edge plus the crossing edge. For ell_n<a, the two within-half segments contribute

    2c_n int_0^(a-ell_n)
        phi(x)phi(x+ell_n)(u(x)-u(x+ell_n))² dx.         (6)

For every ell_n<2a, the crossing segment contributes

    c_n int_(max(0,ell_n-a))^(min(a,ell_n))
         phi(z)phi(ell_n-z)(u(z)+u(ell_n-z))² dz.        (7)

These coefficients contain the original TWO orientations from CC27 exactly, not twice their true value. Equalities ell_n=a or ell_n=2a contribute the appropriately empty or one-sided intervals; there is no endpoint delta mass of positive measure. Use the full active set ell_n<=2a in (1) and the strict geometric inequalities only to describe nonempty segments.

Let X_a(u) be the sum of the second term in (5), all (6), and all (7). Every term is nonnegative, so on the COMPLETE admissible odd domain

    W_phi(u)=int_I V_a(|x|)phi(x)²u(x)² dx +X_a(u),
    X_a(u)>=0.                                         (8)

Equation (2) now becomes the exact **reflected deficit equation**

    X_a(u)=2 int_0^a [d-V_a(x)]phi(x)²u(x)² dx.          (9)

This is a genuinely sharper form of DNE5's diameter minorant. It retains same-half variation and the sign-reversing prime bridges, rather than discarding all geometry after replacing j by its minimum.

## 3. A NON-STRICT pointwise floor suffices to exclude an odd zero

**Theorem DNE6-A.** Suppose 2a>log2, so the ORIGINAL prime2 bridge has an interval of positive length. If

    V_a(x)>=d=-lambda0(H_a) for a.e. 0<x<a,            (10)

then H_a has no nonzero ODD zero eigenvector.

**Proof.** Were such h to exist, (9) would give X_a(u)<=0. Since every X term is nonnegative, X_a(u)=0. The continuous excess kernel `j(|x-y|)-j(x+y)>0` for almost every x,y>0 and phi>0 a.e., so its vanishing implies u is a.e. constant on (0,a). If the constant is t, the prime2 crossing term (7) equals `4c_2 t² int phi(z)phi(log2-z) dz` over its nonempty positive-measure interval. This is strictly positive unless t=0; phi>0 a.e. and c_2>0. Thus t=0 and h=0, contradiction. QED.

Unlike DNE5's strict `Gamma_odd>d`, **equality in the pointwise reflected potential is now allowed** because prime2 supplies an independent strictly positive bridge against constant odd-half functions. This is a sufficient criterion, not a proved inequality for the ACTUAL unknown phi.

**Corollary DNE6-B (necessary bad region).** Any nonzero odd H_a-null at 2a>log2 forces

    measure({x in(0,a):V_a(x)<d})>0.                     (11)

This uses complete native arithmetic and not an old-gap inverse. It remains consistent with a hypothetical off-line zeta zero; no positive lower bound on the measure of that set is obtained.

## 4. A quantitative native interior oscillation constraint

The continuous j has the exact positive exponential expansion

    j(t)=sum_(k>=0) exp[-(2k+1/2)t], t>0.              (12)

Fix 0<delta<a and x,y in [delta,a]. Then r=|x-y|<=a-delta, and x+y>=r+2delta. For every summand in (12), `exp(-lambda r)(1-exp(-2lambda delta))` decreases in r. Hence

    j(|x-y|)-j(x+y)
        >= j(a-delta)-j(a+delta)
        =: alpha_(a,delta)>0.                           (13)

Let S_delta=int_delta^a phi>0 and `bar_u_delta=(int_delta^a phi*u)/S_delta`. The exact weighted variance identity gives

    X_a(u)>=2 alpha_(a,delta) S_delta
                         int_delta^a phi(x)(u(x)-bar_u_delta)²dx. (14)

For an odd H-null, (9) and the inequality `d-V<= (d-V)_+` give

    alpha_(a,delta) S_delta
         int_delta^a phi(x)(u(x)-bar_u_delta)²dx
      <=int_0^a (d-V_a(x))_+ phi(x)²u(x)²dx.            (15)

Thus an odd hypothetical contact with only a small reflected low-potential deficit must be nearly CONSTANT in the interior, while the prime2 bridge penalizes precisely such a constant. The missing quantitative ingredient is now **control of the deficit set and its coupling to the same-side/prime excess on the actual ground state**, not a generic uniform diameter estimate.

Equation (15) is meaningful without pointwise regularity or traces of h; u is merely in the full DNE4 weighted form domain. Truncation/monotone lower-semicontinuity justify all nonnegative integrals.

## 5. Sharp two-site reflected controls: a prime bridge alone is NOT enough

Consider two positive-half sites with phi=(1,1), continuous same-side coupling 3, and reflected continuous weights

    J_plus=[[2,1],[1,1/2]],    J_minus[1,2]=3>J_plus[1,2].

The two-site analogue of (5) gives V=(6,3), and exactly

    W_cont(u1,u2)=12u1²+6u2²+4(u1-u2)²
                 =16u1²+10u2²-8u1u2.                  (16)

The odd full-space weighted physical mass is 2(u1²+u2²). Add a prime-like cross-origin bridge p(u1+u2)², p>=0, retaining an independently nonnegative prime edge. These are ATTRACTIVE full-space graph weights in the ground-state representation; they are not a computed native Weil spectrum.

- At p=0, the lowest odd energy ratio is exactly d=4, attained at u=(1,2), with V_2=3<4. A higher zero can occur when the pole-free ground depth is tuned to d.
- At p=4, the odd form becomes `W=20u1²+14u2²`. The lowest ratio is 7, attained by u=(0,1). Setting ground depth d=7 again produces a higher zero DESPITE a strictly positive crossing bridge. The necessary low-potential region still exists because V_2=3<7.
- For d=2, the pointwise sufficient condition V>=d holds; every nonzero odd trial has W>d times its weighted mass, even with p=0. This confirms theorem A does not assume more than needed.

Thus positivity of every conductance and presence of a prime-like crossing edge do not supply the missing arithmetic inequality (10), nor an unconditional gap above d.

Separately, the true native kernel samples `j(m log4)=2^{-m}/(1-16^{-m})` are positive rational values for m>=1. The exact validator checks the strict comparison (13) on an integer lattice of these actual kernel values as well as the two-site fold/bridge algebra; those finite checks do NOT evaluate phi or prove the continuum theorem.

## 6. Research decision / next checkpoint

**Closed in DNE6:** full-domain reflected potential-plus-excess identity (8), strict same-side positivity, NON-STRICT sufficient pointwise floor (10), necessary positive-measure deficit region (11), and localized oscillation estimate (15). These are exact structural consequences of the original archimedean and von Mangoldt prime jump terms, not numeric evidence for or against RH.

**Still open:** the actual reflected potential `V_a` and ground depth comparison (10) at any unproved aperture; a quantitative deficit-versus-excess bound for actual phi; exclusion of higher EVEN zero-moment modes; either moment-carrying original Q null; global first-contact exclusion, whole 53/50 signed source-Schur, RH/F4 or Lean closure.

**DNE7 target:** use the exact ground-state equation to constrain phi and V_a and test whether the low-potential defect set can coexist with prime2 reflected-bridge coercivity. Prefer a rigorously evaluated constrained lower bound, not an upper Ritz estimate, nor a restatement of `H_a^odd>0`. Examine strongly localized positive-half and oscillatory controls to identify the weakest zeta-specific arithmetic input.

Concurrent CC52 source-Schur and NF18 native mixed tests are independent finite-aperture research, not DNE6 validations. Historical DNE0–5 and all other branches remain untouched.
