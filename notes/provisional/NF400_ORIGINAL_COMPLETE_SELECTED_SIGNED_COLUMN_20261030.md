# NF400 — Reconstruct complete original J242 signed-response column without dense Householder Q

**2026-10-30 PT.** Canonical obligation `W-ODD-NEG` **OPEN**. Source-preserving 242-dimensional selected-response calculation on the **same original fourth NF370 source**, inherited original signed archive and supported strong Fourier realization. Draft research branch stacked above NF399 PR #385; no main merge.

## Previous → current → next

- **NF399 prior:** Original source-authenticated NF398 fixed `j387` moment, with odd pole restored, yielded a strict **all-candidates** necessary half-space and norm restriction: `<j,j387><0` and `||j||>0.3153944` for any original selected `j` approximating fourth lowband within `2.8e-13`. NF399 source-only exact CI [run #41022059857](https://github.com/monocap-tech/weil-lab/actions/runs/41022059857) **SUCCESS**. It did not compute optimal selected projection or a lowband upper.
- **NF400 present:** The full source-pinned original `242×1` pole-restored signed moment column can be obtained from a **single** original archived signed matrix-vector operation plus a four-reflector forward map, preserving all original mixed and pole entries. Code, proof, a 242-entry native output contract and independent exact acceptance verifier are committed. **The native 242-column numerical output is not accepted until actual GitHub run + durable source-native receipt pass.**
- **Next:** If the original source-native report is independently accepted, inspect the physical Gram projection `||P_J m(D)u4||`, selected source coordinates and viable candidate Fourier tails. Do not pretend projected signed column or the necessary norm lower alone proves the true lowband **UPPER** or controls all J-perpendicular response. Keep concurrent sibling NF398 branch custody explicit.

## Original-object identity (no new signed kernel cells)

Let original raw `J=(J0,...,J241)`, physical Gram `H_ij=<Ji,Jj>`, physically near-normalized exact original dyadic frame `D`, `N=D^T H D`, and original signed archive Householder `Q=H0 H1 H2 H3` with **exactly four** actual SHA-authenticated reflectors. Write the **unchanged** original NF370 fourth matched source as

```
u4 = J D alpha + F f,
alpha = Y (I+Y0) T e4,
f = -Y0 T e4.
```

Let original archive `M` represent the complete 242×242 odd signed selected form in the `Q` frame (with certified full archive/Frobenius error) and `L_ik=Wodd(Ji,Fk)` the original 242×4 mixed signed source array. Let `s=J241=sinh(x/2)` and `u4s=<u4,s>=<F T e4,s>`, the separately authenticated original pole-source identity. Define the **physical-multiplier** signed moment column in raw J basis by

```
b_i = <m(D)u4,Ji> = Wodd(u4,Ji) + 2<u4,s><Ji,s>.
```

Then its **D-frame** moment vector is exactly

```
d = D^T b
  = Q M Q^T alpha + D^T L f + 2 u4s D^T H e_241.
```

The full **raw** column is equivalently

```
b = H D N^-1 d,
```

and the squared physical norm of the exact orthogonal selected projection is

```
||P_J m(D)u4||^2 = d^T N^-1 d,
```

provided the inherited original supported form/strong-domain identification allows the multiplier response and original signed form to be paired as stated. This is *not* the signed Weil quadratic-form sign or a full odd-sector theorem.

This formula uses the **same 30,371** original archive source WJJ/WJF cells. No change to `u4`, `J242`, `M`, `L`, `s`, domain, Fourier normalization, cutoff or source SHA. Importantly, **Q^T** acts by applying archived reflectors in *ascending* order; **Q** acts by applying them in *descending* order. No dense 242×242 Householder Q and no per-basis new kernel integration.

## Outward error payment and acceptance

The original archive certifies a Frobenius error upper `eps=sqrt(sq1+sq2)`; because Householder Q is orthogonal, the complete original D-frame moment vector has **global Euclidean error no greater than** `eps ||alpha||` from original signed J-J frame approximation. Certified physical frame `N=D^T H D` has maximum absolute row-sum deviation below `0.01`, so `lambda_min(N)>0.99`. Thus the original selected physical projection norm derived from the Arb frame can be enclosed with additive allowance

```
delta_projection <= eps ||alpha|| / sqrt(0.99).
```

An individual raw-source moment `b_i` receives the conservative Frobenius allowance `eps||alpha|| sqrt(Hii/0.99)`, in addition to 4096-bit Arb outward interval rounding. The original L mixed signed entries remain full native Arb balls, not approximate doubles. These are **original finite projection** bounds and do not pay off the entire original low-frequency integral or infinite selected-space complement.

The code verifies:
- Original SHA of rank, NF369, selected source, physical frame, original signed 30,371-cell ZIP and WJJ/WJF members.
- Authentic four reflectors; exact source-native 242×242 physical H, D-frame N and all 16 original quotient Gram overlaps.
- Entire 242D original pole-restored moment column, physical Gram projection and per-entry/global outward error payments.
- **Independent frozen j387 contraction** in the D frame against the original accepted NF398 native signed/physical moment, *and* source-only rational re-contraction using two actual raw dyadic coefficients `(-10753633,8887300)/2^48`, checking original interval overlap.
- Source-native status retained permanently only after both native stage and independent receipt succeed; failed/queued output is an execution event, not accepted native evidence.

## Exact scope and continuing gap

This pass supplies an original-data full-column **producer and testable acceptance contract**. Until the native workflow actually completes, the full 242-entry numerical column and projected norm remain **UNVERIFIED**. The analytic linear-algebra identity is exact under the inherited original form/frame assumptions.

Even a verified projected norm or a `b` vector only characterizes the selected finite physical projection, not an upper bound on `||t_L-j||` or a lower bound beyond already measured exterior shadow information. A candidate `j` must be constrained by *both* selected projection and the original Fourier-tail/lowband acceptance, with the independent general original operator-domain audit unresolved. **`W-ODD-NEG`, even/whole Weil and RH remain OPEN.**

**Repository files:** `scripts/verify_nf400_original_selected_full_column.py`, `scripts/local_replay/nf400_original_selected_column_exact_receipt.py`, `.github/workflows/nf400-original-selected-response.yml`; accepted native-only files `NF400_original_selected_column_native.json`, `NF400_original_selected_column_acceptance.json`, `NF400_original_j387_scalar_crosscheck_native.json`, typed `NF400_native_execution_status.json` (only when GitHub Actions has actually committed them).

## New complement-only acceptance reduction (exact, source-dependent)

There is a stronger geometric consequence of constructing the complete selected projection; it is **not** a numerical measurement. Under the same inherited supported Hilbert realization write `w=P_I m(D)u4=t_L+e`, `||e||<=H`, `P=P_{J242}`, and choose **the source-determined** `j*=Pw`. Then the selected and exterior terms are physically orthogonal:

```
t_L-j* = (I-P)t_L - P e
||t_L-j*||² = ||(I-P)t_L||² + ||P e||²
            <= ||(I-P)t_L||² + H².
```

The exact source-pinned NF398 highband `H` and fourth lowband norm target `tau=7/25000000000000` satisfy, by independent exact-rational comparison,

```
sigma=11/40000000000000=2.75e-13
sigma²+H² < tau².
```

Hence **if** a future original-object certified upper gives `||(I-P)t_L|| <= sigma`, then the specific *unrestricted* selected projection `j*=P m(D)u4` satisfies `||t_L-j*||<tau`. Conversely, the selected-space least-error candidate for `t_L` itself is `P t_L`, and for every `j in J242`, `||t_L-j||>=||(I-P)t_L||`. Thus the complement is the precise **existence** obstruction for an unrestricted selected-space lowband fit, not another numerical selected trial.

**Important scope:** `j*` may fail additional original *dyadic coefficient* or Fourier-tail entry requirements even if this conditional physical lowband gate passes. This identity neither provides the required `J242^perp` norm upper nor proves the original full lowband upper. Original n512/n513 exterior shadow lower observations do not supply the complement **upper**; no reversal of inequalities is permitted.

Independent source-only exact replay: `python3 scripts/local_replay/nf400_original_complement_budget_exact.py`. This check verifies the source-native NF398 SHA, original cutoff, tau and highband H, and the strict rational squared budget. All new claims in this section are **conditional original-object reductions**, not native column acceptance or closure of `W-ODD-NEG`.
