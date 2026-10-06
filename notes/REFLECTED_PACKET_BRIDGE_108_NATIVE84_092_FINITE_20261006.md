# RPB-108: full 84-vector native restriction certified at 23/25

The aperture is a=23/25 and the physical interval is [-a,a]. The finite
restriction uses the 84 physical L2-orthonormal vectors
sqrt((2n+1)/(2a)) P_n(x/a), for degrees n=0 through 83. The symbol tau denotes
a lower bound for this finite quadratic form in squared physical L2 norm.
The complete complement consists of physical vectors orthogonal to all
84 retained vectors. Finite coercivity alone does not decide the form on
that complement or its mixed coupling to the retained vectors.

The matching native calculation and repeat are byte identical. The repair
uses exponential order 260 and Bernoulli order 240 only at this aperture,
400-digit interval arithmetic, gamma order 20 and 220-term logarithm
bounds. Maximum physical entry width is approximately
1.8524531617125942e-39, strictly below the unchanged required limit 10^-35.
All full and shifted finite pivots are positive. The certified finite
physical coercivity is

    tau = 1/524288000000000000000000.

The native finite output SHA-256 is
`0bc3c388e8dafc480329e08cd650702852a8ea246e175a6f4dd37a2779c8cdbd`.
The outward compact certificate uses grid 10^-80; it repeats byte for byte
and contains all 7,056 original physical intervals. All 42 even and 42 odd
shifted pivots pass, exact reflection parity holds and the negative
control is rejected. Its SHA-256 is
`05469e303ac3edcf2950e4f1b8912e6252596076fd77fe0054f41889fd3f8e97`.

An independent persisted audit verifies the complete raw checkpoint's
constructor hashes and checks all 7,056 raw-to-physical entries using exact
rational interval arithmetic and integer square-root bounds. It checks
all compact inclusions, the native width and the compact/hash/sign custody.
The audit itself repeats exactly. The complete raw checkpoint is retained
in the preceding latest-repeat-row checkpoint; the normalized full output
is recoverable by running the native wrapper on that checkpoint. Its hash
is recorded above, and the accepted compact intervals are stored directly.
The earlier 83-row primary snapshot remains an intermediate record.

Prime powers are exactly 2,3,4,5, with Lambda(4)=log(2). The source certificate
at the same aperture already repeats exactly with source-map error below
1487/10^39. The independently audited complete complement bound remains
626973/1000000 physically and 9/100 logarithmically. These matching inputs
now feed two fresh full nine-panel residual Gram computations. Their
checkpoints bind the source, native compact certificate, constructor,
geometry, Hankel arithmetic and codec hashes. The endpoint-log Gram is
complete in both runs; support-panel integration is underway. No earlier
aperture's Gram checkpoint is reused.

This closes the finite restriction and its outward compact custody at
23/25. The complete source residual Gram and corrected Schur sign remain
pending. Whole-domain positivity is still certified through 91/100 only.
F4, full transport, global endpoint exclusion and historical attachment
remain open. The separate global-lane work is preserved. Lean and workflows
are unchanged.

## Custody

- `notes/data/RPB108_PRIME5_MATRIX84_092_COMPACT80_20261006.json`
- `notes/data/RPB108_PRIME5_MATRIX84_092_VALIDATION_20261006.json`
- `scripts/validate_native_prime5_matrix84_092.py`
- Complete raw recovery input:
  `notes/data/RPB108_NATIVE84_092_LATEST_REPEAT_ROW_CHECKPOINT_20261006.json.gz`
- Matching source:
  `notes/data/RPB108_PRIME5_SOURCE84_092_CERTIFICATE_20261006.json`
- Matching complement:
  `notes/data/RPB108_PRIME5_DEPTH6_COMPLEMENT84_092_CERTIFICATE_20261006.json`

The definitions in
`docs/TERMINOLOGY_RPB108_NATIVE_ROW_RECOVERY_092.md` retain the distinction
between a raw checkpoint and the final native certificate.
