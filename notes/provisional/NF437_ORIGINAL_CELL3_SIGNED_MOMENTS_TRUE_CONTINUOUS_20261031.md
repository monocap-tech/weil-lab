# Weil-Lab NF437 — Original true physical cell3 signed principal moments and complete continuous pz/z²

**2026-10-31 PT; original source; draft PR #458.** The sole canonical RH-facing objective `W-ODD-NEG` and RH remain **OPEN**. Stacked on NF436 exact true original physical cell3 512 native source-Chebyshev coefficients and uniform response tail, and on NF432 accepted true physical cell6 signed result. This pass tests the **original cell3 continuous signed integral**, not a shadow or the global NF404 scalar.

## Previous cursor → current circle → next

**NF436 previous:** Genuine original NF407 242 selected+4 critical dyadic source, original NF405 physical prime branch NF406 exact `J3=(log4−11/10,11/10−log2)`, original NF404 dyadic centering, true physical response z source-correlated Chebyshev a0..a511 and exact `||z-P511||_∞<1e−38` after verifying all 512 numerical interval midpoints. Source pinned to SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`, seams `c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675`. Full signed pz/z² still OPEN.

**NF437 current:** Certify original true J3 signed `p(x)=q(x)+r(x)` Chebyshev moments `m_n=∫J3 p(x) T_n((x-C)/H)dx` for n0..511, and true `dx` Chebyshev moments `J_k=∫J3 T_k((x-C)/H)dx` for k0..1022, with exact actual NF406 irrational endpoints, C=347/1000 and H=61/1000, using 2048-bit Arb cos(n arccos endpoint) primitive, not Gauss/sampled integration. Source of original endpoint `v=u4(B)<0` and Mangoldt `w_n=Λ(n)/sqrt n` from original NF407 principal source, separately independently check NF410 actual original cell3 signed p zeroth-moment enclosure.

## Critical original object-vs-shadow correction: r-jump ≠ number of regular source translates

The original NF405 regular source action for **z** indeed has **both** n2 translates `u4(x−log2)` **and** `u4(x+log2)` active throughout cell3; n3/4 minus only, all others none. NF434–436 correctly retained those two n2 regular terms.

However original NF407 principal discontinuity is **not** the regular translate-support count. It is explicitly:

```
q(x) = v/2 * sgn(x) * log(B/(B-|x|))
r(x) = v*sgn(x)*sum_n w_n * 1_(|x|>|B-log n|).
```

For all x in the original physical cell3 `J3=(log4−B,B−log2)`, **n3 and n4 principal jump indicators are ON, n2 principal jump indicator remains OFF** (its threshold `B−log2` is the right endpoint, not interior). Therefore the exact true original principal function is

`p(x)=v*(log(B/(B-x))/2 + w3+w4)`,

not the earlier erroneous `v*(log/2+2w2+w3+w4)`. The original source is not modified. This is a *typing distinction between a jump shadow and the full regular source object*. A fail-closed first original native moment calculation on the wrong `2w2+w3+w4` had zeroth moment approximately `−2.420497231385526e−12`, not overlapping original NF410 cell3 `m0≈−1.6483423686454099e−12`: **first Actions #41282417260 FAILED**, properly. Correcting original jump routing to only w3+w4 produces an exact independent NF410 m0 overlap with `m0≈−1.6483423686454099e−12`. No fabricated tolerance or overwritten parent source.

## Original exact native moments and integration

The code `scripts/local_replay/nf437_original_cell3_signed_p512_dx1023_native.py` computes exact original `J_k` through Chebyshev primitive

`J0=H(tR−tL)`, `J1=H(tR²−tL²)/2`,
`Jk=H[T_(k+1)/(2(k+1))−T_(k−1)/(2(k−1))]_(tL)^(tR)` for k>=2,

with `tL=(log4-B-C)/H`, `tR=(B-log2-C)/H`. Original length `log(2.2/4? no): J0≈0.1205584583201640717483` (actual exact interval `(log2+B)−log4`; never replace by rational endpoint). The original endpoint log series `log(B/(B-C-Ht))=ell0+Σ_k>=1 2q^k T_k/k`, with `q=H/(B-C+sqrt((B-C)^2-H²))<1/10`, is truncated after 110 modes and its analytic tail paid as exact rational `2*(1/10)^111/[111*(1−1/10)]` plus explicit original v-source radius and true J3 length. This constructs all 512 original signed p moments and 1023 raw dx moments under rigorous outward Arb balls.

[Focused native signed-moment Actions #41282619434 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41282619434). Full 512 p and 1023 dx original-source native output artifact **#13074326015**, ZIP SHA256 `2db0e8b70a49decfdb57e2ed73b17687dca359952a32a67c71729879982a0a98`, generated inner original JSON SHA256 `3007009a33613eda7349f612a71f8cd3c1658e91c2d3f066e081aa6af591b179`, expires 2027-01-30.

For the **actual original continuous true cell3** signed scalar, the exact-Fraction algorithm `scripts/local_replay/nf437_original_cell3_true_signed_from_P511_exact.py` SHA-pins all original numerical sources:

- NF434 genuine source a0..31 original JSON SHA256 `004ff92369474dd31aafdc81da4306f555bcdd0911985142b1e6c5f27226c9ff`.
- NF435 genuine source a32..255 original JSON SHA256 `23be9e821235569c9b8075b3916c843376dbdd742cd71063e49025260bda7546`.
- NF436 genuine source a256..511 original JSON SHA256 `6ae216679eb44c6932a016803ff5f84698c70e708dbc9559b83cee3a7b4170cf`.
- NF436 corrected **true complete cell3 uniform** z−P511 original JSON SHA256 `9bd859e79b0fe5f569abef8cb78c6dc9642123439e0e211041ad3faa34deccb7`, includes midpoint selection max5e−45 for each original coefficient.
- NF437 true original p512 and raw dx1023 moment JSON SHA256 `3007009a33613eda7349f612a71f8cd3c1658e91c2d3f066e081aa6af591b179`.

For each original coefficient interval use its **exact rational midpoint**, not duplicate uncertainty (NF436 epsilon already pays the midpoint selection). Compute `∫pP511=Σ_n a_n m_n`, and using exact `T_iT_j=(T_{i+j}+T_|i−j|)/2`, compute `∫P511²=Σ_k b_k J_k`. Then for original true z=P511+r and `|r|≤epsilon<1e−38`, charge

`|∫p r|≤epsilon*[-m0.lower]` because the original p<0 on J3;

`|∫(z²−P511²)|≤J0.upper*(2 epsilon Σ|a_n|+epsilon²)`.

The original complete true signed cell3 integral `D3=4∫p z +2∫z²` is then rigorously enclosed by the interval sum. **No sign is imposed in advance.**

A first complete original exact-Fraction computation in Actions #41282839977 printed **strict POSITIVE** signed cell3 `D3≈+1.0018870562838712e−22`, with `∫pz≈−5.135803138013453e−23`, `∫z²≈+1.528104155744626e−22`, total true-z tail fee approximately `1.9520847925580568e−48`, then wrapper gate failed on Python's default 4300-digit conversion limit when reading a >5232-digit exact Fraction endpoint. This is an **exact output parsing issue**, not a negative or invalid original numerical result. The independent wrapper was amended to `sys.set_int_max_str_digits(0)` and a corrected full CI was queued: do not call final verified until corrected CI passes. Full signed JSON/ZIP SHA and permanent custody receipt to follow actual success.

## Remaining obligations and next decision

If final complete integral CI passes, **original physical cell3 complete continuous signed contribution is strictly POSITIVE**; original NF432 certified cell6 complete continuous contribution is strictly NEGATIVE. These are both original-source nonprincipal signed cell sectors, not a theorem that their sum meets NF404 or that any other cell is signed a certain way. Six remaining original positive physical cells (1,2,4,5,7,8), full principal `E_p` and original NF410/NF404 global signed scalar, fourth J242 exterior upper, W-ODD-NEG, even/whole Weil, infinite inverse/domain, RH **OPEN**. Do not merge to main.

**Next NF438:** Complete remaining original six physical signed cells with a prioritization of easier interior ones 4/5 before independently solving cell7 near-B complex-ellipse/image collar; preserve cell-specific NF405/406 principal jump activation vs regular z translate support and exact source correlation. Then full NF410/NF404 signed acceptance, not a premature RH promotion.


## Final independent original true continuous signed cell3 gate — ACCEPTED

**[Focused original exact-Fraction source-pinned Actions #41282903842 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41282903842)**. Corrected wrapper disabled Python's arbitrary 4300-digit decimal-to-int threshold; this is necessary to parse the **unchanged** original ~5232-digit Fraction interval endpoints and did not alter the original Cheb polynomials or integration. The independent original signed p512/raw dx1023 source-native [Actions #41282619434 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41282619434), including original NF410 p0 overlap, is separately accepted.

The full source-original **continuous** true cell3 enclosure, conservatively outward rounded from the accepted exact Fraction JSON:

```
true ∫_J3 p z ∈ [−5.135803138013452832822478228e−23,
                 −5.135803138013452832822478227e−23]

true ∫_J3 z² ∈ [1.528104155744626211937318736e−22,
                 1.528104155744626211937318757e−22]

true D3 = 4∫p z + 2∫z² ∈
      [+1.001887056283871290745646182e−22,
       +1.001887056283871290745646222e−22].
```

Thus **true original continuous cell3 nonprincipal signed contribution is STRICT POSITIVE**. Exact raw interval width `≈3.904169585116114e−48`. Original complete-response tail charges remain paid, with actual `epsilon≈1.240272970503549096570565174797e−39`, pz tail fee `≈2.044394485966699e−51`, and z² tail fee `≈9.71953607307095e−49`. The different signs of pz and z² are not grounds for any positivity theorem; only their exact resulting signed sum is accepted on this original physical cell.

Original complete signed JSON **SHA256 `b772b089e5a69a94e8027fee68332d03b5248119f9b7beec0c4e8c6ec80e01d6`**; Actions artifact **#13073851733**, ZIP SHA256 `d7c30cd851eb4bcb83279a7b2188e60e4add0ff070e09337da865e808f63733d`, retained until 2027-01-30. Compact permanent result/source SHA custody `notes/data/provisional/NF437_original_true_cell3_signed_decision_custody_index.json`; raw full exact Fraction JSON permanent archive remains due. **No main merge**.

**Standing/next:** Complete original true signed cell3 **ACCEPTED POSITIVE**, original true signed cell6 **ACCEPTED NEGATIVE**. The six remaining positive physical cells 1,2,4,5,7,8, whole `E_p` and NF410/NF404 global signed criterion, original fourth J242 exterior upper, `W-ODD-NEG`, even/whole Weil and RH **OPEN**. **NF438** should prioritize newly typed principal-jump vs regular-response branch routing on cells 4/5 and evaluate them, with cell7 near-B analyticity obstruction preserved separately.
