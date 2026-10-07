# RPB108: actual drive attachment does not close the critical derivative gate

Date: 2026-10-07 UTC. Recovered live head d712291a8c118e420ec51ee6ce4edafd8824fbe3.
Definitions: [actual native-drive cusp control](../docs/TERMINOLOGY_RPB108_ACTUAL_DRIVE_CUSP.md).
Category: endpoint exclusion / critical derivative promotion.

## Result

At the already certified a=97/100 there is a real supported physical h with all of the following properties:

1. h belongs to global H^(5/8), hence Xcrit and the canonical native domain. Its actual critical positive-source moment is finite. Its physical derivative is not L2.
2. Both signed boundary moments are absolutely convergent and match the genuine actual drives: M_R=2A_R,h(0) and M_L=2A_L,h(0).
3. The physical Hardy budgets, full-residual Hardy budgets, actual drive-variation budgets and the lawful matched Carleman quadratic identities hold at both ends. All compact interior cutoffs have the previously used log^3 Fourier energy.
4. The genuine right exterior flux is negative with leading order -c t^(3/2)log(1/t), c>0. The left flux is zero on a sufficiently short collar. Thus the previously used necessary one-sided null-flux upper sign does not reject this control.
5. This same vector has positive actual native energy Q(h)>=9e-30 ||h||_2^2>0, by reuse of the certified whole-domain result. It is not asserted to be an eigenvector.
6. The exact full-native interior equation fails explicitly:

       q_h(a-v)=v^(1/4)log(1/v)+O(v^(1/4)), v down to 0.    (1)

This strengthens the earlier independently assigned comparison drive into a genuine actual-native-drive control. It is NOT a counterexample to promotion on K_a. The full interior equation is precisely the missing constraint; actual drive attachment, endpoint matching and the sharper actual-zero transverse strip do not replace it.

## 1. Actual prime geometry keeps the two cusps distinct

Take epsilon=1/1000 and delta=1/10000. The registered h0 has a right endpoint cusp v^(1/4), and a one-sided interior cusp u^(1/4)log(1/u) immediately to the right of x0=a-log 2. Its cutoff is one up to delta/2 and zero from delta onward.

The right prime evaluation points are a-log n, n=2,3,4,5; the left points are -a+log n. Rational logarithm enclosures show that their small collars, the two endpoint bump supports and the endpoint cusp are disjoint, except for the intentionally attached prime-2 interior cusp. For prime 2, the right exterior evaluation is exactly x0+u and the right interior evaluation is exactly x0-v. The former enters the one-sided interior cusp; the latter is outside it. This exact correlation is used instead of subtracting uncertain interval endpoints.

All prime evaluation values of h0 at u=0 are zero. The smooth bumps are also zero near every prime evaluation point. No threshold equality occurs at this aperture. Geometry checks use the actual set 2,3,4,5 and verify log 7>2a; no prime-6 term is invented.

The standard cusp difference estimate extends to the logarithmic cusp:

    ||tau_t h_I-h_I||_2^2<=C t^(3/2)(1+log^2(1/t)).

For the edge portion use the squared amplitude on an O(t) region; outside it use the derivative bound C u^(-3/4)(1+log(1/u)) and integrate its square from t to delta. The smooth cutoff portions give O(t^2). Tonelli's fractional difference formula yields H^s for every s<3/4, in particular H^(5/8). Adding smooth bumps preserves this conclusion. H^(5/8) dominates the Xcrit weight r log(e+|xi|), and also r log^3(e+|xi|) on every cutoff. Thus these are proved regularity properties of this actual carrier control, not a prescribed abstract packet.

## 2. Two genuine endpoint constraints can be solved by smooth bumps

For these profiles the actual endpoint inverse moments are absolute: the only endpoint power cusp contributes integral v^(-3/4)dv. All other terms are separated from the endpoints. Using the actual pole normalization p_h(a)=integral 2cosh((a-y)/2)h(y)dy, the boundary functionals are exactly

    L_R(h)=2 integral_(-a)^a J(a-y)h(y)dy
              +2 sum_n Lambda(n)/sqrt(n) h(a-log n),
    L_L(h)=2 integral_(-a)^a J(a+y)h(y)dy
              +2 sum_n Lambda(n)/sqrt(n) h(-a+log n).

These equations use the full actual drive, including the regular Euler integral and pole. Neither is claimed injective. On the bumps the prime evaluation terms vanish, so reflection gives B=[[d,o],[o,d]].

For 0<s<=1, exp(-s/2)>=1-s/2>=1/2 and 1-exp(-2s)<=2s, giving k(s)>1/(4s). Also 2cosh(s/2)<4. On the diagonal bump distances epsilon<s<2epsilon,

    J(s)>1/(8epsilon)-4=121,
    d>242.

For the opposite bump, 1<2a-2epsilon<s<2a-epsilon<2. Here k(s)<2 and 2cosh(s/2)<4, so |J(s)|<6 and |o|<12. These elementary bounds use e<3 and e^2>2. Therefore B has both eigenvalues >230 and is invertible.

The registered coefficients c=B^(-1)(L_R(h0),L_L(h0)) enforce L_R(h)=L_L(h)=0. They are finite real numbers. This changes only smooth interior pieces, preserving both cusps, their amplitudes and their local prime attachment. B is a boundary compatibility matrix, not the response matrix of a hypothetical kernel or a retained WD-T38 packet.

Since h(a-v)=v^(1/4) for v<delta/2, its global derivative is not L2. The smooth correction cannot cancel integral_0 v^(-3/2)dv. The vector is nonzero regardless of the correction coefficients.

## 3. The actual exterior drive reproduces the refined negative-flux control

Let w2=Lambda(2)/sqrt(2)>0. On the right exterior collar only the actual prime-2 term has a nonsmooth profile:

    A_R,h(u)-A_R,h(0)=-w2 u^(1/4)log(1/u)+O(u).         (2)

All other prime profiles vanish there. The pole and regular Euler integral are C1 in u because their kernels are smooth on the fixed compact interval and h is supported L1. The smooth bump corrections affect those smooth terms but do not affect the cusp in (2).

Writing alpha=1/4, the right Carleman difference has the genuine asymptotic

    C_R(u)=M_R-I_alpha u^alpha+O(u),
    I_alpha=integral_0^infinity y^(alpha-1)/(1+y)dy>0.

Indeed M_R-C_R(u)=u integral f(v)/[v(u+v)]dv. Scale the endpoint power part by v=u y; all outer terms are separated and contribute O(u). The power-tail truncation also contributes O(u). Thus the actual complete residual is

    r_R(u)=-w2 u^alpha log(1/u)+(I_alpha/2)u^alpha+O(u).

The Hardy norms with weights L(v)/v on f and 1/[u L(u)] on r and A-A0 are finite. Their integrands have integrable power u^(-1/2) times finite logarithmic factors. The actual ordinary matching limits hold by construction. Consequently the absolute-collar estimate and matched quadratic calculation are lawful here without any full-null premise being smuggled in.

Substitute u=t x in the actual collar flux to obtain

    F_R(t)=-w2 B(5/4,5/4)t^(3/2)log(1/t)+O(t^(3/2)).   (3)

Hence it is negative near zero; the critical absolute flux integral is finite, while its order-3/2 signed integral tends to -infinity with a negative log-squared leading term. This is an exterior flux of a positive-energy carrier vector, not the diagonal-subtracted signed source trace of a null vector. Those quantities must not be identified when the interior equation fails.

At the left endpoint h is zero within distance epsilon. The left prime profiles vanish on a short collar; pole and regular Euler parts are smooth, and left matching makes r_L(u)=O(u). Its Carleman profile has a support gap. The left physical flux is therefore exactly zero for t<epsilon. Both-end matching and all relevant boundary budgets coexist with the rough right derivative.

## 4. The exact interior equation rejects this actual-drive control

For x=a-v with v sufficiently small, all positive prime shifts are outside the support. All negative prime shifts are zero: the prime-2 evaluation is x0-v, on the zero side of its one-sided cusp, and the others lie in the proved gaps. Thus T_a h=0 on this right interior collar.

The actual pointwise archimedean formula there is

    m0(D)h(a-v)=m0(0)f(v)
      +integral_0^infinity k(s)
          [2f(v)-1_(s<v)f(v-s)-f(v+s)]ds,

where f is zero outside (0,2a). It is legitimate on this smooth interior collar; at each fixed v>0 the local second difference cancels the singular kernel. The remaining separated integrations are absolutely convergent.

Fix b<delta/4 and then v<b. On 0<s<v the singular 1/(2s) part scales to O(v^alpha), since the second difference has an integrable quadratic zero at s=0. On v<s<b it equals

    v^alpha log(b/v)-(1/2)integral_v^b (v+s)^alpha/s ds.

The second integral differs from integral_0^b s^(alpha-1)ds by O(v^alpha): use (v+s)^alpha-s^alpha<=alpha v s^(alpha-1) for s>=v and include the omitted (0,v) integral. The bounded local regular kernel contributes O(v^alpha) relative to its boundary value. The distant actual kernel contribution is a constant plus O(v^alpha)+O(v); change variables to place the derivative on the smooth separated kernel, rather than differentiating the distant interior cusp.

It follows that

    q_h(a-v)=q_edge+v^alpha log(1/v)+O(v^alpha),
    q_edge=-integral_0^(2a) k(s)f(s)ds+p_h(a)
                 -sum_n Lambda(n)/sqrt(n)h(a-log n)
            =-(1/2)M_R+A_R,h(0)=0.

The enforced moment match cancels the constant only. It does not cancel the v^alpha log(1/v) term. Equation (1) is therefore nonzero on an entire sufficiently short interior collar, which explicitly rules out the full-native null equation.

Independently, the pinned 97/100 whole-domain certificate gives Q(h)>=9e-30 ||h||_2^2>0. This certifies a positive actual carrier control without inventing an eigenvector or recomputing any aperture matrices. Actual positive source coordinates and the finite critical moment are supplied by the pinned source/Fourier theorem. The accepted |beta_rho|<=3/8 input applies to the same actual zeros, but does not remove this interior defect.

## Exact obstruction and smallest remaining theorem

Failed implication: actual native source/drive attachment + critical membership + both endpoint matches + all proved boundary budgets and quadratic identities + necessary exterior upper sign -> L2 derivative. The constructed positive-energy actual carrier control disproves that implication. It improves the custody of the earlier independently assigned-drive comparisons.

It does NOT disprove h in K_a intersect Xcrit -> h' in L2. The exact full-native homogeneous interior equation is absent, and (1) exposes its absence. That homogeneous promotion remains the smallest critical gate, with whole-contact-kernel critical membership separately required for the finite derivative-chain contradiction. A proof must control the genuine interior/exterior compatibility, not merely realize a matching A_h. The alternative whole-kernel order-3/2 finite-liminf signed trace remains unproved.

Category: endpoint exclusion, not retained historical attachment or enlarged null transport. One unchanged physical carrier vector has its actual drive and source coordinates throughout; the two bumps deliberately construct that vector and are not called same-vector transport of a null witness. No aperture marching, new eigenmode/null existence, full-null source neutrality, RH, Lean, F4 or FULL TRANSPORT CLOSED claim.

## Custody and validation

- MATCHED_96_097_WHOLE_DOMAIN_20261007, blob 8604e8d6429c91b9ccea4a5c8a7e75dee4f078c6: reused positive actual energy at 97/100.
- COMBINED_RIGHT_EDGE_DRIVE_20261007, blob 81851d107b65549dca965f656b92353df7ac0fe7: actual exterior kernel, finite shifts and pole.
- LOGARITHMIC_BOOTSTRAP_20261005, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028: actual m0/T/p normalization.
- L2_NULL_DOMAIN_PROMOTION_20261006, blob b8ef9607e6823444a887ac71d8ec08bc21242510: exact full-native equation required for K_a.
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006, blob 955ff7b4bd0d7f58221c300a962a803824232fd6: actual critical source/Fourier comparison.
- CRITICAL_DERIVATIVE_PROMOTION_20261007, blob 26627f85c34572a8197b32a1216382e8d02e07f5: original cusp and critical gate.
- CRITICAL_ABSOLUTE_COLLAR_20261007, blob 498a8ad4530bd2ed5c613746f4b1afc2780103a7; MATCHED_CARLEMAN_QUADRATIC_20261007, blob a0e9e076f9033aecee2bedb3e485809c8c20781a: boundary estimates and their scope.

Analytic proof: cusp differences, actual endpoint functionals, invertible bump matrix, genuine prime-profile attachment, singular integral asymptotic and positive-energy reuse. The companion rational check audits support intervals, matrix ceilings and exponent thresholds only; it is not a numerical construction of h, an arithmetic null calculation, or a Lean certificate. Historical wording remains intact; the canonical cursor is updated additively and the 97/100 frontier is preserved.
