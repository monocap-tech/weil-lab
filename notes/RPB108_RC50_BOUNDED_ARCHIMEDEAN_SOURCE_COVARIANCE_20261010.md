# RPB108 RC50 — bounded archimedean remainder source covariance

2026-10-10. Parent RC49: `3218862c6ea2b37b54c49e553180531c8cd55569`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

The complete archimedean bounded-remainder self-covariance is now enclosed
on the eight native trials. Its paid actual-source transfer certifies

    sigma_arch^*sigma_arch <=25.05791810404235... M_8
                          <(12529/500)M_8.

This eight-feature canonical source allowance is below 25.058 M_8,
improving the inherited 61.533952065890475... M_8 bound. It does not
extend the refined allowance to the full 1250-feature map. Every
same-parity archimedean-head interval is more than 2.09 times narrower
than RC47's interval; the minimum improvement is 2.0910775957....

The complete original Weil head now has strictly positive diagonal
enclosures for **native features 6 and 7**. Exact parity decoupling and
the actual canonical Gram bounds additionally prove

    Q(h)>=(1/25)||h||_D^2
      for h in span{actual native Riesz representatives r_6,r_7}.

This is a two-dimensional subspace certificate. The full eight-feature
head floor, whole-aperture positivity, and complete mixed source residual
remain unresolved. Generation and reflected logarithmic-moment replay
pass. No RH/F4 or Lean closure follows.

## Source definition and endpoint cancellation

Use B=11/10, R_width=2B=11/5, y=(x+B)/R_width, and the inherited
canonical weight w(xi)=log(e+|xi|). The original archimedean multiplier
is a_arch(xi)=Re psi(1/4+i pi xi)-log pi. On supported polynomials,
RC46 and the canonical source framework give

    L_arch=T0+W+c_R I-K_reg,
    L_w=T0+W+c_R I+K_metric,
    K_arch=L_arch-L_w=-K_reg-K_metric.

Here T0 P_n=H_n P_n, W(y)=-(log y+log(1-y))/2, and
c_R=-gamma-log(2pi R_width). The same endpoint terms, constant and
Fourier convention are used in both formulas. The cancellation removes
the principal unbounded endpoint multiplication. It does not assert
boundedness of either full physical L_arch or L_w. The bounded physical
remainder K_arch, representing a_arch-w, retains the inherited global
norm bound ||K_arch||<8.

Let R_native denote the actual native Riesz map, V the emitted rounded
32-mode trials, i the physical inclusion with ||i||^2<=rho=252/257,
and M_8=R_native^*R_native. The source objects are

    F_trial=K_arch iV,
    F_actual=K_arch iR_native,
    sigma_arch=i^*F_actual.

This pass constructs a nominal physical trial source, encloses actual
physical source entries, and provides a canonical source-Gram Loewner
upper envelope on native features 0 through 7. Actual canonical source
entries and the full 1250-feature map remain unevaluated.

## Nominal logarithmic-polynomial source construction

RC38 represents the logarithmic-metric residual of a trial polynomial
as A_d(y)+B_d(y)log y+C_d(y)log(1-y). Subtracting its known target and
adding T0 V+c_mid V+W V isolates -K_metric V. This algebra is performed
on the emitted rational native coefficients, including their rounding.
The target used internally by the inherited builder cancels exactly;
no native Riesz representative is replaced by that target polynomial.

For the regular archimedean kernel, use RC46's degree-192 rational
coefficients r_p and its uniform remainder epsilon_reg<10^-23. For
v_j(y)=sum_m v_(j,m)y^m, the left convolution is

    left_j(y)=R_width sum_(p=0)^192 sum_(m=0)^31
       r_p R_width^p v_(j,m) p!m!/(p+m+1)! y^(p+m+1).

Reflection supplies the right convolution with the exact feature parity.
Subtracting their sum gives the nominal bounded-remainder source

    F_nom,j(y)=A_j(y)+B_j(y)log y+C_j(y)log(1-y).

The polynomial degree is at most 224. B_j(0)=0 and C_j(1)=0; the
remaining regular logarithmic convolutions have finite physical L2
norms. They are retained in every Gram and source/head integral.

## Paid source approximation error

The inherited constant enclosure has halfwidth
delta_c=488163/(2*10^9). RC38's total metric-source error is
2delta_c+epsilon_metric. That same epsilon_metric is recovered and
checked against the input residual certificate.

After cancellation of the common c_R I term, constant uncertainty in
K_metric alone changes its physical convolution kernel by

    delta_c sin(2pi e r)/(pi r).

This follows by differentiating the odd-power coefficient series with
respect to c_R: its dimensionless kernel is sin(2pi e R_width y)/(pi y).
In physical coordinates this is the Fourier projection kernel onto
[-e,e], restricted to the supported interval. Zero extension,
orthogonal projection and restriction all have norm at most one. Thus
its operator uncertainty is at most delta_c, with no extra identity
contribution.

Schur's test pays the regular archimedean truncation at
R_width epsilon_reg. Altogether

    ||(F_trial-F_nom)a||_2<=delta ||iV a||_2,
    delta>=delta_c+epsilon_metric+R_width epsilon_reg,
    delta<49/200000=0.000245.

Delta is rounded upward at denominator 10^30. The endpoint cancellation
is analytic; approximation errors and interval arithmetic remain paid.

## Complete archimedean self-covariance

Integrate every same-parity entry of F_nom^*F_nom using the six exact
logarithmic moment families. Writing a=k+1, H_a=sum_(j<=a)1/j and
H_a^(2)=sum_(j<=a)1/j^2, these are

    integral_0^1 y^k dy=1/a,
    integral_0^1 y^k log y dy=-1/a^2,
    integral_0^1 y^k log(1-y)dy=-H_a/a,
    integral_0^1 y^k (log y)^2 dy=2/a^3,
    integral_0^1 y^k (log(1-y))^2 dy=(H_a^2+H_a^(2))/a,
    integral_0^1 y^k log y log(1-y)dy
       =H_a/a^2+H_a^(2)/a-pi^2/(6a).

All polynomial products are integrated over the full supported interval
with dx=R_width dy. Opposite-parity entries vanish exactly. Directed
intervals enclose pi and the inherited entire-kernel coefficients; saved
Gram endpoints are rational at denominator 10^20. Same-parity entry
widths are below 10^-18.

The same source representation computes the nominal physical head
<iV_i,F_nom,j>. Paying delta sqrt(T_ii T_jj), where T is the physical
trial Gram, gives a true trial-remainder head enclosure. It is
intersected with RC46's inherited trial-remainder interval.

## Actual source and head transport

Let e_j be RC47's physical Riesz error allowance, v_j an upward square
root of T_jj, and s_nom,j an upward square root of the nominal source
Gram diagonal. Then the true trial action satisfies

    ||F_trial,j||_2<=s_j=s_nom,j+delta v_j.

For the actual bounded-remainder head, self-adjointness gives the entry
transfer error

    e_i s_j+e_j s_i+8 e_i e_j.

Add this to the paid true trial-remainder interval and RC47's refined
actual canonical M_8 interval, then intersect with the previous actual
archimedean interval. This replaces the global 8 sqrt(T_jj) allowance
in the linear terms by an evaluated source norm.

The actual physical source differs from the nominal one by at most
d_j=delta v_j+8e_j. Consequently its source-Gram entry error is
d_i s_nom,j+d_j s_nom,i+d_i d_j. Diagonal intervals are additionally
intersected with the nonnegative axis. These physical entries are not
substituted for actual canonical source entries.

For a whole-map canonical envelope, let Q_up be the nominal Gram center
plus 64h P, where h is the maximum entry halfwidth and the checked
physical native Gram satisfies P>=I/8. Let B_err be RC47's whole-map
physical Riesz error bound. A fixed Young inequality gives

    error_Gram <=D_err=(33/32)*64 B_err+33 delta^2 T.

This pays K_arch i(R_native-V) and F_trial-F_nom together. For any t>0,

    sigma_arch^*sigma_arch
      <=A_t=rho[(1+t)Q_up+(1+1/t)D_err].

Exact rational PSD bisection bounds A_t by lambda_t P for six rational
t values. RC39's actual M_8>=alpha P, alpha=8947777583/17179869184,
then gives A_t<=(lambda_t/alpha)M_8. No floating eigenvalue or
unpaid trial-to-actual identification is used.

## Validation and remaining correlations

Generation integrates all nine logarithmic products. Independent replay
uses reflection to reduce the same-parity pairing to five terms:

    R_width[<A_i,A_j>+2<A_i,B_j>_log_y+2<B_i,A_j>_log_y
       +2<B_i,B_j>_(log_y_squared)+2<B_i,C_j>_(log_y_log_1minusy)].

It also checks the head with the reflected two-term identity rather
than the original three-term integral. Every replayed nominal integral
lies inside the saved interval. Rational replay checks source/head
transport, historical intersections and the whole-map PSD bounds.

    python scripts/validate_rpb108_rc50_archimedean_source_covariance.py
    python scripts/validate_rpb108_rc50_archimedean_source_covariance.py --replay certificates/rpb108_rc50_archimedean_source_covariance.json

The low-eight archimedean self-covariance is now attached to the bounded
original remainder, with its actual-source error paid. Its correlations
with the prime and signed pole source actions remain to be evaluated.
The original matrix floor and full projected mixed residual remain open,
as do the full 1250-feature entries, precise solves and projection.
RC44's complement floor and RC45's conditioning statement are unchanged.
This is not Lean formalization. No new whole-aperture positivity,
RH/F4, or Lean closure is claimed.

## Refined complete original head and positive two-feature span

Combine the new actual archimedean intervals with RC49's actual joint
prime-pole head, then intersect with RC49's complete original intervals.
The diagonal enclosures below are rounded further outward for display:

| Native feature | Complete actual original Weil diagonal |
|---:|---:|
| 0 | [-0.204386, 0.280129] |
| 1 | [-0.020415, 0.099014] |
| 2 | [-0.070511, 0.121491] |
| 3 | [-0.023578, 0.078503] |
| 4 | [-0.008679, 0.063317] |
| 5 | [-0.007774, 0.041298] |
| 6 | [0.035377, 0.079832] |
| 7 | [0.038690, 0.076464] |

The saved exact lower endpoints for features 6 and 7 are positive.
Their ratios to the certified actual canonical diagonal upper bounds
exceed 0.04384548... and 0.04957680..., respectively. The validator
checks both inequalities Q_ii_lower>M_ii_upper/25 exactly. Both the
original head cross entry and canonical Gram cross entry between
features 6 and 7 vanish by opposite parity. Thus for complex a,b,

    Q(a r_6+b r_7)
       >=(1/25)[|a|^2 M_66+|b|^2 M_77]
       =(1/25)||a r_6+b r_7||_D^2.

RC39's positive canonical Gram lower bound ensures these actual
representatives are nonzero and independent. This proof uses actual
entry enclosures and paid source transfer, rather than positivity of
trial polynomials alone. Other head directions and their couplings
remain unresolved; a diagonal or two-feature result does not imply
the full head inequality.
