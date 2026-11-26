# V10B — Weighted sampling by unit rectangles (paper proof, not native certification)

Alternative to the disk-submean overlap argument of 001G. The objective is a direct route using only real-variable interval estimates and weighted Fourier multiplication. No RH assumption; all zero-count inputs are explicit. No ADOPT.

## 1. Receiver

Let f be supported in [-t,t], with f in L² and finite angular log-Fourier energy
E(f) = (1/(2π)) ∫ log(2+|y|) |F(iy)|² dy, where F(z)=∫ exp(zx)f(x)dx.
Let Z be a locally finite weighted family of points s+iy with |s|≤1/2,
nonnegative weights m, and for every integer n
Σ_{n<y≤n+1} m ≤ A log(|n|+3).
Then Σ_Z m |F(s+iy)|² ≤ B_t A E(f), with B_t independent of the index family.

## 2. Unit-interval evaluation

For C¹ complex h on an interval I of length one and p∈I,
|h(p)|² ≤ 2∫_I (|h(q)|²+|h'(q)|²)dq.
Indeed h(p)=h(q)+∫_q^p h', the squared triangle bound and Cauchy–Schwarz
give |h(p)|²≤2|h(q)|²+2∫_I |h'|². Integrate over q.
No boundary extension, point-separation or complex submean theorem is needed.

Apply twice on [-1/2,1/2]×[n,n+1], to H(s,y)=F(s+iy),
first in y and then in s to H and ∂yH. For each point of the cell,
|H(s,y)|² ≤ 4∫cell (|H|²+|∂s H|²+|∂y H|²+|∂s∂y H|²).
The derivatives are respectively transforms of f, xf, ixf, ix²f with
the same exponential weight e^{sx}. Differentiation follows from bounded
support and dominated convergence, including the second derivative.

## 3. Sum the cell bounds

Multiply by m and sum over points of each cell. For y∈[n,n+1],
log(|n|+3) ≤ log(|y|+4) ≤ 2 log(2+|y|).
Summing nonnegative integrals over integer cells yields
Σ_Z m|F(s+iy)|² ≤ 8 A ∫_{-1/2}^{1/2}∫_ℝ w(y)
  (|F(s+iy)|²+2|F'(s+iy)|²+|F''(s+iy)|²) dy ds,
where w(y)=log(2+|y|). For rigor one can first bound arbitrary finite
subsets; monotone supremum then gives the full nonnegative sum.
Endpoint overlaps of the closed rectangles are Lebesgue null, while
half-open cells partition the index family.

## 4. Uniform weighted multiplier estimate

Fix χ∈C_c^∞ equal to 1 on [-t,t]. For j=0,1,2 and |s|≤1/2 set
p_{j,s}(x)=χ(x)x^j e^{sx}. Their first two derivatives have uniformly
bounded L¹ norms, as do the multipliers themselves. Their angular
Fourier transforms K_{j,s} satisfy |K_{j,s}(u)|≤C_t/(1+u²)
by the elementary L¹ estimate and two integrations by parts.
In particular ∫ sqrt(w(u))|K_{j,s}(u)|du is uniformly finite.

Use the angular Fourier convention G(y)=∫e^{iyx}f(x)dx. Then
transform(p_{j,s} f)(y)=(1/(2π))∫ K_{j,s}(u)G(y-u)du.
This convolution identity follows from Fourier inversion of p (K∈L¹)
and Fubini (f∈L¹ by bounded support).
Since 2+|y|≤(2+|u|)(2+|y-u|),
w(y)≤w(u)+w(y-u)≤(2/log 2)w(u)w(y-u).
Weighted Young (L¹*L²→L²) now gives
||sqrt(w) transform(p_{j,s}f)||₂
 ≤ (sqrt(2/log 2)/(2π)) ||sqrt(w)K_{j,s}||₁ ||sqrt(w)G||₂.
This is uniform in s and the three values of j. Integrate the bound
from section 3 over an interval of length one to obtain the receiver.
The physical carrier uses cycles-frequency weight log(2+|2πu|),
which becomes exactly w(y) after y=2πu by V08H/V08I.

## 5. Native decomposition and boundary

B1: unit interval evaluation (real-variable FTC and Cauchy–Schwarz).
B2: rectangle evaluation and finite weighted-cell summation.
B3: logarithmic submultiplicativity and weighted Young.
B4: supported multiplier Fourier identity and uniform kernel bound.
B5: actual zero local-count attachment and bounded lp analysis.
The local-count theorem and arithmetic normalization still need native
attachment. These are proposed Lean gates, not compiled declarations.
The existing 001G disk route remains valid as an alternative; no
equivalence of implementations has been certified. No global signed
Weil positivity is asserted.
