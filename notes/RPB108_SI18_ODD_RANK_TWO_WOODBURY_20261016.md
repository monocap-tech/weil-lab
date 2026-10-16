# RPB108 SI18 — two-direction physically supported odd Woodbury comparison

**Parent:** SI17 merged at \`0f3d6dc5ac58e3013c2f3d34951d8e36a98afcd0\` (PR #112).  
**Front:** independent structural investigation (SI), in parallel with native RC high Schur.  
**Result:** an explicit **rank-two physical positive operator minorant**, with full time-frequency concentration remainders and physically supported original Gram and odd source overlaps, yielding a *strictly better certified upper bound* for the same original odd Birman–Schwinger response. **No full-form positivity, SI11 finite matrix closure, Stage I, F4, Lean or RH.**

## 1. The original supported operator and the inherited signed positivity

SI11 decomposed the complete original supported Weil form \(Q=\mathfrak a-K\) with \(\kappa=1/1000\), \(a(\xi)=\max\{m(\xi),\kappa\}\), and the positive physically supported selfadjoint \(A\) associated with
\[
\mathfrak a[f]=\int_\mathbb R a(\xi)|\widehat{Zf}(\xi)|^2\,d\xi
+2|\langle f,\cosh(x/2)\rangle|^2.
\]
Here \(m\) is the *actual original* signed archimedean-plus-seven-prime multiplier of CC27/RC312–313 (including original base-prime logarithms on prime powers), \(Z\) zero extension on \(I=[-B,B]\), \(B=11/10\). The odd pole vector is \(s(x)=\sinh(x/2)\). We study the same fixed \(2\langle s,A_o^{-1}s\rangle\) as SI12–17; the positive even pole vanishes on odd inputs.

The original all-frequency rational phase/digamma verification of SI13 proves \(m(\xi)>7/5=1.4\) on the *entire* interval \([.22,.38]\) and reflection. The separate SI14 exact continuous proof gives \(m(\xi)>1.201\) across \([.73,.79]\) and reflection. In particular for
\[
c_1=3/10,\qquad c_2=19/25,\qquad r=1/125,
\qquad J_i^\pm=\pm[c_i-r,c_i+r]
\]
with \(\delta_1=1399/1000,\;\delta_2=6/5\), both complete windows are disjoint and satisfy the needed *original signed* \(m(\xi)>\kappa+\delta_i\). No proof depends on positivity at a single sampled frequency.

## 2. Fully paid whole-operator concentration remainders

On the **odd physical Hilbert space** \(H_o\subset L^2(I)\), put
\[
h_c(x)=\sin(2\pi cx),\qquad
T_{J_i,o}=2\int_{c_i-r}^{c_i+r}|h_\xi\rangle\langle h_\xi|\,d\xi.
\]
These are *actual supported* positive frequency-compression operators, not unphysical Fourier restriction of the physical input.

As SI17 proved from the exact first and second frequency derivatives of the physical sine feature, the operator-valued map \(F(\xi)=|h_\xi\rangle\langle h_\xi|\) has the all-real bound
\[
\|F''(\xi)\|\le C:=\frac{10}{3}(44/7)^2B^3.
\]
Symmetric Taylor integration kills its linear term and pays the *complete* operator remainder
\[
\boxed{\|T_{J_i,o}-4r|h_{c_i}\rangle\langle h_{c_i}|\|
\le\varepsilon=\frac23Cr^3<\frac1{16000}.}
\]
Summing two separate signed original positive windows gives the **correct supported Loewner lower bound**
\[
\boxed{
A_o\succeq\kappa' I_o+
\gamma_1|h_{c_1}\rangle\langle h_{c_1}|+
\gamma_2|h_{c_2}\rangle\langle h_{c_2}|,
}
\]
with
\[
\kappa'=\kappa-(\delta_1+\delta_2)\varepsilon>8/10000>0,\quad
\gamma_i=4r\delta_i>0.
\]
This deducts **both** potentially adverse operator-norm remainders from the positive floor, rather than treating their errors as independently positive.

## 3. Fully signed physical Gram and source-overlap custody

For real physical \(h_{c_i}\), the exact Fourier/trigonometric identities are
\[
\begin{aligned}
q_i&=\langle s,h_{c_i}\rangle
=\frac{2[
\frac12\cosh(B/2)\sin(2\pi c_i B)
-(2\pi c_i)\sinh(B/2)\cos(2\pi c_i B)]}
{\frac14+(2\pi c_i)^2},\\
G_{ij}&=\langle h_{c_i},h_{c_j}\rangle
=\frac{\sin(2\pi B(c_i-c_j))}{2\pi(c_i-c_j)}
-\frac{\sin(2\pi B(c_i+c_j))}{2\pi(c_i+c_j)},
\end{aligned}
\]
with the continuous diagonal limit \(G_{ii}=B-\sin(4\pi Bc_i)/(4\pi c_i)\). All these quantities are **actual physically supported integrals**, not projections onto unrestricted Fourier modes.

Using SI06's rigorous rational Machin \(\pi\) enclosure and SI14's rational sine/cosine phase-enclosure code (with rational \(\sinh,\cosh\) Taylor bounds), the SI18 validator checks the following strict *outward* rational intervals:
\[
\begin{array}{l}
541/1000<q_1<543/1000,\quad -167/1000<q_2<-165/1000,\\
1323/1000<G_{11}<1325/1000,\quad
1191/1000<G_{22}<1194/1000,\\
-144/1000<G_{12}<-141/1000,\\
\|s\|_2^2=\sinh B-B<235648/10^6.
\end{array}
\]

## 4. Correct-sign rank-two physical Woodbury inverse

Write \(H:\mathbb C^2\to H_o\), \(Hu=u_1h_{c_1}+u_2h_{c_2}\), and \(\Gamma=\mathrm{diag}(\gamma_1,\gamma_2)\). Our *explicit, invertible, supported reference* is
\[
C_o=\kappa'I+H\Gamma H^*,\qquad A_o^{-1}\preceq C_o^{-1}.
\]
The **exact reference-only** Woodbury identity reads
\[
\boxed{
C_o^{-1}=\kappa'^{-1}I-
\kappa'^{-2}H\left(\Gamma^{-1}+\kappa'^{-1}H^*H\right)^{-1}H^*.
}
\]
There is no claim of an explicit inversion of the original \(A_o\) and no replacement of \(A_o^{-1}\) by the unrestricted multiplier reciprocal \(1/a(\xi)\).

For \(q=H^*s\) and \(G=H^*H\), put
\[
M=\Gamma^{-1}+\kappa'^{-1}G
=\begin{pmatrix}a&b\\b&d\end{pmatrix}\succ0.
\]
Then
\[
2\langle s,A_o^{-1}s\rangle
\le 2\left[\frac{\|s\|^2}{\kappa'}-
\frac{1}{\kappa'^2}\frac{dq_1^2-2bq_1q_2+aq_2^2}{ad-b^2}\right].
\]
The original \(q_1>0,q_2<0,b<0\) signs are included. The exact rational validator uses the **correct adverse sign** for the cross term: here \(bq_1q_2>0\), hence \(-2bq_1q_2\) is negative and cannot be omitted for a *lower* correction certificate. It lower-bounds the numerator using rational outward intervals and upper-bounds the positive denominator by \(a_{\max}d_{\max}\), yielding a fully valid but conservative correction lower bound. The resulting **actual original odd supported inverse upper** is asserted strictly below **29**, improving SI17's certified strict bound below 42.

No claim that 29 is an attained inverse value, that the rank-two reference optimally approximates \(A^{-1}\), or that the original negative odd pole is absorbed is made.

## 5. Strategic outcome and SI19 frontier

This is a concrete structural gain from **two genuinely different physical odd directions**. It also resolves SI17's requested off-diagonal Gram and **correct-sign small Woodbury comparison**. The original supported odd scalar BS threshold remains \(1\); SI18 still falls well short. Also the full negative-frequency operator from SI11 is present in the complete original Weil form, and no complete SI11 finite BS matrix has been certified.

**SI19:** Search for a smaller reference dimension versus stronger supported spectral lower bound by (i) selecting a third independent *original signed-positive* odd frequency direction, (ii) sharpening the polynomial Gram/overlap enclosures and remainder, or (iii) replacing a scalar floor \(\kappa'\) with an odd positive-reference inverse response that accounts for the entire positive-frequency multiplier. The benchmark is strictly below 29 **at a comparable rigor and cost**, then compare the work to the native RC high Schur route. Stop if increasing dimensions merely produces marginal gains without addressing the full signed form.

**Reproduction:** \`python scripts/validate_rpb108_si18_odd_rank_two_woodbury.py\` plus existing full Structural Investigation suite under GitHub Actions. The exact numeric inequalities are regression-certified in Python \`Fraction\`; the operator-valued Taylor theorem and Loewner inverse comparison are analytic inputs, not independent peer review or Lean formalization.

**No full original Weil positivity, original \(A^{-1}s\) vector, complete signed cross-Schur/finite BS eigenvalue, Stage I, F4, Lean or RH claim.**
