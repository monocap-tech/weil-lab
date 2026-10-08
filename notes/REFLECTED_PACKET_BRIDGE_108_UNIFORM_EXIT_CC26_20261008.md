# RPB108 CC26: the non-stalling shell target has RH strength

Date: 2026-10-08 UTC. Coupled parent: 5c3277d99db375b0af6dc8b0fe7d8f0e6ae6ec62.
Definitions: [uniform exit quantifiers](../docs/TERMINOLOGY_RPB108_UNIFORM_EXIT.md).

## Result

With the inherited strict original source anchor and the complete actual domain/source identification, the uniform cap exit property specified below is EQUIVALENT to RH. The forward implication is a finite product of strict shell budgets followed by the classical compact-test Weil criterion. The reverse implication is especially simple: RH makes every original negative source profile zero, so every original incoming shell budget is zero.

This is a proved analytic REDUCTION and a quantifier audit, not a proof of the uniform property or RH. It does not say that a critical leakage estimate without low output or non-stalling steps is RH-equivalent. The arithmetic estimate still missing from CC20 has exactly the strength of the desired exit when supplemented with those obligations.

## 1. Precise property, without an assumed target sign

Let a0=21/20 be the inherited anchor and use the complete ORIGINAL P,N on every finite cap B. Positive observability, closed nested ranges and the exact source-shell identity are inherited analytic dependencies. The anchor in this chart has ||T_a0||<1, so for some delta_0>0,

    D_a0=I-T_a0 T_a0*>=delta_0 I.

We use this as the standing strict source anchor of CC19/NF67, not as a newly evaluated numerical constant. In particular delta_0 is NOT set equal to the joined physical margin 1/(3*10^63).

Uniform cap exit property U:

    For every finite B>a0 there are h_B>0 and 0<=rho_B<1,
    depending on B but not on min spectrum D_s,
    such that for every s in [a0,B) with ||T_s||<1,
    and every s<t<=min(s+h_B,B),

        K_st*D_s^(-1)K_st<=rho_B I.                       (1)

The property quantifies over ALL complete incoming directions. It contains no premise that t is already positive, no physical-strip substitution and no retained source prefix. A bound that permits h_B to shrink with the old gap is a different property. Merely quantifying over an empty critical space after positivity has been lost does not satisfy U: each step begins at a known source-positive s, and U applies before the target sign is known.

## 2. Finite march and explicit product reserve

From (1), the operator D_s^(-1/2)K_st has squared norm at most rho_B. Hence

    K_st K_st*<=rho_B D_s,
    D_t=D_s-K_st K_st*>=(1-rho_B)D_s.                    (2)

For a fixed cap set n=ceil((B-a0)/h_B), and divide [a0,B] into n equal steps. Every step is positive and at most h_B. At the first step the anchor hypothesis allows (1); (2) gives a strictly positive target defect, which provides the old hypothesis for the next step. Finite induction reaches B without a limiting first-contact argument or any generic continuity premise. It proves

    D_B>=delta_0(1-rho_B)^n I>0.                          (3)

If c_B>0 is the inherited positive observability lower constant in the common canonical norm, then

    Q(h)>=delta_0(1-rho_B)^n ||P h||^2
         >=delta_0(1-rho_B)^n c_B^2 ||h||_D^2             (4)

for every h in D_B. The source-input and output defects have the same relevant singular-value gap; (4) follows from ||T_B||^2<=1-delta_0(1-rho_B)^n. Constants are qualitative unless independently evaluated. This does not relabel (4) a new numerical aperture certificate.

Caps B<=a0 inherit positivity by restriction. Every compact smooth test belongs to some finite D_B, so U proves original positivity for ALL such tests.

## 3. Connection to the classical compact-test Weil criterion

Primary sources checked in this pass:

- Connes and Consani, Weil positivity and Trace formula, the archimedean place, arXiv:2006.13771v1, introduction equation (2) and Appendix C Proposition C.1: https://arxiv.org/pdf/2006.13771
- Bombieri, Problems of the Millennium: the Riemann Hypothesis, Section V, printed page 9: https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf

The Connes-Consani formulation explicitly gives the RH criterion using compact smooth multiplicative tests with the pole-transform conditions; Bombieri records the corresponding signed explicit-formula criterion. We import this classical equivalence as an analytic dependency, not a new Lean proof. This is a criterion citation, not a reopening of their semi-local trace-formula strategy.

To check support and sign conventions, set g(x)=x^(-1/2)h(log x). If h is compact smooth, g is compact smooth on the multiplicative positive half-line. Its Mellin transform is

    g_tilde(s)=integral_R h(u) exp((s-1/2)u)du.

The classical pole conditions g_tilde(0)=g_tilde(1)=0 select a subspace of our compact tests. Our full original positivity covers that subspace. On it the pole terms vanish and the normalized source form is the full zero mixed functional of the compact-test criterion, after the inherited beta-reflection pairing. The geometric-side sign in the cited criterion is opposite to the zero-form sign, as the explicit formula states. No poles are deleted for the unrestricted original problem.

Therefore the all-test conclusion of Section 2 implies RH. The external equivalence is not inferred from a fixed aperture or a finite dictionary. Together with (2)-(4), this proves U=>RH under the named inherited framework.

## 4. Reverse implication: original N vanishes under RH

Under RH, beta_q=0 for EVERY original actual divisor copy. Its normalized profile is

    n_q(h)=integral h(x)exp(i theta_q x)sinh(beta_q x)dx=0.

Thus N=0, T_s=0, A_s=0, D_s=I and K_st=0 on every cap. Choose any positive h_B and rho_B=0. Property U holds with zero budget. All copies and partners remain; they are zero coordinates, not omitted rows.

The complete P remains the positive frame supplied by the inherited observability. In its metric Q=||P h||^2 has source defect one, even when its physical lower constant on a large aperture is extremely small. This proves RH=>U, not RH itself.

Combining the two directions gives the claimed equivalence. It explains why the missing all-cap arithmetic source theorem is not a modest unconditional lemma already implicit in the numerical 21/20 certificate.

## 5. Critical correlation: exactly which additions give this strength

For a compatible spectral band Ecrit, let G=Ecrit D_s Ecrit, L=Ecrit K_st. The exact whole budget splits as

    K_st*D_s^(-1)K_st
      =L*G^(-1)L+B_low.

If, for all shells quantified in U,

    L L*<=q_B G,
    B_low<=ell_B I,
    q_B+ell_B<=rho_B<1,                                  (5)

with the same h_B>0, then U follows. In the CC20 generalized physical lifts, the first inequality is exactly J M_t^(-1)J*<=q_B Lambda G, with all mixed rows retained. A protected finite critical rank can make it a finite output matrix, but its incoming domain remains complete. No such actual cap-uniform constants are proved here.

Under RH all these original incoming maps vanish, so a split property permitting the trivial zero critical space also holds with q_B=ell_B=0. A fixed nonzero protected rank need not exist under RH; an artificial requirement of that rank is NOT included in the equivalence.

A critical estimate without an independent low bound does not imply U. A strict budget on each individual shell without a positive cap-only step does not imply U. A fixed finite-rank source compression, a shifted positive physical level or an averaged height asymptotic is not substituted for (5). These exclusions follow from the quantifiers, not from an assertion that every possible arithmetic approach fails.

## 6. Genuine crossing and physical-margin controls

In the genuine H01 differential model, u=2s/pi, v=2t/pi, old critical defect 1-u^2 and critical shell leakage 2u(v-u). For any fixed h>0 with v=u+h on a finite cap beyond contact, its relative critical cost is

    2u h/(1-u^2),

which diverges as u tends to one. Since the whole cost is at least this critical cost, U fails there. This is the expected discrimination: U must exclude an actual finite contact. No arithmetic equivalence is attributed to that model.

One can instead set a gap-dependent step h(u)=rho(1-u^2)/(2u), with fixed rho=9/25. Its critical cost is exactly rho, and for u sufficiently close to one it remains below contact. The step tends to zero. Such critical budgets do not certify a finite march across contact, demonstrating why a fixed strict coefficient alone is insufficient.

Separately, take P=diag(epsilon,1), N=0 in a finite complete source control. The original physical margin is epsilon^2, tending to zero, while T=0 and source defect D=I. Physical smallness is not evidence of near-critical original negative-source gain. This distinction is also valid in the RH=>U direction. We do not infer actual critical source eigenvectors from CC18's small physical margin.

The full positive-level test remains P=I, N=(9/25,12/25), mu=16/25. Adding sqrt(mu) times the entire physical vector for Q-mu I gives shifted whole budget one, while the original budget is 9/34. Under RH the ORIGINAL negative channel vanishes, but this separately added shifted physical mass channel does not vanish merely by setting beta=0. The reverse implication in Section 4 concerns the unshifted original form only.

## 7. Validation and checkpoint

24,554 exact checks pass: 1,224 new and 23,330 inherited CC25 checks. New tests include 720 noncommuting product-budget checks over five anchor defects and 24 steps each; 45 finite-cap partition checks; 285 genuine crossing/non-stalling checks; 171 physical-versus-source margin checks; three full positive-level checks. The noncommuting chain computes each actual model budget and verifies the product margin independently. These rational controls validate algebra and quantifier discriminators, not the actual arithmetic property or RH. The equivalence proof is analytic, with the classical Weil criterion explicitly imported; it is not a new Lean theorem.

We now have an exact statement of the exit's strength. The arithmetic theorem needed for U is still absent. CC22's weighted modulus, CC24's scalar correlation theorem and CC25's finite identity rigidity do not establish (1) or (5). No genuine full-identity countermodel or independence theorem exists in this work.

Whole-domain original positivity remains internally certified through 21/20, even0/odd0, joined physical margin 1/(3*10^63). No new aperture, RH/F4, retained attachment, reusable continuation, accumulated finite-cap relative-loss or Lean closure is claimed. Global remains paused at NF71; Aperture and Pre-Contact Shadow remain paused.

Further progress requires a new independently proved actual joint correlation inequality with the complete low-output and non-stalling quantifiers. Additional equivalence reformulations or structural controls alone should not be reported as movement toward an arithmetic certificate.
