# RPB108 — IP5: cap-uniform small-step forcing and the compact-remainder contact boundary

Date: 2026-10-08. Independent IP5 continues IP4; active Coupled research head CC33 at 80644d007765195afccbed606d1128965f165d06. Classification: new qualitative actual-zeta operator estimate **conditional on the inherited native-source attachment and compact remainder of CC33**, plus a sharp generic source countercontrol. No RH/F4, new aperture, numerical actual critical mode, or Lean result.

## 1. New cap-uniform aperture modulus

Fix B>a0=21/20. Let H_B=D_B be the canonical compact-support logarithmic Fourier Hilbert space, and Pi_s the H_B-orthogonal projection onto D_s, for 0<s<=B. The projections are in the canonical metric, NOT the positive-source metric. The actual native CC33 identity on H_B is
\[
 Q_B(h,k)=\langle h,k\rangle_{H_B}+\langle C_Bh,k\rangle_{H_B},\qquad
 C_B=i_B^*R_Bi_B.
\]
Here i_B:H_B->L2[-B,B] is compact physical embedding; R_B is the bounded selfadjoint complete native remainder consisting of the digamma-minus-log multiplier, all prime-power shifts on the cap, and both Hermitian-cross-pole terms. Thus C_B is compact selfadjoint. Its compression gives the consistent actual right-limit forms on D_t for t<=B.

Define
\[
 \epsilon_B(h):=
 \sup_{\substack{a_0\le s<t\le B\\t-s\le h}}
 \|(\Pi_t-\Pi_s)C_B\Pi_s\|_{H_B\to H_B}.
 \tag{IP5.1}
\]
**Theorem:**
\[
 \boxed{\lim_{h\downarrow0}\epsilon_B(h)=0.} \tag{IP5.2}
\]
The modulus is a pure *absolute increment* bound. No rate is claimed, and it is not an old-defect-relative estimate.

**Proof.** For each a in (0,B], closure of the union of D_s for s<a equals D_a: first use the inherited compact smooth core and then inward shrink the support of each test. For a<B, the intersection of D_t for t>a is D_a: any common member is supported in every [-t,t], hence [-a,a], since H_B convergence implies distributional/L2 convergence. Monotone Hilbert projections therefore satisfy Pi_s->Pi_a strongly from both sides; in particular s->Pi_s v is norm-continuous on [a0,B] for every fixed v in H_B.

For sequences a0<=s_n<t_n<=B with t_n-s_n->0, compactness of [a0,B] gives a subsequence with s_n,t_n->a. The difference Pi_{t_n}-Pi_{s_n} tends strongly to zero, is bounded in norm by one, and hence tends UNIFORMLY to zero over the compact image of the unit ball under C_B. Thus
\[
 \|(\Pi_{t_n}-\Pi_{s_n})C_B\|\to0.
\]
The extra factor Pi_{s_n} is a contraction, proving (IP5.2) by contradiction. This does NOT claim ||Pi_t-Pi_s||->0 in operator norm.

## 2. Actual forced-row corollary

For any strictly original-source-positive old s and t>s on this cap, take an actual generalized critical source-normalized old lift h_i from CC20, with
\[
 \|P_sh_i\|=1,\quad\lambda_i=1-\delta_i,\quad
 c_B^2I\preceq M_t=P_t^*P_t\preceq U_B^2 I.
\]
CC33's exact canonical principal cancellation gives the forced-row Riesz vector
\[
 j_i=(\Pi_t-\Pi_s)C_Bh_i-\delta_i(I-\Pi_s^{D_t})M_th_i.
 \tag{IP5.3}
\]
Because ||h_i||_{H_B}<=1/c_B and the second correction obeys
\[
 \|M_t^{-1/2}(I-\Pi_s^{D_t})M_th_i\|\le U_B/c_B,
\]
we obtain the **actual cap-uniform absolute bound**
\[
 \boxed{
 \|M_t^{-1/2}j_i\|
 \le \epsilon_B(t-s)/c_B^2+(U_B/c_B)\delta_i.
 } \tag{IP5.4}
\]
Every actual critical eigenvector obeys this, independent of its frequency and of the old signed source gap except for the displayed delta correction. The only arithmetic-dependent input is CC33's already proved original native remainder identity and observability, NOT any new arithmetic cancellation.

Equation (IP5.4) makes the complete forced-row norm vanish in the *JOINT* limit t-s->0 and delta_i->0. It gives NO cap-only fixed positive step h_B for which the first term vanishes with delta_i. A positive constant depending on h_B is insufficient for the CC29/CC31 vanishing-modulus target. Nor does compactness provide a quantitative h-power rate from this proof alone.

## 3. Rank-one compact countercontrol at genuine first contact

Let H=L2(0,B), B>1, with D_s=L2(0,s), P=I and complete rank-one negative analysis
\[
 Nh=\int_0^B h(x)\,dx.
\]
Then M=I and the original-style signed form is Q=I+C, where C=-|1_B><1_B| is rank one and compact. The old source gain is exactly lambda_s=s for 0<s<1, with old defect delta_s=1-s; first zero contact occurs at s=1. For any t>1 the enlarged Q has a negative eigenvalue 1-t on its normalized constant supported direction.

The P-normalized old critical lift is h_s=1_[0,s]/sqrt(s). The canonical outgoing native remainder forcing has
\[
 q_s=(\Pi_t-\Pi_s)Ch_s=-\sqrt{s}\,1_{(s,t)},\qquad
 \|q_s\|^2=s(t-s).
\]
Since M=I, the defect correction vanishes and j_s=q_s. The incoming source-shell gain is exactly t-s, while its inverse old-defect relative cost is
\[
 \boxed{\frac{t-s}{1-s}.} \tag{IP5.5}
\]
The uniform compact remainder modulus is explicitly
\[
 \|(\Pi_t-\Pi_s)C\Pi_s\|^2=s(t-s)\le B(t-s).
\]
Despite this uniform O(sqrt(h)) absolute forcing, the relative cost diverges as s->1 for any fixed t>1, and even for cap-only constant small steps t=s+h. With rational s=63/64 and t=33/32, the old defect is 1/64, increment 3/64, row energy 189/4096, relative budget 3, and enlarged negative eigenvalue -1/32.

This finite-rank source model does NOT satisfy the complete actual zeta Weil formula and is not evidence that a zeta contact occurs. It proves only that compactness plus a uniform shrinking-step absolute norm bound cannot exclude first contact.

## 4. Verification, relevance and stopping rule

The companion exact Fraction validator tests the rank-one formulas for multiple rational old windows and target steps, including the explicit sample, and confirms the uniform squared envelope. Those algebra checks do not prove the infinite-dimensional compact projection-continuity argument or calculate actual zeta eigenvectors.

IP4 supplies a complete two-sided exterior test space; IP5 independently bounds the full actual forced row ABSOLUTELY as the aperture step shrinks, without reducing to finitely many packets. The new fact is genuinely weaker than RH and uses the source arithmetic only through CC33's exact native compact remainder.

The **next arithmetic gate is still** a fixed-cap, fixed-positive-step, actual-old-critical-eigenvector bound with a scalar modulus tending to zero WITH the spectral defect:
\[
 \|M_t^{-1/2}j_i\|^2\le b_B\lambda_i\omega_B(\delta_i),\qquad
 \omega_B(\delta)\to0.
\]
Merely shrinking t-s with delta, proving smooth-packet density, bounding high-frequency averages, or invoking compactness again does not meet that gate.

No new certified aperture beyond a=21/20; no global non-stalling, RH/F4, transport or Lean closure. Coupled sole active integration, Global NF71 and Shadow PS3 paused.

## 5. Local exact test outcome

The [reproducible IP5 source-control validator](../scripts/validate_native_small_step_ip5.py) was independently executed using Python Fraction arithmetic: **74 of 74 exact rational assertions passed**. These check the compact rank-one old gain, fixed-step divergence, squared forcing envelope and explicit negative-target sample. The native zeta uniform small-step theorem remains an analytic deduction from CC33 and the supported-domain projection facts, not a numerical zero computation or Lean certification.
