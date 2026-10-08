# Prime–pole discrepancy (RPB108 NF56)

For angular-frequency convention F_h(eta)=integral h(x) exp(i eta x) dx, set C_h(s)=integral h(y+s) conjugate(h(y)) dy and c_h=Re C_h. A vector supported in [-a,a] has C_h supported in [-2a,2a].

The **prime–pole discrepancy measure** on s>=0 is

    dV(s)=sum_(n>=2) Lambda(n)/sqrt(n) delta_(log n)(ds)
           -exp(s/2) ds.

Its right-continuous cumulative function is

    V(s)=sum_(log n<=s) Lambda(n)/sqrt(n)-2(exp(s/2)-1).

Only its restriction to a finite support window is paired with C_h. Lambda is the actual von Mangoldt function: log p on powers of a prime p and zero otherwise. V is a scalar cumulative discrepancy, not a source gain, a Fourier-positive measure, or a physical null vector.

The **discrepancy form** is R_a(h)=-2 integral_[0,2a] c_h(s) dV(s). This Stieltjes expression is defined on the canonical domain without differentiating h. For a smooth compact test it also equals 2 integral_0^(2a) V(s)c_h'(s) ds. The latter formula does not supply a derivative norm bound on the whole canonical domain.
