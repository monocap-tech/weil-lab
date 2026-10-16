# RPB108 SI15 — first genuine supported odd trial inverse with the FULL original residual

**Parent:** merged SI14 \`bf03d1363e27200d0078fb5fb4079a37daaa7c95\`.  
**Track:** independent Structural Investigation, native RC original signed high-inverse/Schur route preserved.  
**Standing:** analytic **actual physically supported** odd trial \(y\in\operatorname{Dom}A\), with a rigorous bound on the **entire, unprojected residual** \(s-Ay\), and a correct-sign supported inverse comparison. The certified bound is a *weak proof-of-interface*, **strictly WORSE than SI14's tighter inverse comparator**; no complete odd-pole positivity, full Weil form positivity, Stage I, F4, Lean or RH claim.

## 1. Recover the genuine supported operator

SI11–14 decompose the original CC27/RC312–313 signed Weil form on \(H=L^2([-B,B])\), \(B=11/10\), as \(Q_{\rm Weil}=\mathfrak a-K\), with
\[
\begin{aligned}
a(\xi)&=\max\{\underbrace{\Re\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n=2,3,4,5,7,8,9}
\frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n)}_{m(\xi)},\,\kappa\},
\qquad\kappa=10^{-3},\\
\mathfrak a[f]&=\int_{\mathbb R}a(\xi)|\widehat{Zf}(\xi)|^2d\xi
+2|\langle c,f\rangle|^2,\quad
c(x)=\cosh(x/2),\quad s(x)=\sinh(x/2),\\
A&=\text{positive selfadjoint operator associated with }\mathfrak a,\qquad A\succeq\kappa I.
\end{aligned}
\]
The original \(\Lambda(n)\) for \(4,8,9\) uses the base-prime logarithm. The physical zero extension \(Z\), not an illicit whole-line inverse, is retained throughout.

The trial is the **concrete odd supported vector**
\[
\boxed{y=\alpha s,\qquad\alpha=\frac1{4800}.}
\]
Because \(s\) is odd and \(c\) even, the original even positive pole annihilates \(s\). Moreover, \(s\in\operatorname{Dom}A\) as a genuine operator vector, not just the form domain. The proof of this domain statement is the global Fourier tail bound below: \(a\widehat{Zs}\in L^2(\mathbb R)\), and for every form-domain \(f\),
\[
\mathfrak a[s,f]
=\left\langle Z^*\mathcal F^{-1}(a\widehat{Zs}),\,f\right\rangle.
\]
Hence the supported operator action is
\[
\boxed{As=Z^*\mathcal F^{-1}(a\widehat{Zs})\in H,}
\]
not \(\mathcal F^{-1}(a\widehat{Zs})\) regarded as a supported whole-line function. In particular,
\(\|As\|_H\le\|a\widehat{Zs}\|_{L^2(\mathbb R)}\).
The entire original supported trial residual is
\[
\boxed{R=s-Ay=s-\tfrac1{4800}As.}
\]
It is *not* a projected/Galerkin residual.

## 2. Fully explicit original high-frequency upper for the entire supported action

Euler's positive decreasing quarter-digamma series
\[
\Re\psi(1/4+iy)=\psi(1/4)
+\sum_{k\ge0}\frac{y^2}{(k+1/4)((k+1/4)^2+y^2)}
\]
obeys
\[
\sum_{k\ge0}g_y(k)\le g_y(0)+\int_0^\infty g_y(t)dt
\le4+\tfrac12\log(1+(4y)^2).
\]
As \(\psi(1/4)-\log\pi<0\), and the original SI06 full signed prime envelope \(2C<8\), with \(\pi<22/7\) and \(4\pi<14\), one obtains the global **upper** multiplier bound
\[
\boxed{0<\kappa\le a(\xi)<12+\log(1+14|\xi|).}
\]
The pointwise bound controls the **positive** multiplier \(a=\max(m,\kappa)\). No unsupported pointwise *inverse* bound is assumed.

For the original odd physical function \(s(x)=\sinh(x/2)\), SI12's rational hyperbolic Taylor enclosures give
\[
\|s\|_2^2=\sinh B-B<\frac14,\qquad
\sinh(B/2)<\frac35.
\]
Integration by parts of the original zero extension gives, for \(|\xi|\ge1\),
\[
\boxed{
|\widehat{Zs}(\xi)|
\le\frac{2\sinh(B/2)}{\pi|\xi|}
<\frac{2}{5|\xi|}.
}
\]
This pays both endpoint jumps **and** the interior derivative; it does not falsely assume zero endpoint traces.

For \(|\xi|\le1\), \(a(\xi)<74/5\), so Plancherel bounds the contribution by \((74/5)^2(1/4)=1369/25\).
For \(|\xi|\in[2^k,2^{k+1}]\) and the reflected band, \(a(\xi)<31/2+(7/10)k\), since
\(1+14\cdot 2^{k+1}<2^{k+5}\) and \(\log2<7/10\). The two-sided integral of \(|\xi|^{-2}\) over each shell is \(2^{-k}\). The exact summation identities
\(\sum2^{-k}=2,\ \sum k2^{-k}=2,\ \sum k^2 2^{-k}=6\)
yield a high-frequency energy upper of
\[
\frac4{25}
\sum_{k\ge0}2^{-k}\bigl(\tfrac{31}{2}+\tfrac7{10}k\bigr)^2
=\frac{52684}{625}.
\]
Therefore
\[
\boxed{
\|As\|_2^2
\le\int_{\mathbb R}a^2|\widehat{Zs}|^2
<
\frac{1369}{25}+\frac{52684}{625}
=\frac{86909}{625}=139.0544<140.
}
\]
This is an analytic bound on the **entire operator action** over all physical frequencies, not a finite grid or truncated tail.

## 3. The original signed positive windows give a lower Rayleigh energy

SI14's exact all-frequency rational certification of three positive original signed windows, all with \(m>\kappa+1\), provides the strict original Fourier odd energy
\[
\boxed{
E:=\int_{J_1\cup J_2\cup J_3}|\widehat{Zs}|^2>
\frac{29396}{1000000}=0.029396.
}
\]
As \(a\ge\kappa\) everywhere and \(a\ge\kappa+1\) on these original signed windows,
\[
\boxed{
q:=\langle s,As\rangle
\ge\kappa\|s\|^2+E.
}
\]
Thus both the complete squared action \(\|As\|^2<140\) and the complete supported Rayleigh energy \(q\) are rigorously enclosed in the signs needed for the residual calculation.

## 4. First fully paid original supported residual and correct-sign inverse response

Let \(S=\|s\|^2\). For the actual \(y=\alpha s\), with \(\alpha=1/4800\),
\[
\begin{aligned}
\|R\|^2
&=\|s-\alpha As\|^2
=S-2\alpha q+\alpha^2\|As\|^2\\
&<(1-2\alpha\kappa)S-2\alpha E+140\alpha^2.
\end{aligned}
\]
SI11's **correct-sign positive residual identity** is
\[
\begin{aligned}
2\langle s,A^{-1}s\rangle
&=4\langle s,y\rangle-2\langle y,Ay\rangle
+2\langle R,A^{-1}R\rangle\\
&\le4\alpha S-2\alpha^2q+\frac2{\kappa}\|R\|^2.
\end{aligned}
\]
Inserting the complete residual bounds (and safely dropping only the *negative* \(-2\alpha^2q\)) gives
\[
\boxed{
2\langle s,A^{-1}s\rangle
<
\frac{2S}{\kappa}
-\underbrace{\left(\frac{4\alpha E}{\kappa}
-\frac{280\alpha^2}{\kappa}\right)}_{\displaystyle
=22219/1800000>0.0123}.
}
\]
The exact SI12 positive Taylor enclosure of \(\sinh B\) then yields the verified scalar upper
\[
\boxed{
2\langle s,A^{-1}s\rangle<471.283.
}
\]
The strict exact rational improvement relative to the scalar-only upper \(2S/\kappa\) is \(22219/1800000\).

### An important negative benchmark

**This is NOT numerically competitive with SI14.** SI14's positive-window supported comparison already gave
\[
2\langle s,A^{-1}s\rangle<412.562.
\]
SI15's \(471.283\) is a substantially **weaker** upper bound. What SI15 contributes is **the first legitimate original supported trial \(y\in\operatorname{Dom}A\) with its full residual \(s-Ay\) rigorously bounded**, not a superior odd-pole constant. It proves the SI11 inverse-response framework can be populated with *an actual operator-domain vector* while charging the full archimedean continuum and signed prime operator. It does not show the true inverse response is close to either bound.

## 5. SI16 target and decision

To improve the currently best SI14 scalar-chord inverse upper, **one-dimensional \(y=\alpha s\) with a global \(\kappa^{-1}\)-weighted residual is insufficient**, at least with the present conservative Fourier-envelope bound. The next useful route is to form an enriched odd trial span with support-adapted vectors and certify the *whole* residual matrix, or use a stronger positive odd residual comparator than \(\kappa I\) so that the full residual is not magnified by \(1000\).

A concrete SI16 candidate is a two-column odd supported span \(\operatorname{span}\{s,\;x(1-x^2/B^2)\}\), with the original \(A\)-action/cross-energy **and residual** computed with certified Fourier tails. An alternative is SI10's physically supported multiband modulated polynomials, restricted to odd parity and full original operator action. Compute actual conditioned rank/error versus RC334's much smaller native signed high-Schur program; stop if the SI global residual remains prohibitively costly.

No original signed full-form positivity, odd-pole BS threshold, complete SI11 finite eigenvalue, Stage I, F4, LF/Lean or RH closure is claimed.

## Replay

\`python scripts/validate_rpb108_si15_odd_full_residual.py\`

This verifier checks the rational analytic constants, exact dyadic infinite-tail sums, inherited signed original positive-window mass, complete residual formula and strict inverse margin. The operator domain/form identities rely on standard Fourier Plancherel and closed-form representation, not Lean formalization or independent peer review.
