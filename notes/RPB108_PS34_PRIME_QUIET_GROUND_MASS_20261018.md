# PS34 — An actual macroscopic nonconcentration certificate for the original even pole-free ground state

**W-PHYSICAL-SHIFT · October 18, 2026 · stacked on PS33 draft PR #202.**
Original object: the **true zero-extended seven-prime, thirteen-source-eliminated, positive-even-pole-FREE even Schur form**
\[
L=\mathfrak S_C^{(0)}|_{\rm even}
=J_C+V_{0,C}-B_0^*A_0^{-1}B_0
\]
from PS27–PS33. This checkpoint upgrades PS32's astronomically microscopic ground-state set-mass estimate to a quantitative result on a **specific, ordinary physical interval of width 1/256**, exploiting *original* PS18 prime-quiet source geometry, original PS13 local positivity, and the negative ground eigenvalue equation. It does **not** calculate the original ground eigenfunction, ground-cell weights on every PS31 cell, second eigenvalue, source-renormalized coherent pole angle, signed odd/even Weil positivity or RH. The inherited infinite-dimensional source/log-form claims and the new Carleman/domain argument require independent mathematical audit.

## 1. Explicit reflected prime-quiet physical window

PS18 certified that
\[
J_{\rm quiet}=[269/5000,\;1163/10000]\subset C
\]
has length \(1/16\), all seven ORIGINAL prime shifts are disjoint from each of the true 13 PS15 source intervals, and the **original archimedean** source-to-\(J_{\rm quiet}\) operator has
\[
\|B_{\rm arch,PJ_{\rm quiet}}\|_{\rm HS}^2<(7/40)^2.
\]
Choose the rational **macroscopic** subinterval
\[
\boxed{H=[9/100,\;9/100+1/256]\subset J_{\rm quiet},\qquad |H|=1/256.}
\]
Let \(E=H\cup(-H)\), a reflection-symmetric subset of the genuine source complement \(C\), with
\[
\boxed{|E|=1/128.}
\]
The maximum possible distance between points of \(E\) is
\(2(9/100+1/256)<1/5<\log2\), so **every original seven-prime self-translation of an \(E\)-supported function vanishes**. Since \(H\subset J_{\rm quiet}\), the true source/quiet prime cross is also zero.

From PS18's explicit *per-source original geometry* HS proof, retaining its original per-channel separation \(d_r\),
\[
\begin{aligned}
\|B_{\rm arch,PE}\|_{\rm HS}^2
&\le |E|\delta\sum_{\text{13 original source }r}
\Bigl(1+\frac1{2d_r}\Bigr)^2\\
&<\frac{|E|}{|J_{\rm quiet}|}\left(\frac7{40}\right)^2
=\boxed{\frac18\left(\frac7{40}\right)^2=:q_E.}
\end{aligned}
\]
This uses the actual original source-shift enumeration rather than scaling an arbitrary HS norm without a uniform pointwise kernel bound.

On the **even** sector, the negative odd pole contributes zero to the pole-free mixed source block \(B_0\); the positive even pole was removed *before* defining \(B_0\). Consequently
\[
\boxed{\|B_0P_E\|^2<q_E,\quad
\|P_E B_0^* A_0^{-1} B_0P_E\|
<q_E\,\frac{9000}{1997}.}
\]
No genuine source inverse is omitted. The original PS27 \(A_0>(1997/9000)I\) remains the only source-inverse premise.

## 2. NEW: the actual auxiliary even Schur is strictly positive on **all** even E-supported profiles

For every original log-form admissible \(h\) that is even and supported in \(E\), split \(h=h_++h_-\), where \(h_\pm\) lie in \(\pm H\) and are reflections.

The original PS13/PS18 local (full signed-pole) estimate, for arbitrary profiles supported on a subinterval of the prime-quiet \(J_{\rm quiet}\), gives
\[
Q[h_+]+Q[h_-]>\frac{133}{500}\bigl(\|h_+\|^2+\|h_-\|^2\bigr).
\]
The original digamma *cross* between \(\pm H\) is an attractive kernel \(-k(|x-y|)\). Their separation is \(d\ge2(9/100)=9/50\). Since the original \(k(u)\le1/(2u)+1\), Schur's bound gives
\[
\|1_H\,k(|x-y|)\,1_{-H}\|
\le |H|\biggl(\frac{1}{2(9/50)}+1\biggr)
=\frac{17}{1152}.
\]
The original cross seven-prime autocorrelations vanish identically, and for **even** \(h\), the full original cross of its positive even pole and negative odd pole is **nonnegative** relative to the sum of the two separate local quadratics. Therefore
\[
\boxed{Q[h]>\left(\frac{133}{500}-\frac{17}{1152}\right)\|h\|^2.}
\]
Carefully remove the original **positive even pole before source elimination**:
\[
Q_0[h]=Q[h]-2|\langle c,h\rangle|^2,\qquad
2\|c1_E\|^2
<2|E|(7/6)^2=\frac{49}{2304}.
\]
The *exact* original source-first Schur, with its genuine \(A_0^{-1}\), thus obeys
\[
\begin{aligned}
L[h]&=Q_0[h]-\langle B_0h,A_0^{-1}B_0h\rangle\\
&>\left(\frac{133}{500}-\frac{17}{1152}
-\frac{49}{2304}
-\frac18\left(\frac7{40}\right)^2\frac{9000}{1997}\right)\|h\|^2\\
&>\boxed{\frac15\|h\|^2.}
\end{aligned}
\]
This is a **genuine original, infinite-dimensional, positive pole-free even Schur local support theorem**, unlike PS18's full positive-pole-included local result. The exact rational strict positive margin is \(>0.2127\). It applies to *all* original admissible even \(E\)-supported profiles, not just a finite toy basis, conditional on accepted original PS13/PS18 source/local analytic lemmas.

## 3. NEW: bounded cross from E to the remaining ORIGINAL complement

Write \(\bar E=C\setminus E\). The original arch cross between \(E\) and \(\bar E\) is **bounded in physical L²** even though \(k(u)\sim1/(2u)\) at the four interfaces. Split
\[
k(u)\le\frac{1}{2u}+1\qquad(0<u\le 11/5).
\]
PS18 proved this for \(u\le1\); for \(u\ge1\), monotonicity and \(k(1)<1\) extend it to the full actual physical diameter. A direct Carleman inequality
\[
\left|\int_{s,t>0}\frac{f(s)g(t)}{s+t}\,dsdt\right|
\le\pi\|f\|_2\|g\|_2
\]
applied on each of the **four actual interfaces** of \(\pm H\), with the coefficient \(1/2\), gives
\[
\|\mathrm{cross}_{E,\bar E}(J)\|
\le 2\pi+\sqrt{|E||I|}
<\frac{44}{7}+\frac17=\frac{45}{7}.
\]
The regular constant-kernel contribution is bounded by \(\sqrt{(1/128)(11/5)}=\sqrt{11/640}<1/7\). This cross is **not** declared Hilbert–Schmidt; it is a real bounded Carleman cross with all interfaces included.

All genuine seven-prime bounded lower-order terms remain in \(V_{0,C}\); PS17's original signed full-pole \(\|V_C\|<13\) and PS27 \(\|c_C\|^2<539/180\) yield
\[
\|V_{0,C}\|<13+\frac{539}{90}<19.
\]
For the entire original source response, use the *small true E-source bound*, rather than the useless global \(\|R\|<1400\):
\[
\begin{aligned}
\|P_E B_0^*A_0^{-1} B_0P_{\bar E}\|
&\le\|B_0P_E\|\,\|A_0^{-1}\|\,\|B_0P_{\bar E}\|\\
&<\sqrt{q_E}\,\frac{9000}{1997}\frac{1403}{80}<5.
\end{aligned}
\]
Thus the actual complete original pole-free even mixed quadratic operator satisfies
\[
\boxed{\|L_{E,\bar E}\|
<\frac{45}{7}+19+5<31.}
\]
This preserves the full original digamma Carleman interface, every original signed seven-prime translation, and the entire actual source inverse correction.

**Form-domain interface qualification:** for the logarithmic zero-extended digamma form, the two-sided characteristic multiplication by these four rational cuts is form-domain preserving; the proof is first on a smooth original form core, using the above bounded Carleman mixed form and \(J\ge0\) to uniformly control the two restricted positive energies, and then passing to the original closed form by lower semicontinuity. This is an explicit analytic step needing independent review; **not** a claim that sharp cutoffs work for arbitrary fractional Sobolev spaces of positive order.

## 4. NEW: actual original positive ground MUST carry >2% of its mass outside H

PS29 gives an original even pole-free lowest eigenfunction \(\phi_0\ge0\), \(\|\phi_0\|_{L^2(C)}=1\), \(L\phi_0=\lambda_0\phi_0\). PS27's true original auxiliary constant negative witness ensures
\[
\boxed{\lambda_0<-4.359740.}
\]
Decompose \(\phi_0=p+z\) with \(p=1_E\phi_0\), \(z=1_{\bar E}\phi_0\), both even and admissible. Testing the **actual original ground eigenvalue equation** against \(p\) gives
\[
\langle p,(L_{EE}-\lambda_0)p\rangle
=-\langle p,L_{E,\bar E}z\rangle.
\]
The new **original positive** local E theorem, original negative eigenvalue and the complete cross bound imply
\[
\left(\frac15+|\lambda_0|\right)\|p\|^2
<31\|p\|\|z\|,
\qquad
\frac15+|\lambda_0|>\frac92.
\]
If \(\|p\|=0\), \(\|z\|=1\) and the result is immediate. Otherwise
\[
\|p\|<\frac{62}{9}\|z\|,
\quad \|p\|^2+\|z\|^2=1
\quad\Rightarrow\quad
\boxed{\|z\|^2>\frac{81}{3925}>0.0206.}
\]
Since the ground state is even and normalized, PS31's **actual true physical** half-carrier ground measure \(\mu(A)=2\int_A\phi_0^2\) satisfies the **new macroscopic bound**
\[
\boxed{\mu(C_+\setminus H)=\int_{C\setminus E}\phi_0^2>\frac{81}{3925}.}
\]
Equivalently \(\boxed{\mu(H)<3844/3925}\). This holds for the fixed original physical interval \(H\) of length \(1/256\), unlike PS32's estimate only at sets of size \(2^{-8096}\). It **does not** give individual PS31 graph bin mass lower bounds on arbitrary cells, pointwise \(\phi_0\), the needed \(W_N\) lower entries or true one-negative-index closure.

## 5. Next test and proof-standing discipline

Focused exact Fraction replay validates the original PS18 rational geometry and all source-arc/Carleman/prime/pole signs, the strict local Schur margin, the full cross allowance, and the exact \(81/3925\) bound. A two-block exact-rational witness tests the logical step from positive local block, negative eigenvalue and bounded cross to a **positive outside-mass requirement**. It is **only an algebraic regression**, not a substitute eigenfunction computation.

**PS35:** improve local cross bounds, build several independent *actual original prime-quiet mirrored intervals*, and/or establish true original positive-mass bounds in specified complementary cells (rather than outside a given one). Incorporate the original eigen-equation or a ground-independent min–max argument to decide \(\lambda_1\ge0\). PS29's original effective-pole \(\beta,\Delta,\alpha\) scalar still require separate certificates after the index sign.

**Custody:** PS34 is explicitly PS-scoped. Canonical \`W-ODD-NEG\` remains open; \`W-EVEN-FORM\`, full original signed Weil, native CC27 D-Riesz bridge and RH remain OPEN. This is a scoped positive local pole-free even Schur theorem and quantitative actual original ground macroscopic nonconcentration, not global positivity.
