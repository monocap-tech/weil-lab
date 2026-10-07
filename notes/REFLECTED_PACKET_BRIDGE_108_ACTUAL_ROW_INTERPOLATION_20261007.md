# RPB108: explicit entire/source interpolation with r actual critical rows

2026-10-07. Recovered head 1722a74ad3f4b44580641156a4c2ad8d92eb3180. Definitions: [actual-row interpolation](../docs/TERMINOLOGY_RPB108_ACTUAL_ROW_INTERPOLATION.md). Conditional on a hypothetical nonzero actual nonnegative contact kernel. Analytic, not Lean-certified.

## Result

The original physical and complete zeta source graph can now be reconstructed explicitly from the auxiliary real-node energy samples PLUS r actual critical-line source rows, where r=dim K. For every supported canonical f,

    F_f(z)=Phi(z) [sum_(i=1)^r F_f(x_i)L_i(z)/Phi(x_i)
                +P_X(z) sum_(Phi(t)=0)
                  F_f(t)/[Phi'(t)P_X(t)(z-t)]].                  (1)

All removable values are interpreted by entire continuation. The series has a canonical-domain physical realization and converges in the COMPLETE actual source norm after that realization. It is not just a formal meromorphic interpolation series or a finite-height identity.

The abstract physical-orthogonal kernel correction from NF46-47 is replaced by an explicit polynomial lift using r independent ORIGINAL source observations. Their existence was already supported by the published distinct-critical sampling theorem; the new result is the corrected entire interpolation formula and its domain/source convergence.

This closes a concrete model-to-source reconstruction interface. It does not prove the finite kernel polynomial vanishes. The actual positive eigenmode has the same interpolation lift at level mu, with its signed full-source equation retaining mu physical mass. Signed sharp-head arithmetic and F4 remain open.

## 1. Choose independent original rows without counting multiplicity copies

Phi is a nonzero compact-support Fourier transform of exponential type. The Jensen bound already proved in GLOBAL_POSITIVE_KERNEL gives O(T) zeros of Phi in a height disk. The pinned actual critical sampling input gives at least c T log T distinct simple critical-line ordinates for large T. Hence arbitrarily many such ordinates are NOT zeros of Phi, and r distinct choices x_i with Phi(x_i)!=0 exist.

No numerical x_i or conditioning floor is asserted. The theorem is an exact conditional existence/construction, not a computed actual packet certificate. Simple actual points supply independent rows; multiplicity copies at an equal ordinate are not used.

At an actual critical point the registered positive source profile is F_f(x_i), and its negative profile is zero. If an implemented coordinate also includes a nonzero positive normalization/copy factor alpha_i, use b_i(f)=p_i(f)/alpha_i. Every subsequent F_f(x_i) means this exact raw Fourier value; normalizations are not discarded from the actual source dictionary.

## 2. Exact finite polynomial correction in the physical kernel

Set P_X(z)=product_i(z-x_i) and L_i(z)=P_X(z)/[(z-x_i)P_X'(x_i)]. The actual kernel's entire profiles are exactly Phi times polynomials of degree at most r-1. Consequently each

    F_Hi(z)=Phi(z)L_i(z)/Phi(x_i)

comes from a unique physical H_i in K. The raw selected actual rows are F_Hi(x_j)=delta_(i,j). Therefore

    C_X f=sum_i F_f(x_i)H_i,
    C_X|_K=I,    C_X^2=C_X.                        (2)

Every selected evaluation is bounded on the compact physical L2 carrier. The finite target lies in D_a, so C_X is bounded on D_a and in physical mass. It is generally NOT the physical orthogonal P_K. Its complementary gauge R_X=I-C_X satisfies

    F_(R_X f)(x_i)=0,
    Q(R_X f,R_X g)=Q(f,g).

Because R_X f=(I-C_X)Pi f, the already proved bounded physical representative Pi from NF46 shows that R_X is a bounded realization of the completed energy quotient into D_a. Nothing requires a conditioning estimate uniform in a or r.

## 3. Actual-row Cauchy correction and domain convergence

For a generator node t, none of the x_i equals t. The real-zero division vector has F_ut(z)=i Phi(z)/(z-t). Apply (2):

    F_(R_X u_t)(z)=i Phi(z) A_(X,t)(z),
    A_(X,t)(z)=1/(z-t)-sum_i L_i(z)/(x_i-t)
             =P_X(z)/[P_X(t)(z-t)].               (3)

The last rational identity follows by matching its pole residue at z=t and its r zeros at z=x_i; equivalently multiply by (z-t) and use polynomial interpolation. Its signs are fixed, and the nonzero denominators P_X(t), Phi(x_i) and Phi'(t) are justified by the two disjoint node sets and the generator's simple zeros.

The full energy basis from NF47 supplies

    [f]=-i sum_t F_f(t)[u_t]/Phi'(t) in H_Q.

The bounded actual-row gauge now gives

    R_X f=-i sum_t F_f(t)R_X u_t/Phi'(t) in D_a,
    f=C_X f-i sum_t F_f(t)R_X u_t/Phi'(t).         (4)

Fourier evaluation and all its fixed-order derivatives are bounded on compact spectral sets for supported physical vectors. Thus (4) gives locally uniform entire-function convergence, including derivatives and all collision values. Taking profiles in (4) yields exactly (1).

The quotient in the individual rational term of (1) is canceled by Phi at z=t. At a selected actual point x_i, P_X(x_i)=0 and every corrected physical cardinal vector has zero row there. These observations concern the complete physical series in (4); no unjustified exchange of separately divergent Cauchy sums is used.

## 4. Complete actual source-range interpolation

Apply bounded complete actual analysis Gamma to (4):

    Gamma(f)=sum_i F_f(x_i)Gamma(H_i)
                 -i sum_t F_f(t)Gamma(R_X u_t)/Phi'(t),           (5)

with convergence in the full source norm. All positive/negative channels, reflected points, actual divisor copies and normalization weights are retained. Source heights are not truncated in this convergence assertion.

The second term has zero values on the selected original critical rows; the first term restores precisely those rows. Thus the auxiliary sampling coordinates and these r actual observations reconstruct the original supported physical/source vector injectively. If all auxiliary samples and all selected actual rows vanish, (4) gives f=0.

This is a lawful explicit source lift, not the claim that arbitrary independent auxiliary/source values are always admissible. For supported physical input the two data sets obey (1). The energy sequence alone reconstructs only a class modulo K. A compatible kernel correction is carried by the actual row polynomial in (1), and its original signed source pairings must still be checked at the relevant spectral level.

## 5. Terminal trace readout on the actual kernel

For h in K all auxiliary samples vanish. Formula (1) reduces to

    F_h(z)/Phi(z)=sum_i F_h(x_i)L_i(z)/Phi(x_i).     (6)

Let g_*=D^(r-1)h_* and kappa_*=kappa_R(g_*)!=0. Since F_(D^j h_*)=(-iz)^j Phi(z), and all earlier derivatives have zero endpoint trace, the highest polynomial coefficient in (6) gives

    kappa_R(h)=kappa_*/(-i)^(r-1)
                  sum_i F_h(x_i)/[Phi(x_i)P_X'(x_i)].            (7)

This is a normalization-audited readout of the already proved terminal functional from actual distinct source rows. It is not offered as a new endpoint-exclusion criterion. The previous signed sharp/log theorem remains the arithmetic target. Nothing here forces the scalar in (7) to vanish; selected original critical rows are observable rather than automatically zero on K.

In the basis H_i, the complete actual signed source Gram is zero at unshifted contact:

    <Gamma(H_i),J Gamma(H_j)>=0 for every i,j.

Each selected critical row is positive, and these rows form an invertible coordinate system. Their contribution must therefore be canceled by the REST of the complete signed source graph. This is the exact actual compatibility to retain; zero auxiliary samples are not pointwise zero actual source coordinates.

## 6. Positive-eigenmode and historical controls

Use the same construction for the actual lowest positive eigenspace of Q at level mu. Its generator has the same simple-real-zero and completeness structure, so r actual critical rows again give (1)-(7) for its Q_mu energy model. Its original full signed-source Gram in the new kernel basis is

    <Gamma(H_i^mu),J Gamma(H_j^mu)>
                              =mu <H_i^mu,H_j^mu>_L2,

not zero. This keeps the mass residual explicit and identifies the equation which a successful arithmetic argument must distinguish. The control still has its proved positive sharp/log coefficient.

| Control | Exact audit |
|---|---|
| Actual rough positive eigenmode | Same source interpolation; signed basis Gram retains mu mass. |
| Artificial compact-good-row logarithmic control | No automatic actual auxiliary sampling/interpolation theorem; its logarithmic slope still rejects generic row-count or compactness sign arguments. |
| Fixed finite source restoration | The restored polynomial here changes the physical representative, not the arithmetic form by deleting a finite source set. Historical O(1) finite-deletion invariance of the sharp coefficient remains unchanged. |
| Two-row comparison contact | Auxiliary comparison rows are not substituted for actual x_i; no actual derivative-skew or interpolation transfer is assumed. |
| Equal-ordinate multiplicity copies | Not independent observations; the chosen x_i are genuinely distinct actual simple critical ordinates. |

The internal graph advances from an abstract kernel gauge to an explicit actual-row source interpolation. The row polynomial remains part of the original graph and can carry nonzero terminal trace. There is no bounded-return mechanism yet, and the final unshifted actual-nullity -> bounded/sublogarithmic sharp subsequence implication remains unproved. Endpoint exclusion, F4, full transport and Lean closure remain open. Aperture-one positivity and historical custody are preserved.

## Validation and provenance

The finite checker validates polynomial/Lagrange correction, disjoint-node denominators, critical-row cardinality, actual normalization factors, terminal leading coefficient and retained mass residual. It does not compute actual zeta nodes or certify analytic convergence/trace arguments. Actual finite-row existence uses the already pinned GLOBAL_POSITIVE_KERNEL theorem and its distinct-critical arithmetic inputs; no new density claim is imported. All actual inputs are pinned in the companion manifest. Historical definitions are preserved; these definitions are additive.
