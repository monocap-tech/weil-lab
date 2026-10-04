# RPB108: native absolute-envelope absorption obstruction

Base: research `d2c0353495e560e9f4c4178f3cbe9748b06fb021`.

## Definitions and scope

Write $M_a(ξ)$ for `rightLimitCompactWeilSymbolMathlib a ξ`, $w(ξ)$ for `logarithmicFourierWeight ξ`, and $E_a$ for `neutralActualZetaNativeLogError a`. A uniform absolute envelope is any real constant $C$ satisfying $|M_a(ξ)-w(ξ)|≤C$ for every real ξ. No minimality of $E_a$ is asserted or needed.

The previous certified scalar theorem gives $M_a(0)<0$; the existing logarithmic weight theorem gives $w(0)≥1$.

## Minimal theorem and proof

For every window $a$ and every uniform absolute envelope $C$,

\[
C\ge w(0)-M_a(0)>1.
\]

The left inequality is the lower half of the absolute bound at zero. The strict inequality uses exactly $w(0)≥1$ and $M_a(0)<0$. Consequently $E_a>1$. Since the existing pole-error constant $P_a$ is nonnegative, $K_a:=E_a+P_a>1$ as well. These statements use no zero simplicity, graph density, retained witness membership or arithmetic positivity premise.

The four additive Lean theorems are:

- `neutralActualZetaNativeLogEnvelope_zero_lower_bound`
- `neutralActualZetaNativeLogEnvelope_gt_one`
- `neutralActualZetaNativeLogError_gt_one`
- `neutralActualZetaNativeGardingError_gt_one`

## Exact consequence and limits

The existing Gårding inequality is $L(f)≤Q_{native}(f)+K_a m(f)$, with $L(f)=‖neutralLogWeightedL2 f‖²$ and $m(f)=‖f.val‖²$. The existing mass comparison is $m(f)≤L(f)$. Using only these two estimates gives

\[
Q_{native}(f)\ge(1-K_a)L(f),\qquad 1-K_a<0.
\]

Thus this direct absolute-error absorption does not certify native nonnegativity and cannot by itself close the background unit factor. A negative lower bound does not imply a negative value. This result supplies neither a supported negative packet nor a background-sign decision.

A stronger supported estimate $m(f)≤θ_a L(f)$ would make this particular route useful only after verifying a sufficient budget such as $K_a θ_a≤1$; no such estimate or budget is claimed here. Support-sensitive signed cancellation may offer a different route. All pole and selected-energy corrections must remain attached to the same graph vector.

## Validation

Lean 4.34.0; exact tested validation head `0e7ae7ae1edacbdc0699ffc71fe5184c838be30d`. [Actions run 37234509224](https://github.com/monocap-tech/weil-lab/actions/runs/37234509224) / job `111530848541` passed isolated 9176/full 9203 build jobs. All four theorem audits depend exactly on `[propext, Classical.choice, Quot.sound]`; unfinished/project-axiom and sorryAx gates passed. Tested module fetched and matched byte-for-byte. Restored `rpb108-actual-native-symbol-sign-verified-v1`; saved `rpb108-actual-native-envelope-obstruction-verified-v1`.

## Updated cursor/residue

At d2c0353, every uniform absolute native logarithmic envelope constant exceeds one, forced by the actual zero-frequency deficit. In particular the canonical NativeLogError and the existing Gårding mass-error coefficient are strictly above one. Combining only mass <= logarithmic norm squared with that Gårding estimate therefore gives a negative lower-bound coefficient, not native or background positivity. This closes the naive absolute-error absorption shortcut without deciding the supported integrated background form. Next arithmetic work must exploit support-sensitive cancellation or an improved supported mass-to-log estimate with its constants actually verified, while retaining cross-pole and selected-energy terms on the same graph vector. The finite-packet and mixed Gram obstruction criteria remain exact; no actual negative packet or uniform unshifted background positivity theorem is established. Retained same-vector source attachment or fresh concrete WD-T38 attained-unit-gain realization and endpoint-null custody remains independent. No full graph density, zero simplicity, spectral operator-domain membership or background positivity is assumed. FULL TRANSPORT CLOSED remains open. SOURCE is off the critical path.
