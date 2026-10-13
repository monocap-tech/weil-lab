# RPB108: finite Legendre coercivity to whole-carrier complement bridge

Base: research \`108185ee573a891706f0c9edf9fa19186bde7437\`.

## Result

The certified Legendre trial-space coercivity can be connected lawfully to a whole-carrier positivity theorem, provided one also controls the physical leakage of the moment-null complement and one finite squared-logarithmic norm on the trial space.

This is a genuine finite-to-global bridge for the **same physical Legendre span** already used by the rational certificates. It does not identify finite-span positivity with whole-domain positivity.

Let
\[
H=D_a,\qquad
\|h\|_H^2=\int_{\mathbb R}w(\xi)|\widehat h(\xi)|^2\,d\xi,
\qquad w(\xi)=\log(e+|\xi|),
\]
and write the actual native form as
\[
Q(h,k)=\langle h,k\rangle_H+\langle Jh,C_aJk\rangle_{L^2},
\qquad \|C_a\|\le c.
\tag{1}
\]
Here \(J:H\to L^2([-a,a])\) is the unchanged physical inclusion.

For \(m\ge1\), let
\[
E_m=\operatorname{span}\{P_j(x/a)\mathbf 1_{[-a,a]}:0\le j<m\}
\]
and
\[
F_m=\left\{f\in H:\int_{-a}^a x^j f(x)\,dx=0,\ 0\le j<m\right\}.
\]
Because the Legendre polynomials span the ordinary polynomials of degree \(<m\), \(F_m\) is exactly the physical \(L^2\)-orthogonal complement of \(E_m\) inside \(H\). Thus every \(h\in H\) has a unique physical orthogonal decomposition
\[
h=e+f,\qquad e\in E_m,\quad f\in F_m.
\tag{2}
\]

Define the finite squared-log constant
\[
d_m:=\sup_{0\ne e\in E_m}
\frac{\|\,w\widehat e\,\|_2}{\|e\|_2}<\infty.
\tag{3}
\]
It is a finite-dimensional generalized Gram norm and can be rigorously enclosed independently.

For \(T>0\), define
\[
\eta_{m,T}:=
\frac1{\sqrt{\log(e+T)}}+
\sqrt{4aT}\,e^{2\pi aT}\frac{(2\pi aT)^m}{m!}.
\tag{4}
\]

If the finite actual restriction satisfies
\[
Q(e,e)\ge\tau\|e\|_2^2\qquad(e\in E_m),\qquad \tau>0,
\tag{5}
\]
and for some \(T\)
\[
\boxed{
\tau\bigl(1-c\eta_{m,T}^2\bigr)
>
(d_m+c)^2\eta_{m,T}^2,
}
\tag{6}
\]
then the actual native form is strictly positive on the entire logarithmic carrier \(D_a\).

Equivalently, a sufficient scalar condition is
\[
\boxed{
\eta_{m,T}^2<
\frac{\tau}{c\tau+(d_m+c)^2}.
}
\tag{7}
\]

Thus the finite Legendre program has a precise lawful route to whole-carrier positivity: certify \(\tau\), certify \(d_m\), and make the moment-complement leakage \(\eta_{m,T}\) small enough. No dense-exhaustion limit or uncontrolled complement is left implicit.

## Moment-complement leakage

Take \(f\in F_m\). Its first \(m\) physical moments vanish, so for \(|\xi|\le T\),
\[
\widehat f(\xi)
=
\int_{-a}^a f(x)\left[
e^{-2\pi ix\xi}
-\sum_{j=0}^{m-1}\frac{(-2\pi ix\xi)^j}{j!}
\right]dx.
\]
The exponential remainder gives
\[
\left|
e^{-2\pi ix\xi}
-\sum_{j=0}^{m-1}\frac{(-2\pi ix\xi)^j}{j!}
\right|
\le
e^{2\pi aT}\frac{(2\pi aT)^m}{m!}.
\]
The Hilbert--Schmidt bound on the rectangle
\([-a,a]\times[-T,T]\) therefore yields
\[
\|\mathbf 1_{|\xi|\le T}\widehat f\|_2
\le
\sqrt{4aT}\,e^{2\pi aT}
\frac{(2\pi aT)^m}{m!}\,\|f\|_2.
\tag{8}
\]
Since \(w\ge1\), \(\|f\|_2\le\|f\|_H\). On the high-frequency region,
\[
\|\mathbf 1_{|\xi|>T}\widehat f\|_2
\le
\frac{\|f\|_H}{\sqrt{\log(e+T)}}.
\tag{9}
\]
Combining (8)--(9) proves
\[
\boxed{\|f\|_2\le\eta_{m,T}\|f\|_H.}
\tag{10}
\]

## Mixed-form control

Write
\[
x=\|e\|_2,\qquad y=\|f\|_H,\qquad \eta=\eta_{m,T}.
\]
By (10) and (1),
\[
Q(f,f)
\ge
(1-c\eta^2)y^2.
\tag{11}
\]

The identity part of the mixed term does **not** vanish under the physical \(L^2\)-orthogonal splitting. Instead,
\[
|\langle e,f\rangle_H|
\le
\|w\widehat e\|_2\|f\|_2
\le
d_m\eta\,xy.
\tag{12}
\]
Also
\[
|\langle e,C_af\rangle|
\le
c\eta\,xy.
\tag{13}
\]
Hence
\[
|Q(e,f)|\le(d_m+c)\eta\,xy.
\tag{14}
\]

Using (5), (11) and Hermitian polarization,
\[
Q(e+f,e+f)
\ge
\tau x^2
-2(d_m+c)\eta xy
+(1-c\eta^2)y^2.
\tag{15}
\]
The scalar \(2\times2\) Hermitian form in (15) is positive definite when
\[
\tau(1-c\eta^2)-(d_m+c)^2\eta^2>0,
\]
proving the whole-carrier claim.

## Consequence for the current eight-vector certificate

At \(a=1/2\), the current rational certificate gives \(m=8\) and
\[
\tau=\frac1{200000}.
\]
The existing coarse actual correction bound gives
\[
c\le 10+6\sqrt e<22.
\]

The determinant condition therefore requires very small complement leakage; in particular a practical sufficient implementation must drive \(\eta_{8,T}\) below the \(10^{-4}\) scale once a rigorous upper enclosure for \(d_8\) is included.

The present \(m=8\) leakage envelope cannot reach that scale. If its first term were below \(10^{-4}\), then
\[
\log(e+T)>10^8,
\]
so \(T>1\). But for \(a=1/2,m=8,T>1\), the second term in (4) already exceeds one:
\[
\sqrt{2T}\,e^{\pi T}\frac{(\pi T)^8}{8!}
>
e^3\frac{3^8}{8!}>1.
\]
Thus **the current coarse moment-leakage bound cannot upgrade the existing eight-vector certificate to whole-domain positivity**. This is a limitation of this envelope, not evidence that the actual complement is large or that \(Q\) is nonpositive.

## What is closed and what remains

Closed here:

1. a lawful direct-sum bridge from finite physical Legendre coercivity to full actual positivity;
2. an explicit complement leakage estimate using the Legendre moment cancellation itself;
3. the exact mixed identity-term correction that must be paid;
4. a proof that the present degree-seven/eight-vector certificate cannot close the whole carrier through this coarse leakage envelope.

Still open:

- a high-degree rational finite coercivity certificate \(\tau_m>0\);
- a rigorous upper enclosure for \(d_m\);
- a pair \((m,T)\) satisfying (6), or an actual finite negative certificate instead;
- endpoint exclusion/global RPB closure.

This is not another carrier retyping. It is the quantitative interface between the exact finite physical certificates and the whole logarithmic carrier.

## Validation and cursor

Analytic proof from the current actual form decomposition, physical Legendre moment cancellation, Plancherel, the logarithmic norm and elementary exponential remainder. No new external input or numerical sign is used. No actual endpoint, global positivity, RH conclusion, Lean source/workflow change or CI claim.

Certified Lean code remains at the prior project checkpoint; this record is not a new Lean formalization.

**Cursor:** the next useful computation is not another fixed \(m=8\) aperture check. It is a degree-growing certified Legendre program that tracks \((\tau_m,d_m)\) together with the rigorous moment-complement leakage (4), searching directly for the whole-carrier determinant margin in (6), or for a certified negative finite block.
