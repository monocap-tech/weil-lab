# MASTER-RECON-V01 — Load-bearing paper-proof verification

2026-11-24. Verification-only docket after 001I. ADOPT 0. Same-session re-derivation, not independent third-party review or Lean certification. No historical investigation released from stay.

## Custody and scope

Reopened the exact branch files:
- 001G-infinite-background.md blob cef1503563aec451bab7e90877428626f051598d.
- 001H-analytic-translation-rigidity.md blob 988dbfb56154c581b6e5935663a911d05b2888d9.
- 001I-terminal-audit.md blob d03cb42c11672743cffff405eaf8d7fde552b8a2.

Checked Bui–Conrey–Young, Acta Arith. 150 (2011), p.35, Theorem 1.1, equation (1.1), DOI 10.4064/aa150-1-3, against published PDF https://aimath.org/~kaur/publications/69.pdf : kappa* >= .4058 for simple critical-line zeros. Only a positive proportion is needed; neither its optimality nor RH is assumed. The Riemann–von Mangoldt local count and the classical polarized explicit formula in the full mixed-pole convention remain standard imported mathematical inputs, not newly formally proved.

## 001G audit

1. X_t is the closed supported subspace of weighted Fourier L² with weight w(xi)=log(2+|xi|). Inward dilation and mollification give density of C_c^infty(-t,t). Dilation convergence follows first for continuous compact frequency functions and then uniform boundedness near scale one. Compact inclusion X_t -> L² follows by truncating frequency: the tail norm is at most 1/sqrt(log(2+R)) and the bounded-frequency restriction of the Fourier transform on [-t,t] is Hilbert-Schmidt.
2. Radius-one submean disks around all complex ordinates (including multiplicity) have overlap O(log(2+|u|)), using the local count and strip |Im gamma|<1/2. Integration over |v|<=3/2 and multiplier chi(x)e^{vx} proves the upper bound. The multiplier estimate follows from w(u)<=C w(u-y)w(y), Schwartz decay of the Fourier kernels uniformly in v, and Young. Individual evaluations pass to X_t by supported L² convergence; all coefficient channels are the actual multiplicity-weighted ones.
3. In the unrestricted complex test class, full mixed-pole term, finite prime shifts and Gamma lower bound give W(f,f)>=||f||_log²-C_t||f||². The identity ||A_+ f||²=W(f,f)+||A_- f||² then gives the lower estimate with an L² defect. No finite-exception assumption or sign of pole pair is used.
4. If A_+f=0 then the entire Fourier transform vanishes at all simple critical-line ordinates, with count >>T log T by the cited theorem and total count. For nonzero f, Jensen centered at z0 with F(z0)!=0 and radius 2R bounds the number of zeros within R by O_f,t(R), contradiction. Thus A_+ injective.
5. Weak X_t / strong L² compactness removes the defect. Constants are uniform in the selected packet for each fixed t, not claimed uniform as t->infinity. Closed range, unique support-preserving preimages and right intersection equality follow. Strong projection convergence becomes norm convergence only under finite selected compression. At first contact the smaller-window positivity passes by inward approximation and Gamma_c>=I/2. No positivity beyond first contact is inferred.

No fatal error found in the raw 001G chain under its stated convention and classical inputs. Native Green metric is not identified with the log metric.

## 001H audit and shorter terminal proof

In the full coefficient Hilbert space let D be the block-diagonal bounded self-adjoint operator whose pair blocks are delta times the off-diagonal matrix [[0,1],[1,0]], and zero on critical-line coordinates. Then ||D||<=1/2. Let E_+ be the positive-channel orthogonal projection. The unbounded heights act by common pairwise phases; they cancel in the real translated positive pairing. Consequently
$$
B(a)=e^{-aD}E_+e^{-aD},\quad P(a)=A_t^*B(a)A_t
$$
are norm-entire in complex a, and for real a give precisely the translated positive form. No adjoint at complex a is inserted. The exponential power series gives
$$
\|B(a)-E_+\|\le e^{|a|}-1,\quad
\|P(a)-P(0)\|\le B_t(e^{|a|}-1).
$$
For example choose r>0 with B_t(e^r-1)<b_t/2 and r<epsilon/4; P(0)>=b_t I gives an inverse via Neumann series throughout the disk. This is an explicit radius in terms of the nonnumerical sampling constants.

For the finite selected negative packet the Riesz vector r(a) for the real-parameter pairing <A_-,Pi k,A_-,Pi tau_-a h> extends holomorphically, by finite exponential sums and fixed Riesz representers (extend conjugate-coefficient series in the second slot, not complex conjugation of a). Translation of test functions and k respects the chosen support margins. Therefore U(a)=P(a)^(-1)r(a) is holomorphic in the fixed X_t, and U(a)=tau_a k for real |a|<r.

**Alternative terminal proof (no exponential Fourier inversion or complex physical translations).** Suppose k != 0 and let d=ess sup supp k. Then d<=c<t. Take 0<s<min(r,t-d). Restrict U(a) to the fixed interval (d,t) by the bounded linear map X_t -> L²(d,t). The resulting Banach-valued holomorphic function is zero for real -r<a<=0 because tau_a k is supported to the left of d. By the scalar identity theorem applied to every bounded linear functional, the restriction vanishes throughout the disk. In particular tau_s k=0 a.e. on (d,t). Therefore k=0 a.e. on (d-s,t-s), which contains (d-s,d) since s<t-d. This contradicts the definition of the essential right support endpoint of a nonzero k. QED.

This avoids the original terminal Fourier exponential-weight step and is valid in any fixed carrier with bounded local L² restrictions and the stated translation identities. The original Fourier proof is also consistent. No analyticity of k is assumed. No finite omitted background assumption is needed; the selected negative response is finite.

## Adjudication and proposed Lean verification order

Paper audit: 001G and 001H retain their original standing in the unrestricted raw model. The simplified 001H endpoint proof should be preferred for formalization. No change to mathematical frontier; no source-level promotion.

Proposed modules, not submitted:
1. Abstract Picard-to-gap compression and finite selected right norm convergence.
2. Bounded strip block generator and analytic coercive inverse, with finite negative forcing extension.
3. Analytic translation orbit cannot have a compact essential right support endpoint.
4. Weighted sampling upper estimate, supported logarithmic compact inclusion and removal of L² defect; explicitly pin classical actual-zeta count and simple-zero-density inputs and the full signed explicit formula.
5. Native normalization and test-class equivalence, then assemble the exact selected marker claim. Audit separate restored-background limits only after their precise source definitions are available.

No Lean or lake execution attempted, no independent third-party audit, no comprehensive novelty review. Existing native signed-column reflected normalization and restored endpoint identification remain outstanding. No broad research release, no RH claim. Maintain ADOPT 0 until independent verification and the applicable formal checks actually pass.
