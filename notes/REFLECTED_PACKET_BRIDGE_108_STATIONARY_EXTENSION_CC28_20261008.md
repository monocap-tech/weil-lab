# RPB108 CC28: stationary translation and analytic extension test

2026-10-08 UTC. Coupled parent CC27
`8ab98d8e1086ba8809460cfbdca3851ee2893336`; paused Global NF71
`6ed350cb6736993fa9801bce9ab15f096c10c200`.
[Definitions](../docs/TERMINOLOGY_RPB108_STATIONARY_EXTENSION.md).

The mechanism investigated is whether exact simultaneous translation
invariance and old-domain positivity determine the mixed translation
correlations sufficiently to control outward critical leakage. There is
an actual new analytic obstruction: for every NONZERO compact physical
vector in the canonical logarithmic domain, the native stationary
correlation is not real analytic at zero. Thus analytic continuation
cannot identify its prescribed extension with a positive-definite one.
The conclusion does not exclude other quantitative arithmetic mechanisms.

## 1. Exact stationarity retains all arithmetic terms

Use tau_r h(x)=h(x-r). The complete divisor pair law from CC21 preserves
its signed metric, and hence

    Q(tau_r h,tau_r f)=Q(h,f).                              (1)

This also follows directly from the native arithmetic expression:
the archimedean multiplier and prime translations commute with tau;
exponential moments transform as m_+(tau_r h)=exp(r/2)m_+(h) and
m_-(tau_r h)=exp(-r/2)m_-(h). Their CROSS products in the two mixed slots
are unchanged. Any additional prime powers in a larger cutoff have
zero overlap in the smaller translated support configuration. The
right-limit cutoff and both orientations are retained. The canonical
Fourier norm is translation-unitary; no H1 premise is introduced.

Let h_i be the generalized old critical lifts from CC20, with orthonormal
positive images and delta_i=1-lambda_i. Then

    Q(h_i,h_j)=delta_i times Kronecker(i,j).

For C_ij(r)=Q(h_i,tau_r h_j), two commonly translated copies of this
critical family have the same signed diagonal matrix G. But (1) does
not control C(r). If their combined translated span is positive, its
block Gram is

    [G C(r); C(r)* G] >=0,

which implies ||G^(-1/2) C(r) G^(-1/2)||<=1. Invoking that positivity
on the enlarged domain would assume the sign to be proved. This finite
translated span is only a necessary test; it does not replace the whole
incoming covariance or CC21's whole-domain two-window generation.
The actual forced row on a translated lift still is

    J_i(tau_r h_j)=C_ij(r)-delta_i<P h_i,P tau_r h_j>.       (2)

Equal translated diagonal energies cannot bound the mixed matrix in (2).

## 2. Exactly where the local positive-definite theorem applies

If h has support in [-c,c] with c<s, every translate with center in
I=(-s+c,s-c) belongs to D_s. For any finite centers r_j in I and
coefficients a_j, old positivity gives

    sum conjugate(a_j) a_k q_h(r_k-r_j)
       =Q(sum a_j tau_rj h,sum a_k tau_rk h)>=0.            (3)

Here q_h(r)=Q(h,tau_r h) is continuous by form continuity and translation
continuity in the canonical domain. Equation (3) is local positive
definiteness on the difference interval I-I. The external scalar
extension theorem applies to this continuous correlation, not directly
to an unsmoothed singular native kernel or automatically to a matrix
kernel of the full moving critical family.

For a mode supported up to both old endpoints, the certified center set
may contain only0. No uniform positive support margin has been proved
for the actual near-critical family. Approximating an old mode by inward
smooth tests gives qualitative convergence, not a defect-scaled uniform
error or cap-only translation interval. No such approximation rate is
assumed here.

A positive-definite extension of the local correlation is an EXISTENCE
object. The actual larger-support arithmetic correlation is prescribed.
Agreement on I-I does not identify these two objects. The new theorem
below rejects a proposed analytic identification, rather than claiming
that every extension must be nonunique.

## 3. Actual native nonanalyticity theorem

Fix a finite B, a nonzero h in D_s with s<B, and the exact frozen symbol

    b_B(xi)=Re psi(1/4+i*pi*xi)-log pi
           -sum_{log n<=2B} [2Lambda(n)/sqrt(n)] cos(2pi xi log n).

Define for every real r the diagnostic frozen correlation

    q_h^B(r)=integral b_B(xi)|Fourier h(xi)|^2 exp(-2pi i xi r) dxi
        +exp(r/2) conjugate(m_-(h)) m_+(h)
        +exp(-r/2) conjugate(m_+(h)) m_-(h).                (4)

Its Fourier integral is absolutely convergent, because h has finite
logarithmic energy and |b_B| is bounded by a constant times
log(e+|xi|). On |r|<B-s it equals the ACTUAL native Q(h,tau_r h).
For larger r the finite cutoff in (4) is frozen and is not presented
as the full larger-cap explicit formula.

**Theorem.** q_h^B is not real analytic at r=0 for any nonzero h as above.
This is an analytic theorem about the actual native multiplier; it
requires neither RH nor an assumption on its critical spectrum.

Proof. The digamma asymptotic gives

    Re psi(1/4+i*pi*xi)-log pi =log|xi|+o(1)

as |xi| tends to infinity. The finite prime sum is uniformly bounded.
Choose R so b_B(xi)>=1 for |xi|>R. The high-frequency measure

    dmu(xi)=1_{|xi|>R} b_B(xi)|Fourier h(xi)|^2 dxi         (5)

is finite and NONNEGATIVE. The low-frequency Fourier integral in (4)
is entire: its finite signed measure has bounded spectral support.
Both pole exponentials are entire. Thus if (4) were real analytic at0,
the Fourier transform of (5) would be real analytic there as well.
No cancellation of a high positive tail by these entire pieces can
remove its nonanalyticity.

We prove the positive-measure implication used at this point. Let mu
be any finite nonnegative measure and H(t)=integral exp(-2pi i xi t)dmu.
If H is real analytic at0, choose C,L>0 with

    |H^(m)(0)|<=C m! L^(-m), m>=0.

For n>=1 the exact centered finite-difference identity is

    integral [2 sin(pi xi t)]^(2n) dmu
       =(-1)^n sum_{j=0}^{2n} (-1)^j binomial(2n,j)
                                            H((n-j)t).   (6)

Divide by t^(2n) and use analyticity on the finite right sum. All lower
Taylor coefficients cancel and its limit is (-1)^n H^(2n)(0).
Fatou's lemma on the nonnegative left side yields

    integral (2pi xi)^(2n) dmu
          <=(-1)^n H^(2n)(0)
          <=C (2n)! L^(-2n).                             (7)

These finite moments also justify differentiating under the integral,
so the first inequality is equality, although the upper bound is enough.
For 0<epsilon<L, Tonelli applied to the nonnegative cosh series gives

    integral cosh(2pi epsilon xi) dmu
        <=C sum_{n>=0}(epsilon/L)^(2n)<infinity.

Since exp(2pi epsilon |xi|)<=2cosh(2pi epsilon xi), mu has an exponential
moment. Applying this to (5) and using b_B>=1 on the tail gives

    integral exp(2pi epsilon |xi|)|Fourier h(xi)|^2 dxi
                                                        <infinity. (8)

The bounded-frequency part of (8) is finite automatically. Cauchy-Schwarz
now makes the inverse Fourier integral for h absolutely convergent and
holomorphic in every narrower strip |Im z|<epsilon/2. It gives a
continuous analytic representative agreeing with h in L2. That
representative vanishes on a real open interval outside the compact
physical support: equality almost everywhere and continuity give
pointwise vanishing there. The identity theorem forces it to be zero
throughout the strip. Thus h=0, a contradiction. This proves the theorem.

Every nonzero actual generalized critical lift is a compact physical
canonical-domain vector, so the theorem applies to its q_h^B. It also
applies to ordinary positive physical eigenmodes and smooth compact
pulses. It says NOTHING about the separate height moments of the
negative-source critical coordinates; no such identification is made.
Finite critical output rank cannot make these native correlations
analytic or give them a compactly supported representing measure.
The conclusion remains true after any finite physical level shift:
that shift changes b_B by a constant and leaves the high-tail argument
unchanged.

This is not a restart of the earlier endpoint-regularity investigation.
No regularity of an actual mode is derived or imposed; analyticity is
assumed only to disprove this specific extension mechanism.

## 4. A genuine crossing gives the exact mixed correlation failure

Use the inherited differential form q(h)=||h'||^2-||h||^2 on
H0^1(-s,s). Put k=pi/(2s)>1 and normalize the compact ground lift by

    h_s(x)=cos(kx)/(k sqrt(s)), |x|<s; zero otherwise.

Then ||P h_s||=1, lambda=1/k^2 and delta=1-lambda.
For 0<r<2s the unnormalized autocorrelation is exactly

    A_s(r)=(s-r/2) cos(kr)+sin(kr)/(2k).

Weak integration by parts, or the derivative correlation, gives
q(h_s,tau_r h_s)=(-A_s''(r)-A_s(r))/(k^2 s). No boundary mass term
is deleted: h_s is H1 but its derivative has endpoint jumps, which
produce the right-hand linear cusp in this correlation.
Set u=2s/pi=1/k. The exact normalized formula is

    q_u(r)=(1-u^2)(1-r/(pi u)) cos(r/u)
                         -(1+u^2)/pi sin(r/u).            (9)

q_u(0)=delta, and by stationarity both translated diagonals equal delta.
For a fixed positive r, however,

    lim_{u->1} q_u(r)=-(2/pi)sin r.

Thus the two-vector signed Gram can fail positivity even though each
translated vector has the same small positive diagonal energy.
This is a physical translation control with the actual old generalized
ground lift, not a declared two-column source model.

For exact rational inequalities, take u=1-2^(-j), j>=8, and r=u/16.
Then r tends to1/16 and remains at least1/32. The elementary bounds
3<pi<22/7 and sin(1/16)>=1/16-(1/16)^3/6 imply

    q_u(r)<=delta-(1+u^2)(7/22)[1/16-(1/16)^3/6]<-1/100.

Also delta<1/128. Hence |q_u(r)|>delta and the two-vector Gram has
a negative eigenvalue, with its relative mixed cost growing without
bound as the old defect shrinks. The target supports fit in the single
finite cap B=2. The target is not assumed already positive. This
control rules out a structural inference from stationarity and old
positivity; it does not reproduce the actual zeta arithmetic.

For a smooth packet strictly inside an old positive differential
window, its local translation correlation DOES satisfy (3). A positive
extension exists by the scalar theorem. Its prescribed whole-line
continuation nevertheless need not be positive definite: for any such
nonnegative nonzero packet, its Fourier representing signed density
is ((2pi xi)^2-1)|Fourier h(xi)|^2, negative near xi=0. Bochner's
uniqueness for finite measures forbids a globally positive-definite
actual continuation. Thus an available positive extension must differ
from that continuation. This supplies a genuine operator discriminator
for the identification step.

## 5. Complete positive-level discrimination

For the differential model shift the ORIGINAL form by physical level
mu=9/16. The full negative analysis is (h,(3/4)h), with total potential
25/16. Its first shifted contact is s=2pi/5, where the ORIGINAL lowest
physical eigenvalue is9/16>0. For a P-normalized ground lift, the
original q(h)=9/25 and the shifted q_mu(h)=0. Both forms are exactly
translation invariant; stationarity alone cannot distinguish them.
The additional physical mass correlation must be retained in every
mixed translated entry, not only at the diagonal.

The inherited finite full-mass control P=I, N=(9/25,12/25) is replayed
independently: original whole budget9/34<1; shifting by16/25 adds the
ENTIRE (4/5)I channel, giving shifted critical plus low budget1. No
shifted null vector is classified as original nullity. The nonanalyticity
theorem also survives finite mass shifts, so it is a mechanism obstruction,
not an original-nullity discriminator or an RH criterion.

## 6. External transfer theorem and exact scope

[Jorgensen--Niedzialomski](https://arxiv.org/pdf/1212.3047),
arXiv:1212.3047v3, 2013-12-31, Corollary7.9: a scalar continuous locally
positive-definite function on the difference of a bounded real interval
has a globally positive-definite extension. Theorem7.11 gives uniqueness
if an extension has compactly supported representing measure. Neither
statement identifies a prescribed arithmetic continuation. We use the
scalar theorem only after smoothing by a supported physical packet;
no distribution or matrix extension theorem is asserted. Nonanalyticity
does not prove nonuniqueness under all other possible uniqueness criteria.

[NIST DLMF5.11.2](https://dlmf.nist.gov/5.11.E2), checked2026-10-08,
is the inherited digamma sector asymptotic, verified on the actual
vertical ray used here. It gives eventual positivity of b_B; no
numerical cutoff R or new global zeta bound is evaluated. The finite
positive-measure lemma and native nonanalyticity theorem are proved
above, not attributed to the extension paper.

24,748 exact checks pass: 144 new checks and 24,604 inherited CC27 checks.
The validator checks exact finite-difference cancellations, the crossing
correlation derivative formula, rational outward-crossing inequalities
and full shifted mass normalization. It replays all24,604 CC27 checks.
These checks do not certify Fatou, holomorphic extension, Krein's theorem
or actual critical correlations in Lean. No actual moving critical Gram
or J M_t^-1 J* is numerically evaluated.

The required independent arithmetic estimate remains

    J M_t^-1 J*<=q Lambda G,
    compatible low budget ell, q+ell<1,

with cap-only constants and non-stalling steps for the all-cap objective.
The positive extension theorem supplies none of that prescribed-covariance
control. Exact stationarity gives equal signed diagonal blocks; the
missing input is still their mode-dependent joint correlations and whole
incoming coverage. No full-identity independence or impossibility theorem
is claimed. No new aperture, RH/F4, retained attachment, reusable
continuation, accumulated finite-cap loss or Lean closure.

Original anchor stays21/20 even0/odd0, joined physical margin1/(3*10^63),
not a numerical source defect. Publication is additive on Coupled alone;
Global, Aperture and Pre-Contact Shadow remain paused. The analytic
positive-extension identification shortcut stops here.
