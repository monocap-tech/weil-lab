# SM20 — first original physically supported odd forward-residual column

**Active obligation:** W-ODD-NEG OPEN. **Dependency:** SM10 original negative-cap Taylor carrier, SI29 original physically supported pole conditioning, SM18 forward-residual identity and SM19 original fourteen-feature Woodbury upper. **Standing:** rigorous analytical tail argument and a source-specific exact-rational enclosure computation, pending Actions verification. No 890-column inverse bound or RH theorem is asserted.

## 1. Original source and physical operator

Take the FIRST actual degree-zero original SM10 sine-Taylor source, not a separately selected convenient witness:
\[
u_0(x)=\sin(2\pi c_0x),\quad x\in[-B,B],\qquad
c_0=\tfrac12(\text{first cluster left}+\text{first cluster right}),\quad B=11/10.
\]
Here the cluster comes from the full verified 973-leaf original signed-negative support cover. We retain the actual original positive multiplier \(a(\xi)=\max(m(\xi),\kappa)\), \(\kappa=1/1000\), the supported form operator \(A_o\) and odd pole \(A_*=A_o-2|s\rangle\langle s|\), \(s=\sinh(x/2)\). All inverse and forward claims refer to the physical support.

## 2. Original full-frequency Fourier graph bound

The original archimedean multiplier has an Euler positive series, with \(y=\pi|\xi|\), \(a_0=1/4\) and \(f(t)=y^2/[t(t^2+y^2)]\):
\[
\operatorname{Re}\psi(a_0+iy)=\psi(a_0)+\sum_{n=0}^\infty f(n+a_0),\quad
\psi(1/4)=-\gamma-\pi/2-3\log2.
\]
The original multiplier subtracts an additional \(\log\pi\), so this constant is negative. For \(N=\max(1,\lceil y\rceil)\), use \(f(t)\le1/t\) for the head and its monotone integral for the tail:
\[
\sum_{n<N}f(n+1/4)\le 5+\log N,\qquad
\sum_{n\ge N}f(n+1/4)\le 1+\tfrac12\log 2<3/2.
\]
Therefore the arch contribution is below \(7+\log(1+\pi|\xi|)\). The original seven prime cosines have absolute total smaller than the existing exact SI06 envelope TWOC < 70751/10000 < 8. As \(\pi<4\) and \(\log4<2\), the complete original multiplier has the conservative bound
\[
\boxed{\kappa\le a(\xi)<18+\log(1+|\xi|)\quad(\xi\in\mathbb R).}
\]

On \(|\xi|\le2048\) this is smaller than 26, using the exact-rational upper \(\log2049<8\). For \(|\xi|\ge2048>2c_0\), the exact shifted finite-interval sine transform gives
\[
|\widehat{Zu_0}(\xi)|\le 2/(3|\xi|),\qquad
a(\xi)<19+\log|\xi|.
\]
Integrating both reflected exterior half-lines and using \(\log2048<8\),
\[
\int_{|\xi|\ge2048}a(\xi)^2|\widehat{Zu_0}(\xi)|^2\,d\xi
 < \frac89\frac{(19+8)^2+2(19+8)+2}{2048}
 =\boxed{\frac{785}{2304}}.
\]
The exterior bounds **the square of the actual unbounded multiplier**, not merely its energy weight. With exact physical sine Gram \(n_-\le\|u_0\|^2\le n_+<9/4\), Plancherel and physical restriction give
\[
\|A_o u_0\|^2<676n_++785/2304.
\]
The original odd pole has \(\|s\|^2=\sinh(B)-B<1\), so
\[
\boxed{\|A_*u_0\|^2<M_0:=1360n_++785/1152.}
\]
In particular this actual physical source belongs to the supported operator domain, including the complete infinite graph tail.

## 3. Nonzero actual forward trial and certified column

Let \(\kappa_*=33621/10^9\) be the SI29/SM01 original pole-conditioned floor. Define an explicit nonzero trial and its *actual* original forward residual:
\[
Y_0=\lambda u_0,\quad \lambda=\kappa_* n_-/M_0>0,\quad
E_0=u_0-A_*Y_0.
\]
The exact inverse-free residual diagonal satisfies
\[
\boxed{
0\le D_{00}=\|E_0\|^2
\le n_+-\frac{\kappa_*^2n_-^2}{M_0}<n_+.
}
\]
Choose a rationally checked integer \(N_0\) with \(N_0^2>M_0\). The lower enclosure \(\max(0,n_--4\lambda N_0)\le D_{00}\) follows from a Cauchy-Schwarz cross estimate and \(\|u_0\|<3/2\).

The true original odd pole residual overlap has interval
\[
t_0=\langle s,E_0\rangle\in
[q_--\lambda N_0,\ q_++\lambda N_0],
\]
where the physical original SI18 rational signed pole overlap is \([q_-,q_+]\).

For **every one of SI29's 14 original continuous positive-frequency means/moments**, evaluate the supported physical sine Gram against \(u_0\) with the inherited rational Simpson/Legendre uniform error \(\tau_i\). If \([\ell_i,u_i]\) is the original Simpson source-to-sine enclosure, the original true residual cross-Gram satisfies
\[
\boxed{
F_{i0}=\langle g_i,E_0\rangle
\in [\ell_i-2B\tau_i-3\lambda N_0,\ 
       u_i+2B\tau_i+3\lambda N_0].
}
\]
Here the exact true SI29 source bounds \(\|g_i\|<3\) and \(\|A_*u_0\|<N_0\) pay the forward-action uncertainty. All 14 signed intervals, the true original source center, \(D_{00}\), \(t_0\), and the global graph tail are reported by the validator. This is **a first actual original source/residual column**, rather than a toy 2x2 inverse matrix.

## 4. Precise limitations and next dependency

The lower-bound-driven trial \(\lambda\) can be very small, and the certified strict decrease of \(D_{00}\) relative to the original source norm upper may be microscopic. It is **not evidence** that the entire 890-column inverse approaches its threshold. The other 889 columns, their coupled residual Gram, complete physical original forward \(H_Y\), 14-by-890 feature overlaps, pole response, and the all-column SM19 rational PSD test remain uncomputed. A localized original positive-action estimate or better Ritz trial will likely be necessary before extending this approach, rather than repeating a weak scalar damping 889 times.

W-ODD-NEG, even/whole form, global zeta transfer, formal Lean attachment, independent mathematical review and RH remain OPEN.

Validator: python scripts/validate_rpb108_sm20_original_source_forward.py
