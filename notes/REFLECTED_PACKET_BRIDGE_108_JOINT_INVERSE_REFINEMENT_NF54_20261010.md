# RPB108 NF54 — refine the remaining complete NF53 witnesses

Client date: 2026-10-09, America/Los_Angeles. File suffixes and ledger
`date_UTC` retain the 2026-10-10 UTC computation provenance.
Aperture: `53/50`. Starting NF53 commit:
`8f8be75830329df947e261fdc965dda3bf366bc7`.
Branch: `research/rpb108-phase-geometry-localization`.

NF54 appends one physical high direction per parity, selected from NF53's
new complete joint lower-bound witness. It preserves the original recovered
archives, joined columns P, exact 53-direction frame T53, and every inherited
high column. All conclusions use paid original native pairings and complete
physical source covariances through one shared original high inverse.

## Selection and complete physical domain

Set `Xi=(R,G)`, `R=PF LP`, `G=PF LT53`, and `kappa=207/1000`.
With `U=(A-kappa)H`, `C=H*(A-kappa)H`, `N=C+U*U/kappa`, and
`W=Xi*U`, selection uses the full joint response

`A0^-1 Xi z=Xi z/kappa-U N^-1 W* z/kappa^2`.

The NF53 witness z is divided by a rational upper bound for its original
physical norm. Selection uses the complete P and T53 coordinates on degrees
112..308 even and 113..307 odd, down-rounds midpoint response coordinates to
denominator `10^100`, projects off all inherited high columns with an exact
rational physical Gram, and normalizes with a rational upper norm. The frozen
coefficients and exact orthogonality are checked independently. Midpoint
selection does not establish any sign conclusion.

The enlarged high families have thirteen even and twelve odd columns.
The original form domain remains `f=P alpha+T53 beta+h`, `h in F112`.
The NF47 unshifted physical floor controls all remaining infinite high
directions. No finite truncation is substituted for that floor.

| Added certified pairings | even | odd | total |
| --- | ---: | ---: | ---: |
| Original native `Q(P,Y), Q(T53,Y), Q(H,Y), Q(Y,Y)` | 69 | 68 | 137 |
| Complete physical source pairings | 69 | 68 | 137 |

The complete original Xi Gram and native Gram of `(P,T53)` remain fixed.
All added high native/source Gram entries and joint crosses are assembled
together. Positive enlarged surplus C and denominator N establish the shared
inverse ceiling

`Xi* A^-1 Xi <= Xi*Xi/kappa-W N^-1 W*/kappa^2`.

Subtracting that ceiling from the original joint native Gram gives a
sufficient 56-direction joint lower matrix per parity.

## Precision, analytic payments and independent route

NF54 retains NF53's scoped 800-digit producer and 900-digit independent
validator, with moment cutoffs 1300 and 1400. The shared precision primitive
is unchanged and hash-pinned by the ledger. Explicit atanh, Machin pi and
Euler–Maclaurin tails remain paid. Grid-dependent caches are cleared during
the single precision switch in each fresh process.

Inherited 500-digit source intervals are promoted exactly to the current
grid. NF53's appended physical source is reconstructed at that grid with
its frozen retained midpoint projection; its certified physical error and
norm bound remain fixed. Historical matrix interval endpoints are read as
exact rationals. This preserves the physical analytic approximants, not just
their nominal coefficients. The new direction's native/source entries are
freshly certified. Moments depend on parity, cutoff and precision; source
cache keys bind the fixed polynomial, and independent action keys also bind
the validator and certificate.

The profiles retain the endpoint logarithm, signed pole, degree-320 regular
kernel, degree-40 pole approximation and all 13 original prime cells. With
`a=53/50`, the uniform analytic infinite payment remains

`eta=2a*4(106/125)^320/(1-106/125)+16(a/2)^41/41!`.

Native crosses pay `eta ||Y|| ||v||`. The retained frozen midpoint projection
pays `eta ||Y||+16 max halfwidth(low_source_coordinates)`; independent
coordinate enclosures must fit that payment. Every complete source covariance
pays `e_i n_j+e_j n_i+e_i e_j` using certified physical errors and approximant
norm bounds. No signed pole, prime cell, cross covariance or infinite
remainder is omitted.

The independent validator does not import the NF54 producer. It reconstructs
the source with the larger moment cutoff, integrates each original cell's
combined polynomial first, and checks every added native/source entry,
physical projection payment, exact high orthogonality, inverse positivity
proof, witness sign and original physical mass. Both routes share the explicit
precision primitive but use distinct grids and pairing assembly routes.

## Correlated gain and remaining gate

The validator certifies the rank-one inverse-reaction gain with exact
cancellation of the common Xi Gram. For `N+=[[N,t],[t*,s]]`, `W+=[W,w]`,
and `delta=s-t* N^-1 t > 0`, the gain matrix is

`(w-W N^-1 t)(w-W N^-1 t)*/(kappa^2 delta)`.

It intersects the old witness's directly enclosed new lower value with its
old value plus this correlated gain. Signed and null rank-one controls,
negative/null/positive joint controls, physical mass shifts, Hankel corners
and the original 13-cell mixed-log identity are checked. A positive gain
alone does not imply a positive complete matrix.

Both independent parity checks pass. The following decimal enclosures round
the exact correlated intervals outward:

| Normalized NF53 witness | even | odd |
| --- | --- | --- |
| Correlated inverse-reaction gain | `[2.6524,2.6530] x 10^-33` | `[9.0004,9.0005] x 10^-30` |
| Refined lower value | `[9.8950 x 10^-34,1.4261 x 10^-33]` | `[6.9621,6.9722] x 10^-30` |

Both inherited NF53 witnesses are lifted to strictly positive lower values.
The full even lower-matrix sign is **UNRESOLVED** at midpoint LDL pivot 11.
The odd matrix is **JOINT_LOWER_BOUND_REJECTED** by a new exact rational
witness, with independently certified original physical quotient enclosed
in `[-5.0499,-4.7618] x 10^-31`.

An additional exact sign-probe record examines all 56 even midpoint LDL
pivots, continuing past the first unresolved candidate. It freezes all 15
selected nonpositive-pivot rational directions, their original physical
masses and exact Fraction interval quadratic values against the certified
800-digit producer lower matrix. Every such enclosure spans zero. This
probe evaluates that recorded interval matrix; it does not reconstruct
additional sources or prove the sign of the entire matrix. The 900-digit
independent native/source/inverse validation is separately authenticated.
The first frozen even direction supplies a concrete next enclosure target.

Negative witnesses of
the sufficient joint lower matrix reject that bound; they do not establish
negative original Weil vectors. The original remaining whole gate is
`D-B S^-1 B* >= 0` in both parities, using the same high inverse for all
56 original joint sources.

The aggregate ledger authenticates compressed and decompressed SHA-256
hashes of the three recovered archives. NF48's literal byte-identical NF46
replay, NF47's physical floor and all historical vectors remain unchanged.
This checkpoint adds new records without editing historical files.

The next gate is to resolve that frozen even sign-probe direction with tighter
complete inverse/source enclosures and discharge the new odd rejecting
witness, then certify the full original Schur inequality in both parities.
Whole positivity at `53/50`, RH, F4 and Lean remain open. The highest certified
whole-aperture anchor remains `21/20`.

## Reproduction

With the authenticated originals in `nf24-inputs/Weil/`, run in fresh processes:

```sh
python scripts/certify_native_joint_refinement_nf54_106.py --parity even --output notes/data/RPB108_NF54_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf54_106.py --certificate notes/data/RPB108_NF54_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF54_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
```

Repeat with `odd` and `ODD`, then run
`python scripts/probe_native_joint_sign_nf54_106.py` followed by
`python scripts/summarize_native_joint_refinement_nf54_106.py`.

