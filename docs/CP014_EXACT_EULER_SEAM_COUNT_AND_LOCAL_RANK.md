# Weil-Lab — CP014
## Original first-52 Euler cut (N(149.5)): proof-level finite-set partition, exact zero-cardinality transport, and a falsifiable Hardy-`Z` local-rank alternative

**Track:** independent CP### cross-projection study, stacked on CP013 PR #829 → CP012 #827 → CP011 #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. **DO NOT TOUCH** the canonical Phase IV original signed Weil IV### support-extension / Lean certification, Phase III NF### numerical matrix-enclosure custody, or separate PI### spectral/Gamma research.

**Status:** Formal source candidates committed against isolated external `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`, Lean v4.35.0. The original published finite-height zero-count and simplicity source theorems are genuine upstream results. CP013's RS-only reassembly and CP014's new mathematical deductions are **NOT yet accepted new Lean kernel declarations**: the proper original `.olean` and `#print axioms` outputs are still required. No claim of full numerical source row #53 identity, verified narrower zero enclosure, mixed signed Weil versus zero-side spectral equality, global Weil positivity or RH.

## 1. Upstream external mathematical source — read, not assumed

The source files have been inspected under the *exact original commit*, and a separate SHA-based automatic CI will verify these primary declarations:

| File | Original Git blob | Genuine accepted original source declaration |
|---|---|---|
| `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` | `c2b1da101a580cc91cfb0a43d72d5839fd97265c` | `riemannZeta.N_gramPoint_eq`, `riemannZeta.order_eq_one_upto`, `riemannZeta.le_N_of_zeros` |
| `Zeta/Zeros/CountCertificates.lean` | `a3e729d23802c3731432de9a3c7d46d18252ba10` | Concrete complete original `certifiedZeroCount : CertifiedZeroCount` |
| `Zeta/Zeros/Certificates/Basic.lean` | `128e19e4bb056332b0fd71a8c107f4075cd8cd07` | Original `BatchSpec.bundle` and kernel-separated certified interval append |
| `Zeta/Zeros/HardyZ.lean` | `9975442b0c14011c35f4624197d0bf26169c7665` | **Actual** `Zeta.hardyZ` and `hardyZ_eq_zero_iff_riemannZeta` for nonnegative ordinate |

The original published full count is (N(g)=1,748,002), and original source `riemannZeta.order_eq_one_upto` states all nontrivial zeros with (0<\Im s<g) have multiplicity one. Here (g) is the actual original certified Gram point slightly above 1,000,449. The source `N(T)` counts strictly (0<\Im s<T) with **multiplicity**; it is *not* always equal to the number of distinct zeros. The finite-height simplicity theorem is exactly what allows this conversion for (T\le g). The original finite-height RH result additionally excludes off-critical-line zeros below (g).

The **separate CP013** candidate reconstructs (52) Euler source-certified zero slots below (c=149500/1000=149.5) and (1,747,950) original RS source-certified slots with first lower boundary at (c), using original `BatchSpec.append`. The source-level interval witnesses are genuine Zeta roots in **open** intervals, so no published certificate counts a root at their common seam. However, a theorem assembled from the original public existential `BatchSpec` must still be shown to supply the concrete finite E/R root witnesses used for the new count.

## 2. New exact finite-set mathematical statement — not a root-number guess

Let
```
  S_g = { s : ζ(s)=0, 0<Im(s)<g }
  E   = { 52 distinct original low-height Euler witness zeros }
  R   = { 1,747,950 distinct original high-height RS witness zeros }.
```
If the reconstructed independent source bundles are kernel accepted and their witness roots are proven to satisfy
```
  E∪R ⊆ S_g,     E∩R=∅,
  |E|=52,        |R|=1747950,
  ∀z∈E, Im z<c,  ∀z∈R, c<Im z,
  |S_g|=1748002,
```
then **(|S_g|=|E|+|R|)** forces (S_g=E∪R). Therefore
```
 {s∈S_g : Im(s)<c} = E
 and      |{s∈S_g : Im(s)<c}| = 52.
```
Because original bounded-height *simplicity* identifies (N(c)) with the finite number of distinct roots below (c), it follows
```
 N(149.5)=52.
```

**Critical promotion boundary:** this conclusion is an exact mathematical deduction under the genuine source saturation hypotheses. CP014 does *not* treat the missing kernel witness mappings (E,R) from the original `BatchSpec.bundle` as already established. The new Lean theorem explicitly receives these properties as arguments; the final unconditional `N(149.5)=52` theorem is **STILL OPEN**.

The original `certifiedZeroCount` already supplies the complete height-(g) equality and simplicity. This permits a separate CP014 genuine Lean source theorem target: for (T\le g),
```
  N(T) = |{z : ζ(z)=0, 0<Im z<T}|.
```
Combined with the source `N(g)=1748002`, it produces a new kernel source target `original_full_source_finite_zero_card` with no assumed numerical zero coordinates. That source-level statement still needs a real Lean compiler pass.

## 3. Four concrete v4.35 Lean modules, distinct proof states

All four are under **`cp011_zeta_v435/`**, preserving the original Weil-Lab v4.34 tree untouched.

1. **`CP014EulerCutLower.lean`** proves as a source candidate the unconditional one-sided target
   [
     52\le N(149.5),
   ]
   using only the *original* already certified 52-row Euler `BatchSpec.bundle`, its last boundary at 149.5, source `riemannZeta.le_N_of_certifiedZeroIntervals` and original monotonicity `riemannZeta.N_mono`. It neither imports an unproven root #53 sign nor presumes the CP013 RS-only theorem has compiled beyond its imported source candidate.
2. **`CP014FiniteCut.lean`** proves exact finite-set cardinal saturation `exhausted_by_two_disjoint_parts`, `exact_low_partition`, and the 52/1747950 zero-count special case; the source witnesses and their membership proofs remain explicit premises.
3. **`CP014ZetaCut.lean`** connects genuine original `N_eq_sum` plus `order_eq_one_upto` to distinct zero finsets for bounded (T). It derives the original full-roster zero-cardinality theorem from original `N_gramPoint_eq`, and then a **conditional** `N_at_Euler_RS_seam_eq_52_of_source_witnesses`. Its precise remaining hypotheses include `hEsub`, `hRsub`, `hdisjoint`, `hEbelow`, `hRabove`, the exact source witness counts, and the height-cut bound. No silent `sorry`, axiom, hash-to-theorem conversion or numerical root acceptance.
4. **`CP014HardyRank.lean`** uses the actual original `Zeta.hardyZ` and `hardyZ_eq_zero_iff_riemannZeta` to formalize the **conditional** observation that `StrictMonoOn Zeta.hardyZ (Icc a b)` implies at most ONE critical-line zeta zero in `Ioo a b`. A certified derivative lower bound supplying strict monotonicity on a short region is a SEPARATE and currently **missing** proposition, not inferred from floating-point samples.

Every one is only a **new Lean SOURCE CANDIDATE**. A separate original Zeta v4.35 manual-only workflow builds the CP013 dependencies and these four CP014 modules, emits actual `.olean` and standard-only `#print axioms` logs, and uses `scripts/cp014_exact_seam_lean_axiom_audit.py` to refuse any `LEAN_PASS` without those receipts. Even a successful workflow would label the output **CP014_ORIGINAL_ZETA_SEAM_PARTIAL_KERNEL_ONLY** and explicitly leave unconditional (N(149.5)=52) open until the E/R witness coverage premises are genuinely discharged.

## 4. Falsifiable rank #53 test: local Hardy-Z monotonicity instead of inaccessible source-row endpoints

CP010 numerically proposed the first Riemann–Siegel positive zero near `150.05352042078`, candidate narrow bracket `(150.05352,150.05353)`. CP012 established that upstream abstract `BatchSpec 200 ...` does not publish every numerical source row. CP013 provided a 149.5 method-seam/count route.

**Exact additional goal:** independently prove that no second zero occurs in the *short gap* (149.5<t<150.05353). A source-correct possible route is:

```
  (i)  N(149.5)=52                                    OPEN unconditional Lean
  (ii) existence of ζ(1/2+iγ)=0 in
        (150.05352,150.05353)                           CP010 kernel OPEN
  (iii) StrictMonoOn Zeta.hardyZ [149.5,150.05353]      OPEN ANALYTIC bound
  (iv) all zeros in that local range lie on Re=1/2      original finite RH theorem
```

Here (iii) combined with `hardyZ_eq_zero_iff_riemannZeta` excludes a second critical-line zero; (iv) excludes off-line zeros, so the proposed root must be the unique zero above 149.5 and below 150.05353, hence the **53rd positive-height zero**. Alternatively prove a local upper count (N(150.05353)=53) directly. Neither claim is made without new evidence.

**Independent exploratory numerical derivative screen:** high-precision `mpmath.siegelz` and its **NUMERICAL** derivative on sampled points in `[149.5,150.05353]` gave `Z'(149.5)≈2.44273814585` and `Z'(150.05353)≈1.62013464885`, with intermediate sampled derivatives also positive. CP014 adds a reproducible optional `--numeric-derivative-screen` using 17 sample points and explicitly prints `NONRIGOROUS`. **This is NOT a uniform positivity enclosure and does not prove (iii).** In particular, it does not solve the original RS analytical sign remainder obstacle: independent interval evaluation of (Z'), or a rigorous analytic lower bound over the entire compact interval, is required. This is a targeted falsifiable test for the proposed cross-projection interface, not a path to a global RH assertion.

**Negative control:** exact finite-set examples show that knowing (N(149.5)=52) and a genuine zero in the new narrow bracket is STILL insufficient to call it #53. Another (hypothetical) zero at 149.8 could precede it unless the independent local upper count/monotonicity excludes that root. A complete count at the final large Gram point alone does not determine the local rank.

## 5. Exact source / compiler custody

New `scripts/cp014_seam_N_cut_and_derivative_screen.py`:
- `--self-test`: fully exact `Fraction` finite-set partition equality, deliberate missing-root/overlap/bad side-of-cut negative controls, and false ordinal-53 inference counterexample.
- `--source-root EXTERNAL_ROOT`: SHA-check **four** exact original external Zeta Lean source blobs above, verify the actual original theorem names and the CP014 local new explicit premises; emit `CP014_SOURCE_SIGNATURE_AND_EXACT_LOGIC_PASS_NOT_KERNEL` only.
- `--numeric-derivative-screen`: independent floating-point Hardy-Z and derivative sample with 17 points, printing **NOT a rigorous derivative enclosure, uniqueness or rank proof**.

New CI `.github/workflows/cp014-original-seam-source-preflight.yml` is PR-triggered lightweight exact rational/source/SHA work, no v4.35 compiler or massive original 1.75m-source data fetch. Separate `.github/workflows/cp014-original-euler-seam-v435-manual-kernel.yml` is MANUAL-ONLY to protect the ongoing original IV### and NF### queues. Actual kernel output is not presumed available.

## 6. Intrinsic / source-dependent preservation laws and next hypotheses

- **Intrinsic:** genuine zeta zeros, multiplicities, positive ordinal sequence, and actual zero count at (T=149.5); the original source `N(g)` with multiplicity yields the combinatorial saturation argument when all E/R witnesses are linked.
- **Certificate-relative:** the original Euler/RS method split, choice of seam (c), source `BatchSpec` existential bundles, the 52/1747950 list segmentation, SHA pins, and whether source root-index witnesses are admitted by a new Lean count theorem. Any interval refinement must preserve the canonical zero without assuming abstract existential endpoint identity.
- **Numerical/technique-dependent:** the exploratory 17-point derivative sample, original Hardy-Z analytic approximant/error and `CP009` high-root dyadic precision schedule. A source positivity margin for `Z'` is a separate new analytical task; no numerical sampling is converted into a proof.

**Next — CP015:** recover CP014 real source/Lean receipts; if the elementary finite-list/count lemmas compile, prove the missing source-to-E/R-root-finset cover directly from original `CertifiedZeroIntervals.zeros`, `BatchSpec.bundle`, `append` and its true endpoint bounds, thereby dropping the final conditional witness hypotheses. In parallel, test a genuine interval-arithmetic derivative lower bound of original `Zeta.hardyZ` on 149.5..150.05353 or a direct rigorous local upper count. Do not scale interval refinements until the first exact source-root rank proof passes.

**Open:** CP013/014 new Lean kernels; unconditional (N(149.5)=52); source witness E/R cover; local strict Hardy-Z monotonicity and N(150.05353)=53; true CP010 narrowed Euler zero sign/error; complete 1,747,950 original refined zero locations; full `Pole − Prime + Arch` 3×3 signed Weil matrix, independent finite spectral integration and original arithmetic/zero-side normalization. **No global Weil positivity or RH**.
