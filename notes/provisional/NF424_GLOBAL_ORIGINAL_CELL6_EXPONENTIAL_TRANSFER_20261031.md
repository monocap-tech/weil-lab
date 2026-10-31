# Weil-Lab NF424 — Global original cell-6 exponential transfer, no new x-centers

**2026-10-31 PT. Canonical `W-ODD-NEG` remains OPEN; RH OPEN.** Stacked on NF423 branch at `09f2c7cee2c37064cc1c01d3a49a0587b6048a50`. Unchanged original NF370 fourth supported source, 242 selected+4 critical generator coefficients from NF407, original NF406 seven prime seams, B=11/10, and NF404 exact dyadic pole center. This pass derives a new **analytic finite-series representation** and a full-cell **uniform truncation budget**; it does not yet produce numeric interval polynomial coefficients, a complete cell-6 integral, or the NF404 signed scalar.

## Previous cursor / current circle / next bold

- **Previous NF423:** shared true source-paid four x-jets at x=9/10; complete open cell 6 derivative bound |z'''|<286758; independent strict local positive island. The conditional second-jet tiling required approximately 667,657 *independently certified centers*, all uncomputed.
- **Current NF424:** replace repeated 398-t-panel evaluations at independently certified x-centers with one full-source **digamma + two endpoint image series**, valid on **every x in J6=(log 7-B,log 8-B)**. Derive and exactly audit a conservative <10^-45 **uniform error of the finite 2048-image expression**, including original native coefficient balls. All source terms are retained together before interval summation.
- **Next:** **Implement native 4096-bit correlated arithmetic for the finite analytic model (including the removable λ=±1/2 pole), construct interval Chebyshev/Taylor x-pieces and integrate signed pz and z² on all of cell 6**. Only after the actual numeric finite model is enclosed should one apply it to cells 3, 7, the other five, and the NF410/NF404 comparison.

## Exact analytic source transfer — no quadrature

Set `a0=1/4`, `d=B-x`, `t1=2(B-x)`, `t2=2(B+x)`, `K(t)=e^(-t/4)/(1-e^(-t))`. Use the *actual* NF422 operator

`S[g](x)=A(x)g(x)+I0[g](x)+I1[g](x)`

with original symmetric `I0` on [0,t1] and one-sided `I1` on [t1,t2]. The NF408/NF423 finite arch coefficient can be rewritten **exactly**

`A(x)=psi(a0)-log(pi)+(J(t1)+J(t2))/2`, where `J(t)=int_t^infinity K(s)ds=2(atanh(e^(-t/4))+atan(e^(-t/4)))`.

This identity follows from NF408's `Phi(d)=log[(d/B)coth(d/4)]+2atan(e^(-d/2))`: `Phi(d)+log(B/d)=J(t1)`. No approximation of the endpoint logarithm is involved.

For a complex generating mode `g(y)=e^(lambda*y)` initially with `|Re(lambda)|<1/2`, write

`D(lambda)=(psi(a0-lambda/2)+psi(a0+lambda/2))/2-log(pi)`.

Combine the exact full semi-infinite symmetric kernel integral (digamma difference) with the two moving physical support corrections. The resulting exact **global physical transfer** is

```
G(x,lambda) := S[e^(lambda*.)](x)
  = e^(lambda*x)*D(lambda)
  + (e^(lambda*B)/2)*sum_{m>=0}
       exp(-2*(m+a0)*(B-x))/(m+a0-lambda/2)
  + (e^(-lambda*B)/2)*sum_{m>=0}
       exp(-2*(m+a0)*(B+x))/(m+a0+lambda/2).
```

Indeed, the t1/t2 corrections from `I0` and `I1` contribute, before cancellation,

`1/2 sum_m [E_(alpha-lambda/2)(t1)-E_alpha(t1)+E_(alpha+lambda/2)(t2)-E_alpha(t2)]`, with `E_beta(t)=exp(-beta*t)/beta` and `alpha=m+a0`. The two `E_alpha` pieces cancel the `J(t1),J(t2)` in `A`, while `psi(a0)+C(lambda)=(psi(a0-lambda/2)+psi(a0+lambda/2))/2`. Exact Fraction symbolic coefficient ledger is replayed by the NF424 script.

The **original source**, not a substitute sine, is

```
u4(y)=sum_(f,k) c_(f,k)*y^k*(sin(2*pi*f*y) if k even
                            else cos(2*pi*f*y))
       + c_p*sinh(y/2).
```

All original 242 selected modes, 32 critical sines and four critical blocks, critical odd pole and exact 4096-bit dyadic midpoint/radius coefficients are reconstructed from the pinned NF407 receipt. Define `G_k(x,lambda)=partial_lambda^k G(x,lambda)`. Then

```
S[u4](x) = sum_(f,k) c_(f,k) *
               (Im G_k(x,2*pi*i*f) if k even
                else Re G_k(x,2*pi*i*f))
            + c_p/2*[G(x,1/2)-G(x,-1/2)].
```

This is a **single shared source-correlated analytic x-function**. The series is separable in x (real exponentials `exp(-2(m+a0)(B±x))`), and the same digamma/polygamma values at source frequencies apply to every physical x-piece. No independent physical t integral is required when evaluating further x coordinates.

**Removable pole:** at lambda=+1/2 the `psi(a0-lambda/2)` and m=0 left image are separately singular, but their sum has the exact regularization

`(e^(lambda*x)/2)*[psi(1+beta)+expm1(-2*beta*(B-x))/beta]`, with `beta=a0-lambda/2` and limiting quotient `-2(B-x)`. At lambda=-1/2 use `gamma=a0+lambda/2` and the symmetric right image, giving limiting quotient `-2(B+x)`. A native evaluator must use these *combined* expressions; evaluating the divergent pieces independently is forbidden.

On the true original open J6, NF406 authenticates exactly five post-seam and two neither original prime branches. Therefore the complete regularized original remainder is, with `v=u4(B)`, `w_n=Lambda(n)/sqrt(n)` and original dyadic center `h`,

```
z(x) = S[u4](x)
       - (v/2)*log(B/(B-x))
       - sum_(n in {2,3,4,5,7}) w_n*(u4(x-log n)+v)
       - h*sinh(x/2).
```

The original n=8,9 contributions are *neither*, not neglected; both are zero on the interior of this cell. Use real one-sided seam values at boundaries; do not cross knots with these formulas.

## Exact rational global error budget

From NF406 rational seam brackets one verifies **0.84<x<0.98** throughout J6. Consequently `t1>6/25`, `t1<1`, and `t2<21/5`. The true original source has `k<=13`, `f<883`, and the exact 246-generator raw dyadic midpoint triangle satisfies

`Uraw=sum |c_(f,k)| B^k + |c_p| < 10^160`;

its total native coefficient-radius bound satisfies `S0<10^-700`. These are deliberately gross source-level overcharges, not a replacement for correlated evaluation of the finite model.

Truncate **each** endpoint-image series at m=2047 (N=2048). The geometric tail `sum_(m>=N)e^(-m*t)=e^(-N*t)/(1-e^(-t))` is valid at both t1,t2. Differentiation in lambda exactly generates `(y)^k` and satisfies `(B+t/2)^k <= B^k exp(13*t/(2B))` for k<=13. The odd pole lambda=±1/2 adds at most `exp(B/2+t/4)<3exp(t/4)`. After collecting **both** image tails, an outward rational overcharge follows with `M=N-65/11>2000`, `M*t1>480`, `1-e^(-t1)>1/6`, `e>8/3`:

`|S[u4_mid]-S_2048[u4_mid]| < (36/2000)*10^160*(3/8)^480 < 10^-45`

**for every real x in the entire true open cell J6.**

For the true NF407 coefficient balls, `|delta u|<=S0` and `|delta u''|<10^12*S0` on [-B,B]. True NF423 `|A|<4`, finite original I0 symmetry `|delta I0|<10^12*S0/8`, true I1 `|delta I1|<8*S0`, original endpoint log subtraction `<3*S0/2`, and original five signed prime weights sum <3, charging `<6*S0`. Hence the entire original regularized z differs from the midpoint-source expression by

`|z_true(x)-z_mid(x)| < (10^12+20)*S0 < 10^-680`.

Combining **uniform series tail plus uniform original source-radius charge** gives the exact output obligation

`sup_(x in J6) |z_true(x)-z_2048(x)| < 10^-45`.

This error bound is **not** a certificate of the arithmetic value or enclosure of `z_2048(x)`; it does not assert that a finite high-order Chebyshev representation has been run or that its interval widths remain small after large source cancellations. Its value is that the hard physical t integral and independently certified x-centers are removed from the outstanding work.

## Verification and method standing

- Exact Fraction source/knot/parent recheck and symbolic transfer ledger: `scripts/local_replay/nf424_original_cell6_global_exponential_transfer_exact.py`.
- Focused replay workflow: `.github/workflows/nf424-cell6-global-exponential-transfer.yml`. A workflow success verifies the declared analytic/source-cap checks, **not** the unevaluated 2048-image finite response or its x-integrals.
- Numerical native remaining obligation: evaluate the **entire combined** full source at enough x-polynomial/Chebyshev degrees on the single true cell; preserve all original source coefficients as **one correlated sum** before rounding, remove odd-pole singularities analytically, and supply outward complex arithmetic for digamma/polygamma, exp, rational log/prime seams and quadrature-free analytic tails. Integrate polynomial `z²`, exact NF410 signed `p z`, and interval remainders without treating `z` as constant across a cell.

**Disposition:** global original cell6 *analytic model and uniform source/tail error bound* are proposed for exact source replay. Full numeric decision-quality cell6 enclosure / integral and NF410/NF404 signed scalar remain OPEN; original fourth exterior inverse, W-ODD-NEG, even/whole Weil and RH remain OPEN. All evidence additive, no main merge.
