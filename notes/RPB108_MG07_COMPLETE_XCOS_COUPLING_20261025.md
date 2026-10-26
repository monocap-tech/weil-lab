# Complete physical xcos coupling against the accepted signed anchor

This calculation evaluates three new original signed-form entries:
Q(f,r), Q(g,r), and a lower bound for Q(r,r). It uses the SAME physical
anchor f=u+(4096/3013)s, g=u-s, u=sin(2*pi*(37/64)x), s=sinh(x/2),
zero-extended from [-11/10,11/10].

The new source r=x*cos(2*pi*(37/64)x)+alpha*s is an exact rational
basis change of the original first-cluster degree-one generator and the
existing sinh source. Alpha is selected with denominator 10^6 using exact
endpoint intervals; this reduces the endpoint jump without changing the
three-dimensional span. Source membership is checked against the original
SI10 first cluster and Taylor order. Independence follows from independence
of sin(wx), x*cos(wx), sinh(x/2) for w>0 (apply D^2+w^2 and use the distinct
real and imaginary exponential roots). No sampled physical columns enter.

## Complete low and high-frequency accounting

All three entries use the same 7168 original rational cells in [0,12].
The original signed seven-prime/digamma multiplier endpoint intervals and
global curvature 2300 are retained. Exact affine-times-quadratic cell
integrals pay the source and multiplier interpolation errors. Each entry's
LOWER and UPPER endpoints are rounded outward separately to 10^-12; no
unpaid baseline rounding is permitted. The genuine physical sinh-pole
products, including both mixed products, are subtracted as intervals.

For xi>=12, SM41 proves a_o<=17+ln xi and the SI06 global negative
bound is Hsup<17. Consequently |m(xi)|<=17+ln xi on the ENTIRE tail.
This includes positive high-frequency mixed terms; none is discarded
when bounding Q(f,r) or Q(g,r).

For the anchor packets the existing exact sine/sinh Fourier identity gives

 |T(xi)| <= [ep+dv/k+n1/(k^2-w^2)+n2/(k*(k^2-w^2))]/(pi*xi).

Using k>=2*pi_lo*xi and
k^2-w^2 >= d*(2*pi_lo*xi)^2, d=1-(wup/(2*pi_lo*12))^2>0,
gives a four-term nonnegative reciprocal-power majorant. Coefficients are
rounded upward only. For r, two physical integrations by parts give

 |T_r(xi)| <= ep_r/(pi_lo*xi)
             +(2*dv_r+L1(r''))/(4*pi_lo^2*xi^2),

 L1(r'') <=4*B*wup+wup^2*B^2+|alpha|*(cosh(B/2)-1).

Products of these majorants are integrated with the complete log envelope:

 integral_L^infinity (17+ln xi)/xi^p dxi
 = L^(1-p)*[(17+ln L)/(p-1)+1/(p-1)^2].

Use ln12<4ln2<4*(347/500) and include both frequency signs exactly once.
For the new diagonal LOWER, all possible negative high-tail action is
paid by the independently replayed SI10 sum M2 times beta_r^2; positive
high diagonal action can be discarded as PSD.

## Matched scalar Schur gate

Accepted anchor inverse artifact 12625472360 from run 40263282082 is
pinned by successful run/source identity, archive digest and JSON digest.
It supplies H^-1<=diag(8000,24) and the existing scalar 7100 I cap.
For the COMPLETE mixed vector b=(Q(f,r),Q(g,r)), completion of the square
gives the true scalar Schur Q(r,r)-b^*H^-1 b. The validator reports

 lower = diagonal_lower -
   min(8000*bf_upper^2+24*bg_upper^2,
       7100*(bf_upper^2+bg_upper^2)).

The calculation is valid for this independent, nonorthogonal source
basis: r need not be L2-orthogonal to the anchor. A strictly positive
lower certifies this scalar physical Schur. A zero or negative lower is
INCONCLUSIVE about actual spectral sign; the workflow accepts honest
interval accounting regardless and records the positivity flag separately.

This is a concrete full-form coupling calculation using an accepted inverse
term, not a count-only source positivity checkpoint. It does not transport
the physical basis into SM34's energy-dual coordinates. All other physical
source couplings, finite/infinite remainder, original analytic/domain
review, W-ODD-NEG, even/CC27, Weil and RH remain OPEN.
