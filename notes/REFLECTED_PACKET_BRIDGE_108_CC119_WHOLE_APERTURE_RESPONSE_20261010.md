# CC119: joint source response closes whole aperture 1.06

The paid joint CC11/DNE3 response certifies the complete even Z56 block at the actual original high floor k=647/1000. Together with CC117's complete odd Z56 certificate, this covers all 112 original retained directions and the entire infinite F112 high space. The even physical gap is greater than 1.61e-37; the odd physical gap is greater than 2.00e-33. A simple common physical guard is 1/10^37.

This is an internal original-form positivity certificate at aperture a=53/50. Original analytic source, operator-domain/symmetry, parity decomposition and high-floor theorems remain inherited. It does not establish a global first-contact theorem, RH, F4 or Lean closure.

Parent CC118: `2cf582be5ee3a9f1833c37c1426504d35851be6b`.
Recovered read-only DNE52: `7d0d03400f78a3bf0d91d01c52a1b6d6a33e4bd4`.
Read-only Native NF61 observed at publication: `a119005c56e3ea39d80f228e5dff57e0297aab96`.
Only `research/rpb108-coupled-continuation` is written. All earlier artifacts are preserved.

## The new load-bearing source calculation

CC118 already authenticated the rank-14 pure-even-high frame Y=(Y_CC11,Y_DNE3), every native pairing, both diagonal response blocks, and both complete 56-row signed responses. It left precisely 33 mixed projected-source correlations unpaid. CC119 pays all 33:

U_ij = <P_F L Y_CC_i, P_F L Y_DNE_j>.

Two new coherent source computations use regular orders 360 and 400 and decimal precisions 760 and 800 respectively. Each evaluates all seven half-translation panels, complete endpoint logs, the regular kernel, signed poles and all six active prime powers in both orientations. Complete E112 coordinates are subtracted before paying the original source L2 errors. No sampled quadrature or true infinite inverse is used.

Each computation pays 47 selected upper entries: the 33 mixed entries and 14 fresh diagonal controls. The diagonal controls authenticate projected norms and overlap the previously certified diagonals; they do not replace the old diagonal blocks. Every replay paid interval is contained in its primary counterpart. Complete action profiles and source reports are archived losslessly with stored and decoded SHA256 custody. The source-only audit's standing-rank and whole-aperture fields describe the state before the response gate; the later response audit is the final CC119 state.

## One joint denominator, one fixed response

Retain the complete native matrix T from CC118 and define X=U/k-T. Assemble

N_joint = [[N_CC, X], [X^T, N_DNE]],

where N_CC and N_DNE are the literal already paid blocks; N_DNE uses DNE50's residual denominator divided by k. Concatenate the corrected complete signed responses W=[W_CC,E_DNE]. Every mixed entry is retained. Neither zeroing X nor summing separately optimized credits is used.

The joint denominator has a certified coefficient floor greater than 0.2346. A decimal finite solve proposes an exact rational 14-by-56 matrix H, frozen on the 10^-100 grid. Exact outward interval arithmetic accepts

S_H = Q56-G56/k + (WH+H^T W^T-H^T N_joint H)/k^2.

An independent entrywise replay expands all 3,136 response-credit entries directly, rather than reusing the producer's matrix-product grouping. Replay credit and complete comparison intervals nest inside the producer intervals. Frozen rational congruences and paid Gershgorin margins prove both complete even matrices positive. The producer's even coefficient floor exceeds 0.00646215.

With the authenticated packet physical mass m and projected-source trace g, the inherited Schur-to-physical conversion gives

gap_even >= min(floor(S_H)/(4*(m+g/k^2)), k/2) > 1.61e-37.

The final auditor also replays CC117's odd positive congruence and its physical conversion. Exact chart ranks and the retained/high physical decomposition are inherited through the authenticated CC117/CC116/DNE49 chain. Thus the complete retained rank is 112, the uncovered retained dimension is zero, and whole-aperture positivity is true at a=1.06. No additional finite inverse or original infinite inverse is certified or evaluated.

## What this establishes about the comparison with DNE

CC118 supplied one exact trial rejecting every convex mixture of the saved CC and DNE even comparisons. DNE52 additionally supplied a common negative trial for the saved DNE3 comparison and an optimized upper over every coefficient choice in the old CC11 family. Those obstructions did not exclude the joint family. Paying its mixed source block now yields a complete positive comparison and closes the one direction still uncovered by DNE52's 111-direction union.

This establishes a strict gain over those current paid bounds on this original aperture. It does not establish universal superiority over all correlated DNE response constructions: DNE itself uses residual-source information. CC117 had already demonstrated a strict collective gain over the plain scalar remaining-source comparison on the full odd packet.

No computational cost dominance is proved. The new step reused all packet sources and paid only the missing mixed block, but required fourteen source profiles in each precision run, 47 selected correlations per run, exact denominator/comparison arithmetic and independent audits. The two source jobs took about 979 and 1,041 seconds respectively, running concurrently. These are measured job durations, not a like-for-like cost benchmark against DNE. Fewer missing inputs do not alone prove a cheaper criterion.

## Recovery and reproducibility

DNE52's five original records are imported unchanged under `notes/cc119-source/`, retaining their original Git blob identities. Its proposed e116 extension remains unpaid and is unnecessary for this closure. Native NF61 was observed read-only; its commit describes target improvements with negative separate target minorants. No NF61 numerical input is consumed by CC119.

The terminology registration precedes the source and response uses. The optional all-coefficients obstruction script is provided for rejected future runs; it was not invoked here because the complete joint gate is positive. This is not a negative-vector claim.

Reproduce the source jobs with `DNE16_ORDER=360 DNE16_PRECISION=760` and `DNE16_ORDER=400 DNE16_PRECISION=800`, respectively, running `scripts/certify_cc119_mixed_source_correlations.py even --output` with the PRIMARY/REPLAY JSON paths. Then run:

```sh
python scripts/validate_cc119_mixed_source_correlations.py --output notes/data/RPB108_CC119_MIXED_SOURCE_VALIDATION_20261010.json
python scripts/certify_cc119_joint_even_response.py --output notes/data/RPB108_CC119_JOINT_EVEN_RESPONSE_20261010.json
python scripts/certify_cc119_joint_even_response.py --replay notes/data/RPB108_CC119_JOINT_EVEN_RESPONSE_20261010.json --output notes/data/RPB108_CC119_JOINT_EVEN_RESPONSE_REPLAY_20261010.json
python scripts/validate_cc119_joint_even_response.py --output notes/data/RPB108_CC119_JOINT_RESPONSE_VALIDATION_20261010.json
python scripts/pack_cc119_source_artifacts.py
```

Readers accept lossless `.json.gz.b64` fallback paths when raw source/response JSON is absent. The physical packet remains plain JSON for direct source reruns. The source audit passes 1,963 explicit exact checks; the joint response audit passes 12,562, for 14,525 fresh explicit checks. All six new scripts compile. The final custody record lists exact independent check counts and all published file hashes; inherited checks are not added to the fresh counts.
