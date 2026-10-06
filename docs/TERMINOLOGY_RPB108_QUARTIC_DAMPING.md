# RPB108 terminology: quartic positive-region Bessel damping

- **Normalized regular solution:** F_n(x)=(2n+1)!! j_n(x)/x^n, extended by F_n(0)=1. Its positivity on 0<=x<=sqrt(n(n+1)) is inherited from the proved spherical-Bessel differential equation argument, for n>=1.
- **Logarithmic derivative:** y_n=-F_n'/F_n. Set p=2n+2, A=1/(p+1), B=A^2/(p+3). The exact equation y_n'+p*y_n/x=1+y_n^2 and the already proved bound y_n>=A*x imply y_n>=A*x+B*x^3 by direct integration.
- **Quartic squared damping:** F_n(x)^2<=exp(-z_n-w_n), where z_n=x^2/(2n+3) and w_n=x^4/[2(2n+3)^2(2n+5)].
- **Integrated quartic rate:** for Y=2*pi*a*T, r_n=2n+1-2*z_n(Y_upper)-4*w_n(Y_upper). Its positivity is checked explicitly. The degree contribution is bounded by 4aT*(2n+1)*Y_upper^(2n)*E_n/[r_n*((2n+1)!!)^2], where E_n bounds exp(-z_n(Y_lower)-w_n(Y_lower)) from above.
- **Complete mass:** retain a finite block of degrees individually and include the existing undamped bound for every remaining degree. No tail degree is discarded.
- **Application scope:** fixed aperture 9/10 with retained dimension 84. A fresh complement and corrected Schur certificate are required before declaring whole-domain positivity.

This is an additive strengthening of the earlier quadratic damping proof, not a change to historical certificates.

- **Candidate 9/10 parameters:** k=84, T=27/2, retained damped degrees 84–131, complete undamped tail from degree 132, physical c=31/50 and beta=50/31; independent logarithmic complement remains 9/100.
- **Corrected sign and conversion:** certify Q84-beta*Rhat84-(beta*delta+tau)I>0 on the pinned matching inputs. With lift norm bound J, use mu=tau*c/[tau+c(1+J^2)] and kappa=mu/[10(mu+23)]. These are claims only after fresh exact verification.

- **Stronger candidate:** after the c=31/50 pivot test failed, use T=69/5, c=627/1000 and beta=1000/627, with the same 48 individually damped degrees and complete tail. The earlier failed pivot test is not a full-form negative certificate.
