# RC283 — reduced positive projection references

Parent: RC282 at `92e0d7876a38a85deee5fa4282118ef9dd059563`.
Aperture: `B=11/10`. The original Weil operator is **unchanged**.

## Structural theorem and certificate

The actual parity-specific original physical form satisfies `G0 >= D-lambda I`
on the full operator form domain, with `lambda=C_b>0` certified at RC277/278
and `D P_n=(H_n+s)P_n` from RC129.

For any initial segment of the matching parity Legendre basis, let
`P_low` denote its exact physical L2 projection. Define a *new* reference

```
G_low = G0 + lambda P_low
      >= D_(P_low) + (D-lambda)_(I-P_low).
```

If `m` is the first omitted matching parity degree, the monotonicity of
`H_n` on the entire infinite-dimensional complement and RC129's exact
lower bound for `s` imply

```
G_low >= mu D > 0,
mu = 1 - lambda/(H_m+s_lower).
```

Also `G_low <= G_full <= nu_old D`; dropping the positive high projection
cannot worsen the *upper* global form bound. This certifies a bounded,
globally coercive reference, not positivity of `G0`.

| Option | Even rank | Odd rank | Total reference rank | Guaranteed D floor |
| --- | ---: | ---: | ---: | ---: |
| Minimal positive | 116 | 185 | 301 | ~0.0000621741 |
| Buffered (>0.005) | 122 | 195 | **317** | >0.0051287 |
| Buffered (>0.01) | 128 | 206 | 334 | >0.0102356 |

The actual source-gate for each distinct reduced reference is
`K_low=Mass_low-lambda U_low*G_low^-1 U_low`. Its full positive
definiteness is equivalent to original Weil positivity under the
standard finite-rank augmentation Schur congruence; that finite gate
has **not** been computed or proved positive.

## Exact Schur correspondence — coupling is retained

The rank-371 old augmented reference is

```
G_full = G_low + lambda U_high Mass_high^-1 U_high*.
```

Partition the *old* auxiliary gate into low/high blocks:

```
K_full = [[K_LL, K_LH],
          [K_HL, K_HH]].
```

RC282 proved `K_HH>0` for the chosen high-degree block. Applying the
resolvent/Woodbury identity, with the actual positive inverse, yields

```
G_low^-1 =
  G_full^-1
  + lambda G_full^-1 U_high K_HH^-1 U_high* G_full^-1,

K_low = K_LL - K_LH K_HH^-1 K_HL.
```

This is an **exact structural elimination** of the high auxiliary
coordinates: their interactions are absorbed into the new reference
inverse, not ignored or assumed small.

The RC280/281 positive five-mode **old** pivots are still valid for
`G_full`, but cannot be inherited as positive for `G_low`.
The validator includes an exact 2x2 indefinite-original test: old
positive pivot `23/488`, old positive high pivot `1/61`, reduced
low pivot `-7/8`. This controls that critical logical distinction.

## Evidence and open gate

The validator checks exact Git-blob pins for RC129, RC278 and RC282;
the rational cutoff inequalities are independently recalculated, with
strict downward inherited floors and full complementary rank counts.
Generation and reverse-order replay return the same JSON. No original
prime, regular, pole or archimedean source action is newly performed,
and no unverified old inverse-response pivot is transferred.

**Next RC284:** construct *fresh* rank-317 reference trials and pay
their complete original-action and inverse residual covariance;
evaluate the coupled low auxiliary gate. Compare against the rank-301
and rank-334 conditioning alternatives without conflating references.

**Stage I, the full remaining gate, RH, global F4 and Lean are open.**

## Reproduction

```bash
python scripts/validate_rpb108_rc283_reduced_reference.py --output certificates/rpb108_rc283_reduced_reference.json
python scripts/validate_rpb108_rc283_reduced_reference.py --output certificates/rpb108_rc283_reduced_reference.json --replay
```

GitHub Actions performs the exact replay on the PR and research branch,
checking the pinned historical certificate bytes; this does not constitute
independent proof of the imported analytic assumptions.
