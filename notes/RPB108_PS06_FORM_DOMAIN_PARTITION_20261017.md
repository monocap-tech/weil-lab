# PS06 — Energy-stable additive partition of the original Weil-form domain

**W-PHYSICAL-SHIFT**, independent scoped investigation, stacked after PS05; **canonical W-ODD-NEG remains OPEN**. This checkpoint repairs the *domain decomposition* issue that PS05 explicitly left unresolved by constructing a bounded, exact, additive partition on the original physical spectral form domain. It does **not** establish that the sharp characteristic-function projection preserves the form domain; it does **not** identify an unconstrained orthogonal edge/interior Schur decomposition or certify positivity of the full signed Weil form.

## 1. The exact original form and its graph norm

On \(I=[-B,B]\), \(B=11/10\), with zero extension \(Zf\), use the same original signed SI10/CC27 physical form as PS01–PS05:
\[
q[f]=c_{\rm arch}\|f\|_2^2+J[f]
-2\sum_{n\in N}w_n\operatorname{Re}C_f(\log n)
+2|\langle f,\cosh(x/2)\rangle|^2
-2|\langle f,\sinh(x/2)\rangle|^2 ,
\]
\[
J[f]=\int_0^\infty k(u)\|Zf-\tau_u Zf\|_2^2du,\qquad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}},\quad
c_{\rm arch}=-\gamma-\frac\pi2-3\log2-\log\pi,\quad
N=\{2,3,4,5,7,8,9\}.
\]
The original weights are \(w_n=\Lambda(n)/\sqrt n\), with exact square roots for \(n=4,9\). By Tonelli and the exact digamma identity of PS01, \(J\) is a nonnegative closed form on physical \(L^2(I)\). All other terms are \(L^2\)-bounded, so the original physically supported form domain is precisely
\[
\mathcal D=\{f\in L^2(I):J[f]<\infty\}.
\]
This identifies the *physical Fourier realization*. Attaching the result to the completed CC27 \(D\)-Riesz model still requires its separate original-operator/domain transfer proof.

By the correctly signed prime and pole bounds,
\[
J[f]-C_*\|f\|^2\le q[f]\le J[f]+C_*\|f\|^2,
\quad
C_*=-c_{\rm arch}+2\sum_{n\in N}w_n+4\sinh B<18.
\]
The pole allowance uses \(\|\cosh(x/2)\|_2^2+\|\sinh(x/2)\|_2^2=\int_{-B}^B\cosh x\,dx=2\sinh B\). All seven prime terms are included. Thus \(G[f]=q[f]+20\|f\|^2\) defines a positive closed graph norm with
\[
G[f]\ge J[f]+(20-C_*)\|f\|^2>J[f]+2\|f\|^2.
\]

## 2. Explicit smooth-enough exact additive edge/interior split

Set
\[
\ell=\log9,\quad a=\ell-B,\quad\delta=B-a=2B-\log9,\quad E=\{x\in I:|x|\ge a\}.
\]
Use a *globally Lipschitz*, real, even cutoff, not the discontinuous sharp projector:
\[
\chi(x)=
\begin{cases}
0,&|x|\le a+\delta/4,\\
\frac{2}{\delta}(|x|-a-\delta/4),&a+\delta/4<|x|<a+3\delta/4,\\
1,&|x|\ge a+3\delta/4.
\end{cases}
\qquad \psi=1-\chi.
\]
Their global Lipschitz constants are at most \(L=2/\delta\). Exact-rational source enclosures certify
\[
1/400<\delta<1/350,\qquad 700<L<800.
\]
For every \(f\in\mathcal D\),
\[
f=\chi f+\psi f,\quad
\operatorname{supp}(\chi f)\subset E,\quad
\operatorname{supp}(\psi f)\subset
F'=[-a-3\delta/4,a+3\delta/4].
\]
The pieces overlap on the two transition collars, by design. There is no false claim of orthogonality.

## 3. Fully explicit energy graph-norm preservation

For any \(0\le\theta\le1\) with global Lipschitz constant \(L\), including both \(\chi,\psi\),
\[
\|Z(\theta f)-\tau_uZ(\theta f)\|_2^2
\le2\|Zf-\tau_uZf\|_2^2
+2\min(Lu,1)^2\|f\|_2^2.
\]
The kernel is bounded using the exact elementary inequalities
\[
k(u)\le\frac1{2u}+1\quad(0<u\le1),\qquad
k(u)<2e^{-u/2}\quad(u\ge1).
\]
Split at \(u=1/L\) and \(u=1\):
\[
\begin{aligned}
I_L&=\int_0^\infty k(u)\min(Lu,1)^2du\\
&<\frac14+\frac1{3L}+\frac12\log L+1-\frac1L+4\\
&<\frac12\log800+\frac{21}4<9.
\end{aligned}
\]
The last bound is checked by *outward exact rational* log estimates, \(\log800=5\log2+2\log5\).

It follows that
\[
J[\theta f]\le2J[f]+2I_L\|f\|^2,
\]
and, **for the actual original signed form**,
\[
\begin{aligned}
G[\theta f]
&\le J[\theta f]+(20+C_*)\|\theta f\|^2\\
&\le2J[f]+(18+20+C_*)\|f\|^2\\
&<2G[f]+56\|f\|^2\\
&<30\,G[f],
\end{aligned}
\]
because \(G[f]>2\|f\|^2\). Thus
\[
\boxed{
G[\chi f]<30G[f],\quad G[\psi f]<30G[f],
\qquad
G[\chi f]+G[\psi f]<60G[f]
}
\]
for \(f\ne0\). These statements prove \(\chi,\psi:\mathcal D\to\mathcal D\) are bounded in the **same original signed form graph norm**. This is an actual domain theorem; no spectral cutoff or auxiliary operator substitution.

## 4. Exact constrained block representation, NOT orthogonal Schur elimination

Define the two separately admissible supported domains
\[
\mathcal D_E=\{v\in\mathcal D:\operatorname{supp}v\subset E\},
\quad
\mathcal D_{F'}=\{w\in\mathcal D:\operatorname{supp}w\subset F'\}.
\]
The bounded additive partition \(T:\mathcal D\to \mathcal D_E\oplus\mathcal D_{F'}\), \(Tf=(\chi f,\psi f)\), has exact range
\[
\boxed{
\operatorname{Ran}T
=\{(v,w)\in\mathcal D_E\oplus\mathcal D_{F'}:\psi v=\chi w\}.
}
\]
The inverse on this constrained range is \(T^{-1}(v,w)=v+w\). Indeed, \(\psi v=\chi w\) implies \(v=\chi(v+w)\), \(w=\psi(v+w)\). With the original Hermitian polarization \(b\),
\[
q[f]=q[v]+q[w]+2\operatorname{Re}b(v,w),
\qquad f=v+w,\quad\psi v=\chi w.
\]
This is a genuine *full-form-domain representation* but **not** a free orthogonal direct-sum block operator: the collars overlap, \(\langle v,w\rangle\) need not vanish, and \(b(v,w)\) includes the original scalar mass, digamma, all seven prime powers and both signed poles.

**Important:** PS04/PS05's disjoint-edge \(L^2\) operator \(B_{EF}\) and its compact \(B_{EF}^*A_E^{-1}B_{EF}\) cannot simply be inserted in place of this *overlap-constrained* \(b\). Such a substitution would omit collar terms and may be invalid even though both prior results remain correct on their stated domains.

## 5. What is now established and what remains

PS06 proves full **physical spectral-form-domain stability** of an exact additive edge/interior split with explicit universal bound. It avoids assuming characteristic-function multiplication is admissible.

PS07 must first derive the correct collar-compatible energy-dual block (or prove the sharper sharp-projector theorem independently), then build a genuinely quantitative finite-dimensional Schur approximation with the original signed cross terms. The complete CC27 D-Riesz identification is still a separate obligation. Neither full even nor odd positivity, finite 890-column gate, global RH synthesis, nor RH has closed.

Run \`python3 scripts/validate_rpb108_ps06_form_domain_partition.py\` for pinned original-source and exact-rational cutoff/graph-constant checks. This validator does not substitute for external proof review or Lean formalization.
