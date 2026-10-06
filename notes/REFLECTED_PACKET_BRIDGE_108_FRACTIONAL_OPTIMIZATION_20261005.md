# RPB108: explicit approach to Gaussian and collar exponent one

Base: 4ddee22f868164432dee3816e36c371d5108dd90.
Definitions: docs/TERMINOLOGY_RPB108_FRACTIONAL_OPTIMIZATION.md.

## Result and scope

The actual full mixed weak-null fractional estimates can be optimized with their constant growth accounted for. At any fixed aperture a>0 define the constants below. Set x_R=1+R/(4*pi). If log x_R>=8K_a, then

    M_R <=[c_a^2 x_R^(-1)
             exp(2 K_a^(1/3)(log x_R)^(2/3))
             +exp(-R/4)] ||h||_2^2.

For either exterior collar of width delta, if log(1/delta)>=8K_a, its actual squared residual mass is at most

    k_a delta exp(2 K_a^(1/3)(log(1/delta))^(2/3)) ||h||_2^2.

These are explicit bounds of order R^(-1+o(1)) and delta^(1-o(1)), with large thresholds and prefactors. They remain conditional on actual full mixed weak-nullity; no nonzero null vector exists by assertion. This is not an exact exponent-one estimate, a half-derivative theorem, exponential Gaussian suppression or endpoint exclusion.

## Constants from the actual source

Retain the preceding note's C0>=0, S_a, b_a=4a sqrt(2a)exp(a), v_a=(4+2a)sqrt(2a)exp(a). These include the actual frozen finite prime set and the actual pole. Define

    W_a=11 S_a+1920,
    F0_a=2b_a+v_a/3,
    E_a=C0/2+W_a+2,
    c_a=2+F0_a,
    g_a=(W_a+S_a)c_a+F0_a,
    K_a=2E_a+3=C0+22 S_a+3847,
    k_a=20g_a^2+16a exp(2a+1).

No prime or pole term is removed to improve the rate. K_a>=3847, so these asymptotic thresholds are not practical new numerical apertures. The constants are uniform on the actual weak-null space at fixed a.

## Paying for proximity to the half derivative

Write d=1-2s, 0<d<1. From the prior exact constants,

    U_s=4+16/d^2<=20/d^2,
    A_s=1+s U_s<=11/d^2,
    D_s=96U_s<=1920/d^2,
    B_s=A_s S_a+D_s<=W_a/d^2,
    F_s=2b_a+v_a/(3d)<=F0_a/d.

The previously derived Y_s norm ceiling was

    C_s=2 exp(s[C0+2(B_s+1)])+F_s/(B_s+1).

Since s<1/2, d<=1 and 1/d<=exp(1/d^2), it follows that

    C_s<=c_a exp(E_a/d^2).

Indeed its first summand is at most 2 exp(C0/2+W_a/d^2+1), bounded by 2 exp(E_a/d^2); the second is at most F0_a/d, bounded by F0_a exp(E_a/d^2).

Similarly, for the actual frozen residual core L_h the previous ceiling was G_s=(B_s+S_a)C_s+F_s. Using 1/d^2<=exp(1/d^2) gives

    G_s<=g_a exp((E_a+1)/d^2).

The squared collar coefficient obeys

    2(8/d+2)G_s^2+16a exp(2a+1)
      <=k_a exp(K_a/d^2),

because 2(8/d+2)<=20/d and 1/d<=exp(1/d^2). Also C_s^2<=c_a^2 exp(K_a/d^2), using K_a>2E_a.

Thus both previous estimates have the same d-dependent bound:

    M_R <=[c_a^2 exp(K_a/d^2)x_R^(-1+d)+exp(-R/4)]H^2,
    collar_mass <=k_a exp(K_a/d^2)delta^(1-d)H^2,

where H=||h||_2. They hold for each chosen 0<d<1; the all-s regularity theorem permits a scale-dependent choice without interchanging any infinite series or limits.

## A balanced choice of exponent

For x>1 put L=log x and choose d=(K_a/L)^(1/3). If L>=8K_a, then 0<d<=1/2, so 1/4<=s=(1-d)/2<1/2 is lawful. The loss from the constant and the exponent balance exactly:

    K_a/d^2+dL=2 K_a^(1/3)L^(2/3).

Apply this with x=x_R for the Gaussian and x=1/delta for the collar. Inserting the equality into the preceding estimates proves both stated results. This balanced choice is sufficient for an explicit rate; no claim of sharp constants or optimal asymptotics is made.

## What this resolves and what remains

The correction exponent divided by L is 2(K_a/L)^(1/3), tending to zero. Thus the displayed Gaussian envelope is R^(-1+o(1)), and the collar envelope is delta^(1-o(1)). Each improves the corresponding fixed exponent below one once the scale is sufficiently large. The prefactors and thresholds are fully accounted for.

The multiplicative correction nevertheless tends to infinity. The established upper estimate does not imply O(R^(-1)) or O(delta), much less exponential suppression. This is a limitation of the estimates proved here, not a lower bound for actual mass or a proof that improved estimates are impossible. No H^(1/2), trace of h, support gap or enlarged residual vanishing interval is obtained. The signed oscillatory Gaussian interaction remains a separate issue.

The fractional route now has an explicit asymptotic rate with its near-half-derivative cost included. Further use of this published norm bound alone will not provide the missing exponential theorem. The next research step needs a stronger estimate from mixed nullity, additional boundary cancellation or an independent endpoint exclusion argument. Retained selected-witness attachment is still separate.

## Validation and standing

The exact rational certificate checks the d-dependent Schur and absorption ceilings at six rational d values and stated test source budgets. At four exact-cube scale ratios it checks the lawful exponent, threshold, balance identity and negative total exponent. A control ignoring the threshold chooses d=2 and is rejected. The test budgets are illustrative, not certified actual aperture constants. Certificate reproduced byte for byte.

These checks audit algebraic constants and choices. Universal operator inputs and the optimization proof are analytic, not mechanically or Lean verified. Numerical aperture frontier remains 81/100. Global endpoint exclusion, retained selected-witness attachment, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms, CI and historical notes unchanged.
