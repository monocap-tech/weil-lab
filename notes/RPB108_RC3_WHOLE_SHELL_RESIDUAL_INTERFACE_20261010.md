# RPB108 RC3 — whole source-shell covariance versus physical response deficit

2026-10-10. Independent branch research/rpb108-route-consolidation.
Parent RC2: 10c6a777f913d88695bd71d5bf8e7b235d601c6a.
Other branches are read-only. No allocation or restart instruction is issued.

## Recovered actual definitions and custody

Historical source definitions and proofs were read at CC119 commit
5df347d3808ac3282864a657b7380e0f54bf4daa:

- docs/TERMINOLOGY_RPB108_SHELL_LEAKAGE.md
  (blob 6ba17782df121e506f4d6fa9793403f57057c140);
- docs/TERMINOLOGY_RPB108_FORCED_SOURCE.md
  (blob d9419bcff18bfd61d8d7f14d8591322ce8e7b4b3);
- notes/REFLECTED_PACKET_BRIDGE_108_SHELL_LEAKAGE_CC19_20261008.md
  (blob 25c6e2736cc4e0fdfec8d8832c3f6e24827d4d06);
- notes/REFLECTED_PACKET_BRIDGE_108_FORCED_SOURCE_CC20_20261008.md
  (blob da2dab5958dd65381bca285c7ff9082d571e6dd8).

These are inherited analytic statements and their hypotheses. Reading them does
not newly certify their original source/domain attachments or Lean equivalents.

Fix a finite aperture cap and the complete original normalized P,N on its
canonical supported domain. Historical normalization is Q=P*P-N*N, retaining
all divisor multiplicities and mixed slots. Let

    V_a=P(D_a), T_a(Ph)=Nh, A_a=T_a T_a*,
    W_st=V_t intersect V_s perpendicular,
    K_st=T_t|W_st, D_s=I-A_s.

The shell is orthogonal in the positive SOURCE metric. It is not a physical
outer strip. For original-positive old s, the historical identities give

    A_t=A_s+K_st K_st*,
    target strict positivity iff ||K_st* D_s^(-1) K_st||<1.       (1)

All original-positive/strict-gain correspondences and closed-range hypotheses
in this assertion remain those of CC19; a target-positive premise is not used
to estimate the right side.

Choose a protected critical output eigenbasis y_i, with lambda_i>0 and
delta_i=1-lambda_i>0. Write Lambda=diag(lambda_i), Gcrit=diag(delta_i).
The old physical lifts h_i are generalized eigenvectors in the positive-source
metric, not ordinary physical eigenvectors. They satisfy

    Q(h_i,f)=delta_i <P h_i,P f> for every f in D_s.

For f in the whole new domain D_t, define

    J_i(f)=Q(h_i,f)-delta_i <P h_i,P f>,
    M_t=P_t*P_t.

Each J_i annihilates the entire old domain. CC20 supplies the exact whole-shell
critical covariance, for L=Ecrit K_st:

    L L*=Lambda^(-1/2) J M_t^(-1) J* Lambda^(-1/2).               (2)

M_t is a bounded positive operator in the canonical domain Hilbert norm, with
M_t>=m I, m=c_cap^2>0, under the inherited observability hypothesis.
Its inverse is protected independently of the signed old defect; the
subsequent critical defect weighting is still required.

Define Dcrit=Lambda^(1/2) Gcrit Lambda^(1/2).
In the chosen eigenbasis this is diag(lambda_i delta_i). The exact separate
critical gate is

    J M_t^(-1) J* <= q Dcrit,
    B_low<=ell I, ell+q<1.                                      (3)

This is sharper than bounding each row separately. It is sufficient for (1);
separate scalar low/critical budgets need not be necessary.

## Why RC2's deficit is not historical shell leakage

RC2's R_Y is the uncovered inverse-deficit energy of a finite PHYSICAL high
trial frame for one fixed-aperture Schur comparison. The historical left side
of (2) acts on generalized critical SOURCE outputs and takes a covariance over
the whole new canonical domain. The metrics, projections, domains and input
vectors differ. The symbol G in RC2 denotes a physical source Gram and is not
Gcrit. No equality R_Y=L L* or replacement of Dcrit by physical mass is valid
without an additional explicit attachment.

A single common source model demonstrates the distinction, rather than merely
using unrelated examples. Take P=I on R^2, N=(a,b), old domain span(e0), and
new domain R^2, with b=4/5 and 0<a<1. Then

    lambda=a^2, delta=1-a^2,
    K=b, J=(0,-ab), M=I,
    J M^(-1)J*/lambda=b^2,
    K*D_s^(-1)K=b^2/(1-a^2).

The same original signed form has physical blocks

    Qret=1-a^2, B=-ab, C=1-b^2=9/25.

Set physical k=C/2 and Y=1. This finite high frame exactly covers the inverse
deficit, so RC2's R_Y is ZERO. Its optimized comparison equals the true Schur
form,

    S=(1-a^2)(1-b^2/(1-a^2))/(1-b^2).

For a=1/2 the shell cost is below one; at a=3/5 it equals one and the original
form has a genuine null; at a=7/10 it exceeds one and the form is indefinite.
R_Y remains zero in all three cases. Thus exact fixed-aperture physical
response coverage does not estimate, or equal, the relative shell leakage.
This is an abstract exact source control, not the literal zeta dictionary.

## Whole-domain finite-trial upper interface for the historical covariance

The following definitions precede their new use. Let X:C^r -> D_t be any finite
canonical-domain trial map, and suppose A_X=X*M_t X>0. It need not be a physical
high frame. Define

    C_X=J X,
    Z_X=X A_X^(-1) C_X*,
    F_X=J* - M_t Z_X.

Adjoints here are with respect to the canonical D_t Hilbert norm. F_X is the
WHOLE canonical dual residual, including action outside the finite trial
space. It is not source-construction error or a omitted polynomial coordinate.

The exact identity is

    J M_t^(-1)J*
       = C_X A_X^(-1) C_X* + F_X* M_t^(-1) F_X.                 (4)

Proof: expand the second term, use X*M_t X=A_X and JX=C_X, and cancel the
two cross terms against one quadratic term. Equivalently this is the
orthogonal projection of M_t^(-1/2)J* onto ran(M_t^(1/2)X).
Every mixed output entry is retained.

The observability floor gives the whole-matrix enclosure

    C_X A_X^(-1) C_X*
       <= J M_t^(-1)J*
       <= C_X A_X^(-1) C_X* + F_X*F_X/m.                       (5)

Consequently the concrete sufficient critical acceptance test is

    C_X A_X^(-1) C_X* + F_X*F_X/m <= q Dcrit,
    B_low<=ell I, ell+q<1.                                    (6)

A certified sharper dual residual matrix can replace F_X*F_X/m.
Finite inverses in (4)-(6) can be enclosed or avoided using a fixed lift and
its fully paid residual; the whole positive inverse is not numerically
evaluated by (6).

In normalized coordinates, define

    T_X=Dcrit^(-1/2) C_X A_X^(-1) C_X* Dcrit^(-1/2),
    E_X=F_X Dcrit^(-1/2).

Then (6) becomes

    T_X + E_X*E_X/m <= q I.                                    (7)

The exact unresolved requirement is a defect-relative upper enclosure of the
combined dual residual, plus room for the measured finite covariance and
the low-output cost. Constants and admissible aperture steps must be cap-only
and independent of the old signed gap. A row norm needs suppression at the
square-root scale sqrt(lambda_i delta_i), with ALL mixed correlations paid;
a uniform bound before this normalization is insufficient. Square-root
scaling alone also does not supply the strict coefficient budget.

This is an acceptance interface, not a proof of the missing arithmetic
estimate. Unlike physical Schur positivity, where a lower bound can certify
positivity, small shell leakage requires an UPPER bound. Increasing a trial
space increases the measured lower covariance; a small measured finite
covariance is not evidence that the whole covariance is small.

The sharp failure control is M=I, J=(0,1), X=e0, Dcrit=d>0.
The finite covariance is zero for every d, while the true normalized covariance
and residual cost are both 1/d. Omitting F_X turns an unbounded cost into a
false zero certificate.

## Actual data obligations exposed by the interface

| Required object | Meaning | Available from the fixed-aperture response certificates alone? |
| --- | --- | --- |
| h_i, lambda_i, delta_i | Generalized old source-critical lifts and defects | No; retained physical packet vectors are not automatically these lifts |
| J on all D_t | Original forced dual rows, annihilating all D_s | Definition inherited; no whole-row numerical bound supplied |
| M_t and m | Complete positive source metric and independently protected cap floor | Qualitative observability inherited; effective bounds need authentication |
| A_X, C_X | Complete positive-metric trial Gram and signed forced pairings | Can be a finite computation once the actual lifts and trial map are attached |
| F_X*F_X | Whole dual residual covariance outside the trial space | Not the archived physical source error or RC2 R_Y |
| B_low, uniform steps | Compatible low-output reserve and non-stalling cap width | Not obtained from a single positive aperture |

No source-engine rerun is initiated to fill these objects by relabeling existing
physical columns. In particular CC119's 33 paid mixed physical correlations and
DNE53's 68-pair extension establish their fixed-aperture gates; their number does
not answer the universal source-shell obligation.

The original paired expansion in CC20 remains relevant: its leading difference
kernel coefficient tends to one as the critical defect tends to zero.
Partner reflection and old-domain annihilation do not supply the needed defect
factor on the new quotient. Equations (4)-(7) organize where an actual joint
arithmetic bound must enter; they do not create that bound.

## Scope, fresh checks, and next gate

The exact validator scripts/validate_rpb108_rc3_shell_residual_controls.py
passes 81 fresh rational checks: nonidentity positive metrics, mixed output
covariances, unequal critical normalization scales, exact dual residual
completion, one-sided upper bounds, a common-source genuine crossing, and the
omitted-residual failure. No actual zeta critical covariance is evaluated.
RC2's positive-eigenlevel mass control remains inherited; no shifted null is
identified with original nullity.

The all-cap exit still needs a strict relative budget rho_cap<1 and positive
cap-only step width for every old-positive shell. Repeated finite steps then
preserve positivity as in CC19. Neither (6) nor any fixed-aperture certificate
has supplied those constants.

Next substantive gate: identify an actual arithmetic relation that bounds the
normalized whole residual in (7), or the exact forced covariance in (3), together
with low-output protection. If using archived physical sources, first prove
their transport to the actual generalized source-critical lifts and canonical
dual rows. Until that transport or arithmetic estimate is supplied, repeating
conditional matrix algebra or refining already completed 1.06 source columns
does not advance the global theorem.

Whole positivity at 1.06 remains established on CC119 and DNE53 in their inherited
scopes. No new aperture, old-gap-independent arithmetic estimate, RH/F4, or Lean
closure is claimed. Historical files and other refs are untouched.
