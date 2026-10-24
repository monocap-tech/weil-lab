# W-ODD-NEG — The missing complement-floor improvement and refined SM40 leakage

**Mandatory correction (October 23):** the original SM33 h-only leakage failed to pay the +κ part of the operator Kminus=(κ-m)+. This note and its validator now use corrected SM33 and min(h_SI10+κ,w_SM40). See [SM33 leakage repair](RPB108_SM33_KAPPA_LEAKAGE_REPAIR_20261023.md). Historical underpaid SM33 decimal measurements are not certified whole-Kminus values.


**October 23, 2026.** Source dimension remains the genuine original \(469+1=470\). The signed odd, even, Weil/CC27 and RH obligations remain **OPEN**. Independent functional-analytic/domain identification is not waived.

## 1. An immediate strict improvement to SM34

Write \(E_0=\operatorname{ran}J\), \(F=E_0^\perp\) and \(Q_0\) for the *same* original 470-source physical projection as in SM32–SM34. The original odd pole \(s=\sinh(x/2)\) belongs to \(E_0\), so \(\langle s,v\rangle=0\) for every \(v\in F\). The genuine original whole positive operator \(A_o\) satisfies \(A_o\succeq\kappa I\) with \(\kappa=1/1000\). SM33 proves the full original signed-negative restriction
\[
 0\preceq Q_0K_-Q_0\preceq\varepsilon I_F,\qquad
 0<\varepsilon<1/15000.
\]
Therefore, on the **entire original infinite complement**, using the ORIGINAL operator \(W_o=A_o-2|s\rangle\langle s|-K_-\),
\[
 \boxed{D_F=W_o|_F\succeq(\kappa-\varepsilon)I_F.}
\]
This is strictly stronger than SM34's inherited \(\mu=17/25000\), and does not change any source generator or complement. It holds on the same closed form domain, subject to inherited SI29/SI10 original-realization premises.

The SM34 energy-dual exact mixed Schur and PSD Cauchy estimate still apply verbatim, now with \(\mu_{\rm new}=\kappa-\varepsilon\):
\[
 S_A[e]\ge a_\star(e,e)
  -\left(1+\frac{\varepsilon}{\kappa-\varepsilon}\right)
      \langle e,K_-e\rangle .
\]
The complete original generalized source sufficient gate is consequently
\[
 \boxed{
 \mathsf N\preceq
 \theta_{\rm new}\mathsf G,\qquad
 \theta_{\rm new}=
 \frac{\kappa-\varepsilon}{\kappa}
 =1-\frac{\varepsilon}{\kappa}
 >\frac{14}{15}>\frac{51}{56}.
 }
\]
The analytic logic is exact. Even at the old SM33 \(\varepsilon\), the clean threshold can be raised from approximately 0.910714 to **strictly above 0.933333**, before further multiplier refinements.

The exact original corrected Schur remains necessary and sufficient; this improved scalar bound is still merely sufficient. A sampled direct negative ratio exceeding \(14/15\) is neither an actual original obstruction nor a negative original signed direction.

## 2. Same b9/470 space, stronger SM40-weighted leakage

The old SM33 bound computes
\[
 \varepsilon=2B\sum_{j=1}^{107}M_j e_j^2,
 \quad M_j=2\int_{J_j}\!h_{\rm SI10}(\xi)\,d\xi,
\]
with cluster-specific exact b9 Taylor errors \(e_j<2^{-9}\). But the *same physical exceptional span* also controls the true negative-frequency multiplier against every later independently valid cap weight, including SM40's rational endpoint-curvature real-frequency envelope \(w_{40}(\xi)\) on the same 3,892 quarter subcells.

On each such subcell use the pointwise minimum
\[
 h_{\rm eff}(\xi)=\min(h_{\rm SI10}(\xi)+\kappa,w_{40}(\xi)).
\]
Both operands are separately verified full-real upper bounds for \((\kappa-m(\xi))_+\); the minimum remains a valid whole-real upper on the SAME original true \(K_-\). Keep every mirrored negative-frequency contribution. For each original cluster define
\[
 M_j^{\rm eff}=2\int_{J_j}h_{\rm eff}(\xi)\,d\xi,\quad
 \varepsilon_{\rm eff}=2B\sum_jM_j^{\rm eff}e_j^2.
\]
Then \(0\preceq Q_0K_-Q_0\preceq\varepsilon_{\rm eff}I_F\) for the original entire \(F\), **and** \(\varepsilon_{\rm eff}\le\varepsilon_{\rm SM33,\,repaired}<1/15000\), while the same true global \(K_-\) norm improves to \(2B\sum_jM_j^{\rm eff}\). No old cap has been silently substituted into a new Galerkin matrix.

This directly yields the stronger exact source sufficiency threshold
\[
 \boxed{\theta_{\rm eff}
  =1-\frac{\varepsilon_{\rm eff}}{\kappa}.}
\]
This new number must be computed from all 3,892 exact rational subcells with the original matched Taylor orders. It is NOT replaced by an inferred decimal or by the sampled direct/cap ratios. The accompanying script checks the entire original geometry, all subcell coverage, original b9 errors, pointwise minimum, exact rational leakage and improved norm bound.

## 3. The strengthened threshold does NOT erase the cap obstruction

For a true nonnegative complement leakage \(\varepsilon_{\rm eff}\), the SM34-type scalar threshold \(\theta_{\rm eff}=1-\varepsilon_{\rm eff}/\kappa\) is **strictly less than one**. SM40's historical SAME-source *sampled* cap/Ritz generalized ratio reached ~1.012044, above even the formal upper ceiling of one, whereas the *sampled direct* negative ratio reached ~0.972929, below one. If a rigorously certified original physical source ray reproduces a cap/action ratio greater than one, **no improvement to the scalar complement leakage alone can salvage the fixed SM40 890-cap Ritz test**; one must tighten the negative cap, use a correlated direct negative-covariance upper on that ray, enrich the Ritz space or return to the exact corrected Schur. None of the historical sampled eigenvalues is a rigorous obstruction.

This is why the new threshold computation and the corrected SM40 ray scout are both necessary and **distinct**. Only after both full-original source-action and negative-cap data are rigorously enclosed is a pass/fail statement justified.

## October 23 verification audit: separate source and cap Taylor orders

A code review exposed a false assertion in the first refined leakage validator: the original SM32/SM33 **b9** exceptional source basis has 469 polynomial generators plus the pole (470 total), whereas the original SM40 **b24** negative upper has 890 covariance/Taylor columns. There is no equality of their cluster-local truncation orders. The updated validator now independently replays both Taylor orders on every one of the same 107 clusters, proves \(\sum_j p_j^{(9)}+1=470\), \(\sum_j p_j^{(24)}=890\), enforces \(p_j^{(9)}\le p_j^{(24)}\), and uses **only** the b9 approximation error \(e_j^{(9)}\) for \(QK_-Q\). It additionally checks that the inherited SM33 mass has actually paid \(\kappa\) on the full reflected width. These are implementation correctness repairs, not acceptance of the refined \(\varepsilon_{\rm eff}\) (full CI still pending).

A separate stdlib-only exact Fraction regression at [verify_rpb108_sm33_kappa_paid_scalar.py](../scripts/verify_rpb108_sm33_kappa_paid_scalar.py) was executed independently. It checks the complete repaired scalar arithmetic, given the inherited full-cluster premises:
\[
H_-=\frac{13244372713}{160000000}=82.77732945625,\quad
\bar\varepsilon_{\rm sharp}
=\frac{1062977491599207}{16000000000000000000},\quad
\theta_{\rm paid}> \frac{14937022508400793}{16000000000000000}
=0.9335639067750495\ldots .
\]
It neither reconstructs the 107 true original cluster estimates nor establishes odd positivity.

## 4. What to test next

The selected 25-source SM40 *noncertifying* direct negative ratios were ~0.965–0.973; the corresponding SM40 negative-cap ratios ~1.003–1.012. The sharper complement threshold could narrow or eliminate the former scalar deficit while leaving the original SM40 cap/Ritz and strong-residual obligations intact. **Do not claim that it crosses 0.973 until the new exact rational leakage run supplies a value.**

For the SAME canonical \(V=\operatorname{ran}J\), the raw-source cap-only gate now becomes
\[
 \boxed{ \theta_{\rm eff} A_J-C_J^{\rm SM40}\succeq0}
\]
instead of \( (51/56)A_J-C_J^{\rm SM40}\succeq0\). The original MG07 complete gate uses the SAME \(\theta_{\rm eff}\) with one uniform \(t>0\); the residual covariance and positive-feature/pole Woodbury corrections remain required. A failed new cap-only ray would reject only this fixed Ritz/cap route, while the exact corrected signed Schur and alternative approximation schemes remain available.

**Replay:** `python scripts/validate_rpb108_sm40_sharp_odd_complement_threshold.py` (the exact Fraction audit must pass before its numerical threshold is treated as an accepted certificate). No RH assertion.
