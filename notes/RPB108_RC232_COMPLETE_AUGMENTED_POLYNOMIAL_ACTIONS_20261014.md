# RPB108 — RC232: complete rationally augmented polynomial action tests

Date: 2026-10-14 UTC. Aperture B=11/10. Branch: research/rpb108-route-consolidation. Parent RC231: `6ea782e1029624c8a969dd8ad70849eaaebe0672`.

RC232 adds rigorous enclosures of the **actual RC115 rational augmentation action** on P0 and P1 to RC231's original Weil action enclosures. The resulting finite polynomial vectors approximate the complete augmented D-Riesz operator N, with all action errors paid in the actual D metric. A band-projection comparison supplies the augmentation enclosure without multiplying the dense degree-2400 rational Fourier kernel.

| Input | Complete augmented squared D-error upper | Error norm / input D-norm upper |
|---|---:|---:|
| P0, even | 0.127512 | 12.348% |
| P1, odd | 0.109311 | 17.620% |

Displayed values are rounded outward. These errors concern a different operator from RC231's original-only tests and are not improvements or regressions of that original-only error. They are not RC228's eight-source canonical inverse width. The present action tests cover every complex combination of P0 and P1, not the complete 639-channel auxiliary source range.

No augmented inverse response, full auxiliary norm below one, Stage I, F4, Lean or RH closure is claimed. The fixed augmentation is still the exact rational RC115 operator; it is not replaced by the ideal band operator.

## Operators, metrics and paid comparison

Use the physical supported-input space P=L2[-B,B], with zero-extension isometry S into ambient L2. Let Pi_U be the orthogonal Fourier-band projection onto [-U,U], and J_U the physical Fourier restriction map. Then

\[
 J_U^*J_U=S^*\Pi_U S.
\]

In each parity Fhat is RC115's exact rational polynomial Fourier kernel on the same rational band U. RC118 explicitly establishes that the contour and Taylor/pi kernel estimates are physical Hilbert-Schmidt bounds before canonical restriction. Hence RC115's stored combined squared error delta^2 gives

\[
 \|\widehat F-J_U\|_{P\to L^2_{\rm freq}}\le\delta,
 \quad \|\widehat F\|\le1+\delta.
\]

The adjoint-product identity is

\[
 \widehat F^*\widehat F-J_U^*J_U
 =(\widehat F^*-J_U^*)\widehat F
  +J_U^*(\widehat F-J_U).
\]

It yields the full physical operator bound epsilon=delta(2+delta). The validator checks this identity exactly with a nonidentity physical metric; Euclidean adjoints are not silently substituted for metric adjoints.

RC231 gives N0, the original D-Riesz action. RC230's chosen augmented operator is

\[
 N=N_0+\lambda D^{-1}\widehat F^*\widehat F.
\]

For comparison only, put N_J=N0+lambda D^-1 J_U*J_U. Since physical-to-D source inversion costs s_lower^-1/2 and the D-to-physical inclusion costs s_lower^-1/2, the **full-input** comparison is

\[
 \boxed{\|N-N_J\|_{D\to D}
 \le\lambda\epsilon/s_{\rm lower}.}
\]

The exact rational bounds are below 0.013313 even and 0.029085 odd. This comparison covers every input in the parity D-energy space. It does not make the identity approximation below a full-input approximation: that additional step is certified only on P0 and P1. No inverse of N_J is computed or substituted into the exact rational response identity.

## Outside-band energy for the two exact polynomials

For any supported physical q,

\[
 q-J_U^*J_U q=S^*(I-\Pi_U)Sq,
 \quad\|q-J_U^*J_Uq\|_2^2
 \le\int_{|\xi|>U}|\widehat q(\xi)|^2d\xi.
\]

The zero-extension endpoint jumps are retained. With k=2pi B,

\[
 \widehat P_0(\xi)=\frac{\sin(k\xi)}{\pi\xi},
 \qquad \widehat P_1(\xi)
 =i\left[\frac{\cos(k\xi)}{\pi\xi}
 -\frac{\sin(k\xi)}{2\pi^2B\xi^2}\right].
\]

The harmless overall sign of the odd transform depends on the derivative convention and does not affect its energy; the relative minus sign is retained. These formulas follow by direct integration and differentiation with the fixed Fourier convention exp(-2pi i x xi).

For a>0 and m>1, integration by parts and absolute integration of the remaining derivative give

\[
 \left|\int_U^\infty\frac{\cos(a\xi)}{\xi^m}d\xi\right|,
 \left|\int_U^\infty\frac{\sin(a\xi)}{\xi^m}d\xi\right|
 \le\frac{2}{aU^m}.
\]

Taking a=4pi B and expanding the trigonometric squares gives the rigorous tails

\[
 T_0\le\frac1{\pi^2U}+\frac1{2\pi^3BU^2},
\]

\[
 T_1\le\frac1{\pi^2U}+\frac1{2\pi^3BU^2}
       +\frac{2}{3\pi^4B^2U^3}.
\]

For P1 the last coefficient pays the oscillatory cross term by 1/(2pi^4B^2U^3) and the remaining nonnegative sine-square term by 1/(6pi^4B^2U^3). No sampled Fourier phase or numerical tail quadrature is used. The code replaces pi by RC115's certified lower bound pi_0-error_pi and rounds upward. Both resulting tail bounds are strictly smaller than the corresponding exact physical polynomial mass.

## Actual augmentation and complete action enclosures

Let m_j=2B/(2j+1), j=0,1. The preceding bounds give

\[
 \|\widehat F^*\widehat F P_j-P_j\|_2
 \le\sqrt{T_j}+\epsilon\sqrt{m_j}.
\]

Thus lambda D^-1 P_j is an approximate **actual rational augmentation action**, with squared D-energy error at most

\[
 \boxed{E_{{\rm aug},j}
 =\frac{\lambda^2}{s_{\rm lower}}
  (\sqrt{T_j}+\epsilon\sqrt{m_j})^2.}
\]

The difference from the ideal band action is paid, rather than identifying that action with Fhat*Fhat. All rational-kernel, Fourier cutoff and adjoint-product errors are included through delta and T_j. Approximation of the full polynomial output by a single polynomial is justified by this full physical norm estimate, not by a finite projected residual.

The actual diagonal D satisfies DP_j=(H_j+s)P_j. Its inherited s interval therefore encloses the trial coefficient lambda/(H_j+s). The code rounds its interval midpoint downward on a 10^-60 grid and pays its radius in D energy using the upper D weight. It adds that rational trial to RC231's degree-64 original-action vector and updates the finite coefficient radius.

If E0,j is RC231's complete original squared error and Er,j is the new trial-rounding squared error, the full augmented bound is

\[
 E_j=(\sqrt{E_{0,j}}+\sqrt{E_{{\rm aug},j}}+\sqrt{E_{r,j}})^2.
\]

The same-input errors are added in norm before squaring; no component orthogonality is assumed. Reflection gives the one exact orthogonality used: the complete even and odd errors have zero D pairing. The resulting diagonal two-input error Gram bounds every complex combination. The finite coefficient radii describe arithmetic uncertainty only; the stored total error additionally pays all global approximation and omitted-output costs.

As a consistency consequence, the augmented forms on these test polynomials are enclosed in [27.532051,29.597430] for P0 and [9.406210,10.647019] for P1, with outward displayed rounding. This is positivity of an already globally positive augmented operator on two tests, not positivity of the original Weil operator. No original inverse gate follows from it.

## Sharper fresh global endpoints and conditional budgets

RC66 supplies the actual complete physical remainder norm kappa in each parity. The canonical inclusion has squared norm at most rho=252/257, so

\[
 A_Q\preceq(1+\rho\kappa)I,
 \quad\|\widehat X\|_c^2
 \le\rho(1+\delta)^2.
\]

Consequently a fresh upper for the **same rational** Hhat is

\[
 b=1+\rho\kappa+\lambda\rho(1+\delta)^2.
\]

RC115's certified lower eta remains unchanged. RC121's canonical/D equivalence then gives mu<=a eta and nu>=2b for N, where a=32125/230953. These endpoints use actual physical K and kernel bounds, not identification with RC114's different exact-kernel augmentation.

| Parity | New nu upper, outward display | Previous conservative nu upper | Exact-action residual degree for correction <=10^-6 | Degree for correction <=10^-12 |
|---|---:|---:|---:|---:|
| Even | 57.692532 | 83.177532 | 1182 | 1891 |
| Odd | 50.351215 | 77.126022 | 1137 | 1817 |

These degrees are sufficient **conditional exact-N-action** budgets recomputed with RC230's directed positive Chebyshev recurrence. They are not completed iterative solves, optimal degree claims, or inexact-action guarantees. The two-column errors in this certificate are not uniform iterative action errors. Every propagated action error must be paid before using a polynomial inverse budget.

## Verification and remaining gate

Exact generation and reversed-input replay reproduce the complete certificate. Its pins include RC231's action certificate and validator, the fixed rational source model, original operator bounds and inherited metric dependencies. Publication is add-only with an expected-head non-force ref update; remote comparison and recursive tree readback verify existing blob preservation and the three additions. Conflict-marker checks cover the additions, not all historical file contents.

```bash
python scripts/validate_rpb108_rc232_augmented_polynomial_action.py --output certificates/rpb108_rc232_augmented_polynomial_action.json
python scripts/validate_rpb108_rc232_augmented_polynomial_action.py --output certificates/rpb108_rc232_augmented_polynomial_action.json --replay
```

The next target is tighter/materialized augmented actions on actual source/response trials and complete full-range inverse residual contracts. RC230's exact range rank is still 639, RC228's finite canonical gate remains passed, and full augmented inverse responses, auxiliary metric/norm below one and Stage I assembly remain open. No dense frequency Gram or exact rational-kernel multiplication was performed in this pass.
