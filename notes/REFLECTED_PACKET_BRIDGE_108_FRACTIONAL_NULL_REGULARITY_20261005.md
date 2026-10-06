# RPB108: fractional regularity and shrinking-collar power bounds from full mixed nullity

Base: 6002bba61cb9abf21e341d72556589f02a5447d4.
Definitions: docs/TERMINOLOGY_RPB108_FRACTIONAL_NULL_REGULARITY.md.

## Result

Fix a>0. For every 0<s<1/2, every actual full mixed weak-null vector h in D_a, extended by zero, satisfies

    ||h||_(Y_s)<=C_(a,s)||h||_2,
    ||f||_(Y_s)^2=integral (1+|xi|)^(2s)|Fourier(f)(xi)|^2 dxi.

Y_s is equivalent to the usual H^s space. The frozen multiplier action also belongs to Y_s. Fractional regularity is derived, not assumed. In particular, the actual moving Gaussian mass satisfies M_R=O_(a,s)(R^(-2s))||h||_2^2, and the actual exterior residual has a squared shrinking-collar bound O_(a,s)(delta^(2s))||h||_2^2. These conclusions use full mixed nullity, not only a carrier norm bound.

The constants below are explicit but very large. No nonzero weak-null vector is asserted to exist. The theorem does not provide H^(1/2), endpoint traces, H1, exponential decay, a larger vanishing interval or global endpoint exclusion.

## Pinned actual identity

Use the actual quarter-line archimedean multiplier m0, finite frozen prime translation operator T_a, pole p_h and support indicator P_a from LOGARITHMIC_BOOTSTRAP_20261005. The exact right-limit prime set includes threshold equalities. Put S_a=2 sum Lambda(n)/sqrt(n), C0>=0 with |m0-w|<=C0 and w=log(exp(1)+|xi|).

The previously derived initial multiplier domain makes the following an L2 identity for every full mixed weak-null h:

    m0(D)h=P_a T_a h-P_a p_h+[m0(D),P_a]h,   P_a h=h.

Also |m0'(xi)|<=144/(1+|xi|), with m0 even. This derivative bound was proved from the actual trigamma series in the pinned bootstrap note. Thus, with r=1+|xi| and t=1+|eta|,

    |m0(xi)-m0(eta)|<=144 |log(r/t)|.

We do not assume a new spectral domain to obtain this identity. Indefinite diagonal zero and selected-only retained records do not suffice for it.

## Uniformly capped fractional weights

For M>=1 define rho_M(xi)=min((1+|xi|)^s,M). Both rho_M and its inverse are bounded multipliers on L2. The map log r -> log min(r^s,M) is s-Lipschitz, so

    rho_M(xi)/rho_M(eta)<=exp(s|log(r/t)|),
    |rho_M(xi)/rho_M(eta)-1|
        <=s|log(r/t)|exp(s|log(r/t)|).

The reciprocal ratio obeys the same estimate. These bounds are uniform in M.

Let

    J_s=integral_R |v|/[2 sinh(|v|/2)] exp(s|v|)dv,
    U_s=4+4/(1/2-s)^2.

On |v|<=1 the quotient is at most one and exp(s|v|)<2; the integral there is at most 4. On |v|>=1 use the previous quotient bound 2|v|exp(-|v|/2), then integrate its majorant over the larger half-line [0,infinity). It follows that J_s<=U_s for s<1/2.

The exact Fourier kernel of P_a is sin(2*pi*a*(xi-eta))/(pi*(xi-eta)). Weighted Schur with weight (1+|xi|)^(-1/2), splitting the two eta signs and substituting t=r exp(v), gives

    ||rho_M [m0(D),P_a] rho_M^(-1)||_(L2 -> L2)
        <=D_s=96 U_s,
    ||rho_M P_a rho_M^(-1)||_(L2 -> L2)
        <=A_s=1+s U_s.

For the first bound use 144/pi<48 and the ratio bound. For the second subtract the L2 projection P_a and use the ratio-minus-one estimate; its extra Schur budget is at most (2s/pi)J_s<=sU_s. The column estimate follows from the reciprocal ratio bound. Equal magnitudes are handled by the continuous limit of log(r/t)/(r-t). These are the same explicit kernel arguments as in the preceding note, now with capped power weights; no fractional domain is presumed.

Prime translations commute with rho_M, hence have norm budget S_a in the capped norm as well.

## The cut-off pole belongs to the fractional space

Let H=||h||_2, b_a=4a sqrt(2a)exp(a), v_a=(4+2a)sqrt(2a)exp(a). As already proved, the zero extension P_a p_h has L1 norm at most b_a H and total variation at most v_a H. Therefore

    |Fourier(P_a p_h)(xi)|<=min(b_a,v_a/(2*pi*|xi|))H.

For |xi|<=1 use (1+|xi|)^(2s)<2. For |xi|>=1 use (1+|xi|)^(2s)<=2^(2s)|xi|^(2s) and pi>3. Integration gives

    ||P_a p_h||_(Y_s)^2
        <=[4b_a^2+v_a^2/(9(1-2s))]H^2,
    ||P_a p_h||_(Y_s)<=F_s H,
    F_s=2b_a+v_a/[3(1-2s)].

The simpler second ceiling uses 0<1-2s<1. It holds also with Y_s replaced by any capped rho_M norm. The pole's jump is why the integrability ceiling here is s<1/2; no trace of h is used.

## High-frequency absorption proves the new domain

Write X_M=||rho_M Fourier(h)||_2, B_s=A_s S_a+D_s. The exact null identity and the uniform operator bounds imply

    ||rho_M m0 Fourier(h)||_2<=B_s X_M+F_s H.

Everything is finite at this stage because rho_M is bounded and the initial multiplier action is L2. Now set

    N_s=exp(C0+2(B_s+1)).

For 1+|xi|>=N_s, the actual envelope gives m0(xi)>=log(1+|xi|)-C0>=2(B_s+1). Split h into those high frequencies and their complement. The low part has capped norm at most N_s^s H. Hence

    X_M<=N_s^s H+||rho_M m0 Fourier(h)||_2/[2(B_s+1)]
        <=N_s^s H+[B_s X_M+F_s H]/[2(B_s+1)].

Absorbing B_s/[2(B_s+1)]<1/2 yields the uniform, M-independent bound

    X_M<=C_s H,   C_s=2N_s^s+F_s/(B_s+1).

Monotone convergence as M tends to infinity proves h in Y_s with this bound. Fatou (or the same inequality and monotone convergence) also proves m0 Fourier(h) in Y_s with norm at most (B_s C_s+F_s)H. Since translations preserve Y_s, the actual frozen core L_h=(m0(D)-T_a)h obeys

    ||L_h||_(Y_s)<=G_s H,
    G_s=(B_s+S_a)C_s+F_s.

This is not an argument that all finite logarithmic moments imply fractional regularity. It is a new absorption estimate using the actual mixed equation and uniformly capped fractional weights.

## Actual Gaussian power rate

Keep beta_R=exp(-(2*pi*xi-R)^2/R) and M_R=integral beta_R|Fourier(h)|^2. On |2*pi*xi-R|<=R/2, we have |xi|>=R/(4*pi). Off that band beta_R<=exp(-R/4). Consequently

    M_R <=[C_s^2(1+R/(4*pi))^(-2s)+exp(-R/4)]H^2.

Thus every fixed power exponent alpha<1 is available, by taking s=alpha/2 for 0<alpha<1. No exponent alpha=1 is obtained from these bounds, and their constants deteriorate as s approaches 1/2. The earlier logarithmic estimates remain valid but are superseded as Gaussian upper bounds by this new result.

## Actual shrinking-collar power bound

For any f in Y_s and any interval E of length delta<=1, split its Fourier transform at |xi|=1/delta. Weighted Cauchy-Schwarz gives the low-frequency supremum bound

    ||f_low||_infinity^2
      <=2(1+1/delta)^(1-2s)/(1-2s) ||f||_(Y_s)^2.

The high-frequency L2 norm squared is at most (1+1/delta)^(-2s)||f||_(Y_s)^2. Using |u+v|^2<=2|u|^2+2|v|^2 yields

    integral_E |f|^2 <=[8/(1-2s)+2]delta^(2s)||f||_(Y_s)^2.

The full residual is the already realized r_h=L_h+p_h, zero on the support interior and equal to the exact native exterior formula outside. On the right collar (a,a+delta), the pole bound is |p_h|<=2sqrt(2a)exp(a+1/2)H. Applying the preceding estimate to L_h gives

    integral_a^(a+delta) |r_h(x)|^2 dx
      <=[2(8/(1-2s)+2)G_s^2+16a exp(2a+1)]
                              delta^(2s)H^2.

Reflection gives the corresponding left-collar estimate. This is derived for actual full weak-null vectors, uniformly in that null space at fixed a. It does not conflict with BOUNDARY_SCALING_20261005: that obstruction concerns arbitrary unit-carrier vectors which need not solve the mixed equation. The null equation now provides the extra information that the earlier norm-only estimate lacked.

The squared collar estimate is not an exponential signed Gaussian pairing estimate. An absolute norm estimate alone does not supply oscillatory cancellation. No strict support gap or larger residual vanishing interval has been produced.

## Validation and standing

The rational certificate checks U_s, A_s, D_s and absorption constants at six rational s values, including s=1/4 where U_s=68, A_s=18 and D_s=6528. It checks capped-weight Lipschitz slopes on rational logarithmic coordinates, Schur tail moment budgets and pole/Fourier collar coefficients. A negative control attempting to include s=1/2 is rejected because both Schur and pole tails cease to have an integrable decay budget. Certificate reproduced byte for byte. These are constant/control checks; the universal Schur, domain absorption, Fatou and Fourier localization proofs remain analytic, not mechanically or Lean verified.

Numerical aperture frontier remains 81/100. No actual endpoint or null vector existence is asserted. Global endpoint exclusion, retained selected-witness attachment, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms, CI and historical notes unchanged.
