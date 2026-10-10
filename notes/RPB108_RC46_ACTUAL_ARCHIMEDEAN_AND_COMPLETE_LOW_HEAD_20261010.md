# RPB108 RC46 — actual archimedean attachment and complete low-eight Weil head

2026-10-10. Parent RC45: `14c5449b8fe6dd8cef3f5da96744816805e3e38d`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

All 36 upper-triangular entries of the **actual** original Weil head on
native features 0 through 7 are now enclosed. This attaches the original
archimedean form to RC43's complete active prime-power head and RC42's
signed pole head. Opposite-parity entries vanish exactly. The degree-192
regular-kernel approximation has uniform error below 10^-23, and an
independent exact replay verifies the polynomial integrals and assembly.

The resulting intervals do **not** certify a positive head floor. Every
diagonal interval contains zero. These are error enclosures, not negative
witnesses for the original form. The current native Riesz approximation
and coarse bounded-operator transport dominate the interval widths.
Neither the mixed source covariance nor the full 1250-feature head or
projection is computed. RC44's complement floor and RC45's conditioning
bounds are unchanged; no new aperture positivity or RH/F4 closure follows.

## Original archimedean kernel, including endpoint logarithms

Use the inherited carrier, B=11/10, R=2B=11/5, Fourier convention
exp(-2pi i xi x), and canonical metric w(xi)=log(e+|xi|). The original
archimedean multiplier is

    a_arch(xi)=Re psi(1/4+i pi xi)-log pi.

Euler's digamma series gives

    Re psi(1/4+i pi xi)-psi(1/4)
      =2 integral_0^infinity j(r)[1-cos(2pi xi r)]dr,
    j(r)=exp(-r/2)/(1-exp(-2r))=exp(r/2)/(2sinh r).

Indeed each Euler-series term is its elementary Laplace integral; setting
the Laplace variable to 2r gives the displayed frequency normalization.
Plancherel therefore writes the form as the mass term
psi(1/4)-log pi plus integral j(r) times twice the mass minus the two
translated overlaps. The overlaps vanish when r>R. Split off 1/(2r)
on (0,R), and put

    r_reg(r)=j(r)-1/(2r),
    (K_reg f)(x)=integral_(-B)^B r_reg(|x-y|)f(y)dy.

The singular part has the RC26/RC30 endpoint-logarithm identity

    L_arch=T0+W_B+c_R I-K_reg,
    T0 P_n=H_n P_n,
    W_B(y)=-(log y+log(1-y))/2,
    y=(x+B)/R,
    c_R=-gamma-log(2pi R).

Here H_n is the harmonic number and P_n the Legendre polynomial. The
formula is used as a quadratic-form identity on supported polynomials;
it retains both endpoint logarithms of their zero extension. It does not
assert that the full physical archimedean operator is bounded on L2.

For clarity, the constant has the same normalization as the canonical
logarithmic metric, rather than a new fitted constant. Its value follows
directly from the kernel split:

    c_R=psi(1/4)-log pi
       +lim_(epsilon->0)[2 integral_epsilon^infinity j(r)dr+log epsilon]
       -log R.

Writing z=exp(-epsilon/2), the integral is atanh z+atan z. The limit is
log4+pi/2. Euler's quarter identity is
psi(1/4)=-gamma-pi/2-3log2. One derivation uses
A_N=sum_(k<N)1/(4k+1), C_N=sum_(k<N)1/(4k+3):
A_N+C_N=H_(4N)-H_(2N)/2 and A_N-C_N tends to pi/4 by the
Leibniz series. Thus 4A_N=2H_(4N)-H_(2N)+2(A_N-C_N), and Euler's
limit log N-4A_N gives that identity. Combining the constants yields c_R.

## Uniform regular-kernel enclosure

Let F(z)=z j(z)=exp(z/2)/(2(sinh z/z)), with its removable value at zero.
Its exact Taylor coefficients satisfy

    a_n=1/(2^(n+1)n!)
        -sum_(2<=k<=n, k even) a_(n-k)/(k+1)!,
    a_0=1/2, a_1=1/4, a_2=-1/48.

The regular-kernel polynomial is sum_(p=0)^192 a_(p+1) r^p.
On |z|=3, |sinh z|>1/10: if |Re z|>=1/10, use
|sinh z|>=|sinh Re z|; otherwise |Im z|>sqrt(8.99)>2 and
|Im z|<=3<pi, so |sin Im z|>=sin3>1/10. Also exp(Re z/2)<5.
Consequently |F(z)|<75. Cauchy's coefficient bound and a geometric
tail give, throughout 0<=r<=R,

    |r_reg(r)-sum_(p=0)^192 a_(p+1)r^p|
       <=epsilon_reg=(375/4)(11/15)^193
       =9.443794197058557... *10^-25 <10^-23.

The script checks sin3>1/10 by an alternating lower partial sum and
exp(3/2)<5 by a positive partial sum with a geometric tail. No sampled
kernel values certify this bound. Schur's test gives physical convolution
operator error at most R epsilon_reg.

## Exact polynomial head and error transport

The actual native Riesz representatives r_i are those of RC39. Use the
emitted 32-by-8 native trial coefficients V, including their rounding,
rather than substituting an unrounded solve. Let P be RC39's physical
native Gram, T=V^*D_mass V the physical trial Gram, and
H_metric=V^*Ghat_32 V the nominal canonical trial Gram. RC38 certifies
the metric-center error E in the physical mass metric; RC39 certifies

    (R_native-V)^*(R_native-V)<=beta P,
    beta=91276884027/64250000000000,
    ||i||^2<=rho=252/257.

All these errors are canonical except where the physical metric is
explicitly named. In y coordinates write v_j(y)=sum_m v_(j,m)y^m.
The left half of the polynomial convolution is exactly

    left_j(y)=R sum_(p=0)^192 sum_(m=0)^31
        a_(p+1) R^p v_(j,m) p!m!/(p+m+1)! y^(p+m+1).

For equal parity, its full energy is 2R integral_0^1 v_i(y)left_j(y)dy.
For unequal parity the energy is zero. The endpoint moments are exact:

    integral_0^1 y^q W_B(y)dy
      =1/[2(q+1)^2]+H_(q+1)/[2(q+1)].

Thus the nominal trial archimedean head is the endpoint matrix plus
sum_n H_n mass_n V_(n,i)V_(n,j), plus c_mid T, minus the polynomial
kernel energy. The inherited enclosure of c_R uses

    c_mid=(-3203794213-3203306050)/(2*10^9),
    delta_c=488163/(2*10^9).

Subtract H_metric from this nominal head to evaluate the trial head of
the bounded physical remainder a_arch-w. The combined trial-entry error
is at most

    (E+delta_c+R epsilon_reg) sqrt(T_ii T_jj).

RC17's inherited global physical bound ||a_arch-w||<8 is justified by
the CC37 archimedean argument (blob
`a8a4ec58ebc43745d73630b97188cac1597b15ed`). That archimedean bound
is global and independent of the earlier arithmetic cap. It combines
|psi(1/4+i pi xi)-log(1/4+i pi xi)|<=4 with a logarithmic comparison
of magnitude strictly below 4. Only this remainder is physically bounded.

Set e_i=sqrt(rho beta P_ii), v_i=sqrt(T_ii). Replacing the two trial
arguments by their actual native representatives costs at most

    8(e_i v_j+e_j v_i+e_i e_j).

Adding RC39's actual canonical Gram entry enclosure then gives the actual
archimedean head entry. This uses the exact decomposition of the
canonical archimedean operator as I+i^*(a_arch-w)i. The large transfer
allowance is paid explicitly; trial polynomials are not identified with
the actual Riesz representatives. Rational endpoints are rounded outward.

## Complete original head and current precision obstruction

For each entry the validator adds the actual archimedean interval to the
RC43 prime interval and RC42 signed pole interval. RC43 includes all seven
active prime powers 2,3,4,5,7,8,9, both translation orientations and their
log(p)/sqrt(n) coefficients. Both signed poles are retained. The complete
diagonal intervals below are displayed with further outward rounding:

| Native feature | Actual original Weil diagonal enclosure |
|---:|---:|
| 0 | [-2.573574, 2.682122] |
| 1 | [-0.556188, 0.634725] |
| 2 | [-0.968798, 1.035047] |
| 3 | [-0.819778, 0.874725] |
| 4 | [-0.813407, 0.884192] |
| 5 | [-0.766024, 0.799599] |
| 6 | [-0.701277, 0.832794] |
| 7 | [-0.672424, 0.787642] |

The certificate contains exact rational endpoints for all entries.
Diagonal uncertainty alone prevents these enclosures from proving the
required positive matrix floor. In particular, interval midpoints are
not certified eigenvalues or positivity evidence. Increasing the regular
kernel degree would not address the main error: its present tail is
already far smaller than the native and operator-transfer allowances.
The immediate useful precision frontier is tighter native Riesz error
and sharper source transport.

For the whole actual bounded archimedean remainder source
sigma_arch=i^*(a_arch-w)i R_native, the same global bound supplies

    sigma_arch^*sigma_arch <=(8rho)^2 M_native.

This is a coarse component envelope. Adding separate component envelopes
does not evaluate the mixed archimedean/prime/pole covariance or the
projected source residual required by the sufficient positivity gate.

## Validation and outstanding gate

Generation and independent replay pass. Replay obtains the coefficients
through a different exact division,
F(r)=exp(-r/2)/(2D(r)), D(r)=(1-exp(-2r))/(2r), checks endpoint integrals
in the Legendre basis, and computes direct triangle moments without
constructing the convolved polynomial. It verifies every nominal trial
entry, actual transport enclosure, input hash, complete-head component
sum, and the component source bound.

    python scripts/validate_rpb108_rc46_native_archimedean_head.py
    python scripts/validate_rpb108_rc46_native_archimedean_head.py --replay certificates/rpb108_rc46_native_archimedean_head.json

The script's defaults use the published RC38, RC39, RC42 and RC43
certificates. Their byte hashes are pinned in the new certificate.
Analytic kernel identities and the inherited form conventions are proved
above and in the cited predecessors; this is not Lean formalization.

RC46 closes the missing low-eight component attachment, while leaving
the original head floor unresolved. Full 1250-feature entries and
projection, validated precise native solves, and complete mixed source
covariance remain open. Historical artifacts and other branches are
preserved. No positivity at aperture 1.10, RH/F4, or Lean closure is claimed.
