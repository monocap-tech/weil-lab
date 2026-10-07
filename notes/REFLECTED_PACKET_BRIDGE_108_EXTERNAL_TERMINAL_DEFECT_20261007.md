# RPB108: outside-zeta terminal-defect mechanisms and exact transfer gaps

Date: 2026-10-07 UTC. Recovered live head 11d47c01b6ad75c1e7832e522d7665c8e458c3b2 and the current cursor.
Definitions: [external terminal-defect comparison](../docs/TERMINOLOGY_RPB108_EXTERNAL_TERMINAL_DEFECT.md).
Category: structural comparison requested by the user; actual sharp-head arithmetic obstruction. Analytic, not Lean-certified.

## Finding

The closest external operator is the EXTERIOR Dirichlet logarithmic Laplacian. Its zero mode can retain the inverse-square-root-log boundary scale. An explicit finite-rank logarithmic-carrier construction below permits, simultaneously, the complete derivative filtration, singular endpoint trace, exact full mixed-nullity and a strictly positive logarithmic height coefficient. Thus these structures do not generically exclude a terminal defect, even at unshifted energy zero.

Outside elimination theorems require an additional selected boundary domain or an exact complete mixed sampling system. Neither is attached to our actual mixed-null graph. No actual bounded return was found, and the global graph does not shorten. The remaining global theorem is still actual unshifted full-null source range -> nonpositive signed sharp/log liminf.

## 1. Closest published operator: logarithmic Laplacian

Primary inputs, all inspected:

- [Chen–Weth, arXiv:1710.03416, Theorem 1.4](https://arxiv.org/pdf/1710.03416): bounded-domain exterior problem with symbol 2 log|xi|, compact logarithmic energy carrier, simple strictly positive first eigenfunction and discrete spectrum. Theorem 1.8 makes the maximum principle equivalent to STRICT positivity of the first eigenvalue.
- [Feulefack–Jarohs–Weth, arXiv:2010.10448, Corollary 1.4](https://arxiv.org/pdf/2010.10448): logarithmic-Laplacian eigenfunctions on bounded Lipschitz domains are bounded and interior continuous; an exterior sphere condition gives continuity with zero boundary values.
- [Hernandez-Santamaria–Lopez Rios–Saldana, arXiv:2401.18033, Theorems 1.1 and 1.4, Lemma A.3](https://arxiv.org/pdf/2401.18033): optimal upper boundary scale ell(d)^(1/2), ell(d)=1/|log(min(d,0.1))|, positive Hopf lower normalized liminf for a continuous nonnegative nonzero weak supersolution, and the weak scaling identity.

Here is the comparison deduction with its hypotheses checked. Start with any bounded interval I and the first eigenfunction phi. For the unitary dilation U_t phi(x)=t^(-1/2)phi(x/t), Fourier change of variables gives

    E_L,tI(U_t u,U_t v)=E_L,I(u,v)-2 log(t)<u,v>,
    lambda_k(tI)=lambda_k(I)-2 log(t).

At t*=exp(lambda_1(I)/2), the UNshifted exterior operator on t*I is nonnegative with a one-dimensional zero kernel. Before that scale its first eigenvalue is strictly positive. Phi*=U_t* phi is positive, bounded, continuous with zero exterior values and belongs to H(t*I), hence to the supersolution carrier V(t*I). Its null equation is E_L(phi*,v)=0 for every supported energy test. The interval satisfies both sphere conditions. The boundary theorems apply with f=0 and prove

    0 < liminf_(d->0) phi*/ell(d)^(1/2)
       <= limsup_(d->0) phi*/ell(d)^(1/2) < infinity.

Consequently phi* is not globally H^(1/2): the zero-extension exterior Hardy contribution dominates integral_0^delta dd/[d log(1/d)], which diverges. Its one-dimensional kernel has F_0=K, F_1=0, matching the actual r=1 terminal filtration. The same normalized scale holds at a positive first eigenvalue, using f=lambda phi and the supersolution inequality when lambda>0.

This does NOT prove existence of an exact averaged trace limit or a sharp/log source limit for phi*. The cited theorems provide upper bounds and positive lower liminf, not our exact kappa_R or an actual divisor identity. That mismatch is retained. Dilation constructs a changed comparison vector and operator; it is not same-vector native transport and is not an aperture computation.

The useful conclusion is permissive: exterior zero support, logarithmic principal symbol, nonnegative first contact and a nonzero critical boundary scale coexist in a genuine unshifted nonlocal problem. Its maximum-principle theorem cannot exclude contact because its hypothesis already requires lambda_1>0. Applying it at contact would assume the conclusion.

## 2. Full matched chain and logarithmic coefficient: explicit construction

This construction is proved here, rather than attributed to an external paper. It upgrades the earlier supported chain control to an EXACT full mixed-null form and a specified spectral head. It is an artificial comparison, not actual zeta nullity.

Fix I=(-a,a) and r>=1. Use the moment-corrected chain construction already audited: a terminal g has smooth interior, equals c_R/sqrt(log(1/v)) at the right edge and c_L/sqrt(log(1/v)) at the left edge, with c_L=sigma c_R, sigma=+/-1, c_R!=0. Smooth cutoffs join these edge profiles. Subtract sufficiently smooth interior functions to make the first r-1 polynomial moments vanish. Its compact (r-1)-fold primitive h then gives

    V=span{h,Dh,...,D^(r-1)h},
    dim(V intersect H^j)=r-j for 0<=j<=r,
    ker(kappa_R|V)=V intersect H^1.

We consume that physical construction unchanged. In particular the chain's terminal trace is an exact averaged limit and its primitives have the stated regular endpoint asymptotics. No actual equation was asserted by that earlier control.

Now let E be the canonical positive logarithmic Fourier inner product with weight w(xi)=log(e+|xi|), using F(u)(xi)=integral u(x)exp(-i xi x)dx and measure dxi/(2pi). Let P_V be E-orthogonal projection onto V and define

    q_0(u,v)=E((I-P_V)u,(I-P_V)v).

This is a nonnegative CLOSED supported form. To check closure rather than assume it: P_V is bounded from the logarithmic carrier to finite V. In fact every E-orthonormal chain vector e_j satisfies w F(e_j) in L2, by the cusp Fourier estimate below, so E(u,e_j)=<u,b_j>_L2 with b_j=1_I F^(-1)(w F(e_j)) in L2(I). Thus E(u)=q_0(u)+sum_j|<u,b_j>|^2, and q_0(u)+||u||_2^2 is equivalent to E(u)+||u||_2^2. Its full mixed kernel is EXACTLY V. All vectors in the chain satisfy q_0(v,u)=0 for EVERY supported logarithmic test u.

The associated operator is a supported logarithmic background minus r bounded finite-rank L2 negative rows. No freely assigned physical sample vectors or energy-to-mass domain swap occurs. For q_mu=q_0+mu<u,v>, the unchanged V is its physical mu eigenspace; its filtration and trace do not change. The family q_epsilon is strictly positive for epsilon>0, reaches the r-dimensional kernel at zero, and is negative on V for epsilon<0. This is a scalar-parameter contact control, not a claim about native aperture geometry.

For completeness the continuous sharp coefficient is exact. A cut-off endpoint cusp f(v)=1/sqrt(log(1/v)) satisfies

    integral_0^delta f(v)chi(v)exp(-i xi v)dv
       =1/[i xi sqrt(log|xi|)]
          +O(1/[|xi| log^(3/2)|xi|]), xi->+infinity.

Proof: integrate by parts, f'(v)=1/[2v log^(3/2)(1/v)]. Below 1/xi, replace the exponential by 1; the error is bounded by xi integral_0^(1/xi) v f'(v)dv=O(log^(-3/2)xi). Above 1/xi, monotonicity of f' on a sufficiently short collar and Dirichlet's oscillatory integral bound give O(f'(1/xi)/xi)=O(log^(-3/2)xi). Smooth cutoff contributions decay faster. Reflection treats the other ray. Interior moment corrections have O(|xi|^-2) Fourier decay and do not alter the term.

Therefore the terminal vector has

    F(g)(xi)=[c_L exp(ia xi)-c_R exp(-ia xi)]
                 /[i xi sqrt(log|xi|)]
             +O(1/[|xi| log^(3/2)|xi|]).

Every regular chain vector has extra inverse powers of xi. For any v in V define

    M_v(T)=(1/(2pi)) integral_(1<|xi|<=T)
                    |xi| w(xi)|F(v)(xi)|^2 dxi.

Squaring the last formula and integrating gives

    M_v(T)=[(|kappa_R(v)|^2+|kappa_L(v)|^2)/pi] log T
                    +O_v(1+log log T).

The interference integral exp(2ia xi)/xi converges by Dirichlet; the squared-error cross term integrates as O(log log T). Regular chain terms have finite M. For a PHYSICAL orthonormal basis of V, boundary balance thus gives

    M_V(T)/log T -> (2/pi)sum_j|kappa_R(v_j)|^2 > 0.

This is the same filtration, balanced trace Gram and numerical logarithmic coefficient as the actual theorem, with a specified continuous Fourier spectral head. The background source is w^(1/2)F(u); the negative source is the finite vector (<u,b_j>)_j. Their signature pairing is exactly q_0, so the FULL mixed-null source relation holds. Assign negative rows any fixed finite heights; their signed head changes by O(1), and the positive logarithmic coefficient survives. The unsigned continuous source tail is O(1/T), directly from |F(g)|^2=O(1/[T^2 log T]).

What differs is precise and decisive: this source range is continuous Fourier plus artificial finite rows, NOT the actual zeta zero-analysis range. It has no literal actual explicit formula or actual paired-source translation law. Its derivative promotion holds on the regular kernel flag by construction; its finite-rank correction is not asserted to commute with differentiation on the whole physical carrier. The construction proves that even exact full mixed-nullity plus the entire terminal morphology and a positive sharp/log coefficient are structurally compatible. It does not produce an actual contact kernel.

## 3. Published mechanisms that eliminate or permit a defect

| Framework and precise theorem | Defect mechanism | Actual transfer audit and positive-eigenmode test |
|---|---|---|
| Fucci–Gesztesy–Kirsten–Littlejohn–Nichols–Stanfill, arXiv:2102.00685, Theorem 3.1, equations (3.5)-(3.9), and Theorem 2.13 | For a strictly positive closed symmetric minimal operator S, Friedrichs S_F stays strictly positive; Krein S_K instead has ker S_K=ker S*. Singular Sturm–Liouville Friedrichs domains impose specified generalized zero boundary values. | Must construct the SAME minimal operator, prove its strict lower bound, identify the native realization as S_F and identify its generalized boundary trace. Form closure alone does not do this. Native kappa is defined on the kernel, not shown to be a continuous form-domain boundary condition. A shift also has a Friedrichs realization, so this name alone cannot distinguish the actual positive eigenmode. |
| Kirsten–Loya–Park, arXiv:math-ph/0511002, Theorems 1.2, 2.1 and 5.2 | Critical Bessel expression -D^2-1/(4x^2) has coefficients c_1 sqrt(x)+c_2 sqrt(x)log(x). Friedrichs sets c_2=0. With outer Dirichlet data, a non-Friedrichs zero mode exists exactly when log R=tan theta; negative mode iff tan theta<log R. Non-Friedrichs realizations have anomalous logarithmic resolvent/heat terms. | Permits contact with a singular coefficient. Its sqrt(x)log(x) boundary variable and inverse-log spectral anomaly are NOT kappa/sqrt(log) and the native signed log head. No boundary-domain or height intertwining is available; no transfer, irrespective of eigenvalue shift. |
| Baranov–Belov–Borichev, arXiv:1112.5551, Theorems 1.1-1.3 | Exact PW_pi kernel system and its biorthogonal family: every mixed partition has defect at most one; positive upper density of the selected biorthogonal subset forces zero defect; an exact exponential system with one-dimensional defect is also constructed. | Potentially excludes the terminal quotient only after an actual physical isometry, exact/minimal system, prescribed partition and positive density of THAT subset are proved. Raw native multiplicity copies are value duplicates, and native J-Gamma orthogonality is not orthogonality to this partition. A valid map must send Q=0 to the homogeneous mixed orthogonality while retaining the mu mass residual for the actual positive eigenmode. No such map has been proved. |

Primary locations: [extension theorem](https://arxiv.org/pdf/2102.00685), [critical Bessel theorem](https://arxiv.org/pdf/math-ph/0511002), [mixed-system theorem](https://arxiv.org/pdf/1112.5551). These are exact hypothesis audits, not assertions of equivalence. The finite derivative chain is not a Jordan chain of the self-adjoint native operator: all its vectors are ordinary kernel vectors. A theorem about algebraic multiplicity or Jordan-root chains cannot be imported by renaming D.

For the Friedrichs route the strict-minimal-lower-bound hypothesis is essential. At a hypothetical contact, smooth form-core approximants to a nonzero kernel vector have q tending to zero and nonzero limiting mass. Thus a strict bound on that same core cannot be inferred from closed nonnegativity. Certified smaller-window bounds do not provide it on the contact window. Our projection control is itself a closed form with a smooth core and a kernel, so calling a realization a Friedrichs form closure cannot eliminate that kernel without the additional strict bound or a genuinely different boundary restriction.

## 4. Exact remaining transfers and controls

Two outside exclusion mechanisms survive as CONDITIONAL research leads: identify actual unshifted nullity with a complete mixed-system defect, or derive a null-specific boundary-domain condition from the full arithmetic equation. Neither is a new proven endpoint criterion or a discharged edge. The published logarithmic-Laplacian and Bessel examples instead show why generic first-contact exclusion is false.

The graph remains: actual full-null equation -> established chain and positive sharp/log limit; independently, MISSING actual source arithmetic -> nonpositive sharp/log liminf; their contradiction would exclude contact. No actual bounded-return mechanism is supplied here.

All four required controls remain active. The actual rough positive eigenmode has the same native boundary/height coefficient; any proposed transfer that drops its mu mass residual fails. The artificial compact-good-row control remains outside the actual divisor, as is our stronger continuous/finite-rank null construction. Fixed finite source restoration changes the normalized head by o(1), and cannot kill either coefficient. The two-row comparison contact already supplies auxiliary contact geometry; the new construction supplies arbitrary full chain dimension and an explicit continuous log coefficient but still no actual rows. No comparison is substituted for actual native full-nullity.

The manifest pins internal custody and external theorem locations. Rational projection/null controls and coefficient/shift checks accompany the analytic argument. No Lean proof, axiom audit, new aperture certificate, same-vector dilation claim, historical packet attachment, actual endpoint exclusion or F4 closure is asserted. The cursor is updated additively and concurrent aperture work is preserved.
