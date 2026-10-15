# RC268 — full-range two-pivot Schur reduction

Parent: `9fc7ab304abc506d00e38524350f1eaf62f55cb5` (RC267).
Branch: `research/rpb108-route-consolidation`.

RC268 incorporates the two certified source gaps into the COMPLETE chosen
augmentation range. It gives an exact remaining Schur problem of dimension
637: 247 even and 390 odd coordinates, with all coupling payments retained.
It also improves the original operator's nonpositive spectral-dimension
upper bound from 639 to 637, counting both negative and zero modes.

This is not original positivity or Stage I closure. The remaining Schur
matrix has not been evaluated or proved positive. The actual augmentation's
rank stays 639; 637 counts unresolved Schur coordinates, not a required
number of separate solves or a newly observed number of negative modes.

| Quantity | Even | Odd | Total |
| --- | ---: | ---: | ---: |
| Exact chosen augmentation rank, unchanged | 248 | 391 | 639 |
| Certified positive signed pivots | 1 | 1 | 2 |
| Remaining exact Schur dimension | 247 | 390 | 637 |
| Original nonpositive spectral dimension upper | 247 | 390 | 637 |

The previous count upper for original eigenvalues strictly below 0.01 is
NOT sharpened by this pass. Its parity bounds remain 248 and 391. The new
bound is at threshold zero, includes nullity, and is a form-inertia result.
It does not transfer numerical eigenvalue thresholds between inequivalent
operator metrics.

## Actual signed form and its finite support

Work on the shared D-energy Hilbert space V from RC230. Let

    N = N0+Kaug > 0,
    Kaug = Q*_D Q,
    Baux = Q N^-1 Q*_D.

Q contains sqrt(lambda) times the actual fixed rational Fhat in each parity;
its adjoint is taken in D energy and the actual frequency metric. Lambda
can differ between parity blocks. This is the RC115 augmentation throughout,
not the ideal band model used to bound its actions.

The signed source form is represented in D energy by

    S = N0-N0 N^-1 N0.

Expanding N0=N-Kaug, without assuming any commutation, gives

    S = Kaug-Kaug N^-1 Kaug
      = Q*_D (I-Baux) Q.

This identity is exact even if the original N0 is singular or indefinite.
Only the already established positive inverse N^-1 is used.

RC230 proves rank(Q)=639 and

    W=range(Q*_D)=range(Kaug)
      = span{P0,P2,...,P494} direct-sum span{P1,P3,...,P781}.

The Chebyshev and Legendre spaces here coincide as complete parity
polynomial spaces. D^-1 maps each space bijectively to itself because its
harmonic diagonal is strictly positive. No approximate Riesz image or
eight-source factorization is substituted for this exact range.

Since Kaug is finite rank, W is closed and W-perp_D=ker(Q)=ker(Kaug).
The form S annihilates W-perp_D and maps into W. Thus S is fully supported
on this known finite range. Its restriction to W, not an arbitrary infinite
test-space restriction, is the full finite signed problem.

## Why the signed finite inertia equals the original nonpositive inertia

Put Y=range(Q) in the actual frequency Hilbert space. Q restricted to W
is a bijection W to Y: it is injective because W intersects ker(Q) trivially,
and it is onto by the orthogonal decomposition of V. Therefore the identity
above is a congruence between the finite form S|W and (I-Baux)|Y.
On Y-perp the auxiliary I-Baux is exactly the identity.

To connect to the original operator, consider the bounded block form

    [ N       Q*_D ]
    [ Q       I    ].

Eliminating the positive N block gives the Schur complement I-Baux.
Eliminating the positive auxiliary identity gives N-Q*_D Q=N0.
These are bounded invertible triangular congruences; they preserve the
negative index and the kernel dimension. Consequently

    n_negative(N0) = n_negative(S|W),
    dim ker(N0) = dim ker(S|W).

The positive infinite-dimensional identity portions do not contribute to
these counts. This is not an equality of the complete positive inertia
counts of an infinite operator and a finite matrix.

The canonical original A_Q and D-energy N0 represent the SAME original
form on the common domain, as established by RC230. Their metrics are
equivalent, aD<=L<=2D. Hence their negative form indices and nullities agree,
even though their numerical spectra need not agree and M and N need not
commute. The positive augmentation and finite-rank correction keep the
nonpositive spectral subspace finite dimensional. Thus the displayed
negative-plus-nullity count bounds the actual original nonpositive spectral
dimension in either formulation.

The abstract congruence uses full-range injectivity, not a computed
conditioning estimate for the 639-dimensional frequency Gram. Numerical
Gram conditioning remains unclaimed. Strict positive definiteness of the
complete finite signed form would imply ||Baux||<1, but is not established
by the two pivots alone.

## Certified actual pivot block

For a polynomial Pj, the diagonal signed form is exactly

    sigma_j = <Pj,N0 Pj>_D
                -<N0 Pj,N^-1 N0 Pj>_D.

RC267 supplies positive lower bounds for j=0 and j=1 after all original,
rational-augmentation, source, inverse and infinite-tail payments:

    sigma_0 >= 0.0014526303292729818 (display approximation),
    sigma_1 >= 0.013865017338385115  (display approximation).

The certificate stores the inherited EXACT rational endpoints. N0, N and
N^-1 preserve actual reflection parity, as does the fixed augmentation.
This follows from the original reflection-symmetric kernels and paired
prime translations and the separate even/odd rational kernel blocks.
It is not inferred merely from truncated numerical source coefficients.
The opposite-parity signed pairing is consequently exactly zero.

In the ordered pivot basis (P0,P1), the actual block is therefore

    Gamma=diag(sigma_0,sigma_1) > 0.

The validator also normalizes the lower bounds using the actual D-energy
upper norms mass(j)*(H_j+s_upper). This gives a common signed-form floor
on the pivot span of approximately 0.0001736866106 in D energy, and half
that in canonical energy using L<=2D. These floors concern the signed form
on this pair, not a positive lower floor for the entire original operator.

Inverse pivot upper bounds are approximately 688.4063894 even and
72.1239632 odd. Exact outward bounds, including lower inverse endpoints,
are saved. The two pivots use the current actual gaps, not the positive
augmented coercivity floors or the earlier canonical eight-source gate.

## Exact 637-dimensional remaining Schur form

Choose the complete remaining basis

    even: P2,P4,...,P494  (247 coordinates),
    odd:  P3,P5,...,P781  (390 coordinates).

In the full range W, order the signed matrix as

    S_W = [ Gamma   C  ]
          [ C*      F  ].

The exact triangular congruence with upper-right block -Gamma^-1 C gives

    diag(Gamma, R),   R=F-C* Gamma^-1 C.

Thus the entire original nonpositive inertia equals that of R, including
kernel dimension. In particular it is at most dim(R)=637, with parity
bounds 247 and 390. The remaining block R is itself parity separated.
The two cross columns are not zero: only their OPPOSITE-parity entries
vanish. Every same-parity coupling must be retained or paid.

This removes two positive pivots from the SIGNED problem; it does not remove
two channels from the actual rational augmentation. Dropping C*Gamma^-1 C
would be an invalid positivity inference. It is subtracted here because
this is a Schur reduction of S. The earlier inverse-response variational
residual correction is still ADDED in its own identity; no correction sign
is transferred between the two formulas.

## Concrete remaining numerical acceptance contract

Let Glo=diag(the two certified pivot lower bounds), and suppose a future
calculation gives a full remaining-block lower enclosure Flo and a cross
column approximation Chat with true error E=C-Chat. Then

    Gamma^-1 <= Glo^-1.

For any chosen rational theta>0, matrix Young gives the valid lower bound

    R >= Flo
           -(1+theta) Chat* Glo^-1 Chat
           -(1+1/theta) E* Glo^-1 E.

A certified upper Loewner enclosure of the weighted ERROR GRAM
E*Glo^-1 E is required; separate entrywise magnitudes do not silently supply
its covariance. With exact cross columns E=0 one may directly use the
sharper Flo-C*Glo^-1 C without the Young allowance.

A positive definite lower bound for this complete remaining form would
close the full signed criterion. A negative lower bound would not by itself
be a negative actual witness. RC268 specifies this concrete contract but
does NOT evaluate Flo, Chat or the cross-error Gram. Structured or matrix-free
uniform bounds remain possible; 637 independent solves are not mandated.

## Exact controls and logical sharpness

The validator implements exact symmetric congruence elimination, including
two-by-two pivots when all diagonal entries are zero. It tracks positive,
negative and zero counts separately. A [[0,1],[1,0]] control checks the
zero-diagonal indefinite case.

Four rational four-dimensional controls preserve parity and use a
nonidentity D metric, a different canonical L metric, and noncommuting M,N.
They check N=M H, both original form representations, the actual signed
identity, the auxiliary inertia, the two-pivot triangular congruence and
the weighted cross-column error payment. Their remaining forms are:

- Two negative directions, despite every signed diagonal being positive.
- Two zero directions, showing nullity must be included.
- One negative and one zero direction.
- A positive definite remaining form.

The first is a direct nonimplication control: both pivot tests and even all
diagonal tests can pass while off-diagonal coupling prevents positivity.
These are ABSTRACT rational controls, not negative Weil directions or
arithmetic counterexamples.

Appending 246 even and 389 odd independent negative scalar blocks to the
four-dimensional negative control gives the same rank/parity dimensions
248+391=639 with exactly 637 negative directions and the same two positive
pivots. The scalar blocks can have N0=-1, Kaug=4, N=3. Thus 637 is the sharp
universal nonpositive bound from these two pivots and rank information alone;
further improvement requires additional actual arithmetic/response evidence.
The actual original operator is not asserted to attain this upper bound.

## Validation, custody and remaining scope

Generation and exact reverse-order replay verify 239 inherited blob pins,
the exact range partition, both positive actual pivot endpoints, D/canonical
normalizations, and all rational matrix controls. Earlier expensive source
and Fourier calculations are reused by immutable pins. The analytic
full-range and common-form inertia proof above is part of the certificate;
finite controls illustrate and check the algebra, rather than numerically
evaluating the actual unevaluated 637-dimensional form.

From repository root:

    python scripts/validate_rpb108_rc268_two_pivot_schur_reduction.py --output certificates/rpb108_rc268_two_pivot_schur_reduction.json
    python scripts/validate_rpb108_rc268_two_pivot_schur_reduction.py --output certificates/rpb108_rc268_two_pivot_schur_reduction.json --replay

The original actual augmentation is unchanged. Both current source tests
stay positive. The complete signed response, full auxiliary norm below one
and original positivity remain unproved. The separate eight-source
canonical inverse width stays 485647/1000000. Stage I, RH, F4 and Lean remain
open/false.

Next: materialize or uniformly bound the 247-even/390-odd remaining Schur
form and its two weighted cross columns, with all discarded-range and
cross-error payments retained.
