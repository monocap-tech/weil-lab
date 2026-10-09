# RPB108 — NF30: enlarged even retained response correction

2026-10-09 UTC. Phase Geometry parent NF29 is
`50723e823db4d102a7b419deec433942d8376423`. Coupled CC72 was read-only
at `fd8ca0ab3800140bb192a512ec953f625c3bb53c`. No other or paused
branch is modified. Definitions are additive:
[NF30 terminology](../docs/TERMINOLOGY_RPB108_EXPANDED_RESPONSE_NF30.md).

## Result

The enlarged even two-direction sufficient matrix is rigorously positive
definite. The complete physical source square is reduced enough to pay
both the high response and the signed mixed determinant.

| Strict certified even quantity | NF29 | NF30 |
| --- | ---: | ---: |
| Response source square / native energy | (0.42957950,0.42957952) | (0.07870226,0.07870228) |
| Inherited floor budget | 0.207 | 0.207 |
| Response sufficient diagonal | negative | $(2.3433429,2.3433431)\times10^{-37}$ |
| Full sufficient determinant | negative | $(7.26550,7.40741)\times10^{-73}$ |
| Two-direction sufficient matrix | rejected | positive definite |

The new response energy lies in (3.78083067,3.78083070)e-37 and its
complete residual square in (2.97559951,2.97559970)e-38. Its signed
source covariance with v is positive, in (1.60580,1.60817)e-37; after
subtracting the floor response from the native mixed energy, the
sufficient off-diagonal is negative. Its sign is not asserted to be
that of the unknown true inverse-weighted covariance.

The native energy reduction is about 11.52%. The certified sufficient
scalar after eliminating the expanded response coordinate is greater
than 3.1004e-36. This is a coordinate Schur lower bound, not a claimed
whole-domain physical gap.

Together with the authenticated, unchanged odd NF29 block, exact
reflection parity gives a positive original four-direction retained
Schur restriction on span(x_even,w_even,x_odd,w_odd), with all original
high modes included. The retained responses remain exactly orthogonal
to their corresponding seeds. This is stronger than positivity of a
finite truncation, but it does not cover the other 108 retained
dimensions or prove the entire original form positive at53/50.

## Fixed additional correction

NF29's even response w_h preserves the original NF27 retained response
w, but its complete source-square/energy ratio remained above 0.42957
against the inherited floor budget kappa=207/1000. NF29's odd
two-direction infinite-high Schur restriction already passed.

NF30 selects only a new even high correction z on the 33 normalized
physical Legendre modes e116,e118,...,e180. Its fixed rational
coefficients are source coordinates of w_h divided by four, downward
rounded to denominator 10^100. The selector and certifier are separate
commands: no trial-selection result itself establishes a matrix sign.
The scale four is not an asserted inverse of the original high form.

The selected finite shell's original physical source-coordinate squares,
after uniform source-error payment, account for a fraction strictly in
(0.89466562,0.89466575) of NF29's complete response source square. Its
degree118 pairing agrees with the independent original signed N720/K620
native oracle authenticated in NF29's validation archive. The selected
correction has physical norm about 1.013115e-19.
This captured fraction is not assumed to be the amount removed by z.
The complete reconstructed corrected source charges all regenerated
H2 coordinates, other high-mode interactions and omitted source tails.

Set t=w_h-z. Its retained component remains exactly w. The original
NF26 corrected critical seed v is unchanged, as is the successful odd
NF29 family. A change of high lift is not merely a basis change of the
old trial space.

## Original energy and complete source proof

The new native energy and mixed energy are reconstructed by the exact
bilinear identities

\[
Q(t,t)=Q(w_h,w_h)-2Q(w_h,z)+Q(z,z),
\qquad Q(v,t)=Q(v,w_h)-Q(v,z).
\]

The old energies are authenticated NF29 native enclosures. Each new
pairing uses a complete reconstructed source and a tiny fixed high
polynomial, paying the appropriate product of physical masses and the
uniform source replacement error eta_unit. In particular,
Q(w_h,z) pays eta_unit ||w_h|| ||z||, Q(z,z) pays eta_unit ||z||^2,
and Q(v,z) pays eta_unit (1001/1000) ||z||. No unit-norm source energy
approximation is used to establish the near-critical native energy.
Separate reversed pairings Q(z,w_h) and Q(z,v) test paid bilinear
symmetry before the matrix comparison.

The complete physical Gram on (P_F Lv,P_F Lt) is integrated exactly
with outward rational polynomial, endpoint-log and endpoint-log-square
moments on all thirteen original translation cells. Every arch/prime/pole
cross is present. The regular kernel degree320, degree40 pole remainder,
and rational grid10^-500 are inherited unchanged. No numerical
quadrature or source sampling is a proof input.

The original retained coordinates of Lw_h come from authenticated native
entries through degree115. The retained coordinates of Lz are enclosed
by exact reconstructed-source moments and paid by projection
contraction. The physical residual error for t is bounded by

\[
(\|w_h\|+2\|z\|)\eta_{\rm unit}
+8\max_j \operatorname{radius}((P_E Lw_h)_j-(P_E\widehat Lz)_j).
\]

For each complete Gram entry the producer pays
eta_i N_j+eta_j N_i+eta_i eta_j, where N_i are reconstructed source
norm upper bounds. It checks original native and complete source Gram
positivity, replays NF29's v source square, and evaluates the full
signed sufficient matrix U=Q2-Gamma/kappa, not merely its diagonals.

## Verification and reproduction

The separate validator authenticates all prior inputs and NF29's
independent signed projection oracle. It replays the exact rational
selection rule, tiny-polynomial energy identities, reversed pairing
overlaps, complete physical Gram payments, matrix determinant and test
status. Exact positive/zero/negative collective crossing controls keep
the first diagonal positive on both sides of a genuine matrix crossing;
they test that directional success does not replace collective positivity.
The separate validator passed, including the original signed projection
overlap, exact trial rule, paid transpose checks, all Gram error payments,
native energy identities, determinant sign and unchanged odd sign.
Both proof scripts passed Python syntax compilation.

With the original NF24 native archives at the documented input paths:

```sh
python3 scripts/certify_native_expanded_response_nf30_106.py choose --output /tmp/nf30-trial.json
python3 scripts/certify_native_expanded_response_nf30_106.py certify --trial /tmp/nf30-trial.json --output /tmp/nf30.json
python3 scripts/validate_native_expanded_response_nf30_106.py /tmp/nf30-trial.json /tmp/nf30.json --output /tmp/nf30-validation.json
```

The fixed trial, certificate and validation JSON files separate selection
from proof and retain signed intervals and paid errors. All old input
hashes and the newly selected trial hash are recorded. The unchanged
odd block is authenticated rather than silently replaced.

The complete retained matrix, whole-domain53/50 positivity, true signed
inverse-weighted collective response and all-aperture continuation remain
open. Highest whole-domain anchor remains21/20. RH, F4 and Lean closure
are not claimed. Historical wording and paused fronts remain unchanged.

## Next frontier

NF31 should move from these successful response probes to a genuinely
collective retained family. The remaining 54 background directions in
each parity require their own complete source and signed couplings,
or a justified common high-lift construction with an entire matrix
bound. CC71's finite collective lifts are candidate inputs, not an
already certified complete-source matrix. A positive selected probe
cannot replace those remaining matrix obligations. Near-critical energy
must continue to use authenticated native entries or small-factor
bilinear identities, not unit-norm approximate source energy.
