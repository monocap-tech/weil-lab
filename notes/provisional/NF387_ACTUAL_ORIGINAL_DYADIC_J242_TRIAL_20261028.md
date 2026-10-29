# NF387 — Explicit original source-custodied dyadic J242 trial, not a hypothetical j

**2026-10-28 PT.** Canonical `W-ODD-NEG` **OPEN**. Stacked on NF386 draft PR #371. This pass constructs ONE actual nonzero selected-space dyadic vector in the **unchanged** original rank-242 raw source coordinates and proves its supported Fourier-tail upper. It does NOT compute the original complete signed low-band mismatch integral, a physical lowband norm upper, the strong residual, full inverse, original n513, or RH.

## Recover the unchanged original source

The original selected-rank node manifest `notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json` has SHA256 `9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2`; its **first retained original center is 37/64, with 14 selected multiplicities**. Under the original odd source convention, its raw source indices 0 and 2 represent respectively `sin(2 pi (37/64)x)` and `x² sin(2 pi (37/64)x)` on `I=[-11/10,11/10]`. The pole remains retained as the last original source. These are **raw source coordinates**, not the normalized `D` orthogonal frame. Thus any nonzero dyadic combination of these two is an actual member of J242, not a newly introduced source.

The unchanged NF375 report has Git blob SHA1 `03c709571046d3f09307614aaded9749f5a15ba1` and original source/native SHA256 `abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770` / `a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559`. It records original NF370 fourth signed sine boundary-moment `A1=-40060235101/1048576000000000000`. As a **deterministic source-informed heuristic only**, not a signed-response optimizer, select the nearest dyadic at denominator `2^48` to `A1/121`, giving `alpha=-88873/2^48`.

The actual frozen candidate is

`j387(x)=alpha*(121-100*x²)*sin(2*pi*(37/64)*x)` for `|x|<=11/10`, zero otherwise.

The **complete original raw J242 coefficient vector** is committed at `notes/data/provisional/NF387_original_J242_dyadic_candidate.json`. Exactly two coefficients are nonzero: index 0 is `-10753633/2^48` and index 2 is `8887300/2^48`; the other 240 coordinates, including the pole, are exactly zero. This is an explicitly constructed original j. Matching `121 alpha` to the source boundary moment does **not** imply that `j387` approximates the original signed low-band action well; that must be tested and is OPEN.

## Exact endpoint and curvature certificate

Put `B=11/10`, `p(x)=121-100x²`, `c=37/64`, `kappa=2*pi*c`. Since `100 B²=121`, `p(±B)=0`; **j387(B)=j387(-B)=0 exactly**.

Use the elementary strict bound `pi<22/7`, hence `kappa < K= (44/7)*(37/64)=407/112`. On [-B,B], `|p|<=121`, `|p'|<=200B=220`, `|p''|=200`. Differentiating twice:

`|j387'(B)| <= 200B |alpha|` and
`||j387''||_L1 <= 2B |alpha| [200+2*(200B)*K+121*K²]`.

Consequently the exact rational combined upper is

`C=2*(200B)*|alpha| + 2B |alpha| [200+2*(200B)*K+121*K²]`

`=44107579160667/17654110539292344320 < 1/400000 < 1/10`.

This proves for an **actual selected source** the hypothetical endpoint/curvature input from NF386 with a much stronger margin. The original Fourier convention is `exp(-2*pi*i*xi*x)`. Integration by parts twice and `pi>3` give the strict selected j tail

`int_|xi|>2^24 |j387hat(xi)|² dxi < 2*(C/36)²/[3*(2^24)^3]`

`= 24018253573018590323455369/35323409218742391829616555637003766558738489270683156715929600`

`≈6.800e-37 < tau4²/64`, where **actual original NF375 direction-4 future lowband norm target** `tau4=2.8e-13`. Thus the selected-j Fourier-tail entry is **strictly certified** without any 242-dimensional signed-kernel recomputation.

## Remaining *actual* signed mismatch obligation

The positive original Fourier-primal sufficient criterion from NF386 for the SAME fixed u4 and this actual selected j is

`I_387=int_|xi|<=2^24 |m(xi)*uhat4(xi)-j387hat(xi)|² dxi`.

A verified nonnegative upper satisfying `I_387 + 6.800e-37 < (2.8e-13)²` would discharge the original NF375 fourth-direction lowband upper (under inherited Fourier/domain identification). **No bound of this type is currently proved.** The dyadic j is source-informed through the original sine moment but **not optimized with respect to I_387**. If its signed Fourier mismatch is too large, this *two-sparse* candidate must be stopped; a full 242-coordinate source-adapted projection or direct physical interval restriction may be needed. Do not claim that the j-tail result controls I_387.

The exact script `scripts/local_replay/nf387_original_dyadic_j242_trial.py` requires the full original rank SHA256, original NF375 Git-blob hash and source/native pins, checks all 242 raw coordinate slots, exact endpoint zero and rational curvature/tail, and emits a provisional machine-readable result. Dedicated focused CI is separately tracked; **not green until verified**.

**Previous:** NF386 only hypothetical original selected-trial boundary condition. **Current:** NF387 real source-custodied dyadic J242 trial and strict original selected-j Fourier tail. **Next:** rigorously enclose the one nonnegative original signed lowband mismatch integral for this frozen j (or method STOP this particular candidate). The full original exterior Schur, selected-source 242 gate, n513 signed native, operator domain, odd/even/whole Weil and RH remain OPEN. No main merge or historical overwrite.
