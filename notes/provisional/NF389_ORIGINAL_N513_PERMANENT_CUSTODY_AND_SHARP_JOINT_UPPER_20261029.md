# NF389 — Source-custody the original n513 and sharpen the complete two-ray upper

**2026-10-29 Pacific.** Active `W-ODD-NEG` remains **OPEN**. Stacked after NF388 PR #373; draft/unmerged. This pass **does not compute the missing original signed low-band Fourier mismatch or full infinite inverse**. It provides (1) permanent-original-n513 GitHub custody workflow with full SHA and overlap preflight and (2) a stricter **exact-rational UPPER on the entire two-ray signed-response shadow**, not the whole Weil object.

## Recovered evidence and scope

NF388 exact original two-direction source audit [run #40954483980](https://github.com/monocap-tech/weil-lab/actions/runs/40954483980) has now **SUCCESS**, retrieving the ORIGINAL NF381 4096-bit physical / 3072-bit full signed n513 native report from [run #40820718599, artifact #12882010193](https://github.com/monocap-tech/weil-lab/actions/runs/40820718599/artifacts/12882010193). Verified original artifact ZIP SHA256: `193483b0c757f88f836479e5d50261b629439ed8534875feeeee66008bb121ad`; member SHA256 `NF381_original_n513_signed_native.json`: `e0aaa0abb29c8ec75b3524ec6197c12235a7fc7fa66d76c77c4643c2ff27bffe`; original exact parent joint replay member SHA256 `fad492046e351634a0ecf520a5a37d67a7e067e1a3518aef031418107a49748b`. This parent preserved 242 new original complete signed J-v cells and 33 original basis-v cells while reusing 30,371 original WJJ/WJF signed archive entries, unchanged all seven primes/arch/pole, 16 parent physical Gram and 32 signed overlaps, exact same rank/source/frame. Original n512 SHA256: `9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b`.

The native n513 JSON is **NOT permanently repo-stored at initial drafting**. NF389's new dedicated push-triggered workflow checks artifact/run identity and all SHA values, performs the new exact-rational two-ray replay and commits the byte-identical original n513 native, original NF381 joint replay, and the NF389 typed exact result into `notes/data/provisional` on this draft research branch. **Do not call that archival transfer complete until the actual commit and native file SHA have been inspected.** GitHub Actions has narrowly scoped `contents:write` only for that research-branch archival job. No main merge, no force push, no historical overwrite.

## New exact mathematical result

Let `D=2401/(2*10^28)` be the unchanged NF370 fourth-direction squared strong-residual acceptance budget. The actual original NF380 native interval and its NF383 rational replay establish for the first original projected exterior sine q512

`x=b512²/(||q512||² D)<145134/10^6`.

The now accepted original n513 native interval independently proves, by exact Fraction endpoint comparison,

`y=b513²/(||q513||² D)<7421/10^6`.

The two unprojected supported original sine harmonics are exactly L2-orthogonal and each has squared norm `B=11/10`; after the exact original projection onto the physical exterior of J242+F4, the unknown physical normalized cross `rho=<q512,q513>/(||q512||||q513||)` satisfies `|rho|<1/75`, as certified in NF388 from original native g intervals. **Do not set rho=0**.

The COMPLETE, exact two-ray squared dual response `d12=b^T G^-1 b` in units of D is

`d12/D=(x+y-2*rho*sqrt(x*y))/(1-rho²)`.

For `R=1/75`, use `2 sqrt(x*y) <= x/4+4y` (Young's inequality). Then strictly

`d12/D < ((1+R/4)*(145134/10^6)+(1+4R)*(7421/10^6))/(1-R²)`

`= 13809111/89984000 ≈ 0.15346184877311522 < 307/2000 = 0.1535`.

Thus the *entire original fixed 512/513 two-witness shadow* occupies less than **15.35%** of the unchanged NF370 fourth-direction squared residual budget, improving NF388's coarser 15.5% upper; the signed joint lower from NF381 was ≈15.15287%. This bound does **not** upper-bound the actual infinite-dimensional physical exterior strong residual, nor the true inverse-form response. Under the inherited OPEN original operator-domain realization, if the complete fourth strong residual squared were at least D, then the component orthogonal in the **physical L2** metric to this fixed two-ray plane must contribute strictly more than `1693/2000 D =84.65% D`. This is a conditional necessary criterion, **not evidence** that the complement is large or small.

The complete 512/513-only obstruction test was stopped already in NF388; NF389 sharpens the quantitative envelope and restores expiring-original-data custody. **STOP** further 512/513 precision refinements unless tied to a new independent complement estimate.

## Replay and next actual mathematical obligation

`python3 scripts/local_replay/nf389_native513_sharper_two_ray_upper.py --original-512 notes/data/provisional/NF380_original_archived_unfitted_signed_dual_native.json --original-513 notes/data/provisional/NF389_original_n513_signed_native.json --output notes/data/provisional/NF389_original_two_ray_sharper_upper_exact.json`

Input `NF389_original_n513_signed_native.json` is populated only after the archive workflow has retrieved and SHA-verified the byte-identical original Actions native. No fabricated reconstruction is allowed.

**Previous NF388:** original n513 native PASS, joint full 2D upper <0.155D; external artifact only. **Current NF389:** sharper genuine original-native 2D upper <0.1535D and a pinned permanent custody workflow. **Next:** the real original NF387 dyadic j two-coordinate signed low-frequency **mismatch** integral or source-adapted physical J242 subtraction upper. If its nonnegative full-line mismatch is too large, issue a scoped sparse-candidate METHOD STOP. Do not produce further generic sine witness scans. Whole original exterior residual upper, full inverse, general analytic/operator domain attachment, other 238 selected directions, even, whole Weil and RH remain OPEN.


## Post-workflow original source custody reconciliation (confirmed)

The branch-only NF389 archive workflow **wrote all three native/report files to the research branch**. A fresh authenticated GitHub file retrieval independently confirmed:

| Permanent branch path | Git blob SHA1 | Source standing |
| --- | --- | --- |
| `notes/data/provisional/NF389_original_n513_signed_native.json` | `c71c0dca54e5e9e0ab753485a6c6aa9dd38d4f8a` | **Byte-for-byte identical original n513 native**; SHA256 `e0aaa0abb29c8ec75b3524ec6197c12235a7fc7fa66d76c77c4643c2ff27bffe` |
| `notes/data/provisional/NF389_original_joint_lower_exact_parent.json` | `8fb2c87dabbec96529e73207169a981e47b02753` | Byte-for-byte identical original NF381 exact rational parent; SHA256 `fad492046e351634a0ecf520a5a37d67a7e067e1a3518aef031418107a49748b` |
| `notes/data/provisional/NF389_original_two_ray_sharper_upper_exact.json` | `704a1ae7df0c4b0d598f1e48730d86f4ac211473` | Derived source-hashed exact rational replay, `d12/D<307/2000`; `W_ODD_NEG=RH=OPEN` |

The original ZIP's two member Git blob hashes were computed independently from the downloaded SHA-verified original archive and **match the new GitHub objects exactly**, which establishes byte identity, not merely metadata agreement. No old source or historical 49-file file was overwritten. This is permanent custody **on the NF389 draft research branch only**, NOT a merge into `main`. The archive commit's specific GitHub Actions overall status should be treated separately from verifying the three actual resulting files; a source-hash match and exact derived report have both been inspected.
