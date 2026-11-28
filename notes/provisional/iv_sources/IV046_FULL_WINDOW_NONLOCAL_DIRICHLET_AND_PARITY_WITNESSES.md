# Weil-Lab — IV046
## Global source prime-shift Dirichlet identity; rigorous sixteen-cell parity witnesses; lower spectral gates remain OPEN

**Standing: ANALYTIC ONLY — exact Fraction preflight PASS, not newly Lean-kernel certified.** No GitHub branch, PR, commit, run, rerun, workflow or CI workload is generated. This memo is explicitly *not* a proof of full original Weil positivity, an independent spectral equivalence or RH.

### 1. Source contract and what is established

Use the **actual original** scalar signed Weil form on the unchanged symmetric physical window
\(I=(-11/10,11/10)\), extending all compactly supported test functions by zero to the line. From the real original IV011 mixed prime definition (`ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean`), the prime term is **both** signed translations with the exact von Mangoldt weights. Its only active terms on this window are \(n=2,3,4,5,7,8,9\), since \(2(11/10)<\log 10\). Let \(d_n=\log n\), \(\kappa_n=\Lambda(n)/\sqrt n\) (positive), and \((U_df)(x)=f(x-d)\).

The genuine NF599 Gamma positive-gain source and classically derived PI007/IV043 finite Fourier atom give the *mathematical*, **not yet source-attached Lean-certified**, logarithmic Gamma energy

\[
\Gamma[f]=\gamma(0)\|f\|_2^2+D[f],\quad
D[f]=\frac12\iint_{\mathbb R^2}\frac{e^{-|x-y|/2}}{1-e^{-2|x-y|}}|f(x)-f(y)|^2\,dx\,dy.
\]

The exact crossed Mellin residues are

\[
\mathrm{Pole}[f]=|\langle h,f\rangle|^2-|\langle k,f\rangle|^2,\quad
h=\sqrt2\,1_I\cosh(x/2),\quad k=\sqrt2\,1_I\sinh(x/2).
\]

All actual source complex-antilinear slot conventions, nonzero \(n=9\) contribution, actual gamma constant, and both signed pole moments are preserved.

### 2. New unsplit arithmetic Dirichlet representation

For every zero-extended \(f\in L^2(I)\), unitarity of translation gives the **exact** real identity
\[
\|f-U_{d_n}f\|_2^2
  =2\|f\|_2^2-2\operatorname{Re}\langle f,U_{d_n}f\rangle.
\]
Because the authentic original prime term is \(P[f]=2\sum_{n\in\mathcal N}\kappa_n\operatorname{Re}\langle f,U_{d_n}f\rangle\), with \(\mathcal N=\{2,3,4,5,7,8,9\}\), we get
\[
\boxed{P[f]=2S\|f\|_2^2-\sum_{n\in\mathcal N}\kappa_n\|f-U_{d_n}f\|_2^2},\quad S=\sum_{n\in\mathcal N}\kappa_n.
\]
No positivity of the prime operator was assumed; **this is an exact change of variables** preserving every phase and original prime-power coefficient.

Hence the **complete literal original signed form** is mathematically
\[
\boxed{W[f]=\mathcal E[f]-C\|f\|_2^2+|\langle h,f\rangle|^2-|\langle k,f\rangle|^2,}
\]
where
\[
\mathcal E[f]=D[f]+\sum_{n\in\mathcal N}\kappa_n\|f-U_{\log n}f\|_2^2\ge0,
\qquad C=2S-\gamma(0).
\]
The local Fraction audit supplies
\[
\boxed{12.447188526925153<C<12.44719164413214}
\]
(the displayed decimals are outward summary of exact rationals). The large **negative mass constant** \(-C\|f\|²\) and the negative **odd pole** remain. An unqualified statement that \(\mathcal E\ge0\) implies \(W\ge0\) would be false.

This explicitly reformulates the missing fixed-window positivity task as an **original-source nonlocal Poincaré inequality**. On even tests \(f\perp h\) and odd tests \(f\perp k\) the signed pole term vanishes, so the necessary and sufficient moment-null target is
\[
\mathcal E[f]\ge C\|f\|_2^2.
\]
On unrestricted even tests, the target is \(\mathcal E[f]+|\langle h,f\rangle|²\ge C\|f\|²\); on unrestricted odd tests it is \(\mathcal E[f]\ge C\|f\|²+|\langle k,f\rangle|²\). **No such global lower bound has been established by this memo.** The rewrite is basis-independent on the fixed original physical support, but is not a new external spectral projection or an operator equivalence with another construction.

### 3. Exact 16-cell piecewise-constant trials

Partition \(I\) into **16 consecutive equal rational intervals** \(I_j=(-11/10+(j-1)11/80,-11/10+j11/80)\), \(j=1,\ldots,16\). Every cell has width \(w=11/80\). Given a rational integer vector \(c=(c_1,\dots,c_8)\), set the coefficients on the right half to the reversal of \(c\) for the even trial and the **negative** reversal for the odd trial. Thus the finite-dimensional trials respect the actual reflection decomposition exactly, not approximately. No finite-dimensional approximation is used to infer **lower** infinite-dimensional spectral bounds.

For a single interval \(J\) with width \(w\), define \(a_n=n+1/4\), \(E(t)=\sum_{n\ge0}e^{-2a_nt}/a_n²\). The genuine full-line Gamma difference energy has exact interval Gram formulas
\[
D[1_J]=\frac{E(0)-E(w)}2,
\qquad D(1_{J_i},1_{J_j})=-\frac{E(g)-E(g+w_i)-E(g+w_j)+E(g+w_i+w_j)}4
\]
for disjoint intervals with gap \(g\ge0\). For touching intervals \(g=0\), use the full \(E(0)=\pi²+8G\) (Catalan constant \(G\)); the singular kernel is correctly integrated rather than assigned a fictitious pointwise value. The original prime integral is the exact physical overlap formula
\[
P[f]=2\sum_{n\in\mathcal N}\kappa_n\sum_{i,j}c_ic_j\operatorname{length}\bigl(I_i\cap(I_j+\log n)\bigr).
\]
The two real Mellin moments are direct sums of endpoint exponentials; the pole is \(2M_+(f)M_-(f)\), with its actual sign.

**All transcendental estimates are outward-rounded exact rational bounds**. IV046 pins the SHA-256 of the independently executed IV045 exact primitive checker, proves a source SHA dependency match, and uses its rational Machin \(\pi\), quarter Gamma, \(\log n\), \(\sqrt n\), Catalan, and exponential interval routines. The new script verifies every translated pair overlap with rational lower/upper bounds, computes \(E(t)\) with rigorous exponential/geometric tails, and rounds intermediate Fraction intervals **outward**, so arithmetic speedups cannot invalidate inequalities. As a regression, the all-one even and odd vector trials reproduce enclosures containing the accepted IV045 original full-interval even and sign-interval odd values.

Four **specified, nonoptimized finite-rank test coefficients** pass the exact-rational checks:

| Test | Left-half integer coefficients \((c_1,\ldots,c_8)\) | Rigorous normalized *full original* W interval | Constrained \(T/|\ell|²\) interval |
|---|---|---|---|
| Even low-energy | 189, 390, 574, 738, 846, 964, 1000, 989 | (0.00839320, 0.00862610) | (-0.997931, -0.997873) |
| Odd low-energy | 447, 783, 1000, 983, 791, 634, 421, 71 | (0.03638349, 0.03660985) | (1.097325, 1.097931) |
| Even constrained | 226, 441, 621, 773, 863, 978, 1000, 977 | (0.00850232, 0.00873517) | (-0.997960, -0.997903) |
| Odd constrained | 540, 847, 1000, 903, 665, 514, 323, 9 | (0.03763544, 0.03786028) | (1.092763, 1.093318) |

These decimals are **presentational outward approximations**. The executable checker uses rational comparisons, certifying especially
\[
\boxed{\inf\sigma(W_{\rm even})<\tfrac{87}{10000}=0.0087},\quad
\boxed{\inf\sigma(W_{\rm odd})<\tfrac{367}{10000}=0.0367},
\]
\[
\boxed{A_e<-\tfrac{9979}{10000}=-0.9979},\quad
\boxed{A_o<\tfrac{547}{500}=1.094}.
\]
The piecewise-constant trials are in the source Gamma log-form domain, not Schwartz. For each piecewise-constant trial inside \(I\), first shrink boundary portions slightly, then convolve with parity-preserving smooth mollifiers. The original logarithmic Fourier symbol and the finite-jump Gamma energy give convergence in the Gamma form norm; the prime shift forms and pole moments are \(L^2\)-bounded. This is the **classical analytic transfer** of upper Rayleigh/constrained test bounds to genuine supported complex Schwartz tests. Its Lean source-domain proof remains open.

The stronger new even upper coefficient is at least four times smaller than IV045's 0.0405 limit. These very small *upper* bounds **do not show any positivity** of an entire sector, nor do they calculate true lowest eigenvalues.

### 4. Exact zero-mode-safe parity gate, tightened but NOT resolved

IV045's index-free criterion remains the proper research target:
\[
W_e\ge0\iff T_e|_{h^\perp}\ge0\ \text{and }A_e\ge-1,
\quad
W_o\ge0\iff T_o|_{k^\perp}\ge0\ \text{and }A_o\ge1.
\]
Our exact tests only give **upper** bounds on the unknown constrained infima. Therefore if full original signed W were nonnegative on this fixed window, necessarily
\[
\boxed{-1\le A_e<-0.9979,\qquad 1\le A_o<1.094.}
\]
We have **not** proved either left-hand inequality; both may fail. Rigorous lower enclosures of the actual infinite-dimensional, closed-form operators are now indispensable. Small projected matrix eigenvalues, even if positive in every tested grid, do not prove a positive lower bound in the full domain. A future lower certificate must pay the complementary high-frequency tail, enforce true pole moment constraints, include n=9, and prove the source Gamma Fourier atom/limit at the actual source SHA.

### 5. Compiler and operational observation

Read-only inspection of existing GitHub Actions detects another concrete CI failure. **IV018** existing run [44850967574](https://github.com/monocap-tech/weil-lab/actions/runs/44850967574), job 136719449330, completed **FAILURE at the Python source preflight** with `AssertionError: ('Missing original source dependency', PosixPath('lake-manifest.json'))` from `scripts/iv018_original_three_cell_coercivity_audit.py`, line 177. Source Lean toolchain, both genuine original three-cell kernel builds, and 20-new/8-upstream strict axiom audits were **skipped**. No new Lean PASS, but also no Lean proof failure. IV023 run [44854690456](https://github.com/monocap-tech/weil-lab/actions/runs/44854690456) had the **same missing lake-manifest.json** Python preflight failure earlier; its Lean build was likewise skipped. This common failure signature suggests a source-checkout/preflight dependency invariant that should be triaged when the CI hold permits coordinated repairs. Do **not** manufacture a successful run or change source to bypass integrity checks under the current hold.

Repaired original IV009 Schwartz polarization and strict Lean axiom audit remain **PASS**. NF750–NF753 true original-source numerical Lean/axiom audits remain accepted, authentic original HD/A frontier **692/968** (71.49%). This is gate custody, not full physical matrix enclosure or global Weil positivity. Latest repository-wide queued count at read-only check: **384** (volatile). The fall does NOT itself prove restoration of healthy runner throughput.

### 6. Reproducibility, open hypotheses, and IV047

Files in the active conversation:
- `IV046_FULL_WINDOW_NONLOCAL_DIRICHLET_AND_PARITY_WITNESSES.md` — source dictionary, exact formula and proof, four explicit variational witnesses, gate/certification limitations.
- `IV046_fixed_window_multicell_variational_checker.py` — **executed** pure-stdlib exact Fraction interval arithmetic, with SHA-pinned predecessor.
- `IV046_fixed_window_multicell_variational_receipt.json` — source/checker SHA-256, outward rational checkpoints, all four source terms per witness.

**Outstanding:** fully source-validated Lean Gamma inverse and closed form; rigorously positive/no-negative lower operator bounds on \(T_e\) restricted to \(h^\perp\) and \(T_o\) on \(k^\perp\); true constrained lower \(A_e\ge-1, A_o\ge1\); complete global Weil positivity for arbitrary supported Schwartz inputs, independent semilocal operator-map equivalence, and RH.

**Next IV047 analytic-only:** devise an infinite-dimensional lower-enclosure strategy for the **positive combined** quadratic energy \(\mathcal E=D+\sum_n\kappa_n\|f-U_{\log n}f\|²\) against explicit mass threshold \(C\), with a genuinely certified tail bound and the two moment constraints. Test for counterexamples before claiming success. Allow IV018/IV023 repair only through controlled CI recovery after the user-directed hold lifts.
