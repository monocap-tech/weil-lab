# RPB108 RC34 — certified whole physical residuals by log-polynomial moments

2026-10-10. Branch research/rpb108-route-consolidation.
Recovered parent 2008488be84e5a9a8cf8714035bf5ed0ab5c1615 (RC33).
Other branches and historical reports are unchanged.

## Result

All eight actual RC31 polynomial trial Riesz vectors now have certified
whole physical residual bounds, including their endpoint logarithms:

| Column | Physical residual norm upper (display) |
|---|---:|
| 0 | 0.067494 |
| 1 | 0.056097 |
| 2 | 0.062957 |
| 3 | 0.053409 |
| 4 | 0.066062 |
| 5 | 0.058252 |
| 6 | 0.089994 |
| 7 | 0.083155 |

The proof data are rational SQUARED upper bounds in the certificate,
not these rounded displays. Every physical norm is below 0.090.

For arbitrary moment coefficients a, the collective estimates are

    ||sum a_j(p_j-L_B v_j)||_2^2 <(31/200) a^*D a,
    ||sum a_j(r_j-v_j)||_D^2 <(19/125) a^*D a.

Thus physical squared error is below 0.155 and canonical squared error
below 0.152. These improve RC32's 0.49 canonical envelope but do not
supply arbitrarily accurate Riesz vectors or certify the native head.

## Entire kernel series in normalized coordinates

Put y=(x+B)/R in [0,1], R=2B=11/5, s=r/R, and Z=2pi e R.
The normalized density has the exact convergent expansion

    R k(Rs) =
      (1-cos(Zs))/(2s)
      +sum_(n odd) (-1)^((n-1)/2)
          (H_n+c_R-1) Z^n s^(n-1)/(pi n!)
      -[sin(Zs)/(pi s)]log s.                       (1)

This is the SAME actual k as RC25, with its logarithmic singularity
retained. To derive it, set
u(z)=pi/2-[sin z Ci(z)-cos z(Si(z)-pi/2)].
Then u''+u=pi/2-1/z. Inserting -sin(z)log z plus an analytic series
gives the odd coefficients H_n-gamma, and the even term
pi(1-cos z)/2; the recurrence uses
H_n-H_(n-2)=1/(n-1)+1/n.
The small-z normalization fixes the analytic linear coefficient:
u(z)=-z log z+(1-gamma)z+O(z^2).
Finally gamma+log Z=1-c_R by RC26.
Equivalently (1) follows by multiplying the convergent Ci/Si series.
No special-function numerical library is used in this certificate.

## Truncation and scalar uncertainty

For coefficient evaluation use c_mid, the exact rational midpoint of
RC26's scalar interval. Let d_c=488163/(2*10^9) be its half-width.
Truncate all series at n<=192. The interval arithmetic verifies Z<42.
For the omitted terms, H_n<=n and |c_mid-1|<5. Also
s^(n-1)|log s|<=1/[e(n-1)]<1 for n>=193.
The absolute normalized density tail is therefore bounded uniformly by

    eps=(4/3)*200*42^193/193! <1e-40.

The ratio of successive majorants is below 1/4 from n=193 onward,
which proves the geometric tail factor 4/3. The operator error on
the interval is <=eps by its row-integral bound in normalized coordinates.

Crucially, changing c in (1) changes the physical kernel by
(c-c_mid) sin(2pi e r)/(pi r). The whole-line sine-kernel multiplier is
the indicator of [-e,e], so its compressed physical norm is <=1.
The scalar multiplication c_R I also changes. Thus the total metric
source error from scalar uncertainty is <=2 d_c ||v||_2.
This keeps the scalar uncertainty OUTSIDE coefficient cancellation.
No broad uncertain c is inserted into the polynomial integrals.

The exact source residual differs from its truncated midpoint-scalar
version by physical norm at most

    (2 d_c+eps)||v||_2.                              (2)

## Exact convolution into polynomial-log form

For v(y)=sum v_m y^m and a kernel power s^p,

    integral_0^y s^p(y-s)^m ds
      =beta(p+1,m+1)y^(p+m+1),

    integral_0^y s^p log s (y-s)^m ds
      =beta(p+1,m+1)y^(p+m+1)
          [log y+H_p-H_(p+m+1)].

The beta factors are rational factorial ratios. The right-distance
integral is the same formula with 1-y and v(1-y). RC31's actual trial
parity gives v_j(1-y)=(-1)^j v_j(y).

Including the exact singular source, the midpoint scalar, and
W=-[log y+log(1-y)]/2, each truncated residual is exactly

    A_j(y)+B_j(y)log y+C_j(y)log(1-y),

with computable polynomial coefficients. Neither endpoint is cut off.

## Exact logarithmic norm moments

For integer n>=0 set a=n+1. The needed unit-interval moments are

    integral y^n =1/a,
    integral y^n log y =-1/a^2,
    integral y^n log(1-y) =-H_a/a,
    integral y^n log^2 y =2/a^3,
    integral y^n log^2(1-y) =(H_a^2+H_a^(2))/a,
    integral y^n log y log(1-y)
      =H_a/a^2+[H_a^(2)-pi^2/6]/a.

Here H_a^(2)=sum_(k=1)^a 1/k^2.
These follow by differentiating the beta integral twice; the
mixed trigamma sum uses sum 1/k^2=pi^2/6.
Their integrability at both endpoints justifies the differentiations.

Expanding the square and applying these moments gives the whole
physical squared norm, multiplied by R. Thus the interior and endpoint
parts are integrated simultaneously. RC33's endpoint certificate
remains a separate valid check, but its budget is not added again.

## Executed enclosure and collective transport

scripts/validate_rpb108_rc34_log_polynomial_residual.py runs using
RC30's 220-digit directed Decimal interval class and bounded Machin pi.
It evaluates all coefficients, reflections and moments with intervals.
Each final nominal squared-norm interval has width below 1e-20.

The certified per-column upper is obtained by taking its upper square
root, adding (2), squaring outward, and rounding UP to a rational
with denominator 10^12. Physical ||v_j||_2^2 is exact from its
Legendre coefficients and diagonal physical mass D.

The collective bound uses trace: for the physical residual map F,

    ||F D^(-1/2)||^2 <=trace(D^(-1/2)F^*F D^(-1/2))
                    <=sum_j epsilon_j^2/D_jj <31/200.

This is a lawful all-coefficient bound without evaluating mixed
residual Gram entries. RC32's supported inclusion norm squared
<=252/257 and RC24's weak source attachment give the canonical bound.
The executed exact rational aggregate is stored in the certificate
and is below 19/125.

Execution: PASS. All eight whole-interval enclosures, truncation
budget, scalar-source transport and aggregate bounds passed.
RC33's order-512 numerical diagnostics lie below the new bounds;
that comparison is a consistency check, not the proof.

The computational assumption remains RC30's documented correctly
rounded Decimal arithmetic behavior. This is analytic plus interval
certification, not a Lean theorem.

## Next obligation and scope

Actual certified whole weak residual upper bounds are now available
for these eight Legendre moment trials. They are not the complete
8600-feature canonical head and they are not native source-response
vectors. The achieved collective canonical norm bound is roughly
sqrt(0.152), not 0.0025.

Next: use the certified source calculation to improve trial vectors
or enlarge the trial space, paying whole residuals rather than the
generic inverse-norm envelope. Tightening scalar uncertainty would
also reduce the small numerical budget in (2), but does not remove
the dominant trial approximation error.

No native head/source positivity, original aperture extension,
RH/F4 theorem or Lean closure is claimed.
