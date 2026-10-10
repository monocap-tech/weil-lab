# RPB108 RC5 — direct native endpoint interface and canonical 1.06 anchor

2026-10-10. Independent branch research/rpb108-route-consolidation.
Parent: 1cd613cc0e995f73f77e12c2e3f9e81be8ac5c44 (RC4).
Only this branch is written.

## Result and scope

The positive-source metric is necessary for the exact CC20 source-shell
quantities, but it is not necessary to STATE a separate sufficient native
first-contact test. RC4's metric ambiguity does not prove that reconstructing
M=P*P must precede every possible endpoint route.

This note provides a direct native formulation of the missing arithmetic
decay bound and derives an actual canonical logarithmic-energy anchor at
a=53/50 from CC119. The native decay bound is not proved. No new compactness,
regularity or generic continuity investigation is reopened: the argument uses
the already established canonical compact-remainder and attained-contact
framework solely to connect the new acceptance statement to the existing
endpoint theorem.

## Definitions before use

On a fixed finite cap B, use the canonical supported logarithmic Hilbert
domain D_B and the inherited native form representation

    Q(h,f)=<h,f>_D+<h,C_B f>_D,
    C_B=i_B*R_B i_B.

R_B is the complete bounded physical remainder from CC33. C_B is its compact
canonical representative under the inherited compact physical inclusion.
Full physical Q remains unbounded; no physical-L2 representation of its
logarithmic principal part is introduced.

Let Pi_a denote the CANONICAL orthogonal projection onto D_a in D_B.
For old-positive s define the bounded self-adjoint supported canonical operator

    H_s=Pi_s(I+C_B)|D_s.

Its energy is <h,H_s h>_D=Q(h,h). This operator is not the positive-source
Gram A_s of CC19. Define the whole outward native forcing into a larger t by

    O_st h=(Pi_t-Pi_s)C_B h, h in D_s, s<t<=B.          (1)

The nested canonical projections commute, so this is precisely the
D_t-representer (I-Pi_s)C_t h from CC33. It is not a spatial strip cutoff.

## Direct native sufficient endpoint property

For each finite cap, ask for cap-only epsilon_B>0, step h_B>0,
constant b_B<infinity and bounded nonnegative omega_B with omega_B(r)->0 as
r->0+. For every old-positive s from the 53/50 anchor, every admissible t,

    s<t<=min(s+h_B,B),

and every canonical unit vector h in D_s with 0<Q(h,h)<=epsilon_B, require

    ||O_st h||_D^2 <= b_B omega_B(Q(h,h)).              (2)

This is a signed-native, whole canonical-domain arithmetic estimate. It uses
neither positive-source eigenvectors nor M_t^(-1). It does not follow from a
small finite trial covariance, an absolute cap remainder bound, or compactness.
It is another sufficient target; no strict improvement in its provability
over the source-metric target is claimed.

### Endpoint implication

Suppose first contact occurs at an interior a of a finite cap. The inherited
attained-contact construction provides near-null canonical unit vectors
h_n in D_s_n for old-positive s_n increasing to a, with Q(h_n,h_n)->0.
For example these can be chosen from the old lower spectral subspaces in the
existing dilated form family. No new spectral continuity theorem is asserted.

Since 0<H_s_n<= (1+||C_B||)I on the old domain,

    ||H_s_n h_n||_D^2
       <=(1+||C_B||)Q(h_n,h_n)->0.                    (3)

The old equation rearranges as

    h_n=-Pi_s_n C_B h_n+o_D(1).

Compactness of C_B and the inherited strong support exhaustion
Pi_s_n->Pi_a imply that a subsequence h_n converges strongly in D_B to a
canonical unit h in D_a. Testing on the dense union of old supported domains
shows Q(h,f)=0 for every f in D_a. Thus h is a genuine original weak-null,
with no physical operator-domain assumption.

Fix t>a inside the cap-only step width. If (2) held, then
O_s_n,t h_n->0. Strong convergence and support exhaustion give

    (Pi_t-Pi_a)C_B h=0.

Combined with old weak-nullity, this means

    Pi_t(I+C_B)h=0,
    Q(h,f)=0 for every f in D_t.                       (4)

The inherited actual strict-enlargement/no-flat-extension theorem in CC29
rules out (4) for nonzero h. One proof uses the native stationary-correlation
nonanalyticity theorem of CC28: extension nullity makes the prescribed
correlation vanish on a neighborhood, which would be analytic there.
Therefore (2), uniformly on every finite cap, excludes first contact.
As before, the inherited classical compact-test Weil implication is then
needed to conclude RH. No part of (2) is established here.

An equivalent stronger-norm version can use ||H_s h|| instead of Q(h,h)
as the small parameter, after cap-only boundedness converts small energy to
small residual as in (3). An unshifted original form is essential: replacing
Q by Q-mu mass changes H_s and the near-null set, and detects a positive
physical eigenlevel instead of original nullity.

## Concrete actual anchor upgrade at 53/50

Pinned dependencies:

- CC119 at 5df347d3808ac3282864a657b7380e0f54bf4daa supplies the inherited
  physical guard eta=1/10^37 at a=53/50.
- CC37 report notes/REFLECTED_PACKET_BRIDGE_108_EFFECTIVE_NATIVE_REMAINDER_CC37_20261008.md,
  read at that same commit, blob a8a4ec58ebc43745d73630b97188cac1597b15ed,
  supplies the global archimedean remainder bound <8 and the rational
  prime/pole envelope construction.

CC37 recorded its cap result only through 21/20. Its SAME algebra extends
to 53/50 after a fresh exact exponential check:

    exp(53/50)<3, exp(53/25)<9.

Thus the active prime powers remain among 2,3,4,5,7,8, with Lambda(6)=0.
All six potential coefficients are safely bounded, keeping both orientations.
The inherited log/square-root enclosures give

    sum Lambda(n)/sqrt(n) < 12093/3740.

Both signed pole terms remain in the actual form; their combined operator
norm is bounded using 4 sinh(53/50)<16/3. Therefore

    ||R_53/50|| < 8+2(12093/3740)+16/3
                 =111079/5610 <20.                   (5)

No source channel or signed mixed term is omitted; (5) is an absolute
remainder norm, not an arithmetic vanishing estimate.

For every canonical h at this aperture, the two inherited inequalities are

    Q(h)>=eta||h||_2^2,
    Q(h)>=||h||_D^2-20||h||_2^2.

Take their convex combination with coefficient eta/(20+eta) on the second
inequality. The physical masses cancel exactly, yielding

    Q(h)>= eta/(20+eta) ||h||_D^2
          > 1/(21*10^37) ||h||_D^2 for h nonzero.     (6)

A non-strict common canonical guard is consequently

    1/(21*10^37).

This is a new explicit norm conversion from the published actual physical
certificate under the inherited native identification. It is not a fresh
whole-source integration, new aperture, source-defect eigenvalue, or Lean proof.
It gives a canonical starting anchor for (2) while retaining every historical
physical bound.

## What data this formulation still lacks

Signed physical source profiles now have a legitimate purpose: evaluate the
complete native outward pairing after canonical Riesz/projection attachment.
The full positive-source metric is no longer part of this particular
acceptance statement. Nevertheless the following remain mandatory:

- exact canonical norm and supported projection attachments for the tested
  near-null vectors;
- whole dual/operator error bounds outside finite retained coordinates;
- an actual estimate vanishing with native near-null energy for all old-positive
  windows and a cap-only positive enlargement step.

The existing 1.06 packet does not provide those universal bounds. Any finite
approximation error must also tend to zero at the required near-null scale.
Increasing a fixed finite frame without such a tail payment is insufficient.

There is no inference from compactness to (2). The exact rank-one native model
Q=I-N*N with N=(u,v), old domain span(e0), and fixed v=1/4 gives

    Q(e0,e0)=1-u^2 ->0,
    O e0=(0,-uv),
    ||O e0||^2 ->1/16.

It has the same compact native block structure and a genuine enlarged
crossing. It rejects automatic outward decay. It is a structural control,
not the literal original Weil arithmetic. Shifting the full mass moves its
old near-null level and must remain explicit.

## Fresh validation and next substantive task

scripts/validate_rpb108_rc5_native_anchor.py passes 30 fresh exact rational
checks: both new aperture exponential bounds, all prime logarithm and square-root
enclosures, the complete remainder arithmetic, the canonical guard conversion,
the persistent native crossing, and the complete mass-shift distinction.
The analytic archimedean constant and compact native framework are inherited;
those are not proved by the finite checks.

Next: test an identified actual prime/archimedean/pole correlation against
the native condition (2), with canonical projection and complete tails paid.
The metric-reconstruction prerequisite is removed from this route, but the
arithmetic no-contact content remains. Repeating conditional algebra or the
completed fixed-aperture sign is not credited as proving (2).

No actual outward modulus, new aperture, RH/F4 theorem, or Lean closure is
certified. CC119 and DNE53 positivity at 1.06 remains intact. Other refs and
historical files are preserved.
