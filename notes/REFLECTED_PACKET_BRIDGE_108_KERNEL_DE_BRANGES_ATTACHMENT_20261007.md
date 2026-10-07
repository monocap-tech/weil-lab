# RPB108: the actual null chain is a finite de Branges space in physical mass

Date: 2026-10-07 UTC. Recovered live head 81dca4d9765fbcbfe9d0718f3d116ce6f22b44ac and current canonical cursor.
Definitions: [kernel de Branges attachment](../docs/TERMINOLOGY_RPB108_KERNEL_DE_BRANGES_ATTACHMENT.md).
Category: actual functional-model attachment and a precise sign/quotient obstruction. Analytic, not Lean-certified.

## Result

The NF43 exponential inverse extends to exact first-order complex null division. It proves that the Fourier image of every nonzero finite actual kernel at nonnegative contact, with its PHYSICAL L2 norm, is a finite-dimensional de Branges space. Its top derivative-chain generator has a Fourier profile Phi with ONLY REAL zeros, and

    B_K=Phi times polynomials of degree <=r-1.          (1)

This is a structural equivalence with all three axioms checked against the complete actual mixed-null equation. It does not borrow a merely analogous equation from an outside model. It also identifies two failed transfers: native-energy evaluation does not descend through its kernel, and the signed actual sharp head uses the reflected OFF-DIAGONAL reproducing kernel, not its positive diagonal.

The known lowest positive eigenspace has exactly the same de Branges attachment, with the spectral level retained. Thus de Branges division, representation and diagonal kernel positivity alone cannot exclude its terminal defect or force the required nonpositive signed sharp/log liminf. The unshifted actual divisor/range condition remains indispensable.

## 1. The complete form is skew under a lawful derivative

For supported canonical u,v with Du,Dv canonical, global integration by parts gives

    Q(Du,v)+Q(u,Dv)=0.                               (2)

The archimedean Fourier terms cancel exactly because their two multipliers are -i eta and +i eta. Absolute convergence follows by Cauchy-Schwarz in the logarithmic form domain. Every actual frozen prime translation commutes with D, so the same identity holds for each prime correlation and scalar term. No prime is discarded.

For the full pole term Q_P(u,v)=2 C(u) overline(C(v))-2 S(u) overline(S(v)), use C(Du)=-S(u)/2 and S(Du)=-C(u)/2. Its first derivative contribution is -S(u) overline(C(v))+C(u) overline(S(v)); the other is its negative. Thus the indefinite poles ALSO satisfy (2). Global H1 support ensures no boundary delta. The identity holds as well for the physical mass term and hence for Q_mu=Q-mu<.,.>_L2.

Equation (2) makes Q(Du,u) purely imaginary. This is the precise extra information needed for one complex division; a second-order positivity estimate or rough differentiation is unnecessary.

## 2. Compact complex division from one exact Fourier zero

Take w outside R, lambda=-iw, and h canonical with F_h(w)=0. Define on [-a,a]

    u(x)=exp(lambda x) integral_(-a)^x exp(-lambda y)h(y)dy,

and set u=0 outside. The left endpoint is zero by construction and the right endpoint is zero because the integral there equals F_h(w). Thus the distributional equation is globally

    (D-lambda)u=h,
    F_u(z)=i F_h(z)/(z-w).                            (3)

There is no cutoff error, boundary delta or enlarged-support substitution. Since Re lambda=Im w!=0, the real-frequency inverse multiplier 1/(-i eta-lambda) is bounded and gains one derivative. Consequently u and Du are canonical and u is globally H1. More generally h in global H^m implies u in H^(m+1). The weighted H1 statement follows from the same multiplier inequality with the logarithmic weight.

If h is in the full actual K and Q>=0, test EXACT mixed nullity against this lawful u:

    0=Q(h,u)=Q(Du,u)-lambda Q(u,u).

Take real parts and use (2): (Re lambda)Q(u,u)=0. Therefore Q(u,u)=0. Nonnegative-form Cauchy-Schwarz gives Q(u,v)=0 for EVERY canonical v. Hence

    u in K intersect H1, and Du=h+lambda u in K.      (4)

This is an actual compact physical realization of division, not an assumed inverse on selected coefficients. It changes the physical vector.

For completeness, off-real zero flipping also preserves the complete native energy on the whole canonical domain wherever the zero permits (3). The flipped physical vector is (D+bar lambda)u, whose Fourier profile is F_h(z)(z-bar w)/(z-w). Expanding both Hermitian energies, their difference is a scalar multiple of Q(Du,u)+Q(u,Du)=0. At contact this native seminorm is degenerate; norm preservation alone is not a Hilbert-space attachment.

## 3. No common nonreal zero; the generator has only real zeros

Suppose every vector of K vanished at one nonreal w. The injective compact inverse (3)-(4) would map all r dimensions into F_1, whose proved dimension is r-1. Impossible. Therefore K has no common nonreal Fourier zero.

The exact derivative-chain theorem gives K=span{D^j h_*:0<=j<r}, with h_* in H^(r-1). Its profiles are (-iz)^j F_h*(z). Any zero of F_h* is common to the whole kernel. It follows that F_h* has no nonreal zeros. Equivalently, division of h_* at such a zero would put a nonzero vector into F_r={0}.

Reality and definite parity of h_* allow multiplication of its profile by a constant phase to obtain a real-type Phi: Phi(bar z)=overline(Phi(z)). This proves (1). Common real zeros and their multiplicities are NOT removed. Arbitrary kernel profiles can still have nonreal zeros contributed by their degree <=r-1 polynomial; lawful division removes those polynomial factors.

For every nonreal w the division map is in fact a bijection

    {h in K:F_h(w)=0} -> F_1.

Its forward direction is (4). Conversely, v in F_1 has (D-lambda)v in K and its Fourier value at w is zero. The top generator's nonzero evaluation gives exactly the dimension r-1 on the left. This extends NF43's two-moment inverse to a full complex division family without aperture calculations.

## 4. Exact de Branges attachment; every hypothesis checked

The named outside framework is the three-axiom characterization of de Branges spaces. Primary source read: Yurii Belov, *Complementability of exponential systems*, C. R. Acad. Sci. Paris I 353 (2015), 215-218, Section 3.1, p.217, [published PDF](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2014.12.004.pdf), DOI 10.1016/j.crma.2014.12.004. It records nonreal zero-flip isometry, bounded nonreal evaluation and conjugation symmetry, and their equivalence with the H(E) model via de Branges' Theorem 23. Its subsequent additional exclusion of common REAL zeros is not assumed here.

| Hypothesis on B_K | Actual verification |
|---|---|
| Nonzero Hilbert space of entire functions | Compact support gives entire F_h; Fourier injection and finite-dimensional K give a complete space with the physical mass inner product. |
| Nonreal zero-flip membership and isometry | Equations (3)-(4) put the flipped vector (D+bar lambda)u in K. On real eta, |(eta-bar w)/(eta-w)|=1; Plancherel proves EXACT physical mass equality. |
| Bounded nonreal evaluation | |F_h(w)|<=sqrt(2a) exp(a|Im w|)||h||_L2. No native-energy estimate is substituted. |
| Conjugation symmetry and isometry | F_h^#=F_(overline(h(-.))). Reality/reflection invariance of the actual form preserves K; the physical mass is unchanged. |

Thus the actual carrier meets the axiomatic definition, not merely a resemblance to a zeta-themed de Branges construction. No zeta-specific de Branges spectral measure, canonical-system Hamiltonian or zero-sampling theorem is identified by this result. The entire-function classification can now lawfully be applied to this FINITE carrier with this norm.

The multiplication model explicitly PERMITS the terminal defect. Multiplication by z within B_K has domain Phi times polynomials of degree <=r-2, corresponding precisely to F_1 under the physical Fourier map. Its domain has codimension one; it is not dense in this finite-dimensional Hilbert space. Its highest-degree vector is not in the global L2 multiplication domain, since the terminal derivative is not H1. Standard densely defined selfadjoint-operator conclusions cannot be silently imposed on this finite model. We do not assert a selfadjoint extension or use its spectral nodes as the actual zeta divisor.

## 5. The exact signed head samples a reflected off-diagonal kernel

Use the complete source-pair convention pinned in NF33. With z_rho=theta_rho+i beta_rho,

    p_rho(h)=[F_h(z_rho)+F_h(bar z_rho)]/2,
    n_rho(h)=[F_h(bar z_rho)-F_h(z_rho)]/2.

The sign in n follows the registered exp(i theta x)sinh(beta x) convention. Hence, for ANY physical ONB of K,

    sum_j (|p_rho(h_j)|^2-|n_rho(h_j)|^2)
       =Re Kcal_K(z_rho,bar z_rho),                 (5)
    S_K(T)=sum_(|theta_rho|<=T) |theta_rho|
                      Re Kcal_K(z_rho,bar z_rho).   (6)

All actual copies and existing normalization weights are retained; if the divisor is grouped into weighted pairs, the same fixed pair weight multiplies (5)-(6). This is a finite-head identity, so no conditional infinite interchange is used.

Choose real orthonormal polynomials p_0,...,p_(r-1) for the positive physical measure |Phi(eta)|^2 d eta/(2pi). Then

    Kcal_K(z,w)=Phi(z) overline(Phi(w))
                         sum_(j<r) p_j(z) overline(p_j(w)),
    Kcal_K(z,bar z)=Phi(z)^2 sum_(j<r) p_j(z)^2.     (7)

In contrast, the positive diagonal is |Phi(z)|^2 sum |p_j(z)|^2. These coincide only for real z. Hermite-Biehler/RKHS diagonal positivity gives no sign for the real part in (7).

Exact two-dimensional de Branges control: span{1,z}, norm ||a+bz||^2=|a|^2+|b|^2/64, has ONB {1,8z}. A linear zero flip preserves this norm, evaluations are bounded and conjugation is isometric. Its kernel is 1+64 z bar w. At z=i/4, WITHIN the accepted transverse strip,

    Kcal(z,z)=5, but Re Kcal(z,bar z)=-3.

At z=0 both are +1. Thus even a genuine de Branges space has both signs in the reflected observation; diagonal positivity is the wrong sign theorem. This polynomial example is not a compact physical or actual-divisor model and is not represented as a counterexample to global native positivity.

## 6. The native-energy quotient cannot supply the missing evaluation axiom

At nonzero contact, the seminorm sqrt(Q(h,h)) vanishes on K. A nonreal point evaluator cannot descend to D_a/K: the generator has NONZERO value at EVERY nonreal w, whereas its class is zero. In particular an estimate |F_h(w)|<=C_w sqrt(Q(h,h)) is false there for every nonreal w.

Canonical logarithmic evaluation continuity and positive-source observability do not repair this: their norms are nonzero on K. The physical mass norm on B_K is also nonzero there. Using any of these bounds as the native-energy evaluation axiom would change the Hilbert space and discard the exact issue.

This is the precise failed transfer for treating the full semidefinite native form itself as a de Branges Hilbert norm at contact. On the kernel, the physical-norm attachment of Section 4 succeeds. On the native-energy quotient with unchanged Fourier evaluations, it fails before any reproducing-kernel theorem can be used. No new equivalent endpoint criterion is offered as a replacement for the arithmetic gate.

## 7. Controls, level custody and remaining theorem

| Control | Audit |
|---|---|
| Actual rough lowest positive eigenspace | Q_mu=Q-mu mass is nonnegative and obeys (2). Its whole kernel therefore has the SAME compact complex division, real-zero generator, physical de Branges carrier and codimension-one multiplication domain. It retains the proved positive sharp/log coefficient. The actual unshifted divisor pairing on this space equals mu times physical mass, not zero. All hypotheses of the structural attachment hold; the shift is not silently removed. |
| Artificial compact-good-row logarithmic control | Generic rows need not obey (2), so no automatic actual division theorem is transferred to them. Their positive logarithmic slope remains a control against a generic compact-row sign theorem. The polynomial example above separately audits the proposed RKHS sign step. |
| Fixed finite actual restoration | A fixed finite alteration of (6) is O(1), hence o(1) after division by log T. The complete form is used in (2)-(4); source deletion does not authorize retaining those identities for a changed form. |
| Two-row comparison contact | Its auxiliary rows must be included in derivative integration by parts and generally do not satisfy (2). Its null vectors are not made actual null by this classification. No endpoint exclusion is inferred. |

For the physical ONB, complete signed source/native equality gives the entire unweighted sampling Gram equal to ZERO on K. For K^mu it equals mu I. More strongly, against EVERY canonical test v, the unshifted full mixed pairing is zero in the first case and mu<h,v>_L2 in the second. These are different equations and are retained as such. The physical de Branges norm and axioms do not encode this zero-versus-mu divisor sampling identity, and no outside theorem checked here forces its weighted sharp head to have a bounded return.

What shortened is the INTERNAL graph: actual complex division, common-factor zero location and exact finite de Branges membership are proved, rather than left as attachment hypotheses. The final GLOBAL exclusion arrow does not shorten:

    actual unshifted FULL source-range nullity
      -> bounded/sublogarithmic sharp subsequence
      -> contradiction with the positive sharp/log limit.

The first arrow remains UNPROVED. The smallest remaining theorem is still signed actual sharp-head arithmetic, now expressed exactly by (6)-(7), not a generic sign property of a reproducing kernel. No actual bounded-return or oscillation mechanism was found. There is no r<=2, terminal-trace vanishing, actual common-source zero, RH, same-vector transport, F4 or FULL TRANSPORT CLOSED claim.

## Custody and validation

Pinned analytic inputs at recovered live head:

- POLE_GREEN_NULL_ATTACHMENT_20261007: bc08f1d10446088871c490815d3e833b46b0c293.
- KERNEL_DERIVATIVE_CHAIN_20261007: e124b8a31a00df61908ce71cedd4ab7f83a14c76.
- SHARP_ARITHMETIC_FRAMEWORK_AUDIT_20261007: a2607dee10e2aa834456ea363ea56ec4e9b5d76f.
- ACTUAL_SHARP_LOG_LIMIT_20261007: 310fbfd874f2fb6a0cda70f38d50fb656c26029e.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.

Primary outside input is ONLY the three-axiom framework in Belov Section 3.1. This note derives all actual membership hypotheses directly; it does not import Belov's complementability conclusion, the later no-common-real-zero assumption, or any purported proof of RH. The companion exact rational-complex checker passes 1,266 assertions, including 48 polynomial division cases, and records pole skew algebra, complex zero-flip energy/mass identities and the positive-diagonal/negative-reflected-kernel control. Analytic support/domain and full-null arguments are documented above, not certified by sampled finite checks. Lean is unavailable in the partial mirror and no axiom or Lean proof is added. Historical notes/certificates and the separate aperture lane remain unchanged except for additive cursor entries.
