# RPB108 terminology: finite integrated logarithmic-derivative iteration

- **Positive region:** n>=1, 0<=x<=sqrt(n(n+1)), with F_n=(2n+1)!!j_n(x)/x^n positive as proved previously. Put p=2n+2 and y=-F_n'/F_n.
- **Iteration polynomial:** P_0(x)=x/(p+1); define P_(r+1)(x)=x^-p*integral_0^x t^p*(1+P_r(t)^2)dt. Every coefficient is nonnegative and y>=P_r by induction from the exact integral equation for y.
- **Squared damping polynomial:** H_r(x)=2*integral_0^x P_r(t)dt. Then F_n(x)^2<=exp(-H_r(x)). Depth one is exactly the earlier quartic bound; depth two retains terms through x^8 and depth three through x^16.
- **Integrated rate:** if H_r(x)=sum_j h_j*x^(2j+2), use rate=2n+1-sum_j (2j+2)*h_j*Y_upper^(2j+2), and attenuation exp(-H_r(Y_lower)). Positive region and every rate must be checked separately.
- **Complete mass and aperture scope:** every retained degree is integrated individually and the complete undamped infinite tail is added. These are fixed-aperture bounds, never an unverified uniform attenuation over varying apertures.
- **Farther preflight aperture:** 23/25, physical lengths d=46/25 and L=92/25, retained dimension 84. Active prime powers remain 2,3,4,5; generated actual translation panels and prime chains must be freshly checked. Complement-only success leaves matching native/source/Gram/sign obligations open.

All historical certificates and terminology remain unchanged.

- **Outward numerical application:** round the damping exponent and integrated rate down on the 80-digit grid before using them; positive exponential partial sums and every mass term are enclosed outward. Decreasing either positive input increases the mass bound.
- **Next matched target:** 91/100, T=69/5, depth three, candidate physical c=317/500 and beta=500/317. A farther complement-only check at 23/25 uses T=137/10, depth three, c=623/1000 and beta=1000/623. Both retain degrees 84–131 plus the complete undamped tail from 132.
- **Prospective constructor ceilings:** at 91/100, L=91/25 and d=91/50; exp(L)<39 and L/(1-exp(-L))<5L/4=91/20. At 23/25, exp(L)<40 and the corresponding kernel ceiling is 23/5. The actual source alternating-kernel ceiling remains 9/4 at both apertures. These checked constants prepare, but do not certify, the future full native/source constructors.
