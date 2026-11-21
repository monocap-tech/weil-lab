# PI023 — Canonical Haar conversion audit and the unmatched Gamma boundary-pole no-go

**PI### Potential Interface | ANALYTIC-ONLY | 2026-11-20.** Source parent: \`research/pi022-analytic-real-place-factor-two-falsifier\`. PI registry issue #792. Keep NF numerical Lean/CI work active and independent; preserve IV and CP analytic programs. **This stage adds ONLY this source-audit memo and a standalone exact rational script. No PR, Lean module, new Actions workflow, or kernel acceptance claim.**

## Executive result and strict boundary

Direct reinspection of the authentic 940-page November 2026 manuscript, Alessandro Maria Masullo, *The Music of the Primes*, https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf , confirms that the **real, complex and finite local coefficients in Theorem 12.5.1.1 are the canonical-versus-Tamagawa Haar conversion factors recorded in Appendix B.4.4.7**. Theorem 13.3.1.1 prints the same local principal-value symbols and \(d\mu_v\) measures WITHOUT these factors. No independent redefinition of the Chapter 13 \(\int'_{F_v^\times,\alpha_{v,0}}\) notation as a canonical-measure principal value was found in the inspected source. It is reasonable to suspect unfinished editing, especially given the author's explicit factor-of-two/\(2\pi\) warning, but **intentional typo versus an unstated alternate convention is UNRESOLVED; no manuscript correction is silently made**.

More strongly: in the \(F=\mathbb Q\), norm-radial, all-translations experiment of PI019–PI022, taking BOTH printed formulas literally and assuming the SAME pole, prime, Haar and zero-strip dictionary yields a **conditional impossibility**. The residual real Gamma kernel has a nonzero Laplace pole at \(s=-1/2\); the nontrivial zeta-zero divisor produces no pole there. An analytic continuation/residue argument therefore rules out their claimed equality **for all separated smooth phase tests under those explicit identifications**. This is a falsifier of that combined source interpretation, **NOT a proof that an unverified manuscript theorem fails under every possible intended convention, not RH, and not an identification of a corrected spectral operator**.

## 1. Source audit: where each normalization comes from

Reopened the actual PDF with page-image inspection (PDF index = printed page minus one):

| Printed page / PDF index | Source assertion |
|---|---|
| **519 / 518**, eqs. (12.5.1.1–12.5.1.3) | Real-place PV coefficient **1/2**; complex-place coefficient **1/(2π)**; finite place coefficient **log(q_v)/mu_v(O_v^×)**, all integrals displayed with \(d\mu_v\); full zero multiplicity \(N(c)\) on an allowed relative strip. |
| **520 / 519**, proof eq. (12.5.1.4) | The original global source kernel is matched to the full \(N(c)\) zero sum. No proof here of critical-line-only capped multiplicity or the Chapter 13 moment-domain extension. |
| **522 / 521**, eqs. (13.3.1.1–13.3.1.5) | Critical-line zero sum with \(N_{\rm spec}(c)=\min(N(c),[F:\mathbb Q])\); real/complex PV integrals **without 1/2 or 1/(2π)**; finite coefficient **log(q_v)** with no unit-volume denominator. The same \(\int'_{F_v^\times,\alpha_{v,0}}\cdots d\mu_v\) notation is printed. Unfinished “Theorem ??”, “Insert statement”, and “State and prove the Main Theorems” occur immediately below. |
| **560 / 559**, Definitions A.3.2 and (A.3.2.1–A.3.2.2) | For \(F=\mathbb Q\), \(\mu_\infty=dx/|x|\), \(\mu_p(\mathbb Z_p^\times)=1\), and the global compact-fiber Haar volume is \(\bar\mu_1(C_\mathbb Q^1)=1\). For general fields the finite unit volumes need not equal 1. |
| **619 / 618**, Prop. B.4.3.2 & Def. B.4.4.1 | Principal values on the **displayed** \(d\mu_v\) are defined as distributions relative to the source additive character. Changing the local additive character adds identity-supported terms; it does not multiply an integral away from the identity by 1/2. Footnote 16 explicitly calls for the factors **2 and 2π** to be checked. |
| **620 / 619**, eqs. (B.4.4.2–B.4.4.4) | \(\mu_{\rm can}=\mu_\infty/2\) at a real place, \(\mu_{\rm can}=\mu_v/(2\pi)\) at a complex place, and \(\mu_{\rm can}=(\log q_v/\mu_v(O_v^\times))\mu_v\) at a finite place. The source's \(\int'\cdots d\mu_v\) itself does not mean canonical measure. |
| **624 / 623**, Thm. B.4.4.7, eq. (B.4.4.16) | The actual idelic explicit formula has **\(1/M_v\)** for infinite places (\(M_v=2\) real, \(2\pi\) complex) and **\(\log q_v/\mu_v(O_v^\times)\)** at finite places. This independently corroborates the Chapter 12 coefficient pattern, NOT the bare Chapter 13 pattern. |

**Verdict on the requested source question:** Chapter 13's displayed real \(1\), complex \(1\), and finite \(\log q_v\) are **not a second documented canonical-Haar convention** in the inspected pages; they omit the explicitly defined conversion multipliers while writing \(d\mu_v\). The pattern and editorial flags make an incomplete transcription a plausible hypothesis, but **the author has not supplied a verified correction here**. Treat the **literal printed formulas** separately from the **hypothetically corrected canonical-measure version**.

## 2. Off-identity local comparison is impervious to PV/contact changes

At \(F=\mathbb Q\), for \(h\in C_c^\infty(\mathbb R;\mathbb C)\) whose support has positive distance from \(u=0\), define \(f_h(x)=h(\log|x|)\) on \(\mathbb R^\times\). It vanishes near \(x=\pm1\), so both local PV definitions act as ordinary integrals. With the SOURCE multiplicative Tamagawa Haar \(dx/|x|\), set
\[
K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}\quad(u\ne0).
\]
Splitting \(x=\pm e^u\) gives
\[
R_\mu(h)
=\int_{\mathbb R^\times} f_h(x)\frac{|x|^{1/2}}{|1-x|}\frac{dx}{|x|}
=2\int_{\mathbb R}h(u)K(u)\,du.
\]
Thus **the unedited Chapter 12 real term is \(\int hK\)** and **the Chapter 13 real term is \(2\int hK\)**. Their difference is \(\int hK\), a source-distributed non-contact functional.

For \(F=\mathbb Q\), the finite local volume factor \(\mu_p(\mathbb Z_p^\times)=1\) ensures the **printed finite-place coefficients** match, and \(\bar\mu_1(C_\mathbb Q^1)=1\) removes an otherwise additional global scaling. General fields retain additional complex and ramified-place questions. Two hypotheses remain explicit: the same global-to-local norm-radial lift/measure and the identical pole and finite geometric terms.

PI019's legitimate smooth phase tests use \(\rho_0\ge0\), nonzero, \(C_c^\infty\), \(\phi=\rho_0'\), \(a>\operatorname{diam}(\mathrm{supp}\rho_0)\), and \(D_e(a)=C(\cdot+a)+C(\cdot-a)\), \(D_o(a)=i[C(\cdot-a)-C(\cdot+a)]\) for \(C(v)=\int\phi(x)\phi(x-v)dx\). Both satisfy \(D(0)=\int D=0\) and are supported away from \(0\); \(\int D_eK<0\) and \(\int D_oK=0\). This family is therefore a **genuine smooth intersection-domain test**, not a point-mass approximation or the non-smooth PI018 Gamma compensator.

## 3. A stronger CONDITIONAL boundary-pole obstruction

### 3.1 What is assumed, not proved

Assume the following combined source dictionary **H023**:

1. Both printed Chapters 12 and 13 formula statements are valid for the norm-radial \(\mathbb Q\) lift of **every** \(D_e(a),D_o(a)\) for **all** \(a>d\), with a fixed allowed zero strip containing the compared nontrivial zeta zeros. This is not authenticated: Chapter 13's displayed proof is unfinished.
2. They use exactly the same global Haar disintegration, pole terms, prime terms and unrenormalized \(\mu_v\)-principal-value meaning **as printed**, with no extra unprinted spectral/cutoff correction. The page-619 and page-620 definitions are the standard reference.
3. The spectral difference on these radial tests has the PI020 form from a **locally finite zeta-zero divisor**, with multiplicities of at most polynomial counting growth: \(B(h)=Z_{12,I}(h)-Z_{13,\rm cap}(h)=\sum_j b_j\widehat h(z_j)\), where \(z_j=\gamma_j-i(\beta_j-\tfrac12)\). In particular there is **no term corresponding to a zero at \(\beta=0,\gamma=0\)**; for ordinary \(\zeta\), \(\zeta(0)=-1/2\ne0\). Trivial-zero conventions, source zero-strip selection and any character extras must be checked before applying this to the literal manuscript.

These are *testable missing premises*, not conclusions already furnished by the manuscript. We will derive a contradiction from their conjunction, **not** infer RH.

### 3.2 Exact paired phase reduction

Let \(\lambda_n=2n+\tfrac12\), and set
\[
R(z)=\int\rho_0(x)e^{izx}dx,\quad
t_j=b_jz_j^2R(z_j)R(-z_j),\quad
G(a)=\sum_jt_je^{iaz_j}.
\]
Schwartz decay on the bounded imaginary strip and the unconditional zero-counting estimate \(N_\zeta(T)=O(T\log T)\) give \(\sum_j|t_j|<\infty\). These facts do **not** assume RH.

PI020's exact transforms and PI022's **NONZERO** corrected real residual give, under H023,
\[
\begin{aligned}
B(D_e(a))&=G(a)+G(-a)=\int D_e(a;u)K(u)du,\\
B(D_o(a))&=i[G(a)-G(-a)]=\int D_o(a;u)K(u)du=0.
\end{aligned}
\]
Therefore for every \(a>d\),
\[
\boxed{G(a)=\tfrac12\int D_e(a;u)K(u)du
=\int C(v)K(a+v)dv.}
\tag{PI023-phase-equality}
\]

Now use the actual source physical Gamma expansion for \(a+v>0\),
\[
K(a+v)=\sum_{n\ge0}e^{-\lambda_n(a+v)}.
\]
Integration by parts for \(\phi=\rho_0'\) gives
\[
\int C(v)e^{-\lambda_nv}dv
=-\lambda_n^2P_n^-P_n^+,
\quad
P_n^\pm=\int\rho_0(x)e^{\pm\lambda_nx}dx>0.
\]
Consequently the exact necessary identity becomes
\[
\boxed{
G(a)=-\sum_{n\ge0}\lambda_n^2P_n^-P_n^+e^{-\lambda_na}
\quad\text{for ALL }a>d.
}
\tag{PI023-Gamma-series}
\]
This series is absolutely convergent for a>d. It is NONZERO, with a strictly negative first coefficient.

### 3.3 Meromorphic Laplace transforms force an impossible pole

Choose any \(A>d\) and put \(a=A+t,\ t\ge0\). On a common right half-plane of \(s\), the Laplace transform of (PI023-Gamma-series) yields
\[
\boxed{
\sum_j\frac{t_j e^{iAz_j}}{s-iz_j}
=-\sum_{n\ge0}
\frac{\lambda_n^2P_n^-P_n^+e^{-\lambda_n A}}{s+\lambda_n}.
}
\tag{PI023-meromorphic}
\]
The exchanges are justified: left weights are absolutely summable and \(|\Im z_j|<1/2\) for nontrivial zeros; right coefficients are exponentially summable because \(A>d\). Both sides therefore have meromorphic continuations, with locally finite candidate pole sets. The identity theorem extends the equality from the right half-plane across the complement of both pole sets.

The RHS has a simple pole at the **boundary point**
\[
s=-\lambda_0=-\tfrac12
\]
with exactly the NONZERO residue
\[
\boxed{
\operatorname{Res}_{s=-1/2}(\mathrm{RHS})
=-\tfrac14e^{-A/2}
\Bigl(\int\rho_0(x)e^{-x/2}dx\Bigr)
\Bigl(\int\rho_0(x)e^{x/2}dx\Bigr)<0.
}
\tag{PI023-boundary-pole}
\]

But every nontrivial zeta-zero frequency has
\[
iz_j=(\beta_j-\tfrac12)+i\gamma_j,
\quad 0<\beta_j<1,
\]
hence NO spectral pole at \(s=-\tfrac12\). In particular \(\zeta(0)=-1/2\ne0\), so even if a source zero-strip includes further zeros there is no genuine zeta zero at \(\beta=0,\gamma=0\). The LHS is therefore **holomorphic at \(s=-1/2\)**. This contradicts the nonzero RHS residue.

**PI023 SOURCE-NO-GO THEOREM (conditional, classical):** The three explicit assumptions H023 cannot all hold. Under the natural common radial/pole/prime/zero dictionary, the two **printed** trace formulas cannot simultaneously represent the same functionals on the *entire* two-phase translation half-line without an additional source correction. **No RH hypothesis is used anywhere in this contradiction.**

This is stronger than PI022's "nonzero local residual" observation: not only must the spectral difference equal the physical residual, it **cannot have the required lowest archimedean pole** if built solely from the stated nontrivial zeta-zero divisor.

**Scope and caution:** the source's full zero indexing \(\Omega(C_F)_I\), possible completed versus uncompleted L-conventions, and its allowed \(I\) are not proved to equal precisely the proposed \(z_j\) set. An extra spectral/regularization term having a pole at the boundary could invalidate H023(3), and a source-accurate canonical measure conversion invalidates H023(2). Such possibilities must be confronted openly, not ruled out by assertion. We have **not independently validated either theorem or any author's intended correction**, nor proved the actual global Weil form positive or RH.

## 4. Three distinct repair scenarios and their precise proof debts

**A — Explicit canonical-Haar correction (most direct editorial candidate).** Revise the Chapter 13 arch/finite coefficients to \(1/2\) real, \(1/(2\pi)\) complex, and \(\log(q_v)/\mu_v(O_v^\times)\) finite—or equivalently change its \(d\mu_v\) to an **explicitly defined canonical measure** and update all pole/global factors consistently. Then the PI022 local distributed residual vanishes on off-identity tests. This would restore PI021's **conditional** zero-divisor overlap equation, which is *so strong* that proving the revised Chapter 13 theorem would still require a real zero-location/multiplicity argument. Correcting a coefficient does not supply that proof.

**B — Source-authenticated spectral or cutoff boundary term.** Keep the unweighted real Chapter 13 integral but add an independently derived spectral/finite-part term whose translated Laplace transform has the missing \(s=-1/2\) pole, along with any required trivial-zero and unit-group contributions. No such term was identified in the Chapter 13 displayed theorem. One cannot insert it merely to make the PI023 calculation cancel.

**C — Demonstrably different test-lift or Haar/zero indexing.** Prove that the same-looking \(\varphi(g)\), \(d\mu_v\), \(\int'\) or relative strip in Chapters 12 and 13 denote different source objects, and provide an exact dictionary including their local/prime/pole differences. Such a dictionary would negate H023(1–3); it is not present in the displayed formulas inspected. Local additive-character changes can add identity-supported terms, but cannot change the off-identity \(\int D_eK\) factor.

Each repair requires a primary-source revision or an explicit derivation with all signs, Haar factors, and zero multiplicities. A text edit is **not** a proof of a spectral trace theorem.

## 5. Independent exact regression and custody

The no-go argument above uses genuine smooth derivative-bump tests and classical meromorphic continuation. A separate, intentionally limited \`fractions.Fraction\` script provides exact controls:
\`scripts/pi023_source_haar_boundary_pole_exact_preflight.py\`.

Independently executed Python preflight **PASS**:
- 14 rational-square \(u=\log q\) cases with exactly \(R_\mu=2K\) and \(R_{\rm can}=K\);
- 100 negative coefficients of the discrete signed two-atom **model**, which is NOT an admissible smooth test;
- 24 exact Laplace residue-isolation inequalities on finite model truncations and a synthetic strip-confined spectral sum;
- for the model at \(a=\log9\), the first RHS arch pole at \(s=-1/2\) has nonzero residue **\(-1/6\)**. This is a model check and is NOT the smooth-test residue (PI023-boundary-pole).

This regression does NOT calculate zeta zeros, execute a spectral trace, justify an original IV011 Lean theorem, or establish RH. The smooth residue nonvanishing is proved above from \(\rho_0\ge0\).

Only this memo and script were committed to
\`research/pi023-analytic-canonical-haar-and-boundary-pole-obstruction\`.
**No new PR, .lean module, or Actions workflow**. This respects the user's analytic-first mode and protects NF's numerical certification priority.

## 6. PI024 next — source correction before any renewed spectral equivalence conjecture

1. **Source-normalization matrix:** independently inspect any subsequent primary-source erratum/revision for the precise real \(1/2\), complex \(1/(2\pi)\), finite unit-volume factors, global compact-fiber Haar and pole terms. Pin the actual revised document bytes/date; never attribute an unobserved correction to the November manuscript.
2. **Zero-index dictionary:** determine whether the actual Chapter 12 strip includes only nontrivial ζ zeros, any trivial/arch boundary terms, or additional idelic characters. Identify whether any independently legitimate pole at \(s=-1/2\) enters the spectral **difference**. If none enters and the local coefficients remain as printed, the conditional no-go becomes a stronger verdict after test-space admissibility is paid.
3. **Full real/complex/finite place test:** for general number fields keep \(M_v=2\) or \(2\pi\) and \(\mu_v(O_v^\times)\) explicit. Demonstrate all off-identity local terms preserve the **same source-normalized** functional before claiming a spectral projection from the original signed Weil form.
4. **IV/CP communication:** the original IV signed n=9 phase amplitude and CP's finite zero roster cannot absorb the archimedean distributed residual. Use the paired phase tests with varying \(a\) as a source falsifier, not a claim of global RH.
5. **Formalization remains frozen** on PI/IV/CP until the analytic source compatibility is resolved. Keep NF compiler/CI recovery active; review existing CI without adding workload.

**PI023 verdict:** the displayed Chapter 13 geometry lacks the canonical Haar conversion factors recorded in the manuscript's own appendix. Under an explicit, source-plausible common normalization hypothesis, its difference from Chapter 12 produces an **unmatched \(s=-1/2\) Gamma Laplace pole** on smooth tests that satisfy both stated trace-domain restrictions. The resulting conditional no-go is precise and strong. It does not independently validate or refute the actual intended corrected theorem, and it proves neither global Weil positivity nor RH/GRH.
