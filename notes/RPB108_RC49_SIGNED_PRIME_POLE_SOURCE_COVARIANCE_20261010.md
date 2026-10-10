# RPB108 RC49 — signed prime-pole source covariance

2026-10-10. Parent RC48: `434bf3084898ddfca97d257b46a249dbcd622388`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

The physical pole source actions and all symmetrized prime-pole trial
source correlations are now enclosed on native features 0 through 7.
Both signed poles and every active prime power remain present. Transport
of the complete joint source, retaining its correlations, certifies

    (sigma_prime+sigma_pole)^*(sigma_prime+sigma_pole)
       <=13.336601410692442... M_8 <(667/50)M_8.

This is an entire-map **eight-feature** canonical source bound below
13.34 M_8. The separate-component triangle bound from RC48's prime
allowance and RC42's pole allowance is 58.40591860680101... M_8.
The joint certificate improves that allowance by more than 4.37 times.
It does not extend the refined bound to all 1250 features.

Every diagonal of the symmetrized trial prime-pole cross Gram is strictly
negative. This is a proved diagonal correlation statement; no negative
semidefinite matrix order for the complete cross Gram is assumed. The
full mixed matrix is retained in the covariance calculation.

Joint source actions also tighten every same-parity prime-plus-pole head
interval by more than 21/20 relative to adding the previous component
intervals. The resulting complete original-head refinement still has
all eight diagonal intervals crossing zero. Generation and independent
exponential-primitive replay pass. No head floor, whole-aperture
positivity, or full archimedean/prime/pole covariance is certified.

## Signed physical source definitions

Keep B=11/10, x=B t, the same canonical carrier D, physical inclusion
i, and ||i||^2<=rho=252/257. Let R be the actual native Riesz map, V
the emitted rounded 32-mode trial map, M_8=R^*R its actual canonical
Gram, and E_phys=i(R-V). Define

    c(x)=cosh(x/2), s(x)=sinh(x/2),
    K_pole=2|c><c|-2|s><s|,
    F_prime=K_prime iV,
    F_pole=K_pole iV,
    F_joint=F_prime+F_pole.

K_prime is RC43's negative sum of both translations for each active
power 2,3,4,5,7,8,9. RC42's pole operator is retained with its original
positive-even and negative-odd signs. The actual canonical source is

    sigma_joint=i^*(K_prime+K_pole)iR.

Trial physical Grams, actual physical Grams, and actual canonical Grams
are distinct. This pass encloses physical entries and provides a
Loewner upper envelope for the canonical covariance. It does not
evaluate the actual canonical covariance entries or their projected
residual.

All input byte hashes are pinned: RC39 native attachment, RC43 primes,
RC42 poles, RC47 correlated Riesz error, and RC48 prime source covariance.
Cross-hashes are checked against those certificates. Historical
artifacts and other branches remain unchanged.

## Pole actions and translated exponential moments

For a trial column of parity j, set

    m_j=<exp(x/2),iV_j>_physical,
    z_j=<exp(x/2),F_prime,j>_physical,
    g_j=c if j is even, s if j is odd,
    epsilon_j=(-1)^j.

Reflection identifies m_j=<g_j,iV_j> and z_j=<g_j,F_prime,j>.
Consequently

    F_pole,j=2 epsilon_j m_j g_j,
    ||c||_2^2=B+sinh B,
    ||s||_2^2=sinh B-B.

The m_j intervals are recomputed more precisely and checked inside
RC42's trial moment intervals. Every active prime term contributes to
z_j. Substituting y=x+/-ell_n before integrating yields

    z_j=-B sum_n c_n [
         exp(-ell_n/2) integral_(-1+ell_n/B)^1 v_j(t)exp(Bt/2)dt
        +exp(ell_n/2) integral_(-1)^(1-ell_n/B) v_j(t)exp(Bt/2)dt],
    ell_n=log n, c_n=log p/sqrt(n).

The formula includes both original support truncations and translations.
Generation integrates a degree-100 rational Taylor polynomial for
exp(bt), b=B/2=11/20. Uniformly on |t|<=1 its tail is bounded by

    epsilon_exp=2 b^101/101! <10^-180,

because the remaining positive terms have ratio below 1/2. If
A_j=sum_n |V_(n,j)| in Legendre coefficients, |v_j(t)|<=A_j. Thus
each supported physical integral has tail at most 2B A_j epsilon_exp;
the translated moment error additionally pays the positive weights
c_n[exp(-ell_n/2)+exp(ell_n/2)]. No sampled exponential values certify
the error. Directed intervals enclose the remaining log, square-root
and exponential parameters.

Moment endpoints are rounded outward at denominator 10^35. The source
Gram endpoints are rounded at denominator 10^25. All same-parity joint
trial source-Gram interval widths are below 10^-22.

## Complete mixed physical covariance

For equal parity, the symmetrized cross covariance and pole covariance
are exactly

    X_ij=<F_prime,i,F_pole,j>+<F_pole,i,F_prime,j>
         =2 epsilon_i(m_j z_i+m_i z_j),
    O_ij=<F_pole,i,F_pole,j>=4m_i m_j ||g_i||_2^2,
    U_joint=U_prime+X+O.

For opposite parity all these entries vanish exactly. U_prime is the
complete RC48 trial prime source Gram, including every prime-prime and
orientation correlation. The validator adds X with its actual signed
intervals, rather than estimating its magnitude and discarding its
cancellation.

For example, the first physical trial source diagonal has the following
values, shown descriptively; exact rational enclosures are in the certificate:

| Contribution to feature-0 trial source squared norm | Value |
|---|---:|
| Prime source Gram | 9.08213396... |
| Pole source Gram | 44.56833227... |
| Symmetrized prime-pole cross term | -39.26374744... |
| Complete joint source Gram | 14.38671878... |

The negative cross term is essential to the joint norm bound. It is not
a negative value of the original Weil form.

## Whole-map transfer to actual sources

Let P be the physical native Gram and U_center the midpoint matrix of
the joint trial Gram. If h is its maximum entry halfwidth, then the
checked P>=I/8 inequality gives

    U_joint<=U_up=U_center+64h P.

Let B_err be RC47's whole-map physical Riesz error Gram bound. Reflection
makes this matrix exactly block diagonal by parity. RC43's physical
prime norm is at most k_prime, and RC42 gives the pole parity norms
2||c||^2 and 2||s||^2. Therefore the joint physical operator has the
safe parity bounds

    k_even=k_prime+2||c||^2,
    k_odd=k_prime+2||s||^2,

using the inherited outward norm endpoints. If S has diagonal k_even
on even coordinates and k_odd on odd coordinates, then

    [(K_prime+K_pole)E_phys]^*[(K_prime+K_pole)E_phys]
       <=S B_err S.

This follows by applying the two operator bounds separately to the
orthogonal even and odd physical subspaces. Young's inequality gives,
for every t>0,

    U_actual_phys<= (1+t)U_up+(1+1/t)S B_err S,
    sigma_joint^*sigma_joint<=A_t
       =rho[(1+t)U_up+(1+1/t)S B_err S].

The inclusion factor rho is applied as a matrix order bound, not by
scaling off-diagonal physical entry intervals. Exact rational PSD
bisection certifies lambda_t P-A_t>=0 for six rational Young parameters.
The best certified candidate in that finite set uses t=1/32. RC39's
actual M_8>=alpha P, alpha=8947777583/17179869184, then proves

    sigma_joint^*sigma_joint<=lambda P<=(lambda/alpha)M_8,
    lambda/alpha=13.336601410692442... <667/50.

The separate-component comparison is itself a valid bound:
if kappa_prime is RC48's source-Gram allowance and kappa_pole is RC42's
canonical pole operator norm, the triangle inequality gives

    ||sigma_joint a||_D
      <=(sqrt(kappa_prime)+kappa_pole)||R a||_D.

An upward rational square root yields the recorded squared allowance
58.40591860680101.... The exact certificate verifies that its ratio
to the joint allowance exceeds 437/100. This comparison applies to the
same actual eight-feature map.

## Source-specific joint head transport

Let e_j bound ||E_phys,j|| and let s_j be an upward square root of the
joint trial source diagonal. Self-adjointness of K_prime+K_pole gives,
within each parity block,

    |(H_actual_joint-H_trial_joint)_ij|
       <=e_i s_j+e_j s_i+k_parity e_i e_j.

The trial joint head is the RC48 trial prime head plus
2 epsilon_i m_i m_j. Actual intervals are intersected with the sum of
the previously certified actual prime and pole intervals. Their minimum
width improvement is 1.0542318908..., strictly above 21/20.

Actual physical joint source-Gram entries are also enclosed, paying
k_parity(e_i s_j+e_j s_i)+k_parity^2 e_i e_j. Their diagonal intervals
are intersected with the nonnegative axis. These physical entries are
not used as if they were actual canonical entries.

Add the new joint-head intervals to RC47's retained actual archimedean
intervals, and intersect with RC48's complete original-head intervals.
The diagonal endpoints below are rounded further outward for display:

| Native feature | Complete actual original Weil diagonal |
|---:|---:|
| 0 | [-0.357988, 0.433731] |
| 1 | [-0.119244, 0.197843] |
| 2 | [-0.170394, 0.221374] |
| 3 | [-0.123071, 0.177996] |
| 4 | [-0.103937, 0.158575] |
| 5 | [-0.092659, 0.126183] |
| 6 | [-0.046511, 0.161720] |
| 7 | [-0.035841, 0.150994] |

Every diagonal still contains zero. The interval refinement therefore
does not establish the required original head floor or a negative
original test-vector witness.

## Independent replay and remaining gate

Replay computes the pole moments using an exact exponential primitive:
for a polynomial p, solve q'+bq=p by backward coefficient recurrence,
then integral p(t)exp(bt)dt=q(t)exp(bt). For prime-source moments it
reconstructs the summed translated source on all 15 support segments
and applies that primitive to each segment. This differs from
generation's untranslated-variable substitution and Taylor integration.
Every independently enclosed moment lies inside the saved interval.
Rational replay verifies all signed mixed products, head/source error
transport, intersections and whole-map PSD inequalities.

    python scripts/validate_rpb108_rc49_prime_pole_covariance.py
    python scripts/validate_rpb108_rc49_prime_pole_covariance.py --replay certificates/rpb108_rc49_prime_pole_covariance.json

Generation and replay pass. Analytic source identities and the stated
operator/Cauchy/Young inequalities give the meaning of these checks;
this is not a Lean formalization.

The low-eight physical prime and pole source actions are now attached
with their mixed trial correlations and paid actual transfer. The
archimedean remainder source actions and their correlations with both
components remain to be evaluated. Full 1250-feature entries, precise
native solves and the full canonical projection remain open. RC44's
complement floor and RC45's conditioning bounds are unchanged. No new
positivity at aperture 1.10, RH/F4, or Lean closure is claimed.
