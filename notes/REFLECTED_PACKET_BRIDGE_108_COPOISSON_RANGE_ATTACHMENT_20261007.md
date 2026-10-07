# RPB108: lawful rough co-Poisson attachment and its completeness obstruction

Date: 2026-10-07 UTC. Recovered live head 5923ded080bf30a51c8a9a9c5fe9a4c294223a61 and the canonical cursor. The concurrent 0.995 preflight is preserved.
Definitions: [co-Poisson range attachment](../docs/TERMINOLOGY_RPB108_COPOISSON_RANGE_ATTACHMENT.md).
Category: actual source-range arithmetic / candidate-framework obstruction. Analytic, not Lean-certified.

## Result and scope

For every supported actual vector h in the already established weak-critical translation class, there is an injective nonlocal map

    T_a h in L_lambda, lambda=exp(-a)<1,
    Mellin(T_a h)(s)=zeta(s)H_h(1-s).

All nontrivial-zero jets up to their actual multiplicities vanish. The same statement applies to the actual rough positive eigenmode. Every nonzero image lies in Burnol's nontrivial co-Poisson complement P_lambda and lies OUTSIDE L_1. Thus multiplying the actual profile by zeta does solve the jet attachment problem, but cannot supply exclusion by complete zero sampling. This is stronger than merely saying that no attachment was specified: this concrete lawful attachment has the wrong carrier for both null and positive-eigenvalue profiles.

No bounded/sublogarithmic sharp subsequence has been found. The global graph is unchanged. Actual unshifted source-range nullity -> bounded/sublogarithmic sharp subsequence remains unproved.

## 1. Inputs consumed without reopening analytic work

The sharp/log and null-Abel notes establish D_w(t;h)=O(|t|) for actual full null vectors, and for the actual positive eigenmode after retaining its mu mass term. The sublog prime-bulk note derives the continuous physical Fourier tail, uniformly for exp(bx)h, |b|<=1. In particular its identical Tonelli argument at b=0 gives

    integral_(|u|>T) log(e+|u|)|Fourier(h)(u)|^2 du <= C_h/T.

Positive layer cake immediately gives integral (1+|u|)^(3/4)|Fourier(h)(u)|^2 du < infinity. We consume this subcritical H^(3/8) consequence; no critical derivative promotion or new endpoint criterion is asserted.

The sole additional growth input is the unconditional classical convexity bound |zeta(1/2+iu)| <= C_epsilon(1+|u|)^(1/4+epsilon). It is recorded in Adam Harper's primary [Bourbaki exposition 1159, section 2, page 8](https://www.bourbaki.fr/TEXTES/Exp1159-Harper.pdf). Choose epsilon=1/16. Its squared exponent is 5/8, strictly below 3/4. Consequently

    integral |zeta(1/2+iu)H_h(1/2-iu)|^2 du < infinity.

No RH, new transverse bound, or higher native source moment is used here.

## 2. Construct and close the actual rough attachment

Use right Mellin normalization integral f(t)t^(-s)dt and cosine transform 2 integral cos(2pi tu)f(t)dt. For f_h(t)=t^(-1/2)h(log t), change of variables gives

    ||f_h||_L2(dt)=||h||_L2(dx),
    hat(f_h)(s)=H_h(1-s),
    support(f_h) subset [lambda,1/lambda].

For smooth h supported inside [-a,a], set

    F_h(t)=sum_(n>=1) f_h(t/n)/n-hat(f_h)(1).

The smooth co-Poisson identity and Mellin formula give

    cosine(F_h)(t)=sum_(n>=1) f_h(n/t)/t-hat(f_h)(0),
    hat(F_h)(s)=zeta(s)H_h(1-s).

These identities and Mellin Plancherel are [Burnol, math/0203120, equations (6)-(9)](https://arxiv.org/pdf/math/0203120). The spaces L_lambda require both functions to be constant on (0,lambda); Proposition 2.2 provides continuous completed Mellin jet evaluators. Theorem 3.1 identifies their orthogonal complement as P_lambda when lambda<1 and proves completeness at lambda=1.

Here is the rough extension, with all carrier hypotheses checked. Approximate h in supported H^(3/8) by smooth vectors inside the same interval. One construction first contracts support by h_delta(x)=h(x/(1-delta)), then convolves with a smooth approximate identity narrower than the resulting boundary margin. Dilation continuity and mollification convergence in H^(3/8) follow by Fourier change of variables, dominated convergence on bounded frequencies, and the integrable weighted tail; choose a diagonal sequence. The zeta multiplier estimate above makes the smooth F_h converge in L2(dt). L_lambda is closed: restriction to (0,lambda) must belong to the closed one-dimensional constant subspace, for both the function and its unitary cosine transform. Hence the limit T_a h belongs to L_lambda and has the stated Mellin profile. This defines the rough sum by L2 closure, not by choosing pointwise representatives in an infinite sum.

Compact support also gives uniform local convergence H_(h_n)->H_h in the complex plane by Cauchy-Schwarz. The completed Mellin identity extends to the meromorphic profile pi^(-s/2)Gamma(s/2)zeta(s)H_h(1-s). At every nontrivial zero rho the gamma factor is holomorphic and nonzero, and zeta has its actual multiplicity m_rho. Thus every derivative of order 0 through m_rho-1 vanishes, including multiple zeros. Continuous evaluators give the same conclusion directly from L_lambda convergence. No simplicity hypothesis or substitution of repeated native value samples for derivative jets occurs.

## 3. Injectivity and the exact wrong-carrier obstruction

If T_a h=0, its critical-line Mellin profile vanishes almost everywhere. Zeta is a nonzero analytic function there, with discrete zeros of measure zero. Therefore H_h(1/2-iu)=0 almost everywhere. Fourier/Mellin Plancherel implies h=0. T_a is injective on this class.

Because every zero jet vanishes, T_a h belongs to P_lambda. If a nonzero image also belonged to L_1, its jets would vanish in that carrier too: completed meromorphic Mellin continuation is unique and the evaluator convention is the same. Complete zero sampling in L_1 would imply T_a h=0, contradicting injectivity. Hence

    h != 0 -> T_a h != 0 and T_a h not in L_1.

The weaker statement that there are guaranteed simultaneous constant intervals of length lambda is not an assertion that these intervals are maximal. Even accidental promotion of both to length 1 is excluded by the preceding completeness argument.

A dilation cannot promote the guaranteed gaps. For U_r F(t)=r^(1/2)F(rt), the function gap becomes lambda/r and the cosine gap r*lambda, whose product stays lambda^2<1. Both cannot be at least 1. Dilation also changes the physical image, so it would never be same-vector native transport. This proves only the limitation of scaling these guaranteed gaps; it does not forbid a distinct null-specific construction.

The transformation does not preserve the original source vector Gamma h or its quadratic sharp head. All-zero-jet vanishing of zeta H is an arithmetic factorization property shared by every h in the class, whereas actual full nullity is the mixed equation J Gamma h perpendicular to the actual source range. No individual native p/n coefficient is set to zero. Inferring one from the other would be the exact failed implication.

## 4. Stronger mixed-system theorem does not remove the surviving defect

[Burnol, arXiv:1106.4751, Theorem 1](https://arxiv.org/pdf/1106.4751) bounds the defect of an admissible mixed system of zeta quotients and biorthogonal zero jets by one in the Mellin image of L_1. It does not prove zero defect. Theorem 2 adds the domain condition for multiplication by s. Its proof of Theorem 1 combines two defect vectors to impose G(0)=0 before division by s.

Our actual rough quotient already has dimension one. Even a lawful identification with this mixed system would therefore give no contradiction from that defect bound alone. Moreover the new co-Poisson image is not in L_1 for nonzero h, and no admissible-partition identification of the native mixed-null graph has been proved. The domain of multiplication by s cannot be inferred from subcritical H^(3/8). These are independent hypotheses, not analogous equations.

Physical derivative-chain central moments are at H_h(1/2). For a nonnegative compact bump phi, h=D^m phi has H_h(s)=(-(s-1/2))^m H_phi(s), so its first m central moments vanish while both H_h(0)=(1/2)^m H_phi(0) and H_h(1)=(-1/2)^m H_phi(1) are nonzero. In our bare transformed profile G(s)=zeta(s)H_h(1-s), G(0)=zeta(0)H_h(1) is therefore nonzero as well. This smooth control is not an actual null vector; it rules out the generic moment substitution only.

## 5. Remaining theorem, dependencies and controls

The smallest global gate stays

    actual unshifted full-null source range -> liminf S_K(T)/log T <= 0.

Combined with the established sharp/log limit (2/pi)Lambda_K>0, this excludes a nonzero contact kernel. No edge on that global path was discharged here. A candidate-specific sufficient compatibility would be actual full-null h -> T_a h in L_1. The preceding theorem would then force h=0, but this compatibility is NOT proved and is not promoted as a new global criterion. One must exploit the unshifted native equation to obtain it, or choose a different genuinely null-specific range map.

| Dependency or control | Audit |
|---|---|
| Exact actual weak correlation -> weak Fourier tail -> lawful co-Poisson L2 image | Closed analytic inputs plus the strict convexity multiplier budget; all hypotheses checked. |
| Image zero jets -> exclusion | Fails at L_lambda, lambda<1; nontrivial P_lambda is the exact obstruction. |
| Actual rough positive eigenmode | Same weak-critical class and same actual zeta multiplier; nonzero image has all jets zero but lies outside L_1. This decisively prevents distinguishing nullity by the present construction. |
| Artificial compact-good-row logarithmic control | Its physical vector is smooth, so the transform is lawful, but artificial rows are not the actual divisor or native null graph. Transform jets supply no restriction on its artificial sharp slope. |
| Fixed finite actual restoration | Native sharp normalization changes by o(1). Completeness at L_1 uses the FULL divisor; deleting jets at lambda=1 is not assumed harmless. The attachment uses the full zeta function throughout. |
| Two-row comparison contact | Weak-class physical vectors can be attached, but auxiliary nullity is not the actual mixed-null equation. No gap promotion follows from contact geometry. |

The manifest pins source custody. The executable checks exact multiplier exponents, dilation gap products, central-moment distinction and four-control scope. These are algebraic safeguards, not numerical proofs of completeness or actual null exclusion. No Lean or axiom closure is claimed. Certified positivity, historical certificates and the concurrent aperture cursor are preserved; F4 remains open.
