# RPB108 CC32: hypothetical contact forces an individual persistent critical residual

Date: 2026-10-08 UTC. Parent: 5b52813afb77923fdab97410798cced607f6d47d.
Definitions: [persistent critical row](../docs/TERMINOLOGY_RPB108_PERSISTENT_CRITICAL_ROW.md).
Scope: conditional actual-source lower bound. No new arithmetic upper
bound, actual contact existence, aperture certificate or Lean proof.

## Result

CC31 reduces the vanishing-covariance target to scalar critical residual
norms. The reduction does not hide first-contact leakage in a collective
combination: at every sufficiently close old aperture, a SINGLE actual
critical eigenvector has nonvanishing complete residual norm while its
defect tends to zero at least as fast as the expected contact defect.

Let a be a hypothetical attained actual nonnegative contact. Fix a finite
cap B>a and a target t with a<t<=B, and normalize its contact output y
to unit norm. Set

    gamma=<y,(A_t-A_a)y>>0,
    d_s=<y,(I-A_s)y>->0 as s increases to a.

The positive gamma is the established CC29 actual native rigidity result,
conditional on this contact. Let d_B and eta_B be CC31's fixed-cap rank
bound and fixed critical band, and choose any M>=||A_t||. Define

    C=16 M^2/gamma^2.

For every sufficiently close s<a, there is a unit critical eigenvector
y_i of A_s, with lambda_i=1-delta_i, for which

    0<delta_i<=C d_s,
    ||K_st* y_i||^2>=gamma/(2d_B),                         (1)
    ||M_t^-1/2 J_i*||^2
       >=(1-eta_B) gamma/(2d_B).                          (2)

Here M_t=P_t*P_t is the complete protected positive metric, not the
scalar M used for the operator-norm bound. The quantities in (1)-(2)
are not evaluated numerically for zeta. Conditional contact implies
d_B>=1; if d_B=0 the rank result already rules out such a contact.

The selected eigenvector can depend on s. No norm-continuous source
projection, continuous eigenvector branch, simple contact or fixed phase
choice is required. The target t remains a fixed strict enlargement.

## 1. Recovering the live integration head

The active head advanced concurrently from CC31 to 5b52813afb77923fdab97410798cced607f6d47d.
That additive commit introduces RPB108_PHASE_GEOMETRY_IP1_CROSS_FRONT_HANDOFF_20261008.md.
It records fixed-test localization and phase identities from independent
IP1, with no adaptive critical residual bound. This pass preserves that
note and its scope, and does not merge or modify the independent branch.
All CC29--CC31 source dependencies are retained unchanged.

## 2. A shrinking filter locates the obstruction inside the fixed band

Use the complete common-cap source operators from CC29. For old strict
s<a, A_s>=0, ||A_s||<1, A_s<=A_a<=A_t, and A_s->A_a strongly.
The contact equation gives d_s>0 and d_s->0. Take s close enough that

    epsilon_s=C d_s<=eta_B<1,
    F_s=1_[1-epsilon_s,1)(A_s), v_s=F_s y.

This is a diagnostic subprojection of the FIXED E_s. Its rank is at most
d_B by CC31. Spectral calculus yields

    ||y-v_s||^2<=d_s/epsilon_s=1/C,
    ||v_s||<=1.                                          (3)

The diagnostic error need not tend to zero. A uniformly small error is
enough for this row-selection theorem. The previous fixed-band argument
still proves convergence of the full critical projection to y.

Let H_s=A_t-A_s>=0. It has norm at most M, and

    <y,H_s y>=gamma+d_s.

Replacing y by v_s changes this quadratic pairing by at most
2M||y-v_s||. By (3) and the specified C,

    <v_s,H_s v_s>
      >=gamma+d_s-2M/sqrt(C)
      =gamma/2+d_s>=gamma/2.                              (4)

In particular F_s is nonzero. The proof uses only complete source
positivity/order and CC29 flux, not a separated phase estimator.

## 3. Trace selection of a genuine old eigenvector

The finite positive covariance F_s H_s F_s on ran F_s satisfies

    tr(F_s H_s F_s)>=<v_s,H_s v_s>>=gamma/2.               (5)

Choose any orthonormal A_s eigenbasis of ran F_s. Its r_s<=d_B diagonal
entries sum to the trace in (5). Therefore at least one entry obeys

    a_i=<y_i,H_s y_i>>=gamma/(2r_s)>=gamma/(2d_B).

Because y_i belongs to F_s, its source defect satisfies
delta_i<=epsilon_s=C d_s. The exact CC20 scalar identity gives

    ||M_t^-1/2 J_i*||^2=lambda_i a_i,

and lambda_i>=1-eta_B yields (2). This proves the stated lower bounds
for an INDIVIDUAL actual eigenvector row, not only for a combined row.
The trace is of the full shell covariance, not a truncated source Gram.

This procedure gives a selection at each old aperture. It does not
assert a single index can be followed to contact or that the selected
vectors have a finite coordinate height moment.

## 4. Quantitative violation of every scalar vanishing-modulus proposal

For a bounded nonnegative omega with omega(x)->0 as x->0, define

    Omega(epsilon)=sup_(0<u<=epsilon) omega(u).

On the selected row, if omega(delta_i)>0, (1) implies

    ||M_t^-1/2 J_i*||^2/[lambda_i omega(delta_i)]
       =a_i/omega(delta_i)
       >=gamma/[2d_B Omega(C d_s)] ->infinity.            (6)

If omega(delta_i)=0, its proposed upper bound is already incompatible
with the strictly positive numerator. No monotonicity or power form of
omega is needed. In particular for omega(u)=u^alpha, alpha>0, the
selected scalar cost is at least

    gamma/[2d_B C^alpha d_s^alpha].                       (7)

For the strict linear cost the lower bound is gamma/(2d_B C d_s).
This is weaker than CC29's best collective reaction bound, but it
identifies which kind of SINGLE-mode arithmetic estimate must prevent
contact. It does not prove that contact exists or that the desired upper
estimate fails for the actual divisor.

The filter width epsilon_s tends to zero ONLY for selection in this
conditional obstruction proof. It is not substituted for the fixed
critical band in CC29 or CC31 and does not shrink t-s to evade contact.
For any proposed cap-only step h_B>0, choose fixed t>a with t-a<h_B/2;
then t-s<h_B for all sufficiently near-contact s.

## 5. Genuine crossing and full positive-level controls

In the genuine H01 differential crossing, the one-dimensional old
critical row has defect 1-u^2 and exact shell leakage 2u(v-u).
At fixed v=1+1/16 the leakage tends to 1/8 while its defect vanishes.
It is already an individual persistent row, so no hidden collective
phase phenomenon is needed to explain this obstruction.

The complete positive-level control remains P=I,
N=(9/25,12/25), mu=16/25. Its original cost is 9/34<1;
the shifted form with the entire mass channel has old gain 481/625,
defect 144/625, and critical plus low cost exactly one. Finite rank,
row selection and a shifted null equation still do not distinguish
original zero from a positive physical level.

Finite rational rotating-projection and coherent-cluster controls test
the selection inequalities with real eigenvectors, nontrivial phase
coherence and complete positive inverse bookkeeping inherited from the
earlier controls. They are not actual zeta vectors or native-form
countermodels. Source coordinate truncation and artificial divisor
substitution remain excluded.

## Validation and standing

All 25,477 exact checks pass: 102 new and 25,375 inherited from CC31.
The validator replays CC31 and adds exact diagnostic-filter, trace-row,
rotating eigenvector, coherent-cluster, power and genuine-crossing checks.
The conditional infinite source theorem is an analytic deduction from
CC29 flux and CC31 uniform rank. Rational tests are not a proof of those
inputs, a numerical evaluation of gamma or a Lean certificate.

No actual scalar arithmetic upper bound is supplied. Original whole-domain
positivity stays certified through 21/20, even0/odd0, physical margin
1/(3*10^63). RH/F4, retained attachment, reusable continuation and Lean
closure remain open. Global NF71, Aperture and Pre-Contact Shadow remain
paused. The concurrent IP1 cross-front handoff is preserved.
