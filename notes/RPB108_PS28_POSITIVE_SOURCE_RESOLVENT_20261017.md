# PS28 — The original effective even pole is strictly positive: source resolvent positivity and a two-sided scalar bound

**W-PHYSICAL-SHIFT · October 17, 2026 · stacked after PS27.** Canonical **W-ODD-NEG**, **W-EVEN-FORM**, native **CC27 D-Riesz** domain/norm identification, complete original Weil positivity and **RH remain OPEN**. PS28 is not a finite matrix numerical evaluation of the source inverse. It proves an **infinite-dimensional positivity property of the true pole-free source resolvent** that determines the sign of the *whole effective pole vector*, supplies an explicit admissible even representative for the exact PS27 scalar variational gate, and gives a nontrivial exact-rational **two-sided** interval for the scalar source response. All conclusions refer to the original same zero-extended signed physical seven-prime form; the negative auxiliary form must not be confused with the original Weil form.

## 1. Recovered PS27 true original source-first pole factorization

Write \(I=[-B,B]\), \(B=11/10\), \(R=11/5\), \(c=\cosh(x/2)\), \(s=\sinh(x/2)\). Let \(P\) be PS15's exactly thirteen source intervals of width \(\delta=R-\log9\), \(C=1-P\). The complete *original* signed form is
\[
Q[f]=J[f]+c_{\rm arch}\|f\|^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\Re C_f(\log n)
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2,
\quad
J[f]=\int_0^\infty k(u)\|Zf-\tau_uZf\|^2\,du,
\]
where \(k(u)=e^{-u/2}/(1-e^{-2u})>0\), \(w_n=\Lambda(n)/\sqrt n>0\), and \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi<0\).

Define **the genuinely pole-free auxiliary** \(Q_0=Q-2|\langle c,f\rangle|^2\). Its original source operator \(A_0=A_P-2|c_P\rangle\langle c_P|\) obeys PS27's strict \(\boxed{A_0>1997/9000}\). The mixed source-to-complement operator \(B_0\) is the ACTUAL original \(Q_0\) cross including digamma, all seven nonperiodic prime shifts and the negative odd pole (the last vanishes on even vectors). The source-first positive-pole Schur identity is EXACT:
\[
\boxed{
\mathfrak S_C=\mathfrak S_C^{(0)}+\alpha|d\rangle\langle d|,\qquad
v=A_0^{-1}c_P,\quad
t=\langle c_P,v\rangle,\quad
d=c_C-B_0^*v,\quad
\alpha=\frac2{1+2t}.
}
\]
PS27 established \(0\le t<455/1997\), hence \(\alpha>3994/2907>1.37\). No step substitutes the *incorrect* post-Schur naive pole direction \(c_C\) for the effective original \(d\).

## 2. New INFINITE-DIMENSIONAL sign theorem: the original even pole-free source resolvent is positivity preserving

The physical source carrier \(P\) is invariant under reflection (\(r\leftrightarrow9/r\)). The even part of its pole-free auxiliary form has a particularly important structure.

For every complex **even** source-form-admissible \(p\), the pointwise modulus \(|p|\) remains even and form-admissible, and
\[
J[|p|]\le J[p]
\]
because \(\big||p(x)|-|p(x-u)|\big|^2\le|p(x)-p(x-u)|^2\) for each translated pair. For each of the **SEVEN original prime-power shifts**, \(w_n>0\) and
\[
\Re\,C_p(\log n)\le C_{|p|}(\log n).
\]
The pole-free scalar \(c_{\rm arch}\|p\|^2\) is unchanged by modulus, and the negative odd-pole term vanishes **exactly** on the even subspace since \(s\) is odd. Consequently
\[
\boxed{Q_0[|p|]\le Q_0[p]\quad(p\in\mathcal D_P,\ p\ \mathrm{even}).}
\]

The original source forcing \(c_P=P\cosh(x/2)\) is **even and nonnegative**. The strictly coercive source variational functional
\[
p\longmapsto Q_0[p]-2\Re\langle c_P,p\rangle
\]
has the unique minimizer \(v=A_0^{-1}c_P\) in the even source domain. Replacing any candidate minimizer by its modulus cannot increase the quadratic term or increase the linear penalty, as
\(\Re\langle c_P,p\rangle\le\langle c_P,|p|\rangle\). The minimizer therefore equals its modulus by uniqueness:
\[
\boxed{v=A_0^{-1}c_P\ge0\quad\text{a.e. on }P,\qquad v\text{ even}.}
\]
This is a true original **positivity-preserving resolvent** result, not an assumption about signs of a finite Galerkin matrix.

## 3. New INFINITE-DIMENSIONAL pointwise result: the effective pole exceeds the original \(\cosh\)

For every nonnegative even admissible \(h\) supported on the actual complementary \(C\), the **pre-pole original source/complement mixed operator** has a negative pairing with nonnegative even \(v\):
\[
\boxed{\Re\langle B_0h,v\rangle\le0.}
\]
This is because the mixed original archimedean kernel is **\(-k(|x-y|)\)** on disjoint supports, and each of the seven original signed prime shifts has a negative mixed coefficient \(-w_n\). The diagonal original \(c_{\rm arch}\|f\|^2\) has no disjoint-support cross; the positive even pole is removed by definition of \(Q_0\); and the original negative odd pole vanishes on even inputs. No other original coupling is silently dropped.

The original PS15 Carleman analysis proves \(B_0^*v\in L^2(C)\). Since the nonnegative even form-domain tests are dense in the nonnegative even \(L^2(C)\) cone, and \(B_0^*v\) is even, the mixed inequality forces
\[
\boxed{B_0^*v\le0\quad\text{a.e. on }C.}
\]
Thus the EXACT source-renormalized original positive pole is pointwise
\[
\boxed{
d=c_C-B_0^*v\ge c_C=\cosh(x/2)\ge1
\qquad\text{a.e. on }C.
}
\]
This proves rigorously what PS27 had left open: **\(d\ne0\)** and has a fixed nonnegative sign. Its source inverse response is not small or ignored; rather it **increases** the effective positive even pole pointwise, while the source minimization reduces the overall coefficient \(\alpha<2\).

The true thirteen-source intervals have total physical measure \(13\delta<13/350\), so
\[
|C|=R-13\delta>\frac{757}{350}.
\]
Consequently
\[
\boxed{\|d\|_{L^2(C)}^2>|C|>\frac{757}{350}\approx2.162857.}
\]

## 4. A CANONICAL admissible even representative for the scalar gate

Let \(u_0=R^{-1/2}\) be the original RC315 normalized constant mode and \(h_C=Cu_0\). The PS15 sharp projection theorem guarantees \(h_C\) belongs to the original even logarithmic form domain. From the preceding sign theorem,
\[
a_C=\langle d,h_C\rangle
\ge\frac{|C|}{\sqrt R}
>\frac{757/350}{\sqrt{11/5}}>0.
\]
Define the explicit **form-admissible** representative
\[
\boxed{
e=\frac{h_C}{\langle d,h_C\rangle},
\qquad \langle d,e\rangle=1,\quad
\|e\|_2^2<\frac{350}{757}<\frac12.
}
\]
No assumption that \(d\) itself belongs to the logarithmic form domain is made. This repairs the earlier tempting but unjustified choice \(e=d/\|d\|^2\), and fixes a canonical source-pinned test for PS29's coherent scalar infimum.

Set \(K_{\rm eff}=\{k\in\mathcal D_C:k\text{ even},\ \langle d,k\rangle=0\}\). The exact original even acceptance obligations are now **fully well-posed with a demonstrated nonzero admissible e**:
\[
\boxed{\mathfrak S_C^{(0)}[k]\ge0\quad(k\in K_{\rm eff})}
\]
and
\[
\boxed{
\inf_{k\in K_{\rm eff}}\big(\mathfrak S_C^{(0)}[e+k]+\alpha\big)\ge0.
}
\]
Both positivity inequalities are **OPEN**. The entire true original odd form remains \(\mathfrak S_C\vert_{\rm odd}=\mathfrak S_C^{(0)}\vert_{\rm odd}\), with the original negative odd pole retained, and its positivity is **OPEN**.

## 5. Nontrivial TWO-SIDED rational source scalar \(t\) bound without evaluating a huge inverse

To go beyond PS27's one-sided bound \(t<455/1997\), use the TRUE source variational identity
\[
t=\langle c_P,A_0^{-1}c_P\rangle
=\sup_{0\ne p\in\mathcal D_P}
\frac{|\langle c_P,p\rangle|^2}{Q_0[p]}.
\]
Choose the actual original source trial \(p=c_P\), which is even, nonnegative, and logarithmic-form admissible:
\[
t\ge\frac{\|c_P\|_2^4}{Q_0[c_P]}.
\]
Since the pole-free \(Q_0[c_P]\) has \(c_{\rm arch}<0\), all original prime correlations nonnegative (and their coefficients \(-w_n<0\)), and vanishing odd pole,
\[
0<Q_0[c_P]\le J[c_P].
\]

We certify a global elementary original-kernel upper on \(J[c_P]\) using actual physical source interval geometry. The original \(c_P\) has \(26\) source endpoint jumps, \(\sup|c_P|<7/6\), derivative \(|c'|<7/24\) inside P, and
\[
\mathrm{TV}(c_P)
\le26\frac76+13\delta\frac7{24}<31.
\]
For \(D_{c_P}(u)=\|Zc_P-\tau_u Zc_P\|^2\), BV translation and Cauchy give
\[
D_{c_P}(u)\le2\|c_P\|_\infty\,u\,\mathrm{TV}(c_P)
<\frac{217}{3}u,
\quad
D_{c_P}(u)\le4\|c_P\|_2^2<4\frac{91}{1800}.
\]
The same original \(k(u)\) satisfies \(k(u)\le1/(2u)+1\) for \(0<u\le1\), and \(k(u)<(7/6)e^{-u/2}\) for \(u\ge1\), by \(e^2>7\). Split the actual integral at \(\delta\in(1/400,1/350)\) and \(1\). The rational enclosure \(\log(400)<6\) yields the explicit all-rational upper
\[
\begin{aligned}
J[c_P]
&<\frac{217}{3}\left(\frac1{700}+\frac1{2(350)^2}\right)
+4\frac{91}{1800}(3+1)
+4\frac{91}{1800}\frac73\\
&<1.385<\frac32.
\end{aligned}
\]
Also \(\|c_P\|_2^2\ge|P|=13\delta>13/400\). It follows strictly that
\[
\boxed{
\frac{169}{240000}
<t=\langle c_P,A_0^{-1}c_P\rangle
<\frac{455}{1997}.
}
\]
**Both endpoints are genuine original-source rational certificates.** These bound the scalar response but do NOT numerically evaluate \(A_0^{-1}c_P\) or the effective pole function \(d\).

Monotonicity of \(\alpha=2/(1+2t)\) gives
\[
\boxed{
\frac{3994}{2907}<\alpha<
\frac{240000}{120169}
\quad
(1.373925\ldots<\alpha<1.997187\ldots).
}
\]
The positivity of \(d\) also gives a coherent correction on the original restricted constant \(h_C\):
\[
\boxed{
\alpha|\langle d,h_C\rangle|^2>
\frac{3994}{2907}\frac{(757/350)^2}{11/5}
>2.9.
}
\]
This **is not a positivity certificate** for the original \(\mathfrak S_C[h_C]\): PS27 only provided an **upper** negative bound on its auxiliary pole-free part \(\mathfrak S_C^{(0)}[h_C]<-4.35974\), not a compensating lower bound. No sign for their sum may be inferred.

## 6. Consequence and remaining proof dependency

PS26 identified the necessity of retaining the global even pole; PS27 proved its exact source-renormalized vector structure; **PS28 now proves the effective direction is nonnegative and pointwise at least the original \(c_C\)**, explicitly constructs a form-admissible scalar-section vector, and provides a two-sided source-resolvent scalar interval. This is a positive structural fact of the original source coupling, not a numerical eigenvalue pass.

**PS29 next:** use the positivity-preserving source resolvent and canonical \(e\) to analyze the actual signed \(\mathfrak S_C^{(0)}\vert_{K_{\rm eff}}\) and its one coherent even scalar minimization. At the same time, investigate the original **odd** Schur sign separately, retaining the negative odd pole. A rigorous one-negative-index bound for the even auxiliary form plus the coherent scalar gate would materially advance the entire original signed positivity obligation. The exact CC27 D-Riesz native norm/domain bridge and independent analytic audit are still mandatory.

**No full original signed Weil positivity, W-ODD-NEG, W-EVEN-FORM, CC27 carrier transfer or RH claimed.**

Replay: \`python3 scripts/validate_rpb108_ps28_positive_source_resolvent.py\` replays PS27→PS26→...→source-pinned RC315, checks all physical source, TV/digamma/log-rational inequalities and the derived exact two-sided \(t,\alpha\) bounds, the physical complement mass and admissible even representative controls, and fail-closed original canonical open governance. The proof of positivity preservation and mixed nonpositivity is analytical at the true operator/form level; passing CI checks the finite rational inequalities and inherited source, **not an independent machine formalization of infinite-dimensional cone preservation**.
