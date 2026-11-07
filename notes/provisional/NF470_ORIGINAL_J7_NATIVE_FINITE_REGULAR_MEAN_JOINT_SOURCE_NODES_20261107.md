# Weil-Lab NF470 — Native original J7 regular mean and joint compact-source nodes

**2026-11-07. Standing: NEW EXECUTABLE NATIVE EVALUATOR, ORIGINAL COMPUTED INTERVALS PENDING CI.** This is a numerical *execution* pass, not another purely algebraic or derivative-only pass. Parent NF469 draft PR #497, [focused exact jet gate CI #42408129557](https://github.com/monocap-tech/weil-lab/actions/runs/42408129557) SUCCESS. Original NF407 source SHA256 \`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce\`; original NF406 physical seam SHA256 \`c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675\`. Canonical W-ODD-NEG OPEN.

## Repo custody and source branch dependency

The NF469 working branch does **not** contain the original NF459 native J8 evaluator. It would be incorrect to run an import or to claim that an unmerged source-native script exists on our own working tree. NF470 therefore uses a **two-checkout CI architecture**: the original NF459 full original-source native tree pinned to immutable Git SHA \`f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05\` (branch \`research/nf459-matched-points\`), plus the proposed additive NF470 script from the new PR head. No ancestral merge, rewritten source, or floating cross-branch dependency is assumed. The runner copies only the new NF470 script into the pinned native execution tree. The native input SHA checks re-establish source/seam custody. An upstream change to NF459 therefore cannot silently change the NF470 native reproduction.

## Two distinct original numerical tasks

**A. Genuine six-prime regular mean over original J7 macroscopic panel.** Original physical regular response from NF446/NF459:

\[
F_7(x)=-\sum_{n\in\{2,3,4,5,7,8\}}w_n[U(x-\log n)+v]
-C_{404}\sinh(x/2),\quad v=U(B),
\]
where weights are imported from the *original NF411* outward source receipt and \(C_{404}=6677356497477490213/4611686018427387904\). Over \(I=[26/25,53/50]\) length \(L=1/50\),

\[
\boxed{\bar F_7=-{1\over L}\sum_nw_n
\left(\int_{a-\log n}^{b-\log n}U(y)\,dy+Lv\right)
-{2C_{404}\over L}\bigl[\cosh(b/2)-\cosh(a/2)\bigr].}
\]

The implementation integrates every original 273 polynomial-frequency mode **exactly up to outward Arb arithmetic**. For \(\omega=2\pi f>0\),

\[
P_0(y)=(i\omega)^{-1},\qquad P_k(y)={y^k-kP_{k-1}(y)\over i\omega},\qquad
\int y^k e^{i\omega y}\,dy=e^{i\omega y}P_k(y).
\]

Original even-\(k\) sine and odd-\(k\) cosine projections use the original NF459 generator parity. The actual original sinh pole is integrated as \(2\cosh(y/2)\). Each original shift endpoint lies inside \([-B,B]\); **n=9 is correctly absent**. No invented data, quadrature mesh or discarded coefficient correlations. Source radius and original weight interval uncertainties are charged by \(100S_0+901\sum\delta w_n+10^{-60}\), with original \(S_0<10^{-700}\) and \(\sum\delta w_n<10^{-32}\). The program outputs the source-certified interval for \(\bar F_7\), *if CI completes*. This is **not** the complete \(\bar z\): the compact arch mean is still missing.

**B. Actual original complete source at two J7 rational points.** The runner evaluates the full original NF446 compact joint arch \(\mathcal J_U(x)\), full six-prime \(F_7(x)\), and true \(z(x)=\mathcal J_U(x)+F_7(x)\) at \(x=26/25\) (independent NF417/418 source-positive anchor check) and \(x=21/20\) (new macroscopic interior J7 node). This uses the old NF459 exact 1400-mode physical bulk Laplace-frequency recurrence and pole, with local \(tK(t)\) Taylor \(L=100\), terminal \(H\) and the same original source; it does **not** evaluate digamma and image families separately. Point signs must never be promoted to whole-panel signs.

## An improved analytic carrier, beyond the NF469 B-centered 4000-jet route

Instead of a 4000-term Taylor expansion about \(B\) and Horner translation, NF470 constructs the genuine original source's Taylor jet **directly about each J7 physical point**. With local cutoff \(t_0=1/8>2(B-26/25)=3/25\), every local source argument is within \(t_0/2=1/16\) of its own center. The inherited entire original source bound \(M_U=10^{800}\) on radius \(R=1/5\) remains valid because \(x+R\le1.26<1.3\) on J7. Thus

\[
q={t_0\over 2R}={5\over16},\quad
E_N\le10^{800}\,{(5/16)^N\over1-5/16}.
\]

At \(N=1800\), \(E_N<10^{-100}\). Unlike the NF469 B-centered ratio \(49/80\) requiring \(N=4000\), this **re-centering of the source itself** reduces the necessary jet length to 1800 while preserving all original 273 terms.

The actual local source remainder vanishes at least as \(t^N\), so its kernel integral with \(K(t)\sim1/t\) is finite. The \(L=100\) rational \(tK\) Taylor remainder bound \(8t_0^{100}/(1-t_0)<10^{-80}\) is charged. At \(t_0=1/8\) the original 1400-mode bulk source tail is \(<10^{-60}\), and the terminal 40-mode \(H(b)\) tail \(<10^{-59}\). Native interval arithmetic uses 4096 bits. A conservative \(10^{-26}+901\sum\delta w_n+10^8S_0\) charge covers full point source/truncation uncertainty.

**Important:** All of these bounds only become original-source computed enclosures after the new CI actually executes. They are not substituted numerical results.

## Status and next obligation

**Established:** a concrete, pinned cross-branch native executable to evaluate (i) the **actual original six-prime finite J7 mean** by exact source primitives and (ii) the **actual original complete joint physical J7 point responses** with rigorously paid local and bulk remainders. The source-centered 1800-jet error gate is strictly stronger for execution than the previous B-centered 4000-jet approach.

**Pending:** actual GitHub Actions replay, exact output intervals, any pointwise signed sign, and original NF417 overlap check at left panel anchor. A passing workflow must be inspected, and actual intervals must be copied to permanent source custody before numerical standing is promoted. **Still OPEN:** \(\int_I\mathcal J_U\), full \(\bar z\), covariance/variance, signed \(D_I\), complete J7/J8, NF404, W-ODD-NEG, RH.

**Next bold NF471:** audit original native CI and register the actual \(\bar F_7\), \(z(1.04)\), \(z(1.05)\) intervals; then build rigorous source-correlated integration of the joint compact arch \(\int_I\mathcal J_U\), not a mesh of unverified point samples. No main merge.
