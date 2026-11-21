# Weil-Lab — CP006
## Source-locked complete-zero theorem and adaptive dyadic spectral interval certification

**Independent CP### stage.** This research branch stacks on CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. No IV###, NF###, or PI### source files are modified. The CP004 IV022-based original Lean companion #802 is a separate draft. The IV### and NF### programs remain responsible for their own existing compiler and physical-source certification.

**Proof boundary:** A formal upstream theorem about complete zero COUNT is NOT a certified high-precision EXPORT of every zero. An exact adaptive numerical error budget is NOT a full certified arithmetic–spectral equality. New CP006 local tests/CI are source-content/rational arithmetic checks, not Lean kernel acceptances; external direct Lean builds are also gated by compiler/axiom receipts. No RH beyond a finite height or global signed Weil positivity is established.

## 1. Source-locked upstream theorem and exact certificate path

Use only `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3` (tag `v1-1e6`) with upstream **Lean/Mathlib v4.35.0**, distinct from original Weil-Lab **Lean/Mathlib v4.34.0**.

The exact source chain was independently inspected:

- `Zeta/Zeros/Certificates.lean`: `certifiedZeroIntervals` (a noncomputable joined `CertifiedZeroIntervals` bundle), and `certifiedZeroIntervals_length : certifiedZeroIntervals.intervals.length = 1748002`. Also `certifiedZeroIntervals_getLast?` pins the LAST zero interval right endpoint to `Enclosure.sfrac false 1000449286 1000` = 1,000,449.286.
- `Zeta/Zeros/CountCertificates.lean`: `certifiedZeroCount : CertifiedZeroCount` combines the generated interval bundle with the certified Gram-block sequence and supplies the actual Turing `count` and `below` proofs.
- `Zeta/Zeros/Count.lean`: structure `CertifiedZeroCount` extends both certified gram and zero-interval structures and requires `minIdx+1 = intervals.length` and `height <= gramPoint minIdx`.
- `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean`: `riemannZeta.N_gramPoint_eq Z : N(gramPoint Z.minIdx)=Z.intervals.length`, plus genuine simplicity and off-line-exclusion theorems.
- `Zeta/Main.lean`: finite-height `Zeta.riemannHypothesisUpTo_1000449` and `Zeta.simpleZerosUpTo_1000449`, with source `#guard_msgs/#print axioms` allowing only standard axioms. A text inspection is NOT a rerun of the upstream kernel.

**Important boundary:** the last certified interval endpoint 1,000,449.286 is NOT the Gram point itself (roughly 1,000,449.797), and `N(g)=1748002` is a count to the Gram point, **not necessarily** `N(1,000,000)=1748002`. CP006 retains all certified intervals through the actual Gram point `g>10^6` and truncates only above `g`, for which CP005's bound from T=10^6 is conservative.

**Verified source blobs at the pinned commit** (Git blob SHA-1, not release archive digests):
- `lean-toolchain` `a6aff065db2882c535684f8c5bcd4f16e9a23915`
- `lakefile.toml` `bbec128d14c0ddaac4abb40900dc61bd43138561`
- `Zeta/Main.lean` `20e5a9ae3ae3cdab3462e5f85865e918ec672e00`
- `Zeta/Zeros/Certificates.lean` `54fce07cbc5bf0913ceccb108cbf73f1227857c0`
- `Zeta/Zeros/CountCertificates.lean` `a3e729d23802c3731432de9a3c7d46d18252ba10`
- `Zeta/Zeros/Count.lean` `b8c458cca723b20cdf71a5f8d662d9d8e952c983`
- `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` `c2b1da101a580cc91cfb0a43d72d5839fd97265c`

The new `source_lock.json` and `cp006_external_zero_source_lock.py` hash and check these pinned original bytes and their required exact declarations. This is a **SOURCE CONTRACT CHECK**, not an axiom audit, a kernel reproduction, or an imported .olean verification.

## 2. New stronger interval-error bound: use actual height, not blanket 1e−9 precision

Let `phi` be the original CP001 real-even Schwartz bump, and `Phi(y)=∫_{-1}^1 phi(u)cos(yu)du`.

Existing CP003 exact derivative input gives `||phi''||_1<16`, `||phi'||_1=2`; therefore for `y≠0`, twice integrating by parts establishes

```
 |Phi(y)|  <= min(2,16/y²),
 |Phi'(y)| <= min(1,20/y²).
```

The derivative bound follows from `Phi'(y)=-∫ u phi(u)sin(yu)du` and
`||(u phi)''||_1 <= ||phi''||_1 + 2||phi'||_1 <20`.
This is an analytic derivation from the same bump, not an unrelated test or an imported RH assumption. It still needs formal source/bump linkage for Lean acceptance.

For each root bracket `I_k=[a_k,b_k]` with `0<a_k<=gamma_k<=b_k` and midpoint `mu_k=(a_k+b_k)/2`, define `delta_k=(b_k-a_k)/2`. It is unnecessary for every `delta_k` to be ≤10^(−9), provided the *total* weighted localization error is small.

Partition by dyadic bins: `2^j <= a_k < 2^(j+1)` (integer j, possibly negative). For a frozen test of physical radius h_i, set

```
 A_i(j)=min(2,16/(h_i²*2^(2j))),
 D_i(j)=h_i * min(1,20/(h_i²*2^(2j))).
```

Because both the true ordinate and midpoint are ≥a_k≥2^j,
`|Phi(h_i*gamma)|<=A_i(j)`,
`|d/dgamma Phi(h_i*gamma)|<=D_i(j)` throughout the bracket.

For the exact CP004 positive-zero cosine moment
```
 J_ij(gamma)=2*h_i*h_j*Phi(h_i gamma)*Phi(h_j gamma)
                      *cos((c_i-c_j)gamma),
```
the fundamental theorem of calculus gives, without any zero-line assumption *outside the finite certified range*,

```
 |J_ij(gamma_k)-J_ij(mu_k)| <= 2*h_i*h_j*delta_k *
       (D_i(j)*A_j(j)+A_i(j)*D_j(j)+|c_i-c_j|*A_i(j)*A_j(j)).
```

With physical `G=diag(h_i a2)`, `a2>24/25`, and `sqrt(h_i h_j)<=(h_i+h_j)/2`, the normalized real symmetric matrix spectral norm is bounded by maximum absolute row sum:

```
 E_loc^adaptive(r) =
   max_i sum_j sum_bins Δ_bin * (25/24)*(h_i+h_j) *
     (D_i(bin)*A_j(bin)+A_i(bin)*D_j(bin)
                      +|c_i-c_j|*A_i(bin)*A_j(bin)),
 Δ_bin = sum_(k in bin) delta_k.
```

All band sums and weights are **nonnegative rational numbers**. Each `A_i<=2` and `D_i<=h_i`, so `E_loc^adaptive` is **at most** CP005's uniform Lipschitz bound on the same actual brackets. High-zero bands can be far smaller. Importantly, we do NOT claim that the available upstream default maximized brackets already meet the required sum budget; CP006 must measure the actual certified bracket widths.

The conservative all-zero tail remains `E_tail(r)` from CP005 at T=10^6, independent of the width of the finite brackets, and a separately proved `E_quad(r)` covers profile/cosine quadrature. The required certification condition is

```
 E_tail(r)+E_loc^adaptive(r)+E_quad(r) < 1/500 .
```

No unconditional numerical bound for `E_loc^adaptive` is asserted without actual individually certified bracket data. An externally declared `E_quad<=1/50000` is a **budget allowance**, not a verified quadrature receipt.

## 3. New exact-rational roster-to-band converter: fail closed

`scripts/cp006_dyadic_zero_bracket_budget.py` reads an externally supplied exact rational two-column positive-zero roster and a pinned CP005/CP006 source manifest:

- source archive digest and exact tag/commit are checked against the pinned manifest, though these claims **cannot authenticate the source proof without checking its real evidence**;
- all 1,748,002 rows must have positive ordered rational endpoints, be below a declared Gram-point lower bound, and match the raw SHA-256 checksum;
- checks no strictly overlapping intervals; touching intervals are counted and marked a separate potential zero-index/source-proof concern;
- NO per-row 1e−9 requirement: aggregate `Δ_bin` is computed exactly from the input rows in dyadic height bands;
- computes the exact rational matrix row-sum bound for each radius, the conservative tail, and a strictly allocated quadrature allowance;
- emits `STRUCTURAL_BUDGET_WITHIN_THRESHOLD` only when the *declared* external source receipts, actual data and arithmetic budget are structurally consistent; otherwise `NOT_READY` or `BUDGET_EXCEEDED`. **These are NOT kernel-accepted zero proofs**, since source interval-to-proof correspondence and quadrature are still unaudited.

A self-test uses SYNTHETIC interval bandwidth fixtures for exact arithmetic regression and negative controls. It does not pretend to generate the 1.748-million-zero certificate.

## 4. Distinct upstream v4.35 Lean compatibility bridge

Weil-Lab original physical Lean is still v4.34.0; upstream Zeta is v4.35.0. CP006 includes an **isolated v4.35.0 Lake subproject** with the external package pinned to tag `v1-1e6`. The CI verifies that this tag resolves to the full immutable source commit `c06b4e13d9c847e50a32c3d738271cbad62ae9f3` before building. The candidate file imports `Zeta.Main` via Lean's new `module` syntax, calls the real `riemannZeta.N_gramPoint_eq certifiedZeroCount`, and audits the actual imported finite-RH and simple-zero standard-axiom declarations.

**No source copying into v4.34.0 and no unverified cross-toolchain .olean transfer.** A full external build may require the upstream `v1-1e6` Linux release archive (~887 MB) and its pinned Mathlib; dedicated workflow logs/axiom receipts must be recovered before marking the bridge accepted. The release's published SHA-256 alone is insufficient; the downloaded bytes must be hashed in a real build before accepting a binary.

The bridge does not export all individual zero brackets or prove the original Weil mixed-form dictionary. It certifies only that the external theorem can actually be imported under its own correct toolchain, if and when its dedicated build and axiom audit pass.

## 5. Precise falsifiers and CP007

**Zero-data falsifiers:** count mismatch, source commit/blob mismatch, a root interval not linked to an actual certified batch, failed Turing completeness, nontrivial zero above the stated Gram cutoff falsely included, or nonzero standardized kernel axioms.

**Spectral dictionary falsifiers:** a rigorously non-real, nonsymmetric, unequal-old-diagonal or negative-principal-minor finite critical-line cosine Gram compression; or rigorously disjoint full-original arithmetic/finite-spectral matrix enclosures beyond `E_tail+E_loc^adaptive+E_quad`.

**What remains open:** actual `phi` Schwartz construction and n9 matrix linkage to original v4.34 IV011, individual certified zero bracket proof lineage, optimized band budget based on REAL data, independently certified `Phi` and cosine interval quadrature, original signed two-pole/Gamma/full-prime mixed entry enclosures, normalization of the entire Weil-zero-side dictionary. These cannot be replaced by the CP006 model checker or by source-pinned version metadata.

**Next CP007:** obtain real bracket export with per-batch source digests, produce the first actual adaptive band budget, make the full original mixed arithmetic 3×3 enclosures, and test CP-C1 against a rigorously enclosed finite spectral matrix. No global Weil positivity or RH conclusion.
