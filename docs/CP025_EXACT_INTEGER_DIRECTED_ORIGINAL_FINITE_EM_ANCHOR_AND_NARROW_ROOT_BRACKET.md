# Weil-Lab — CP025
## First original source-faithful, integer-directed narrow root-sign and (Z'(149.5)) enclosure for (M=6,N=256)

**Track:** independent CP### original analytic/spectral cross-projection chain, stacked on CP024 PR #846 → CP023 #845 → CP022 #844 → CP021 #843 → CP020 #842 → CP019 #840. Original IV### signed Weil support extension, NF### numerical acceptance and PI### pole/prime/Gamma comparison are unchanged. CI remains source-only opt-in, never ordinary push/PR fan-out.

### Precisely what is new and what is NOT

**NEW:** a reproducible, integer-directed interval algorithm evaluating the ACTUAL original published finite Euler–Maclaurin approximant (A_{6,256}), its **complex first derivative**, and the ACTUAL original theta-Stirling **order-two** phase at the rational heights (149.5), (150.05352), (150.05353). Every transcendental evaluation is bounded by elementary **rational Taylor tails** and every intermediate computation is rounded OUTWARD at (10^{55}) fixed integer scale, not mpmath. The result includes conservative published original theta/Gamma/derivative errors and source-derived original zeta remainder allowances, and establishes **strict external arithmetic enclosures** for two root signs and the first derivative anchor.

**TRUST LEVEL:** the numerical inequalities have been independently executed in local Python integer/Fraction arithmetic and passed, and all six upstream original source Git blob SHAs and theorem signatures were checked directly. They are **external mathematical interval enclosures conditional on source-derived analytic comparison lemmas that still require new Lean integration**, **not original Lean v4.35 kernel accepted theorems**. In particular, the original original `CP021BorweinLeaf`, `CP021GermLeaf`, full CP019 holomorphy/Cauchy integration, CP024 uniform Gamma phase formal bridge, and CP010 original root bracket attachment do not have new genuine `.olean` or standard-only `#print axioms` receipts. Do not conflate a source-only SHA pass, Python output or external sign-bracket enclosure with a kernel certificate.

### 1. Original six-source fidelity

Original frozen external `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`, with six directly re-fetched immutable Git blob SHA+theorem-interface checks, ALL PASS:

| Original source | SHA | Exact source fact |
|---|---|---|
| `Zeta/EulerMaclaurin/Continuation.lean` | `1bb01e946fa7e344497eaf7694fbecff0a714d09` | `zetaApproximant`: **255** (n^{-s}) terms (1≤n<256); pole correction, half term, six Bernoulli–Pochhammer terms |
| `Zeta/EulerMaclaurin/ErrorBound.lean` | `01184af0dbfd1369e14725e02e990b016bedfe6f` | published `norm_zetaRemainder_le` for the **actual** original (R_{6,256}) |
| `Zeta/Zeros/HardyZ.lean` | `9975442b0c14011c35f4624197d0bf26169c7665` | original `hardyZ`, **published** `abs_riemannSiegelTheta_sub_approximant_two_le` gives (|\theta(t)-\widetilde\theta_{2,0}(t)|≤12/t^4) for (t>0) |
| `Zeta/Gamma/LogGammaStirling.lean` | `50b98a2a3dfef8cb4e6d77de82d33ac52c8ecaca` | original exact `logGammaStirling_two`: (\mathrm{Im}[(w-1/2)\Log w-w+\frac12\log(2π)+\frac1{12}w^{-1}-\frac1{360}w^{-3}]) |
| `Zeta/Gamma/DigammaStirling.lean` | `9b5a21dfefe6c778411b03fc7e0cf8e8c5bcfac8` | original genuine `norm_digamma_sub_log_le'`, controls original theta first-derivative approximation error |
| `Zeta/Gram/Averaging.lean` | `6a30171433903a57736de2ab83b120ef660e08bd` | genuine `hasDerivAt_riemannSiegelTheta` |

The exact original approximant is

[
A_{6,256}(s)=
\sum_{n=1}^{255}n^{-s}
+\frac{256^{1-s}}{s-1}
+\frac12\,256^{-s}
+\sum_{k=1}^6\frac{B_{2k}}{(2k)!}(s)_{2k-1}\,256^{-s-(2k-1)}.
]

It is NOT the Riemann–Siegel 52-term approximant, a substitute Dirichlet cutoff, or a made-up scaled proxy. Bernoulli numbers (B_2,B_4,B_6,B_8,B_{10},B_{12}) are independently computed by an exact Fraction recurrence and checked against (1/6,-1/30,1/42,-1/30,5/66,-691/2730). Its (s)-derivative is calculated **symbolically term by term** in the interval engine, including the derivative of the pole term and each Pochhammer polynomial; it does **not** differentiate an original value-only numerical error bound.

### 2. Original finite-phase evaluation, with actual published source theta error

For (t>0) let (s_t=1/2+it), (w_t=1/4+it/2), and

[
\widetilde\theta(t)=
\Im\Big[
(w_t-\tfrac12)\Log w_t-w_t
+\tfrac12\log(2\pi)+\tfrac1{12}w_t^{-1}
-\tfrac1{360}w_t^{-3}
\Big]-\tfrac t2\log\pi.
]

This is literally the original source `riemannSiegelThetaApproximant 2 0 t`, via the original theorem `logGammaStirling_two`. In exact elementary real terms the algorithm evaluates

[
\widetilde\theta(t)=
\frac t2\left(\log|w_t|-\log\pi-1\right)
-\frac\pi8+\frac14\arctan\frac1{2t}
+\frac1{12}\Im(w_t^{-1})-\frac1{360}\Im(w_t^{-3}).
]

The published original theorem (already upstream formalized, separate from new local theorem candidates) gives

[
\boxed{
|\theta(t)-\widetilde\theta(t)|\le\frac{12}{t^4}.
}
]

The original first phase derivative is (\theta'(t)=\frac12(\Re\psi(w_t)-\log\pi)). Define the **directly evaluable first-order Stirling approximation**

[
\widetilde\theta'_0(t)=
\frac12\big(\log|w_t|-\log\pi
-\Re[(2w_t)^{-1}]\big).
]

For these three heights (|w_t|>74), the original published `norm_digamma_sub_log_le'` at (a=1/4) and (π>3) give the rigorous **mathematical bound**

[
\boxed{
|\theta'(t)-\widetilde\theta'_0(t)|<1/10000.
}
]

CP024 independently derived the **uniform phase bound** (\theta'(t)≤9/5) on ([149.5,150.05353]) from original Stirling–Cauchy and logarithm inequalities; its new Lean glue is UNCOMPILED.

### 3. Exact signed integer interval arithmetic, NOT floating sampling

The source engine `scripts/cp025_original_EM_integer_directed_firstjet_root_bracket.py` evaluates everything on a (10^{55})-scaled integer lattice, rounding DOWN on lower and UP on upper interval endpoints for every addition/multiplication/division.

* (\pi=16\arctan(1/5)-4\arctan(1/239)) with exact rational alternating arctangent series tails (Machin identity).
* Positive real (log x) via power-of-two range reduction and (\log u=2\sum_{j≥0}y^{2j+1}/(2j+1)), (y=(u-1)/(u+1)in[0,1/3]), with explicit geometric remainder (\le2y^{2N+1}/((2N+1)(1-y^2))).
* (n^{-1/2}) for (1≤n≤255) via exact `math.isqrt` integer lower and upper enclosures.
* (\sin,\cos) at each rational-height angle (t\log n) using an integer phase-reduction multiple of (2π), **validated by a strict resulting ([-4,4]) enclosure**, then 50 Taylor terms and explicit Lagrange errors bounded by (4^{101}/101!), (4^{100}/100!). A floating conversion only chooses the integer multiple, not the values, bounds or acceptance.
* Actual complex arithmetic (A(s),D_s A(s)) via rectangular interval arithmetic and exact polynomial product-rule recursion. Complex norms upper-bounded by exact rational integer-square-root ceiling.
* (widetilde\theta,\widetilde\theta'_0) via the exact original source expressions and elementary analytic remainder bounds; both point values are rational heights, not rounded input floats.

All computed values and interval/error margins are derived from the original frozen formulas and elementary rational certificates; a separate **high-precision mpmath calculation** only screened the expected locations and matched 20+ digits, **not used in the acceptance code**.

The audit includes exact Bernoulli recurrence, scale/floor/ceiling arithmetic negative controls, exact (\pi,\log2) benchmark enclosures (benchmarks are assertions, not inputs), source theorem names and SIX immutable original source SHA pins. No `sympy`, `mpmath`, `numpy` or external numeric dependency is needed to issue the exact arithmetic certificate.

### 4. Mathematical error transfer and the three strict numeric enclosures

Define the EXACT true original Hardy (Z(t)=\Re[e^{i\theta(t)}\zeta(1/2+it)]), and write (Z_A(t)=\Re[e^{i\theta(t)}A_{6,256}(s_t)]), (Z_R(t)=\Re[e^{i\theta(t)}R_{6,256}(s_t)]).

For each endpoint, the integer engine computes (widetilde Z_A(t)=\Re[e^{i\widetilde\theta(t)}A_{6,256}(s_t)]). The mathematically justified error inequality is

[
|Z(t)-\widetilde Z_A(t)|\le
|A_{6,256}(s_t)|\frac{12}{t^4}+\frac3{10^{13}}.
]

Here **the phase bound is a published original Zeta Lean theorem**, while the uniform source (R) cap is proved as a mathematical original Borwein rational bound in CP020/21 and represented by **NEW original v4.35 Lean source proof CANDIDATES without accepted compiler receipts**. Original published `norm_zetaRemainder_le` carries the analytic source-to-error implication. No assumption that a raw finite Dirichlet sum equals ζ is made.

At the derivative anchor (a=149.5), the interval engine evaluates the exact *source complex approximant derivative* (A'_{6,256}(s_a)) and

[
\widetilde D_A(a)=
\Re\left[
e^{i\widetilde\theta(a)}i
\left(\widetilde\theta'_0(a)A_{6,256}(s_a)+A'_{6,256}(s_a)\right)
\right].
]

Its error is bounded, **without differentiating a scalar value-only inequality**, by

[
\begin{aligned}
|Z'(a)-\widetilde D_A(a)|
\le{}&
\underbrace{\frac{12}{a^4}}_{\delta_\theta}
\left[
(|\widetilde\theta'_0(a)|+10^{-4})|A_{6,256}(s_a)|
+|A'_{6,256}(s_a)|
\right]\\
&+\underbrace{10^{-4}}_{\delta_{\theta'}}|A_{6,256}(s_a)|
+\frac{87}{5\cdot10^{13}}.
\end{aligned}
]

The final term is the CP024 **source-derived, not yet NEW LEAN kernel-accepted** complex zeta remainder derivative budget, with the original phase bound. **All terms are explicitly enclosed by outward integer intervals.**

External exact rational interval preflight (conservative outward decimal enclosures):

| Original object at exact t | Lower | Upper |
|---|---:|---:|
| (Z'(149.5)) | **2.4426** | **2.4429** |
| (Z(150.05352)) | **−0.000000682** | **−0.000000681** |
| (Z(150.05353)) | **+0.000015519** | **+0.000015520** |

Strict inequalities hold. The external unrounded interval has a lower derivative bound approximately **2.442616685493**, and the endpoint sign enclosures are decisively separated from zero. A much looser first-derivative error contribution (10^{-4}|A|approx1.2\times10^{-4}) was deliberately retained; these are NOT unsupported last-digit extrapolations.

Thus, **mathematically, under the explicitly source-grounded analytic comparison bounds above**, the external interval enclosure proves

[
\boxed{
Z'(149.5)>2.4426>12/5,
}
]

and

[
\boxed{
Z(150.05352)<0<Z(150.05353).
}
]

The original upstream Zeta Hardy-`Z` continuity and critical-line zero equivalence then imply **a genuine original critical-line zeta zero exists in the open narrow bracket ((150.05352,150.05353))** at the external analytic/arithmetic level. This is NOT the more specific statement that it is the *53rd* zero, or that a Lean kernel has accepted its existence. Original CP016 canonical index #53 and original 149.5 zero-count attachment still require genuine kernel receipt and independent zero-rank reconciliation.

**New mathematical separation:** the root EXISTS from opposite signs and continuity WITHOUT first proving global (Z'(t)>0) over the entire 0.55353 height window. The CP017 (|Z''|≤4) route is one sufficient route for strong monotonicity/uniqueness, not a prerequisite for this particular bracketing existence proof. The global curvature gate remains OPEN.

### 5. Actual execution status and fail-closed provenance

The new Python file was developed and tested in the active container from exact integer/Fraction arithmetic, with all source constants, six Bernoulli values, three heights, complex first derivative, theta approximation and error bounds, and ALL strict interval assertions passing. Its output status is **`CP025 ORIGINAL M6N256 INTEGER DIRECTED FIRST-JET + NARROW BRACKET: PASS NOT LEAN`**, never `LEAN PASS`.

Its `--receipt` mode **fails closed** unless both `--self-test` AND `--original-zeta` (six actual immutable original upstream Git blob SHA+theorem-signature checks) run successfully. That JSON explicitly sets:
- external exact interval sign/first derivative success = true,
- actual NEW original v4.35 Lean `.olean` / strict axiom acceptance = **false**,
- source ordinal 53 exact-root attachment = **false**,
- original whole-interval strict monotonicity / curvature ≤4 = **false**,
- original signed Weil complete spectral-form compatibility = **false**,
- global Weil positivity and RH = **false**.

The existing opt-in only source workflow `.github/workflows/cp021-original-independent-leaf-source-only-opt-in.yml` now downloads TWO additional primary source files (`HardyZ.lean`, `LogGammaStirling.lean`) beyond CP024's original 4 relevant files and runs the CP025 exact integer certificate, six SHA gates, strict JSON/negative controls. **No new workflow file, NO ordinary push/PR-created/synchronize CI fanout, and NO heavy NF/IV job started.**

Live inherited CP021 head #843 Actions: CP013 original source-lineage workflow `44878586071` now **completed with success**, as has CP014 original source-lineage workflow `44878586072`. Those are **source-lineage** successes, not NEW CP021–25 complete Lean kernel theorem acceptance.

### 6. The open interfaces after CP025

1. **Kernel:** original Zeta v4.35 source proof acceptance of the independent `CP021BorweinLeaf` and `CP021GermLeaf`, and of actual original complex Cauchy/phase-transfer proof `CP019...`, (\theta',\theta'') CP024 glue. No source-only Git SHA or Python interval can replace a genuine standard-only `#print axioms` and `.olean`.
2. **Original root existence inside Lean:** embed the conservative *external interval enclosures* as actual kernel-checked rational inequalities over original definitions and apply original continuity+IVT and Hardy-`Z`–ζ zero equivalence. Do **not** treat printed JSON booleans as kernel axioms.
3. **Original zero rank:** certify or reconcile the exact original source 52-root Euler count and original canonical RS index 53, including the strict source predecessor/successor boundaries. Existence of some zero in the narrow bracket does not establish it is #53.
4. **Monotonicity/uniqueness:** the original CP017 endpoint derivative + whole-interval (|Z''|≤4) curvature obligation remains OPEN; CP025's point derivative proof does not establish global curvature or uniqueness.
5. **Weil:** original signed Pole−Prime+Gamma (3×3) comparison against the COMPLETE normalized spectral/zero-side form, all collar phases/masses, support-independent positivity and RH remain **OPEN**. Local original ζ critical-line zero certification is NOT equivalent to RH or a global signed Weil positivity proof.

**Next CP026:** create actual original-v4.35 Lean attachment obligations for the explicit three rational point enclosures WITHOUT adopting their truth as axioms. Obtain real leaf compiler receipts when NF/IV capacity permits. Separately pursue original finite (Z_A'') validated **whole-interval** enclosure for CP017 uniqueness, and source-rank 53 attachment only after the original 52-root predecessor count is genuinely checked.

**NO global signed Weil positivity or RH claim.**
