# PI028 — Three distinct first-prime Gamma cancellations: exact smooth counterexample to uniqueness

**Potential Interface / analytic-only.** Parent: research/pi027-prime-gamma-phase-cancellation-and-source-matrix. Registry: issue #792. No pull request, Lean module, workflow, Actions dispatch, IV/CP/NF mutation, or RH/positivity claim. This memo is a paper-level derivation from PI027's original signed Weil source formula, supplemented by an independent exact-rational support audit. It is not a new Lean theorem.

## 1. Main result

PI027's existence theorem for a zero of the original relative-phase amplitude
\[
\Theta_m(a)=B_m(a)-P_m(a)
\]
is **not a uniqueness theorem**. More strongly, there is one explicitly specified nonnegative smooth bump \(\rho\in C_c^\infty((0,d))\), \(d=\log(10/9)\), for which **every** PI027 annihilator order \(m\ge1\) has **at least three distinct zeros**, all inside the genuine \(n=3\) prime window. Each is a live cancellation \(P_m(a)=B_m(a)>0\), and the three zeros lie in narrow, disjoint, fully analytic brackets of width \(d/100\). No integration or numerical quadrature is required to locate these brackets.

This **refutes general uniqueness** over PI027's admissible class. It does NOT establish how many roots any particular single-lobed bump has, nor that any of these roots is simple/transversal.

## 2. One explicit smooth \(\rho\), all orders \(m\)

Put
\[
d=\log(10/9),\quad \ell=d/100,\quad \Delta=d/2,\quad x_0=d/5.
\]
Define the standard explicit flat bump
\[
b(x)=\begin{cases}
\exp[-1/(r(1-r))],&0<x<\ell,\ r=x/\ell,\\
0,&\text{otherwise}.
\end{cases}
\]
Set
\[
\boxed{\rho(x)=b(x-x_0)+b(x-x_0-\Delta).}
\]
It is nonnegative, nonzero and \(C_c^\infty((0,d))\): its two compact support intervals are
\([d/5,d/5+\ell]\) and \([7d/10,7d/10+\ell]\), strictly inside \((0,d)\).

Use PI027's **unchanged** operator and correlation:
\[
L_m=D\prod_{j=0}^{m-1}(D^2-(2j+1/2)^2),\qquad
\eta_m=L_m b,\qquad
\phi_m=L_m\rho,
\]
\[
Q_m(u)=\int_{\mathbb R}\eta_m(x)\eta_m(x-u)\,dx,\quad
C_m(u)=\int_{\mathbb R}\phi_m(x)\phi_m(x-u)\,dx,\quad
J_m=C_m(0)>0.
\]
The derivative operator commutes with translation, so
\[
\phi_m(x)=\eta_m(x-x_0)+\eta_m(x-x_0-\Delta),\qquad
\boxed{C_m(u)=2Q_m(u)+Q_m(u-\Delta)+Q_m(u+\Delta).}
\]
The compact support of \(Q_m\) lies in \([-\ell,\ell]\), and \(Q_m(\pm\ell)=0\). As \(\Delta>2\ell\), the three correlation channels are disjoint. Writing \(q_m=Q_m(0)=\|\eta_m\|_2^2>0\), we have **exactly**
\[
J_m=2q_m,\qquad
C_m(0)=J_m,\qquad C_m(\Delta)=q_m=J_m/2,
\]
\[
\boxed{C_m(\ell)=C_m(\Delta-\ell)=C_m(\Delta+\ell)=0.}
\]
These identities use only support geometry and translation, not the sign of \(Q_m\) away from its origin. The nonzero \(q_m\) follows because a compactly supported nonzero smooth \(b\) cannot be annihilated by the nonzero constant-coefficient differential operator \(L_m\).

The unchanged PI027 Laplace polynomial gives \(S_m(0)=S_m(\pm1/2)=0\), so both original poles vanish. At each separation \(a>d\), PI027's diagonal autocorrelation family and its contact-free difference \(D_a=h_{1,m,a}-h_{-1,m,a}\) remain genuine Schwartz tests, with
\[
W(h_{\beta,m,a})=W(C_m)+\Theta_m(a)\Re\beta,\qquad
W(D_a)=2\Theta_m(a).
\]

**Fixed original physical window:** if invoking IV's physical support cutoff \([-11/10,11/10]\), translate both constituent physical bumps together by \(-1/2\) before forming the autocorrelation. This leaves \(C_m,h_{\beta,m,a},D_a\) and all displayed values exactly unchanged. For the present \(a\in[\log3-d,\log3]\), the translated physical support stays strictly within \((-11/10,11/10)\). This does not place the bumps in IV's narrower old-collar positivity class.

## 3. Strict signed bounds through the full first-prime window

Parameterize the separation by \(t=\log3-a\), \(0\le t\le d\). The correlation support is inside \((-d,d)\). The rational facts
\[
\frac{3}{(10/9)^2}=\frac{243}{100}>2,
\qquad 3(10/9)=\frac{10}{3}<4
\]
show that throughout \(a\in[\log3-d,\log3]\), the **only** possible original von Mangoldt sample is \(n=3\). Thus, with \(\kappa_3=\log3/\sqrt3>1/3\),
\[
\boxed{P_m(\log3-t)=\kappa_3 C_m(t).}
\]
The true PI027 Gamma channel obeys \(B_m(a)>0\) for \(a>d\), and
\[
0<B_m(a)\le dK(a-d)J_m
<\frac19J_m \qquad
(\log3-d\le a\le\log3).
\]
Indeed \(a-d\ge\log(243/100)>\log2\), \(K\) is decreasing,
\(K(\log2)^2=8/9<1\), and \(d<1/9\). The strict bound is uniform in \(m\) and in the chosen nonnegative bump.

At the five **exact** control separations \(a(t)=\log3-t\):

| \(t\) | \(C_m(t)/J_m\) | Sign of \(\Theta_m(a(t))\) |
|:--|:--|:--|
| \(\Delta+\ell=51d/100\) | \(0\) | \(B_m>0\) |
| \(\Delta=d/2\) | \(1/2\) | \(<J_m/9-J_m/6=-J_m/18\) |
| \(\Delta-\ell=49d/100\) | \(0\) | \(B_m>0\) |
| \(\ell=d/100\) | \(0\) | \(B_m>0\) |
| \(0\) | \(1\) | \(<J_m/9-J_m/3=-2J_m/9\) |

Continuity now gives at least one zero in **each** of the following three nonoverlapping brackets:
\[
\boxed{\begin{aligned}
a_{\mathrm{sat},-}&\in
(\log3-51d/100,\ \log3-50d/100),\\
a_{\mathrm{sat},+}&\in
(\log3-50d/100,\ \log3-49d/100),\\
a_{\mathrm{central}}&\in
(\log3-d/100,\ \log3).
\end{aligned}}
\]
Each bracket has exact width \(d/100=\log(10/9)/100\), a **rigorously localized** interval for this explicit \(C_c^\infty\) test, not a numerical fit. There may be additional zeros.

At every one of these roots,
\[
B_m(a)=P_m(a)=\kappa_3 C_m(\log3-a)>0,\quad
W(D_a)=0,\quad W(h_{\beta,m,a})=W(C_m)
\]
for every unit phase \(\beta\). Thus the same fixed underlying \(\rho\) supports at least three separated, genuinely prime-active, exactly phase-flat realizations.

## 4. Transversality and perturbation: separate obligations

The actual derivative criterion is exact:
\[
B_m'(a)=-\sum_{n\ge m}(2n+1/2)A_{m,n}e^{-(2n+1/2)a}<0,
\quad A_{m,n}>0,
\]
\[
\boxed{\Theta_m'(a)=B_m'(a)+\kappa_3 C_m'(\log3-a).}
\]
A zero is transversal iff this quantity is nonzero. In particular, \(C_m'(\log3-a)\le0\) is a sufficient condition for \(\Theta_m'(a)<0\). **None** of the three sign-change arguments alone establishes transversality, uniqueness within its bracket, or a differentiable root branch.

There is nevertheless a genuine weaker stability theorem. The five strict endpoint signs are continuous under sufficiently small real \(C^{2m+1}\) perturbations of \(\rho\) with support held in a fixed compact subinterval of \((0,d)\); for the original nonnegative admissible family, the original Gamma positivity and source law persist. Therefore **at least three** roots in the same three open brackets persist for all sufficiently small admissible perturbations of this explicit \(\rho\). The three brackets do not establish individual root identity or smooth continuation. A transversality theorem would need strict derivative enclosures (or another genuine regular-value argument).

## 5. Exact original/CP/Masullo spectral interface

Let \(\Xi_m(z)=\int \eta_m(x)e^{izx}\,dx\) and \(\Phi_m(z)=\int \phi_m(x)e^{izx}\,dx\). Direct complex-source Fourier algebra (no RH) gives
\[
\Phi_m(z)=e^{izx_0}(1+e^{iz\Delta})\Xi_m(z),
\]
\[
\boxed{\widehat D_a(z)=2\cos(az)\,\Phi_m(z)\Phi_m(-z)
=2\cos(az)[2+2\cos(\Delta z)]\Xi_m(z)\Xi_m(-z).}
\]
At a zero \(\rho_\zeta=\sigma+i\gamma\) of zeta, the PI027 source Fourier argument is
\(z_{\rho_\zeta}=\gamma-i(\sigma-1/2)\). Equivalently CP001's centered Mellin argument is \(w_{\rho_\zeta}=\rho_\zeta-1/2\) with \(z_{\rho_\zeta}=-iw_{\rho_\zeta}\). The offcritical evaluation uses \(\cosh(a w_{\rho_\zeta})\), **not** a critical-line modulus square; full multiplicities and noncentral roots are retained.

CP001's conditional complete-zero Hermitian compression dictionary, if proved for these exact test functions with correct source scaling and an exhaustive zero tail, would require the complete centered zero functional on each \(D_a\) to equal \(W(D_a)=2[B_m(a)-P_m(a)]\), hence **zero at all three crossings**. This is a new adversarial test family for that dictionary, but CP001's frozen three-cell basis is a different test family: no numerical CP-C1 matrix result is being transferred here.

Independently, the *literal printed* Masullo Ch12/Ch13 comparison inherited from PI027 would, **if both distinct trace identities truly apply on the common radial contact-free domain with the stated canonical Haar/strip/cutoff dictionary**, require at each crossing:
\[
Z_{12}(D_a)=0,\qquad Z_{13,\mathrm{cap}}(D_a)=2B_m(a)>0.
\]
These are conditional required zero-side values, not computed spectral sums. Chapter13's accompanying proof text remains incomplete and its real-place normalization differs as printed. This memo neither proves nor refutes the author's intended corrected trace theorem.

## 6. Verification and next gate

The companion standalone \`scripts/pi028_three_crossing_support_exact.py\` uses only \`fractions.Fraction\` to check all five support controls, the exact n=3 isolation window, Gamma-envelope rational consequences, the three disjoint certified brackets and both rational negative margins. All smoothness, positivity of the Gamma mode sum, and IVT assertions are supplied by the mathematical derivation above, **not** claimed to be verified by executing rational code.

**PI028 result:** general uniqueness is false for original prime/Gamma cancellation, with an explicit fixed smooth \(\rho\) and three independently bracketed crossings for every \(m\ge1\). The next analytical task is to test transversality or bound root counts within individual brackets with validated derivative estimates for this exact bump, and to keep full complex spectral/comparison normalization distinct from phase-blind graph data. NF remains the sole compiler-active certification priority.