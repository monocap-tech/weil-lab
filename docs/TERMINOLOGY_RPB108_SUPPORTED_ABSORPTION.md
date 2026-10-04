# Terminology: RPB108 supported absorption audit

Additive register; historical wording remains unchanged.

| Term | Definition | Scope and certification |
| --- | --- | --- |
| Whole-domain absorption coefficient | theta with physical mass m(f) <= theta L(f) for every canonical-domain f | Distinct from a Green-range-specific coefficient |
| Support-band mass bound | Fourier mass on [-R,R] <= 4aR m(f) | Derived from support, L1 Cauchy–Schwarz and Fourier integral; analytic proof |
| Supported cosine test | cos(pi x/(2a)) on [-a,a], zero elsewhere | Nonzero canonical-domain H1 vector; no Green graph or source/null membership inferred |
| Whole-domain absorption obstruction | K_a theta > 1 for a >= 1/(8e) | Analytic cosine proof plus Lean-certified K_a > 3; concerns the existing absolute-error argument |
| Green-range absorption budget | A proved mass/log bound restricted to actual Green physical coordinates, with K_a theta <= 1 | Remains independent and unresolved |

Formalized here: M_a(0) < -2 and absolute envelope, E_a, K_a > 3. The support-band and cosine proofs are not Lean formalizations.
