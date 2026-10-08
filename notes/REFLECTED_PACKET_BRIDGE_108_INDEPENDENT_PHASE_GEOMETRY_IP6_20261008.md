# RPB108 — IP6: finite-rank approximation of actual critical lifts and fixed exterior witnesses at hypothetical contact

2026-10-08. Independent NF after IP5. Active Coupled analytic inputs: CC20 (exact generalized lifts/forced rows), CC29 (strict outward native flux at hypothetical first contact), CC31 (cap-uniform critical rank), CC32 (individual persistent rows under hypothetical contact), CC33 (canonical identity plus compact actual native remainder), CC34 (unsigned remainder cannot be small), CC35 (parity pole correlation). Coupled research at latest observed CC35 `d688561bdacc509ad15465c65dfb8ce795d2daf9`.

**A (actual conditional-free structural theorem):** On every fixed finite cap, every old generalized critical lift with small source defect is uniformly approximable by support projections of a fixed finite-dimensional range. The approximation is independent of the old signed gap; it is not an RH proof, a new zeta arithmetic cancellation, or a computed source eigenvector.

**B (conditional finite-witness theorem):** If the actual Weil form has a first zero contact at some a, then a single finite list of smooth two-sided EXTERIOR tests at any fixed t>a detects every normalized contact null direction and, for all sufficiently close old near-critical lifts, their forced rows. This strengthens the observational form of CC32's conditional scalar persistence, but does not exclude actual contact. It does not supply an upper defect modulus.

No new positive aperture beyond 21/20, RH/F4, full transport, or Lean closure.

## 1. Complete actual spectral-selection identity

Fix B>a0=21/20. Use the canonical supported Hilbert carrier H_B=D_B with logarithmic Fourier norm, and `Pi_s:H_B->D_s` its CANONICAL support projection. The original complete signed form is `Q_B=I+C_B`, with C_B compact selfadjoint as established in CC33, and the bounded positive-source metric is `M_B=P_B^*P_B`, satisfying
\[
 c_B^2I\preceq M_B\preceq U_B^2 I.
\]
Neither C_B nor the signed source N is replaced by a finite zero dictionary.

For any old-positive s<=B and source-normalized actual generalized critical lift h_i in D_s, `||P_sh_i||=1`, source eigenvalue `lambda_i=1-delta_i`, the old critical equation is
\[
 \Pi_s(I+C_B-\delta_iM_B)h_i=0.
\]
Since Pi_s h_i=h_i, this is equivalently
\[
 \boxed{h_i=-\Pi_s C_Bh_i+\delta_i\Pi_s M_B h_i.}       (1)
\]
This equation is exact for the actual complete Weil form. Its leading identity cancellation is inherited from CC33, but IP6 uses it to select an approximate common critical mode chart.

## 2. Uniform finite-rank approximation, without the old gap

Given epsilon>0, compactness of C_B supplies a finite-rank bounded operator F_epsilon (even finite-rank selfadjoint if desired) with
\[
 \|C_B-F_\epsilon\|\le\epsilon.
\]
Take L_epsilon=ran F_epsilon in H_B, fixed independent of old aperture s, spectral eigenvector and signed defect. By (1),
\[
 \operatorname{dist}_{H_B}(h_i,\Pi_s L_\epsilon)
 \le \|h_i+\Pi_sF_\epsilon h_i\|
 \le(\epsilon+\delta_i U_B^2)\|h_i\|.
\]
Positive observability gives `||h_i||<=1/c_B`, hence
\[
 \boxed{
  \operatorname{dist}_{H_B}(h_i,\Pi_s L_\epsilon)
    \le\frac{\epsilon+U_B^2\delta_i}{c_B}.}           (2)
\]
L_epsilon can be chosen spanned by finite smooth compact-supported approximations in H_B, by the inherited smooth core and approximation of finite rank images. Such vectors are not automatically a single modulated mother packet, and Pi_s applied to them need not preserve their physical pointwise shape. No unproved frequency-band invariance is invoked.

Moreover, because s->Pi_s is STRONGLY continuous on the compact cap interval [a0,B], the set `{Pi_s v:s in [a0,B],v in L_epsilon,||v||<=R}` is compact for fixed R. Letting epsilon->0 in (2) proves the following **uniform precompactness near zero defect**:

For every sequence of old-positive s_n in [a0,B] and P-normalized actual old critical lifts h_n with delta_n->0, there is a canonically strongly convergent subsequence of h_n. This is a relative compactness statement only for sequences with defects tending to zero, not all source eigenmodes.

If s_n->a and h_n->h strongly, then ||P_B h||=1, h in D_a, and Q_a(h,k)=0 for every k in D_a. To prove the mixed equation, test first compact smooth k supported strictly inside (-a,a), which lies in D_{s_n} for all large n (the case a=a0 and s_n>=a0 is also covered); use the old eigen-equation with delta_n->0 and continuity of Q_B and M_B, then extend by the canonical smooth core. The limit h is a normalized actual weak null mode on D_a, conditional on such a sequence existing.

This theorem is a consequence of the exact native compact remainder and support-projection continuity. It does not identify a new special arithmetic phase constraint absent from generic identity-plus-compact models.

## 3. Finite fixed exterior witnesses at a hypothetical first contact

Now ASSUME an actual first zero contact at a in (a0,B), with the original Q_a nonnegative and nontrivial null space
\[
 K_a=\{h\in D_a: Q_a(h,k)=0\quad\forall k\in D_a\}.
\]
The compression of Q_B to D_a is identity plus compact, hence K_a is FINITE dimensional, of dimension r>=1. The full P-norm is equivalent to the canonical norm.

Fix any t with a<t<=B. CC29's native no-flatness theorem shows: for every nonzero h in K_a there exists some f in D_t such that Q_t(h,f)!=0. The nonzero mixed row vanishes on D_a. IP4's exterior smooth packet density `closure(D_a+E_at)=D_t`, where `E_at=C_c^infinity((-t,-a) union (a,t))`, therefore shows that the family of linear functionals
\[
 \ell_f:K_a\to\mathbb C,\qquad \ell_f(h)=Q_t(h,f),\quad f\in E_{a,t},
\]
separates points of K_a. By FINITE-dimensional linear algebra, there exist **r fixed exterior smooth packets** f_1,...,f_r such that their restriction functionals form a basis of K_a^*. Consequently a constant kappa_{a,t}>0 exists with
\[
 \boxed{\sum_{j=1}^{r}|Q_t(h,f_j)|^2
      \ge\kappa_{a,t}\|P_a h\|^2\quad(h\in K_a).}     (3)
\]
The packets and kappa depend on the HYPOTHETICAL contact a, the chosen fixed t and the actual Q. They are existential, not computed, not uniform over all potential contact apertures, and not an upper arithmetic estimate.

For ANY source-normalized old critical lifts h_n at apertures s_n↑a with delta_n->0, the compactness theorem in section 2 gives subsequential strong limits in K_a. Since the finite list (3) has a positive lower bound for EVERY normalized h in K_a, the same finite list must satisfy, for all sufficiently near a and sufficiently small defects,
\[
 \boxed{\sum_{j=1}^{r}|J_n(f_j)|^2\ge\kappa_{a,t}/2.} \tag{4}
\]
Otherwise a violating sequence yields a compactly convergent subsequence with P-normalized nonzero h in K_a, and `J_n(f_j)=Q_t(h_n,f_j)-delta_n<P h_n,P f_j>` converges to Q_t(h,f_j), contradicting (3).

This is a fixed-list conditional persistence result, not a claim that one selected j works for all critical directions. By Cauchy–Schwarz,
\[
 \|M_t^{-1/2}j_n\|^2\ge
 \frac{\kappa_{a,t}}{2\sum_{j=1}^r\|P_tf_j\|^2}.
 \tag{5}
\]
CC32 proved a persistent individual whole-row residual conditionally at contact; (4) identifies a finite fixed collection of genuine exterior witness functionals measuring it. The finite-list property is not supplied by a random finite source prefix or artificial divisor.

## 4. Exact rank-one source model and independent controls

Use the original-style model H=L2(0,B), D_s=L2(0,s), P=I, N h=int_0^B h, and Q=I+C, C=-|1_B><1_B|, with B>5/4. Its first contact is a=1 and contact kernel on D_a is K_a=span(1_[0,1]), dimension r=1. The fixed exterior packet f=1_(1,5/4) is a legitimate L2 exterior test for this rank-one model (it is NOT a smooth logarithmic-domain packet and does not pretend to be). For h=1_[0,1] normalized in P,
\[
 Q(h,f)=-1/4,\quad \|f\|_2^2=1/4,
\]
and the one-test normalized dual energy is `|Q(h,f)|^2/||f||^2=1/4`.

For old s<1, take `h_s=1_[0,s]/sqrt(s)`, lambda_s=s, delta_s=1-s. The exact forced functional on this fixed f is
\[
 J_s(f)=-\sqrt{s}/4,\qquad
 |J_s(f)|^2/\|f\|^2=s/4\longrightarrow1/4.
\]
The full dual energy on D_{5/4} is `s(5/4-s)`, and the remainder outside the fixed f test is `s(1-s)`, which tends to zero. The original-style relative incoming shell cost diverges as s->1 for this fixed target. This demonstrates that a finite fixed outward witness can detect genuine contact while supplying no mechanism that prevents it. The finite source model does not preserve zeta arithmetic, and its L2 step function is NOT transferred to the original logarithmic carrier.

## 5. Decision, validation scope, stopping rule

IP6 proves two useful qualitative facts about the actual original-source architecture (relative to accepted analytic dependencies): a **cap-uniform finite-dimensional approximation chart for near-zero-defect eigenvectors**, and **finite fixed exterior witnesses of any hypothetical first contact**.

Neither fact proves that actual first contact exists. Neither supplies its needed contradiction. The new finite witness theorem is conditional and is a different representation of CC29–CC32's mandatory persistent leakage, NOT the CC29/CC31 arithmetic upper bound.

No unweighted zero-frequency lower Riesz frame, per-height transverse density premise, or near-unit phase-distribution bound is imported; CC30's Lindelof warning still applies.

The next genuinely discriminatory arithmetic problem is to establish that, for every possible P-normalized contact-mode limit h and fixed exterior packet f, the complete Weil native mixed form enforces Q_t(h,f)=0 — while CC29 proves it would have to be nonzero. That would close RH, and currently no such arithmetic cancellation is proved. Alternatively, a concrete **new restricted theorem** might bound selected actual native exterior pairings without universalizing to RH. Do not present the finite-dimensional witness or compactness as that missing estimate.

Coupled remains active. Global NF71, Aperture and Shadow PS3 remain paused. CC35 remains the live Coupled mathematical parent. No new a>21/20 certificate, RH/F4, transport or Lean closure.
