# RPB108 — Independent phase geometry IP4: exterior-shell test completeness and native forcing

Date: 2026-10-08. Parent independent IP3: `cda12d48a595475d3fe0f2492fd8f2b0a6167cbc` (the prior independent branch head). Coupled analytic dependency: CC20, CC27, CC29, CC31; active Coupled last observed research head CC31 `00dfd25de49cb62c05caba8b365d7efaa7ea91ee`. This is an independent analytic checkpoint, not a new CC theorem, new aperture, new RH claim, or Lean certification.

## 1. The complete exterior quotient is accessible in the genuine logarithmic norm

Let H_a be the established canonical supported logarithmic Fourier Hilbert space with squared norm
\[
 \|f\|_{\log}^2=\int_{\mathbb R}\log(e+|\xi|)|\widehat f(\xi)|^2\,d\xi.
\]
For 0<s<t set `E_st=C_c^\infty((-t,-s) union (s,t))` as a LINEAR space, permitting both sides and arbitrary sums. Then
\[
 \boxed{\overline{D_s+E_{st}}^{D_t}=D_t.}                       (1)
\]
This is a genuine new *density statement* about a specific Hilbert carrier, not a sign statement.

Proof: smooth compact tests are dense in D_t by the inherited canonical core theorem. For any fixed `f in C_c^\infty(-t,t)`, choose three smooth cutoffs `chi_-,chi_0,chi_+`, supported respectively in `(-t,-s),(-s,s),(s,t)`, with sum one except on two neighborhoods of `x=±s` of width at most C epsilon. Define `f_j=chi_j f` and `r_epsilon=f-sum_j f_j`. This smooth residual is supported in the two epsilon-neighborhoods, has `||r_epsilon||_2<=C_f epsilon^(1/2)` and `||r_epsilon||_{H^1}<=C_f epsilon^(-1/2)`, because cutoff derivatives are O(1/epsilon). For any fixed `0<sigma<1/2`, interpolation yields `||r_epsilon||_{H^sigma}<=C_{f,sigma} epsilon^(1/2-sigma)`. Since `log(e+|xi|)<=C_sigma(1+|xi|^2)^sigma`, the H_log norm tends to zero. Thus f is in the closure of D_s+E_st. No physical delta/point trace is present at ±s in this logarithmic norm. This proof does not claim that characteristic cutoffs are bounded operators on every D_t vector; the smooth-core argument is sufficient.

Let `R_s=i M_s^-1 i* M_t` be CC20's M_t-orthogonal projection onto D_s, where M_t=P_t*P_t >= m_B I in the canonical carrier. Its bounded complementary projection `I-R_s` maps D_t onto the full outgoing positive-source-orthogonal subspace
\[
 Z_{st}= \{u\in D_t:\langle P_tu,P_s v\rangle=0\ \forall v\in D_s\}.
\]
Applying `I-R_s` to (1) gives
\[
 \boxed{\overline{(I-R_s)E_{st}}^{\,D_t}=Z_{st}.}             (2)
\]
For any old generalized critical row `J_i`, `J_i|D_s=0`, hence `J_i(f)=J_i((I-R_s)f)`. The exact complete dual norm is
\[
 \boxed{\langle j_i,M_t^{-1}j_i\rangle =
 \sup_{f\in E_{st},\ f\ne0}
 \frac{|J_i(f)|^2}{\|P_t(I-R_s)f\|^2}.}                      (3)
\]
There is no missing quotient direction: both exterior sides and arbitrary finite linear combinations are included. Formula (3) is a COMPLETE test-space characterization, NOT a defect-relative upper bound and not evidence that the supremum is small.

## 2. Exact native arithmetic expression for separated exterior forcing

For old h_i in D_s (not assumed smooth), let f be a smooth exterior test with strictly separated support from [-s,s]. Let `c_n=Lambda(n)/sqrt(n)`, `ell_n=log n`, and, for d>0, the established CC27 continuous native exterior density
\[
 C_{\mathrm{off}}(d)=2\cosh(d/2)-\frac{e^{-d/2}}{1-e^{-2d}}.  (4)
\]
This contains the ORIGINAL Hermitian-cross-pole and off-diagonal archimedean terms. At separation d>0 the singular local diagonal distribution contributes zero; do NOT extend this expression to d=0.

For a right-exterior f supported in (s,t), the unchanged original native mixed form has the exact separated-support pairing
\[
 Q(h_i,f)=\int_{s}^{t} f(y)\Bigg[
   \int_{-s}^{s} \overline{h_i(x)}\,C_{\mathrm{off}}(y-x)\,dx
  -\sum_{\substack{n\ge2\\\log n\le s+t}}
       c_n\,\overline{h_i(y-\ell_n)}
 \Bigg]dy.                                                    (5)
\]
Define h_i=0 a.e. outside [-s,s]. The n-sum is over PRIME POWERS and includes both original prime orientations before the right-support reduction. All other orientations vanish by support; active old primes remain, even when no new prime threshold has entered. The effective threshold `ell_n<=s+t` comes from separated support geometry, not a replacement of the right-limit source cutoff `ell_n<=2t`: omitted terms have identically zero pairings.

For a left-exterior f in (-t,-s), the arch/pole density is the same with `|y-x|`, and the surviving translation is `h_i(y+\ell_n)`, with the same effective finite upper threshold. General f in E_st is the sum of its two exterior pieces.

CC27 proves the smooth separated-support kernel formula. Equation (5) extends to a rough canonical h_i because the old smooth core is dense, the supports remain at a fixed positive distance, the continuous kernel is bounded on that separated rectangle, finitely many translations are bounded in physical L2, and Q is continuous on D_t. This is a new explicit right/left packet specialization of the inherited CC27 form; **it is not an evaluation of the actual critical h_i**.

The full forced residual remains
\[
 \boxed{J_i(f)=Q(h_i,f)-\delta_i\langle P_t h_i,P_t f\rangle.} (6)
\]
The entire last term is mandatory and may not be replaced by a local physical kernel or dropped because supports are disjoint. It has the full original positive-source summation, including all divisor partners and multiplicity copies. The old eigen-equation forces cancellation ONLY for old-domain f, not for these exterior tests.

## 3. A two-sided exact finite-source discrimination

Take H_t=C^3, H_s=span(e_1), the complete positive-source metric and negative row
\[
 M=\begin{pmatrix}1&1/2&0\\1/2&1&0\\0&0&1\end{pmatrix},
 \quad N=(3/4,3/4,3/4).
\]
M is strictly positive. The old generalized lift h=e_1 has P-norm1, lambda=9/16, delta=7/16. The old forced row `J(f)=Q(h,f)-delta<Mh,f>` equals, in canonical coordinates,
\[
 j=(0,-9/32,-9/16).
\]
The positive-orthogonal outgoing basis is `z_2=e_2-\tfrac12e_1`, `z_3=e_3` with exact Gram diag(3/4,1). One exterior test at z_2 gives restricted forced energy `27/256`, and one at z_3 gives `81/256`; together they give the COMPLETE norm
\[
 \boxed{\langle j,M^{-1}j\rangle=27/64.}
\]
The corresponding exact original critical shell gain is `(27/64)/(9/16)=3/4`, and relative to old defect the reaction is
\[
 \boxed{(3/4)/(7/16)=12/7>1.}
\]
Thus retaining only one exterior side can badly underestimate the full forced covariance. Keeping both sides is sufficient to detect this model's negative crossing, but does not prevent it. This is an abstract finite model, not an actual zeta divisor with the same native Weil explicit formula.

## 4. What is gained and what remains impossible to certify here

**Gained:** A rigorous *complete exterior packet test space* for the original supported logarithmic domain and an explicit native forcing formula valid for separated pulses. Unlike IP1's old-only Fourier packets, these tests can detect the actual CC20 forced row, and density ensures no hidden quotient directions escape when ALL exterior smooth tests are allowed.

**Not gained:** No actual generalized critical h_i was constructed or evaluated; no complete native prime/pole/positive-source mixed residual was computed on it. The normalized exterior supremum (3) is still the WHOLE inverse-dual norm; it may require arbitrary superpositions and has no old-defect suppression from density alone. It is therefore *not* a new RH-easier bound. Using CC31's finite critical rank still requires an independently proved bound for each actual row:
\[
 \sup_{f\in E_{st}\setminus\{0\}}
 \frac{|J_i(f)|^2}{\|P_t(I-R_s)f\|^2}
 \le b_B\lambda_i\omega_B(\delta_i),\qquad \omega_B(x)\to0,
\]
uniform with cap-only fixed critical band and positive step as in CC29–CC31.

**Next meaningful experiment:** On an aperture with independently available ACTUAL critical lifts h_i and the complete normalized source dictionary, evaluate the right- and left-exterior kernel integrals (5), subtract the full positive-source correlation (6), source-orthogonalize both-sided outward smooth packets, and certify a WHOLE omitted-packet dual tail. In absence of such h_i or such a global dual-tail enclosure, stop and do not claim arithmetic progress.

No change to the internally certified original aperture 21/20, to RH/F4 or Lean standing. Coupled is sole active integration. Paused Global NF71 and Pre-Contact Shadow PS3 are untouched.

## 5. Exact finite-control validation

The committed [IP4 exact rational validator](../scripts/validate_native_exterior_packet_ip4.py) was independently executed: **21 exact rational assertions passed**. It validates full positive-metric inversion, source-normalized old generalized lift, two one-sided shell packet energies and their complete sum, and an actual negative direction of the generic finite-source control. This is not a machine proof of the logarithmic density theorem, CC27's analytic native kernel, or any actual zeta critical source estimate.

## Subsequent checkpoint

[IP5 — cap-uniform small-step native remainder forcing](REFLECTED_PACKET_BRIDGE_108_INDEPENDENT_PHASE_GEOMETRY_IP5_20261008.md) derives a whole-operator absolute shrinking-aperture modulus from CC33's compact native remainder and the canonical support-projection continuity. A rank-one source contact demonstrates that this absolute modulus cannot supply CC29's defect-relative fixed-positive-step suppression. This links IP4's complete exterior test-space result to a genuine, but insufficient, whole-dual small-step bound.
