# RPB108 DNE11 — Exact polynomial-log native source split and certified analytic-tail budget

**DNE11** is the physical-source Gram investigation following DNE10's exact Q-to-H pole transfer. It is not a new full-space sign certificate.

For supported finite polynomials p on I=(-a,a), the COMPLETE original signed Weil source is

    s_Q(p)(x)=s_arch(p)(x)
       -sum_(ell_n<=2a) c_n [p_tilde(x+ell_n)+p_tilde(x-ell_n)]
       +exp(x/2)m_-(p)+exp(-x/2)m_+(p),

with c_n=Lambda(n)/sqrt(n), ell_n=log n and m_±(p)=int_I p(y)exp(±y/2)dy. Both prime shift orientations and both Hermitian pole terms are retained; the pole-free source removes ONLY the last two exponential terms.

**Endpoint singularity separation.** Define

    r(t)=exp(t/2)/(2sinh t)-1/(2t), t>0, r(0)=1/4,
    D[p](x)=(1/2)int_I (p(x)-p(y))/|x-y|dy.

Then D[p] is a polynomial and the EXACT physical archimedean source is

    s_arch(p)(x)
      =-(gamma_E+log(2pi))p(x)
       -(1/2)p(x)log(a²-x²)
       +D[p](x)-int_I r(|x-y|)p(y)dy.

The endpoint logarithm is exact and left untruncated. The remaining integral kernel is analytic for |t|<pi and smooth over the entire a=53/50 distance interval.

**Exact Taylor coefficients.** Set q(t)=t*exp(t/2)/(2sinh t), q(0)=1/2, with rational Taylor coefficients q_k determined recursively by

    q_n=1/(2^(n+1) n!)-sum_(k=1..floor(n/2)) q_(n-2k)/(2k+1)!.

The degree N-1 polynomial r_N(t)=sum_(k=1..N) q_k*t^(k-1) has strictly rational coefficients. For rational aperture a, K_N[p](x)=int_I r_N(|x-y|)p(y)dy is a polynomial in x with rational coefficients whenever p has rational coefficients.

**Effective analytic bound at a=53/50.** On |z|=R=5/2 one has |q(z)-1/2|<11 (using |sinh z|>1/2 and exp(5/4)<4). At max distance 2a=53/25, ratio 2a/R=106/125. Cauchy's estimate gives for all 0<=t<=2a,

    |r(t)-r_N(t)| <=delta_N=(550/19)*(106/125)^N.

The exact integer comparison yields delta_600<10^-40. The corresponding operator error from the regular integral kernel obeys

    ||s_arch(p)-s_arch,N(p)||_L2(I)
       <=(2a)*delta_N*||p||_2
       <3*10^-40||p||_2 at N=600.

This is an L2 OPERATOR-NORM bound independent of polynomial degree and of the number of finite high Legendre correction modes. It is NOT a bound on the native signed source itself or on the full high residual.

**Complete source Gram:** For any finite physical-polynomial family w_i let S_i=s_Q(w_i), S_i,N=s_Q,N(w_i). The exact high physical residual Gram is

    P_ij = int_I S_i(x)S_j(x)dx
            -sum_(e_k in E_parity)Q(w_i,e_k)Q(w_j,e_k).

Every original native low pairing in the subtraction must be paid; one may NOT replace P by a finite sampled-high Gram. The truncated Gram is computable from explicit piecewise polynomial, polynomial-times-log and exponential pieces, including all source cross terms. If W maps finite coefficient vectors to physical w and eps=(2a)delta_N||W||, the L2 source Gram operator error satisfies

    ||S*S-S_N*S_N|| <=eps*(2||S_N||+eps).

The finite remaining integral and its rigorous quadrature/interval evaluation have NOT been executed yet. DNE11 supplies the effective analytic-tail budget and finite elementary-integral reduction, not a positive DNE9 Schur or reflected gate.
