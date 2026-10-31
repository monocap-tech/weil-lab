# Weil-Lab NF428 — Original cell6 native 256 coefficients and all 1500 signed principal moments

**2026-10-31 PT**. Canonical `W-ODD-NEG` OPEN, RH OPEN. Stacked on [NF427 draft PR #434](https://github.com/monocap-tech/weil-lab/pull/434), which certifies the true original full-cell6 degree-1499 Chebyshev SERIES cutoff and native n=0..63 coefficient intervals. Preserve original NF407 242 selected plus four critical generators, original NF406 seven physical prime seams, original NF404 dyadic center, NF424 common generating function and exact analytic finite-image charge. No main merge.

## Previous / current / next

**Previous NF427:** exactly 1500 original cell6 Chebyshev-series coefficient intervals mathematically suffice to represent the unchanged original regularized `z` to <2e-45 uniformly on `J6=(log 7-B,log 8-B)`, B=11/10; first 64 n=0..63 intervals certified native at width <1e-25 and independent original NF416 pointwise full-physical x=0.9 overlap PASS. Missing original 1436 n=64..1499 and signed original pz/z² integral OPEN.

**Current NF428:** submit two separate source-pinned native computations:

1. Native `arb/acb` 2048-bit full **original** digamma + 2048 shared endpoint image + signed seven-branch response: directly certify the source-correlated series **n=0..255**, requiring outward interval width <1e-25 for each and independent full original physical NF416 x=0.9 overlap. This is a 4x larger coefficient block than NF427, not a surrogate reconstruction. If PASS, there are **1244** coefficients n=256..1499 still to calculate.
2. Derive and native-enclose **all 1500 exact signed original cell-6 principal moments** `m_n=∫_(J6) p(x) T_n((x-C)/H) dx`, where `p=q+r`, **not** `z`. Preserve original u4(B) signed source interval and physical original prime powers 2,3,4,5,7. Use the true logarithmic endpoints and a remainder-certified endpoint log series. Cross-check n=0 with the independent previously accepted original NF410 signed p moment. If PASS, the complete **linear integration functional on any future 1500 coefficients** is ready, but **not** its value at missing coefficients or original signed pz.

**Next:** compute native modes 256..1499 in correlated blocks with permanent custody of the interval JSON. Then evaluate certified signed full cell6 `∫pz` from the complete coefficient/moment pairing and `∫z²` from rigorous Chebyshev product moment recursion, charging source/image/series/coeff radii; extend original cells3/7 and the remaining five, and finally NF410/NF404.

## Exact high-degree signed principal moment identity

On the original fixed cell 6, original physical support branches `n=2,3,4,5,7` are post-seam; n8/n9 are neither. From NF407 original principal formula, with original endpoint source `v=u4(B)<0`,

`p(x)=v/2 * log(B/(B-x)) + v * W,`
`W=log(2)/sqrt(2)+log(3)/sqrt(3)+log(2)/sqrt(4)+log(5)/sqrt(5)+log(7)/sqrt(7).`

The n=4 prime power has `Lambda(4)=log 2`, and no prime-power sign or seam is guessed. Each coefficient is checked against original NF407 signed-Mangoldt outward intervals. The original signed `p` is defined on the actual open cell `J6=(log 7-B,log 8-B)` with no crossing on its interior.

Define `C=91/100,H=7/100, t=(x-C)/H`; true `t_l,t_r` arise from the source log7/log8 knot intervals and satisfy `-1<t_l<t_r<1`. For all n>=0 put

`J_n=H*∫_(t_l)^(t_r) T_n(t)dt`.

These have the exact elementary endpoint primitives:

- `J_0=H*(t_r-t_l)`, `J_1=H*(t_r²-t_l²)/2`.
- `J_n=H*[T_(n+1)(t)/(2(n+1)) - T_(n-1)(t)/(2(n-1))]_(t_l)^(t_r)` for n>=2.

Evaluate `T_n(t_{l/r})=cos(n arccos(t_{l/r}))` with native Arb; this avoids fake high-order source interval recurrence growth.

Let `A=B-C=19/100, Q=(A+sqrt(A²-H²))/2, q=H/(A+sqrt(A²-H²))<1/5`. The **original endpoint logarithm** admits the exact Chebyshev expansion

`log(B/(B-C-Ht))=ell_0+sum_(k>=1) ell_k T_k(t)`
`ell_0=log(B/Q), ell_k=2q^k/k.`

For original `J6`, `log(8/7)<1/7`. Truncate endpoint-log Cheb at **K=110**. The true uniform log remainder is explicitly

`delta_log <= 2*(1/5)^111/[111*(1-1/5)] <10^-70.`

Using `T_jT_k=(T_(j+k)+T_|j-k|)/2`, the exact signed principal moment becomes

`m_n=v*(W*J_n + (ell_0*J_n + 1/2*sum_(k=1)^110 ell_k [J_(n+k)+J_|n-k|])/2) + e_n`

with rigorous error `|e_n| <= |v|*(1/2)*(1/7)*delta_log`, **plus the explicit original source interval u4(B) radius charge**. This error bounds **each** n=0..1499 independently and analytically, no numerical x quadrature or derivative expansion. All original 1500 moment balls inherit exact original endpoints and original source signs, not a retyped smooth surrogate.

The moment script: `scripts/local_replay/nf428_original_cell6_signed_chebyshev_moments_native.py`. Native full source 256 interval coefficients: `scripts/local_replay/nf428_original_cell6_correlated_cheb256_native.py`. Focused CI: `.github/workflows/nf428-original-cell6-cheb256-signed-moments.yml`. The native moment n=0 must **overlap** the accepted original NF410 signed Taylor degree-zero cell6 moment and all moment widths must be <1e-25. Both jobs retain original source-pinned JSON evidence as artifacts upon PASS.

## Standing before focused CI

**No result asserted from script existence.** The n=0..255 numerical coefficient block is a pending verification gate, as are the signed m0..m1499 source moment intervals. Do not combine merely submitted code with mathematically accepted evidence. If both pass, accept separately: 256 finite native coefficient intervals and 1500 signed original p moment enclosures; do **not** claim complete original cell6 pz/z² integral or NF404/RH.

Remaining theorem-level obligations: missing n256..1499 source-correlated z coefficients, full original signed cell6 pz and z², other cells, NF410/NF404 complete scalar, original fourth exterior J242 upper, infinite complement inverse/domain, W-ODD-NEG, even/whole Weil, RH OPEN.


## Focused native results — both original-source jobs PASS

[GitHub Actions #41248984553](https://github.com/monocap-tech/weil-lab/actions/runs/41248984553) completed **SUCCESS** at exact source SHA `7a791d5246151f12a29a1813edbdff3197b45ca2`. Independent original-native jobs:

1. `original-native-256-source-coefficients` **PASS:** all 256 outward source-correlated coefficient intervals `a_0,..,a_255` computed in 2048-bit Arb, original 99 physical frequency groups formed from all 246 generators, all 2048 shared endpoint-image indices retained, source/image uncertainty charged, each certified interval width <1e-25. The complete generating-function z(0.9) interval **overlapped independently certified original NF416 separate physical I0/I1**. Source-native 256 coefficient JSON artifact `NF428-original-cell6-native-256-chebyshev-coefficient-intervals`, ID **13059744821**, digest **sha256:a0636895566c28be3184e78fd9c72dc186953a37cb6eacc63cbaca7ca85b7ac4**.
2. `original-native-signed-p-moments-1500` **PASS:** original NF407 signed source endpoint and five actual positive prime jumps, true NF406 irrational log7/log8 knots, all 1500 source-signed `m_0,..,m_1499` outward 2048-bit intervals width <1e-25 individually, K=110 logarithm Chebyshev tail analytically charged, original endpoint-source radius charged, and **m0 independently overlapped original NF410**. Complete 1500 original signed principal-moment JSON artifact `NF428-original-cell6-signed-p-chebyshev-moments-1500`, ID **13059719501**, digest **sha256:61fcfa62ef12538e767cc5a4e7621c9b95edd4fd9ee891a280d446f17c98e246**.

Both artifacts expire **2027-01-29** under current GitHub Actions retention. Native scripts, source pins, mathematical derivations and CI workflow have permanent repository custody; the **generated actual JSON intervals still need permanent archival** before retention expiry.

**NF428 accepted:** (i) original full physical cell6 source-correlated `z` Chebyshev **series coefficient intervals n0..255** (256/1500), all width <1e-25; (ii) full original signed principal moment **linear functional** `m0..m1499` in accepted outward intervals. **Still OPEN:** source-correlated coefficient intervals n256..1499 (**1244 left**), complete original cell6 `∫pz` (requires all coefficients, not merely signed moments), `∫z²` (also requires full coefficients and Cheb-square moment contractions), other seven cells, the NF410/NF404 whole signed original scalar, fourth J242 exterior upper, infinite inverse/domain, `W-ODD-NEG`, even/whole Weil and RH. This native CI PASS is **not** proof of RH or of a completed cell6 signed scalar.
