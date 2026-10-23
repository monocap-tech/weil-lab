# W-ODD-NEG — Original 470 physical sources in the strong multiplier domain

**Date:** October 23, 2026. **Scope:** an analytic SOURCE-DOMAIN consequence of
SM35 source geometry and SM41 multiplier growth, *conditional on the original
supported Fourier operator/form realization*. This does not close that
independent realization/interface audit, MG07, the signed odd form, even, CC27,
the Weil criterion, or RH.

## Exact source family and the missing domain question

SM35's exceptional synthesis (J:\mathbb R^{470}\to H_o) consists of
469 odd zero-extended compactly supported generators
(f_{c,k}(x)=x^k\sin(2\pi c x)) for even (k), or
(x^k\cos(2\pi c x)) for odd (k), at the 107 distinct original
rational cluster centers, together with (s(x)=\sinh(x/2)).
Each is supported on ([-B,B]), (B=11/10), and belongs to
(W^{1,1}(-B,B)). The zero extensions can have boundary jumps:
we do **not** incorrectly assume global (W^{1,1}(\mathbb R))
or twice differentiability of the zero extension.

With the Fourier convention (\widehat f(\xi)=\int f(x)e^{-2\pi i\xi x}dx),
integration by parts inside ([-B,B]), explicitly retaining BOTH boundary
terms, gives for (\xi\ne0)
[
 |\widehat f(\xi)|\le
 \frac{|f(B)|+|f(-B)|+\int_{-B}^B|f'(x)|dx}{2\pi|\xi|}.
]
For polynomial generators, evaluating the derivative's monomial integral
and bounding the oscillatory derivative yields the rational envelope
[
 |\widehat{f_{c,k}}(\xi)|\le \frac{C_{c,k}}{|\xi|},\qquad
 C_{c,k}=\frac{1+\mathbf1_{k>0}}3 B^k+
               \frac{2cB^{k+1}}{k+1}.
]
Here we used (\pi>3); the bound is deliberately conservative. For
the actual supported pole, writing (y=B/2=11/20<1), the elementary
positive series gives (\sinh y\le y/(1-y^2)), hence
[
 |\widehat{s}(\xi)|\le\frac{C_s}{|\xi|},\qquad
 C_s=\frac23\frac{y}{1-y^2}=\frac{440}{837}.
]
The latter accounts for the exact two pole endpoint values and the
full (L^1) norm of its derivative.

## The all-470 strong high-frequency Loewner bound

SM41's independently certified ORIGINAL odd positive multiplier growth
bound (subject to its inherited Fourier assumptions) states
(0<a_o(\xi)\le17+\log|\xi|) for (|\xi|\ge1).
Direct substitution (u=\log t) gives the exact identity
[
 \int_{|\xi|\ge1}\frac{(17+\log|\xi|)^2}{\xi^2}d\xi
 =2\int_1^\infty e^{-u}(17+u)^2du
 =650.
]
Let (C=(C_{c,k},C_s)\in\mathbb Q_{>0}^{470}). For every actual
470-coefficient vector (z), pointwise triangle and coefficient Cauchy
give
[
 |\widehat{Jz}(\xi)|\le\frac{\|C\|_2\|z\|_2}{|\xi|}.
]
Thus for the **entire**, untruncated original high-frequency tail,
[
 \boxed{\int_{|\xi|\ge1}a_o(\xi)^2
               |\widehat{Jz}(\xi)|^2d\xi
      \le650\|C\|_2^2\|z\|_2^2.}
]
This is a true finite, rational, full-470 source-coefficient scalar
Loewner bound. It is NOT expected to be quantitatively useful for
the tiny MG07 residual budget: absolute values destroy cancellation.

The original real digamma-plus-seven-prime multiplier is continuous and
bounded on the compact band ([-1,1]), and compactly supported sources
have Fourier transforms in (L^2). Combining low and high intervals
proves (a_o\widehat{Jz}\in L^2(\mathbb R)) for every (z).

Under the usual closed, supported, positive Fourier-form construction,
this sufficient multiplier condition places all columns of (J) in
(\operatorname{Dom}(A_o)): the form functional
(g\mapsto\int a_o\widehat f\overline{\widehat g})
has an (H_o)-bounded Riesz representative obtained by orthogonal
projection of the full-line multiplier action. Since
(2|s\rangle\langle s|) is bounded on (H_o),
(\operatorname{Dom}(A_\star)=\operatorname{Dom}(A_o)).
Any finite linear combination of these actual generators is therefore
a legitimate strong-domain trial vector **in that precise realization**.

**Remaining essential audits:** prove independently that the project's
claimed original Weil/odd operator actually equals the above closed
supported Fourier-form realization, and certify the full original
470×470 `G0`, `N0cap` and (if cap-only viable) `DB` on a matched
Galerkin trial. No equivalence is inferred from this domain lemma alone.

**Replay:** `python scripts/validate_rpb108_odd470_strong_domain_tail.py`.
Only rational exact source-envelope and geometry assertions are checked.
The analytic integration-by-parts and Fourier-form representation
arguments still require mathematical review.
