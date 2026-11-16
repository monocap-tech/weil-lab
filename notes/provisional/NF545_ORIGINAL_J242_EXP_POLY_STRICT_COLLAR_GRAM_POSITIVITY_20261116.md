# NF545 — Source-specific J242 exponential-polynomial independence and strict two-collar Gram positivity

**2026-11-16 PT. Source-exact, analytic uniqueness proof + independent exact-rational node audit, stacked on NF544 draft #572. Lean rational-signature module and source verification workflow PENDING actual Actions receipt.** Original NF407 selected basis JSON SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`. Original NF500 selected-moment custody JSON SHA256 `7e261d540c8b658bced4b44d1bf998c23ef7f975fc07daa0f30ae6438dcffb05`. Original NF494 U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181` unchanged. Original 242 selected modes, genuine sinh pole, (B=11/10,\delta=1/500) strict two collars, all true zeta divisor copies unchanged.

## 1. The exact source-specific structural certificate

The unmodified NF407/NF505 `original_selected_generator_node_orders` contains **241 oscillator rows** from exactly **67 distinct strictly positive rational frequencies** (f). Each frequency appears in one contiguous monomial block (k=0,1,\ldots,m_f-1). The final original selected row, index 241, is precisely the sinh-pole (\sinh(x/2)). The selected generators are

```
j_{f,k}(x) = x^k sin(2π f x)   for k even,
j_{f,k}(x) = x^k cos(2π f x)   for k odd,
j_{241}(x) = sinh(x/2).
```

This is not the six-polynomial NF523 control or a new selected family. The exact rational source audit reads the SOURCE file, verifies SHA256, checks all 242 positions and all 67 complete block lengths and compares the exact `ℚ × ℕ` table compiled into the new Lean module. Frequencies range from (37/64) to (113013/128) in the source's original order. Their grouping is not an approximation or frequency-phase fit.

## 2. Direct mathematical proof of original J242 analytic independence

Suppose a complex linear combination of the original 242 (j_i) vanishes on a nonempty real open interval (U\subseteq E). Every (j_i) is an entire function of (z), so analytic uniqueness implies that the combination vanishes for all (z\in\mathbb C).

Write the full original combination as a finite exponential polynomial,

```
F(z)= Σ_{λ ∈ Λ} P_λ(z) exp(λ z),
Λ={±2π i f: f in the 67 exact original rationals} ∪ {±1/2}.
```

For each oscillator group, its polynomials at (\pm2π i f) are explicit mixtures of the even-order sine and odd-order cosine monomials, while the two pole polynomials are opposite nonzero constant multiples of its original coefficient. Because all 67 (f>0) are distinct rationals and (\pi>0), **all 136 characteristic roots (λ\in Λ) are distinct**, including real pole roots (\pm1/2) versus all imaginary oscillator roots.

Fix (λ\inΛ). With (D=d/dz), apply to (F=0) the differential operator

```
L_λ = ∏_{μ∈Λ, μ≠λ} (D-μ)^{deg(P_μ)+1}
```

(allow any exponent at least the fixed finite source block order, even if some (P_μ=0)). Every term with (μ≠λ) is annihilated, giving

```
exp(λz) [ ∏_{μ≠λ} (D+(λ-μ))^{deg(P_μ)+1} ] P_λ(z) = 0.
```

For nonzero (a\in\mathbb C), (D+a) is injective on polynomials: the leading coefficient of (aP+P') is (a) times the leading coefficient of (P). As (λ-μ≠0), every factor above is injective; hence (P_λ=0). This holds for every characteristic root. For each original frequency the `+` polynomial has even-degree coefficients from sine terms and odd-degree coefficients from cosine terms, in disjoint monomial degrees, so all its original (c_{f,k}=0); the two distinct real pole roots then force (c_{241}=0).

**Therefore the EXACT unchanged original 242 selected functions are linearly independent on EVERY nonempty real open subinterval, including each original terminal collar.** This is a complete analytic source-specific linear-independence proof, not a claim of compiled Mathlib exponential-polynomial uniqueness. Its finite source premises are checked by the independent source-SHA-pinned exact audit and the Lean rational signature candidate.

## 3. Explicit even smooth cutoff supported INSIDE original E

Set
```
B=11/10, δ=1/500, c=B-δ/2=1099/1000, r=δ/4=1/2000,
ρ(t)= exp(-1/(1-t²)) if |t|<1, and 0 otherwise,
χ(x)=ρ((x-c)/r)+ρ((x+c)/r).
```

Standard flat-bump regularity gives (χ\in C_c^\infty(E)), (χ\ge0), even, and strictly positive on ((c-r,c+r)) and its negative reflection, both compactly contained in the **original** (E=(-B,-B+δ)\cup(B-δ,B)). The exact-rational audit independently checks (B-δ<c-r<c+r<B) and the reflected inequalities.

Define (b_j=χj_j\in C_c^\infty(E)); since every original (j_j) is real odd and (χ) is real even, each (b_j) is real odd. No 242-dimensional numerical inversion or condition-number assertion is necessary.

With the true original complex-linear physical moments (M_i(f)=\int_{-B}^{B}\overline{j_i(x)}f(x)dx), the true weighted Gram (G_{ij}=\int χ(x)j_i(x)j_j(x)dx) satisfies for every nonzero (d\in\mathbb C^{242}),

```
Re Σ_i conj(d_i) (G d)_i
= ∫ χ(x) |Σ_j d_j j_j(x)|² dx > 0.
```

The strict inequality follows because the analytic linear combination cannot vanish identically on the nonempty open (χ>0) region; where nonzero, it remains nonzero on a smaller open interval of positive Lebesgue measure. Thus the **exact source-specific Hermitian positivity premise** isolated by NF544 follows ANALYTICALLY for the original family on E. It is not merely an assumed generic positive definite matrix.

Consequently NF544's explicit finite-dimensional inverse (R=B\circ G^{-1}) is analytically available for the real original source and preserves strict collar support, all 242 moments and the real-odd symmetry. The original (C_c^\infty(E)) corrected approximants satisfy the true same-source log-domain entry once NF542's generic Schwartz theorem is compiler-accepted. The original singular (\ell_U) is **not** claimed (H^1).

## 4. Uniform full true-divisor graph membership for each fixed correction column

Every (b_j\in C_c^\infty(E)), hence all `b_j`, (b_j') vanish at support endpoints. For the actual two-source Fourier evaluation (F_b(z)=\int b(x)e^{izx}dx) and zero strip `|Im z|≤1/2`, integration by parts twice gives

```
|F_b(t+i u)| ≤ e^{B/2} ‖b''‖₁/t² (|t|≥1),
|F_b(t+i u)| ≤ e^{B/2} ‖b‖₁ (all t),
|F_b(t+i u)| ≤ C_b/(1+t²),
C_b = 2 e^{B/2}(‖b‖₁+‖b''‖₁).
```

The genuine (P/N) combinations with `1/√2` obey by the parallelogram identity `|p_+|²+|p_-|²=|F_b(\bar z)|²+|F_b(z)|²≤2 C_b²/(1+t²)²`. On the original multiplicity-preserving dyadic band `2^n≤|t|<2^{n+1}`, use the already established unconditional genuine divisor count `#D_n≤A(n+2)2^n` to conclude for (N≥0)

```
Σ_{n≥N} Σ_{q∈D_n} (|p_+(b_j;q)|²+|p_-(b_j;q)|²)
 ≤ 2 A C_{b_j}² Σ_{n≥N}(n+2)8^{-n}
 = 2 A C_{b_j}² (56N+120)/(49·8^N).
```

The rational tail formula is checked symbolically by its exact recurrence plus decay. The analytic proof establishes that each of the **actual fixed 242 correction columns** has square-summable positive AND negative true-divisor samples with all multiplicity copies. Since there are finitely many columns, their Gram-correction synthesis (R) has bounded range into the complete actual (P/N) graph, provided the graph is instantiated as the closure of actual physical source sampling. This avoids assuming that Green packets are dense in the entire source graph. The proof is ANALYTIC; source-graph Lean implementation is still open.

The original (\ell_U) graph approximation itself remains the NF524/NF528 analytic result and **is not proved by source-column membership alone**.

## 5. Promotion conditions and honesty boundary

**What NF545 resolves analytically:** exact original frequency/signature audit; all-242 **original** analytic independence on any open collar interval; a canonical true strict-two-collar even positive smooth (χ); genuine source-specific Hermitian positive Gram and hence NF544's R; and every correction column's full true-multiplicity (P/N) graph square summability with an explicit dyadic tail.

**What the new Lean signature module establishes if CI succeeds:** ONLY the exact original rational frequency-list count, frequency distinctness/positivity and multiplicity sum. It does **not** formalize the analytic-uniqueness differential-operator proof or the weighted Gram positivity. Nor does it instantiate the actual (j_i), (χ), (M) and (R) as Lean functions.

**Remaining formally open:** NF542→544 compiler repairs, actual j_i exponential-polynomial identity in Lean, the explicit true 242 weighted χ Gram positivity and C∞ bump in Lean, authentic full-divisor graph closure/approximation, NF527 true gamma+n9 prime+both poles coercivity, NF539 signed graph formula, original source nonzero sign, global W_ODD_NEG and RH.

**No source substitutions, main merge, accepted odd-branch sign, or RH assertion.**
