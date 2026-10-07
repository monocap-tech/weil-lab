# RPB108 Gaussian action moment terminology

First load-bearing use: GAUSSIAN_ACTION_MOMENT_20261006. Historical wording is preserved.

- **Integer signed Gaussian action**: a_n(h)=Re A_a(h; conjugate(K_n*h)), with the unchanged physical h, the actual frozen multiplier and the Hermitian pole.
- **H1 action weight**: v_n=n^(3/2)/log(e+n), n>=2. It accounts for the width sqrt(n) of the project Gaussian and the native logarithmic multiplier.
- **Positive action moment**: S_+(h)=sum_{n>=2} v_n max(a_n(h),0), allowing infinity. It observes the positive Fourier tail; it is not a boundary inverse moment.
- **One-sided derivative energy**: J_+(h)=integral_{xi>0} xi^2 |Fourier(h)(xi)|^2 dxi.
- **Two-tail action criterion**: finiteness of S_+(h) and S_+(Jh), where Jh(x)=h(-x). Reflection changes the physical vector; it is not enlarged-null transport.
- **Real-kernel action target**: finite action moment for a real basis of a hypothetical full actual nonnegative kernel. This remains an unproved arithmetic input.
