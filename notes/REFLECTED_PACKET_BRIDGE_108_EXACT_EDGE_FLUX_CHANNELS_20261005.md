# RPB108: actual edge-flux channels and reflection parity

Base: 1ef926fcd11525c80395beac0560ddfc8920b245.
Standing: analytic continuation with algebra/geometry controls; not Lean certified.
Definitions: docs/TERMINOLOGY_RPB108_EDGE_FLUX_CHANNELS.md.

## Exact right-edge profile and source dictionary

Fix an actual full mixed weak-null h in D_a. Put L=2a and f(v)=h(a-v), zero for v outside (0,L). For u>0 the previously derived actual exterior residual is

    r_h(a+u)=Pi_h(u)-integral_0^L k(u+v)f(v)dv
                      -sum_(ell_n<=L) alpha_n f(ell_n-u),
    ell_n=log(n), alpha_n=Lambda(n)/sqrt(n),
    Pi_h(u)=M_-(h)exp(a/2)exp(u/2)+M_+(h)exp(-a/2)exp(-u/2),
    k(s)=exp(-s/2)/(1-exp(-2s)).

The sum is the unchanged frozen right-limit set; threshold equality is included. Terms with Lambda(n)=0 can be omitted. The positive translate h(a+u+ell_n) vanishes by support. The negative translate is exactly f(ell_n-u). All statements are almost everywhere and use L2 representatives, not endpoint traces.

Let rho(s)=k(s)-1/(2s), the recovered bounded-near-zero remainder. The recovered boundary scaling note proves its corresponding Hankel operator H_rho is Hilbert-Schmidt on input L2(0,L) and output L2(0,infinity).

## Four actual flux channels

For 0<t<min(1,L), define

    Pole(t)=Re integral_0^t Pi_h(u) conjugate(f(t-u))du,
    Singular(t)=Re integral_0^t [integral_0^L f(v)/(u+v)dv]
                                      conjugate(f(t-u))du,
    Remainder(t)=Re integral_0^t H_rho f(u) conjugate(f(t-u))du,
    Prime(t)=sum_(ell_n<=L) alpha_n Re integral_0^t
                                  f(ell_n-u) conjugate(f(t-u))du.

Then the actual same-vector flux from the preceding note satisfies exactly

    F_h(t)=Pole(t)-Singular(t)/2-Remainder(t)-Prime(t).       (1)

For each positive t these integrals converge: the Carleman/Hankel operators are bounded on L2, finite translations preserve L2, Pi_h is bounded on the finite strip, and the testing profile is L2. Expanding the Hankel integral is justified by absolute product integration, using positivity of the absolute-value kernel and its L2 bound. No critical t-integrability is asserted by that fact.

Equation (1), together with F_h(t)=-D_m(t)+(cosh(t/2)-1)P0, is a genuine physical-versus-spectral boundary relation. It has no missing coefficient carrier or enlarged-null hypothesis.

## Interior echoes and opposite-edge threshold echoes

The frozen prime set is finite. Choose t0>0 smaller than 1, L, and every positive ell_n and L-ell_n for strict terms 0<ell_n<L. If there are no strict terms, omit those minima. For 0<u<t<t0:

- Each strict term samples f on (ell_n-t,ell_n), a source interval strictly inside (0,L).
- A threshold term ell_n=L samples f(L-u)=h(-a+u), the opposite boundary collar.

Thus thinning the exterior collar does not annihilate a general null vector's prime action. Strict terms still read its interior profile, and a threshold term still reads the opposite endpoint. The earlier boundary-concentration construction made the translations miss a specially chosen concentrated source; that was not a theorem that these prime channels vanish on full mixed-null vectors.

An exact threshold equality with nonzero Lambda occurs at at most one n. Its coefficient must remain in (1), regardless of how small t is. At the numerical frontier a=81/100 no such equality is claimed; the classification concerns a hypothetical endpoint at its actual aperture.

## Lawful reduction to real reflection parity

The actual multiplier m_a is real and even, its finite translations occur in both orientations, and the pole kernel is 2cosh((x-y)/2), real and invariant under simultaneous reflection. Consequently conjugation and reflection R h(x)=h(-x) preserve the full mixed-null equation on D_a. This follows by conjugating its real-kernel form identity and changing variables in both mixed slots; complex linearity then preserves the kernel.

If any nonzero complex null vector exists, at least one of its real or imaginary parts is nonzero and null. Splitting that real vector into (h+Rh)/2 and (h-Rh)/2 supplies a nonzero real even or odd null vector. Write R h=sigma h, sigma in {+1,-1}. No positivity-improving theorem or sign-definite ground mode is used.

For that parity representative f(L-u)=sigma f(u). The exact threshold contribution is therefore

    Prime_threshold(t)=alpha_threshold sigma integral_0^t f(u)f(t-u)du.  (2)

Its sign in the total flux is the negative of (2). A real even/odd profile need not have constant sign near the boundary, so (2) does not by itself establish a sign for the convolution. The other prime terms still sample strict interior intervals. This reduction narrows a future exclusion proof to two real parity sectors without asserting either sector empty.

## Remaining cancellation is collective

The critical target from the preceding note is integrability of |F_h(t)|/t^2. Formula (1) specifies exactly the singular, remainder, prime and pole terms whose signed sum would need that control. Hilbert-Schmidt compactness of H_rho does not establish weighted critical integrability, and absolute Cauchy-Schwarz on each channel does not supply collective cancellation. Real parity fixes the opposite-edge relation but not the sign of a general profile.

This pass does not establish the critical condition, H^(1/2), exponential Gaussian cancellation or endpoint exclusion. Its concrete next task is to obtain a quantitative boundary relation from the actual interior null equation controlling the signed sum in (1); if that fails, pursue an independent endpoint-exclusion argument. Further norm-only boundary thinning or dropping the threshold echo is not a valid substitute.

Numerical frontier remains 81/100. Retained selected-witness attachment, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms and CI unchanged. No actual nonzero null vector existence is asserted.

## Verification boundary

Pinned inputs: EXACT_TRANSLATION_BOUNDARY_FLUX_20261005 at this base, and the inherited ENDPOINT_BOUNDARY_REGULARITY and BOUNDARY_SCALING notes. The geometry certificate checks the coordinate identity, strict versus threshold placement and both reflection parities with exact rational controls. A control dropping a nonzero threshold echo is rejected. Controls are representative profiles, not actual null modes. The kernel and mixed-form statements are analytic arguments, not mechanically certified by these controls.
