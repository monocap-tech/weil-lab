# SI29: actual full-J physical residual normalization

## Target and standing

Parent custody is draft PR #328, commit `a2f4ca5a664a796a5cf5322bad46f653754a2f4a`, successful Actions run `40375247309`. That gives an analytic rank proof with exact geometry witnesses: the actual 14 continuous SI29 features are independent modulo full J470, so the reduced energy inverse exists under inherited original coercivity/domain assumptions. It does not give a numerical lower bound.

This calculation targets a numerical basis for that same 14-dimensional quotient. It retains every original SI10 b9 physical source and the sinh pole. It does not repeat frequency integration, increase the feature count, or replace the full J projection by a selected subspace. The code fails if its precision cannot establish the declared normalization. A workflow result must be checked before describing this target as attained.

Let H=J*J, Bm=J*F, Fm=F*F. The script builds all original physical H470, Bm470x14 and Fm14x14 entries as rigorous ball enclosures, solves H X=Bm with verified ball arithmetic, and encloses

    S=Fm-Bm* X = F*(I-P_J)F.

It then seeks a fixed exact dyadic 14x14 C such that

    (99/100)I <= C* S C <= (101/100)I.

This is physical L2 normalization of the actual full-J residual family W=(I-P_J)F C. It is not energy normalization and does not compute the Astar-projected matrix.

## Closed-form physical integrals

Each polynomial trigonometric J source is one term x^k sin(2*pi*c*x) for even k or x^k cos(2*pi*c*x) for odd k. The pole is represented by -i sin(i*x/2). Each true mean is

    sin(Cx) sin(Rx)/(Rx), C=2*pi*c, R=2*pi*r,

and each true first moment 3 E[u sin(Cx+Rxu)] is

    3 cos(Cx) [sin(Rx)-Rx cos(Rx)]/(R^2 x^2).

Their removable singularities are entire, as the original frequency integrals show. Product-to-sum identities reduce all physical Gram entries to finite sine/cosine moments, with powers >=-4. Reflection doubles the positive physical half-interval and cancels the product-to-sum factor 1/2. Positive powers use exact integration-by-parts recurrences, with exact zero-frequency handling on rational frequency keys. The pole requires the same entire sine-integral formulas at complex arguments.

The negative-power primitives are regularized only to remove divergent Taylor monomials:

    I_-1,s(w) = Si(wB),
    I_-2,c(w) = (1-cos(wB))/B - w Si(wB),
    I_-3,s(w) = (wB-sin(wB))/(2B^2) + (w/2) I_-2,c(w),
    I_-4,c(w) = (1-cos(wB)-w^2 B^2/2)/(3B^3) - (w/3) I_-3,s(w).

These are respectively integrals of sin(wx)/x; (cos(wx)-1)/x^2; (sin(wx)-wx)/x^3; and (cos(wx)-1+(wx)^2/2)/x^4 over [0,B]. The sum of all subtracted divergent monomials is exactly zero for each original entire product. Linearity therefore recovers its ordinary physical integral. No finite-part interpretation is imposed on the original physical functions. Individual divergent terms must not be integrated as ordinary integrals.

The formula checker independently expands the actual 14 features using exact band moments, all 15 generators at the first original cluster, and the pole into degree-255 entire Taylor polynomials. It integrates their entire 30x30 polynomial Gram using a physical moment matrix and verifies every closed-form entry against rigorous Taylor product-error bounds. This catches normalization, first-moment signs, pole factors, negative-power regularization and higher source orders independently of the Si formulas. The native ball runtime is pinned and its wheel retained for replay.

## Why physical normalization gives an energy lower bound

For A=Astar and the inherited whole-original coercivity A>=kappa_star I,

    T_A(F C) = C* [F* A F - F* A J (J* A J)^-1 J* A F] C
              >= kappa_star C* S C.

This follows by minimizing the energy and L2 quadratic forms separately over the same full J470 space. It does not identify the energy projection with the physical projection. If the normalization check passes, it supplies

    T_A(F C) >= (99/100) kappa_star I = (3328479/100000000000) I.

This removes the tiny coordinate scale from a valid lower-bound denominator. It does not improve the underlying response: the matched forcing must change to C* F* R0, with J*R0=0, and the Schur response remains invariant under invertible feature changes. No small response can be inferred from normalization alone.

## Remaining acceptance gates

Even a successful physical normalization does not certify the Astar energy condition number, actual energy entries, normalized forcing, a response value or the complete MG07 signed inequality. Astar upper bounds, action and full original residual terms remain necessary. The independent original analytic/domain review is inherited and open. W-ODD-NEG, even-sector obligations, CC27/Weil transfer and RH remain open. No automatic merge or obligation reassignment is implied.

Implementation references: python-flint arb_mat verified solve documentation, https://python-flint.readthedocs.io/en/latest/arb_mat.html ; exact midpoint/radius dyadic representation, https://python-flint.readthedocs.io/en/latest/arb.html ; entire complex sine integral, https://python-flint.readthedocs.io/en/latest/acb.html . These document the runtime interface, not a substitute for the original operator proof.
