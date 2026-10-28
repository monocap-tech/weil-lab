# Weil-Lab NF361 — Four-mode near-critical transfer stops the NF360 scalar 242-source gate

**Custody:** read-only local mathematical audit. Original `W-ODD-NEG` remains OPEN; RH remains OPEN. No GitHub write, native Arb computation, fresh 242-dimensional inversion, or change of the selected source space. The sharpened exterior floor from NF356 is a locally replayed conditional result, **not** a native repository CI certificate. Original signed-form/operator realization is inherited and independently open.

**Source chain:**
- PR #348, source `8217c8c97520c37f7b1889da340ac13b7cff0594`, successful GitHub run `40516665209`, artifact `12738593751`, original `original_four_mode_critical_block.json`; SHA256 of downloaded ZIP `735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968` and JSON `a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922`.
- PR #350 retained `original_BS_pruned_rank_bound.json`; downloaded ZIP SHA256 `3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09`, JSON SHA256 `9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2`.
- Prior local NF356 and NF360 rational exterior-floor reports, not independently accepted as a repository native certificate.

## 1. Abstract transfer lemma, no inverse response computation

Let \(A=A_*\) be selfadjoint with \(A\ge\kappa I>0\), let \(K=K_-\ge0\) be bounded, and \(W=A-K\). Let \(J\subset H\) be a finite-dimensional physical space, \(F=J^\perp\), \(E=A^{-1}J\). Assume the supported closed-form realization and

\[
 0\le k(v,v)\le\varepsilon\|v\|^2,
 \qquad w(v,v)\ge\mu\|v\|^2, \quad v\in F\cap D(a),
\]
where \(\varepsilon,\mu>0\). The finite-dimensional map \(P_JA^{-1}|_J\) is strictly positive and invertible, so every \(f\in D(a)\) has a unique \(A\)-form-orthogonal splitting \(f=e+v\), \(e\in E\), \(v\in F\cap D(a)\): \(a(e,v)=0\). This is **not** physical orthogonality.

On \(F\), \(a(v,v)=w(v,v)+k(v,v)\ge\mu\|v\|^2+k(v,v)\). Hence
\[
 \frac{k(v,v)}{a(v,v)} \le \frac{\varepsilon}{\mu+\varepsilon}=:r.
\]
For nonzero \(e\), write \(t(e)=k(e,e)/a(e,e)\). By positive-semidefinite Cauchy–Schwarz for \(k\), then ordinary Cauchy–Schwarz in \(\mathbb R^2\),
\[
\begin{aligned}
 k(f,f)&\le \bigl(\sqrt{k(e,e)}+\sqrt{k(v,v)}\bigr)^2\\
 &\le\bigl(\sqrt{t(e)a(e,e)}+\sqrt{r a(v,v)}\bigr)^2\\
 &\le (t(e)+r)\,[a(e,e)+a(v,v)]
 =(t(e)+r)a(f,f).
\end{aligned}
\]

**Lemma (near-critical rank transfer).** Suppose an \(n\)-dimensional actual form-domain plane \(L\subset D(a)\) obeys
\[k(f,f)\ge(1-\eta)a(f,f)\quad(0\ne f\in L),\qquad 1-\eta>r.\]
The \(A\)-energy projection \(L\to E\) is injective: if \(e=0\), the quotient is at most \(r\), contradicting the lower bound. Its image \(L_E\subset E\) has dimension \(n\), and every nonzero \(e\in L_E\) satisfies
\[
 \frac{k(e,e)}{a(e,e)}\ge 1-\eta-r
 =\frac{\mu}{\mu+\varepsilon}-\eta.
\]
By finite-dimensional min–max, the \(n\)-th largest generalized eigenvalue of
\[
 \mathsf G(h,k)=\langle h,A^{-1}k\rangle,\quad
 \mathsf N(h,k)=\langle A^{-1}h,K A^{-1}k\rangle \quad(h,k\in J)
\]
obeys
\[
 \boxed{\lambda_n(\mathsf N,\mathsf G)\ge\frac{\mu}{\mu+\varepsilon}-\eta.}
\]
This is a lower bound on the **actual proposed finite inverse-response pair**, without evaluating it; the critical physical plane itself is **not** asserted to lie in \(E\) or \(J\).

## 2. Exact inputs and contradiction

PR #348 certifies on a four-dimensional actual original plane \(L\): \(\|W|_L\|\le\sigma\|c\|^2\), physical Gram \(\ge0.99I\), and inherited \(A\ge33621/10^9\). Thus \(k(f,f)\ge(1-\eta)a(f,f)\) on **every** nonzero vector in that plane, with rational
\[
 \eta=\frac{\sigma}{(33621/10^9)(99/100)}
 = 2.9552733316649424\ldots\times10^{-12}<3\times10^{-12}.
\]
PR #350 certifies the unchanged 242-dimensional selected-space complement leakage
\[
 \varepsilon=1.6767873157142093\ldots\times10^{-5}.
\]
Use the local NF356 floor \(\mu=0.009981124873103065\ldots\) provisionally. Exact-rational recomposition gives
\[
 r=0.0016771407318221386\ldots,\qquad
 \theta_*:=1-r=0.9983228592681779\ldots.
\]
The lemma, with \(n=4\), forces
\[
 \boxed{\lambda_4(\mathsf N_{242},\mathsf G_{242})
 \ge\theta_*-\eta\approx0.9983228592652226.}
\]
But NF360's proposed strict, convenient sufficient gate was \(\mathsf N_{242}\preceq(12479/12500)\mathsf G_{242}\), i.e. every generalized eigenvalue \(\le0.99832\). The fourth **alone** exceeds that by an exact-rational positive margin
\[
 \boxed{\theta_*-\eta-0.99832
 \approx2.8592652225880951\times10^{-6}>0.}
\]
Equivalently, the same fixed `0.99832` gate is impossible for **any** exterior floor \(\mu>0.009964109023651378\ldots\) with the retained \(arepsilon\), because then \(\mu/(\mu+arepsilon)>0.99832+\eta\). The locally reproduced floor exceeds this threshold.

Therefore the proposed NF360 scalar gate is **mathematically impossible under its own new-floor premise**, and no original 242-dimensional inverse solve should be launched to test it. This disproves that *sufficient method*, **not** original Weil positivity.

Equivalent one-line contradiction: the proposed gate would force
\[
 w(f,f)\ge(1-0.99832-r)\,a(f,f)
 \approx2.859268178\times10^{-6}\,a(f,f)
\]
for every vector in the entire odd form domain. The already certified four-plane has \(w(f,f)/a(f,f)\le\eta\approx2.9553\times10^{-12}\). Contradiction.

## 3. Independent of the unaccepted improved floor

The rank-transfer lemma does **not** require NF356. Substituting the inherited, repository-certified \(\mu_{\rm old}=0.001-\varepsilon\) gives \(\theta_{*,\rm old}=1-\varepsilon/0.001\approx0.9832321268428579\) and the conditional original-realization result
\[
 \lambda_4(\mathsf N_{242},\mathsf G_{242})
 \ge\theta_{*,\rm old}-\eta\approx0.9832321268399027.
\]
The local stronger floor moves the numerical threshold, not the structural saturation. For **any** feasible scalar method of this form, its sufficient threshold must be within \(\eta\) of \(\theta_*=\mu/(\mu+\varepsilon)\); the existing near-null modes forbid a larger *uniform positive A-energy reserve*. The actual full operator may still be positive with a tiny or zero minimum.

## 4. Frontier decision

STOP the NF360 `N242 <= 0.99832 G242` scalar sufficient test. **Do not** schedule a 242-dimensional positive-resolvent campaign for this threshold, add source dimensions, escalate precision on a false inequality, or identify energy-dual \(E\) with physical \(J\).

If remaining on `W-ODD-NEG`, the next justified investigation is a **matched, directional** infinite Schur comparison that retains the actual mixed-coupling operator (or an equivalent exact BS/Feshbach correction), rather than its sharp but overpaying scalar Cauchy replacement. In particular, a sufficient scalar bound with a predetermined reserve \(2.86\times10^{-6}\) is incompatible with the near-critical four-plane. An exact eigenvalue comparison at the true tiny reserve is a different, extremely demanding task and must not be presumed achievable.

**Validation:** `/mnt/data/nf361_critical_transfer_no_go.py` hashes the archived native #348 and pruned #350 evidence, verifies the rational \(\eta\), verifies the NF360 retained \(\varepsilon\), recomposes \(r,\theta_*,\theta_0\), and proves the exact positive contradiction margin with `fractions.Fraction`. This arithmetic replay is not an independent formal proof of the functional-analytic rank-transfer lemma; that lemma is proven in Section 1. No GitHub changes.
