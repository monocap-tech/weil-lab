# RPB108: sharp source cutoffs are not physical null tests

Date: 2026-10-07 UTC. Recovered live head f396010281602b9e11c15dad1a9516393b071a3c.
Definitions: [physical source graph and critical height error](../docs/TERMINOLOGY_RPB108_SOURCE_HEIGHT_GRAPH_ERROR.md).
Category: endpoint exclusion / exact source-test obstruction. Analytic; no new arithmetic bound or Lean certificate.

## Result and failed direct attack

A nonzero compact supported canonical physical vector has INFINITE complete actual source support. Consequently a nonzero finite-height cutoff of its joint source packet cannot be the complete source analysis of any compact physical test, even after a finite support enlargement.

At a hypothetical nonnegative actual zero kernel, projecting that cutoff back to the same-window physical source graph yields a lawful null test. The entire sharp signed first-height sum is then exactly the discarded graph error:

    S_h(T)=<Jsrc Gamma_a h,(I-Pi_a)M_T Gamma_a h>.       (1)

No sign or uniform height bound follows from this identity. It isolates the missing source-graph estimate rather than silently testing nullity against an unrealizable finite divisor packet.

This pass does not revisit historical packet attachment. Finite actual negative selection and the already constructed effective packet remain valid observations/syntheses; neither claims finite COMPLETE source support of its physical reconstruction.

## 1. No finite complete source packet can be a nonzero compact physical vector

Suppose h in D_a and both actual complete channels vanish outside a finite coordinate set F. Choose any b>a and epsilon<b-a. The unchanged-source exact pair law implies that Gamma_b(tau_t h) is supported in those same finitely many blocks for every |t|<epsilon: hyperbolic mixing occurs only within each actual pair, and a zero pair stays zero.

All these physical translates belong to D_b, with support custody. The established positive observability lower bound at this ONE fixed b makes Gamma_b injective. Therefore their physical linear span has dimension at most the finite number of retained source slots.

But arbitrarily many distinct small translates of a nonzero compact L2 vector are independent. A finite relation gives

    hhat(xi) sum_j c_j exp(-2 pi i xi t_j)=0 a.e.

The set where nonzero hhat is nonzero has positive measure. The exponential polynomial must vanish on a set with an accumulation point and thus identically; independence of distinct exponents gives all c_j=0. This contradicts the finite source-span bound. Hence h=0.

No modulus inequality, zero-density count with multiplicity converted to a distinct-zero count, or derivative regularity is needed. The proof uses the already established actual supported positive observability at b, including its documented external critical-zero-density dependency.

Finite-height joint packets are finite-coordinate packets: actual local zero counting gives finitely many divisor copies below each finite height. Thus any nonzero Pi_T Gamma_a h, or M_T Gamma_a h, lies outside every compact physical source range. At heights where M_T Gamma_a h=0, the packet is zero and this assertion deliberately makes no nonzero claim. A nonzero h cannot have all observations confined to theta=0, since that would be finite complete support.

This theorem says nothing against finite R h, an orthogonal compression onto N0(K), or R* synthesis. The full graph of a synthesized physical vector still has infinitely many coordinates. A finite coefficient carrier is not a claim that all complete observations vanish outside it.

## 2. A lawful graph projection keeps an exact nonvanishing error

Fix the original aperture a. Bounded sampling and the positive lower bound show that Gamma_a has closed range V_a and a bounded inverse on that range in the logarithmic norm. Thus

    v_T=Gamma_a^(-1) Pi_a M_T Gamma_a h

is a lawful supported canonical test at the SAME aperture. No physical dilation or enlarged-null equation is used.

For h in the actual full K_a, full mixed nullity gives

    <Jsrc Gamma_a h,Gamma_a v>=0 for every v in D_a.

Hence Jsrc Gamma_a h is orthogonal to V_a in the positive source metric. In particular its pairing with Pi_a M_T Gamma_a h is zero. Its pairing with M_T Gamma_a h is the legal finite S_h(T). Subtracting gives (1), or equivalently

    S_h(T)=<Jsrc Gamma_a h,[M_T,Pi_a]Gamma_a h>.       (2)

This is the complete full-native null equation expressed on its actual source range. The projector is the complete graph projector, not the negative kernel-image projector from the earlier compression note. The two projectors cannot be identified.

For a physical orthonormal basis of the finite full kernel, summing (2) identifies the sharp trace with the trace of this signed off-graph commutator quadratic. A uniform ONE-SIDED upper bound on this trace is exactly the finite-height sufficient target proved by the preceding Abel interface. It is not established here.

The automatic estimate is only

    |S_h(T)|<=||Gamma_a h|| ||E_T(h)||<=T ||Gamma_a h||^2.

It grows with T. The source graph's finite-dimensional kernel does not change that height multiplier into a bounded one. Uniform unweighted source-tail approximation likewise supplies no uniform estimate for E_T.

## 3. Exact control: projecting is not free and the sign is unrestricted

An algebraic two-dimensional control demonstrates the failed projection step. Let positive and negative carriers each be C^2; let Tswap exchange their two coordinates. Put Gamma h=(h,Tswap h), so the induced form is identically zero. Its graph projector is

    Pi(x,y)=((x+Tswap y)/2,(Tswap x+y)/2).

Let the height multiplier be diag(1,2) in BOTH channels. For h=(0,1), Gamma h=(0,1;1,0), so S=2-1=1. The projected weighted packet is (0,3/2;3/2,0), which pairs to zero with Jsrc Gamma h. The retained error is (0,1/2;-1/2,0), whose pairing is exactly 1. For h=(1,0) the sign reverses.

Thus even a nonnegative null form, an injective closed source graph and a positive height multiplier do not permit dropping the error or assigning it a nonpositive sign. This finite algebraic graph is not an actual divisor model and does not satisfy the infinite-support theorem's actual physical translation hypotheses. Its purpose is only to audit the null-test projection algebra.

## 4. Signed-tail form of the same missing arithmetic estimate

Write d_q^K=sum_basis (|p_q(h_j)|^2-|n_q(h_j)|^2). Actual full nullity gives sum_q d_q^K=0; absolute unweighted summability is retained. Layer-cake on the finite head proves

    S_K(T)=integral_0^T Delta_K(u)du-T Delta_K(T).       (3)

Indeed a coordinate at height v<=T contributes v after subtracting its tail rectangle, while a coordinate above T cancels. The convention Delta_K(T)=sum_(v>T)d_q^K handles the atoms exactly. Signed interchange is legal on [0,T] since sum |d_q^K|<infinity.

The bounded Abel multiplier also gives directly

    A_tau^K=integral_0^infinity exp(-tau T) Delta_K(T)dT. (4)

Absolute convergence follows from |Delta_K(T)|<=sum |d_q^K| and tau>0; alternatively apply Tonelli separately to the two channels. Thus an independent bound integral_0^infinity (Delta_K(T))_+ dT<infinity would suffice, as would eventual Delta_K(T)<=0. Neither is proved. Ordinary tails tend to zero, and derived subcritical tails are o(T^(-r)) for every r<1; those rates do not control the critical integral in (4) as tau decreases.

A nonzero hypothetical actual kernel must instead have A_tau^K->+infinity by the existing critical promotion/native comparison. Hence integral (Delta_K)_+=infinity and Delta_K is positive at arbitrarily large heights. This is a conditional obstruction, not existence of a kernel, an assertion of eventual positivity, or a new actual arithmetic tail rate.

The positive-tail-minus-negative-tail balance and the graph error are two exact formulations of the missing signed estimate. Replacing them by zero through coefficient truncation would discard actual source-range custody.

## Smallest remaining theorem and standing

Exact failed implication: actual full mixed nullity + finite kernel + complete source-tail convergence -> a uniform signed first-height bound by testing with the finite divisor cutoff. The prescribed finite cutoff has no nonzero compact physical realization. Projecting it produces (1)-(2), whose signed error is uncontrolled. This is an endpoint-exclusion obstruction, not a retained-attachment or same-vector transport failure.

For THIS graph-projection route, the smallest remaining theorem is the uniform one-sided trace bound in (2) on every hypothetical nonnegative actual contact kernel. An integrable positive signed tail in (4) is a separate sufficient route. No estimate for either term is claimed. Both must use the actual source graph; the scalar-shift comparison and finite algebraic graph do not identify that graph's arithmetic constraints.

Pinned reads at recovered head:

- ACTUAL_KERNEL_SOURCE_COMPRESSION_20261006: 32fd6b8d4eecdc0c0d52284cb7b974ad1d89595a.
- FINITE_SOURCE_REGULARITY_20261006: 03b6f5a9d6cb9caa6044d3fd247156606703e91b.
- POSITIVE_SOURCE_HEIGHT_MOMENT_20261006: 7997a0a3ccb0666d117f696dd208b743255b7ac5.
- ABEL_SHARP_HEIGHT_20261007: a51b2becce5c0ffaa394f4b7d29f6aa136473687.

Analytic audit checks fixed-b translated support, same actual pair coordinates, source injection before dimension comparison, positive-measure Fourier independence, closed graph inverse, full SAME-WINDOW mixed nullity, the retained projector error, and finite/infinite signed Fubini for (3)-(4). The two-dimensional rational control is verified exactly in the companion check; it certifies algebra only. No new external theorem, Lean build/axiom audit, actual contact vector or critical arithmetic bound. Historical records are immutable and additions are explicit. Concurrent aperture work and certified positivity through 973/1000 are preserved. No aperture marching, prescribed packet replacement, enlarged actual-null transport, endpoint exclusion, RH, F4 or FULL TRANSPORT CLOSED.
