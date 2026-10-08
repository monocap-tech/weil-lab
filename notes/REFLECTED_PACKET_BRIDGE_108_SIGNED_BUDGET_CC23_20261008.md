# RPB108 CC23: signed covariance, the unit budget and circularity

Date: 2026-10-08 UTC. Coupled parent: 96e24d75abc37060bd0c41d65ffa44176eb9db92 (CC22).
Definitions: [signed budget](../docs/TERMINOLOGY_RPB108_SIGNED_BUDGET.md).

## Finding

The complete ORIGINAL signed identity gives an exact completion of the whole incoming-shell form. Its unit relative-loss inequality is EQUIVALENT to original nonnegativity at the target aperture. A Cauchy-Schwarz argument for this signed form on that enlarged domain would therefore assume the target sign. It is not a new source of the defect cancellation missing from CC22.

This audit rejects that specific proposed closure and identifies the quantitative distinction: a unit budget gives nonnegativity, while reusable continuation needs a strict budget with a uniform cap-dependent reserve and admissible steps. The complete Weil identities encode the actual arithmetic correlations; no theorem of formal logical independence from those identities is proved. Neither their desired implication nor its negation is certified here. No generic structural model is passed off as the actual arithmetic divisor.

## 1. Actual source identity, with its sign retained

The original decomposition on D_t is Q(h,f)=<P h,P f>-<N h,N f>, including all actual partner and multiplicity copies. The native mixed identity in ActualZetaNativeWeilForm.lean writes this same form as the archimedean-minus-prime Fourier pairing plus its signed pole pairing on the Green-vector dictionary. Its existing canonical extension is inherited analytically. The diagonal native theorem explicitly asserts an equality, not positivity. We do not assume positivity of the native symbol or discard either pole.

Positive observability protects P_t and its inverse on its closed range independently of the signed gap. It allows the exact source chart V_t=V_s orthogonal-direct-sum W_st. It makes the POSITIVE metric an inner product. It does not make Q_t an inner product.

Since P,N are the complete original analyses, T_t on this chart is [T_s,K], not a retained-source or finite trial matrix. Assume the old gain ||T_s||<1. Write

    H=I-T_s*T_s on V_s,
    D=I-T_s T_s* on the complete negative ambient,
    C=T_s*K.

H and D are invertible at this individual old aperture. Their inverses may depend on its old gap; we are using them for an exact identity, not claiming an independent estimate.

## 2. Exact completion, all incoming directions

In positive-source coordinates p in V_s, w in W_st, the enlarged original form has block matrix

    [ H             -T_s*K ]
    [ -K*T_s        I-K*K  ].                               (1)

Completing the old square gives

    Q_t(p,w)
      =<p-H^(-1)Cw, H(p-H^(-1)Cw)>
         +<w,[I-K*K-K*T_s H^(-1)T_s*K]w>.                  (2)

The bounded-operator resolvent identity

    I+T_s H^(-1)T_s*=D^(-1)                               (3)

turns its exact signed Schur complement into

    S=I-K*D^(-1)K.                                        (4)

These are whole-domain bounded source-chart identities. No finite critical rank or source-height cutoff is used. Mixed critical/low covariance and every incoming direction remain in (4).

Consequently

    Q_t>=0  iff  K*D^(-1)K<=I  iff  K K*<=D.               (5)

The last equivalence follows by applying the norm bound to D^(-1/2)K and its adjoint. Also A_t=A_s+K K*. Thus (5) is the full output defect inequality D_t>=0 in another chart. It is not a previously unevaluated positive estimate extracted from the arithmetic source equality.

Strictly, ||K*D^(-1)K||<1 implies D_t>=(1-||B_st||)D with a positive bounded margin. Conversely if D_t>=m I, m>0, then D<=I gives K K*<=D-m I<=(1-m)D, hence ||B_st||<=1-m<1. This establishes equivalence with a target gain strictly below one. The target positive-source margin is not substituted for an already known independent constant.

At an old critical eigenvector with lambda_i=1-delta_i, the mixed original row on the shell is -sqrt(lambda_i) times the critical incoming row. Equation (2) produces its inverse delta_i cost. Replacing it by a positive-source Cauchy-Schwarz estimate supplies no sqrt(delta_i) cancellation. CC20's forced covariance J M_t^(-1)J* and CC22's weighted phase increment remain the same quantities; (2) does not evaluate them.

## 3. The circular candidate and the exact scope of rejection

If Q_t were nonnegative, its positive-semidefinite Cauchy-Schwarz inequality would be valid. Conversely, demanding that inequality for all pairs, with nonnegative diagonal, already demands Q_t>=0. Applying it between an old near-critical vector and an arbitrary enlarged-domain vector to prove target positivity uses precisely this missing premise.

One can lawfully use Cauchy-Schwarz separately for P or N, since each source Gram is nonnegative. Such bounds control unsigned source norms. They do not give the original small defect in the mixed signed pairing. The old signed Cauchy-Schwarz inequality is valid on D_s, where positivity is known, but its second argument cannot be moved to D_t without a new estimate. On D_s the forced row J already vanishes identically, so this lawful use yields no incoming information.

There is no claim that all possible arguments from the full explicit formula are circular. The rejected argument is this specific use of enlarged-domain signed Cauchy-Schwarz, or an equivalent assertion that the whole signed source Gram is already nonnegative. The actual prime/archimedean/pole identity is exact and may support a future new arithmetic inequality. The current source estimates do not supply its quantitative mixed sign.

## 4. Identical diagonal data, opposite mixed sign

Finite exact controls isolate the omitted correlation. Set P=I on a two-dimensional physical space, old domain span(e1), and a=1-2^(-j), j>=4. Take incoming norm c=1/2. Compare complete negative analyses

    N_safe   = [ a  0 ; 0  c ],
    N_unsafe = [ a  c ; 0  0 ].

They have the same old gain a^2, old defect delta=1-a^2, positive Gram I, incoming negative energy c^2=1/4, and identical original signed diagonal entries (delta,3/4). Their signed traces also agree. Their cross-correlation differs.

Safe relative cost is c^2=1/4. Unsafe cost is c^2/delta, tending to infinity. The unsafe signed off-diagonal square is a^2 c^2, larger than delta(1-c^2); its two positive diagonal entries do not make its signed Gram nonnegative. Thus separate source energies, even with all diagonal margins and a protected positive metric, cannot determine the joint signed Schur sign.

These finite models are controls for an inference from those enumerated data only. They do NOT reproduce the actual hyperbolic sampling profiles, the full Weil explicit formula or its native arithmetic coefficients. The actual identities contain mixed correlations as formulas; what remains absent is a proved cap-uniform bound for those correlations. This distinction rules out treating the models as an impossibility theorem for actual zeta.

## 5. Genuine crossing: strict reserve versus contact

In the genuine H01 differential crossing model Q(h)=||h'||^2-||h||^2, set u=2s/pi, v=2t/pi. The exact old ground defect is 1-u^2 and its critical shell leakage is 2u(v-u). A critical budget q forces

    v-u<=q(1-u^2)/(2u).                                   (6)

At contact v=1, its critical cost is 2u/(1+u), tending to one. The full cost at contact is exactly one. Thus even a critical cost strictly below one at every precontact old aperture does not provide a uniform strict reserve, nor does it establish a strict whole budget.

For any fixed q<1 and u sufficiently close to one, the maximal step in (6) remains below contact, and

    (v-u)/(1-u)<=q(1+u)/(2u) -> q.

The allowed step collapses with the distance to contact. At a fixed target beyond contact the critical cost diverges. This is the explicit test that prevents equating an old-gap-dependent safe step, a unit budget, and the requested all-cap reusable continuation estimate.

The controls use the inherited exact differential shell formula; they do not establish an arithmetic crossing. The canonical logarithmic genuine crossing remains an inherited discriminator. No regularity or endpoint classification route is reopened.

## 6. Positive original level, full shifted mass

Keep P=I, N=(9/25,12/25), original physical level mu=16/25. The original two-dimensional form is strictly positive and its old-to-incoming relative budget is 9/34. For Q-mu I, add the ENTIRE negative physical mass channel sqrt(mu)I. The resulting signed form is nonnegative with zero determinant and zero Schur complement; its whole budget is one. Its null vector has positive original Q equal to mu times its physical mass.

Therefore a unit signed budget can occur at a positive original eigenlevel after the full lawful shift. It does not identify original nullity or give an original arithmetic strict reserve. The added mass rows are not dropped, retyped as hyperbolic zero-source rows, or evaluated with the original old defect.

## 7. Validation, certificate scope and stop condition

20,836 exact checks pass: 2,484 new and 18,352 inherited CC22 checks. The new checks include 180 whole Schur/resolvent/sign tests, 1,080 independent completion-square and minimizer tests across 54 whole finite source cases (32 strictly positive, 22 indefinite), 427 identical-diagonal correlation controls, 793 genuine crossing budget controls and four full positive-level checks. Noncommuting old input/output metrics are included. Rational finite checks verify algebra and discriminators; the complete infinite operator derivation is analytic, not a new Lean theorem or actual divisor evaluation.

Certified standing remains whole-domain original positivity through 21/20, even0/odd0, joined physical margin 1/(3*10^63). Global is paused at NF71, Aperture and Pre-Contact Shadow remain paused. No aperture increase, RH/F4, retained attachment, reusable continuation, accumulated finite-cap relative loss or Lean closure.

Stop the automatic signed-Gram/Cauchy-Schwarz cancellation candidate. Further repackaging of (1)-(5) is not arithmetic progress. To reopen it, supply an independently proved inequality for the actual mixed quotient rows, for example J M_t^(-1)J*<=q Lambda G plus a compatible low budget, with cap-dependent strict constants and admissible steps. Otherwise the correct present status is that the complete source identity specifies the missing correlation but the current proved estimates do not certify it. Formal logical nonimplication from the full identities remains unproved and is not implied by this audit.
