# RPB108 RC4 — native transport audit and weaker endpoint target

2026-10-10. Independent consolidation branch.
Parent: f5f8609451cbf82e5c7de4897eb06d2a2a56af3a (RC3).
Other branches remain read-only.

## Correction to the consolidated minimum target

RC3 gave a sufficient strict relative-budget test for finite-step continuation.
Its final wording emphasized a strict reserve and low-output protection as the
next global requirement. That is stronger than necessary for the DIFFERENT
first-contact endpoint route already established in CC29.

The source audit recovers the following inherited endpoint sufficiency:
on every finite cap, a bounded vanishing modulus of the complete critical
covariance, with a fixed critical band and positive cap-only aperture step,
excludes first contact. It requires neither a coefficient below one nor a
low-output budget. Those remain requirements of the separate finite-step
product proof. Historical RC3 is preserved; this additive statement corrects
the consolidated minimum obligation.

Also, CC31 already supplies a cap-uniform finite critical-rank bound from
the actual Garding and source-observability estimates. That rank theorem is
an inherited analytic dependency, not a new arithmetic estimate or a fixed
112-direction numerical certificate.

## Recovered source custody

Read at pinned CC119 commit 5df347d3808ac3282864a657b7380e0f54bf4daa:

| Report | Git blob |
| --- | --- |
| notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_FLUX_LIMIT_CC29_20261008.md | 1d139126c805a96fa6bc92c0311fa89111e5f42f |
| notes/REFLECTED_PACKET_BRIDGE_108_UNIFORM_CRITICAL_RANK_CC31_20261008.md | 87b4d82a2e970b5e16ccdc89376122b0a95fd350 |
| notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_REMAINDER_FORCING_CC33_20261008.md | e4476bc892a9275abde387705bed8cb561e4a904 |

CC119's fixed-aperture report and CC20's source definitions were also read.
The assertions below retain those reports' analytic/domain hypotheses. No
original integrations or historical audits were rerun.

## Definitions and actual native transport

Let D_t be the canonical logarithmic supported Hilbert domain, with its
inner product representing E_log. On a fixed cap B, let i_t:D_t->L2[-B,B]
be physical inclusion. The inherited actual native identity is

    Q=E_log+<i_t h,R_B i_t f>,
    C_t=i_t*R_B i_t,
    canonical form operator of Q = I+C_t.

R_B is ONLY the bounded physical remainder: the bounded digamma-minus-log
symbol, all active prime-power shifts in both orientations, and both signed
pole terms. It is not a bounded physical representation of the full logarithmic
Weil form. No physical operator-domain assumption for a rough h is introduced.

Let M_t=P_t*P_t be the complete POSITIVE source metric in D_t. For a normalized
old source-critical lift h_i, use lambda_i>0, delta_i=1-lambda_i>0,
||P h_i||=1, and let Pi be the CANONICAL orthogonal projection onto D_s.
Define the forced dual Riesz vector j_i and outward native forcing q_i by

    j_i=(I+C_t-delta_i M_t)h_i,
    q_i=(I-Pi)C_t h_i.

The actual old generalized equation annihilates the whole D_s, so

    j_i=q_i-delta_i(I-Pi)M_t h_i.                         (1)

CC33 supplies the positive-inverse correction estimate

    | ||M_t^(-1/2)j_i||-||M_t^(-1/2)q_i|| |
       <= K_B delta_i, K_B=U_B/c_B.                     (2)

This is the available native-to-forced transport. The canonical projection
Pi is neither a strip cutoff nor the positive-source shell projection.
Every prime, pole and archimedean term acts before this same projection.

The native physical source archives can help compute signed pairings once
the exact h_i and projection are attached. They do not identify those h_i
or M_t simply by recording many physical retained/high vectors.

## Smaller arithmetic obligation for the endpoint route

Define a bounded nonnegative modulus omega_B with omega_B(x)->0 as x->0+,
a fixed band eta_B<1, a positive step h_B, and a finite b_B. All must be
cap-only, independent of the old signed gap and target positivity.
Let d_B be the inherited CC31 critical-rank upper bound.

One sufficient ACTUAL scalar native target is

    ||M_t^(-1/2)q_i||^2
       <= b_B lambda_i omega_B(delta_i)                  (3)

for every actual source-critical basis row in that fixed band and EVERY
old-positive s and admissible t with

    s<t<=min(s+h_B,B).

No numerical b_B, modulus, or such estimate is supplied here.

Writing lambda_min=1-eta_B>0, (2) gives

    ||M_t^(-1/2)j_i||^2
       <= 2 b_B lambda_i omega_B(delta_i)
          +2 K_B^2 delta_i^2
       <= lambda_i [2b_B omega_B(delta_i)
                     +(2K_B^2/lambda_min)delta_i^2].     (4)

The bracket is a bounded vanishing modulus. CC31's full Gram
Cauchy--Schwarz argument, with rank at most d_B, then yields

    L_st L_st*
       <= d_B [2b_B omega_B(Gcrit)
                 +(2K_B^2/lambda_min)Gcrit^2].            (5)

All mixed output correlations remain in this Loewner bound. They are paid
through a genuine full-row estimate, not deleted or treated as independent.

By CC29's inherited attained-contact and strict-enlargement framework, (5)
on every finite cap excludes first contact: near a hypothetical contact,
the old critical defect goes to zero but incoming covariance into one fixed
strict enlargement remains positive. The vanishing right side contradicts
that positive flux. No low-output subtraction or strict coefficient reserve
is required for this contradiction.

Any positive power omega(x)=x^alpha is sufficient in this endpoint route.
For 0<alpha<=2, the correction x^2 can be absorbed in a cap multiple of
x^alpha. For alpha>2, the unconditional transported modulus is
x^alpha+x^2, which still vanishes and remains endpoint-sufficient. RC3's
linear-defect normalization is therefore not the only viable global target.

This recovers and consolidates CC29/CC31/CC33; it is not a new proof of (3).
The inherited theorem package retains its original analytic and Lean status.

## What RC3's finite trial test becomes for this route

For whole forced rows J and canonical trials X, RC3 gives

    J M_t^(-1)J* <= C_X A_X^(-1)C_X*+F_X*F_X/m,

where A_X=X*M_t X, C_X=JX, F_X=J*-M_t X A_X^(-1)C_X*,
and M_t>=m I. A sufficient endpoint test can bound this upper matrix by

    C_B Lambda omega_B(Gcrit),                           (6)

with no requirement C_B<1. If omega vanishes at positive arguments,
the corresponding exact covariance row must vanish; do not divide by a
zero modulus. Direct Loewner comparison avoids such division.

For native q_i one can analogously project q_i onto a whole positive-metric
trial frame and pay its full dual residual, then use (4). This does not
make a selected finite covariance a whole-domain upper bound. The actual
unresolved error must vanish with the old defect, at some rate; a constant
error bar fails both the linear and weaker endpoint tests.

Old-only trials give JX=0 exactly because J annihilates D_s. Consequently
a zero old-only trial covariance carries no information about the outgoing
whole residual. Outgoing tests and whole dual-error control are essential.

## Signed physical data do not identify the positive source metric

This limitation can be proved with complete signed form data, not merely
with a finite prefix. Fix the same original Hermitian form on R^2,

    Q=[[1/4,-1/4],[-1/4,1]].

It is strictly positive, with physical Schur value 3/16. For each of
(m,n)=(1,2),(2,3),(4,5), take

    M=diag(m,n), P*P=M, N*N=M-Q.

M-Q is positive definite in all three cases, so these are legitimate complete
source decompositions of EXACTLY THE SAME signed Q. Every physical form
pairing and physical operator action is identical.

With old domain span(e0), however,

    delta=(1/4)/m, lambda=1-delta,
    normalized old lift h=e0/sqrt(m),
    J=(0,-1/(4sqrt(m))),
    J M^(-1)J*=1/(16mn).

The critical weighted incoming cost is

    1/(16mn lambda delta)=1/(4n lambda),

and the full shell cost, including low output, is

    1-1/n+1/(4n)=1-3/(4n).

These source defects, critical costs, and full budgets differ across the
three models, while all signed physical data stay unchanged. Each whole
cost remains below one, consistent with the same positive Q.

Equivalently, adding the same bounded channel to P and N changes the
positive metric while preserving Q=P*P-N*N. The actual normalized zeta
dictionary is fixed and DOES NOT authorize such an addition. Thus this
is a precise information-limit control: signed native/form certificates
alone cannot reconstruct that dictionary's M, generalized eigenvectors,
or forced-row normalization. It is not a countermodel to the fully
specified original Weil identities.

No impossibility of a transport exploiting the actual dictionary is claimed.
A successful transport must retain the separate positive-source metric;
equality of signed form data is insufficient.

## Consolidated next gate and validation

The remaining native endpoint target is (3), with the actual generalized
h_i and the whole positive inverse. There are two concrete approaches:
attach those source-critical lifts to an evaluable canonical metric and
whole residual computation, or prove an actual arithmetic outward-forcing
bound uniformly over all such lifts. Neither is completed by the current
fixed-aperture response archives.

The freshly run script scripts/validate_rpb108_rc4_metric_transport_controls.py
passes 77 exact rational checks: legitimate nonidentity source metrics with
identical signed form, different critical normalization/budgets, zero
old-only pairing despite positive whole residual, and squared defect
correction algebra for weaker and stronger powers.

The finite tests do not prove CC29's endpoint theorem or reconstruct actual
zeta source-critical lifts. No actual modulus, source metric inverse,
new aperture, RH/F4 theorem or Lean closure is newly certified. CC119 and
DNE53 whole 1.06 positivity remain intact. Only this independent branch
is written; other routes and historical wording remain unchanged.
