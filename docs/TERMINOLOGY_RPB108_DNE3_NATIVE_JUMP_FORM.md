# DNE3 — Complete native Lévy/jump representation and scalar threshold

**Native archimedean symbol** a_arch(xi)=Re psi(1/4+i*pi*xi)-log pi. Its zero-frequency value is a0=psi(1/4)-log pi=-gamma_E-pi/2-3 log2-log pi.

**Native jump density** j(d)=exp(-|d|/2)/(1-exp(-2|d|)), d nonzero, strictly positive and even. The digamma increment has EXACT multiplier identity a_arch(xi)-a0=int_R j(d)[1-cos(2*pi*xi*d)]dd (DLMF 5.9.16). j(d) is approximately 1/(2|d|) near zero and integrable at infinity.

**Active arithmetic jump coefficients** c_n=Lambda(n)/sqrt(n), ell_n=log n, S_a=sum_(ell_n<=2a)c_n, retaining all active prime powers and both physical translation orientations.

**Native positive jump form** for zero-extended h supported [-a,a]:

    J_a(h)= (1/2) int_R j(d) ||h-tau_d h||_physical² dd
              + sum_(ell_n<=2a)c_n ||h-tau_(ell_n)h||_physical².

The entire supported canonical logarithmic domain D_a is the form domain of J_a. It is NOT only a smooth core identity.

**Exact original pole-free decomposition**:

    H_a(h)=J_a(h)-kappa_a ||h||_2²,
    kappa_a=log pi-psi(1/4)+2 S_a
           =gamma_E+pi/2+3 log2+log pi+2 S_a.

The signed original poles must be restored to recover Q_a. No additional prime term, boundary term, or physical mass is inserted.

**Native exterior killing density** for the continuous jump part:

    k_a(x)=int_(a-x)^infty j(t)dt+int_(a+x)^infty j(t)dt,
    |x|<a.

The zero extension is essential: J_a contains the continuous exterior contribution int_-a^a k_a(x)|h(x)|²dx and prime exterior jump contributions. Dropping these terms would change the supported operator.

**Odd crude coercivity floor**:

    F_odd(a)=2 int_a^infty j(t)dt+
                2 int_a^(2a) j(t)dt+
                  sum_(ell_n<=2a) c_n/N_n(a)²,
    N_n(a)=floor(2a/ell_n)+1.

For odd h, J_a(h)>=F_odd(a)||h||_2². This sufficient lower bound is not equal to the lowest odd jump eigenvalue, and strict F_odd>kappa is only a sufficient route to H_a^odd>0.

**DNE3 classification:** full unweighted jump-form identity, not a global full weighted ground-state quotient representation. DNE2's global weighted semigroup is separate. Full weighted integral-form core transfer remains open.
