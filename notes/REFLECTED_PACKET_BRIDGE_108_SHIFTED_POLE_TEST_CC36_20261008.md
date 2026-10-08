# RPB108 CC36: parity pole correlation retains the whole shifted mass channel

Date: 2026-10-08 UTC. Parent: eed85147c6ebf4cec20ebaa8ff06190470859f5a.
Definitions: [shifted pole test](../docs/TERMINOLOGY_RPB108_SHIFTED_POLE_TEST.md).
Result: the positive-level control survives the exact native pole split.
No arithmetic defect estimate is certified.

## Exact shifted native equation

The canonical shifted form is I+C_t-mu B_t, B_t=i_t*i_t.
For an exact shifted critical lift its forced row is

    j_mu=(I-Pi)(C_t-mu B_t-delta_mu M_t)h
         =q_mu-delta_mu(I-Pi)M_t h,
    q_mu=q_0+sigma a v-mu w, w=(I-Pi)B_t h.             (1)

The same principal cancellation and complete positive inverse as CC33
apply. In particular the norm difference between j_mu and q_mu is
at most (U_B/c_B)delta_mu. The mass term has only the absolute bound

    ||M_t^-1/2 mu w||<=mu/c_B^2.                        (2)

Indeed ||i_t||<=1, ||B_t||<=1 and ||h||_D<=1/c_B.
For fixed positive mu this does not vanish with delta_mu. No proof
that w is zero or lies in the pole direction is available for native
shifted critical lifts. B_t is injective on the infinite-dimensional
canonical carrier, so it has infinite rank. This statement concerns
B_t, not the rank of its projected off-diagonal block w.

For v nonzero write in the full dual metric
q_0=z_0 v+r_0 and w=z_w v+r_w, both remainders perpendicular to v.
Then the exact CC35 identity becomes

    ||q_mu||_*^2=||r_0-mu r_w||_*^2
                  +||v||_*^2 |z_0-mu z_w+sigma a|^2.    (3)

For v=0 retain ||q_0-mu w||_* directly. Thus both the transverse and
longitudinal tests change under a physical level shift. Deleting mass
from either test is unjustified. Also h itself and delta_mu are selected
by the shifted source, not borrowed from the original eigenproblem.

Even if w happens to vanish, the old defect and output normalization
change. With ||Ph||=1, testing the old equation by h gives

    Q(h)=delta_mu+mu||h||_2^2.                          (4)

The left is the original Rayleigh defect of this vector, not necessarily
an original source eigenvalue. In particular delta_mu=0 describes a
positive original physical level when mu>0 and h is nonzero. It is not
an original Weil null. No global endpoint argument can identify the
two merely because their projected forcing happens to coincide.

## Exact full positive-level control

Replay the complete control P=I, N=(a,k), a=9/25, k=12/25,
mu=16/25, old domain span e_1. Physical inclusion is I, so w=0.
For h=e_1 the original and shifted forced rows are both -ak e_2.
Nevertheless their old defects differ:

    delta_original=1-a^2=544/625,
    delta_mu=1-a^2-mu=144/625,
    lambda_mu=a^2+mu=481/625.

The ORIGINAL whole incoming budget is k^2/(1-a^2)=9/34<1.
With the complete shifted negative source (N,sqrt(mu)I), its incoming
column has all three coordinates (k,0,sqrt(mu)). Its critical contribution
and low complement are

    critical=a^2 k^2/(lambda_mu delta_mu),
    low=k^2+mu-a^2 k^2/lambda_mu,
    critical+low=1, low>0.

The shifted Schur complement is zero while the original remains
strictly positive. The vector (a,k) is an original eigenvector of Q
with positive physical eigenvalue mu and becomes null only after
the shift. Its original signed value is mu(a^2+k^2)>0.
Thus identical forced numerators alone do not certify identical
reaction, and a retained parity pole calculation cannot remove this
control. This is an exact source control, not an actual Weil divisor.

Additional rational controls check (3) with nontrivial positive metric,
both parity signs and nonzero transverse mass. All 99 new checks and
25,873 CC35 checks pass, total25,972. These are finite algebra controls;
the native identities above are analytic and no actual critical
zeta covariance or Lean certificate is computed.

## Standing

This pass completes a positive-level test of CC35's proposed native
correlation measurement. It supplies no suppression of either term
in the original mu=0 problem. Neither a shifted control nor the
failure of a shift-blind argument proves logical nonimplication from
the complete original Weil identities.

IP6/IP7 handoffs are preserved as read-only inputs. IP7's finite-cap
Schur gate remains uncomputed on an actual native matrix and has not
certified a new aperture. Original positivity remains21/20, even0/odd0,
physical margin1/(3*10^63). RH/F4, original outward suppression,
retained attachment, reusable continuation and Lean closure remain open.
