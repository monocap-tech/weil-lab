# RPB108 DNE48: the complete computed packet closes by residual response

Mathematical parent DNE47: `da5b09e3b72b8e05e3daab5e37e6b3398a5558f8`.
Preparation checkpoint: `98bcb73cfc11a7126b57d720b71ce4e4b0bedd4c`.
Branch: `research/rpb108-direct-null-exclusion`. Definitions were registered
before load-bearing computation in
`docs/TERMINOLOGY_RPB108_DNE48_TRIAL_SOURCE_RESPONSE.md`. All historical
certificates remain immutable.

DNE48 certifies **all 44 even directions of the computed packet** by a paid
original inverse-response upper. Together with DNE46's complete odd packet,
this gives **88 retained directions**, up from 87, coupled to the **entire
infinite F112** space at aperture a=53/50. The original high floor remains
647/1000. The common physical guard remains **1e-37**. There are **24
uncovered retained dimensions**, all outside the computed packet.

This closes the packet direction that could not be paid by the refined
shell/global-prime-norm route. It does not certify whole-aperture positivity
or RH, and it does not evaluate the actual infinite inverse.

## 1. New original high-trial source actions

Append DNE47's three exact physical high trial polynomials Y to the frozen
44 even columns Z=(T4*S,X[0:40]). The new source packet has 47 columns;
these are **44 retained packet columns and three high trial columns**,
not 47 independent retained directions.

The original source engine directly reconstructs each action, including
the archimedean regular part and exact endpoint logarithms, both signed
pole orientations, and every active prime power 2,3,4,5,7,8 in both
translation orientations. It integrates the 138 new upper-triangle
correlations and preserves the old 44x44 source entries unchanged.
All 56 same-parity retained source coordinates are subtracted to obtain
complete original projected source Grams. There is no unaccounted high
degree or frequency cutoff and no sampled quadrature.

| Run | Regular order | Directed precision | Completed runtime |
| --- | ---: | ---: | ---: |
| Primary | 360 | 600 | 1050.9 seconds |
| Replay | 400 | 620 | 1160.9 seconds |

Each run uses the original analytic error
2 a (550/19)(106/125)^N + 3e-99, a 250-digit polynomial coefficient grid,
and 100-digit outward storage. Polynomial/log rounding and complete source
Gram errors are paid. Both runs finished, with all seven panels checkpointed.
The packed archives are lossless deterministic gzip/base64 copies of their
raw JSON bytes. Decoded hashes are recorded in the validation and custody.

For the three new trial actions, also compute all 91 even physical source
coordinates through degree180. These coordinates permit direct original
native pairings against the existing 44 columns and the three high trials.
Only the first 56 coordinates enter the F112 projection. Paying the native
pairing error by the source L2 error times the exact target norm upper
avoids reconstructing a high action by subtracting two large scaled actions.

The independent source audit passes **25,973** new exact rational checks.
It authenticates the original helpers and passing DNE44 audit, reconstructs
the exact47-column physical input, checks every projection and source error
payment, verifies the literal old-block identities, and checks primary/replay
enclosures and complete trial coordinates. Inherited checks are not added
to this new count.

## 2. Evaluate the full residual response matrix

Let L=L_F112>=kI, k=647/1000; f=P_F112 L_original Z. The validated new source
Gram supplies G=f*f, B=f*(LY), and D=(LY)*(LY). The new complete trial action
coordinates supply M=Z*L_original Y=f*Y and A=Y*LY, with original errors paid.
Every entry of these 44x3 and 3x3 matrices is saved as a rational interval.

Define E=B-kM and W=D-kA. A fresh positive congruence certificate proves
W>0. Its certified coefficient floor is approximately 1.05569739919. A
numerical solve only proposes a 3x44 coefficient matrix J; it is frozen on
an exact rational grid 10^-25. No numerical sign is used as proof.

For r=f-LYJ, the original response identity and residual estimate give

    f*L^(-1)f = MJ + J*M* - J*AJ + r*L^(-1)r
              <= MJ + J*M* - J*AJ + r*r/k.

Hence the original finite Schur matrix is bounded below by

    R/k,  where R = kN-G + EJ + J*E* - J*WJ.

DNE48 independently certifies the **complete 44x44 R>0**, including all
mixed entries. It does not certify only the last direction's diagonal,
and it does not substitute an ideal unmeasured inverse for the paid J.
The resulting original finite Schur coefficient floor is approximately
**0.006900527808349515** in the fixed packet coordinates.

The previous scalar comparison kN-G had inertia (43,1,0) in the even packet.
Its negative comparison direction was an inconclusive sufficient-bound
failure. The new matrix R is strictly positive: the three original high
trials supply enough paid response credit to remove that failure while
keeping the original scalar high floor fixed.

## 3. Retained rank, physical gap, and inclusion

The even Z packet has exact retained rank 44, authenticated by DNE46's
invertible positive/negative comparison chart and retained-rank audit.
A strictly positive full response budget therefore proves positivity on
all44 projected retained directions together with the infinite F112 space.
DNE46's 43-direction even positive embedding is contained in the full
44-column packet algebraically. The complete 44-direction odd packet and
its infinite-high coupling are retained from DNE46. Thus the full prior
87-direction space is included.

| Parity | DNE46 retained rank | DNE48 retained rank | Uncovered inside the computed packet |
| --- | ---: | ---: | ---: |
| Even | 43 | 44 | 0 |
| Odd | 44 | 44 | 0 |

The new even physical gap pays the complete packet mass and original source
trace, using the true inverse norm bound only for the conversion from
coefficient energy to physical norm. If d is the certified R coefficient
floor, the saved lower is

    min{ (d/k)/(4*(physical_packet_mass + source_trace/k^2)), k/2 }
      = approximately 1.7247575800292447e-37.

The inherited odd lower is approximately 1.8069395448934553e-33. Both exceed
the common physical guard **1e-37**, now valid for the 88-direction span
plus the whole infinite high space.

The independent response audit passes **10,264** new exact rational checks.
It reconstructs every original trial native pairing and its error payment,
all E and W entries, the positive W certificate, the frozen rational J,
every full response and mixed entry, the full positive congruence, inherited
rank/inclusion evidence, and the exact all-high physical gap. The combined
new check count is **36,237**, all PASS.

## 4. Reproduction

Run from the repository root. The two source commands may run as independent
processes, and must finish before packing and validation.

```sh
DNE16_ORDER=360 DNE16_PRECISION=600 python scripts/certify_dne48_trial_source_Gram.py even --output /tmp/dne48_even_360.json
DNE16_ORDER=400 DNE16_PRECISION=620 python scripts/certify_dne48_trial_source_Gram.py even --output /tmp/dne48_even_400.json
python scripts/pack_dne48_source_archives.py /tmp/dne48_even_360.json /tmp/dne48_even_400.json
python scripts/validate_dne48_trial_source.py notes/data/RPB108_DNE48_TRIAL_SOURCE_20261010.json.gz.b64 notes/data/RPB108_DNE48_TRIAL_SOURCE_REPLAY_20261010.json.gz.b64 --output notes/data/RPB108_DNE48_TRIAL_SOURCE_VALIDATION_20261010.json
python scripts/certify_dne48_residual_response.py --output notes/data/RPB108_DNE48_RESIDUAL_RESPONSE_20261010.json.gz.b64
python scripts/validate_dne48_residual_response.py notes/data/RPB108_DNE48_RESIDUAL_RESPONSE_20261010.json.gz.b64 --output notes/data/RPB108_DNE48_RESIDUAL_RESPONSE_VALIDATION_20261010.json
```

Six scripts compile. All source jobs and the final validation pipeline
finished. The preparation note remains a historical pending-computation
checkpoint; this validated result supersedes its pending status additively.

## 5. Remaining original task

Of the 112 retained dimensions, **24 remain uncovered**,12 in each parity,
outside Z's current 40 frozen remainder columns. Their complete original
source correlations and mixed response bounds remain to be constructed or
bounded collectively. The validated trial actions can be reused; their
correlations with any added even packet columns must also be paid.

The high floor is unchanged at .647; the new progress is directional original
response control, not another global prime norm estimate. Whole-aperture
positivity at 1.06, first-contact exclusion, evaluation of the actual infinite
high inverse, RH, and Lean remain open. No original negative or null vector
is asserted. Other branches have not been altered.
