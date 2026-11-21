# Weil-Lab — CP020
## A complete SOURCE-CANDIDATE proof of the original M6/N256 Borwein all-circle remainder bound and exact derivative-germ transport

**Track:** independent CP### cross-projection, stacked on CP019 PR #840 → CP018 #839 → CP017 #838 → CP016 #837 → CP015 #836 → CP014 #831 → CP013 #829 → CP012 #827 → CP011 #825 → CP010 #822 and older CP source branches. **Original IV### Phase IV signed Weil form, NF### physical original HD/A numerical custody, and PI### independent gamma/prime comparison remain unchanged**.

**Crucial status:** This package consists of **three newly written external Zeta Lean v4.35 theorem SOURCE CANDIDATES (17 theorem declarations)**, independently derived mathematical inequalities and exact Fraction arithmetic, six real immutable upstream source Git hash/signature checks, an opt-in source preflight, and a fail-closed real Lean-kernel/standard-axiom verifier. **NO NEW CP013–CP020 .olean or actual CP020 Lean kernel receipt is available.** In particular, neither source-only arithmetic nor a no-sorry theorem candidate constitutes a completed Lean proof. Do not announce a new "original all-circle Lean PASS" until the opt-in compiler and all 17 actual `#print axioms` checks complete.

## 1. Exact genuine source problem and its fully quantified CP020 mathematical proof

The original upstream `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3` source:
- `Zeta/EulerMaclaurin/ErrorBound.lean`, Git blob `01184af0dbfd1369e14725e02e990b016bedfe6f`, defines the **genuine** `zetaRemainderBound z M N` and proves `norm_zetaRemainder_le` for complex `z` satisfying `Re z>-(2M+1)`.
- `Zeta/EulerMaclaurin/Continuation.lean`, Git blob `1bb01e946fa7e344497eaf7694fbecff0a714d09`, proves the exact original `riemannZeta_eq_approximant_add_remainder`.

Freeze (M=6), (N=256), (a=149.5), (b=150.05353), (s_t=1/2+it), and complex radius (r=1/4). For **every** (t\in[a,b]), and **every** (z\in\{|z-s_t|=r\}), prove:

[
\Re z\ge\tfrac14,\qquad
|z|\le\tfrac12+t+\tfrac14
\le150.80353<151.
]

Then exact source Borwein prefactor:

[
K(z)=\frac{|z+13|}{\Re z+13}
\le\frac{151+13}{13+1/4}
=\frac{656}{53}.
]

Original Mathlib `ascPochhammer_succ_eval` gives induction on n:
[
|(z)_n|\le\prod_{j=0}^{n-1}(151+j)
\quad\text{whenever }|z|\le151;
\qquad
|(z)_{13}|\le\prod_{j=0}^{12}(151+j).
]

The source `bernoulli` is a rational definition; exact recurrence gives (B_{14}=7/6). The actual source complex power satisfies

[
|256^{-z-13}|=256^{-\Re z-13}\le256^{-13}
]

by the genuine original `Complex.norm_cpow_eq_rpow_re_of_pos` and Mathlib's `Real.rpow_le_rpow_of_exponent_le`. Consequently, the original SOURCE bound function itself satisfies

[
egin{aligned}
\operatorname{zetaRemainderBound}(z,6,256)
&\le\frac{656}{53}\,
 \frac{7}{6\cdot14!}\,
 \frac{\prod_{j=0}^{12}(151+j)}{256^{13}}\\
&=\frac{181596617021805363}
       {633825300114114700748351602688}\\
&\approx2.865089433777896\times10^{-13}
<\boxed{3\times10^{-13}}.
end{aligned}
]

This is an **unconditional mathematical inequality** of the original bound function, valid throughout the family of complex circles. CP020 commits the corresponding universal original-source Lean **candidate theorem** `CP020BorweinCircle.original_Borwein_all_circles`. Unlike CP019's conditional theorem, CP020's new declaration takes **NO** `hBorweinOnCircle` premise. It uses two companion candidate proofs: exact source `CP020Pochhammer.original_bernoulli_fourteen` and source `norm_ascPochhammer_eval_le_product`, then original true complex-power and source real prefactor estimates. Its source proof is explicit, but **kernel acceptance is still pending**.

The source `original_EM_Cauchy_all_heights` combines it with CP019's original genuine Mathlib Cauchy theorem and original EM holomorphy source candidate to obtain for **every** k and t:

[
\boxed{
\left\|D^k R_{6,256}(\tfrac12+it)\right\|
\le k!\frac{3\times10^{-13}}{(1/4)^k}
= k!\,3\times10^{-13}\,4^k.
}
]

The source third-order specialization `original_EM_third_derivative_all_heights` gives (1152/10^{13}=1.152\times10^{-10}). These are **derivatives with respect to complex (s) of the original complex zeta Euler–Maclaurin remainder**, not the real Hardy-`Z` derivatives.

## 2. Independent second proof: original zeta EM germ identity transports to all complex derivatives

The genuine original published identity on the open domain ({\Re s>-13\}\setminus\{1\}) is

[
\zeta(s)-A_{6,256}(s)=R_{6,256}(s).
]

An equality holding on an **open complex neighborhood** implies equality of **all derivatives**. Mathlib's actual frozen `Filter.EventuallyEq.iteratedDeriv_eq` handles this rigorously: first prove equality of germs at a point, then transfer the `k`th iterated complex derivative. This route does not differentiate the absolute value inequality and does not assume a new zeta derivative bound.

New `CP020DerivativeTransport.lean` explicitly implements:
1. `original_zeta_EM_germs_equal`, using the real `riemannZeta_eq_approximant_add_remainder` and the open punctured source strip;
2. `original_zeta_EM_derivative_error_identity`, a true source-level `Filter.EventuallyEq.iteratedDeriv_eq` application for **all** k;
3. `original_center_valid`, exact proof Re((1/2+it))=(1/2), (s_t\neq1);
4. `original_zeta_approximant_derivative_error_all_heights`, source combination with the Cauchy budget;
5. `original_zeta_approximant_third_derivative_error_all_heights`, exact k=3 uniform bound.

Therefore, if the new original external v4.35 modules actually pass their kernels and accept source proof dependencies, then (zeta-A_{6,256}) satisfies the same uniform all-height k=0..3 derivative errors, exactly:

| Complex derivative order | Source-derived uniform error bound |
|---:|---:|
| (k=0) | (3\times10^{-13}) |
| (k=1) | (1.2\times10^{-12}) |
| (k=2) | (9.6\times10^{-12}) |
| (k=3) | (1.152\times10^{-10}) |

**No new source local `.olean` is currently accepted**; the bounds are solid mathematical calculations plus formal proof candidates, not yet trusted as repository kernel results.

## 3. Actual new Lean modules, exact source contracts and source SHA custody

New isolated `cp011_zeta_v435/` Lean modules:
- `CP020Pochhammer.lean` — **4** candidates: arbitrary n Pochhammer norm product bound, exact original Bernoulli (B_{14}), original real coefficient norm, nonnegative scalar product;
- `CP020BorweinCircle.lean` — **8** candidates: complex-circle geometry, Borwein prefactor, original complex power, omitted term norm, exact real product rational cap, universally quantified **source original all-circle bound WITHOUT hypotheses**, Cauchy all k, exact k=3 specialization;
- `CP020DerivativeTransport.lean` — **5** candidates: true original open-domain identity germ, original all-order complex derivative transport, positive-height source centers away from pole, uniform zeta approximant derivative errors all k, k=3 numeric bound.

Four Mathlib original `v4.35.0` files explicitly inspected and pinned:
- `Mathlib/RingTheory/Polynomial/Pochhammer.lean`, Git blob `f3503627af3430a48c087b85b03095e84dfb2824`, `ascPochhammer_succ_eval`;
- `Mathlib/NumberTheory/Bernoulli.lean`, Git blob `45d389886738789e80185fd2a6da4185727ab502`, exact recursively defined rational `bernoulli`;
- `Mathlib/Analysis/Calculus/IteratedDeriv/Lemmas.lean`, Git blob `d9348833bece1297dd8ffe57e6b976fcc268af38`, `Filter.EventuallyEq.iteratedDeriv_eq`;
- `Mathlib/Analysis/Complex/Liouville.lean`, Git blob `70382d63ec267d2704790b1d77692e1f5cd5faed`, genuine source Cauchy n-th derivative norm theorem.

The original two Zeta source SHA pins are provided above. Direct source hash/signature tests confirm the mathematical APIs exist. Source SHA verified is **not a substitute** for actual compilation of the three CP020 modules or any of the 15 inherited uncompiled CP013–CP019 modules.

The new `scripts/cp020_original_borwein_circle_fraction_source_gate.py` checks:
- the exact rational geometry endpoints and (	frac14) disk radius;
- independent Bernoulli (B_{14}) recurrence, including (B_{12}=-691/2730);
- exact Borwein prefactor and all 13 Pochhammer majorants;
- the exact numerator and denominator fraction and strict (<3/10^{13}) target;
- all k=0..3 Cauchy derivative caps, plus deliberate negative controls;
- six exact upstream original source Git hashes and true theorem signatures;
- all 17 new CP020 Lean theorem source names and their `#print axioms` commands.

A source pass emits status `CP020_ORIGINAL_SIX_BLOB_SOURCE_AND_FRACTION_PASS_NOT_KERNEL`, not LEAN PASS.

The new `scripts/cp020_original_Borwein_and_germ_kernel_axiom_audit.py` is strict: genuine original v4.35 compiled **3** new CP020 `.olean` and **15** preceding CP013–CP019 `.olean`, all **17** new printed standard-only axioms receipts, no `sorryAx`, no unproved `hBorweinOnCircle` source premise. Only genuine completed receipts may produce `CP020_ORIGINAL_ZETA_M6N256_BORWEIN_COMPLEX_CIRCLE_AND_DERIV_TRANSPORT_KERNEL_PASS`.

Two CI workflows are **strictly opt-in** and do **not** automatically activate on ordinary PR creation/update/push:
- `.github/workflows/cp020-original-borwein-six-immutable-sources-opt-in.yml`: explicit PR label `cp020-borwein-source` or eligible manual dispatch; six SHA and exact Fraction, NOT LEAN;
- `.github/workflows/cp020-original-borwein-circle-v435-kernel-opt-in.yml`: explicit PR label `cp020-borwein-lean` or eligible manual dispatch; ACTUAL external Lean 4.35 full 18-target build and standard-only axiom audit.

This protects the existing original NF###/IV### queue (inherited CP013 and CP014 source workflows remain queued). Neither CP020 source nor kernel workflow is presumed run at PR creation.

## 4. Preservation and remaining obligations

**Now mathematically explicit:** a genuine original complex-neighborhood Euler–Maclaurin remainder bound transports to complex derivatives of the original (zeta-A_{6,256}) difference. This is a theorem about source-faithful **holomorphic approximation control**, not the original signed Weil form. The complex phase and derivative identities remain distinct and must be separately certified before comparing the analytic/prime and spectral/zero projections.

**New CP020 proof-source obligation:** actual Lean acceptance of (B_{14}=7/6), the Pochhammer inductive norm inequality, source complex powers, universal circle estimate, and all-order iterated-derivative transport. Do not describe these source candidates as LEAN PASS until they compile. Source-level tactic failures must be repaired with concrete compiler logs.

**Still open after a genuine CP020 kernel success:**
1. A verified analytic/ball enclosure for the **finite** original (A_{6,256}) and its complex derivatives (zeta',zeta''), including full cancellation in the rotated real Hardy-(Z) second jet. Uniform error on (zeta-A) **alone** does not enclose the finite approximant's values.
2. Verified original phase (	heta) and (	heta',	heta'') balls and any necessary phase derivative remainders. The source **identities** and source **numerical enclosures** must not be conflated.
3. The true Hardy-(Z) derivative anchor (Z'(149.5)\ge12/5) and uniform curvature (|Z''(t)|\le4) on the entire frozen interval. CP018's eight-cell alternatives and source moment/phase cancellation remain available but unresolved.
4. A genuine original v4.35 Lean narrow critical-line zero existence certificate in ((150.05352,150.05353)). CP016 source-defined canonical rank 53 is distinct from that numerical root. Original phase-spectral equivalence and full signed Weil `Pole−Prime+Arch` 3×3 remain separately OPEN.
5. The inherited CP013–CP020 real Lean compiler backlog. Source proof candidates may require significant repair; NONE has been silently promoted.

**Next CP021:** recover real original kernel logs/repair source proof errors; produce rigorous validated *finite* original (A_{6,256}) analytic interval balls on the eight subintervals with ζ phase derivatives, and attach the Hardy-(Z) first derivative (\ge2.4) plus curvature (\le4) only after actual validated enclosures. Keep the original signed Weil–spectral 3×3 dictionary and global RH/Weil positivity separately OPEN.

**No global Weil positivity or RH claim.**
