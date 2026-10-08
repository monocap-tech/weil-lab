# Canonical prime smearing (RPB108 NF57)

Use the original Fourier convention hhat(xi)=integral h(x)exp(-2pi i xi x)dx and E_log(h)=integral log(e+|xi|)|hhat(xi)|²dxi. The physical correlation is C_h(s)=integral h(y+s)conjugate(h(y))dy; c_h=Re C_h.

At fixed aperture a, the active dictionary consists of ALL prime powers with log n<=2a, including equality. Its **prime budget** is S_a=2 sum_active Lambda(n)/sqrt(n).

The **width-delta smeared form** Q_(a,delta) retains the exact archimedean and original pole forms and replaces each active prime correlation c_h(log n) by (1/(2delta))integral_(-delta)^delta c_h(log n+u)du. Zero-extended physical correlations are used, including beyond the support edge. This is an approximation to the original form, not a changed actual divisor or a new null equation.

The **canonical smearing error** is the norm of the Hermitian form Q_a-Q_(a,delta) on the canonical logarithmic carrier, measured relative to E_log. Any positive-eigenmode mass shift is separate and retained in both forms.
