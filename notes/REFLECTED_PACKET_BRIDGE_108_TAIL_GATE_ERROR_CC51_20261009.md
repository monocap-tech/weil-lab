# RPB108 CC51 — Pay the constructive tail error through the signed gate

Date: 2026-10-09 UTC. Publication base46df0b2a9f37e11b75ea6b15b9c5dce59e95226b.
[Definitions](../docs/TERMINOLOGY_RPB108_TAIL_GATE_ERROR_CC51.md).
This supplies an effective GEOMETRIC error payment for CC49–50 at53/50.
It does not evaluate the native columns or the high inverse Gram.

## 1. Cap constants for the original constrained problem

For B=53/50 a rational exponential series gives exp(2B)<9. The only
possible active prime powers remain2,3,4,5,7,8. Thus CC37's signed
pole-free physical remainder envelope still gives

    ||R_0||<8+2(12093/3740)=27053/1870<15,
    |H(f,g)|<=16||f||_D||g||_D.                         (1)

This bound concerns H=E_log+R_0, not physical boundedness of H. Both prime
orientations remain included. The actual poles vanish on the exact
moment-zero problem; approximate vectors are evaluated with H when
approximating its gate, not assumed to have exactly vanishing moments.

NF16's original F112 lower kappa=207/1000 holds on CC49's Fplus by
subspace inclusion. Since moments vanish there, C=Q|Fplus=H|Fplus,

    ||y||_D^2 <=(1+15/kappa)C(y).

For ANY form-domain input f, its complete high mixed response Wf satisfies

    ||Wf||_C <=16 sqrt(1+15/kappa)||f||_D <144||f||_D.   (2)

The inequality is a cap-only continuity envelope, not defect suppression.
It uses the form Riesz construction; no physical source representative
or unbounded operator-domain assertion is inserted.

## 2. Effective construction error for one compensated tail row

CC50's BV argument extends to every supported Legendre mode n>=0:
||phi_n||_D^2<=10n+13. In each parity, the sum of these bounds on E112
is31528 even and32088 odd, both<180^2. Hence every physical unit low
vector, including an orthonormal basis of E112 intersect ker m, has D norm
at most180. The exact normalized high moment tail has D norm<34, by its
positive coefficient ratios and Minkowski's inequality.

For CC49's t=f/||f||-(q/p)b, p=||Ew||,q=||Fw||, the low moment norm
satisfies p>1 in the even sector and p>1/3 in the odd sector. The former
follows from pairing cosh with the constant mode. The latter follows from
sinh(x/2)>=x/2 for x>=0 and its pairing with the linear mode:
p>=B^(3/2)/sqrt6>1/3. CC48's rational physical-tail bounds give q<1e-210
in both parities. Since ||b||_D<=180, the compensated low term has D norm
<540e-210<1e-200. In particular ||t||_D<35.

Let t_hat be the physically normalized12-term positive high polynomial
from CC50, with each positive relative coefficient replaced by its rational
interval midpoint. It intentionally omits the compensated low term,
paying that omission rather than declaring its moment zero. The certificate
interval widths are<=1e-79. On these12 modes n<=135, D norms are<37.
The midpoint errors have physical norm<=12e-79 and D norm<=444e-79.
Normalizing this perturbed polynomial changes its D error by at most

    [444e-79+34(12e-79)]/[1-12e-79] <1e-75.           (3)

Together with CC50's exact normalized truncation error<1e-59 and the low
compensation omission<1e-200, this gives

    ||t-t_hat||_D < epsilon=3e-59, ||t_hat||_D<36.    (4)

The polynomial's physical normalization may be kept as an exact square
root or enclosed outward; extra numerical normalization error must be
paid separately if it is introduced. No scalar susceptibility beta is
divided by in this construction.

## 3. Full signed Schur perturbation, including response Gram

Keep the exact Fplus FIXED. Define K(f,g)=H(f,g)-C(Wf,Wg). For an old
physical-unit moment-free vector u, (1),(2),(4) give

    |K(t,u)-K(t_hat,u)|
       <=[16*180+144^2*180]epsilon <4e6 epsilon.     (5)

For the diagonal, factor the differences in both the form and response
Gram, retaining their mixed terms:

    |K(t,t)-K(t_hat,t_hat)|
       <=[16+144^2](35+36)epsilon <4e6 epsilon.     (6)

Both are <2e-52. Only the one tail row/column per parity changes.
On the resulting56-coordinate finite gate, maximum absolute row sum
therefore bounds the geometric matrix operator error by

    eta_geom<56(2e-52)<2e-50.                       (7)

This pays the RESPONSE Gram perturbation as well as the finite native
form. A finite-row error without the W term would not be sufficient.

If a future computed approximant gate has certified coefficient lower
mu, with all OTHER kernel/source/inverse errors paid by eta_other, then

    mu > eta_other+2e-50                            (8)

is a sufficient strict-sign gate. The exact constrained physical basis
Gram is diagonal with tail norm squared1+(q/p)^2<2; a coefficient lower
mu-eta_other-2e-50 implies a physical finite lower at least half that
number. CC49 then supplies the full constrained floor with the high bound.
This is a numerical stopping rule, not a statement that (8) holds.

## 4. Scope controls and remaining missing input

The response in (5) uses the exact enriched high carrier even though
t_hat is not its retained vector. Replacing that carrier with the
orthogonal complement of the truncated polynomial is a different problem;
(7) does not pay that projection/inverse change. Likewise Q(t_hat) differs
from H(t_hat) by its actual pole square. One must compute the specified H
approximant or pay that extra discrepancy, not silently drop it from Q.

For a physical positive-level shift H_mu=H-mu I, the form bound becomes
16+mu and the original high lower becomes kappa-mu when positive. Thus
the response amplification factor changes too; the original144 cannot
be reused indiscriminately. At mu=1/10, the recomputed factor is<192.
Genuine positive-level and differential crossings remain compatible with
this conditional error theorem; it cannot certify positivity of an
uncomputed gate or turn shifted contact into original contact.

The validator rechecks the exp(2B)<9 enclosure, coefficient intervals,
both physical tail bounds, parity D norm sums, normalization payment,
the ORIGINAL complete response/error constants and the shifted factor.
All41 new exact checks pass; no historical chain total is added.
No native high inverse, signed source column, or actual zeta null is
evaluated. The geometric budget is now explicit, but eta_other and the
finite signed lower mu in (8) remain unknown. Whole-domain positivity
stays21/20; the enriched gate, collective frame bound, RH/F4 and Lean
closure remain open.
