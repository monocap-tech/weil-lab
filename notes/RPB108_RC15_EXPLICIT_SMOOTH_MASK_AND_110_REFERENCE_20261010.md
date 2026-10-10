# RPB108 RC15 — explicit smooth mask and quantitative 1.10 reference

2026-10-10. Independent route consolidation.
Parent: fbf54ff3074304b2cf174f7e86338af1d1cfc885 (RC14).
Only research/rpb108-route-consolidation is written.

## Concrete result and scope

RC14's unspecified mask derivative ratio is now certified for an EXPLICIT
smooth nonnegative mask. The construction gives

    D epsilon^2 <= 7500/961.

At cap B=11/10 the complete correlation correction has physical operator
norm <58, the full native physical remainder has norm <22, and the positive
phase-reference operator has canonical floor >1/2100.

This is a reference metric certificate at 1.10, NOT original Weil positivity
at 1.10. The actual normalized correlation spectrum, finite head and whole
tail are still unevaluated. The original whole 1.06 certificate is unchanged.

## Explicit smooth mask, with definitions before use

Put L=log9. For any epsilon allowed by RC13's finite-cap count rule define

    r=4epsilon/5, delta=epsilon/10,
    t_r(x)=max(1-|x|/r,0).

This triangular base is nonnegative, compactly supported and in H1.
Define a standard smooth probability bump

    b_delta(x)=exp(-1/(1-(x/delta)^2)) for |x|<delta,
               0 otherwise,
    Z_delta=integral b_delta(x) dx >0,
    mu_delta(x)=b_delta(x)/Z_delta.

No numerical approximation of Z_delta is needed: only positivity, total
mass one and support within [-delta,delta] enter the bounds.
Set

    g_real=t_r * mu_delta,
    g(x)=sum_{k in integers} g_real(x-kL).

The convolution is C-infinity and nonnegative, with support radius
r+delta=9epsilon/10<epsilon. The periodized sum is locally finite.
Since L>2 and epsilon<=1/1000, adjacent copies and their derivatives do not
overlap. Thus the periodic L2 norms of g and g' equal the real-line norms
of g_real and g_real'.

Let

    G_0=integral_0^L g^2,
    G_1=integral_0^L (g')^2,
    D=G_1/G_0.

The mask is now an explicitly defined smooth function with G_0>0,
not a hypothetical derivative-ratio parameter.

## Analytic derivative certificate

The exact triangular integrals are

    ||t_r||_2^2=2r/3,
    ||t_r'||_2^2=2/r,
    ||t_r'||_2^2/||t_r||_2^2=3/r^2=75/(16epsilon^2).

Convolution with the probability bump contracts L2, so

    ||g_real'||_2<=||t_r'||_2.

The H1 translation inequality and the support of mu_delta give

    ||g_real-t_r||_2
      <= integral mu_delta(s)||t_r(. -s)-t_r||_2 ds
      <=delta ||t_r'||_2.

Since sqrt75<9,

    delta ||t_r'||_2/||t_r||_2 <9/40,
    ||g_real||_2 >= (31/40)||t_r||_2.

Consequently

    D <= [75/(16epsilon^2)]/(31/40)^2
       =7500/(961epsilon^2).                         (1)

This is an analytic smooth-mask certificate. No sampled quadrature,
uncontrolled mollifier derivative, or numerical normalization is used.

## Actual native attachment and norm allowances

The full native Q and canonical remainder are inherited from RC5 and RC14.
Their pinned source is
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, and the effective remainder
envelope from
notes/REFLECTED_PACKET_BRIDGE_108_EFFECTIVE_NATIVE_REMAINDER_CC37_20261008.md,
blob a8a4ec58ebc43745d73630b97188cac1597b15ed,
both read at CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.

CC37's global archimedean remainder norm <8 is inherited. The prime-power
and signed-pole envelopes below are freshly extended to B=1.10 using that
same full-form decomposition; no channel is omitted.

Define F(h)=(1/G_0)integral_0^L Q(g(. -s)h) ds and E=Q-F.
RC12--RC13 supply the positive physical reference guard

    F(h)>=gamma||h||_2^2, gamma=627/16000,

for all smooth supported h on the selected finite cap, with no moment
restriction. RC14 represents E by the bounded physical operator T_E.
Using split scale r_0=epsilon, its bound and (1) give

    ||T_E|| <=
      4B(2exp(B)+1)+log(2B/epsilon)
      +2 sum_{log n<=2B} Lambda(n)/sqrt(n)+1875/961.    (2)

The full sum replaces the autocorrelation loss by one only as an upper
bound; all signed prime terms remain in the actual operator.
Both pole moments remain in its continuous kernel.

## Fully quantitative anchor reference

At B=53/50, exp(2B)<9 gives N_B=ceil(2B/L)+2=3.
Choose epsilon=1/(1000*9^2)=1/81000.
The fresh exponential enclosures exp(B)<3 and exp(13)>2B/epsilon, with
RC5's inherited coefficient sum upper 12093/3740, yield

    ||T_E|| <
      459523/9350+1875/961 <52.

The already certified native remainder norm is <20. RC14's canonical
reference conversion therefore supplies

    A_F >= gamma/(gamma+20+52) I > (1/1900)I.

The known original anchor guard eta=1/10^37 additionally gives
Q >= [eta/(eta+52)]F > [1/(53*10^37)]F.
This relative inequality uses the old original certificate; it is not a
new positivity result at another cap.

## Quantitative reference at B=11/10

Fresh exact bounds give

    9<exp(11/5)<10, log9>2,
    3<exp(11/10)<10/3.

Thus 1<2B/L<2 and N_B=4. Choose

    epsilon=1/(1000*9^3)=1/729000.

The active prime powers are exactly 2,3,4,5,7,8,9. The original six
coefficients sum to less than 12093/3740, and prime9 has coefficient
Lambda(9)/sqrt9=log3/3<11/30. It is not log9/3.

The full signed pole allowance is

    4sinh(B)=2(exp(B)-exp(-B))<91/15,

using exp(B)<10/3 and exp(-B)>3/10.
The COMPLETE physical native remainder therefore satisfies

    ||R_B|| <
      8+2(12093/3740+11/30)+91/15 <22.               (3)

Also exp(15)>2B/epsilon. Equation (2) gives

    ||T_E|| <
      4(11/10)(23/3)+15
      +2(12093/3740+11/30)+1875/961 <58.              (4)

These are fresh cap-specific arithmetic envelopes, not positivity tests.

Let D_B be the inherited canonical logarithmic carrier, i_B its physical
inclusion, and define the actual positive reference operator

    A_F=I+i_B^*(R_B-T_E)i_B.

As in RC14, its physical guard and canonical Garding bound combine to give

    A_F >= gamma/(gamma+22+58) I
         = [627/1280627]I > (1/2100)I.                (5)

This is whole-domain positivity of F in canonical coordinates at 1.10.
F is the averaged masked form; it is not the original Q.
The mask, correction norm and reference floor are now all quantitatively
specified without assuming original positivity on that cap.

## What remains unevaluated

The actual normalized missing-correlation operator is

    K=A_F^(-1/2)i_B^*T_E i_B A_F^(-1/2),
    Q=A_F^(1/2)(I+K)A_F^(1/2).

Formula (5) makes the normalization legitimate and quantitative.
It does not show that inf spectrum(K)>-1. The unsigned norm allowance (4)
is not a certified lower bound on I+K.

RC14's complete certificate remains the acceptance condition:
a finite normalized head floor m, whole complementary block bound
tau<1, and cross-block bound rho satisfying

    m>rho^2/(1-tau).

None of those actual spectral blocks is evaluated here. The smooth mask
construction removes one reference-data obligation; it does not replace
the remaining arithmetic correlation certificate with a norm conversion.

## Fresh validation and standing

scripts/validate_rpb108_rc15_explicit_smooth_mask.py passes 35 exact rational
checks: triangular norms, support and smoothing ratios, derivative retention,
the 7500/961 mask bound, cap counts and exponentials, all newly active prime
and signed-pole costs, both correction envelopes and reference floors.
The source coefficient envelope and archimedean constant are inherited;
the convolution and H1 norm arguments are proved analytically above.
Finite scale controls are not a quadrature-based certificate.

The original whole 1.06 positivity and RC12 sparse theorem remain intact.
No whole positivity at 1.10, actual correlation spectrum, whole tail, negative
original vector, RH/F4 theorem or Lean closure is claimed.
Other branches and historical files remain unchanged.
