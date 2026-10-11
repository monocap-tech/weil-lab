# RPB108 RC103 — Polynomial complement inverse and lifted responses

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC102, commit `ac1cc2a9529d766751d566e177ecded1af533b66`.
Aperture B=1.10. Actual sufficient head H has rank 1250.

RC103 provides a structural alternative to RC102's rejected scalar-floor correction transport. It preserves the actual complement operator and constructs a polynomial approximation to its inverse. The correction residual can then be made uniformly small, with certified finite degree budgets, before estimating the remaining six lifted responses.

This does not evaluate those lifted responses or prove the remaining strong floor. It removes one estimate obstruction in a conditional completion route; whole-aperture positivity remains open. The six-dimensional positive certificate and nonpositive spectral-dimension upper 1244 are unchanged.

## Keep the actual complement inverse

Let A_Q be the original canonical Weil operator. With the actual projections onto H and E=H orthogonal complement, set

    D=P_E A_Q P_E|E,    B=P_H A_Q P_E,
    A_H=P_H A_Q P_H,
    F=A_H-B D^(-1)B*.

The accepted complement lower is D>=alpha I with alpha=247/2500. Hence D is invertible, and full original positivity is equivalent to positivity of the exact effective head F. RC100/101 used the sufficient lower

    T_alpha=A_H-alpha^(-1)B B*.

Since D^(-1)<=alpha^(-1)I, F>=T_alpha. The existing three-input weak lower L in each parity therefore remains valid: W*F W>=L>0. Here W consists of the three known canonical vectors in that parity; S=H orthogonal W is the remaining strong space.

RC102's correction estimate used the whole vector alpha^(-1)P_E A_Q W. RC103 instead approximates the true complement solve D^(-1)P_E A_Q W. These are different constructions.

## A smaller spectral upper for the complement

The original operator is A_Q=I+i* K i, with bounded physical remainder K. On E, RC95's embedding norm tau1250 gives

    ||D-I|| <= tau1250^2 kappa,
    alpha I<=D<=b I,
    b>=1+tau1250^2 kappa.

Here kappa is the corresponding complete physical parity norm from RC66. The spectral upper is rounded upward to a 10^-6 rational grid:

| Parity | Certified complement spectral upper b |
| --- | ---: |
| Even | 2067533/500000 = 4.135066 |
| Odd | 3239591/1000000 = 3.239591 |

This uses the complement embedding, rather than the global embedding used for the full original operator norm. The bounds alpha and b apply to the complete infinite complement, not just a numerical sample or trial subspace.

## Uniform polynomial inverse theorem

For n>=1, define

    c=(b+alpha)/(b-alpha)>1,
    p_n(x)=T_n((b+alpha-2x)/(b-alpha))/T_n(c),
    q_(n-1)(x)=(1-p_n(x))/x,
    epsilon_n=1/T_n(c).

T_n is the Chebyshev polynomial. Because p_n(0)=1, the quotient q_(n-1) is an actual polynomial of degree n-1. On [alpha,b], its affine argument lies in [-1,1], so |T_n|<=1 gives

    |1-x q_(n-1)(x)|<=epsilon_n<1.

The selfadjoint functional calculus therefore proves

    ||I-D q_(n-1)(D)||<=epsilon_n,
    ||D^(-1)-q_(n-1)(D)||<=epsilon_n/alpha.

The quotient is positive on the spectral interval. No small-norm assumption ||D-I||<1 is needed; the inherited bounds would not support a simple Neumann series.

Let R=P_E A_Q W and form the canonical complement lift

    Y=q_(n-1)(D)R,
    r=R-DY=p_n(D)R.

The existing common source coupling upper G bounds R*R. Consequently

    Gram(r)<=epsilon_n^2 G.

This is an operator theorem for the actual original sources and complete complement. It constructs Y through the original operator, but does not numerically evaluate Y or certify a finite approximation to it. Polynomial evaluation can apply D to a block of three vectors per parity; the theorem requires no dense 1244-direction head matrix. A verified implementation still has to account for operator-action and source approximation errors.

## Residual-controlled exact completion

There are two exact identities, valid for any lift Y into E if r=R-DY:

    W*F W = Gram_A_Q(W-Y)-r*D^(-1)r,
    P_S F W = P_S A_Q(W-Y)-P_S B D^(-1)r.

Here Gram_A_Q denotes the mixed Weil form of the lifted vectors, not their canonical norm Gram. The identities follow by expansion and D^(-1)R=Y+D^(-1)r. The first gives a residual-paid weak lower even for an approximate lift. For the polynomial lift, it also shows convergence to the exact Schur weak form; the old lower L is already retained independently by F>=T_alpha.

For the cross identity, use RC102's bound

    ||B||^2<=g=rho tau1250^2 kappa^2,
    rho=252/257,
    V=(g/alpha^2)G.

Then

    Gram(P_S B D^(-1)r)<=epsilon_n^2 V.

If a new arithmetic or structural estimate gives U_lift>=Gram(P_S A_Q(W-Y)), a common Young inequality yields

    Gram(P_S F W)<=2 U_lift+2 epsilon_n^2 V.

Thus the following is a sufficient completion package in each parity:

    F|S>=beta I,
    U_lift<=beta L/4,
    epsilon_n^2 V<=beta L/8.

The corrected cross Gram is then at most 3 beta L/4. Its Schur budget has slack at least beta L/4>0, proving F>0 and therefore positivity of the full original form. The two substantive remaining estimates are the strong floor and the lifted-response Gram.

The same route works with any rigorously computed approximate lift Yhat. Certify the actual posterior residual Gram(R-DYhat) and use it in place of epsilon_n^2 G. A nominal residual without its original-source and arithmetic-action errors is insufficient.

## Exact degree budgets

RC103 computes an exact relative upper lambda_V with V<=lambda_V L. Approximate displays are 2358.317979619 in the even block and 347.2041126185 in the odd block. It then finds the first integer n satisfying

    epsilon_n^2 lambda_V<=beta/8.

All beta values below are hypothetical strong-floor targets. None is proved for the original remaining strong block.

| Hypothetical beta | Even residual degree n | Odd residual degree n |
| --- | ---: | ---: |
| 1 | 19 | 14 |
| 10^-3 | 30 | 23 |
| 10^-6 | 41 | 33 |
| 10^-9 | 52 | 43 |
| 10^-12 | 63 | 53 |

The inverse polynomial degree is n-1. The certificate stores exact epsilon_n, inverse-error norm upper, residual correction budget and conditional lifted-response target. It verifies the corresponding Loewner inequality beta L/8-epsilon_n^2 V>=0 with exact rational arithmetic.

Minimality means first degree satisfying this particular relative-upper budget, not minimal possible work for the actual arithmetic operator or an optimal degree among all proofs. In particular, a posterior residual certificate may be much cheaper than a uniform spectral budget.

Because c>1, T_n(c) grows without bound. For every positive beta, some finite n meets the residual allowance. RC102's unavoidable failure of its fixed norm-transport upper therefore does not persist for this inverse-lift construction. This does not assert that the lifted-response target itself is small: its arithmetic correlations still need proof.

## Verification and limits

Direct inputs are RC102, RC101, RC100, RC95 and RC66. Byte SHA-256 digests, predecessor crosslinks, original source upper G, corrected weak lower L, complete physical norm and complement floor/embedding are checked. No source integrals are added and no Lean files are changed.

Generation evaluates T_n(c) by recurrence. Independent replay uses the positive binomial formula

    T_n(c)=sum_k binom(n,2k)c^(n-2k)(c^2-1)^k.

It recomputes the degree budgets and exact PSD tests and requires equality with the saved certificate. In illustrative noncommuting finite-dimensional controls, generation evaluates inverse polynomials by Horner recurrence; replay uses powers and an explicit adjugate complement inverse. Both verify the quotient, residual Gram and approximate-lift Schur identities. The illustrative full operator and exact effective head are positive while scalar-floor elimination rejects the same control. These controls are algebraic examples, not additional original arithmetic certificates.

The next task is to realize and rigorously control these six original lifted responses, or supply a structural theorem bounding them, while separately establishing an effective strong floor. This is an alternative sufficient route at 1.10; spectral exclusion, arithmetic factorization and Global/F4 first-contact exclusion remain available. A separate 1.10 positivity calculation is not declared logically mandatory.

- `scripts/validate_rpb108_rc103_complement_inverse_lift.py`
- `certificates/rpb108_rc103_complement_inverse_lift.json`
- `notes/RPB108_RC103_POLYNOMIAL_COMPLEMENT_INVERSE_AND_LIFTED_RESPONSE_ROUTE_20261011.md`
