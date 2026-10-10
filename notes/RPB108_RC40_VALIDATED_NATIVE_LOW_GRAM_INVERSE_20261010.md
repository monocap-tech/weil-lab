# RPB108 RC40 — validated inverse of the low native canonical Gram

2026-10-10. Branch `research/rpb108-route-consolidation`.
Recovered parent: `1f071f92c77c5d35bf869614ca453b801da97387` (RC39).

## Result

RC39's enclosure of the first eight actual native Chebyshev feature
Gram entries now supplies a validated inverse and finite solves.
Let M_native be this actual eight-by-eight canonical Gram. RC40 emits
a compact rational center Q and its exactly verified inverse B=Q^(-1).
The actual inverse is enclosed by

    [1/(1+eta)] B <= M_native^(-1) <=[1/(1-eta)] B,

where eta is approximately 0.002197808446325 and is proved <11/5000.
For convenient outward decimal bounds,

    0.997807 B <= M_native^(-1) <=1.002203 B.

The certificate stores the exact rational factors, rather than relying
on these rounded displays. The center-normalized inverse error is
below eta/(1-eta), approximately 0.002202649447886.

For EVERY coefficient right-hand side b, let x=M_native^(-1)b and
x_hat=B b. The actual canonical coefficient norm is
||a||_(M_native)^2=a* M_native a. Then

    ||x_hat-x||_(M_native) <=eta ||x||_(M_native).

Thus the relative solve error is below 0.22% in the actual canonical
feature metric. This bound is simultaneous for all right-hand sides;
it is not a test on selected coordinate columns.

This closes the validated low-block inverse step of RC22's canonical
matrix interface. It does not evaluate the exact actual inverse or
validate an inverse for all 8600 features. This block inverse is not
the leading block of the inverse of the full 8600-feature Gram.

## Rational center and rounding transport

RC39 gives an exact rational enclosure center N and

    -tau M_phys <= M_native-N <=tau M_phys,

with M_phys the exact physical Chebyshev polynomial Gram for features
0–7. Its certified tau is approximately 0.001146546710.
The RC40 validator verifies by exact rational LDL that

    M_phys >=(1/8)I.

Round N entrywise to the nearest multiple of 10^-12, preserving
symmetry and all exact opposite-parity zeros. Denote this rational
matrix by Q, and let h=max_ij |Q_ij-N_ij|<=1/(2*10^12).
The Euclidean operator error is at most 8h. Therefore

    -epsilon_round M_phys <=Q-N<=epsilon_round M_phys,
    epsilon_round=8h/(1/8).

Combining this with RC39's actual Gram enclosure gives

    -epsilon M_phys <=M_native-Q<=epsilon M_phys,
    epsilon=tau+epsilon_round.

This pays the new entry rounding error at the matrix level. It does
not interpret an entrywise bound as a Loewner inequality without
conversion.

Exact rational LDL and bisection certify

    Q >=gamma M_phys,
    gamma=573590239297/1099511627776

(approximately 0.521677283629288). The complete rounding and inherited
actual Gram budget consequently implies

    -eta Q<=M_native-Q<=eta Q,
    eta=epsilon/gamma<11/5000<1.

In particular, Q and M_native are both positive definite.

## Exact inverse and actual inverse enclosure

The validator constructs B using exact rational elimination, verifies
B is symmetric positive definite, and checks both Q B=I and B Q=I
exactly. The center uses twelve-decimal rational entries so the emitted
inverse remains compact; no floating-point inverse is used.

The relative Gram bracket is

    (1-eta)Q <=M_native<=(1+eta)Q.

Inversion reverses Loewner order for positive definite matrices,
yielding the inverse bracket in the result. Equivalently,

    ||Q^(1/2)[M_native^(-1)-B]Q^(1/2)||
      <=eta/(1-eta)<1/450.

This is a validated enclosure of the ACTUAL canonical inverse.
The exact center inverse alone would not certify it; the inherited
RC39 error and new rounding budget are essential.

## Relative solve error in the actual metric

The same Gram bracket implies

    (1-eta) M_native^(-1) <=B<=(1+eta) M_native^(-1).

Thus the Hermitian matrix
M_native^(1/2) B M_native^(1/2) has spectrum in [1-eta,1+eta].
For b=M_native x,

    M_native^(1/2)(B b-x)
      =[M_native^(1/2) B M_native^(1/2)-I]M_native^(1/2)x.

Taking Euclidean norms proves the all-right-hand-side relative solve
bound. Since M_native is the true canonical Gram of the native Riesz
features, this coefficient norm is exactly the canonical norm of the
represented feature vector. No physical projection is substituted for
the canonical metric in the conclusion.

## Source-Gram subtraction interface

For this low block, let R be the exact native Riesz map, sigma the
actual bounded remainder source map, V_src=R* sigma, and U=sigma* sigma.
These original Weil source matrices have not been computed here.
If their entries are later certified, RC22's exact residual Gram is

    Gamma=U-V_src* M_native^(-1) V_src.

Set S=V_src* B V_src>=0. The validated inverse immediately supplies

    U-[1/(1-eta)]S <=Gamma<=U-[1/(1+eta)]S.

This specifies the safe direction for future source-Gram subtraction.
Subtracting S without the inverse error factors would not by itself
certify the desired upper bound on Gamma. Additional enclosures for
U and V_src must also be transported when they are approximate.
This interface is for the eight-feature block, not the complete
8600-feature head and its complement.

## Reproduction, execution and scope

Run from the repository root:

    python scripts/validate_rpb108_rc40_native_low_gram_inverse.py > /tmp/rc40.json

The input defaults to the committed RC39 native low Gram certificate;
an explicit input path is also accepted. Proof data are in
`certificates/rpb108_rc40_native_low_gram_inverse.json`, including
the input SHA-256 digest, compact rational center, exact inverse,
rounding budgets, relative Gram error and inverse factors.

Execution: PASS. Physical Gram coercivity, center symmetry and parity,
rounding budget, quantitative center lower bound, relative error below
0.0022, exact inverse identities and positivity passed. A separate
saved-certificate replay checked the inverse and inherited enclosure
budgets. RC40's finite computations use exact rational arithmetic;
the actual Gram attachment inherits RC39 and RC38's analytic plus
interval assumptions. This is not a Lean theorem.

Next: certify the original Weil head and remainder source matrices
for this low native block, or extend the certified native feature
range. Gram positivity and validated inversion do not establish the
original Weil head floor. The other 8592 features, the full native
projection, source-cross acceptance, aperture extension and RH/F4
remain open. Only this research branch receives new files; historical
artifacts are preserved.
