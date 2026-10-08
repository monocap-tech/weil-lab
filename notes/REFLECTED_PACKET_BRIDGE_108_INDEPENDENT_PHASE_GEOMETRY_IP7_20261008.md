# RPB108 — IP7: finite-cap native sign certificate through low-frequency compact-embedding modes

Date 2026-10-08. Independent checkpoint after IP6, based on active Coupled CC33–CC35 and CC31. **A: exact abstract-to-native finite-rank Schur criterion** with a quantitative rank bound obtained from the actual compact physical embedding; **C: mathematical/information limit** — criterion is sufficient, and a failing finite trial does not establish negativity unless its finite form itself has a certified negative value. NO new actual aperture sign, numerical zeta eigenvector, arithmetic defect suppression, RH/F4, or Lean theorem is claimed.

## 1. The full original target on a fixed aperture (without old positivity)

Fix finite B>=a0=21/20. Let H_B=D_B be the canonical supported logarithmic Fourier Hilbert space with squared norm integral log(e+|xi|)|hat h(xi)|² dxi. Use the ACTUAL original full divisor Weil signed form as represented in CC33:
\[
 Q_B=I+C_B,\qquad C_B=i_B^*R_B i_B.
\]
Here i_B:H_B->L²[-B,B] is the compact canonical physical embedding, R_B is the bounded selfadjoint COMPLETE native remainder after subtracting canonical log energy. Its contributions are the digamma-minus-log bounded multiplier, ALL active prime-power shift pairs through log n<=2B, and BOTH Hermitian cross-pole terms. CC33 supplies
\[
 \|R_B\|\le r_B:=r_*+
 2\sum_{\log n\le2B}\Lambda(n)/\sqrt n+4\sinh B,
\]
where r_*=sup_real_xi |Re psi(1/4+i*pi*xi)-log pi-log(e+|xi|)|<infinity. r_* is not numerically enclosed here. This native identity is analytic in the prior work; neither Q_B nor R_B is a finite modified zero dictionary. No sign of Q_B is assumed.

Let F be ANY finite-dimensional canonical subspace of H_B with orthogonal projector E, and suppose a rigorously VERIFIED physical tail bound is available:
\[
 \|i_B(I-E)\|^2\le\eta,\qquad
 r_B\eta<1.
\tag{1}
\]
The retained matrix is the exact native restricted signed form
\[
 A_F=E Q_B E|_F=I_F+E C_B E|_F.
\]
The complement operator D=(I-E)Q_B(I-E) and mixed block H=(I-E)Q_B E obey
\[
 D\succeq(1-r_B\eta)I,\qquad
 \|H\|\le r_B\sqrt\eta.
\tag{2}
\]
The first bound follows from |<Cy,y>|<=r_B||i_By||²; the second from |<Cx,y>|<=r_B||i_Bx||||i_By||, using ||i_BE||<=1. Identity contributions are orthogonal and have NO cross term.

## 2. A complete finite-dimensional strict positivity/negativity test

The exact full Schur complement is S=A_F-H*D^-1 H. Using (2),
\[
 S\succeq A_F-\frac{r_B^2\eta}{1-r_B\eta}I_F.
\tag{3}
\]
Thus
\[
 \boxed{\lambda_{\min}(A_F)>
       r_B^2\eta/(1-r_B\eta)\implies Q_B\succ0.}
\tag{4}
\]
This is positivity on EVERY vector of the entire infinite-dimensional D_B, hence also all D_s with s<=B. It is stronger than checking finite trial sign alone and makes no positivity assumption at B. Conversely if the actual retained A_F has a strictly negative eigenvalue, Q_B has a negative direction on F. If 0<=lambda_min(A_F)<=the threshold, the certificate is INCONCLUSIVE, not a sign result.

More quantitatively, for any 0<=mu<1-r_B eta, if
\[
 \lambda_{\min}(A_F)>
   \mu+\frac{r_B^2\eta}{1-r_B\eta-\mu},
\tag{5}
\]
then Q_B \succeq mu I (strict if (5) strict). This is the correctly shifted whole-complement test, not a positive physical eigenlevel confused with the ORIGINAL unshifted sign. To claim a numerical native sign one must enclose every finite retained entry with its actual prime/pole source errors and certify the inequality in rational intervals.

At a hypothetical nonnegative contact Q_B with a nonzero null h=x+y, x in F, y in F^\perp, D is positive by (2), so
\[
 y=-D^{-1}Hx,\qquad
 \|y\|\le \frac{r_B\sqrt\eta}{1-r_B\eta}\|x\|.
\tag{6}
\]
In particular the null vector cannot have x=0. Along that contact vector, <A_Fx,x>=<D^-1Hx,Hx> and the finite form has a direction no greater than the threshold in (4). This supplies a QUANTITATIVE finite contact witness, conditional on contact, not an exclusion.

## 3. A specific finite-rank space with explicit dimension and error estimates

Work in the actual H_B Fourier convention, and define the low-physical-frequency analysis map
\[
 V_R:H_B\to L^2([-R,R]),\quad V_R h=\widehat h|_{[-R,R]},
\qquad Z_R=V_R^*V_R.
\]
For any xi, |hat h(xi)|<=sqrt(2B)||h||_2<=sqrt(2B)||h||_{H_B}, so V_R is Hilbert--Schmidt, and
\[
 \operatorname{tr}Z_R=\|V_R\|_{HS}^2\le4BR.
\tag{7}
\]
This is CC31's already established low-frequency compact-observation construction, reused here for a NEW whole-target finite-Schur certificate. Fix R>=1 and tau>0. Choose E_{R,tau} the spectral projection of Z_R onto eigenvalues at least tau. Then
\[
 d:=\operatorname{rank}E_{R,\tau}\le 4BR/\tau.
\tag{8}
\]
For y perpendicular to its range,
\[
 \|i_By\|^2
 =\int_{|\xi|\le R}|\hat y|^2+\int_{|\xi|>R}|\hat y|^2
 \le\bigl(\tau+1/\log(e+R)\bigr)\|y\|^2.
\]
Thus the tail parameter in (1) is CERTIFIABLY
\[
 \boxed{\eta_{R,\tau}=\tau+1/\log(e+R).}               \tag{9}
\]
Combining (4), (8) and (9) is the promised finite-aperture test with explicit cap-dependent dimension and outside-space error budget. It does not require an a priori old signed gap or a source spectral eigenvector.

The spectral projection E_{R,tau} is mathematically specified but NOT yet numerically constructed in a rigorously enclosed basis. The inequality on A_F has NOT been evaluated at any target B, and r_* has not been bounded by an explicit interval in this pass. A future executable certification must enclose the finite spectral basis, the full native A_F matrix (including exact prime shifts and pole cross terms), r_*, and truncation errors. Therefore this theorem is NOT an evaluated positivity certificate.

The logarithmic tail is very slow: to make 1/log(e+R) less than a small eta requires R of order exp(1/eta). The resulting dimension bound grows at least with this R for this particular conservative construction. The method can be wildly impractical and does not replace the optimized CC18 finite native/source Gram computations.

## 4. Decisiveness away from contact, and the contact limitation

Choose any sequence R_n->infinity and tau_n->0 with eta_n->0. By (2),
\[
 \|C_B-E_n C_B E_n\|\le r_B(2\sqrt{\eta_n}+\eta_n)\to0.
\]
So if Q_B is STRICTLY positive with a fixed lower margin, the sufficient test (4) eventually succeeds at large enough n. If Q_B has a STRICT negative direction, the exact finite retained A_F eventually has a negative direction. At exact zero contact the test can remain inconclusive indefinitely. This is a mathematical finite-detection property, not a bounded-runtime algorithm with available arithmetic matrix computations.

A true all-aperture theorem would require successful sign certificates at arbitrarily large B, not merely availability of this method or its success at one finite B. The new criterion is strictly weaker than RH at any fixed cap and retains entire-domain sign custody.

## 5. Generic finite controls and relation to concurrent work

The companion exact rational validator tests the two-dimensional block Schur bound, shifted margin, a contact matrix with a one-dimensional kernel, a negative matrix not detected by a positive retained block, and genuine compact-remainder crossing ratios. It does NOT compute actual Q_B.

The new result is not CC31's critical-rank theorem: CC31 bounds the dimensionality of near-unit source spectral outputs on all old windows of a cap, whereas IP7 gives a target-aperture positivity/negativity bracket on the ENTIRE signed form from one certified finite retained native matrix and a full complement budget. It shares CC31's low-frequency compact observation tool, clearly identified in (7).

CC34 rejects unsigned smallness as the source-defect estimator; IP7 does not demand unsigned native remainder smallness on an actual near-critical lift. It only bounds the complement physically and keeps every SIGNED native entry of A_F. CC35's parity-pole correlation is retained exactly inside A_F, rather than thrown away or assumed to cancel.

**Next independent concrete task**: construct at one fixed new aperture B>21/20 a fully enclosed low-frequency spectral basis and evaluate the complete native A_F matrix and r_* with sufficiently tight intervals to decide (4), (5), or a negative trial. Before that numerical/symbolic audit, no positivity frontier is advanced.

Coupled is sole active integration frontier; IP7 is an independent finite-certification procedure and read-only dependency. Paused Global NF71 / Aperture and Pre-Contact Shadow PS3 are untouched. No RH/F4, retained transport or Lean closure is claimed.
