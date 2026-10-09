# RPB108 — DNE1 weighted native contact conductance

**Inherited original pole-free form:** H_a is the complete archimedean-plus-prime native signed form, with both original Hermitian pole cross terms removed and no other modification. CC43 gives its simple nonnegative even physical ground state phi_a and lowest eigenvalue lambda_0(a).

**Native jump kernel:** j(d)=exp(-|d|/2)/(1-exp(-2|d|)), d != 0. Every active prime-power shift has positive conductance coefficient c_n=Lambda(n)/sqrt(n), ell_n=log n. They are weights after the ground-state transform, not original positive terms of H.

**Ground-state product core:** h=phi_a*u where u is a bounded real smooth Lipschitz multiplier. This multiplication preserves the supported logarithmic form domain. Neither phi_a>0 a.e., h/phi_a bounded, nor density of this product core in the full D_a is asserted without separate proof.

**Native weighted jump energy D_phi(u):**

    (1/2) int int j(x-y) phi(x)phi(y)(u(x)-u(y))^2 dxdy
       + sum_(ell_n<=2a) c_n int phi(x)phi(x+ell_n)(u(x)-u(x+ell_n))^2 dx.

The exact identity is H_a(phi*u)-lambda_0||phi*u||_2^2 = D_phi(u). It is a ground-state/Picone representation, not an assertion that H_a is positive (lambda_0 can be negative).

**Odd reflected conductance:** for odd real u and even phi, the continuous part folds onto x,y in (0,a) as

    int int phi(x)phi(y)[ j(|x-y|)(u(x)-u(y))^2 + j(x+y)(u(x)+u(y))^2 ] dxdy.

Because j decreases, this is at least

    4 int_0^a phi(x)u(x)^2 [int_0^a j(x+y)phi(y)dy] dx.

Prime conductances are additional nonnegative terms.

**Ground-depth surplus criterion:** A lower bound for D_phi(u)/||phi*u||_2^2 that is strictly greater than -lambda_0 on every relevant non-ground, parity-and-moment-constrained vector would exclude a higher zero-moment H_a null, PROVIDED the bound extends from the product core to the actual supported eigenfunction domain. This is not established by positivity of conductances alone; the possible equality is tested by two-point crossing controls.

**DNE1:** first mathematical investigation on the independent DNE branch. DNE0 was organizational custody only.
