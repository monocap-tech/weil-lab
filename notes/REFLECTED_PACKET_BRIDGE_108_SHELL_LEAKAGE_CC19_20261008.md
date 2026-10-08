# RPB108 CC19: minimal arithmetic shell correlation and its information limit

2026-10-08 UTC. Coupled base CC18 `b384e566150c72b7b3f28c9e77129478d9178dae`.
Coupled remains the sole active integration frontier. Global NF71 and the
other independent investigations stay paused. [Definitions](../docs/TERMINOLOGY_RPB108_SHELL_LEAKAGE.md)
precede use. This is the requested reusable continuation investigation,
following the completed even0 / odd0 fixed-aperture gate.

**Result: classification C.** The complete original identities yield an
exact criterion, but their currently established norm, nesting, spectral
and contact consequences do not establish a quantitative strict,
old-gap-independent shell bound on every finite cap. The missing input is
a WHOLE incoming covariance dominated by the old defect, with a strict
budget after the low-output reaction is paid. The strong power estimate
in NF67 is sufficient but is not minimal. In a protected finite critical
rank, even linear suppression can suffice with an adequate coefficient.
No such coefficient or whole critical covariance is established for the
actual arithmetic beyond the certified anchor.

This is a proved limitation of the stated information/estimator class,
not a proof that the fully specified zeta arithmetic cannot imply the
desired inequality. The countermodels do not reproduce zeta's individual
divisor rows. Neither an actual zeta crossing nor failure of the candidate
arithmetic inequality is asserted. Deciding the all-cap inequality from
those specific rows remains an open arithmetic task.

## 1. Exact criterion and the quantifiers that matter

On a finite cap B retain the ORIGINAL complete P,N and their historical
normalization, all ordinates, multiplicities and mixed slots:

    Q(h,k)=<P h,P k>-<N h,N k>.
    V_a=P(D_a), T_a(P h)=N h, A_a=T_a T_a*.
    W_st=V_t intersect V_s^perp, K=T_t|W_st.

The positive observability gives the closed ranges. Orthogonality here
is in the positive SOURCE metric. In particular the physical lift of a
shell vector can have an interior part. All ranges use the same ambient.
For ORIGINAL-positive s the established NF67 identities are

    A_t=A_s+K K*, D=I-A_s>0,
    B_st=K* D^-1 K,
    original gain at t <1 iff ||B_st||<1.

The exact minimal FULL correlation target is consequently

    K* D^-1 K <= rho_B I, rho_B<1.                 (1)

Equation (1) is an equivalence/target, not an independent proof. The crude
bound ||K||^2/min spectrum D explicitly depends on the old gap. If t is
already assumed nonnegative, B_st<=I follows, but this is circular for
continuation and gives no strict reserve. An arbitrary finite bound on
B_st is also insufficient: the threshold is one.

A reusable non-stalling result needs independently obtained cap constants
h_B>0 and rho_B<1 such that (1) holds for every old-positive s from the
anchor up to B and every s<t<=min(s+h_B,B). A finite partition then reaches
B; each completed block and old block has a positive gap at each of the
finitely many steps. Bounds whose admissible step shrinks with the old
gap do not supply this exit. Neither those uniform constants nor an
equivalent finite accumulated relative-loss bound is supplied here.

## 2. Minimal critical arithmetic correlation

Choose eta>0 and Ecrit=E_s([1-eta,1)), Elow=I-Ecrit.
Let G=Ecrit D Ecrit on the critical output space and L=Ecrit K. Then

    B_st=B_low+L* G^-1 L,
    B_low=K* Elow D^-1 Elow K
           <= ||Elow K||^2/eta I.

If an independent low-output bound B_low<=ell I is available, the minimal
separate critical norm estimate sufficient to close the gate is

    L L* <= q G,  ell+q<1.                       (2)

It is equivalent to L*G^-1 L<=q I: both are precisely
||G^-1/2 L||^2<=q. The equivalence uses operator norms, not commutation.
Separate low/critical scalar budgets are sufficient rather than necessary
for the exact full bound (1), since their worst shell directions may differ.

With an independently protected codimension-d complement and the complete
positive upper bound on the cap, a suitable critical band has rank at
most d, as in NF67. Its eigenvectors y_i are WHOLE negative-source
combinations with defects delta_i>0. For h_w=P_t^-1 w, the entries to bound
are the complete mixed arithmetic correlations

    <y_i,Lw>=<y_i,N h_w>,
    sup_(||w||=1) sum_i |<y_i,N h_w>|^2/delta_i.

The condition w perpendicular V_s retains all old positive correlations.
It is not a spatial support deletion or a height prefix. Even if all
source norms and ordinary Grams are known, their direction relative to
these defect eigenvectors is additional inverse/spectral information.
All off-diagonal covariance terms in L L* must remain. A compatible
low-output bound and protected-rank theorem must be independently valid
on the cap or local chart where (2) is used; CC18's F112 compression is
not declared protected at every aperture.

## 3. Power, Dini and finite-rank estimates

Define the whole-shell cumulative leakage

    F(r)=K* E_s([1-r,1)) K, 0<r<=1.

Spectral calculus, with no source compactness assumption, gives

    B_st=K*K+integral_0^1 F(r) dr/r^2,
    L*G^-1 L=F(eta)/eta+integral_0^eta F(r) dr/r^2. (3)

All integrals are bounded for a fixed old positive s; gap independence
requires a uniform majorant as its defect decreases. Thus

    F(r)<=C_B r omega_B(r) I,
    integral_0^eta omega_B(r) dr/r <infinity

implies the critical bound

    q<=C_B[omega_B(eta)+integral_0^eta omega_B(r) dr/r].

A power r^(1+alpha), alpha>0, is one sufficient choice. It is not minimal:
omega(r)=(1+log(eta/r))^(-1-epsilon), epsilon>0, has finite Dini integral
and yields q<=C_B(1+1/epsilon). An independent strict budget is still
required. A norm-Dini majorant is sufficient, not necessary for the
operator integral: shell directions need not commute or coincide.

Without a critical rank bound, F(r)<=C r alone is insufficient. An exact
finite-dimensional family has delta_j=2^-j, squared incoming coordinates
delta_j/4, j=1,...,n. Its raw incoming norm is below1/4 and F(r)<=r/2 for
EVERY r, yet its weighted cost is n/4. The dimension grows across this
family; it is not a counterexample to an independently fixed rank bound.

With critical rank <=d the conclusion changes. If F(r)<=C r I uniformly,
then each individual spectral coordinate has squared row norm <=C delta_i.
The trace of L*G^-1L is <=d C, so its norm is <=d C. Consequently

    ell+d C<1                                      (4)

is a sufficient old-gap-independent bound on a protected finite-rank
chart. This is the precise finite-rank qualification to NF67's general
critical-power warning. It supplies no actual value of C or protection
on arbitrary caps. The matrix inequality (2) is sharper and avoids the
rank-factor trace loss. The rank dimension alone supplies no C.

## 4. Explicit genuine differential shell control

Use the ORIGINAL control form on nested H0^1(-a,a):

    q(h)=||h'||^2-||h||^2, P h=h', N h=h.

Its fixed-cap positive range consists of mean-zero derivative functions
supported in (-a,a). T is integration with zero boundary values. The
gain is 2a/pi. The first actual contact is a*=pi/2, with the next physical
eigenlevel still positive and bounded nonzero complete source energies.
This is the genuine differential operator already proved in CC4.

For s<a*, normalize its old ground output
e_s(x)=cos(pi x/(2s))/sqrt(s), zero outside (-s,s). It is an eigenvector
of A_s with eigenvalue 4s^2/pi^2 and defect d_s=1-4s^2/pi^2. The adjoint
T_t* e_s is the derivative of the exact Dirichlet solution -u''=e_s on
(-t,t). The old solution is u_s=e_s/(pi/(2s))^2. The larger solution has
the SAME interior derivative and linear exterior tails; its interior
constant changes to join those tails. Its boundary slope magnitude is
2sqrt(s)/pi. Since T_s*e_s is the projection onto V_s, exact orthogonal
shell completion gives

    ||K_st* e_s||^2
      =||T_t*e_s||^2-||T_s*e_s||^2
      =8s(t-s)/pi^2.                              (5)

Independently, the new interior constant is
c=2sqrt(s)(t-s)/pi and integral e_s=4sqrt(s)/pi.
The Dirichlet energy identity gives the same difference c*integral e_s.
This verifies (5) without inferring it from a guessed eigenvalue curve.

This uses the genuine source shell, including its interior physical lift.
In dimensionless rational coordinates u=2s/pi, v=2t/pi,

    d=1-u^2, leakage=2u(v-u).

At t=a* the weighted old-ground contribution is

    leakage/d=2s/(a*+s) ->1 as s approaches a*.

The whole cost equals1 at contact by exact completed nullity. Hence even
arbitrarily thin shells do not give a uniform strict reserve. Leakage
is asymptotic to d, so every uniform superlinear estimate C d^(1+alpha)
fails. With the spectral threshold just above the old top eigenvalue,
the linear coefficient required approaches1. With rank1 and nonnegative
low cost this cannot satisfy a uniform strict budget (4).

For any fixed t>a*, still within one finite cap,

    leakage/d=2s(t-s)/[(a*-s)(a*+s)] ->infinity.

Thus even a finite OLD-GAP-INDEPENDENT weighted upper bound for all
old-positive s and allowed target t fails in this genuine model. The
complete source maps remain bounded on that cap. If targets are restricted
to already-positive windows, the bound <=1 follows from positivity and
has no independent exclusion force. These are distinct quantifiers.

The logarithmic-growth objection is also addressed by CC4's genuine
control q=E_log-kappa mass on the exact canonical carrier, with
P=sqrt(w) Fourier and N=sqrt(kappa) h. Choose 1<kappa below the attained
lowest E_log level at aperture1. It has a positive anchor. Dilating a
fixed smooth unit bump makes E_log tend to1, producing a negative vector
at a FINITE larger aperture. Compact physical inclusion and the canonical
I+compact family supply an attained finite first contact and a locally
protected critical chart. The exact shell criterion therefore reaches
unit cost there. No all-cap strict shell inequality can follow from
logarithmic growth, those source identities and structural bounds alone.
This analytic control is not a computed zeta vector or a theorem of
negative original Weil energy.

## 5. Genuine positive-level control

For the differential ORIGINAL q=derivative mass minus mass, shift by
mu=9/16. The full negative analysis becomes (h,sqrt(mu)h), so its Gram
potential is kappa=25/16. The shifted contact occurs at v=4/5, while the
unshifted original lowest physical eigenvalue there is exactly9/16>0.

For old u<v the shifted defect is 1-kappa u^2 and shifted leakage is
kappa*2u(v-u); their ratio is 2u/(v+u), tending to1. The ORIGINAL old
source defect stays above9/25 and the ORIGINAL target gain squared is
16/25<1. Its original shell cost is strictly below1. All shifted A,K,
critical directions and low blocks must be recomputed with the added
physical mass channel. A shifted unit cost cannot be relabeled original
nullity. The controls check this with exact rational parameters.

## 6. What the original arithmetic currently supplies

The actual fixed-aperture CC18 certificate supplies whole-domain positivity
through21/20, even0 / odd0, with inherited joined physical margin
1/(3*10^63). It evaluates a full physical compression reaction at that
aperture. It does not evaluate the source-orthogonal K_st for all incoming
vectors or the critical-source matrix (2) on arbitrary larger caps.

The complete original P/N identity supplies equality of the signed mixed
arithmetic, not a sign or suppression inequality for its near-critical
components. Positive observability, bounded complete analysis, compact
physical inclusion, finite contact rank and finite active prime count
give the definitions and structural gates. The controls above satisfy
those structural gates while reaching contact; their output therefore
cannot be used to derive an arithmetic strict reserve.

At every finite cap the real source computation must retain ALL original
active prime powers, Lambda(p^r)=log p, both orientations, both signed
poles, all divisor channels and every mixed old/new correlation. Equality
at a prime threshold gives zero supported overlap; this prevents a form
jump but bounds no inverse-defect-weighted leakage. No frozen prime
dictionary, rowwise domination, shift-null inference, auxiliary defect
channel or physical-strip replacement is accepted.

Precisely missing is an independent evaluation/estimate of the whole
covariance L L* relative to G and a compatible low-output budget, with
constants that retain a uniform strict reserve and admissible shell width
on each finite cap. A proof exploiting the actual cross-prime,
archimedean, pole and divisor correlations could supply it. The complete
identities do not automatically supply that proof, and the present finite
source columns do not measure the universal quantifiers in (1)-(2).

## 7. Validation, custody and exit

The validator passes **7,032 exact rational checks**: 5,460 new controls
and all1,572 NF67 source-shell controls replayed. New checks include80
approaching-contact scales,80 positive-level scales,80 varying-rank
critical-power families,48 fixed-rank cases,18 whole covariance cases,
and5 Dini partial-sum bounds. Exact source algebra, null completion and
noncommuting whole resolvent controls are inherited from NF67. Rational
coordinates express the differential formulas exactly; finite checks are
not the proof of the Green calculation or logarithmic model. Those
analytic arguments are separately given above and inherited from CC4.
No Lean certification or fresh full divisor-source reconstruction is
claimed. Input and artifact byte hashes are pinned in the custody record.

The reusable arithmetic inequality is **not certified and not disproved
for zeta**. Its derivation from the available structural consequences is
refuted with precise countercontrols. No new aperture, actual contact,
RH/F4, accumulated finite-cap loss or non-stalling theorem is claimed.
The next gate is (2), or the exact full bound (1), with independently
protected low output and cap-uniform strict/step budgets. Further fixed
remainder expansion is not reopened. Historical proofs and paused refs
remain intact; publication is additive on Coupled only.
