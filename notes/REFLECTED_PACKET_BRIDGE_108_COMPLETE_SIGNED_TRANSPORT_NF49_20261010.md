# RPB108 NF49 — complete signed remaining sources and joint high transport

Date: 2026-10-10 UTC. Aperture: `53/50`.
Starting Native Source checkpoint: NF48,
`6847ef8c2501682d60d497043f510987dd70d93b`.

## Fixed objects and original input custody

NF48 recovered and authenticated the original NF17–NF19 Library archives and
reproduced unchanged NF46 selection, certification and independent validation
byte-for-byte. NF47 had already discharged the original unshifted physical
F112 floor `A >= (207/1000) I`. NF48 certified the finite remaining native
matrix C53 and all signed native joined couplings B0 in both parities.

NF49 keeps exactly the same P columns, T53 frame and eight even / seven odd H
columns. It supplies the missing complete source data and tests one assembled
56-direction high-condensed lower matrix per parity. Original archive bytes,
all prior vector coefficients and historical records are unchanged.

The three decompressed original SHA-256 values remain:

| Original archive | Decompressed SHA-256 |
| --- | --- |
| E112 | `f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81` |
| Boundary112–113 | `da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee` |
| Boundary114–115 | `0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad` |

## Complete original source data

Write `R=PF L P`, `G=PF L T53` and `U=(A-kappa)H`, where
`kappa=207/1000` and PF is the original physical orthogonal projection off
degrees 0–111. No source is projected onto a finite list of high modes.

The full physical source profiles retain the analytic endpoint logarithm,
the signed pole polynomial, the original regular archimedean kernel and all
13 prime translation cells. The regular kernel truncation remains degree320
and the pole approximation degree40. Their infinite remainders are paid by
the original uniform physical source error:

`eta_unit = 2a * 4(106/125)^320/(1-106/125) + 16(a/2)^41/41!`.

For each remaining column `t_i`, its exact signed retained source coordinates
come from the authenticated original native entries. The new physical error
is `eta_unit ||t_i|| + 8 max halfwidth(retained_source_coordinates_i)`.
The factor 8 bounds sqrt(56). P and H use their authenticated original physical
source errors; their unchanged norms and coordinates are reconstructed from
the historical definitions.

The computation pays every entry in the following table:

| Signed source data | even | odd |
| --- | ---: | ---: |
| Symmetric `G*G` | 1,431 | 1,431 |
| `G*R` | 159 | 159 |
| `G*PF L H` | 424 | 371 |
| Total source entries | 2,014 | 1,961 |

There are 3,975 source entries in total. The additional 795 signed native
`Q(T53,H)` couplings pay the original high-source coordinate errors. The
surplus crosses are assembled as

`G*U = G*PF L H - kappa Q(T53,H)`.

For reconstructed source norms `n_i,n_j` and physical errors `e_i,e_j`, every
signed source cross pays `e_i n_j + e_j n_i + e_i e_j`. The norm bound for an
inherited P or H approximant is its certified original norm upper plus its
physical error. Signed midpoints are preserved before these symmetric error
payments; no off-diagonal source cross is discarded.

## One joint high inverse ceiling

The existing high surplus matrix and source Gram are

`C=H*(A-kappa)H > 0`,

`U*U=GH-2kappa QH+kappa^2 MH`,

`N=C+U*U/kappa > 0`.

The form inequality

`A0=kappa I+U C^-1 U* <= A`

implies `A^-1 <= A0^-1`. For all 56 original sources simultaneously,
`Xi=(R,G)` and `W=Xi*U`, Woodbury gives

`Xi* A^-1 Xi <= Xi*Xi/kappa-W N^-1 W*/kappa^2`.

NF49 constructs this full matrix, with all paid native/source crosses, and
subtracts it from the original native Gram of `(P,T53)`. Its upper-left
three-by-three interval block is checked byte-for-byte against the unchanged
NF46 even / NF45 odd fixed joined lower block. The remaining blocks are
assembled through this same inverse ceiling. The finite native elimination
from NF48 is not separately combined with a fixed-packet high response.

This is a sufficient Loewner lower matrix. A positive matrix in both parities
closes whole-aperture positivity. A negative value of this lower matrix only
rejects the selected minorant proof; it does not determine the original form's
sign. The exact original condition remains the same joint high-condensed
`D-B S^-1 B* >= 0` from NF47.

## Arithmetic and independent validation

The producer applies Hankel moment matrices by exact signed integer
convolution, followed by outward rounding on the original 500-digit grid.
GMP optionally accelerates unsigned integer multiplication; a tested exact
Python-integer fallback computes the same products. The C helper performs no
floating arithmetic or sign decisions. Signed convolution controls include
large coefficients, negative entries, zero products and the fallback path.

The moment adjoint preserves global polynomial/log moments and every cell's
signed terms. Five end-to-end Gram checks per parity use the unchanged
historical pairwise integration formula on diagonals, signed remaining
crosses and joined/high crosses.

The independent validator does not import the NF49 certifier. It rebuilds
the original physical columns and all source profiles with moment cutoff1200
(producer1100), reconstructs the exact T53 constraints independently, and
integrates each translation cell's **combined** polynomial source first. Its
Hankel interval centers round upward, while the producer's round downward;
the interval and scalar accumulation implementations also differ. Every
source entry and physical error payment is checked, with independent rational
Gaussian inverse candidates and positive congruence/residual proofs for the
original C and N matrices. Decimal arithmetic chooses candidates only.

Reported negative lower-bound witnesses use exact rational coefficients and
an independently computed original physical mass. Reported positive lower
matrices require independent rational congruence positivity. Exact negative,
null and positive joint-block controls, whole-mass shifts, endpoint-corner
Hankel controls and a signed 13-cell mixed-log identity are checked.

Final statuses, certificate hashes, verified signs and the whole-aperture
classification are recorded in the aggregate checkpoint and independent
validation reports accompanying this note.

## Joint outcome and next exact gate

The producer certifies **JOINT_LOWER_BOUND_REJECTED** in both parities. The
independent validators both report **PASS** and independently certify those
negative upper quadratic endpoints after checking every source entry. The
fixed joined upper-left blocks remain exactly their certified positive
historical blocks. The complete 56-direction bound nevertheless has these
fixed rational negative values:

| Parity | Lower-matrix witness value | Value divided by original physical mass |
| --- | --- | --- |
| even | approximately `[-0.0708981997131515, -0.04964321215906148]` | `[-1.2307747252871987e-36, -8.617935441893757e-37]` |
| odd | approximately `[-7.125542753688125, -6.872959529253883]` | `[-2.935823525371325e-34, -2.8317556953068183e-34]` |

Exact coefficients, physical masses, values and independent checks are in
the certificates and reports. The midpoint LDL pivots choose a candidate
only; the negative sign is certified by the original outward rational lower
matrix's strictly negative **upper** quadratic endpoint.

The even witness is supported on P and the first four T53 columns; the odd
witness uses P and the first T53 column. The obstruction therefore appears
already in these seven- and four-direction joint subspaces, respectively.

This closes the missing-source-data stage and identifies a genuine obstruction
to this selected high-minorant certificate. It does not close the exact
original remaining Schur inequality and does not supply a negative original
Weil vector. Increasing arithmetic precision alone cannot reverse the sign
of this particular exact lower form.

A next high minorant must improve the **joint** inverse ceiling on these
witnesses. For each witness, an inverse-reaction reduction strictly larger
than the negative upper endpoint's absolute value is necessary for a strictly
positive refined lower form on that witness; it is not sufficient for the
whole matrix. The aggregate report records exact independently checked
physical thresholds. The next candidate should use the full joint source
`R alpha+G beta`, rather than the three-column joined source alone, and must
pay all new signed crosses with the unchanged P and T53 columns.

Whole-aperture original Weil positivity at `53/50` remains open. The highest
certified whole-aperture anchor remains `21/20`. The complete signed sources
are now available for a refinement of the high inverse bound on the exact
same domain.

## Reproduction

With the three authenticated original archives installed under
`nf24-inputs/Weil/`, run from the repository root for each parity:

```sh
python scripts/certify_native_complete_transport_nf49_106.py --parity even --output notes/data/RPB108_NF49_EVEN_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64
python scripts/certify_native_complete_transport_nf49_106.py --parity odd --output notes/data/RPB108_NF49_ODD_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_complete_transport_nf49_106.py --parity even --certificate notes/data/RPB108_NF49_EVEN_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF49_EVEN_COMPLETE_TRANSPORT_VALIDATION_20261010.json
python scripts/validate_native_complete_transport_nf49_106.py --parity odd --certificate notes/data/RPB108_NF49_ODD_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF49_ODD_COMPLETE_TRANSPORT_VALIDATION_20261010.json
```

Certificates are deterministic gzip, mtime zero, encoded as base64 text.
Private resumable computational caches live under `work/nf49/` and are not
repository inputs or published source substitutes. Compiler and GMP absence
affect speed only. Original Library archives remain untracked.

RH, F4, all-aperture continuation and Lean closure remain outside this
checkpoint. Other research branches remain unchanged.
