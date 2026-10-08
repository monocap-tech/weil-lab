# RPB108: exact physical translation mass and normalized opening branches

2026-10-07. Recovered head 401f6b3970280a79da974661cbb806b78b4ea1ca. Definitions: [physical translation scale](../docs/TERMINOLOGY_RPB108_PHYSICAL_TRANSLATION_SCALE.md). Conditional actual analytic theorem, not Lean-certified.

## Result

For every actual contact vector h with nonzero right trace c, the complete native correlation and balanced strong endpoint traces give

    V_mass(R)=O_h(1/[R log R]),
    D_mass(t)~|c|^2 t/log(1/t).                       (1)

In particular ||tau_t h-h||_2^2~2|c|^2 t/log(1/t). The leading physical mass of the translation difference is exhausted by the two strips outside the support overlap; its mass inside the overlap is o(t/log(1/t)). This sharpens the previously proved D_mass=o(t), without imposing a pointwise endpoint asymptotic.

Choose the real definite-parity terminal chain vector h, let m=||h||_2^2, and C(t)=Q(h,tau_t h). The exact TWO-VECTOR physical compression has

    lambda_sum(t)=C(t)/(2m-D_mass(t))
                  ~-|c|^2 t/(2m),
    lambda_difference(t)=-C(t)/D_mass(t)
                  ~log(1/t).                        (2)

Thus the negative direction opens linearly while the other compressed direction has large positive Rayleigh quotient. The coefficient Gram's eigenvalues are both order t; physical normalization changes one branch dramatically. No full enlarged spectral asymptotic or arithmetic exclusion is asserted.

## 1. Recover the logarithmic Fourier translation defect

Write L=log(1/t). The pinned actual null correlation gives C_h(t)=-|c|^2 t+o(t). The full native translation identity, including the actual bounded pole defect, gives

    D_m(t)=|c|^2 t+o(t),
    |D_w(t)-D_m(t)|<=C_a D_mass(t).                (3)

The second inequality is the registered finite envelope |m_a-w|<=C_a, with all fixed-aperture primes included. No pointwise sign of the low-frequency native symbol is needed. The prior NULL_ABEL_LOG_SLOPE argument has already proved D_mass=o(t), including its actual shifted positive-eigenmode counterpart. Hence

    D_w(t)=|c|^2 t+o(t).                            (4)

The subsequent argument uses this POSITIVE logarithmic Fourier defect. It does not substitute a signed source tail or assume an unregularized first-height moment.

## 2. Averaging gives the improved physical Fourier tail

For all sufficiently small t, D_w(t)<=A_h t with finite A_h. Tonelli on the nonnegative Fourier measure gives

    R integral_0^(1/R) D_w(t)dt
      =integral [1-sin(2pi xi/R)/(2pi xi/R)]
                             w(xi)|hhat(xi)|^2 dxi
      <=A_h/(2R).

For |xi|>R the bracket is at least 1-1/(2pi)>1/2. Therefore W_tail(R)<=A_h/R for sufficiently large R. Since w(xi)>=log R on that region,

    V_mass(R)<=A_h/[R log R].                      (5)

This is a Fourier tail estimate on the same physical vector, not the actual divisor-copy O(1/T) tail from ACTUAL_SHARP_LOG_LIMIT. No actual zero counting or new external Tauberian theorem is used.

## 3. The physical low-frequency second moment admits a sharper bound

Let H(R)=integral_(|xi|<=R)xi^2|hhat(xi)|^2 dxi. Nonnegative layer-cake gives

    H(R)<=integral_0^R 2u V_mass(u)du
          =O_h(R/log R).                           (6)

The initial interval contributes a finite constant. Above a fixed large cutoff use (5). To bound integral du/log u, split at sqrt(R); its lower part is O(sqrt(R)) and its upper part is at most 2R/log R. This verifies (6) with elementary estimates. It does not claim a finite full derivative moment.

Fix ANY 0<alpha<1 and split at R=t^(-alpha). On the lower band, 1-cos(2pi xi t)<=2pi^2 xi^2 t^2 and (6) imply

    D_mass,low(t)=O_h,alpha(t^(2-alpha)/L)=o(t/L).

On the upper band w>=alpha L, so (4) gives

    D_mass(t)<=D_w(t)/(alpha L)+o(t/L),
    limsup_(t down to0) L D_mass(t)/t<=|c|^2/alpha.

Send alpha upward to one AFTER taking the limsup. This improves the older crude physical-mass split, which only allowed alpha<1/2. It proves the sharp upper coefficient <=|c|^2 without a rate-uniform limit in alpha.

## 4. Endpoint strips force the matching lower coefficient

The translated and original supports have two disjoint nonoverlap strips. On the right strip the difference equals a translated copy of h; on the left it equals -h. The established strong rescaled L2 traces and balanced trace Gram give

    integral_0^t |h(a-v)|^2 dv~|c|^2 t/L,
    integral_0^t |h(-a+v)|^2 dv~|c|^2 t/L.

These two masses alone contribute 2|c|^2 t/L to ||tau_t h-h||_2^2. Since D_mass is half that norm, the liminf of L D_mass/t is at least |c|^2. Together with section3 this proves (1).

Subtracting the two strip masses from the full norm shows that the squared difference on the support overlap is o(t/L). This is an integrated conclusion. No pointwise normalized interior trace, global H1 membership or additional derivative of the rough vector is inferred.

## 5. Exact physical compression for the real terminal vector

The derivative chain admits a real terminal vector of definite reflection parity with c!=0. Translation and the real actual form give real R(t)=<h,tau_t h> and real C(t). The simultaneous-translation law makes both diagonal energies zero and both diagonal masses m. Their matrices are therefore

    Q_matrix=[[0,C],[C,0]],
    M_matrix=[[m,R],[R,m]], R=m-D_mass.

The sum and difference vectors are orthogonal for BOTH matrices. Their energies are 2C and -2C, and their squared physical masses are 2(2m-D_mass) and 2D_mass. Thus their Rayleigh quotients are exactly those in (2). Translation continuity makes 2m-D_mass positive, and (1) makes D_mass positive for small t, so these are genuine two independent physical directions.

The full two-vector coefficient Gram has eigenvalues C and -C, both order t. Its physical mass-normalized eigenvalues behave differently: the sum branch is negative of linear size; the difference branch divided by log(1/t) tends to ONE. This universal coefficient follows from the same actual trace in the energy and physical mass asymptotics. The small-mass difference branch does not provide an additional low negative eigenvalue.

Simultaneously center both vectors by -t/2 to fit aperture a+t/2, preserving all pairings. The negative branch reproduces the one-sided opening trial from NF51. The positive branch is only a compression value; it does not bound a particular full-operator positive eigenvalue from below or assert an enlarged spectral gap.

## 6. Shifted control and standing

For the actual lowest positive eigenspace at level mu, the pinned argument gives D_mass=o(t), and the pole/native defect has D_m=mu D_mass+|c|^2 t+o(t). Thus (3)-(4) and all subsequent estimates remain valid for the same physical vector. For its real terminal choice, C_mu(t)=Q_mu(h,tau_t h)=-|c|^2 t+o(t).

The original actual compression is Q_mu_matrix+mu M_matrix. Its physical eigenvalues are

    mu-|c|^2 t/(2m)+o(t),
    mu+log(1/t)[1+o(1)].

The finite mass residual is retained, and the first branch need not be negative when mu>0. The estimates therefore discriminate the physical normalization issue, not the unshifted arithmetic contact gate.

The same-vector physical tail and exact mass scale now supply quantitative custody for translated trials. They do not create an actual contact at a certified aperture or exclude possible contact beyond it. Signed sharp-head arithmetic, global endpoint exclusion, F4 and full transport remain open. Whole-domain positivity through aperture one and historical work remain preserved.

## Validation and provenance

The finite checker validates averaging/tail budget constants, the layer-cake second-moment inequality on independent rational measures, two-strip factors, generalized two-vector eigenvalue formulas, and the shifted mass residual. It does not certify analytic limits or compute actual Fourier/source nodes. Those arguments above use pinned trace, actual correlation, logarithmic envelope and translated-kernel results. No new external theorem, Lean file/build or axiom is introduced.
