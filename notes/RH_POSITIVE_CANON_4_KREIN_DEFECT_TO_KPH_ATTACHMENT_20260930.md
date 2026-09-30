# RH-POSITIVE-CANON-4 — Krein-defect to KPH attachment audit

Date: 2026-09-30
Repository: monocap-tech/weil-lab
Branch: investigation/rh-positive-canon
Parent: RH-POSITIVE-CANON-3

Status: COMPLETE / NO DIRECT C_ZP->KPH COMPRESSION / EXACT COMMON RAW CAUCHY CARRIER FOUND / FINITE SELECTED BRIDGE IMPOSSIBLE / ATTACHMENT SEAM TYPED / RH NOT PROVED

## 0. Mission

Start from the common off-RH Krein defect

  Theta_xi = e^{i beta} B_Z/B_P,

its signed atom decomposition

  B_P F_eta
  =
  const_eta
  [ k_{bar eta}^{B_Z} - k_{bar eta}^{B_P} ],

and the cross-model operator

  C_ZP
  =
  P_{K(B_Z)} | K(B_P).

Compare this with the selected KPH reciprocal-Cauchy carrier

  (C_F)_{jk}
  =
  1/(lambda_j-lambda_k),
  j != k,

with KPH(F)=sigma_min(I+C_F).

The objective is to determine whether KPH is an exact finite compression, Schur complement, divided difference, or other native projection of the common Krein defect.

## 1. The natural finite Cauchy matrix on the Krein side is not C_F

The Suzuki/Emmel route produces bounded q-samples at reduced B_Z zeros q:

  C_psi(q)
  =
  sum_gamma
  m_gamma hat psi(gamma)/(q-gamma).

SEAM-5D identifies the exact associated Cauchy-de Branges sampling matrix

  M_{q,gamma}
  =
  m_gamma/(q-gamma),

with:
- row index q in the reduced +1 divisor Z(B_Z);
- column index gamma in the zeta-zero divisor.

By contrast, KPH uses

  C_F(lambda_j,lambda_k)
  =
  1/(lambda_j-lambda_k)

with both row and column indices inside one selected zeta packet F.

Thus the natural finite matrices differ before any metric question:

  Krein/CdB:
    (+1 divisor) x (zeta divisor),

  KPH:
    (selected zeta packet) x (selected zeta packet).

No retained theorem identifies the +1 divisor with the selected packet or turns M_{q,gamma} into C_F by an exact finite Schur/Feshbach compression.

## 2. Finite selected recovery from the Krein q-samples is algebraically impossible

SUZ-BOMB-BRIDGE-0 gives the exact obstruction.

A finite linear combination of q-samples has zero-coordinate multiplier

  r(gamma)
  =
  sum_j a_j/(q_j-gamma).

To reproduce a finite selected marker, r(gamma) would have to vanish at every unselected zeta zero while remaining nonzero on the selected packet.

But a nonzero rational function with finitely many poles has only finitely many zeros.

Since the unselected divisor is infinite, this forces r identically zero.

Therefore:

  no nonzero finite q-sample combination
  can isolate a finite selected zeta packet.

This rules out the most direct finite selected bridge from the C_ZP/q-sample carrier to the packet-native KPH carrier.

It also rules out any finite invertible mixing of those q-samples as a selector-preserving repair.

## 3. Infinite inversion does not solve the KPH attachment automatically

Infinite recovery of a selected zero coordinate from the full q-sample family is exactly the Cauchy-de Branges completeness/inversion problem isolated by SEAM-5D/6.

That problem is not solved in the natural zeta topology.

Even if it were solved algebraically or in the auxiliary CdB norm, KPH would still require the selected packet's native leverage/barycentric metric.

SEAM-5D explicitly separates:

1. infinite Cauchy sampling inversion;
2. transfer from the auxiliary CdB norm into Suzuki H_0.

The KPH route adds another metric layer beyond that:

3. transfer into the selected packet leverage/KPH metric.

So an infinite q-sample inverse is not itself a KPH theorem.

## 4. The exact common object is lower-level: raw exponential/Cauchy response

RH-LOTUS-INTERFACE-2 already provides the exact same-ray identity.

For a selected coefficient vector v on a packet F,

  E_v(tau)
  =
  sum_j v_j e^{-i rho_j tau},

and

  R_v(w)
  =
  sum_j v_j/(w-rho_j).

On the common half-plane,

  R_v(w)
  =
  -i int_0^infty e^{i w tau} E_v(tau) d tau.

Thus the common Krein/Weil and KPH constructions meet exactly at:

  selected zero-exponential carrier
  <-> one-sided Cauchy/Laplace response.

This is stronger than mere shared divisor labels.

It is also weaker than a native operator bridge.

## 5. KPH itself is an internal selected-packet Cauchy geometry

G2C-6 fixes the packet-native object:

  C_F(j,k)
  =
  1/(lambda_j-lambda_k),

  H_F
  =
  J(I+C_F),

  KPH(F)
  =
  sigma_min(I+C_F).

R83/G2C give the exact barycentric similarity

  A_F^poly
  =
  B_F(I+C_F)B_F^{-1},

and the exact generalized barycentric metric removes the spurious condition-number loss.

Therefore KPH is not missing a representation theorem.

Its native finite packet geometry is already exact.

What is missing is why an actual off-RH Krein defect, after selection and support/metric restriction, must enter a KPH-dangerous direction.

## 6. C_ZP and C_F differ in operator type

The mismatch is not merely notation.

C_ZP:
- global cross-model projection;
- bounded contraction;
- acts from K(B_P) to K(B_Z);
- native question is cross-model angle / corona stable coprimeness;
- retains the whole divisor through model-space structure.

C_F:
- finite packet reciprocal-Cauchy matrix;
- skew-symmetric before Krein symmetrization;
- acts on selected packet coefficients;
- native question is the minimum singular margin of I+C_F;
- can become large/singular under packet collision and is handled by barycentric/Feshbach reblocking.

No retained exact intertwiner preserves:
- the selected packet;
- the finite marker;
- the KPH leverage metric;
- and the C_ZP model-space norm/angle.

Hence:

  C_F is not presently a finite compression or Schur complement of C_ZP
  in a custody-preserving sense.

No impossibility theorem for every conceivable nonlinear/common-parent transform is claimed.

## 7. Exact response-level attachment already known

The selected KPH eigenchannel has an exact completed-zeta scalar representation.

For a KPH channel v, provenance gives:

  r_v(z)
  =
  sum_j v_j/(z-lambda_j),

and, on the zero-moment defect channel,

  v^T Omega^Xi
  =
  - sum_{mu notin F} m_mu r_v(mu).

At an exact defective null, one gets the global cancellation

  v^T Lambda^Xi
  +
  sum_{mu notin F} m_mu r_v(mu)
  =
  0.

Therefore the KPH side is already attached to the actual full divisor through the same rational response species.

This still does not identify C_F with C_ZP.

It shows that both descend to Cauchy/resolvent observables on the same global zero-exponential substrate.

## 8. The actual attachment seam

The missing bridge is now exactly typed.

Starting from the common raw carrier, one needs a theorem transporting:

  global Krein/Hardy defect information
  or cross-model angle information

into:

  selected packet KPH leverage geometry

while preserving:
- selected packet identity;
- dangerous-channel identity;
- compact/support jurisdiction where relevant;
- native leverage/barycentric metric;
- worst-packet quantifiers.

Equivalent acceptable forms include:

1. a selected compression theorem mapping the global signed model-space defect to the packet Cauchy pencil with quantitative metric control;
2. a common parent operator whose Krein compression is C_ZP and whose selected finite Feshbach compression is I+C_F;
3. a same-ray response theorem that turns a global/model-space defect bound into KPH softness or safety on the selected packet;
4. a direct actual-zeta theorem bypassing the carrier bridge and proving the KPH floor.

No retained theorem supplies 1-3.

## 9. Relation to prior same-ray and global-source stops

This CANON-4 result is consistent with two prior terminal statements:

- SUZ-BOMB-BRIDGE-0:
  common raw exponential carrier exists, finite selected q-sample bridge is impossible, infinite bridge needs new completeness plus metric transfer.

- RH-LOTUS-INTERFACE-2:
  selected P/Krein-like activation and Q rational response share an exact raw exponential-Cauchy identity, but support/native metric transfer and Q channel alignment remain open.

Thus CANON-4 does not discover a hidden old compression.

It unifies these stops under the RH-positive-canon question.

## 10. Determination

CANON-4 establishes:

- KPH is an exact finite compression of C_ZP under current custody: NO;
- KPH is an exact Schur complement of C_ZP under current custody: NO;
- KPH is an exact divided-difference of C_ZP under current custody: NO;
- the natural finite Cauchy matrix on the C_ZP side is M_{q,gamma}: YES;
- M_{q,gamma} has the same row/column indexing as C_F: NO;
- finite q-sample mixing can isolate the selected zeta packet: NO / exact algebraic obstruction;
- infinite q-sample recovery is already a parked new Hilbert-topology theorem: YES;
- both sides share an exact raw exponential/Cauchy response carrier: YES;
- KPH is already exactly attached to a completed-zeta complement response on its selected channel: YES;
- a custody-preserving global-Krein to selected-KPH native metric transfer is known: NO;
- the missing KPH attachment edge is now precisely typed as selected compression/native-metric transport: YES;
- RH proved: NO.

## 11. Next cursor

RH-POSITIVE-CANON-5 / COMMON-PARENT OPERATOR TEST

Mission for next pass only:

1. search the already-custodied signed paired-divisor response tensor / explicit-formula operators for a common parent of:
   a. the global Krein cross-model defect; and
   b. the finite packet KPH Cauchy pencil;
2. require exact projections/compressions with native metrics, not thematic similarity;
3. test whether C_ZP and I+C_F are two reductions of one operator before support/selector loss;
4. if no common parent exists in current custody, stop the unification route and record the attachment as genuinely new theorem input.

Do not reopen generic BRS/CdB inversion in CANON-5.

RH remains unproved.
