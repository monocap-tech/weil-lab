# RPB108: moving the jump closes whole-domain generation and gives exact native real sampling

2026-10-07. Recovered live head 811b0826abf45d688d1e2da7900cda852103ddee; concurrent aperture-one whole-domain positivity is now certified and is preserved. Global analytic input is NF46 at e3bf87d06d426be37547e6a6a9c136d1c25fd519. Definitions: [moving-jump sampling](../docs/TERMINOLOGY_RPB108_MOVING_JUMP_SAMPLING.md).

## Result

At any hypothetical nonzero actual nonnegative contact, the real-zero division family generates the ENTIRE completed native-energy quotient, not just one jump response:

    H_Q=H_jump=H_div.

Every supported canonical pair f,g has the exact sampling identity

    Q(f,g)=sum_(Phi(t)=0) c_t F_f(t)overline(F_g(t)),
    c_t=d_t/|Phi'(t)|^2>0.                         (1)

The series is absolutely convergent for the mixed pairing. The energy quotient is isometric onto the full square-summable real-node sequence space. Original physical/source reconstruction still has the finite null-kernel correction:

    Gamma(f)=Gamma(P_K f)
              -i sum_t F_f(t)Gamma(Pi u_t)/Phi'(t), (2)

where the series converges in the complete actual source norm. These sampling nodes belong to Phi, not to a purported real zeta divisor. The theorem is conditional on contact and supplies no contact exclusion. The shifted actual positive eigenspace has the same result for Q_mu, and its original native form retains mu physical mass.

## 1. Lawful jump at every interior point

For xi in (-a,a), define inside the unchanged window

    k_w^xi(x)=exp(iw xi)exp(-iwx)
                 [integral_(-a)^x exp(iwy)h_*(y)dy/Phi(w)
                                      -1_(x>xi)].

Both outer endpoints match, and the only jump is -1 at xi. The Fourier and distributional equations are exactly

    F_kwxi(z)=i[exp(iw xi)Phi(z)/Phi(w)-exp(iz xi)]/(z-w),
    (D+iw)k_w^xi=exp(iw xi)h_*/Phi(w)-delta_xi.    (3)

For fixed xi the same jump cancellation as NF45 makes k_w^xi-k_v^xi globally H1 with canonical derivative. Exact full nullity cancels the h_* forcing in its skew identity. Thus it produces a Pick function M_xi with

    Q(k_w^xi,k_v^xi)
           =[M_xi(w)-overline(M_xi(v))]/(w-bar v). (4)

No delta is paired in Q. All derivatives in the argument are derivatives of differences with identical jumps. For fixed nonreal w, the map xi -> k_w^xi is continuous into the logarithmic domain on compact interior xi intervals: its jump-step difference is a translated finite interval indicator, whose full-line logarithmic norm tends to zero with its interval length; the remaining term is an ordinary smooth scalar multiple of a fixed canonical vector. Local boundedness follows as well. These are Bochner-integrable actual tests against a smooth compact weight.

## 2. Every interior jump has the same real atoms and no infinity coefficient

At a simple real generator zero t, the form-valued residue is

    Res_(w=t) k_w^xi=exp(it xi)u_t/Phi'(t).

The phase has modulus one. Therefore M_xi has the SAME atom weight c_t at every t, independently of xi.

For imaginary w=iy the exact global auxiliary formula is

    k_(iy)^xi(x)=exp(y(x-xi))1_(x<xi)
                         -exp(-y xi)R_y h_*(x)/Phi(iy).           (5)

The tails cancel identically outside [-a,a]. Translation does not change the full-line logarithmic norm of the first term. NF46's Laplace asymptotic gives

    |exp(-y xi)/Phi(iy)|
               =O(exp(-(a+xi)y)y^r sqrt(log y)).

For each fixed interior xi, a+xi>0; on a compact interior set this is uniformly exponentially small. Hence

    ||k_(iy)^xi||_D^2=O(log y/y).

Every M_xi therefore has zero linear infinity coefficient, and only the same real atoms. The one-variable Herglotz theorem already used and pinned in NF46 gives

    Q(k_w^xi,k_v^xi)=sum_t c_t/[(w-t)(bar v-t)].   (6)

Applying NF46's orthogonal projection argument with the phase-bearing residues yields

    [k_w^xi]=sum_t exp(it xi)[u_t]/[Phi'(t)(w-t)]
                                          in H_Q.              (7)

Thus EVERY interior jump test belongs to the original division carrier H_div. The phase is retained; it cannot be set to one when comparing distinct jump locations. The real constants in M_xi need not be fixed or compared because they disappear from the Gram identity.

## 3. Exact synthesis of all smooth compact tests

Fix one w in the upper half-plane. For a smooth compact v inside (-a,a), put f=(D+iw)v. Its Fourier transform at w is zero by integration by parts:

    F_f(z)=i(w-z)F_v(z),  F_f(w)=0.

Take the actual logarithmic-domain Bochner integral

    U=int_(-a)^a f(xi) k_w^xi dxi.

Local domain continuity from Section 1 justifies this integral; f has compact interior support. Equation (3), integrated distributionally, gives

    (D+iw)U=h_* F_f(w)/Phi(w)-f=-f.

Both U and v are globally compact. The only compact distributional solution of (D+iw)(U+v)=0 is zero: its global solution is a scalar exponential, which cannot have compact support unless the scalar vanishes. Therefore

    v=-int f(xi) k_w^xi dxi.                       (8)

Every class [k_w^xi] lies in the closed H_div by (7). Passing the Bochner integral through the bounded quotient map shows [v] lies there too. Smooth compact interior vectors are a proved dense form core of D_a. Hence H_div=H_Q. This is the actual generation hypothesis missing in NF46; it is now discharged by (8), rather than assumed from an external model or inferred from the Pick function alone.

## 4. Exact full native sampling and its normalization

The residue/projection formula at jump location xi is

    Q(k_w^xi,u_t)=exp(it xi)d_t/[Phi'(t)(w-t)] .

Insert (8) and F_f(t)=i(w-t)F_v(t). For every smooth compact v,

    Q(v,u_t)=-i d_t F_v(t)/Phi'(t).                (9)

Both sides are continuous in the canonical domain: Q is a bounded mixed form there and compact-support Fourier evaluation is physical-L2 bounded. Thus (9) extends to every v in D_a. The factors i and Phi'(t), including the sign of Phi'(t), are fixed by the registered angular Fourier convention.

Because [u_t]/sqrt(d_t) is now a COMPLETE orthonormal family in H_Q, Parseval and polarization give (1). The mixed series is absolutely convergent by sequence Cauchy-Schwarz. In particular

    Q(f,f)=sum_t c_t |F_f(t)|^2,
    Q(f,f)=0 iff F_f(t)=0 for every generator node t.

These real point evaluators DO descend to D_a/K: every kernel profile is Phi times a polynomial and therefore vanishes at all t. This contrasts with the previously audited nonreal evaluation, which does not descend. The energy evaluator bound is

    |F_f(t)|<=Q(f,f)^(1/2)/sqrt(c_t).

The sampling map is onto all l2 node coordinates. Indeed T_Phi(u_t/sqrt(d_t)) is a modulus-one scalar times the coordinate vector at t, since F_ut(t)=i Phi'(t) and all other node values vanish. Complete orthonormality and quotient completion supply the onto statement. No physical L2 sampling norm or actual-divisor positive channel norm is silently substituted.

## 5. Physical and actual-source lifting retains K

The bounded gauge Pi from NF46 converts quotient convergence into canonical-domain convergence. The expansion is now available for EVERY supported f, not just a jump test:

    Pi f=-i sum_t F_f(t) Pi u_t/Phi'(t) in D_a.

Complete actual analysis is bounded on D_a, so (2) follows. The correction P_K f is the physical orthogonal projection onto the actual finite kernel. Nothing in real-node sampling observes it; complete zeta analysis does observe it. Consequently (1) is a complete representation of native ENERGY and is not an injective reconstruction of the original physical/source graph without this correction.

A strictly positive auxiliary real sampling measure at contact is compatible with a nonzero null kernel because the kernel's Fourier profiles vanish at every auxiliary node. This is not pointwise vanishing at the actual zeta divisor: Phi has no nonreal zeros, whereas the native actual analysis may evaluate nonreal source points and their reflections. The equality in (1) concerns the complete signed native pairing on the fixed supported domain. It does not equate its new real node measure to the actual divisor measure or authorize moving to an arbitrarily larger support window.

The model-to-actual-source compatibility question is therefore explicit: how does the actual signed divisor analysis realize the real sampling pairing AND the finite kernel correction (2) at spectral level zero? Full-native nullity forces signed orthogonality to every canonical test, but those equalities alone have not supplied the required sharp height-weighted sign.

## 6. Shifted countercontrol and remaining arithmetic distinction

For the actual lowest positive eigenspace at its fixed certified window, use Q_mu=Q-mu mass. All preceding steps, moving-jump generation included, hold with its generator Phi_mu, division energies d_t^mu and weights c_t^mu. Its actual unshifted full form obeys

    Q(f,g)=mu<f,g>_L2
                  +sum_(Phi_mu(t)=0)c_t^mu F_f(t)overline(F_g(t)).

This is an exact retained mass residual, not a modification of the actual prime/pole terms. The actual positive eigenmode retains its positive sharp/log coefficient. Therefore whole-domain generation and positive real sampling by themselves do not exclude the terminal defect. They do supply a fully attached spectral model of the native form at the relevant level, and remove the invisible-positive-summand ambiguity on the actual carrier.

| Control | Audit |
|---|---|
| Actual rough positive eigenmode | Same full generation theorem for Q_mu; unshifted pairing keeps mu mass. |
| Compact-good-row logarithmic control | No automatic moving-jump/skew theorem; its positive slope still obstructs generic sign inferences. |
| Fixed finite source restoration | Sharp/log coefficient remains unchanged; full actual equation is required in Sections 1-4. |
| Two-row comparison contact | Auxiliary rows generally break derivative skew; no actual sampling theorem is inferred. |
| Previously invisible positive direct summand | Possible for an abstract response, but actual reconstruction (8) now proves there is no such summand in H_Q. |
| Observable null-kernel direction | Remains in the physical/source graph through P_K and Gamma(P_K f), despite complete quotient sampling. |

The internal graph shortens substantially: whole-native generation, all-domain real-node evaluation bounds, and complete native-energy sampling are proved analytically. The final signed sharp-head arithmetic arrow remains unproved. No bounded-return mechanism, endpoint exclusion, F4, full transport or Lean closure is claimed. The newly certified aperture-one positivity is preserved and is not an input to this conditional all-window contact theorem.

## Verification and dependencies

The exact checker verifies the moving-jump Fourier identity, Bochner synthesis algebra, phase-bearing residue coefficients, node evaluation and Parseval normalization, and shifted mass/source-gauge controls. Analytic logarithmic continuity, core density and infinite completion are proved above and not certified by finite checks. The pinned NF46 classical Herglotz dependency is reused; no new external theorem is imported. The companion custody manifest pins every actual analytic dependency and helper. Historical wording and certificates remain unchanged.
