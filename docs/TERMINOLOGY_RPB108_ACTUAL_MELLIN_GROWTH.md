# RPB-108: actual complex Mellin tail comparison

`neutralActualZetaThetaMellinTailIntegrand s t` is `(t : ℂ) ^ (s - 1) * (neutralActualZetaThetaRemainder t : ℂ)`. The actual complex Mellin tail is its integral over `Ioi 1`. This is only the large-t part of the completed-zeta construction.

The integer moment domination condition is `s.re - 1 ≤ (n : ℝ)`. Above one, the complex power's norm is `t ^ (s.re - 1)`, bounded by `t ^ n`. Thus the existing actual theta moment controls both tail integrability and its integral norm.

Natural-radius disk domination means `‖z‖ ≤ (n : ℝ)`. It implies the integer moment condition for each actual completed-zeta exponent, `z / 2` and `(1 - z) / 2`.

The same positive kernel-derived p and C bound every admissible tail norm by `C * (n! / (p/2)^n) * (exp(-p/2)/(p/2))`. This is not yet an identification with completedRiemannZeta₀, a circle-envelope rate, local sampling boundedness, or a source/null attachment.
