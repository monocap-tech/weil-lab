# RPB108: linear signed-height operator growth and failure of uniform smoothing transfer

2026-10-07. Recovered head 97a3f8348b4bb68bb67b9ad3ab3bd6ced7ab7a71. Definitions: [height limit nonuniformity](../docs/TERMINOLOGY_RPB108_HEIGHT_LIMIT_NONUNIFORMITY.md). Analytic, not Lean-certified.

## Result

At every fixed actual window a>0, the COMPLETE signed first-height forms obey

    c_a T <= N_a(T) <= C_a T for all sufficiently large T. (1)

This is proved using actual smooth modulated packets, the complete source derivative identities, the native logarithmic symbol and all frozen prime/pole corrections. No hypothetical contact is needed for (1). Consequently a global uniform bound on B_T/log T in the canonical norm is false.

At a hypothetical nonzero actual contact, choose h with nonzero terminal trace and same-window smooth v_j->h in D. Then

    lim_j lim_T S_vj(T)/log T =0,
    lim_T lim_j S_vj(T)/log T =eta |kappa_R(h)|^2>0. (2)

The order of these two limits cannot be exchanged. The selected actual-row terminal readout v->kappa_R(C_X v), although bounded in D, is unbounded in the native energy norm on the smooth core. Neither smoothing nor the complete real-node energy model supplies the missing uniform height bound. No arithmetic exclusion estimate is proved.

## 1. Finite-height continuity and the upper bound

Complete actual analysis Gamma:D_a->source is bounded, say by L_a, in the positive source metric. The finite signed height multiplier has norm at most T, so

    |B_T(f,g)|<=T L_a^2 ||f||_D ||g||_D.            (3)

All original pairs, multiplicity copies and normalization factors remain in Gamma. Thus every fixed height is continuous in the same canonical topology in which smooth approximation is lawful. The bound explicitly depends on T.

## 2. High-frequency smooth packets in the complete native form

Fix nonzero psi in C_c^infinity((-a,a)), m=||psi||_2^2>0, and let f_N=exp(-i N x)psi. Set g_N=exp(-i N x)psi'. These stay in the same window. The pinned Fourier convention is F(z)=integral f exp(i z x), so their observations center at +N and f_N'=-i N f_N+g_N.

The canonical symbol is w(xi)=log(exp(1)+|xi|), and the actual quarter-line archimedean symbol satisfies |m0-w|<=C0. Shifting the Schwartz Fourier transform of psi by N/(2pi) gives

    ||f_N||_D^2=m log N+O_psi(1),
    ||g_N||_D^2=O_psi(log N).                       (4)

For clarity, the upper remainder follows from the logarithmic triangle bound and integrability of w times the Schwartz density; on |xi+N/(2pi)|<=N/(4pi), w=log N+O(1)+O(log(e+|xi+N/(2pi)|)), and the complementary Schwartz tail contributes O(1). Plancherel supplies m. Any retained additional bounded physical-mass term in an equivalent canonical norm only changes O(1); the normalization used here is the registered logarithmic Fourier norm.

At fixed a the frozen prime operator is bounded in physical L2, with norm at most the finite sum 2 sum_(log n<=2a) Lambda(n)/sqrt(n). Both actual pole rows are bounded physical L2 functionals. Therefore, with ALL corrections included,

    Q_a(f_N,f_N)=m log N+O_(a,psi)(1).              (5)

This is a high-frequency test calculation, not global positivity or a computed eigenmode. No source row is deleted.

## 3. Centered actual source moments control the truncation error

Use the exact derivative-source identities on f_N and its lawful derivative. In the original pair convention,

    -i(theta_q-N)p_q(f_N)=p_q(g_N)+beta_q n_q(f_N),
    -i(theta_q-N)n_q(f_N)=n_q(g_N)+beta_q p_q(f_N).

With v_q=|p_q(f_N)|^2+|n_q(f_N)|^2 and the pinned finite transverse bound B,

    V_N=sum_q v_q=O(log N),
    M_N=sum_q (theta_q-N)^2 v_q
       <=2[||Gamma g_N||^2+B^2||Gamma f_N||^2]=O(log N). (6)

Both follow from complete canonical sampling and (4). No new zero-density input is needed. Since f_N is smooth, its complete first-height pairing is absolutely convergent. Cauchy-Schwarz and ||theta|-N|<=|theta-N| give

    |B_infinity(f_N,f_N)-N Q_a(f_N,f_N)|
                           <=sqrt(M_N V_N)=O(log N). (7)

Here B_infinity is used ONLY for this smooth packet, for which its absolute convergence has just been justified. It is not defined on a rough null vector.

At |theta|>2N, |theta-N|>N and |theta|<=2|theta-N|. Thus the complete unsigned omitted first-height tail is at most 2 M_N/N=O(log N/N). Combining (5)-(7),

    B_(2N)(f_N,f_N)=N m log N+O_(a,psi)(N),
    B_(2N)(f_N,f_N)/||f_N||_D^2=N[1+O(1/log N)]. (8)

The larger O(N) remainder includes the bounded physical corrections in (5); it is not silently replaced by O(log N). Choosing N=T/2 proves a positive lower bound c_a T for every sufficiently large real T. Together with (3), this proves (1).

The argument survives a fixed scalar shift Q_mu: subtracting mu mass affects only the O(1) term in (5). It is therefore not an unshifted-contact discriminator.

## 4. Exact noncommuting limits for a hypothetical rough actual null

Let h in K have kappa_R(h)!=0, and choose smooth compact v_j->h in D by canonical core density. For each fixed j, the source derivative identities give finite second-height moments, so S_vj(T) has a finite limit as T->infinity. Therefore its normalized limit is zero.

For every fixed T, (3) implies S_vj(T)->S_h(T). The pinned actual null sharp theorem gives S_h(T)/log T->eta|kappa_R(h)|^2. These two individually lawful limit passages give exactly (2).

In particular there cannot be constants T0,C independent of j with |S_h(T)-S_vj(T)|<=C log T ||h-v_j||_D for all T>=T0, nor a comparable uniform estimate with any modulus tending to zero as v_j->h. Taking T first would contradict (2). Finite-height source convergence does not carry such a modulus at infinite height.

A cutoff-dependent diagonal choice j(T) can approximate each finite head arbitrarily well, since (3) is finite for each T. That does not give a useful sign bound: if the error is o(log T), the diagonal smooth head must inherit the positive null coefficient. A fixed smooth head has normalized limit zero, but the selected smooth vector changes with T.

## 5. Original-row terminal readout is unbounded in energy on the smooth core

Let ell(v)=kappa_R(C_X v), using the NF48 actual-row interpolation. It is bounded in D. For the above sequence, C_X v_j->h in finite-dimensional K, hence ell(v_j)->kappa_R(h)!=0. Form continuity and actual nullity give Q(v_j,v_j)->0. No v_j has zero energy unless it is zero: a zero-energy smooth vector would lie in K intersect H^r={0}.

Thus |ell(v_j)|/sqrt(Q(v_j,v_j)) diverges. The original-row readout cannot be extended as a bounded functional of the complete real-node energy samples alone. Those samples converge to zero in the energy sequence norm, while the missing original-source correction remains observable in D. This is precisely the kernel loss in the quotient, now witnessed by same-window smooth approximants.

At the positive-eigenmode control the identical argument uses Q_mu(v_j,v_j)->0 and retains Q(v_j,v_j)->mu||h||_2^2, not zero. The original actual source Gram keeps the mu physical-mass residual.

## Remaining theorem and validation

This closes a concrete proposed limit transfer: global canonical continuity at each finite height, smooth source decay, and complete real sampling do not justify a uniform height/smoothing exchange. The linear growth theorem is unconditional at each fixed actual window; the noncommuting limits and unbounded energy readout are conditional on the hypothetical nonzero contact kernel.

No actual nonpositive normalized sharp subsequence, bounded return, endpoint exclusion, F4 or full transport is produced. Whole-domain actual positivity through a=1 and historical certificates remain preserved. The next arithmetic argument must control the actual null range with a height-uniform estimate stronger than generic canonical sampling; such an estimate is still unproved.

The finite exact checker audits derivative-coupling signs, centered moment inequalities, tail constants, and a separate rational noncommuting-limit control. It does not compute actual zeros, certify the analytic operator growth or prove the missing arithmetic bound. Dependencies and normalization are pinned in the companion custody manifest. No new external theorem, Lean file, build or axiom is added.
