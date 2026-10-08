# RPB108 CC20: actual forced numerator and protected positive-inverse covariance

2026-10-08 UTC. Recovered Coupled CC19
`f3ef1c262fb2bcd015a042438c069fe7ce56945f` and paused Global NF71
`6ed350cb6736993fa9801bce9ab15f096c10c200`. Coupled is the sole active
integration frontier. This completes STAGE ONE of the requested staged
NF: specify the actual arithmetic numerator and a falsifiable candidate
estimate. [Definitions](../docs/TERMINOLOGY_RPB108_FORCED_SOURCE.md) precede use.

**A: exact analytic covariance interface.** The complete critical leakage
matrix is exactly the covariance of a forced ORIGINAL arithmetic dual
residual through the full POSITIVE source inverse. This inverse is
protected independently of the old signed gap. The required defect
weight remains explicit; it has not been eliminated by a change of chart.

**C: automatic small-factor candidate rejected.** Complete paired-source
orthogonality and partner reflection do not supply a defect factor in
that numerator. The exact paired expansion retains an unsuppressed
difference kernel. This does not disprove a sharper estimate exploiting
actual zeta correlations. No new all-cap arithmetic inequality, aperture,
accumulated-loss or non-stalling theorem is certified.

## 1. Named actual input and unchanged normalization

Fix a finite cap B and the actual complete normalized analyses on D_B.
The historical raw pair sources are (F(conj gamma)+F(gamma))/sqrt(2)
and (F(conj gamma)-F(gamma))/sqrt(2), summed over EVERY divisor
multiplicity copy. Their raw difference is twice the native form.
Accordingly the already normalized source channels used here are

    p_q(h)=[F_h(conj gamma_q)+F_h(gamma_q)]/2,
    n_q(h)=[F_h(conj gamma_q)-F_h(gamma_q)]/2,
    Q(h,f)=sum_q conjugate(p_q(h))*p_q(f)
                    -conjugate(n_q(h))*n_q(f).

Copies, partner-fixed points and both mixed slots remain. Grouping by a
zero point instead would require its explicit multiplicity weight; no
orbit representative is chosen here. The negative channel sign is the
historical conjugate-minus-original sign. Flipping both negative factors
would not cancel their product.

These conventions are read from `ActualZetaSourceDecomposition.lean`,
`NeutralLogSelectedSourceAttachment.lean` and `ActualZetaNativeWeilForm.lean`.
Their existing Green-vector statements and the established analytic
canonical-domain extension are dependencies. CC20's NEW identities on
the whole canonical domain are analytic, not new Lean theorems. No claim
is made to identify the independently named historical WD-T38 carrier.

The cap observability is c_B||h||_D<=||P h||<=C_B||h||_D with c_B>0.
It makes M_t=P_t*P_t bounded positive with M_t>=c_B^2 I, for t<=B.
This lower bound concerns the POSITIVE source metric; it does not assume
original positivity at t. Its existing qualitative constant is not
relabeled an evaluated effective numerical bound.

## 2. Critical original lifts and the forced residual

Let s be original-positive and use the exact NF67 source shell. A_s=T_s T_s*
acts on the complete negative ambient. On a finite critical output space
choose orthonormal eigenvectors y_i with eigenvalues lambda_i>0 and
delta_i=1-lambda_i>0. The protected-rank hypothesis, where used, must
hold independently on that chart; it is not assumed on arbitrary caps.

Define p_i=T_s* y_i/sqrt(lambda_i) in V_s, and h_i=P_s^-1 p_i.
The p_i are orthonormal, T_s p_i=sqrt(lambda_i)y_i and
T_s*T_s p_i=lambda_i p_i. Consequently for EVERY k in D_s,

    Q(h_i,k)=delta_i<P h_i,P k>.                   (1)

These are generalized eigenvectors in the POSITIVE SOURCE metric, not
physical L2 eigenvectors with an invented level. In particular an actual
positive physical eigenmode theorem cannot be attached to them by name.
Define the bounded canonical dual row on D_t

    J_i(f)=Q(h_i,f)-delta_i<P h_i,P f>.            (2)

It annihilates D_s exactly by (1). It retains the ORIGINAL physical form,
including all active prime powers, both orientations and both signed
poles, followed by an EXACT complete positive-source correlation.
It is not a physical L2 source asserted to exist for a rough form vector.
No global H1 or full physical operator-domain assumption is used.

## 3. Exact source-shell lift, with the whole positive inverse

Let i:D_s->D_t be the canonical support inclusion. On this common
supported Fourier norm i is isometric. M_s=i* M_t i. The positive-metric
projection and its source-shell complement are

    R=i M_s^-1 i* M_t,
    z=(I-R)f, P z perpendicular V_s.

R is bounded, idempotent and M_t-self-adjoint. It is not the physical
strip projection. On its old-range value, (1) gives

    Q(h_i,z)=Q(h_i,f)-delta_i<P h_i,P Rf>
            =Q(h_i,f)-delta_i<P h_i,P f>=J_i(f).

The positive orthogonality also gives

    <y_i,N z>=-J_i(f)/sqrt(lambda_i).             (3)

For w=Pz in W_st the left side is exactly the i-th coordinate of
L=Ecrit K_st. Thus (2)-(3) specify the complete actual incoming
correlation; no row or quotient trial is substituted.

Write Lambda=diag(lambda_i), G=diag(delta_i), and view J:D_t->C^d.
The map H_t=P_t^-1:V_t->D_t satisfies H_t H_t*=M_t^-1. Since J kills
the entire old domain, J H_t kills V_s. Its covariance on W_st is
therefore the SAME as its covariance on all V_t. Equation (3) proves

    L L*=Lambda^-1/2 J M_t^-1 J* Lambda^-1/2.     (4)

An independent projection calculation verifies the same identity:

    (I-R) M_t^-1 (I-R)*
          =M_t^-1-i M_s^-1 i* >=0,
    J[M_t^-1-i M_s^-1 i*]J*=J M_t^-1 J*,

because J i=0. The adjoints are canonical D_t adjoints in this formula.
All whole-domain shell directions and the complete positive metric are
present. Finite critical OUTPUT rank does not make the incoming domain
finite. This is a finite matrix of whole dual norms, not the Gram of a
finite source prefix or finite trial subspace.

The inverse in (4) is uniformly protected by positive observability on
the fixed cap and does NOT divide by the collapsing ORIGINAL defect.
The subsequent division by G remains essential. This distinction is the
useful new interface; it is not a proof of suppression or non-stalling.

## 4. The candidate estimate is now specified in actual arithmetic rows

By (4), the minimal separate critical condition from CC19 is exactly

    J M_t^-1 J* <= q Lambda G,
    B_low<=ell I, ell+q<1.                       (5)

Both matrices on the right are critical-source spectral metrics. All
mixed J-row covariances on the left must remain. A sufficient version
that uses only the independently protected positive inverse bound is

    ||(Lambda G)^-1/2 J||_(D_t -> C^d)^2
                <=q c_B^2.                      (6)

Equivalently, for every coefficient vector alpha, the canonical dual
norm squared of sum_i conjugate(alpha_i)J_i/sqrt(lambda_i delta_i)
is at most q c_B^2||alpha||^2. This is a whole combined residual estimate,
not independent bounds on its native and positive-source summands.
The exact condition (5) can be sharper than (6).

The independent low-output estimate and a compatible critical band remain
required. An all-cap exit additionally needs uniform strict budgets and
admissible steps as in CC19. Neither a nonconstructive positive-source
constant nor a forced-row identity produces those constants.

This candidate is distinct from CC12's physical residual B-CZ and CC18's
fixed-aperture physical source frame. Those data do not give the actual
generalized h_i, the complete positive Gram M_t, or J on every new-domain
vector. In particular CC18's precise weak odd trial is not relabeled a
critical source eigenvector, and its small source-construction error is
not an estimate of (2).

## 5. Exact paired arithmetic expansion: where the missing factor resides

Write gamma_q=theta_q+i beta_q. On the actual normalized dictionary,

    p_q(h)=integral h(x) exp(i theta_q x) cosh(beta_q x) dx,
    n_q(h)=integral h(x) exp(i theta_q x) sinh(beta_q x) dx.

For a FINITE divisor cutoff, set its paired mixed kernels

    D_q(x,y)=exp(i theta_q(y-x))*cosh(beta_q(x-y)),
    S_q(x,y)=exp(i theta_q(y-x))*cosh(beta_q(x+y)).

Product identities give positive and negative mixed kernels (D_q+S_q)/2
and (S_q-D_q)/2, respectively. Hence the forced residual kernel for row i
is EXACTLY

    (1-delta_i/2)D_q-(delta_i/2)S_q.              (7)

Equation (7) is summed with all actual multiplicity copies, then paired
against conjugate(h_i(x))*f(y). The complete limit is taken AFTER this
legal mixed pairing: the P/N mixed series are absolutely convergent by
their complete square bounds. No pointwise infinite zero-kernel sum is
asserted, no cutoff is interchanged with an operator supremum, and no
cutoff explicit formula is falsely substituted for the full native one.

The first coefficient in (7) tends to ONE as delta_i approaches zero.
Only the sum-kernel coefficient has an explicit defect factor. On a
source-shell z, <P h_i,P z>=0 says the FULL paired sum of D_q+S_q is zero.
It makes the full J pairing equal to the D_q pairing, not to a defect
multiple of it. The old critical equation says J vanishes on D_s, which
locates a quotient residual; it gives no bound on that quotient norm.

Partner reflection sends beta to -beta. Both D_q and S_q are unchanged.
The two negative channels flip sign together, so their mixed product
is unchanged. Reflection duplicates these pair contributions instead
of cancelling them. Critical-line beta=0 makes that pair's negative
channel zero, but the full divisor is not assumed critical-line only.
The accepted transverse strip, even if used, cannot suppress the
complete paired kernel by a factor of delta_i.

Therefore the automatic candidate

    source-shell orthogonality + old critical equation + partner symmetry
      -> J is O(delta_i) with a gap-independent quotient norm

does NOT follow from the expansion. Formula (7) itself leaves an
unsuppressed full difference pairing. A genuine zeta-specific estimate
of that quotient pairing, relative to delta_i, is the missing input.
NF55's individual-pair tanh bound remains rejected; it is not restarted.

## 6. Crossing and positive-level checks of this specific candidate

CC19's genuine differential model supplies the actual source-shell
covariance along its old ground eigenvector. In u=2s/pi, v=2t/pi,
lambda=u^2, delta=1-u^2, and leakage=2u(v-u). The EXACT forced covariance
in (4) is consequently

    J M_t^-1 J*=lambda*2u(v-u).

At its genuine target contact v=1, dividing by lambda delta gives
2u/(1+u), approaching1. The row dual norm in the M_t^-1 metric is of
order sqrt(delta), not order delta. Thus the proposed automatic
defect-factor version fails in a genuine operator, not just a renamed
scalar eigenlevel. The entire positive-source inverse stays protected
on the finite cap. CC4's genuine canonical logarithmic crossing similarly
reaches unit full cost, so switching back to logarithmic growth does not
close the strict budget. Those controls do not reproduce zeta's rows.

The full positive-level control uses original P=I and
N=(9/25,12/25). Its ORIGINAL lowest physical level is mu=16/25>0.
The original incoming cost on the old first coordinate is9/34<1.
The shifted negative analysis adds sqrt(mu) times the ENTIRE physical
vector. Its old lambda becomes481/625 and its defect144/625. Its critical
and low-output costs are recomputed; they add to EXACTLY1. The shifted
null vector has Q(h)=mu*physical mass>0 in the original form.
Omitting the mass channel or reusing the original critical metric would
give the wrong candidate test. No shifted contact is called original nullity.

The finite whole-source controls independently compute L L* using the
direct source-shell physical lift and compare it with the forced rows
and full positive inverse. They include nonidentity positive metrics,
nonorthogonal old physical coordinates, all mixed critical covariances,
positive completions and negative completions. They are model controls,
not evaluations of actual critical source coordinates.

## 7. Checkpoint, validation and next staged obligation

**11,308 exact checks pass:** 4,276 new checks and all7,032 CC19 checks
replayed. New checks comprise3,456 source covariance checks across384
complete-source cases,384 quotient projection checks,117 paired hyperbolic
dictionary checks,72 partner/normalization checks,7 full mass-shift checks
and240 genuine differential scaling checks. The source-shell physical
lift and the full inverse covariance are computed through separate routes.
The operator derivation and infinite mixed-series passage are analytic;
finite samples do not certify them in Lean. No actual zeta source cutoff,
critical vector, complete M_t inverse or numerical J covariance is evaluated.

Stage one now has an explicit actual numerator, its full covariance, a
protected inverse interface and a specified arithmetic inequality (5).
The next stage is to obtain a NEW actual arithmetic bound on that forced
quotient pairing. Merely reproducing (7), bounding its two terms separately,
adding source precision or invoking the old gap is not an advance.
A candidate must exploit an identified relation of the actual divisor
dictionary and survive the crossing/positive-level discrimination tests.
If no such relation is supplied, this interface alone is not a reason to
continue generic conditional calculations.

The whole-domain CC18 anchor through21/20, even0 / odd0, remains intact.
No new aperture or all-cap positivity is claimed. Accumulated finite-cap
relative loss, non-stalling, RH/F4, retained attachment and Lean closure
remain open in their existing scopes. Publication is additive on Coupled;
paused refs and historical bytes are preserved.
