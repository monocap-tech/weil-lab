# RC313 — original Weil prime and signed-pole distributional identification on the complete polynomial core

**Parent:** RC312 merged \`96cb955efc0682b42e505197b63d120140b7a353\`.  
**Pinned original source:** CC27 native Weil form, Git blob \`e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482\`.  
**Standing:** Stage I positivity, a positive full spectral lower bound, signed Chebyshev inverse response, 314-Schur, F4, RH and complete Lean formalization remain **OPEN**.

## 1. The original source, not an interpolated matrix

The original mixed Weil form from CC27, in the fixed Fourier convention
\[
 \widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx,
\]
contains, for compactly supported inputs \(h,f\) on \(I=[-B,B]\),
\[
 Q(h,f)=\langle \widehat h,a_{\rm arch}\widehat f\rangle
 -\sum_{\log n<2B}\frac{\Lambda(n)}{\sqrt n}
 \langle h,T_{\log n}f+T_{-\log n}f\rangle
 +\overline{m_-(h)}m_+(f)+\overline{m_+(h)}m_-(f),
\]
where \(m_\pm(f)=\int_I f(x)e^{\pm x/2}dx\), and both translates are taken **after zero extension**. RC312 has independently audited the archimedean term. RC313 audits the two remaining original terms as *operators and distributions on the entire polynomial core*, not merely as samples on a few columns.

### 2. The prime multiplier is precisely the paired translation operator

For \(T_\ell f(x)=\widetilde f(x+\ell)\), Plancherel gives
\[
 \widehat{T_\ell\widetilde f}(\xi)
     =e^{+2\pi i\ell\xi}\widehat f(\xi).
\]
Consequently
\[
 -\frac{2\Lambda(n)}{\sqrt n}
      \cos(2\pi\xi\log n)
 \quad \stackrel{\mathcal F^{-1}}{\longleftrightarrow}\quad
 -\frac{\Lambda(n)}{\sqrt n}
    (T_{\log n}+T_{-\log n}).
\]
Both shifts are taken on the real line and restricted to \(I\), so boundary support is truncated and never wrapped periodically. The pair already carries the factor of two. Thus **neither the coefficient nor the number of translations is doubled again**.

For the cap \(B=11/10\), the exact rational Taylor estimate \(9<e^{2B}<10\) proves that the active prime powers are exactly
\[
  \{2,3,4,5,7,8,9\}.
\]
The coefficient \(c_{p^k}=\log p/\sqrt{p^k}\) uses the **base prime** even when \(k>1\), not \(\log(p^k)/\sqrt{p^k}\). RC313 independently re-encloses each \(\log n\) and \(\log p/\sqrt n\) by a 360-term positive rational \(\operatorname{atanh}\) series with rigorous remainder and a high-precision integer-square-root interval; the native RC43 intervals must enclose each independent interval.

For arbitrary polynomials \(h,f\), the overlap
\[
 \langle h,T_\ell f\rangle
 =B\int_{-1}^{\,1-\ell/B}\overline{h(Bt)}
     f(B(t+\ell/B))\,dt
\]
is exactly a finite polynomial integral; the reverse direction is \(\langle f,T_\ell h\rangle\) after adjunction (with the appropriate complex conjugation). The script computes these from **two independent monomial coordinate expansions**, one in \(t\), the other in \(u=t+1\). It checks paired signs, Hermitian symmetry, parity selection, and both positive and negative component quadratic responses on selected rational test polynomials.

The argument is all-degree because it is the Fourier translation identity and a general variable substitution, **not** an extrapolation from the test inputs.

### 3. The two cross-paired poles are a signed rank-two operator

For the compactly supported transform \(\widehat f\), analytic continuation gives
\[
 m_+(f)=\widehat f\bigl(i/(4\pi)\bigr),
 \qquad
 m_-(f)=\widehat f\bigl(-i/(4\pi)\bigr).
\]
Write \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\). Since \(m_\pm=m_c\pm m_s\), the full original *sesquilinear* pole term is algebraically
\[
 \overline{m_-(h)}m_+(f)+\overline{m_+(h)}m_-(f)
 =2\overline{m_c(h)}m_c(f)
   -2\overline{m_s(h)}m_s(f).
\]
Therefore the native physical action has rank two:
\[
 \boxed{K_{\rm pole}
       =2|c\rangle\langle c|
        -2|s\rangle\langle s|.}
\]
Its even sector is positive, odd sector **negative**. This is not a positivity theorem for their sum with the other Weil terms. Compact physical support bounds both moments continuously on \(L^2(I)\), so the rank-two extension has no high-degree source ambiguity.

The validator independently evaluates the native polynomial moments by a degree-40 exponential Taylor model and the positive Rodrigues/integration-by-parts Legendre series, with an explicit uniform exponential tail. It checks all \(P_0,\ldots,P_6\), the parity sign and the two-moment algebra exactly.

### 4. Transfer to the *original CC27 form* on the common completed carrier

RC311 identifies the entire logarithmic endpoint matrix with the physical \(W_B\) multiplier. RC312 identifies the full archimedean digamma form and verifies Poisson-remainder cancellation against the canonical logarithmic metric. RC313 identifies the **original CC27 prime and pole sources** independently of any finite Legendre-column interpolation.

Consequently, **relative to CC27's pinned original-form definition**, the full original Weil polynomial form agrees on every finite polynomial with the bounded native \(D\)-Riesz model
\[
 N_0=I+D^{-1}\bigl[E-(\log2+789/125)I
    -K_{\rm reg}+K_{\rm prime}+K_{\rm pole}\bigr].
\]
The RC121 form equivalence covers the completed canonical logarithmic carrier. Since the original form and this model are continuous in the corresponding \(D\)-form topology and finite Legendre polynomials are a dense form core, the bounded representative is unique on that completion. This is a **source-identification theorem**, conditional on the pinned CC27 original explicit-formula definition and the standard Plancherel, Fourier-translation, and polynomial-density facts. It does not establish an original spectral **lower** bound.

The RC43 finite support-chain estimate also sharpens the operator-norm budget for the prime term from RC307's coarse \(2\sum_n c_n\) to its native fixed-cap estimate (approximately 4.103149 in physical \(L^2\)). RC313 uses that smaller already-certified bound to sharpen RC309's conservative *upper* bound for the full \(D\)-Riesz operator. The positive rank-317 augmentation is separately bounded as in RC310; its positivity alone does not give positivity of the complete original form.

### 5. Boundary of this result

**Discharged relative to CC27:** original archimedean, prime and cross-pole normalization and complete polynomial-core source identification, followed by uniqueness of their bounded \(D\)-form extension. The all-degree derivation is mathematical and the exact rational computations reproduce its finite algebra; it is not itself a Lean formalization.

**Not discharged:** independent transport from all actual zeta-zero divisor carriers to every proposed retained/source/null witness, any positive lower spectral bound on the original signed form, the 314-Schur principal positivity gate, a signed inverse-response certificate, Stage I, F4, or RH.

## RC314 — actual positivity frontier

The next step must attack the genuine **lower-bound** problem, not continue to spend turns reconstructing source identities. Revisit the rank-314 principal Schur block and RC292 signed Chebyshev inverse conditions on the now identified original action. A bounded selfadjoint operator can still have negative spectrum; no positivity follows from finite-certificate replay or the improved operator-norm bound alone.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc313_prime_pole_distributions.py --output certificates/rpb108_rc313_prime_pole_distributions.json
python scripts/validate_rpb108_rc313_prime_pole_distributions.py --output certificates/rpb108_rc313_prime_pole_distributions.json --replay
\`\`\`
