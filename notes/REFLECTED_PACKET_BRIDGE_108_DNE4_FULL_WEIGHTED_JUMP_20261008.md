# RPB108 DNE4 — Complete ground-state-weighted jump identity on every admissible quotient

Date: 2026-10-08 America/Los_Angeles. Independent research branch `research/rpb108-direct-null-exclusion`, parent `be834f237121d8625be4551d83f82cd80345b066` (DNE3). Definitions: [DNE4 complete weighted domain](../docs/TERMINOLOGY_RPB108_DNE4_WEIGHTED_FORM_DOMAIN.md). Concurrent CC49 and NF16 are read-only and NOT merged. **Result: analytic full-domain identity and exact domain equality. No numeric zeta ground state, gap surplus, actual null exclusion, RH/F4 or Lean certification.**

## 1. The exact original arithmetic input

On I=(-a,a), let `J_a` be the complete POSITIVE pure-jump form from DNE3, including zero-extension to all real positions:

    J_a(f) = (1/2) int_R int_R j(x-y)|f(x)-f(y)|² dxdy
           +sum_(ell_n<=2a) c_n int_R |f(x)-f(x+ell_n)|² dx,

    j(d)=exp(-|d|/2)/(1-exp(-2|d|)),
    c_n=Lambda(n)/sqrt(n), ell_n=log n.

Every original prime power is present; the undirected prime edge in the displayed integral counts the two physical translation orientations exactly once each in the square expansion. The supported form domain is precisely the canonical `D_a` (DNE3), and `H_a=J_a-kappa_a ||.||²`, with the original signed poles removed **only** in H. The full original Q is obtained by restoring those signed Hermitian pole terms.

CC43/CC41: H has a normalized simple nonnegative even physical ground eigenfunction phi, eigenvalue lambda0, with `phi in Dom H`. DNE2: `phi>0` Lebesgue almost everywhere. Set `mu=kappa_a+lambda0` so that, for every g in D_a,

    J_a(phi,g)=mu <phi,g>,                              (1)

with `mu` equal to the bottom of the positive J_a spectrum. No H1, phi-infinity, inverse-phi bound, pointwise endpoint value or boundary trace is assumed.

Decompose J_a into its INTERNAL jump-pair form `B_a` and exterior killing `K_a`:

    J_a(f)=B_a(f)+int_I k_a^tot(x)|f(x)|²dx.             (2)

Here B_a uses j(x-y) on I² and each prime edge with x and x+ell_n both in I; the total exterior killing k_a^tot equals the continuous DNE3 k_a(x) plus `sum_n c_n(1_{x+ell_n notin I}+1_{x-ell_n notin I})`. Both pieces are nonnegative. For f in D_a, int k_a^tot |f|² is finite. Importantly **do not delete it** from (1) or (2).

## 2. New theorem — exact full weighted domain and energy

Define `m_phi(dx)=phi(x)²dx`. For measurable real u on I let

    W_phi(u)= (1/2) int_I int_I j(x-y)phi(x)phi(y)
                                           (u(x)-u(y))² dxdy
        +sum_(ell_n<=2a)c_n int_(x,x+ell_n in I)
                  phi(x)phi(x+ell_n)(u(x)-u(x+ell_n))²dx.  (3)

Interpret W_phi as +infinity when the integrals diverge. This is a nonnegative closed Markov jump form on `L²(m_phi)`. Let the DNE2 full Doob form be

    E_phi(u)=H_a(phi u)-lambda0||phi u||²
            =J_a(phi u)-mu ||phi u||²,
    Dom(E_phi)={u in L²(m_phi):phi u in D_a}.           (4)

**Theorem DNE4.** On the COMPLETE supported canonical logarithmic domain,

    Dom(E_phi)={u in L²(m_phi): W_phi(u)<infinity},
    E_phi(u)=W_phi(u)                                  (5)

for every real u in this domain. Complex vectors follow by separate real/imaginary parts and Hermitian polarization. Consequently (3) is valid for the ratio of ANY actual higher H eigenfunction h/phi; smoothness, bounded quotient, a positive boundary trace, and density of the specific DNE1 smooth product tests are **not** premises.

### Proof, direction I: arbitrary supported physical f has no hidden weighted energy

The interval indicator `1_I` belongs to D_a. Indeed its Fourier transform is O(1/|xi|) for |xi| large, and int log(e+|xi|)/(1+xi²)dxi is finite. Equivalently its positive continuous exterior killing has only an integrable logarithmic divergence at the endpoints (DNE3); prime exterior costs are finite.

For real **bounded** f in D_a and eps>0, let `phi_eps=phi+eps` on I and define `g_eps=f²/phi_eps` on I, zero outside. The usual bounded Lipschitz chain/product rule for the pure-jump form applies: f² in D_a, `1_I` in D_a, and the map t ->1/(t+eps) is bounded Lipschitz on t>=0. Therefore g_eps belongs to D_a; no division by zero is performed.

Insert g_eps in the *actual* ground equation (1). For every internal continuous or discrete prime jump edge x,y in I, the elementary exact identity

    (f_x-f_y)² - (phi_x-phi_y)
                 [f_x²/(phi_x+eps)-f_y²/(phi_y+eps)]
      =(phi_x+eps)(phi_y+eps)
        [f_x/(phi_x+eps)-f_y/(phi_y+eps)]²           (6)

holds (the constant eps cancels in the phi difference). At an EXTERIOR edge y outside I, the same subtraction is `eps f_x²/(phi_x+eps)`, not zero. Thus for the complete original J, including its killing,

    J_a(f)-J_a(phi,g_eps)
       =W_eps(f) + int_I k_a^tot(x)
                            eps f(x)²/(phi(x)+eps) dx, (7)

where W_eps has exactly the inner edge weights from the right side of (6).

Using (1) and `J_a(phi,g_eps)=mu<phi,g_eps>`, obtain

    E_phi(f/phi)
       =W_eps(f)
        +int_I k_a^tot eps f²/(phi+eps)
        -mu int_I eps f²/(phi+eps).                 (8)

Because phi>0 a.e., the latter two integrals tend to zero by dominated convergence: respectively, `k_a^tot f²` is integrable by (2) and f² is integrable by hypothesis. Hence `W_eps(f)->E_phi(f/phi)`. Fatou on the nonnegative internal pair measures gives

    W_phi(f/phi)<=E_phi(f/phi).                        (9)

The bounded truncations f_N=(-N)vee f wedge N converge to f in the `J_a+L²` norm. The zero-extended pure-jump and killing integrands are dominated by four times those for f, so this follows from pointwise convergence and dominated convergence without H1 regularity. Moreover f_N/phi -> f/phi in weighted L²; subsequences converge a.e. Fatou extends (9) to ALL f in D_a. In particular every u in Dom E_phi has finite W_phi and W_phi(u)<=E_phi(u).

### Proof, direction II: every finite weighted jump-energy vector belongs to the full transformed domain

First take real u bounded with W_phi(u)<infinity. The elementary two-edge estimate, for nonnegative A,B and |u|,|v|<=M, is

    |A u-B v|² <=2AB|u-v|²+2M²(A-B)².           (10)

It follows by splitting into `sqrt(AB)(u-v)` plus `(sqrt(A)-sqrt(B))(sqrt(A)u+sqrt(B)v)`. Applied to A=phi(x),B=phi(y) on every internal original continuous/prime edge, and to the zero-extended outside edges, this shows `phi*u in D_a`, because phi is in D_a and W_phi(u) is finite. The same estimate applies to `phi*u²`, since `|u_x²-u_y²|<=2M|u_x-u_y|`; hence that vector is a lawful ground-equation test.

Subtract (1) with test phi*u² from J_a(phi*u). The complete edge identity now gives exactly

    J_a(phi*u)-J_a(phi,phi*u²)=W_phi(u).             (11)

At exterior edges the two terms coincide, so their killing contributions cancel (rather than being silently omitted). The weak ground equation (1) makes (11) identical to `E_phi(u)=W_phi(u)`.

Finally any finite-W u has bounded truncations u_N in Dom W with `u_N->u` both in weighted L² and in W-energy: the jump differences of `u_N-u` are bounded by twice those of u and tend to zero pointwise, so dominated convergence applies. The complete transformed form E_phi is closed (DNE2), and E_phi(u_N-u_M)=W_phi(u_N-u_M), so u belongs to Dom E_phi and E_phi(u)=W_phi(u). This proves (5) without assuming a form-core theorem for the old DNE1 smooth multipliers. QED.

## 3. Consequences for actual hypothetical null vectors

The unitary full-domain transform has associated nonnegative selfadjoint generator G_phi, and its form is EXACTLY the weighted jump expression (3) on every eigenvector. Thus if `H_a h=0` and h!=0 (the DNE/CC moment-zero pole-free channel), the a.e. ratio u=h/phi is an admissible vector satisfying

    W_phi(u)=(-lambda0)||h||².                        (12)

In particular for odd h, since phi is even, the full odd reflection formula from DNE1 applies to u itself, not only to smooth approximate quotients:

    W_phi(u)>=4 int_0^a phi(x)u(x)²
                    [int_0^a j(x+y)phi(y)dy]dx.      (13)

The original prime jump terms are additional nonnegative energies. If a valid arithmetic bound makes the right side exceed `(-lambda0)||h||²` for all nonzero odd h, no odd pole-free zero mode exists. The scalar `Gamma_odd` of DNE1 is now a genuine sufficient FULL-DOMAIN criterion when its ratio is defined and evaluated; **the numerical/sign inequality `Gamma_odd> -lambda0` remains unproved**.

Even zero-moment modes obey (12) and additionally `<h,phi>=0`, `c(h)=0`; the analogous strictly weighted constrained spectral lower estimate remains open. Moment-carrying original Q nulls retain their original even/odd signed pole terms and are NOT settled by (12).

## 4. Exact killed-graph control and threshold sharpness

To test (6)-(11), use the rational symmetric three-site jump form with internal conductances `j_01=j_12=1/2, j_02=1/4` and exterior killing rates `k=(3/2,1/2,3/2)`. Its positive jump matrix is

    J=[[9/4,-1/2,-1/4],[-1/2,3/2,-1/2],[-1/4,-1/2,9/4]].

The normalized-up-to-scale positive ground state `phi=(1,2,1)` satisfies `J phi=phi`, so mu=1 and the ground form E=J-I has exact weighted conductances `j_ij phi_i phi_j`. For all trial vectors the weighted sum equals `f^T(J-I)f`; moreover the eps-Picone identity includes the nonzero killing residual `sum_i k_i eps f_i²/(phi_i+eps)` and subtraction of `mu sum_i eps f_i²/(phi_i+eps)`. These are exact algebraic and boundary controls, not actual Weil spectral data.

Let H=J-(5/2)I. Its ground eigenvalue is -3/2 and its higher odd eigenvector f=(1,0,-1) has Hf=0. Its quotient u=f/phi has weighted jump energy 3, mass 2, and gap ratio 3/2 exactly `-lambda0`. Hence the COMPLETE weighted integral identity coexists with a higher odd null. DNE4 solves the domain-transfer problem; it does NOT provide the strict arithmetic spectral surplus necessary to exclude that null in the actual Weil problem.

## 5. Custody / stopping decision

**Closed:** the full-domain weighted-jump equality (5), including all original continuous jump and prime-power conductances, and legitimate application of DNE1's odd folding to any actual transformed eigenfunction. The only additional native form fact needed was `1_I in D_a`, valid at logarithmic order; it would fail in some stronger nonlocal Sobolev settings.

**Open:** a strict `Gamma_odd(a,phi)>-lambda0(a)` inequality for actual Weil coefficients; the even constrained weighted spectral floor; parity moment-carrying null exclusion; any all-aperture first-contact impossibility; whole a=53/50 positivity; RH/F4/transport/Lean. DNE4 imports no positive target sign from CC49 or the concurrent NF16 finite E96/remainder certificate.

A standard nonlocal Dirichlet-form decomposition is consistent with the proof, but no external regularity/h-transform theorem is used to assert the crucial domain equality without verification. Structural references: Schilling--Uemura, *On the Structure of the Domain of a Symmetric Jump-type Dirichlet Form*, Publ. RIMS 48 (2012), https://doi.org/10.2977/PRIMS/58; Frank--Lenz--Wingert, *Intrinsic metrics for non-local symmetric Dirichlet forms and applications*, https://arxiv.org/abs/1012.5050. The explicit elementary epsilon-test, exterior residual payment, and truncation argument above are the stated proof.
