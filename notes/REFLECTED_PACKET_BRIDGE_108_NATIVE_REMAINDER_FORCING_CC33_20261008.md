# RPB108 CC33: the leading logarithmic form cancels, leaving explicit native remainder forcing

Date: 2026-10-08 UTC. Parent: a5519501a69b61bf22b0aa177ac5d5d429f51e2d.
Definitions: [native remainder forcing](../docs/TERMINOLOGY_RPB108_NATIVE_REMAINDER_FORCING.md).
Scope: exact actual arithmetic numerator decomposition and controlled
defect correction. No arithmetic vanishing bound, new aperture or Lean proof.

## Result

For every exact source-normalized old critical lift, the forced row's
canonical leading identity part cancels upon projection outside the old
canonical domain. The row is

    j_i=q_i-delta_i (I-Pi^D_st)M_t h_i,
    q_i=(I-Pi^D_st)C_t h_i.                               (1)

The complete positive-inverse correction is bounded independently of
the old gap:

    | ||M_t^-1/2 j_i||-||M_t^-1/2 q_i|| |
       <=(U_B/c_B) delta_i.                              (2)

Here C_t is specified by the actual native archimedean remainder,
finite-cap prime powers and signed poles. Its coefficients do not acquire
an automatic delta_i factor. CC31's remaining endpoint arithmetic task
can therefore be placed on the native remainder forcing q_i, with the
entire positive inverse retained and an explicitly vanishing correction.

The mere boundedness or compactness of C_t does not establish this task.
Under hypothetical contact, CC32 forces one q_i to remain nonzero in
the positive-inverse norm as delta_i tends to zero. All such contact
statements are conditional, not actual zeta contact data.

## 1. The actual bounded physical remainder

Retain CC27's normalized native form and mathlib Fourier coordinate.
Let w(xi)=log(e+|xi|) and

    r_arch(xi)=Re psi(1/4+i*pi*xi)-log pi-w(xi).

Digamma asymptotics give Re psi(1/4+i*pi*xi)-log pi
=log|xi|+o(1) at large |xi|. Since w(xi)-log|xi| tends to zero,
r_arch tends to zero. At finite xi it is continuous: the vertical line
has positive real part and meets no digamma pole. Thus

    r_* = sup_real_xi |r_arch(xi)| < infinity.

Primary input read again: NIST DLMF 5.11.2,
https://dlmf.nist.gov/5.11.E2 . Its stated sector includes these vertical
rays. No effective numerical r_* is evaluated in this pass.

On physical L2[-B,B], use extension by zero outside the cap. The remainder
R_B consists of the compressed r_arch Fourier multiplier, minus EVERY
active prime-power shift pair with coefficient Lambda(n)/sqrt(n), plus
the two cross-paired pole moments. The sum includes all log n<=2B;
larger displacements have zero pairing on this cap. Threshold overlap
of measure zero causes no extra atom in this L2 form. This is the exact
finite-cap native identity, not a source-coordinate truncation.

Every translation is an L2 contraction after compression. Each physical
pole profile e^(+/-x/2) has squared norm 2 sinh B. Consequently a valid
cap-only norm bound is

    ||R_B|| <= r_* +2 sum_(log n<=2B) Lambda(n)/sqrt(n)
                       +4 sinh B = r_B.                 (3)

The two pole terms are cross-paired, not replaced by positive squares.
R_B is bounded selfadjoint. This represents ONLY Q-E_log; it does not
resurrect the rejected bounded physical L2 representation of the full
logarithmic form.

For physical inclusion i_t:D_t->L2[-B,B], t<=B, define

    C_t=i_t* R_B i_t.

Then the canonical form operator of Q on D_t is I+C_t, exactly. We have
||C_t||<=r_B because ||i_t||<=1. The inherited compact physical embedding
makes C_t compact, but no continuation inference is drawn from this.
This is not a statement that the complete negative-source analysis N
or its Gram is compact.

## 2. Canonical principal cancellation for the actual critical row

Choose an old source eigenvector y_i as in CC20--CC31, and normalize

    p_i=T_s* y_i/sqrt(lambda_i), h_i=P_s^-1 p_i,
    ||P h_i||=1, delta_i=1-lambda_i.

The exact generalized old equation is

    Q(h_i,k)=delta_i<Ph_i,Pk> for ALL k in D_s.

View h_i in D_t. With M_t=P_t*P_t and canonical adjoints, the Riesz
representer of its full forced dual row is

    j_i=(I+C_t-delta_i M_t)h_i,
    J_i(f)=<j_i,f>_D.

Let Pi^D_st be the CANONICAL orthogonal projection onto D_s in D_t.
Old criticality gives Pi^D_st j_i=0, while h_i belongs to D_s and
Pi^D_st h_i=h_i. Projecting the last displayed identity proves (1).

The cancellation is canonical: the leading logarithmic form is the
domain inner product, so its Riesz vector is the old vector h_i itself.
It does NOT say that its mixed kernel vanishes between disjoint physical
strips, or that Pi^D_st is a strip cutoff. The old positive-source shell
projection in CC20 is a different, M_t-orthogonal projection. No physical
operator-domain or H1 regularity of h_i is assumed.

All remainder terms still act before the same projection; no prime,
pole, archimedean or cross covariance term is deleted from j_i.

## 3. The positive-inverse correction genuinely has a defect factor

The whole metric obeys c_B^2 I<=M_t<=U_B^2 I. The complete positive
source of an old supported h_i is unchanged at t, so

    ||M_t^1/2 h_i||=||P_t h_i||=1,
    ||M_t h_i||<=U_B.

Pi^D_st is an orthogonal canonical projection. Therefore

    ||M_t^-1/2 (I-Pi^D_st)M_t h_i||<=U_B/c_B.

The norm triangle and reverse triangle give (2). In particular

    ||M_t^-1/2 j_i||^2
       <=2||M_t^-1/2 q_i||^2+2(U_B/c_B)^2 delta_i^2,       (4)

and the same inequality with j_i and q_i exchanged holds. M_t is not
replaced by I, and it need not commute with Pi^D_st.

Since lambda_i>=1-eta_B>0 in the fixed band, a scalar native estimate

    ||M_t^-1/2 q_i||^2<=b_B lambda_i omega_B(delta_i)        (5)

would supply CC31's scalar residual bound with the augmented modulus
omega_B(x)+x^2 and a finite cap constant. The converse holds with the
same type of augmentation. Both moduli vanish at zero. For powers
0<alpha<=2, x^2 is absorbed into a cap multiple of x^alpha on the fixed
band. For alpha>2, this argument alone does NOT preserve the stronger
power; cancellation with the correction might be needed.

Equation (5) is NOT established. This is an exact identification of its
arithmetic numerator, rather than an estimate of actual critical vectors.
The available absolute bound is only

    ||M_t^-1/2 q_i||<=r_B/c_B^2,

because ||h_i||_D<=1/c_B. This is O_B(1), not a vanishing modulus of
delta_i. Compactness cannot silently add that missing factor.

## 4. Hypothetical contact persists in the native remainder

Use the selected row from CC32, with delta_i<=C d_s and

    ||M_t^-1/2 j_i||>=k_0,
    k_0=sqrt((1-eta_B)gamma/(2d_B))>0.

Equation (2) then gives

    ||M_t^-1/2 q_i||>=k_0-(U_B/c_B)delta_i.

For sufficiently near-contact s it is at least k_0/2. Thus the isolated
native remainder forcing is precisely where a prospective scalar
arithmetic suppression argument would have to rule out such contact.
The correction is not responsible for that persistent leakage.

This imports no existence of an actual contact, numerical flux gamma,
negative-source height moment or continuous eigenvector branch.

## 5. Nontrivial-metric and crossing controls

For an exact finite source control take

    M=[[1,b],[b,1]], |b|<1, P*P=M,
    N=(u,v), Q=M-N*N, old canonical domain=span e_1,
    h=e_1, delta=1-u^2, lambda=u^2.

The canonical native-style remainder is C=Q-I. Its old equation holds,
and direct computation yields

    q=(0,b-uv), j=(0,u^2 b-uv),
    j=q-delta(0,b),
    ||M^-1/2 j||^2=(u^2 b-uv)^2/(1-b^2).

This checks the complete inverse metric and noncommuting projection:
discarding the delta M term is not an exact identity. With b=0 and
fixed v=1/4, the correction vanishes, q=j=(0,-uv), and its squared
norm tends to 1/16 as delta tends to zero. C has rank one and the old
form is positive, but the enlarged form crosses. Thus principal
cancellation and compact remainder alone do not imply (5). This finite
control is not an actual native Weil arithmetic countermodel.

The genuine differential crossing and full positive-level mass controls
are replayed through CC32. They remain necessary: an original positive
physical level may become null after shifting, and the entire added mass
channel must remain in its form and positive-inverse bookkeeping.

## 6. Relation to the concurrent IP2 handoff and standing

The live parent preserves IP2's positive-inverse packet checkpoint and
IP1's fixed-test phase handoff. IP2's whole-domain trial/error inequality
can be applied to j_i as before; (1)-(4) identify and pay its explicit
defect correction if an arithmetic trial instead addresses q_i.
No finite packet Gram is substituted for the full M_t inverse, and no
packet approximation with defect-relative error is furnished here.
Neither independent branch is modified or restarted by this pass.

The concurrently recovered IP3 outgoing-shell handoff is also preserved.
Its old-packet annihilation test is compatible with (1): q_i too is
canonically orthogonal to D_s, so an old-only packet trial gives no forced
pairing. Outgoing tests require the complete positive projection, full
Gram and omitted dual error. IP3's historical CC31 standing is superseded
additively here by the preserved CC32 mathematical result and this CC33
decomposition; its historical handoff text is not rewritten.

All 25,657 exact checks pass: 180 new and 25,477 inherited from CC32.
The validator replays CC32 and adds exact principal-cancellation,
noncommuting-metric, squared-error, and compact-rank-one crossing checks.
The actual digamma remainder and infinite-domain identities are analytic
deductions, not actual zeta covariance measurements or Lean proofs.

Original whole-domain positivity stays certified through 21/20,
even0/odd0, physical margin 1/(3*10^63). RH/F4, retained attachment,
reusable continuation, arithmetic remainder suppression and Lean closure
remain open. Global remains paused at NF71 with IP1 metadata preserved;
Aperture and Pre-Contact Shadow remain paused.
