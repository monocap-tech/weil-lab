# NF393 — Cancellation-free original pole restoration for the frozen selected trial

**2026-10-29 Pacific.** Canonical original `W-ODD-NEG` **OPEN**. Stacked on NF392 draft PR #377, no merge. Aim: remove the unnecessary large-coefficient cancellation in the pole-corrected original NF390 selected moment, then acquire a genuine source-native selected moment and classify the actual frozen `j387`. This note **does not** assert that result is available. This is a mathematically exact source representation refinement, not a new Weil operator or an RH claim.

## Recovery — a concrete blocker, not a new arbitrary threshold

The verified original selected signed archive is intact: GitHub Actions original artifact #12776684037; historical ZIP SHA256 `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`, true complete original selected WJJ SHA256 `33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa`, original 968-entry WJF SHA256 `19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23`. The NF392 selected native output `NF392_original_j387_pole_restored_native.json` is not present as a verified source file at NF393 entry. The connected GitHub commit workflow listing is limited to 50 runs and does not reliably show this focused native job; absence there does not prove failure or successful completion. Original n512/n513, NF369, NF375, NF387 source data are not missing.

Independent exact JS BigInt arithmetic on genuine `notes/data/provisional/nf372_nf369_fields.json` (Git blob SHA1 `22a214ac2dff90960c35613aafaad1f44d5011a6`) and original dyadic fourth column

`T e4=(-2271087,-1621433,1115405,1048576)/2^20`

proves every component of `f=-Y0*T*e4` has `2*10^92<|f_i|<10^93`. These **raw coefficient scales** must be distinguished from the small *physical* matched residual or candidate signed moment: large cancellation is intrinsic to this source projection. Compared with NF392's `1.31e-20` sufficient moment-discrepancy diagnostic, the raw scale/diagnostic comparison exceeds 112 decimal orders. This is a precision-risk observation, NOT a theorem that 113 digits are sufficient or necessary for the complete signed projection. It strongly favors correlated Arb interval arithmetic, never ordinary double precision or independently rounded signed summands.

## The exact original pole identity

On unchanged J242, let `F` be the four original critical source-column map, `X` the exact **physical** J242 projection coefficients of F, `E=F-J242 X`, `Y0` original NF369 true dyadic quotient response, and `T` original NF370 four-column dyadic transformation.

The matched fourth source is

`u4 = F*T*e4 - E*(I+Y0)*T*e4`.

Since `E⊂J242^perp` **in physical L2** and the original odd rank-one pole generator `s=sinh(x/2)` is retained as selected raw source index 241 in J242,

`<E*(I+Y0)*T*e4,s>=0` **exactly**, hence

`<u4,s>=<F*T*e4,s>`. (NF393)

For the fixed **actual original selected** h=j387,

`<m(D)u4,h> = Wodd(u4,h) + 2*<F*T*e4,s>*<h,s>`.

This is the original complete seven-prime/arch/pole form `Wodd=P_I m(D)P_I-2|s><s|` under the inherited source-domain/operator identification. The pole correction is **not zero** on a selected h; replacing the left overlap by the original FTe4 physical source overlap is legitimate and avoids subtracting very large H D alpha and V f raw contributions simply to recover this one pole scalar.

The revised `scripts/verify_nf390_original_j387_selected_moment.py`, now on the NF393 research branch, computes `u4s_direct=(V*T)[241,3]` from the original physical 242×4 J-F matrix V and unchanged T; independently reconstructs `u4s_reconstructed=(H*D*alpha+V*f)[241,0]` and requires their **native Arb interval difference contains zero**; and uses only the *direct* value for `2*u4s*<h,s>`. The complete signed selected Wodd(u4,h) still reuses all 30,371 SHA-pinned original signed WJJ/WJF archived cells, pays the archive/physical-frame error, and must be computed by the native validator; no other off-support signed domain is assumed.

This identity checks the same original object through two independently routed physical projections, a useful custody check. It is not a surrogate for the missing full signed selected moment. Any agreement only certifies the original finite selected pole interface.

## Verification and stopping conditions

Exact-source-only verifier `scripts/local_replay/nf393_original_pole_source_cancellation_preflight.py` checks the exact original NF369 Git blob, original NF387 two-source dyadic j Git blob `d705ae312be5324bff64f3a9540e30e8b8bd34dc`, original rank/source SHA, full four components of `-Y0*T*e4` and strictly verifies each magnitude `(2e92,1e93)` using arbitrary-precision Fraction, not float. Independent BigInt source endpoint comparisons were checked at custody.

Focused workflow `.github/workflows/nf393-original-direct-pole-native.yml` runs source-only exact preflight first and then original SHA-pinned 4096-bit Arb physical selected projection / archive-reused signed Wodd / **direct pole correction**. Its native report includes both independent original physical pole overlap intervals and the exact source projection identity check. The authenticated report feeds the existing exact NF391/NF392 orthogonal Bessel STOP criterion for the **same original (j387)** and emits `STOP` or `INCONCLUSIVE`, never `PASSED` for lack of negative evidence. The original candidate must be explicitly left `UNDECIDED` until this actual native output is successfully verified.

- **Previous NF392:** original fixed j polynomial geometry gives a source-only sufficient moment discrepancy STOP ceiling <`1.31e-20`; original selected native not verified.
- **Current NF393:** exact original object pole projection identity, quantified enormous raw-coordinate cancellation, revised native validator + replay/CI. **No measured selected moment claimed at this checkpoint.**
- **Next:** recover genuine NF393 native output, verify the original archive, frame and physical source identity and exact interval endpoints, apply the NF391/NF392 strict candidate test. If strict, STOP only frozen j387; otherwise label it inconclusive and pursue source-adapted physical J242 selected subtraction rather than more generic threshold refinement.

**Standing:** source/direct-pole identity proven; source exact dyadic dynamic-range preflight independently checked. Original full low-band UPPER, actual NF387 selected moment/STOP, infinite exterior inverse, general original operator domain, other original directions, `W-ODD-NEG`, even sector, whole Weil and RH **OPEN**.
