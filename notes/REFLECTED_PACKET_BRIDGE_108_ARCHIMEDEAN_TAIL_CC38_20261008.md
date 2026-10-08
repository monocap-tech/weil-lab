# RPB108 CC38: effective decay and certified archimedean tail error

Date: 2026-10-08 UTC. Parent: 87d8327117ab372d6c57e57024608452daee9415.
Definitions: [archimedean remainder tail](../docs/TERMINOLOGY_RPB108_ARCHIMEDEAN_TAIL.md).
Actual arithmetic result: |r_arch(xi)|<4/|xi| for |xi|>=1,
and ||C_arch,>R||<=4/[R log(e+R)] for every R>=1.

## Effective oscillatory integral bound

Reuse the primary NIST identity DLMF5.9.13,
https://dlmf.nist.gov/5.9.E13 , with CC37's

    k(u)=1/(1-exp(-u))-1/u, g(u)=exp(-u/4)k(u).

We already have 0<=k<=1. Direct differentiation gives

    k'(u)=1/u^2-1/[4 sinh^2(u/2)]>=0,

because 2sinh(u/2)>=u. Taylor expansion at zero gives k(0+)=1/2;
at infinity k tends to1. Hence int k'=1/2. Also g tends to zero
at infinity, is absolutely continuous up to zero, and

    int_0^infinity |g'(u)|du
       <=int exp(-u/4)k'(u)du+(1/4)int exp(-u/4)k(u)du
       <=1/2+1=3/2.                                    (1)

The real part of the digamma remainder is -int g(u)cos(yu)du,
y=pi*xi. Integration by parts has no boundary contribution: sin0=0
and g tends to zero at infinity. Thus for y nonzero,

    |Re psi(1/4+iy)-log|1/4+iy|| <=3/(2|y|).           (2)

This is a real-part estimate, not a claimed 3/(2|y|) bound on the
full complex remainder. The imaginary boundary term is not deleted
from a complex estimate. All integrability needed for (2) follows
from (1); no asymptotic remainder constant is assumed.

With x=|xi|>0, b=1/(4pi), the other logarithmic difference is

    (1/2)log(1+b^2/x^2)-log(1+e/x).

Using log(1+v)<=v, e<3 and pi>3 gives

    |r_arch(xi)|<=3/(2pi x)+e/x+1/(32pi^2 x^2)
                 <7/(2x)+1/(288x^2)<4/x  (x>=1).      (3)

Together with CC37, this is a rigorous global finite/tail envelope:
8 at all frequencies and 4/x beyond x=1. It proves an explicit rate
for the actual native archimedean remainder, not for critical leakage.

## Complete-domain truncation error

For canonical supported h,f, the omitted archimedean tail pairing
is the integral of r_arch times the two Fourier coordinates on |xi|>R.
Weighted Cauchy-Schwarz and monotonicity of x log(e+x) give

    |Q_arch,>R(h,f)|
       <=4/[R log(e+R)] ||h||_D ||f||_D.                (4)

Thus compression to any finite supported cap preserves the same
canonical operator bound. A coarser rational bound is 4/R since
log(e+R)>=1. This is a whole-domain error bound; it is not inferred
from values on finitely many test packets. In particular replacing
the archimedean remainder by its finite frequency band is lawful
only with this tail error still budgeted.

For a source-normalized critical lift and canonical old projection Pi,
the tail contribution to its outward complete-dual forcing obeys

    ||M_t^-1/2(I-Pi)C_arch,>R h||
       <=4/[c_B^2 R log(e+R)].                         (5)

Pi is not a physical Fourier cutoff, but its canonical contraction
suffices. The full inverse M_t remains in the bound. A fixed R gives
an absolute error. Turning (5) into a defect-dependent error requires
R to grow with the defect and also proving the retained band estimate;
neither requirement is discharged by the tail bound alone.

## Limits of the improvement

The complete native prime translations remain bounded physical
operators whose Fourier multipliers do not decay at large frequency.
This pass does not attach the archimedean tail rate to those terms,
or delete prime/pole cross correlations. Nor is the low-frequency
band itself a finite-rank canonical matrix: physical compactness can
support finite approximation but its actual approximation error must
still be computed or enclosed.

IP8's generic IP7 feasibility obstruction is preserved. Its huge
Fourier-radius requirement concerns the full unsigned physical
remainder envelope and logarithmic embedding tail, not the sharper
archimedean component alone. This component improvement therefore
does not invalidate that stopping rule, certify its finite matrix,
restart the paused aperture front, or supply CC35's signed adaptive
correlation estimate.

The validator replays CC37's 25,985 checks and adds eight exact
rational tail-budget checks, total25,993. Infinite-domain derivative,
integration-by-parts and multiplier bounds are analytic deductions;
no actual zeta critical covariance or new Lean proof is evaluated.

Original whole-domain positivity remains21/20, even0/odd0, physical
margin1/(3*10^63). RH/F4, defect-relative outward suppression,
retained attachment, reusable continuation and Lean closure remain open.
