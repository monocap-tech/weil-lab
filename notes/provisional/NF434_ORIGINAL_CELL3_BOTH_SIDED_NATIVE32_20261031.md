# Weil-Lab NF434 — Original cell 3: two-sided n=2 source reconstruction and native first Chebyshev block

**2026-10-31 PT.** Canonical `W-ODD-NEG` OPEN, RH OPEN. Stacked on NF433 original physical seam geometry [draft PR #445](https://github.com/monocap-tech/weil-lab/pull/445). NF432 true complete continuous signed physical cell 6 remains accepted and unmodified.

## Previous cursor / current circle / next bold

- **NF433 previous:** exact original NF405/406 positive physical cell 3 is `(log 4−B,B−log2)`, B=11/10. Original prime-power n=2 **both** `u4(x−log2)` and `u4(x+log2)` survive, with n=3/4 only minus and n=5/7/8/9 neither. Cell3 admits wide Bernstein ellipses E2..E5 at C=347/1000, H=61/1000. Cell7 E2..E5 invalid near B.
- **NF434 current:** instantiate all original NF407 source contributions and the full 2048 matched endpoint images using 2048-bit native Arb/Acb Chebyshev coefficients a0..a31 for the **correct cell3 analytic branch**, not copied cell6 branch. Preserve 242 selected +4 critical generators, all 32 critical sine frequencies, true original odd removable m0 pole, NF404 exact dyadic center, and physical NF405 signs. Numerically independently compare direct `u4(x±log n)` from the original NF407 sine/cosine source with the entire original transformed source prime contributions at x=C, and `u4(B)` with independently reconstructed original endpoint source.
- **Next:** if focused native CI passes, increase cell3 certified modes until a sourcewise frequency/order tail plus the cell3-specific true-image radius and original signed p moments is decision quality; then exact integrate its true original pz/z² as NF432 did for cell6. Otherwise retain verified branch/geometry and isolate the native discrepancy. Cell7 endpoint collar remains separately blocked.

## Correct original source prime signs

For physical positive cell3, write the four original translate terms as shifts `h` with `u4(x-h)`:

```
(n, Lambda base, h) =
(2,2,+log2),
(2,2,-log2),
(3,3,+log3),
(4,2,+log4).
```

Use the **original** weight `Lambda(n)/sqrt(n)`, so n=4 has base2, not base4. The source generator `c y^k sin(2π f y)` for even k and cosine for odd k is reconstructed by `alpha=-i c/2` for even k and `alpha=c/2` for odd k, with paired frequencies. Thus the correct shifted Chebyshev coefficients of the source factor `(x-h)^k exp(lambda(x-h))` are `exp(-lambda*h) · coeff[(x-h)^k exp(lambda*x)]`; **the sign of h may be negative**. Do not collapse n2 to one translate or double the wrong directional amplitude. The source odd sinh translate `-w*pole*sinh((x-h)/2)` and the per-active-translate original boundary subtraction `+w*u4(B)` are likewise retained for both signs.

The original arch transfer still contains complete digamma terms and the 2048 per-side odd-correlated endpoint images and the analytically canceled m0 sinh pole. The original endpoint logarithm remains `-u4(B)/2 * log[B/(B-x)]`; the signed four original translations each contribute `+w*u4(B)` in the same fixed branch.

## Source image and interval budget

The original cell3 true support `J3` lies inside the rational outer interval `[C-H,C+H]=[0.286,0.408]`. On this outer interval `B-x≥173/250=.692`, so `exp(-2(B-x))<1/3`; with the same original NF424 2048 matched image construction and NF407 exact 4096-bit dyadic coefficient balls, the original finite-image/source real-cell error can be outward overcharged at `<2e-45`, and each positive-index Chebyshev series coefficient may be charged `4e-45`. This is an original-cell3-specific, source-pinned real-axis geometric-image argument, **not** a claim that the original cell6 fitted polynomial or finite source response itself transfers. For the original analytic branch, the upper rational outer interval extends past the n2 plus-translate physical seam by ~0.0012, but only its **analytic continuation** is used to construct Chebyshev coefficients; no physical branch is switched outside J3. Source uncertainty for the extra <=0.002 support overshoot is paid with a factor of two.

The separate true original cell3 finite polynomial a0..a31 is not yet a full cell3 function approximation; source-specific n>=32 and signed p and dx moments are outstanding even if the first block passes.

## Verification and custody

- Focused native script: `scripts/local_replay/nf434_original_cell3_both_sided_native_cheb32.py`.
- Focused CI: `.github/workflows/nf434-original-cell3-both-sided-cheb32.yml`.
- Source: original NF407 242+4 4096-bit dyadic coefficient balls; source overlap check uses independent original `U.at` from NF415 source kernel rather than lambda/Bessel construction.
- Cell: original NF406 true irrational `log4-B` to `B-log2` and original NF405 both-sided support.
- Acceptance: outward real Arb coefficient widths <1e-25 for each n0..31, independent direct signed source overlap including both n2 branches and endpoint u(B), correct original source hashes and prime branches, original 2048 matching image indices. All signed pz/z² and NF410/NF404 remain **OPEN**.

The original fourth J242 exterior upper, `W-ODD-NEG`, even/whole Weil, infinite domain/inverse and RH remain OPEN. No merge into main.
