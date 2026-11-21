# Weil-Lab — CP004
## Verified finite-height zero geometry, real cosine-moment compression, and fail-closed falsification interface

**Independent CP### head:** CP004 stacked on CP003 PR #799 -> CP002 #796 -> CP001 #790. Do not modify or renumber Phase IV IV### (currently observed IV022 PR #800), Phase III NF###, or PI### trace-test work. The CP004 code contains **no claim of new kernel-accepted Lean original-source attachments, certified exhaustive zero data, arithmetic/spectral equality, global Weil positivity, or RH**.

## 0. Sources, actual evidence, and the remaining gap

1. CP003 exact-rational calculations derived the conditional original frozen-span prime burden `pi(V_r)<23/240`, signed full-form lower margins `lambda(V_1/1000)>7/10` and `lambda(V_1/500)>11/20`, and an explicit normalized zero-tail `E_r<1/500` at `T=2^20`. Its source correspondence to IV011/IV019 remains an OPEN Lean/kernel attachment.
2. Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to 3·10^12*, Bull. London Math. Soc. 53 (2021), DOI 10.1112/blms.12460; arXiv:2004.09765, rigorously verified all zeta zeros with 0<gamma<=3e12 lie on Re rho=1/2. This **published finite verification** covers our T=1,048,576 unconditionally; it is not an RH assumption for unbounded height. **It is not an authenticated, complete, individually enclosed zero table** for all gamma<=T.
3. Andrew Odlyzko's zero tables report the first 2,001,052 imaginary parts to about ±4e-9, with positive heights extending beyond T (https://www-users.cse.umn.edu/~odlyzko/zeta_tables/). Dataset precision and coverage do not, by themselves, certify complete enumeration, multiplicity, exact zero enclosures, or error propagation into the Weil matrix. No Odlyzko file is imported or asserted formally checked in CP004.
4. Elchin Hasanalizade, Quanli Shen, Peng-Jie Wong, *Counting zeros of the Riemann zeta function*, Journal of Number Theory 235 (2022), arXiv:2107.06506, supplies unconditional zero-count majorants for the CP003 tail. A **zero-count upper/lower interval wider than one integer is not enough** to prove enumeration completeness. A rigorous Turing count or equivalent certified argument-principle count at the same cutoff is required.

## 1. A completely explicit FINITE spectral matrix, without global RH

Fix exactly the CP001/CP002 three genuine real even translated bump tests:
`
phi(u)=exp(1-1/(1-u^2)), |u|<1; phi(u)=0 outside,
h=1/2000, c=1099/1000, u0=1/5, r in {1/1000,1/500},
f_-=phi((x+c)/h), f_+=phi((x-c)/h), t_r=phi((x-u0)/r).
`
Write `a2=integral_-1^1 phi(u)^2du >0`. Their fixed physical mass Gram is
`G_r=diag(h a2,h a2,r a2)`; this is not a positive representation of the original signed Weil form.

Let the *unscaled* Fourier shape transform be
`Phi(y)=integral_-1^1 phi(v)cos(y*v)dv`.
It is REAL and even, by the true even real bump. For `H_f(z)=integral_R f(x)e^(zx)dx`, substitution gives the exact real-height formula
`H_(b_(c,h))(i gamma)=h exp(i c gamma) Phi(h gamma)`.

By the Platt–Trudgian published finite-height theorem, every *true* nontrivial zero with 0<gamma<=T has `rho=1/2+i gamma`; the negative-height partner is its complex conjugate, with multiplicities. Therefore CP001's centered zero pairing `H_f(z_rho)conj(H_g(-conj z_rho))` reduces **on this finite verified range only** to a positive Gram contribution. Define for scale a,b and displacement d:
`
 J_(a,b)(d;T)=2*a*b*sum_(0<gamma<=T, all TRUE zeros with multiplicity)
                   Phi(a gamma)*Phi(b gamma)*cos(d gamma).
`
The whole finite zero-side compression, **if all actual zeros are enumerated**, is EXACTLY the real-symmetric 3x3 matrix
`
 Z_(T,r) =
 [ J_(h,h)(0)     J_(h,h)(2c)       J_(h,r)(c+u0) ]
 [ J_(h,h)(2c)    J_(h,h)(0)        J_(h,r)(c-u0) ]
 [ J_(h,r)(c+u0)  J_(h,r)(c-u0)     J_(r,r)(0)   ] .
`
Important independent structural tests:
- `Z_(T,r)` is positive semidefinite, as a finite sum of rank-one Gram contributions for +/-gamma pairs. This is NOT a positivity result for the complete arithmetic Weil form or for any zeros above T.
- The two old diagonal entries are IDENTICAL termwise; this follows from the equal-shape/equal-width translated bumps.
- All nine entries are REAL because `phi` is real-even and the +/-gamma pair sums are conjugates.
- The central mixed spectral entries are not zero merely because their **prime parts** vanish; they are genuine cosine-moment sums.
- The normalized operator error `||G_r^-1/2 (A_r-Z_(T,r)) G_r^-1/2||<=E_r<1/500` remains CONDITIONAL on the original full mixed arithmetic–zero-side dictionary and the independent CP003 analytic tail assumptions. The off-line zeros above T are still handled by the full reflected-factor bound, never dropped.

The exact old diagonal equality and finite PSD are powerful **negative controls** on any proposed independently computed spectral matrix, even before the arithmetic dictionary is formally accepted.

## 2. A rigorous necessary contradiction gate for supplied enclosures

Let `A_r` be the literal ORIGINAL full `Pole-Prime+Arch` Hermitian compression, and suppose both `A_r` and an independently computed `Z_(T,r)` have OUTWARD mathematical interval enclosures.

**If** the complete Weil mixed-form normalization/zero-side dictionary and the CP003 `E_r<1/500` bounds are proved, then every entry must satisfy
`
 |(A_r-Z_(T,r))_(ij)| <= E_r*sqrt(m_i*m_j)
                      <= E_r*(h_i+h_j),
`
because `m_i=||f_i||_2^2 <= 2*h_i` from `0<=phi<=1`, and AM–GM gives `sqrt(m_i m_j)<=h_i+h_j`. Here `(h_i)=(h,h,r)`.

Thus a **rigorous separation of even a REAL component** of an arithmetic and spectral entry by more than `E_r*(h_i+h_j)` is a falsifier for the conjunction of the claimed dictionaries, enclosures, and tail estimate. It does not demonstrate an off-line zero or prove RH false: a source mismatch is the first diagnosis.

CP004 adds a pure-Fraction fail-closed **contradiction scanner**, `scripts/cp004_finite_spectral_falsifier.py`. It accepts only user-supplied 3x3 rational real interval arrays for the *full original signed* arithmetic and the *complete truncated zeros-side* matrices with explicit provenance metadata. It checks:
- matrix size, rational parsing and interval ordering;
- finite zero-side necessary structure (real symmetry, equal old diagonals and nonnegative diagonal), in the sense that intervals must admit such a matrix;
- the exact CP003 rational upper tail `E_r`;
- direct interval separation larger than `E_r*(h_i+h_j)` as a **necessary incompatibility**.

It prints `FALSIFIED`, `INCONCLUSIVE`, or `NOT_READY`; it never prints `CERTIFIED_COMPATIBLE`. A compatible-looking interval match is only **not falsified**, not a proof, because the checker does not independently verify zero completeness, a Turing count, integral enclosures, Hermitian source attachment, SHA provenance or the full explicit-formula map.

## 3. Two distinct proof obligations for finite zero data

**Finite-line verification (externally available):** Platt–Trudgian covers the absence of off-critical zeros at gamma<=T. This supplies a valid *finite* critical-line reduction without RH.

**Enumeration completeness (still open locally):** construct a list `gamma_k in [l_k,u_k]` of actual zeros with certified sign/argument-principle isolations, multiplicities and an independently verified exact `N_+(T)` count equal to the sum of listed multiplicities. The validator must also establish that the chosen cutoff T is not in an unresolved interval. This cannot be inferred from Platt–Trudgian's critical-line theorem alone, a raw Odlyzko table, or the 2022 coarse N(T) error estimate. Independently control the effect of each gamma interval and of numerical quadrature for `Phi(h gamma)` and all five cosine arguments.

**Dependency graph:**
```
 original IV011 mixed correlation and IV008/IV009 Hermitian form
   -> original signed full A_r (pole, ALL primes including n9, Gamma)
          |
          +----> source-bound arithmetic 3x3 interval enclosure
                    |
 published finite RH-to-3e12 + a complete Turing-validated zero roster
          |
          +----> real even cosine-moment 3x3 Z_(T,r)
                    |
 HSW unconditional all-zero tail + bump derivative/mass enclosures
          |
          +----> E_r<1/500 and necessary entrywise compatibility test
```

No leg may be silently replaced by a numerical guess, abstract Gram surrogate, imported operator positivity assumption, or unproved global RH.

## 4. Phase IV source-bridge design and the IV022 boundary

The CP004 companion original-source integration must live on a separate **draft branch based on IV022** (not on CP003, which intentionally has no unmerged IV imports). Its source candidates should expose:
`CP004OriginalCorrelationIntegral` using original `neutralIV011MixedCorrelation_eq_schwartzIntegral`,
`CP004OriginalPrimeFiniteTen` using the true `neutralIV011OriginalMixedPrime_eq_finite`,
`CP004OriginalPrimeSingleN9_of_otherTermsZero` using original source terms without inventing a new prime oracle.

These are **intermediate conditional source-interface lemmas**, not yet the fully instantiated CP001 bump construction. The next genuine task is to supply the frozen real bump functions as authenticated complex Schwartz tests, prove the pointwise signed log-gap table, then reduce all three original prime entries including genuine `n=9`. Do not present conditional source lemmas as a kernel-accepted three-bump prime theorem.

IV022's separate *four-cell* prime-gap and conditional `1/16` project advances independently. CP004 uses ONLY the three frozen CP001 bumps, with no assumed fourth-cell transfer or IV022 quantitative bound.

## 5. Falsification and next CP005

**CP004 result:** a new independent real cosine-moment spectral dictionary valid *at the rigorously verified finite height*, and a mathematically explicit, rational necessary cross-comparison test. The numerical data legs are not completed here.

**Falsifiers / negative controls:** proposed Z is non-Hermitian/non-real, has unequal old diagonal entries or violates finite PSD despite retaining all positive-height verified critical-line zeros; one rigorously separated full A/Z interval entry by more than `E_r*(h_i+h_j)`; true-source n9 sign/normalization disagreement; or a purported certified zero list with nonmatching Turing count.

**Next CP005:** finish actual three-bump Lean source instantiation (not merely source wrappers), acquire a complete independently certified Turing-counted zero roster to some T with a verified tail threshold, enclose the five `J_(a,b)(d)` moments with outward rounding, and run the first nonvacuous full `A_r` versus `Z_(T,r)` matrix test. A failed certificate is a research finding; it is not a global RH conclusion.

**External references:** Platt–Trudgian https://doi.org/10.1112/blms.12460 / https://arxiv.org/abs/2004.09765 ; HSW https://arxiv.org/abs/2107.06506 ; Odlyzko https://www-users.cse.umn.edu/~odlyzko/zeta_tables/ ; CP003 PR #799; IV022 PR #800.
