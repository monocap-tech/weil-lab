# NF494 — Original full J8 analytic H400 construction and true whole-square source integration

**November 10, 2026 PT. Stacked research draft [PR #522](https://github.com/monocap-tech/weil-lab/pull/522), based on NF493 #521.** The first 4096-bit original full NF446 joint-compact analytic \(H\) source computation has **SUCCESS** [GitHub CI #42850200418](https://github.com/monocap-tech/weil-lab/actions/runs/42850200418), original native source artifact #13781650172. The independently computed real source \(H(0)\) overlaps source-accepted NF450 \(z(B)\), and the 400-jet \(H(1/500)\) matches independently accepted NF492 true physical \(H(1/500)\). **The full original physical squared energy and NF404 verdict require a SECOND, independent original-source Fraction integral audit.** Its actual signed result is NOT presumed here; only a successful focused complete replay may promote it. No main merge.

## Why NF494 can calculate 400 real H jets without an 18000-image Gram

Original fixed \(J_8\) source:
\[
B=\frac{11}{10},\quad d=B-x,\quad 0\le d\le\delta=\frac1{500},
\quad a=2d,\quad b=4B-2d,\quad T=4B=\frac{22}{5},
\quad K(t)=\frac{e^{-t/4}}{1-e^{-t}},\quad Q(t)=K(t)-\frac1t.
\]
The source \(U\) is the **unchanged original NF407** 242 selected+four critical 4096-bit Arb dyadics, all 273 authentic frequency/order modes, 32 critical sine carriers and genuine odd sinh \(m=0\) pole. The \(J_8\) original NF406 physical regular minus terms are all seven \(n=2,3,4,5,7,8,9\), with \(c_n=\Lambda(n)/\sqrt n\) and \(v=U(B)\), plus the original NF404 centered sinh term.

NF492 already source-accepted the **exact, complete, fully matched original physical endpoint identity**
\[
\boxed{z(B-d)=H(d)+g(d)\log(B/d),\quad
g(d)=\frac{U(B-d)-U(B)}2,\qquad
w(B-d)=p+z=H(d)+vC_8+\frac{U(B-d)}2\log(B/d).}
\]
Here \(H\) is holomorphic around \(d=0\) on the fixed n9-active branch with certified complex radius \(R=1/25\). The analytic whole-square 400-jet truncation error is <\(10^{-96}\); this is an **analytic remainder** and not by itself a finite native numerical coefficient certificate.

The original NF446 expression for \(H\) has two moving compact-source integrals. They can be transformed *exactly* into ONE fixed linear operator plus two **short moving edge corrections** without ever squaring a component:
\[
\begin{aligned}
F(d)&=\frac12\int_0^T K(t)[U(B-d)-U(B-d-t/2)]\,dt,\\
L(d)&=\frac12\int_0^{2d}K(t)[U(B-d)-U(B-d+t/2)]\,dt,\\
R_+(d)&=\frac12\int_{T-2d}^{T}K(t)[U(B-d)+U(B-d-t/2)]\,dt.
\end{aligned}
\]
Put \(Q_0=\int_0^TQ(t)dt\),
\(Q_s(d)=\int_0^{2d}Q(t)dt\),
\(Q_t(d)=\int_{T-2d}^TQ(t)dt\),
and \(T_K(T)=\int_T^\infty K(t)dt\). Then the genuine complete analytic remainder is the **exact identity**
\[
\boxed{\begin{aligned}
H(d)= {}&C_*U(B-d)+F(d)+L(d)+R_+(d)\\
&+\frac{U(B-d)}2\left[
\log\left(1-\frac{d}{2B}\right)-Q_s(d)-Q_t(d)
\right]\\
&-\sum_{n\in\{2,3,4,5,7,8,9\}}
c_n[U(B-d-\log n)+v]
-C_{\rm NF404}\sinh((B-d)/2),
\end{aligned}}
\]
where
\[
\boxed{
C_*=\frac{\psi(1/4)+\psi(1)-2\log\pi+\log(2/T)+T_K(T)}2.
}
\]
The constant follows from the exact original kernel identity
\[
Q_0=\psi(1)-\psi(1/4)-\log T-T_K(T).
\]
The temporary \(U(B-d-t/2)\) used by the fixed \(F\) and \(R_+\) can be the entire analytic continuation just beyond \(-B\), **but their difference is the original NF446 physical compact expression, with all real \(U\) arguments back inside \([-B,B]\)**. Neither temporary term is a new physical observation or an independently squared analytic-continuation shadow.

## Finite 273-mode source multiplier: digamma/polygamma, not numerical quadrature

For an authentic complex original source generator \(y^k e^{i\omega y}\) and \(s=i\omega/2\), define the **finite** original same-source compact aperture moments
\[
J_0(s)=\int_0^T K(t)(1-e^{-s t})dt,\quad
J_j(s)=\int_0^T t^jK(t)e^{-s t}dt,\quad1\le j\le k\le13.
\]
They are source-independently represented by
\[
\begin{aligned}
J_0(s)
&=\psi(1/4+s)-\psi(1/4)
-\sum_{m\ge0}\left(\frac{e^{-(m+1/4)T}}{m+1/4}
-\frac{e^{-(m+1/4+s)T}}{m+1/4+s}\right),\\
J_j(s)
&=(-1)^{j+1}\psi^{(j)}(1/4+s)
-\sum_{m\ge0}\int_T^\infty t^j e^{-(m+1/4+s)t}dt.
\end{aligned}
\]
Each remaining tail integral has the explicit original source-free recursion
\[
I_0(r)=\frac{e^{-rT}}r,\qquad
I_j(r)=\frac{T^j e^{-rT}+jI_{j-1}(r)}r.
\]
Therefore the fixed compact operator maps the **same original finite polynomial×oscillator span to itself**:
\[
\boxed{
F[y^ke^{i\omega y}](x)
=\frac{e^{i\omega x}}2
\left[
x^kJ_0(s)-
\sum_{j=1}^k\binom kj x^{k-j}
\left(-\frac12\right)^j J_j(s)
\right].
}
\]
Only **14 moments per original frequency** are required, not 400 independent physical integrations. The real sine/cos source amplitudes are combined across all 273 grouped original generators BEFORE producing each of the 400 Taylor coefficients.

For the original genuine \(\sinh(y/2)\) carrier, the \(s=-1/4\) term has an \(m=0\) **zero rate**; it is never evaluated via invalid \(\psi(0)\). NF494 computes its exact removable rate-zero finite contribution \(T\), and an ordinary convergent \(m\ge1\) digamma/corrected tail. This preserves the original special pole.

The source native fixed-window Laplace corrections are summed through \(m=999\). The remaining real tail over \(t\ge T\) has a strict source-independent geometric control from \(e>8/3\), hence \(e^{-t}<(3/8)^4\) for \(t\ge4\). The original complex whole-source input/growth envelope allows a deliberately conservative \(|F_{\ge1000}(d)|<10^{-1200}\) throughout \(|d|\le1/25\) after the accepted original polynomial oscillator growth over \(t\ge T\). All 4096-bit native midpoint/radius uncertainty remains explicitly included.

## Both genuine moving physical cutoffs: fully exact beta/harmonic recurrences

Write \(U(B-d)=\sum_{j\ge0}u_j d^j\). The original \(L(t)=tK(t)=\sum_{k\ge0}\ell_kt^k\), \(\ell_0=1\), \(\ell_1=1/4\). The upper kernel coefficients at \(T\) are \(\kappa_k\) from
\[
K(T-u)=\sum_{k\ge0}\kappa_k u^k,\qquad
\kappa_k=\frac1{k!}\sum_{m\ge0}(m+\tfrac14)^k e^{-(m+1/4)T}.
\]

The complete original short-left moving correction is
\[
\boxed{
[d^n]L(d)=\frac12\sum_{j=1}^n
u_j\ell_{n-j}2^{n-j}\,
\mathcal B(j,n-j),
}
\]
where \(\mathcal B(j,0)=\sum_{r=1}^j1/r\), and for \(k\ge1\),
\[
\mathcal B(j,k)=\frac1k-\frac{(k-1)!\,j!}{(k+j)!}.
\]
The right original **odd-source-supported** moving endpoint has exact coefficients
\[
\boxed{
[d^n]R_+(d)=\sum_{j+k=n-1}
u_j\kappa_k2^k\left[
\frac1{k+1}-(-1)^j\frac{k!\,j!}{(j+k+1)!}
\right].
}
\]
The scalar \(\int_0^{2d}Q\), \(\int_{T-2d}^{T}Q\) and \(\log(1-d/(2B))\) are analytic with their **exact Taylor coefficients** derived from \(\ell_j,\kappa_j\). All seven genuine \(U(B-d-\log n)\) translations are expanded at their exact original 4096-bit source locations and subtracted with *true* interval weights \(\log p/\sqrt n\), checked against NF411 original rational c_n outward balls, plus the original exact NF404 sinh center.

The independent [NF494 rational method script](../../scripts/local_replay/verify_nf494_original_J8_analytic_H400_method_exact.py) compares the direct complete NF446 moving-interval toy kernel \(K=1/t\) with the independently refactored \(F+L+R_+\) analytic Taylor coefficients **for six adversarial exact odd polynomial source carriers over fifteen coefficients each** (90 distinct exact source algebra controls), while separately checking actual immutable original raw dyadic NF407/406 source hashes and a source-specific \(m\ge1000\) compact finite-window tail estimate. The toy is a pure algebraic cross-check, not a replacement for the actual \(K\) in the original native calculation.

## Actual original 4096-bit source-native numerical result so far

The full original NF494 [native source job #42850200418 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/42850200418) computes every one of the **400 original complete \(H\)-coefficients** and the corresponding 400 true \(U(B-d)\) source coefficients. The first 400 complete \(U\) jets were independently accepted by NF493, and the full native \(H\) now source-matches:
\[
\boxed{
H(0)=z(B)\approx-4.38192122468351\times10^{-10}
}
\]
and
\[
\boxed{
H(1/500)\approx-7.617627806127017\times10^{-10},
}
\]
the latter agreeing with separately source-accepted NF492 genuine whole physical value rather than with a new independently fitted response. These are *pointwise checks of actual source-native 400 coefficients*, not values of the whole positive energy integral.

Each source-native output coefficient ball includes the original native 4096-bit Arb rounding radius plus an explicitly conservative separate \(10^{-300}25^j\) global source-input+tail overcharge. The original NF492 400-jet **analytic** H remainder is independently \(<10^{-99}\) on the true \(0\le d\le1/500\) interval, the corresponding source U 400-jet remainder \(<10^{-119}\). Neither was conflated with native source coefficient numerical uncertainty.

## Independent full physical square and NF404 selected-source obligation

NF494 independently replays the just-generated true original 400-H/400-U source coefficient intervals against accepted NF493 original U jets, the accepted NF492 **true original physical H(1/500)** receipt, NF450 original \(z(B)\), and canonical NF491 genuine \(J_8\) positive-bulk gate. It forms from the **joint 400 source before projecting components**:
\[
A(d)=H_{400}(d)+vC_8,\qquad C(d)=U_{400}(B-d)/2,
\qquad w_{400}(d)=A(d)+C(d)\log(B/d).
\]
Then it computes one actual source-certified **improper complete original positive square**
\[
\boxed{
E_{w,T}=\int_0^{1/500} w(B-d)^2\,dd
\approx \int_0^{1/500}
\bigl[A(d)^2+2A(d)C(d)L(d)+C(d)^2L(d)^2\bigr]dd
}
\]
with **exact rational** NF488 log/ log² polynomial moments and properly paid original source-native 400-coefficient intervals. If actual original source coefficient tails permit a smaller retained polynomial, the cutoff is computed **a posteriori from all 400 genuine normalized source coefficient balls** with its explicit absolute \(\ell^1\) error; no guessed frequency decay or unverified midpoint mesh. The final square error integrates the genuinely improper logarithm using \(\int L<8\delta\), \(\int L^2<65\delta\), and the accepted original \(|w|\) envelope.

Only after independent exact original-source Fraction CI SUCCESS may the actual \(E_{w,T}\) interval be promoted. The true NF491 last \(10^{-15}\) collar is then subtracted to obtain \(E_{w,\mathrm{bulk}}\); the original NF482 first irrational signed n9 panel and NF483 terminal principal \(E_p\) give the **authentic complete signed \(D_8\)**. Its selected-source NF404 acceptance is a **distinct threshold comparison**, not a whole Weil positivity or RH result.

**Standing:** full original \(H_{400}\) and \(U_{400}\) native source coefficients **SOURCE-NATIVE COMPUTED; independent square still PENDING**. The complete physical source energy and original \(D_8\) upper, NF404 selected scalar, W-ODD-NEG, exterior \(J_{242}\), whole even/odd Weil operator/domain, RH are **OPEN unless and until the separate exact source square CI passes**.

**Next bold NF495:** independently audit the original 400 complete joint-source coefficients and whole physical square, reconcile the NF491 acceptance/certain-failure corridors without silently promoting a failed source interval, then assess the remaining exterior/odd/operator-domain RH obligations. No main merge.
