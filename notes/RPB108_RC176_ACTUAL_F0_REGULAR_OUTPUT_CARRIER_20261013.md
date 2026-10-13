# RC176: complete actual f0 regular output carrier

Parent: RC175, `93fd7326ce1f8f942369aa38c980336ec7d0c709`.

RC175 represented the actual regular f0 source with a paid input tail, but evaluated only its zeroth and second output coefficients. RC176 supplies all even output coefficients through degree 512 and pays the entire remaining output tail. It also realizes the finite -r D^-1 f0 correction, making the canonical first-action trial explicit in the unchanged native frame.

The evaluated operator is

\[
 L=D+h+R-rI,\quad D P_n=(H_n+s)P_n,\quad
 B=11/10,\quad r=789/125,\quad s=c_R+\log 2+r.
\]

The physical regular source is Rf0. The trial for the canonical source action is D^-1 Lf0. Neither is an original Weil action.

## 1. Analytic spatial kernel

RC170 proved the Poisson representation

\[
 R=\int_0^\infty (1-e^{-et})\chi P_t\chi\,dt/t,
 \qquad P_t(x-y)=\frac{2t}{t^2+4\pi^2(x-y)^2}.
\]

For d>0 its spatial kernel is

\[
 k(d)=2\int_0^\infty\frac{1-e^{-et}}{t^2+(2\pi d)^2}\,dt
      =\frac{h(2\pi e d)}{\pi d},
 \qquad h(w)=\int_0^\infty\frac{1-e^{-wu}}{1+u^2}\,du.
\]

The standard Laplace representation and sine/cosine integral series give

\[
 h(w)=\cos w\,\mathrm{Si}(w)-\sin w\,\mathrm{Ci}(w)
       +\frac\pi2(1-\cos w)
 =\frac\pi2(1-\cos w)+
 \sum_{j\ge0}\frac{(-1)^j w^{2j+1}}{(2j+1)!}
       (H_{2j+1}-\gamma-\log w).
\]

Primary formula controls: [NIST DLMF 6.7.13](https://dlmf.nist.gov/6.7.E13), [6.6.5](https://dlmf.nist.gov/6.6.E5), and [6.6.6](https://dlmf.nist.gov/6.6.E6). The harmonic coefficient identity can also be checked from h''+h=pi/2-1/w and h(w)=w(1-gamma-log w)+O(w^2). The series solves this differential equation with that boundary behavior.

Set t=(B-x)/(2B), v=(B-y)/(2B), and c=4 pi B e. The scaled kernel is K(d)=2B k(2Bd), d=|t-v|. With C=gamma+log c=1-c_R=1-s+log2+r, it has polynomial and logarithmic coefficients

\[
 K(d)=\sum_{j\ge0}(A_j d^j+B_j d^j\log d),
\]

\[
 F_j=\frac{4Be(-1)^{j/2}c^j}{(j+1)!},\quad
 A_j=F_j(H_{j+1}-C),\quad B_j=-F_j\quad(j\text{ even}),
\]

\[
 A_j=\frac{(-1)^{(j+3)/2}c^{j+1}}{2(j+1)!},\quad B_j=0
 \quad(j\text{ odd}).
\]

The script fixes rational centers e_c, pi_c, C_c before any ill-conditioned monomial arithmetic. True constant uncertainty is paid globally, rather than independently propagated through large cancelling polynomial coefficients.

For the actual-to-centered parameter replacement, let delta_e and delta_pi bound the parameter errors, and

\[
 \delta_C=(s_+-s_-)/2+\delta_{\log2}
                  +\delta_e/e_-+\delta_\pi/\pi_-.
\]

The supported row norm is at most A_inf=4B e_+ +1: split the Poisson integral at 4B and use the row bound min(1,4B/t). Differentiating the e parameter costs delta_e/e_-. Differentiating pi costs at most 4 A_inf delta_pi/pi_-; the factor includes the centered Poisson kernel mass ratio below 2. The C replacement costs 4B e_c delta_C because its kernel difference is -4B e_c delta_C sinc(c_c d). Replacing the universal pi/2 in the odd series by pi_c/2 adds at most delta_pi c_c/pi_c, using 1-cos(w)<=w. The sum is a valid bound in both physical L2 and Linfinity.

For K=192, all omitted terms have j>=K+1. H_{j+1}<=j+1 and d^j|log d|<=1/j yield the uniform bound

\[
 \epsilon_K\le
 \left(4Be_c+\frac{c_c/2+4Be_c(|C_c|+1)}{K+2}\right)
 \frac{c_c^{K+1}/(K+1)!}{1-c_c/(K+2)}.
\]

A uniform scaled-kernel error bounds the supported L2 operator error by the same scalar, by Schur's test on the unit interval. The certificate gives epsilon_K < 2.021e-54.

## 2. Exact convolution into a finite analytic source

Use RC175's rational input centers through degree M=172; the actual f0 still extends through degree 988. The omitted input is paid with RC174's actual R smoothing theorem. The center polynomial is

\[
 q(v)=\sum_{\substack{2\le n\le172\\n\text{ even}}}
          \alpha_nP_n(1-2v)=\sum_{l=0}^{172}a_l v^l,
 \quad
 a_l=\sum_{n\ge l}\alpha_n(-1)^l\binom nl\binom{n+l}l.
\]

Exact rational reflection verifies q(1-v)=q(v). For k=j+l+1 and beta=j! l!/(j+l+1)!,

\[
 \int_0^t(t-v)^jv^l\,dv=\beta t^k,
\]

\[
 \int_0^t(t-v)^j\log(t-v)v^l\,dv
   =\beta t^k(\log t+H_j-H_k).
\]

The right integral has the same expression at 1-t by reflection. Therefore the complete represented source is

\[
 \widehat g(t)=\sum_{k=1}^{365}
  \{w_k[t^k+(1-t)^k]+b_k[t^k\log t+(1-t)^k\log(1-t)]\},
\]

\[
 w_k=\sum_{j+l+1=k}a_l\beta[A_j+B_j(H_j-H_k)],\qquad
 b_k=\sum_{j+l+1=k}a_l\beta B_j.
\]

Every stored w_k,b_k is a rational center with an outward radius. Directed 360-digit operations retain cancellation; rounding uses a 10^-80 grid. The uniform rounding error is bounded by the sum of 2 radius(w_k)+2 radius(b_k)/k. Endpoint values use the continuous limit t^k log t=0 at t=0.

Write Gamma_tail and Gamma_center for RC175's physical input error energies, and Gamma_prefix for the exact rational-center input norm squared. RC174 gives phi_172 for the regular input tail. The whole-function error is

\[
 E_2=\phi_{172}\sqrt{\Gamma_{tail}}
   +r\sqrt{\Gamma_{center}}
   +(\epsilon_{parameter}+\epsilon_K)\sqrt{\Gamma_{prefix}}
   +\sqrt{2B}\epsilon_{round}.
\]

Consequently ||D^-1(Rf0-g_hat)||_D <= E_2/sqrt(s_-). This includes every output coefficient of the input error; it is not assigned only to retained modes.

The source samples and modes 0/2 agree with RC175's independent Poisson construction within their paid actual-source enclosures.

## 3. Closed Legendre projection and full infinite output tail

For even n, use the exact moments over u in [-1,1], t=(1-u)/2:

\[
 J_n(k)=\int_{-1}^1t^kP_n(u)\,du
 =\frac{2(k!)^2}{(k-n)!(k+n+1)!}\quad(k\ge n),
\]

with J_n(k)=0 for k<n. Their differentiated moments are

\[
 L_n(k)=J_n(k)(2H_k-H_{k-n}-H_{k+n+1})\quad(k\ge n),
\]

\[
 L_n(k)=(-1)^{k+1}\frac{2(k!)^2(n-k-1)!}{(n+k+1)!}
 \quad(n>k).
\]

The coefficient of the symmetric source is

\[
 \widehat g_n=(2n+1)\sum_k[w_k J_n(k)+b_k L_n(k)],
\]

and odd coefficients vanish. The certificate stores every even coefficient through N=512 and the rational D^-1 coefficient centers, paying the actual s enclosure in each division.

Above N, the polynomial part is identically zero. For the single symmetric log basis with power k, the exact tail coefficient magnitude is

\[
 2(2n+1)(k!)^2\frac{(n-k-1)!}{(n+k+1)!}.
\]

Since the factorial denominator is a product of 2k+2 factors, each at least n-k, set

\[
 A_k=2+\frac{2k+1}{N+2-k},\qquad D_{first}=H_{N+2}+s_-.
\]

The basis tail energy is bounded by

\[
 T_k^2\le\frac{4B A_k(k!)^4}
 {D_{first}(4k+2)(N-k)^{4k+2}}.
\]

Indeed the individual D^-1 energy is at most 8B A_k(k!)^4 (n-k)^(-4k-3)/D_first. Summing the even grid from N+2 is bounded by half the integral from N to infinity. This pays infinitely many output modes.

The represented full tail satisfies T_hat <= sum_k |b_k| T_k. No cancellation of unknown tail errors is assumed. Exact integer square-root upper bounds use a 10^-300 grid; this avoids amplifying a coarse square-root floor by large monomial coefficients.

The low coefficient-rounding error and the represented output tail have disjoint D supports, so their energies add. The actual whole-function error E_2/sqrt(s_-) is then added by the triangle inequality. It is not declared orthogonal to either projection error.

## 4. Result and canonical first action

| Quantity | Certified upper bound |
|---|---:|
| Whole physical source error ||Rf0-g_hat||_2 | 0.000194699899 |
| Whole source error in D^-1 norm | 0.000099857958 |
| Represented infinite output tail in D^-1 norm | 0.000000023131 |
| Complete actual D^-1 Rf0 carrier error in D norm | 0.000099881089 |
| Complete canonical f0 first-action trial error in D norm | 0.000099881089 |

The final canonical trial is

\[
 f0+w14+\widehat p_{-rD^{-1}f0}+\widehat p_{D^{-1}Rf0}.
\]

The negative-r correction has stored even coefficients through degree 988. Its coefficient error is paid separately. RC129's full Cf0-w14 error remains in the total. Native f0 and w14 retain their existing exact meanings; no new source frame replaces them.

The seven-source canonical inverse, the correlated P0/P2/f0 action Gram, and any actual Riesz iteration remain unevaluated. Stage I is open: the actual augmented Weil floor and auxiliary response bound have not been established. No whole-aperture original positivity, RH, F4, or Lean claim is made.

## 5. Replay and next cursor

The validator hashes its RC175, RC174, RC170, and RC129 inputs and checks their cross-links. Generation and replay use opposite kernel-convolution summation orders and must produce identical certificate JSON. It checks exact input reflection, all-range kernel truncation, actual sample and coefficient control overlap, and both complete error thresholds.

Independent exact controls also passed: direct integration of expanded Legendre polynomials verifies 30 polynomial/log moment pairs (n=0,2,4,10,20; k=0,1,2,5,20,35), and multiplication of the Si/Ci series verifies the first 12 odd harmonic-kernel coefficients. The stored carrier dimensions are 257 regular output modes, 494 negative-r correction modes, and 365 analytic source powers.

```bash
python scripts/validate_rpb108_rc176_f0_regular_output_carrier.py \
  --replay --output certificates/rpb108_rc176_f0_regular_output_carrier.json \
  certificates/rpb108_rc175_f0_regular_physical_source.json \
  certificates/rpb108_rc174_regular_source_tail_compression.json \
  certificates/rpb108_rc170_poisson_regular_action.json \
  certificates/rpb108_rc129_four_vector_joint_moment.json
```

Next cursor: pay the f0 canonical action diagonal and mixed action Gram with the new complete carrier, then extend canonical inversion from P0/P2 to P0/P2/f0. This does not substitute for Stage I's original Weil targets.
