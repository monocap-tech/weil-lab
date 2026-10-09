# RPB108 — DNE4 complete weighted jump representation

**Parent:** DNE3 at `be834f237121d8625be4551d83f82cd80345b066`. DNE4 investigates the full-domain ground-state weighted representation; it does not change CC or Aperture work.

Let `I=(-a,a)`, `D_a` be the original supported logarithmic form domain, and `J_a` the unweighted complete positive jump form of DNE3, including the zero-extension killing contribution and all active von Mangoldt prime-power jumps. Write `H_a=J_a-kappa_a ||.||²`.

**Ground state:** `phi=phi_a` is the normalized simple nonnegative even pole-free ground eigenfunction with `H_a phi=lambda_0 phi`, and `phi>0` Lebesgue almost everywhere (DNE2). Put `mu_a=kappa_a+lambda_0`, the lowest eigenvalue of `J_a`. No boundedness, pointwise positivity, or boundary trace of phi is assumed.

**Weighted Hilbert space:** `L²(I,phi² dx)` with unitary `Uu=phi*u`. The complete ground-transformed closed form is `E_phi(u)=H_a(phi*u)-lambda_0||phi*u||²` on `{u:phi*u in D_a}`.

**Weighted positive jump form:** For measurable real u on I,
```
W_phi(u) =
   1/2 int_I int_I j(x-y)phi(x)phi(y)(u(x)-u(y))² dxdy
 + sum_(log n<=2a) c_n int_(x,x+log n in I)
                    phi(x)phi(x+log n)(u(x)-u(x+log n))² dx .
```
Here `j(d)=exp(-|d|/2)/(1-exp(-2|d|))` and `c_n=Lambda(n)/sqrt(n)`. Every prime power, both physical shift orientations, all continuous off-diagonal interactions, and original support restriction are retained. The weighted form does **not** have a separate exterior killing term: it cancels against the ground equation. Original unweighted `J_a` **does** have killing, and it is crucial in proving the cancellation.

**Full-domain identity:** DNE4 proves `Dom E_phi={u in L²(phi²dx):W_phi(u)<infinity}`, and `E_phi(u)=W_phi(u)` for the complete domain, including quotients of genuine higher eigenfunctions. No assumption that `u=h/phi` is bounded, smooth or defined pointwise at phi-zero exceptional points.

**Regularizing test:** For bounded `f in D_a` and epsilon>0 put `g_e=f²/(phi+epsilon)` inside I, zero outside. The indicator `1_I` belongs to D_a because the logarithmic jump exterior killing is integrable over I. Therefore `g_e in D_a` by bounded Lipschitz functional calculus and product estimates. This enables the global-domain Picone proof.

**Ground-depth spectral target:** A higher moment-zero null `H_a h=0` corresponds to `W_phi(h/phi)=-lambda_0||h||²`. Establishing a strict lower eigenvalue bound **greater** than `-lambda_0` on the corresponding parity/moment constrained subspace is still open; DNE4 proves the representation, not that bound.
