# NF466 — Original J7 correlated signed-moment operator

**Standing: ACCEPTED algebraic identity / PROVISIONAL numerical route; no original macroscopic signed integral certified.** Parent NF465 draft PR #493, original NF407 246-source SHA `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`; original NF406 seam SHA `c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675`. Canonical W-ODD-NEG remains OPEN.

## Exact reduction of signed panel to mean, covariance and variance

Take the genuine NF464 panel I=[26/25,53/50]=[1.04,1.06], L=1/50. The physical original J7 principal is p(x)=v(C7+(1/2)log[B/(B-x)]), B=11/10, v<0. The original regular response z is the complete NF446 compact-source joint arch kernel, the original six J7 minus regular prime-power shifts n=2,3,4,5,7,8, and the exact NF404 centering.

Define the **actual source-dependent** means
[
\bar z=L^{-1}\int_I z(x)dx,\qquad
\bar p=L^{-1}\int_I p(x)dx,
]
and fluctuations e=z-\bar z, h=p-\bar p, so \int_I e=\int_I h=0. Exact algebra, with no approximation, yields
[
\boxed{\int_I(4pz+2z^2)dx
=4L\bar p\bar z+2L\bar z^2
+4\int_I he\,dx+2\int_I e^2\,dx.}
]
The final variance is nonnegative. This representation preserves the correlation that independent bounds on pz and z² discard. In particular, a source-certified mean and covariance may give a decision-quality result without pointwise source certification on a 10^-15 mesh.

If an original-source approximation P has sup|z-P|<=eps, the previously derived NF464 error charge remains valid; this identity is an alternate acceptance interface, not a new source enclosure.

## Exact principal moment

Set d=B-x and q(d)=C7+(1/2)log(B/d). With d_left=B-26/25=3/50 and d_right=B-53/50=1/25, an antiderivative is F1(d)=d(q(d)+1/2), since F1'=q. Thus
[
\int_I p(x)dx
=v[F1(3/50)-F1(1/25)].
]
Also \bar p=(1/L) times this exact integral. The principal p is monotone decreasing on I (v<0), so its oscillation is exactly
[
\omega_p=|v|\,\frac12\log\frac{3}{2}.
]
For any source-certified uniform fluctuation bound |e|<=eta on I, the conservative, fully rigorous covariance bound
[
|\int_I he|\le L\,\omega_p\,\eta
]
holds, while 0<=\int_I e²<=L eta². Consequently
[
4L\bar p\bar z+2L\bar z²-4L\omega_p\eta
\le D_I\le
4L\bar p\bar z+2L\bar z²+4L\omega_p\eta+2L\eta².
]
This inequality is conditional on **actual** source-certified \bar z and eta, which are not supplied by NF446's coarse |z|<25000.

## Concrete next numerical obligation

Construct a joint interval evaluator for the original NF446 compact kernel, preserving the same original source coefficient intervals in all evaluations of U, U', regular six-minus shifts, and pole/centering. Integrate z to enclose \bar z, and independently enclose \int_I(p-\bar p)(z-\bar z) and \int_I(z-\bar z)^2 (or certify eta). Use the exact principal moment above. Only then claim a signed macroscopic D_I interval.

**NF466 closes:** exact mean-covariance-variance source-preserving reduction and exact principal panel moment. **Not closed:** numerical \bar z, eta, covariance, variance, D_I, full D7/D8, NF404, W-ODD-NEG, RH.

**Next bold NF467:** implement a genuine source-native compact-kernel interval integration of \bar z over [1.04,1.06], preserving original coefficient correlations; reject a source-free synthetic z or unverified floating-point interval.
