# MG62 — Genuine original two-frequency-cell Jensen singular-gap test for 2D strong-action source positivity

**Status: implemented; producer and independently authored exact-rational replay acceptance PENDING.** Previous [MG61 Actions #39963056297](https://github.com/monocap-tech/weil-lab/actions/runs/39963056297) **PASSED** 48 original-source orthogonal-gauge moment tests and found **0 strict positive 2D lower Grams**. In MG61 each second plane direction had negative conservative Young lower diagonal; the closest was original orthogonal coordinate 5, with lower diagonal approximately −0.0609213.

The MG61 2D lower is conservative, not a theorem that the true original physical strong-action source moment is negative. MG62 therefore changes the inequality, not merely the rational balancing parameters. It tests **two actual original Fourier cells separately**, using cell mean Jensen positivity and a rigorous 2×2 singular-value perturbation bound.

## Physical original source and the genuinely new proof method

Keep all 55 independently certified true original signed seven-prime/digamma Fourier source cells from MG57/MG58, 25 SI10 physical source functions, 23 MG11 adapted plus actual sinh pole 24D frame and true pole-corrected strong action

```
u_j(xi)=a_o(xi)t_j(xi)-2t_p(xi)b_j,  b=F^*s.
```

For a real original physical source plane `W=[v/9,w_i]` or `W=[v/18,w_i]`, where `||v||²=82`, `w_i=e_i-(v_i/82)v` and `v·w_i=0`, the genuine two-vector projected strong Fourier action is
```
y(xi)=(y_{v/sc}(xi), y_{w_i}(xi)).
```

On each accepted original physical positive-frequency cell I=[l,r] of width h=r-l, MG59's independently verified true source/pole common-scalar interval gives
```
y(xi)=c_I+x*d_I+e_I(xi),     x=xi-(l+r)/2,
|e_{I,k}(xi)|<=rho_{I,k}.
```
Thus the ACTUAL physical Fourier-cell **mean** satisfies
```
mean_I y = c_I+delta_I,    |delta_{I,k}|<=rho_{I,k},
```
because the affine slope has zero cell mean. No independence of pole and source Taylor errors is assumed. Applying scalar Jensen to all real 2D source-combination coefficients z on a single cell yields
```
integral_{I and -I} |z·y(xi)|² dxi >= 2h |z·mean_I y|².
```
The factor two is the genuine negative-frequency mirror under the accepted real original source convention, NOT a discarded tail.

For TWO distinct positive-frequency original cells I,J, write C for the 2×2 matrix of the exact rational center means weighted by sqrt(2h), and delta C the unknown perturbation from physically justified source radii. Then
```
Q=C^TC=sum_{K=I,J} 2h_K c_K c_K^T,
E=sum_{K=I,J} 2h_K (rho_{K,1}²+rho_{K,2}²),
||delta C||_op <= ||delta C||_F <= sqrt(E).
```
By the standard singular-value perturbation inequality,
```
sigma_min(C+delta C) >= sigma_min(C)-sqrt(E).
```
Compute the EXACT rational lower
```
L=det(Q)/trace(Q) <= lambda_min(Q)=sigma_min(C)².
```
**Strict proof acceptance requires L > E > =0**, not a rounded eigenvalue. Then an explicit rational original source-coefficient Euclidean lower on this genuine source two-plane is
```
kappa = (L-E)²/[4L (||v/sc||²+||w_i||²)] > 0.
```
This follows by `(sqrt(L)-sqrt(E))² >= (L-E)²/(4L)` when L>E. The genuine original physical action moment outside the two selected original positive-frequency cells remains a positive-semidefinite contribution to the actual true `S_*=(A_*F)^*(A_*F)`. Thus this is a valid **restricted 2D original physical source coercivity** if and only if the accepted rational gap holds.

Crucially, this method NEVER charges MG15's global diagonal 2D Young error and does not construct a spurious source moment lower by mixing data from different frequency partition cases.

## Finite exact acceptance gate

For all 24 original coordinate source planes and both rational balancing factors (48 valid original planes), inspect the 55 *accepted genuine physical Fourier cells*. A floating exploratory score ranks **only candidate original cell pairs** by the proposed singular gap. It has **NO proof authority**. Select the three strongest disjoint-index original cell pairs per source plane; 48×3=**144 original 2D cell-pair exact-rational tests**. Any accepted 2D source plane must pass the strict rational center Gram `det/tr>E` inequality. Record every exact center covariance entry, determinant, lower smallest singular squared, physical error Frobenius upper and explicit rational source coefficient coercivity if positive.

No claim that a finite search failing rules out other cell pairs, larger collections of cells, a differently sampled original Fourier carrier, another 2D source plane or actual physical operator positivity.

## Independence

The producer reuses the accepted MG58 55-cell original physical source archive and MG59 project-before-error true original action interval. The separate verifier imports **neither MG62 source producer nor its pair-selection algorithm**. It regenerates all new original genuine Fourier cells via the accepted independently authored MG58 physical source generator, reconstructs the 41-cell original MG57 baseline and genuine pole-column physical Gram, and derives projected cell center/radius by the independent MG59 physical action formula. It independently checks all 144 selected genuine cell-pair exact rational Q matrices, Frobenius E values, determinant/tr inequalities and normalized lower bounds. Floating pair ranking cannot insert a false positive.

Regardless of any 2D result, full24 original strong-action coercivity, original source residual 24D contraction, full470D inverse, signed odd 51/56 cap, independent original Fourier/form/domain verification, even/Weil/CC27/RH remain OPEN. Restricted source-plane positivity may not be promoted into a global 24D rank-two Loewner lower without complement control.
