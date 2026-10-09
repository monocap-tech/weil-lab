# RPB108 DNE1 — Ground-state jump representation and the higher-null gap

Date: 2026-10-08 America/Los_Angeles. Independent DNE parent: DNE0 at `4f3738ea729e19a9a49ae2ed31a42ffa19714924`. Definitions: [DNE1 native jump conductance](../docs/TERMINOLOGY_RPB108_DNE1_GROUND_STATE_CONDUCTANCE.md).

**Classification: new exact native ground-state product-core identity, parity-resolved nonnegative jump decomposition, a quantitative conditional gap criterion, and sharp controls. NO original all-aperture null exclusion, no actual higher eigenmode tested, no RH/F4 or new whole positive aperture.** The full support domain, all prime powers and both translation orientations are retained. CC43 is a read-only dependency; this result is DNE1, not CC44.

## 1. What CC43 gives, and what it does NOT

Let `H_a` be the complete original pole-FREE Weil form, with only the two original Hermitian pole cross terms removed. Its selfadjoint physical realization on the supported logarithmic Dirichlet carrier has compact resolvent (CC41). CC43 proves a simple nonnegative even ground eigenfunction `phi=phi_a`, normalized in physical L2, with lowest eigenvalue `lambda_0(a)`. It does NOT assert that phi is bounded, bounded below, pointwise smooth or of nonzero boundary trace; nor that all higher H spectrum is positive.

At a nonnegative ORIGINAL contact `Q_a>=0`, a zero-moment null h is a higher H eigenvector with Hh=0, orthogonal to phi and lambda_0<0. In the even case the relevant pole moment c(h)=int h cosh(x/2) vanishes; in the odd case s(h)=int h sinh(x/2) vanishes. Any closure must retain BOTH the ground-state orthogonality and the pole-moment constraint. The original Q carries a positive even and negative odd pole, so no pole contribution is inserted into H or silently made positive.

## 2. Exact DNE1 ground-state/Picone identity on the admissible product core

Use the complete original native archimedean off-diagonal density `-j(x-y)`, where

    j(d)=exp(-|d|/2)/(1-exp(-2|d|)) >0,    d!=0,

and active prime atoms `-c_n` at displacements `+/-ell_n`, where `c_n=Lambda(n)/sqrt(n)>0`, `ell_n=log n<=2a`. All other local diagonal/renormalization terms remain part of H, but cancel in the identity below.

For real bounded smooth Lipschitz u, multiplication by u and u² preserves the supported logarithmic form domain. Let h=phi*u. The weak ground-state equation `H_a(phi,f)=lambda_0<phi,f>` is lawful with f=phi*u². Subtract:

    H_a(phi*u,phi*u)-lambda_0 ||phi*u||_2²
      = H_a(phi*u,phi*u)-H_a(phi,phi*u²)
      = D_phi(u),                                          (1)

where

    D_phi(u) =
      (1/2) int_(-a)^a int_(-a)^a j(x-y)phi(x)phi(y)
                                      (u(x)-u(y))² dxdy
      + sum_(ell_n<=2a) c_n int_R phi(x)phi(x+ell_n)
                                      (u(x)-u(x+ell_n))² dx. (2)

Both prime orientations are already present in each squared difference; there is no extra hidden factor 2 multiplying the c_n displayed here. All vectors are zero extended. The continuous integral near d=0 is finite because j(d)=O(1/|d|), |u(x)-u(y)|²=O(|d|²), and phi in L2. Each prime term is finite by L2 Cauchy-Schwarz and bounded u. The symmetric bilinear algebra follows from

    u(x)²+u(y)²-2u(x)u(y)=(u(x)-u(y))².

The same identity is available as a standard nonlocal ground-state transform principle, but (1)-(2) specify the ACTUAL Weil kernel and its precise von Mangoldt coefficients. Analogues: Frank--Lenz--Wingert, *Intrinsic metrics for non-local symmetric Dirichlet forms and applications to spectral theory*, arXiv:1012.5050, and Frank--Seiringer, *Non-linear ground state representations and sharp Hardy inequalities*, arXiv:0803.0503. No external theorem supplies any missing zeta-specific positive gap.

**Important domain restriction:** (1)-(2) are proved for h=phi*u with bounded smooth Lipschitz u. This pass does NOT divide an arbitrary CC43 eigenfunction by phi or assert density of such products in Dom H. In particular, application to an actual hypothetical zero-moment h requires a lawful approximation or ground-state-transform closure theorem, not supplied here. CC43 proved phi nonnegative, not a uniform positive lower bound.

## 3. Strict positive jump energy is not enough to exclude zero eigenvalues

The continuous kernel is positive between every two distinct physical points, so D_phi(u)>=0, with strictness when u is not constant on positive-phi mass. This recovers simplicity of the ground state within the product core but gives only

    H_a(phi*u) >= lambda_0 ||phi*u||²,

which was already known from the variational minimum. If a non-ground H-null exists with lambda_0<0, the exact energy balance must be

    D_phi(u)= -lambda_0 ||phi*u||².                 (3)

There is no contradiction: both sides are strictly positive. The relevant exclusion theorem would need a LOWER bound on D_phi(u)/||phi*u||² STRICTLY GREATER than -lambda_0 on the actual parity-and-moment-constrained null class, with domain transfer proved.

If `phi` happens to belong to L-infinity with M=||phi||_infinity<infinity, let S=int_-a^a phi>0. Since j is strictly decreasing in |d|, j(|x-y|)>=j(2a) for x,y inside the cap. For every u with `int phi²u=0`,

    D_phi(u)
      >= j(2a)[S int phi u² -(int phi u)²]
      = j(2a) S min_t int phi(u-t)²
      >= j(2a) S/M * int phi² u².                 (4)

Thus

    Gamma_floor(a,phi)=j(2a) S/M

is an explicit conditional (potentially weak) non-ground spectral-gap floor on this product core. It is NOT an evaluated actual zeta constant; boundedness of phi and requisite product-core density have NOT been proved. A sufficient conditional exclusion is Gamma_floor > -lambda_0 together with domain transfer. No such inequality has been established.

## 4. Sharper odd-parity reflection conductance

Because phi is even, for real odd u, reflecting the x<0 half to x>0 gives the EXACT full continuous jump part

    D_phi,cont(u)
      = int_0^a int_0^a phi(x)phi(y) [
          j(|x-y|)(u(x)-u(y))²
          + j(x+y)(u(x)+u(y))² ] dxdy.             (5)

The first term contains same-side differences; the second is the opposite-side interaction across the physical origin. The prime jump terms in (2) remain nonnegative. Since |x-y|<=x+y and j is decreasing,

    D_phi(u) >= 4 int_0^a phi(x) u(x)²
                          [int_0^a j(x+y)phi(y)dy] dx.    (6)

No maximum principle for the FULL signed-pole Q is imported: (5)-(6) apply specifically after CC43 removes both poles and uses its true attractive ground state.

If phi>0 a.e. and the following ratio has a positive essential infimum on phi>0, define

    Gamma_odd(a,phi)
       = 2 essinf_(0<x<a,phi(x)>0)
                  [int_0^a j(x+y)phi(y)dy]/phi(x). (7)

Then D_phi(u)>=Gamma_odd||phi*u||_2² for odd product-core u. If Gamma_odd > -lambda_0 and the transform extends to any hypothetical odd zero-moment H-null, that channel is excluded. This is an explicit scalar **reflected-jump versus ground-depth** condition. It is not currently verified for the actual zeta ground state or any global cap.

The even higher null has no automatically favorable reflected plus-term for sign-changing u; it requires its separate orthogonal/moment-constrained conductance estimate. Hence (7) cannot be relabeled a solution to all three DNE contact cases.

## 5. Exact sharp contact and prime-edge controls

Retain the CC43 two-site attractive-kernel model but expose the sharp gap balance and prime-edge effect. For rational b>0 and p>=0, set

    H_(b,p)=[[-b, -(b+p)], [-(b+p),-b]],
    phi=(1,1)/sqrt(2),
    lambda_0=-2b-p,
    lambda_1=p.                                      (8)

Interpret b as continuous attractive cross-edge, p as an additional attractive discrete prime-like edge (toy model, NOT exact zeta). Give the even pole moment c(x,y)=sqrt(b)(x+y). Then original-analogue

    Q_(b,p)=H_(b,p)+2|c><c|
           =[[b,b-p],[b-p,b]],                      (9)

which is positive semidefinite for 0<=p<=2b, with eigenvalues 2b-p and p. For p=0, the zero-moment antisymmetric vector h=(1,-1) is an exact higher Q-null while the ground of H is simple positive. It is simultaneously a higher H-null. The jump representation has non-ground spectral gap

    lambda_1-lambda_0=2b+2p.                        (10)

At p=0 this equals -lambda_0=2b: EXACT equality of the proposed strict gap criterion. Thus no argument using merely a strictly attractive ground kernel, simple even ground state, nonnegative jump form, or rank-one pole stabilization can exclude a higher zero null.

At 0<p<2b, the additional edge makes `lambda_1=p>0` and yields a STRICT surplus `(lambda_1-lambda_0)-(-lambda_0)=p`. This shows HOW an arithmetic-specific jump-conductance surplus could work, but not that actual Weil's prime edges supply it: they also lower lambda_0, and their weighted spatial distribution matters.

The genuine differential first-contact and full physical positive-level-shift controls remain additional falsifiers: both possess legitimate contact/domain/ground-transform identities, so the existence of the identity alone cannot distinguish original zero contact. The toy model also explicitly fulfills the CC43 zero-moment obstruction.

## 6. Decision and next DNE frontier

**Proved:** exact positive weighted native jump decomposition (1)-(2) on the product core, strict positivity of its continuous conductance for nonconstant ratios on positive-phi support, exact odd folding (5) and inequality (6), conditional bounds (4),(7), and sharp finite-graph controls (8)-(10).

**Still open:** positivity-a.e./boundedness and product-core density for the actual pole-free ground state; any evaluated original cap-wide Gamma_odd or even constrained conductance surplus; exclusion of higher zero-moment eigenvectors; exclusion of the even/odd moment-carrying contacts; full a=53/50 positivity, RH/F4, retained transport and Lean.

**DNE2 next test:** Decide whether actual supported ground-state regularity makes the transform global, then derive or reject a quantitative `Gamma_odd > -lambda_0` estimate from the precise Weil kernel and ground state. Audit the even second-eigenvalue/moment constraints separately. Reject proofs that replace the unknown `phi` by an arbitrary positive bump or infer a signed strict gap solely from kernel positivity.

No new whole-aperture sign follows from NF14's positive E64 and NF10's positive F112, whose middle and source-Schur couplings remain open. This DNE branch does not modify the active Coupled, Aperture, paused Global, or Shadow branches.

## 7. Validation / external comparison

The exact graph controls admit an independent rational validator. Their execution checks are **model discriminators**, not computations of actual zeta eigenfunctions. The infinite-domain form algebra is an analytic deduction from CC27/CC41/CC43 and is not Lean-certified by running finite tests. Standard ground-state transform comparisons: https://arxiv.org/abs/1012.5050 and https://arxiv.org/abs/0803.0503.
