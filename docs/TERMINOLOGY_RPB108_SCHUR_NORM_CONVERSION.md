# RPB-108 Schur norm conversion terminology

- **Inherited Schur inputs:** the previously certified corrected finite margin tau=10^(-29), physical complement lower bound c=51/100, and physical lift norm bound L=10 at aperture 81/100. This pass pins the archived proof note, validation manifest and logarithmic bridge note by Git blob hash; it does not rerun their full Gram construction.
- **Lifted remainder:** z in the physical complement, with h=s+z-Ts, s in the matching finite span and ||T||<=L. The existing Schur argument gives Q(h)>=tau||s||^2+c||z||^2.
- **Norm conversion coefficient:** mu=tau*c/[tau+c(1+L^2)]. It is a sufficient whole-domain physical lower bound derived from those inherited inputs, not a new corrected matrix margin.
- **Conversion matrix:** the real symmetric 2x2 matrix with entries tau-mu(1+L^2), -mu L, c-mu. Its positive semidefiniteness certifies the scalar norm conversion.
- **Updated logarithmic coefficient:** kappa=mu/[10(mu+23)], using the previously certified actual inequality Q>=(1/10)Elog-23||h||_2^2.

New physical coefficient: 51/(5151*10^29+100).
New logarithmic coefficient: 51/[10(118473*10^29+2351)].
The numerical aperture frontier stays 81/100; historical attachment, global endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain open.
