# RPB108 RC24 — physical source of the canonical logarithmic metric

2026-10-10. Independent route consolidation.
Parent: dc1a8fdaf4046a4bbe5e85f7a9d146e361d70c9a (RC23).
Only research/rpb108-route-consolidation is written.

## Result and boundary

The exact canonical metric has a physical source formula on Lipschitz
trial vectors, including both boundary terms created by zero extension.
At B=11/10 the source belongs to physical L2 and satisfies

    ||L_B v||_2 <=(13/4)||v||_infinity
                  +(33/20)Lip(v).

This proves an actual domain/source attachment for a concrete class of
trial vectors. It makes their physical residual norm a lawful upper bound
on the complete canonical weak residual required by RC23.

The actual constant trial source is identified as 1+E_B(x), with
E_B unbounded logarithmically near either endpoint. Consequently a
constant physical function is NOT the canonical Riesz representative of
the constant moment. The same distinction applies to the polynomial head.

No Riesz solution, small actual residual, finite matrix or positivity
certificate is computed. The result supplies the trial-source interface,
not the missing approximate inverse or actual head/source estimates.

## Metric and standing

The supported logarithmic carrier has norm

    ||h||_D^2=integral log(e+|xi|)|Fourier(i h)(xi)|^2 dxi,

Fourier convention exp(-2pi i xi x), and physical inclusion ||i||<=1.
Here e is the base of the natural logarithm.
The metric source L_B is the compressed physical logarithmic multiplier
on its operator domain; it is not bounded on all physical L2.

RC22 defines an 8600-feature canonical Chebyshev moment head.
RC23 requires whole dual residuals for trial Riesz and source vectors,
and gives their matrix error transport and conditional acceptance gate.
RC21 supplies a bounded physical native remainder ||R_B||<18, with

    Q(v,h)=<v,h>_D+<R_B i v,i h>_2.

Its native attachment remains pinned to CC27 blob
e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482 at CC119
5df347d3808ac3282864a657b7380e0f54bf4daa.

## Exact Poisson representation

For s>=0, differentiating a convergent nonnegative integral in s and
using its value zero at s=0 proves

    log(e+s)=1+integral_0^infinity
                 exp(-e t)(1-exp(-s t))/t dt.        (1)

The derivative integral is 1/(e+s).
This is an elementary proof, with no asymptotic substitution.

In the stated Fourier convention, inverse transformation of exp(-t|xi|)
gives the Poisson density

    P_t(r)=2t/(t^2+4pi^2 r^2),  t>0,

by integrating the two exponential half-lines. Its integral over the
real line is one.

For r>0 define the metric jump density

    ell(r)=2integral_0^infinity
               exp(-e t)/(t^2+4pi^2 r^2) dt.         (2)

It is positive. Integrating without the exponential or bounding the
denominator by 4pi^2 r^2 gives

    ell(r)<=1/(2r),
    ell(r)<=1/(2pi^2 e r^2)<1/(4r^2),               (3)

using pi>1 and e>2 in the last conservative bound.
The density is not used at r=0 without the difference cancellation.

## Source formula with both exterior terms

Let v be Lipschitz on [-B,B], with amplitude V=||v||_infinity and
Lipschitz constant K. Extend it by zero outside the interval.
On the physical cap define

    E_B(x)=integral_(B-x)^infinity ell(r)dr
           +integral_(B+x)^infinity ell(r)dr,

and

    (L_B v)(x)=v(x)
       +integral_(-B)^B [v(x)-v(y)]ell(|x-y|)dy
       +v(x)E_B(x),   -B<x<B.                      (4)

Both exterior terms arise from the zero extension. Neither may be
deleted by declaring the compressed Poisson convolution to preserve
constants. It does not preserve constants on a finite interval.

To attach (4), first truncate the t integral in (1) away from zero
and infinity. Its multiplier is bounded and Fourier inversion gives
the compressed Poisson difference exactly. Splitting integration over
the interval and its exterior gives the truncated version of (4).

The internal difference is absolutely integrable, since
|v(x)-v(y)|<=K|x-y| and (3) cancels the near-diagonal singularity.
The truncated densities are bounded by ell. The exterior estimates
below provide an L2 dominating function. Thus the truncated sources
converge in physical L2 to (4).

The zero extension of a Lipschitz interval function is of bounded
variation, with Fourier transform O(1/|xi|). Its logarithmic energy is
finite, so v belongs to D_B even when its endpoint traces are nonzero.
The truncated metric multipliers converge in the canonical weak form;
Cauchy--Schwarz with the weight and the finite energy justifies that
limit on the dense smooth core and then on D_B.
Therefore (4) has the FULL weak attachment

    <v,h>_D=integral conjugate(L_B v)(x)(i h)(x)dx

for every h in D_B. This proves the needed physical operator-domain
statement for these trial vectors; it does not derive one for arbitrary
form-domain vectors.

## Explicit endpoint and L2 budgets at B=11/10

For d>0 let F(d)=integral_d^infinity ell(r)dr.
Splitting at r=1 in (3) gives

    F(d)<= (1/2)log_+(1/d)+1/4.

For d>=1 the stronger F(d)<=1/(4d) also holds.
Consequently

    E_B(x)<= (1/2)log_+(1/(B-x))
             +(1/2)log_+(1/(B+x))+1/2.             (5)

Since B>=1, the two unit-width endpoint logarithm strips are disjoint.
Using integral_0^1 log(1/d)^2 dd=2, their half-weighted sum has L2 norm
one. Also sqrt(2B)<3/2. Hence

    ||E_B||_2<=1+(1/2)sqrt(2B)<7/4.                 (6)

The logarithmic integral identity follows directly from d=exp(-u) and
two integrations by parts; it is not a sampled endpoint estimate.

The internal integral in (4) has pointwise magnitude at most
(K/2)*(2B)=BK. Combining the physical constant term, that internal bound,
and (6) proves

    ||L_B v||_2
      <=sqrt(2B)V+B sqrt(2B)K+(7/4)V
      <=(13/4)V+(33/20)K.                          (7)

All quantities are physical cap norms. A boundary logarithm can be
unbounded pointwise while still belonging to physical L2.

For a finite Chebyshev trial v(x)=sum a_k T_k(x/B),

    V<=sum |a_k|,
    K<=(1/B)sum k^2|a_k|,

because T'_k=k U_(k-1) and |U_(k-1)|<=k on [-1,1].
Thus a direct certificate for its physical metric-source norm is

    ||L_B v||_2
      <=(13/4)sum |a_k|+(3/2)sum k^2|a_k|.          (8)

This is a coarse source norm allowance, not a small residual estimate.

## Actual constant source and the Riesz distinction

For v=1 on the cap, the internal difference in (4) is zero, so

    L_B 1=1+E_B(x).

The exterior source is genuinely nonconstant and unbounded at the
endpoints, not merely given an unbounded upper envelope.
For 0<r<=1/100, restrict (2)'s t integral to [0,2pi r].
Using 2pi e r<1 from pi<22/7 and e<3 gives exp(-e t)>1/3 there.
The remaining elementary integral equals 1/(4r), hence

    ell(r)>=1/(12r), 0<r<=1/100.

For endpoint distance d<1/100,

    E_B(x)>= (1/12)log[(1/100)/d],

which diverges as d tends to zero.
It follows that no scalar constant trial v=a can solve L_B v=1.
The constant-moment Riesz vector requires an actual inverse construction.
Physical Chebyshev orthogonality likewise cannot replace the canonical
Riesz metric.

## Lawful weak residuals for the finite certificate

Let p_j(x)=T_j(x/B), and let r_j represent its moment functional in D_B.
For a Lipschitz trial v_j, define the attached physical residual

    f_j=p_j-L_B v_j.

The just-proved weak identity gives

    ||r_j-v_j||_D
      =||ell_j-<v_j,.>_D||_(D*)
      <=||f_j||_2.                                (9)

For a Lipschitz trial source vector w_j, the physical residual for the
source functional built from v_j is

    g_j=R_B i v_j-L_B w_j.

The bounded actual R_B supplies its physical L2 term; (4) supplies the
metric source. Thus

    ||i^*R_B i v_j-w_j||_D<=||g_j||_2.              (10)

Certified SMALL whole physical residual norms in (9)--(10) would supply
RC23's epsilon_j and zeta_j without finite-test substitution.
No such norms are evaluated or certified here.

The full compressed native source on any Lipschitz trial also has the
lawful physical L2 representative L_B v+R_B i v, with bound

    ||L_B v+R_B i v||_2
      <=(121/4)V+(33/20)K.

This concerns the trial operator domain on the finite cap.
It does not make full Q a bounded physical L2 operator.

## Validation and remaining work

scripts/validate_rpb108_rc24_log_metric_source.py passes 20 exact rational
checks: disjoint endpoint strips, logarithmic L2 budgets, physical source
constants, near-kernel lower control, Chebyshev derivative budgets,
both exterior tails and the native source allowance.
The Laplace/Fourier, domain and endpoint-divergence proofs are analytic
arguments above; finite controls do not evaluate the kernel by quadrature.

The next actual data obligation is a validated approximation of the
metric inverse on the chosen moment/source functionals, with whole
physical residual enclosures from (4). Endpoint logarithms must be
retained in those enclosures. No inverse, small residual, head matrix
or source Gram is supplied in this step.

No original negative vector, new whole aperture positivity, RH/F4 theorem
or Lean closure is claimed. Existing 1.06 positivity and prior restricted
theorems remain intact. Other branches and historical files are unchanged.
