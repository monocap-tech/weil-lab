# RPB108 RC2 — response deficit and the global transfer boundary

2026-10-10. Independent consolidation investigation.
Branch: research/rpb108-route-consolidation.
Base: RC1, 19b4dcc3f572b9044458895a58848ccbab0cba14.

## Scope correction and recovery

The user's clarification is that this investigation does not follow or direct
the other branches, but is still recorded in the repo. RC1's allocation table is
a proposed organizational interpretation, not an instruction to pause or
reactivate independently running threads. This additive clarification leaves
RC1 and all other historical wording intact. Only this new branch is written.

Read-only recovered inputs:

| Route | Observed head | Result |
| --- | --- | --- |
| Coupled | 19b4dcc3f572b9044458895a58848ccbab0cba14 | RC1 metadata; CC119 certificate at 5df347d3808ac3282864a657b7380e0f54bf4daa |
| DNE | b09d6bb5cc760169e9533c4b1fc728405d747fdf | DNE53 complete even56 plus inherited CC117 odd56; whole a=53/50; common physical guard 1e-39 |
| Native | 048e58e0ac01de518513aa6c18669510fe09c41d | NF62 lifts both frozen targets; an odd residual rejects its sufficient lower matrix; no whole gate on that route |
| Global | 60af21664204303fe9d90c89b18930d213da33a4 | Metadata head; NF71 remains mathematical research head |

DNE53 stored source and response audits were read: PASS with 40,801 and 19,825
exact checks respectively. Its source-only whole-aperture-false field precedes
the response gate; the final response audit is whole-aperture-positive. These
are stored reports, not freshly rerun source integrations here. DNE53 therefore
supersedes RC1's provisional description of pending DNE53 work.

CC119 and DNE53 use different finite high response frames but the same basic
comparison mechanism. NF62's failed lower matrix does not contradict their
positive original-form certificates.

## Definitions before use

Work at one fixed aperture. Let E be a finite-dimensional retained coefficient
space, F a physical high Hilbert space, and C a self-adjoint high operator with
C >= k I for k>0. Let B:E -> F be the complete original retained-to-high source
map and Q a Hermitian retained matrix. The original block form is

    q(u,v) = u*Q u + 2 Re <B u,v> + ||C^(1/2) v||^2,
    u in E, v in D(C^(1/2)).

This is a form statement; no bounded operator representation of the whole
logarithmic Weil form is assumed. B's existence in physical F and the original
domain attachments are hypotheses, not conclusions of finite matrix algebra.

Let Y:R^r -> D(C) be a finite high trial frame, with complex coefficients
allowed in the Hermitian version. Define the complete paid data

    G = B*B,
    T = Y*C Y,
    U = (CY)*(CY),
    N = U/k - T,
    W = B*(C-kI)Y.

All mixed entries are retained. Define the true retained Schur form S and the
fixed-response comparison L_H for an r-by-dim(E) coefficient matrix H:

    S = Q - B*C^(-1)B,
    L_H = Q - G/k + (WH + H*W* - H*N H)/k^2.

Define the bounded positive inverse-deficit operator, response vectors, and
response residual:

    Delta = I/k - C^(-1) >= 0,
    V = Delta^(1/2) C Y,
    t = Delta^(1/2) B.

If N>0, let P_V be the orthogonal projection onto ran(V) and set

    R_Y = t*(I-P_V)t >= 0,
    H_opt = N^(-1)W*.

R_Y is the unresolved inverse-deficit energy of this trial frame. It is not
ordinary source energy, and it is not automatically the historically defined
aperture-shell leakage. Identifying it with a historical leakage object would
require an explicit additional attachment.

## Proposition 1: exact response-deficit decomposition

Under these hypotheses, N=V*V and t*V=W/k. Therefore

    S = L_H + R_Y
        + (H-H_opt)*N(H-H_opt)/k^2.                 (1)

Proof: C Delta C=C(C-kI)/k on trial vectors in D(C), giving N=V*V.
Also Delta C=(C-kI)/k, giving t*V=W/k. Orthogonal projection yields

    t*P_V t = W N^(-1) W*/k^2,
    t*t = W N^(-1) W*/k^2 + R_Y.

Finally S=Q-G/k+t*t. Completing the finite square gives (1).

In particular L_H <= S for every H. Even if N is singular, the fixed-response
inequality still follows directly from

    S-L_H = (t - V H/k)*(t - V H/k) >= 0.           (2)

The positive-denominator hypothesis is needed for the optimized formulas, not
for (2). No true infinite inverse needs to be evaluated to certify L_H>0 from
the paid Q,G,N,W,H data. The inverse appears only in this explanatory proof.

At an actual retained null u with S u=0, (1) gives

    u*L_H u = -||(I-P_V)t u||^2
              -||V(H-H_opt)u||^2/k^2 <= 0.         (3)

Thus coefficient error and incomplete response coverage explain why a
sufficient lower comparison can fail. Removing both errors makes the comparison
exact; it does not make a genuine null positive.

## Proposition 2: DNE and CC are the same fixed-response family after scaling

In DNE53 notation, its response denominator is

    W_DNE = U-kT = kN,
    E_DNE = W,

and its paid budget is

    D_J = kQ-G + WJ + J*W* - J*(kN)J.

Setting H=kJ gives D_J/k=L_H exactly. This is a symbolic equality when Q,G,T,U
and the physical frame describe the same exact objects. It does not identify
different published frames, outward interval widths, or their runtime costs.

CC119's union frame and DNE53's six-trial frame can both succeed without either
criterion being universally stronger. Their strict improvements over older
saved bounds are improvements in paid correlated frames and coefficients.
A comparison of independent jobs is not a like-for-like cost benchmark.

## Proposition 3: finite response completeness alone is not global exclusion

There is even an existential exact finite frame at each fixed operator:
take trial columns Y=C^(-1)B and discard dependent columns of V. These columns
are in D(C), since C has a bounded inverse. Then ran(t) is contained in ran(V),
R_Y=0, and an optimized response recovers S exactly. Empty response rank is
allowed when t=0.

This existence result is not a computable construction from the paid source
data: choosing these Y requires the inverse response whose evaluation the
certificate method avoids. It explains why the key remaining issue cannot be
merely the existence of some finite response frame.

An explicit crossing control makes the distinction decisive. Let E=R,
let F=l2(N_0), and take

    k=1,
    C e_j = (2+log(1+j)) e_j,
    B u = u e_0,
    Q_a = 5/2-a,
    Y=e_0.

C is an unbounded logarithmic diagonal operator with a fixed positive high
floor. The full form is defined on its genuine form domain. Every retained
response is in the e_0 direction, so

    G=1, T=2, U=4, N=2, W=1, H_opt=1/2,
    R_Y=0,
    L_Hopt(a)=S(a)=2-a.

The original full block form is positive for a<2, has the genuine null
(u,v)=(1,-e_0/2) at a=2, and is indefinite for a>2. In particular it is
strictly positive at 53/50, with exact response coverage throughout. The
remaining diagonal high directions stay positive. Smooth source/retained data,
a uniform high floor, and even exact response computation permit first contact.

This is an abstract control, not an operator with the literal original Weil
source identities, aperture filtration, or singular endpoint trace. It refutes
a transfer theorem based only on the extracted block/response hypotheses. It
does not refute a theorem using extra arithmetic identities specific to zeta.

A separate positive-level control uses the invariant two-plane matrix
[[2,1],[1,2]]. The vector (1,-1) has eigenvalue 1, positive energy 2, and fails
the unshifted null equations. Its shifted equation must retain the mass term.
No eigenlevel is silently changed to zero.

## What an actual global transfer must add

A cap-uniform response certificate is one sufficient formulation, not a newly
proved minimal arithmetic estimate. For every finite cap A, it would require
complete original charts and sources at every a in [53/50,A], with

    k_a >= k_A > 0,
    ||C_a^(-1)B_a|| <= d_A < infinity,
    L_Ha >= s_A I with s_A>0,

and uniform chart-to-physical bounds when retained coordinates are not
orthonormal. Trial dimensions and frames may vary; their identities, mixed
entries, and domain attachments must remain explicit.

With orthonormal retained coordinates, completing the original block square
then gives a physical gap at least

    min(s_A/(2*(1+d_A^2)), k_A/2) > 0.

Indeed q >= s_A||u||^2+k_A||v+C_a^(-1)B_a u||^2, while
||u||^2+||v||^2 <= 2(1+d_A^2)||u||^2
                    +2||v+C_a^(-1)B_a u||^2.

No such cap-uniform positive retained margin is supplied by CC119 or DNE53.
Requiring it without deriving it simply restates a substantial coercivity
obligation. Alternatively, a genuinely arithmetic theorem could directly
exclude every first-contact null. It must add information that rules out the
crossing control at the level of the actual source equations.

The concrete next task here is to match R_Y and the response-frame defects to
the historical near-critical source-shell objects, preserving the canonical
domain and actual unshifted null equation. Only after that attachment can a
candidate old-gap-independent arithmetic correlation estimate be stated and
tested as sufficient. No numerical “minimal correlation constant” is invented
from the fixed-aperture certificates.

## Fresh validation and non-claims

scripts/validate_rpb108_rc2_response_controls.py runs 86 exact rational checks:
nonzero unresolved defects, optimized and nonoptimized coefficients, positive,
null and negative Schur values, the fully covered crossing, and the positive
eigenlevel control. PASS. The logarithmic infinite extension is justified by
the displayed diagonal construction, not by those finite arithmetic checks.

Fresh checks validate the abstract identities and countercontrols only. They
do not rerun CC119, DNE53 or NF62; no original source integration, arithmetic
leakage estimate, universal positivity, RH/F4 theorem, or Lean proof is newly
certified. Other branch refs are untouched.
