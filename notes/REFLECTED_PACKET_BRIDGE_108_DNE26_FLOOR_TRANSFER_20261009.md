# RPB108 — DNE26: NF38's unchanged selected frame passes the available high floor

Definitions precede use in [DNE26 terminology](../docs/TERMINOLOGY_RPB108_DNE26_FLOOR_TRANSFER.md).
Parent DNE25: 103e2bb998790f0e2f30c591c9451996858561f0.
Read-only Phase NF38: d84bc1079b44bb6d8d724945354c7334c29e6eaf.
Read-only Coupled CC79: dd93e5cc7d003d44cdc240c5710f4c253dc1346f.
Only research/rpb108-direct-null-exclusion is written.

## Result

The fixed rational joint map selected in NF38 passes with DNE17's
already certified original infinite high floor 11/25. No correction
direction, coefficient, native energy or source Gram is changed.
Both original three-column restrictions include every vector in F112.

| Paid quantity | Even | Odd |
| --- | ---: | ---: |
| A smaller floor already sufficient for this selected frame | 0.30 | 0.25 |
| Available original F112 floor | 0.44 | 0.44 |
| Scaled sufficient positive margin g | >0.147051 | >0.149641 |
| Original full-high physical gap | >1.47051e-35 | >1.49641e-31 |
| Reported physical gap guard | 1e-35 | 1e-31 |
| Three-column native source contraction credit | 0.01 | 0.06 |

NF38's universal rejection at 0.207 stays valid. It is not a universal
rejection at 0.44: this unchanged selected frame is now an explicit
passing member of the same two-direction family. Passage of one member
does not mean that every correction functional passes.

The retained components are the same x,w,u32 already included in
DNE23's Z8. Thus DNE26 adds no retained directions and does not enlarge
the eight-direction certified plane. It supplies new passing source
packets for a different high lift, and resolves the old-floor family
obstruction for that chosen lift using an existing independent theorem.
Whole 1.06 positivity and the remaining 104-dimensional Gram stay open.

## Exact source transfer

The two full NF38 source certificates and two frozen selection trials
are imported byte-exact, in lossless gzip/base64 custody. The consumer
authenticates their decoded SHA256 hashes and the existing DNE22
certificate. NF38's original native and complete source matrices retain
the endpoint logarithms, N320 regular kernel, paid pole tail, thirteen
original translation cells and every signed source cross. Their source
errors and native errors are inherited; their expensive producers are
not rerun in this turn.

The same original sources give

    U_k=Q-Gamma/k, k=11/25.

Each matrix entry is enclosed by exact rational subtraction. Slightly
different rounding orders in symmetric source entries are reconciled by
intersecting their valid overlapping intervals, not by discarding an
uncertainty or a covariance. Both parities have strictly positive paid
rational congruence/Gershgorin margins using DNE22's fixed scales.
The same test also passes at 3/10 even and 1/4 odd. These smaller numbers
are sufficient thresholds, not the minimal possible required floors.
They are legitimately supplied by the independently stronger 11/25
original high theorem.

The NF38 universal rational witness remains strictly negative on the
SAME selected frame at k0=207/1000, and becomes strictly positive at
11/25. This is an exact paid quadratic calculation, not a floating
eigenvalue diagnosis. The selected native/source packet is held fixed
throughout. Estimator failure at the old floor never implied original
negativity; the new passage illustrates that distinction directly.

## Physical norm and native source credit

NF38 supplies physical norm upper bounds for the frozen base columns.
The two imported high polynomials have exact rational coefficients,
positive mass, and exact zero physical inner product. For selected joint
coefficients C, the new norm upper bound is

    m_i=base_mass_i+sum_j |C_ji| sqrt(||z_j||^2).

This bounds the actual selected polynomial without pretending that its
retained and high coordinates are an orthonormal three-column frame.
Source diagonal upper bounds give b_i=m_i+sqrt(Gamma_ii_upper)/k.
Original high square completion and weighted Cauchy give

    physical_gap >= [sum_i (s_i b_i)^2/g+1/k]^-1.

All square roots are enclosed outward on rational 160-digit grids and
replayed at 200 digits. Every original high vector is included; there is
no high truncation in this conclusion.

The native comparison g diag(s_i^-2)>=(c/k)Q is separately checked by
strict rational scaled row margins, with c=1/100 even and c=3/50 odd.
Consequently this selected frame satisfies Gamma<=(k-c)Q. These are
new THREE-column credits. Applying them to the FOUR-column DNE25
criterion would additionally require paid native/source interaction
with the low mode. That interaction is not established here. DNE23's
eight-direction theorem remains on its original frame and is untouched.

## Validation and controls

Primary and higher-precision consumers each pass 39 explicitly counted
outer rational assertions; the symmetric interval overlap and root
helper checks are additional. The separate validator passes 432 checks:
authenticated inputs, 248 flat complete mixed quadratic tests, 162
nonorthogonal physical/high-completion tests, replay comparisons, the
old/new floor witness signs, three genuine original crossings and three
whole-mass positive-level controls. Both scripts compile.

A control has native retained identity, projected source square 1/4
and actual high diagonal one. The SAME positive original form rejects
the 0.207 coarse floor and passes the 0.44 floor. Varying the actual high
diagonal through 1/5,1/4,1/2 separately crosses negative/null/positive
original Schur sign. Whole-mass shifts of an exact rank-one null matrix
give positive ground levels; subtracting the shift only from its retained
block misses those nulls. These controls are abstract, not original Weil
countermodels.

## Remaining interface

DNE26 shows that enlargement of NF38's correction span is not required
to pass the named selected three-column sufficient test once the
available 0.44 floor is used. It does not rule out such enlargements
being useful for sharper response or for the full remaining frame.
NF38's fixed-0.207 universal theorem and CC79's reduced-packet acceptance
windows remain valid under their stated hypotheses.

The next arithmetic requirements remain complete collective remainder
sources and their energy-normalized reaction. One can use DNE25's paid
four-column budget on its original tested frame, or first certify the
low-mode border for these new three-column sources before recomputing a
four-column credit. Neither may be inferred from the improved diagonals.

No source/integration branch is changed. Global actual-null exclusion,
whole 1.06 positivity, full retained inverse response, all-aperture
continuation, RH/F4/full transport and Lean stay open. The results are
outward computational consequences of authenticated source packets and
inherited analytic high theorems, not Lean proofs.

## Reproduction

```sh
python3 scripts/certify_dne26_floor_transfer.py notes/data/RPB108_DNE26_NF38_EVEN_INPUT_20261009.json.gz.b64 notes/data/RPB108_DNE26_NF38_ODD_INPUT_20261009.json.gz.b64 notes/data/RPB108_DNE26_NF38_EVEN_TRIAL_20261009.json.gz.b64 notes/data/RPB108_DNE26_NF38_ODD_TRIAL_20261009.json.gz.b64 notes/data/RPB108_DNE22_PROBE_PLANE_CERTIFICATE_20261009.json --output /tmp/dne26.json
```

Replay with --digits 200 and a separate output. The validator takes the
two outputs, the even and odd encoded source inputs, and its output path.
The imported complete-source producer is not needed for this arithmetic
consumer; reproducing original integration requires NF38's authenticated
archives as documented in its original note.
