# Stop the original SM40 envelope gate for all Galerkin enrichments of J470

Base: PR #344 / 3654d8b256ec3ceaaade8d415404847cf02f3ea3.
Active W-ODD-NEG remains OPEN. Every operator statement below retains the
inherited original Fourier/closed-form/domain assumptions. Arithmetic CI
does not independently discharge those assumptions.

## Decision and exact scope

The ORIGINAL SM40 step envelope is too large for the capped original
470-source energy-dual inequality, even with threshold theta=1. The result
also stops the cap-only necessary test for EVERY exact Astar-Galerkin trial
that CONTAINS the original J470, regardless of added trial directions.
This includes the canonical 484D SI29 enrichment and the exact full inverse
energy-dual image. Every Young parameter using this SAME envelope is covered.

Consequently, raising the complement threshold, tuning the Young parameter,
adding Galerkin trial directions while retaining J, improving residuals, or
computing a more accurate inverse cannot repair THIS capped comparison gate.
Do not launch its full arch/484D calculation. A cap below this envelope or a
different criterion is required. Non-Galerkin sufficient inequalities and
trial/source choices outside the stated class are NOT ruled out.

This is NOT a negative direction of Astar-Kminus. It is a stopping theorem
for a comparison operator which overpays the true negative multiplier.
The true odd operator, exact signed Schur, even/CC27/Weil/RH remain OPEN.

## Operators and the two original diagnostic rays

Use the original odd physical L2 space on [-B,B], B=11/10. Let A=Astar be
the original closed positive pole-corrected operator (possibly UNBOUNDED),
with inherited SI29 coercivity. Let P be the PHYSICAL orthogonal projection
onto the original J470, Q=I-P. The genuine sinh pole belongs to J. Therefore

    a(q,q)>=kappa ||q||^2 on QH intersect the form domain, kappa=1/1000.

This uses the original positive-multiplier floor and the vanishing pole
on QH. kappa is NOT kappa_star=33621/10^9; no global floor is upgraded.

Let w40 be the original even step envelope on all 3892 original SM40
subcells, zero outside the inherited cover, and define the bounded PSD

    E40=V* w40 V,     Kminus<=E40,
    ||E40||<=M=max w40=3114203/250000=12.456812.

Retain the SAME original physical rays

    f_d=12001 sin(2*pi*(37/64)x)+16384 sinh(x/2),
    f_c=3013 sin(2*pi*(37/64)x)+4096 sinh(x/2),

both in J. No new source direction is introduced.

## Whole-complement transport from the accepted Hermite bounds

PR #344 retained a uniform bound |fhat(xi)|^2<=L_leaf ||f||^2 for EVERY
odd f in J-perp on each of all 973 original negative leaves. That proof
uses the exact Fourier zeros already imposed by the existing J generators.
Its pointwise bound is independent of which nonnegative frequency weight
is subsequently integrated. Reweight it with the actual w40 subcells:

    Q E40 Q <= epsilon40 Q,
    epsilon40=sum_(3892 cells) 2*width*w40*L_parent_leaf
              =2.4301374667791075e-8... <2431/10^11.

This is a direct weighted integration of retained Fourier bounds. We do
NOT infer it from the order Kminus<=E40. Source constraints, physical
projection, all 107 clusters and all reflected frequencies are unchanged.

Since E40 is bounded and positive, E40^2<=M E40 by spectral calculus.
Compressing this inequality, then taking the norm and the adjoint, gives

    ||E40 Q||^2=||Q E40||^2 <= beta2=M*epsilon40
                 =3.027176555782359e-7... .

No identity between a physical compression square and a squared multiplier
is used. This bound controls the ENTIRE infinite complement, not only the
fourteen normalized SI29 directions. It pays all correction cross terms.

## Bounded scalar original calculation

The scalar certificate constructs a lower for E40(f) and a COMPLETE upper
for A(f), without a full source matrix or an inverse. Let

    t_f(xi)=integral_(-B)^B f(x) sin(2*pi*xi*x) dx,
    r(xi)=(kappa-m(xi))_+.

The original odd Fourier convention is fhat=-i t_f. For real source
coefficients, |fhat|^2=t_f^2; both sine/pole components and their cross term
are retained before squaring.

### Same envelope, independently reconstructed

The producer rebuilds the exact original 3892 weights from the 973 pinned
parent leaves, original SI06 prime intervals and original rational arch
lower. It omits unnecessary Hankel LDL work. Monotonicity shows the SM39
rational-left candidate already dominates the SM37 integer-left candidate,
so the final weight is min(parent, SM39 candidate, SM40 candidate).
The independent checker explicitly reconstructs ALL THREE stages and
compares EVERY weight. Their two-sided mass is exactly
1073441879/64000000 and the unchanged 24-bit Taylor column count is 890.
There is no new envelope or redefined cap hidden in this test.

### Real-frequency remainder and clipping payment

Each original SM40 cell is split into 16 for this scalar calculation:
62272 closed intervals, no gaps. At the exact rational midpoint, 512-bit
Arb encloses the ORIGINAL signed multiplier, including the quarter-digamma
and all seven prime powers (2,3,4,5,7,8,9). The original rational prime
coefficient bounds are cross-checked against the native constants.

For all real xi, the trigamma series gives

    |d/dxi Re psi(1/4+i*pi*xi)|
       <=pi sum_(n>=0) (n+1/4)^-2 <=20pi.

The original seven-prime first-derivative bound is <69, checked exactly.
Thus |m'|<132 globally. This is the source of the whole-interval upper

    r(xi)<=u_I=min(w40, max(0,kappa-m_mid_lower+132*width/2)).

It remains valid across every positive-part kink; no sign guess, complex
interval wrapping assumption or interpolation of sampled signs is used.
NIST trigamma series reference: https://dlmf.nist.gov/5.15.E1 .

To integrate t_f^2 on I, retain the native sine and pole Fourier basis
intervals at its two endpoints and midpoint, rounded OUTWARD to 24 decimal
places. Leibniz and physical support imply

    |(t_f^2)^(4)| <=(4*pi*B)^4 ||f||_L1^2
                  <=((88/7)*B)^4 *2B*N_f,
    N_f=2B*(|alpha|+(3/5)|b|)^2 >=||f||^2.

The sinh bound sinh(B/2)<3/5 follows from an exact positive Taylor series
with geometric tail. Standard Simpson error on a FULL width d is

    |integral t_f^2 - d*(t_l^2+4t_mid^2+t_r^2)/6|
       <=d^5 sup|(t_f^2)^(4)|/2880.

NIST reference: https://dlmf.nist.gov/3.5.E6 . The factor differs from the
half-step notation by 2^5; exact quartic saturation checks it. Total
weighted Simpson errors are <0.001746 direct / <0.000110 second. The
point enclosures and the analytic remainder BOTH contribute to the bounds.
All 124651 distinct native Fourier point records and all 62272 native
midpoint multiplier intervals are retained for independent exact replay.
The multiplier intervals are rounded outward to 12 decimal places.

Summing 2*w40*integral_lower/upper gives E40(f) bounds, and summing
2*u_I*integral_upper gives a COMPLETE Kminus(f) upper. The factor 2 pays
the two frequency signs once. The inherited cover pays all other real
frequencies; no negative-frequency tail is dropped.

### Whole signed form via physical shifts

Use the exact identity

    Q_o(f)=A(f)-Kminus(f)=<f,m(D)f>-2|<f,sinh(x/2)>|^2.

Define autocorrelation A_f(s)=integral_(-B)^(B-s) f(x)f(x+s) dx for
0<=s<=2B and zero for s>=2B. With

    c0=psi(1/4)-log(pi), k(s)=exp(s/2)/sinh(s),

NIST DLMF 5.9.16 gives the complete original arch form

    c0 ||f||^2 + integral_0^(2B) k(s)(||f||^2-A_f(s)) ds
                 +||f||^2 integral_(2B)^infinity k(s) ds.

Reference: https://dlmf.nist.gov/5.9.E16 . The final infinite integral is
2 sum_(n>=0) exp(-(2n+1/2)*2B)/(2n+1/2). Sixty-four positive terms plus
an explicit geometric tail bound pay it completely.

The finite integrand is evaluated in the nonsingular form
(s*k(s))*D_f(s), D_f(s)=(||f||^2-A_f(s))/s. Represent f using its FOUR
exact complex exponentials. This gives elementary closed overlap formulas;
exp-relative factors are evaluated as exp(z/2)*sinc(i*z/2), entire at zero.
The resulting D_f is entire, with D_f(0)=f(B)^2. The regular kernel is
s*k(s)=exp(s/2)/sinc(i*s). Arb's certified complex integrator encloses this
finite integral at 512 bits, with explicit work limits. Its integrand is
meromorphic; possible denominator zeros cause nonfinite enclosures and
subdivision, not an assumed holomorphic region or an ignored branch cut.
The native integral, constants and tail intervals are retained.

All seven prime-power terms are -2 log(p)/sqrt(n)*A_f(log(n)), with the
original physical clipping. The genuine pole is subtracted exactly.
Independent inherited trigonometric physical primitives check the norm,
pole, ALL SEVEN translated overlaps and four original Fourier points.
Additional checks verify D_f(0), its nonzero-shift identity, and the
quarter-digamma constant against native digamma. The resulting native
whole signed energies are approximately +42084.9580696451 direct and
+2654.6470665440 second. Their positivity is a proof INPUT here, not a new
source-dimension campaign or a statement about the energy-lifted vectors.

Finally A(f)<=Kminus_upper(f)+Q_o_upper(f). These are bounded NEW scalar
calculations; the old expensive 7168-cell integration is not rerun.

## Uniform energy-lift inequality

Suppose g=f-q with q in QH and a(g,q)=0. Then

    a(g,g)=a(f,f)-a(q,q),  a(q,q)>=kappa ||q||^2.

The negative-envelope action is NOT invariant under the correction:

    E40(g)=E40(f)-2 Re<q,E40 f>+E40(q)
          >=E40(f)-2 sqrt(beta2)||f|| ||q||.

Completing the square gives the ENTIRE complement payment

    E40(g)-a(g,g)
       >=E40(f)-a(f,f)-beta2*N_f/kappa.

The correction is arbitrary within the whole complement subject to energy
orthogonality; no fixed 14D inverse, forcing approximation or sum of
component inverse charges is substituted.

| Original ray | E40(f) lower | A(f) upper | Whole-complement correction upper | Strict remaining lower (rounded down) |
|---|---:|---:|---:|---:|
| Direct | 198909908.136661... | 193238241.547270... | 317412.193305... | >5354254.396 |
| Second | 12494892.627069... | 12138779.313706... | 19931.058067... | >336182.255 |

Exact Fractions carry acceptance; only one strict ray is needed. The
remaining lower is for the CAPPED comparison, not Astar-Kminus.

## Exact energy-dual source gate: no computed inverse required

A is coercive, so A^-1 is bounded and positive even though A itself may be
unbounded. On finite J define T=P A^-1 restricted to J. It is strictly
positive and hence invertible. For either original f in J, set

    h=T^-1 f in J,   g=A^-1 h,   q=f-g.

Then Pg=f, q in QH and a(g,q)=<h,q>=0. Thus the uniform bound applies.
Also g is NONZERO because Pg=f is nonzero. For every bounded PSD cap
C>=E40, and every 0<theta<=1,

    <g,Cg>-theta a(g,g) >= E40(g)-a(g,g)>0.

Therefore the EXACT original 470-source capped gate N_C<=theta G fails.
The source preimage h is mathematically defined, not claimed to be a
serialized numerical/rational 470-vector. Existence and the uniform
strict margin suffice to refute the full real-coefficient Loewner gate.
This does not refute N_Kminus<=G for the genuine operator.

## Every exact Galerkin enrichment retaining J

Let V be ANY finite form-domain trial space containing J. Let Z_V h be its
exact A-Galerkin solution for h in J. T_V=P Z_V restricted to J is strictly
positive: <h,T_Vh>=a(Z_Vh,Z_Vh)>0 for nonzero h, since h belongs to V.
Consequently choose h=T_V^-1 f, g=Z_Vh. Then Pg=f and q=f-g belongs to
V intersect QH. The Galerkin equation gives a(g,q)=<h,q>=0, so the SAME
strict uniform bound applies. Hence

    theta Z_V* A Z_V - Z_V* C Z_V

has a negative original-source coefficient direction for every such V,
every C>=E40 and every 0<theta<=1. Adding nonnegative MG07 residual/Young
payments cannot repair a failed necessary cap-only test. This stops
Galerkin trial enrichment, including J-only and full SI29, for this cap
family. It does NOT rule out all trial spaces or all non-Galerkin bounds.

## All Young parameters for this same SM40 envelope

Let R_env be the w40-weighted Fourier analysis and R0 its same original
890-column, 24-bit Taylor approximation. The original construction gives
||R_env-R0||^2<=e2, e2=2B*mass40*2^-48. For ANY tau>0, Young's inequality
implies

    E40=R_env*R_env
      <= C_tau=(1+tau)R0*R0+(1+1/tau)e2 I.

Thus every Young parameter for this same envelope is covered. Changing
tau alone cannot avoid the stop. A genuinely tighter envelope (not required
to dominate E40) or a different original signed criterion remains open.

## Verification, custody and next bounded decision

One pinned #344 archive carries the exact native geometry, original
negative leaf data, accepted source cases and Hermite packet certificate:
run 40445502180 / source 3654d8b256ec3ceaaade8d415404847cf02f3ea3 /
artifact 12707773653, archive SHA256
5d934bc52849a8c9e1f267b6f4fbcfa0830563b5b815a11684c828ae18187141.
The workflow verifies EVERY matched JSON hash, replays the retained Hermite
packets, rebuilds the same SM40 weights, evaluates the bounded native
scalar certificate and independently replays all rational payments.
Local full computation takes about 44 seconds, guarded at 120 seconds.
No full 470/484 matrix, full inverse, new source family or arch mixed block
is assembled. Independent exact models test the whole-width Simpson
constant, graph correction for different complement subspaces, Young
majorization, and true signed positivity despite failure of a loose cap.

Native ball/complex-integration enclosures, this analytic argument,
independent arithmetic replay and original domain identification retain
separate standing. Parent legacy serializer failures remain documented;
no claim that all historical repository CI is green is made here.

Reconcile: the improved #344 complement threshold remains useful, but
cannot rescue this SAME envelope because the capped gate fails even at
ONE. Stop refining thresholds/residuals/trial dimensions for that family.
The next justified bounded investigation must target envelope overpayment
or an original criterion that uses the true negative action more directly.
A different cap must demonstrate a relevant finite-source feasibility gain
before a large matrix run. No automatic dimension campaign follows.

W-ODD-NEG, the true original signed sign, exact true signed Schur,
independent original-domain review, even/CC27/Weil/RH remain OPEN.
No manifest acceptance/status change. Draft/unmerged.
