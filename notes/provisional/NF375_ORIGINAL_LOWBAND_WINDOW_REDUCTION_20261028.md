# Weil-Lab — NF375: original matched signed low-band window entry

**2026-10-28.** **Scope:** *certified alternative cutoff/budget pairs only*. The actual low-frequency residual has **not** been evaluated; do not label NF375 a full residual pass. Github-first custody is in force under repository `GOVERNANCE.md`, without repeated permission. This note is additive to PR #359.

## Previous cursor / current circle / next

- **NF374 (previous):** 4096-bit Arb native original J242 matched exterior physical 2nd-derivative Gram and 4 signed whole-real high-frequency multiplier tails at `Λ=2^24` succeeded. The original source, NF369 dyadic `Y0`, NF370 `T`, the seven-prime signed continuum `m(ξ)`, and the 242 physical source directions are unchanged. The original signed whole-exterior Schur and W-ODD-NEG remain OPEN.
- **NF375 (current):** before committing to millions of cells in a correlated physical low-band integration, rigorously reallocate the very conservative high-frequency estimates at smaller dyadic cutoffs. This is a finite exact-rational optimization **with a real quantitative acceptance statement**, not a low-band computation.
- **Next:** NF376 must construct and bound `H_i(Λ;j_i)` for actual specified `j_i∈J242` and an actual signed low-band continuum, using at least one certified cutoff/low-band reserve pair below. Its acceptance is a separate obligation.

## Analytic proof and original Fourier objects

Use the exact original signed multiplier hypothesis already inherited in NF371–NF374,

`|m(ξ)| ≤ 17+log|ξ|` for `|ξ|≥1`, with the exact 32 original sine frequencies `c_n=5n/11`, original `sinh(x/2)`, `B=11/10`, and `T` dyadic fixed by NF370. The original matched four-direction candidate is `u_i=f_{T e_i}−w_i`, `w_i=(I−P_J)F(I+Y0)T e_i`.

From the original PR355 critical source coefficients `a_(n,i)` after the exact NF370 shear, retain the signed sine endpoint moment `A1_i=Σ_n(-1)^n n a_(n,i)` and absolute cubic moment `A3_i=Σ_n n³|a_(n,i)|`. Since `sin(πnx/B)` vanishes at both endpoints, the **exact** supported sine Fourier transform has one common oscillatory factor. For `|ξ|>Λ≥2^20`, set `ρ=(32/(2BΛ))²<1/2`. Then

`|hat f_(i,sine)(ξ)| ≤ (1/(2π B)) (|A1_i|/|ξ|² + A3_i/[4B²(1−ρ)|ξ|⁴])`.

The rational estimates `π>3`, `1/(2π B)<1/6`, `1/[4B²(1−ρ)]<1` imply the conservative source-sine upper `|A1_i| sqrt(J4)/6 + A3_i sqrt(J8)/6` in the complete signed multiplier norm. The *actual original sinh coefficient* `b_i` is paid using `|b_i|sqrt(J2)/5+|b_i|sqrt(J4)/12`. For the **original actual matched exterior** use NF374 native strict caps `A_i>|w_i(B)|`, `D_i>|w_i'(B)|`, `K_i>∫_0^B|w_i''|`; its signed tail is below `A_i sqrt(J2)/3+(D_i+K_i)sqrt(J4)/18`.

Each `Jq(Λ)=2∫_Λ^∞ (17+log ξ)² ξ^(−q)dξ` is evaluated explicitly for `q=2,4,8`; at `Λ=2^k`, `L=17+logΛ<17+7k/10` by `log2<7/10`. Exact rational upper bounds to each square root use integer `isqrt` outward rounding (precision `10^−44`) and no unverified decimal approximation. Input original parent source and native report SHA-256s are mandatory; the native original boundary and second-curvature caps are independently checked from Arb-ball outward strings before use. This pays every sign and both Fourier half-lines. The pole is in J242, and the whole original multiplier tail statement inherits the same supported closed-form domain assumptions as NF374.

## Five certified alternative entry windows

Let `H_i(Λ;j_i)=||P_I F^{-1}[1_(|ξ|≤Λ) m(ξ) hat u_i]−j_i||_(L²(I))` for an **as-yet unconstructed** `j_i∈J242`. The following *strict* targets were independently checked with exact Fractions. All numeric entries below are **low-band norm acceptance targets**, **not measured low-band values**.

| Λ | Reduction vs NF374 interval | Needed `H1` | Needed `H2` | Needed `H3` | Needed `H4` |
|---|---:|---:|---:|---:|---:|
| `2^20` | **16×** | `<2.8e-11` | `<5.7e-12` | `<3.4e-13` | `<1.5e-13` |
| `2^21` | **8×** | `<3.2e-11` | `<6.5e-12` | `<4.6e-13` | `<2.0e-13` |
| `2^22` | **4×** | `<3.4e-11` | `<7.0e-12` | `<5.3e-13` | `<2.5e-13` |
| `2^23` | **2×** | `<3.6e-11` | `<7.3e-12` | `<5.8e-13` | `<2.7e-13` |
| `2^24` | 1× (NF374) | `<3.6e-11` | `<7.3e-12` | `<5.9e-13` | `<2.8e-13` |

For each of the **20 checks**, the script verifies in exact rational arithmetic

`(high_i(Λ) + target_i(Λ))² < (49/50000)*d_i/4`, with original `d=(6.5e−18, 2.7e−19, 2.1e−21, 4.9e−22)`.

Thus **any one** of these common cutoffs, if its four *actual* low-band norm targets are independently certified, suffices to discharge the same NF370 four-direction residual upper bound. This is an exact statement about *alternative sufficient criteria*, not evidence that the low band is small. The optimally efficient choice cannot yet be selected without seeing actual lowband numerical behavior. The interval count scales linearly with cutoff only for a fixed-cell-width method; we do not claim all possible algorithms cost 16× less.

## Mathematical boundary and research STOP

- `NF375_LOWBAND_ENTRY_CUTOFF_REDUCTION`: **EXACT-RATIONAL CERTIFIED** (under inherited original multiplier bound and NF374 native source-custody assumptions).
- `NF375_ACTUAL_LOWBAND_FOR_4_DIRECTIONS`: **OPEN**. No physical original low-band `J242` subtraction was computed, nor any signed continuum integral.
- `NF375_WHOLE_4D_RESIDUAL`: **OPEN**; remaining 238 directions **OPEN**.
- Original-domain review, even/whole Weil and RH: **OPEN**. No new source family; no alteration to any historical source or theorem statement.

**Next bold:** evaluate an original signed low-band feasibility witness, first at `Λ=2^20` or `2^21`, with a rigorously representable `j_i∈J242`. An unsuccessful finite low-band sufficient test is a method-class STOP only, not a negative eigenvalue certificate. Do not initiate blind `2^24` uniform-mesh integration or treat a finite Galerkin inverse lower slice as the infinite exterior inverse upper.