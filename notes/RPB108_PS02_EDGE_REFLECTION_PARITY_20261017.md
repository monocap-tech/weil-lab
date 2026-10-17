# PS02 — Exact edge-strip parity incomparability in the original signed Weil form

**Lane:** W-PHYSICAL-SHIFT (parallel; scoped). **Parent:** PS01 physical difference-energy identity; RC313/315 exact seven-prime original translations. **Active canonical obligation stays W-ODD-NEG.** No completed W-ODD-NEG, W-EVEN-FORM, whole Weil positivity, or RH.

## 1. Half-interval Toeplitz–Hankel decomposition (exact)

Let \(B=11/10\), \(R=2B\), and \(h\in L^2([0,B])\). For \(\sigma\in\{+1,-1\}\), extend to the original physical carrier \(I=[-B,B]\) by
\[
(E_\sigma h)(x)=\begin{cases}h(x),&0\le x\le B,\\ \sigma h(-x),&-B\le x<0.\end{cases}
\]
Both extensions have squared physical norm \(2\|h\|_{L^2(0,B)}^2\). Define for \(0<u<R\)
\[
T_h(u)=\begin{cases}\displaystyle\int_0^{B-u}h(t)\overline{h(t+u)}\,dt,&0<u<B,\\0,&B\le u<R,\end{cases}
\]
\[
H_h(u)=\int_{\max(0,u-B)}^{\min(B,u)}h(t)\overline{h(u-t)}\,dt,
\]
and \(H_h(u)=0\) for \(u\ge R\). The reflected integrand is self-conjugate under \(t\leftrightarrow u-t\), so \(H_h(u)\in\mathbb R\).

For the original zero extension \(Z E_\sigma h\), *without wrapping*,
\[
\operatorname{Re}C_{E_\sigma h}(u)=2\operatorname{Re}T_h(u)+\sigma H_h(u)
\quad(0<u<R).
\]
Thus \(\|ZE_\sigma h-\tau_u ZE_\sigma h\|_2^2=4\|h\|_2^2-4\operatorname{Re}T_h(u)-2\sigma H_h(u)\), with both correlations zero past \(R\).

Use PS01's **complete** original signed seven-prime physical form:
\[
Q[g]=c_{\rm shift}\|g\|^2+
\int_0^\infty k(u)\|Zg-\tau_u Zg\|^2\,du
+\sum_{n\in\{2,3,4,5,7,8,9\}}w_n
\|Zg-\tau_{\log n}Zg\|^2
+2|\langle g,c\rangle|^2-2|\langle g,s\rangle|^2,
\]
where \(k(u)=e^{-u/2}/(1-e^{-2u})\), \(w_n=\Lambda(n)/\sqrt n\), \(c=\cosh(x/2)\), \(s=\sinh(x/2)\). Compare the same physical half-profile in the two parities. All scalar and Toeplitz contributions cancel:
\[
\boxed{\begin{aligned}
\Delta[h]:=Q[E_+h]-Q[E_-h]
={}&-4A_H[h]-4\sum_nw_n H_h(\log n)\\
&+8|\textstyle\int_0^B h(t)\cosh(t/2)\,dt|^2
+8|\textstyle\int_0^B h(t)\sinh(t/2)\,dt|^2,\\
A_H[h]={}&\int_0^{R}k(u)H_h(u)\,du .
\end{aligned}}
\]
The formula is established first for compactly supported piecewise-\(C^1\) profiles, for which the original log-weighted Fourier form is finite; standard form-domain extension must be justified for other inputs. **This is parity difference, not a claim either sector is nonpositive.**

## 2. Unexpected sign feature: archimedean Hankel is positive

The complete-monotone exponential series
\[
k(u)=\sum_{j\ge0}e^{-(2j+\frac12)u}
\]
gives on finite-energy profiles
\[
\boxed{A_H[h]=\sum_{j\ge0}\left|
\int_0^B e^{-(2j+\frac12)t}h(t)\,dt\right|^2\ge0.}
\]
Thus the entire archimedean **reflection** component is PSD, despite the original archimedean form having an additional Toeplitz and scalar contribution. Its contribution to \(\Delta\) has a *fixed nonpositive sign*. By contrast, each discrete prime-power reflection \(H_h(\ell)\) is indefinite on a nonempty symmetric overlap strip.

## 3. New original edge-strip theorem: neither parity dominates the other

Pick the **true largest original prime-power shift** \(\ell=\log 9\) and the supported half-interval strip
\[
a=\ell-B,\quad J=[a,B],\quad \delta=B-a=2B-\log9>0.
\]
Exact rational-log enclosures prove
\[
1<a<B,\quad \delta<1/100,\quad
2a>\log8\ge\log n\quad(n\in\{2,3,4,5,7,8\}).
\]
For every \(h\) supported in \(J\), all the *other six* true prime reflection terms vanish **exactly**, because \(t+s\ge2a>\log8\). The \(n=9\) reflection \(\mathcal R h(t)=h(\ell-t)\) maps \(J\) unitarily to itself and is an involution.

Choose *two explicit actual supported \(L^2\)-normalized* profiles, extended by zero off \(J\):
\[
h_+(t)=\delta^{-1/2}{\bf1}_J(t),
\qquad
h_-(t)=\sqrt{12/\delta^3}\,(t-\ell/2){\bf1}_J(t).
\]
They satisfy \(\mathcal Rh_+=h_+\), \(\mathcal Rh_-=-h_-\). Therefore
\[
H_{h_+}(\log9)=+1,\qquad H_{h_-}(\log9)=-1,
\]
and both full-domain extensions \(E_\sigma h_\pm\) are genuine compactly supported bounded-variation original-form test vectors.

Because \(a>1\), on \(J^2\) one has \(u=t+s>2\) and \(0<k(u)<2\). Consequently, for \(\|h\|_2=1\),
\[
0\le A_H[h]\le2\delta.
\]
The original signed pole terms retain their exact signs, and their sum in \(\Delta\) is nonnegative and bounded by
\[
0\le P[h]:=8|\langle h,c\rangle|^2+8|\langle h,s\rangle|^2
\le8\delta\cosh B.
\]
Writing \(w_9=\Lambda(9)/\sqrt9=\log3/3\), this yields **strict original signed parity-comparison witnesses**
\[
\boxed{\Delta[h_+]\le-4w_9+8\delta\cosh B<0},
\]
\[
\boxed{\Delta[h_-]\ge+4w_9-8\delta>0}.
\]
The validator independently certifies exact-rational strict margins greater than \(1.42\) and \(1.44\), respectively, with the two *different* supported \(h_\pm\) on the original half interval. Both parity extensions have norm squared \(2\). This **rules out both** \(Q_{\rm even}\succeq Q_{\rm odd}\) and \(Q_{\rm odd}\succeq Q_{\rm even}\) under the canonical half-interval identification.

This is a genuine **method no-go** for direct parity-order transfer. It does *not* prove either form has a negative direction: comparisons of two nonnegative forms can themselves be indefinite.

## 4. Why the edge strip matters for subsequent work

- The \(\log9\) reflection remains an \(L^2\) isometry on its nonempty edge strip even though that strip is only \(\approx0.0027754\) wide. Small geometric width cannot be used as a *small operator-norm* replacement.
- The archimedean reflection is a positive Hankel energy, explicitly a sum of rank-one Laplace moments. The finite prime reflection is a signed involution on the isolated strip. This is a structural difference between the prime and archimedean operators, not simply smaller quadrature error.
- Whole original even/odd operators might still share useful preconditioners. The proved incomparability rules out *simple sign-order* transfer; it does not rule out a coupled joint Schur argument.
- A promising PS03 question is whether one can factor out the **common Toeplitz energy**, then pay finite prime reflection involutions and the archimedean Hankel moments in a single certified operator inequality, preserving the original signed poles and all mixed couplings.

## 5. Reproducibility and standing

\`python3 scripts/validate_rpb108_ps02_edge_reflection.py\` checks seven original log shifts, precise dominance \(2(\log9-B)>\log8\), finite overlap, true weight \(w_9=\log3/3\), exact conservative kernel/pole envelopes, both strict parity-gap margins, and the original canonical obligation/PS01 parent.

This is an analytical result with source-rational inequality checks; it is **not independent peer review, not Lean formalization, not numerical 890x890 Schur PSD**, and does not establish the original signed Weil form positive. **Canonical W-ODD-NEG stays OPEN.**
