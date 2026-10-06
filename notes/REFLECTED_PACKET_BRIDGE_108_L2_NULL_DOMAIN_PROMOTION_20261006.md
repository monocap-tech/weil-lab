# RPB108: supported L2 null equations derive their own form domain

Base: research 055a915df254cb4deff8463b88463944b64b10e3.
Definitions: docs/TERMINOLOGY_RPB108_L2_NULL_DOMAIN_PROMOTION.md.

## Result and attachment consequence

Let h be a global L2 function supported in [-a,a]. Suppose its full actual native distribution satisfies
\[
m_a(D)h+p_h=0\quad\hbox{on }(-a,a),
\quad p_h=M_-(h)e^{x/2}+M_+(h)e^{-x/2}.
\tag{1}
\]
Then m_a(D)h is globally L2, h belongs to the canonical supported logarithmic domain D_a, and h is full mixed weak-null on D_a.

Thus the supported L2 solutions of (1) are exactly K_a, the full native form kernel. Logarithmic form membership need not be supplied separately once supported L2 custody and the exact full distributional equation are proved.

This does not attach the retained WD-T38 identity. A selected-background equation, zero diagonal, or an abstract source record cannot replace (1).

## Why the existing boundary proof extends to L2 input

The earlier gapless-residual theorem stated h in D_a. Audit its proof: off-support kernel convergence, exterior bounds, and H^{-1/4} removability only require supported L2 input; the assumed interior equation supplies its remaining premise.

First, m_a has logarithmic growth, |m_a-w|<=C_a, w(xi)=log(e+|xi|). Consequently m_a(D)h is a well-defined tempered distribution in H^{-1/4}, since
\[
\sup_\xi \frac{|m_a(\xi)|^2}{(1+|\xi|^2)^{1/4}}<\infty.
\tag{2}
\]
No logarithmic energy of h is used.

The actual off-support archimedean Euler kernel remains valid for this input:
\[
v_{\rm ext}(x)=
-\int_{-a}^a\frac{e^{-|x-y|/2}}{1-e^{-2|x-y|}}h(y)\,dy
-\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
 [h(x-\log n)+h(x+\log n)],\quad |x|>a.
\tag{3}
\]
To justify the weaker input explicitly, finite Euler multipliers are uniformly bounded by C+w. For any Schwartz test phi, their Fourier pairings are dominated by
\[
(C+w)|\widehat h|\,|\widehat\phi|,
\]
whose integral is finite by ordinary L2 Cauchy-Schwarz, because (C+w) Fourier(phi) is L2. On separated compact exterior tests, the summed physical kernels converge absolutely against h, which is L1 on its finite support. This establishes the exterior distribution dictionary without using D_a membership.

The previously proved Carleman Schur estimate applies to every L2 edge profile. With S_a=2 sum_{log n<=2a} Lambda(n)/sqrt(n), it gives
\[
\|v_{\rm ext}\|_{L^2(|x|>a)}\le(4+S_a)\|h\|_2.
\tag{4}
\]
The threshold-equality prime terms are retained. There is no boundary gap or trace assumption. The pole moment bounds similarly give
\[
\|p_h\|_{L^2(-a,a)}\le4ae^a\|h\|_2.
\tag{5}
\]

Define v=-p_h in the interior and v=v_ext in the exterior. Then v is globally L2 and
\[
\|v\|_2\le B_a\|h\|_2,\qquad B_a=4+S_a+4ae^a.
\tag{6}
\]
Equations (1) and (3) show m_a(D)h-v is supported on the two endpoints; by (2) it belongs to H^{-1/4}.

For a compact smooth test phi choose smooth collars chi_delta equal to one near both endpoints. The scaling estimates
\[
\|\phi\chi_\delta\|_2=O(\delta^{1/2}),\qquad
\|\phi\chi_\delta\|_{H^1}=O(\delta^{-1/2})
\]
and Fourier interpolation give
\[
\|\phi\chi_\delta\|_{H^{1/4}}=O(\delta^{1/4})\longrightarrow0.
\]
A distribution S supported on those endpoints has S(phi)=S(phi chi_delta); H^{-1/4} continuity forces S(phi)=0. Hence m_a(D)h=v globally. No hidden endpoint distribution remains.

Plancherel and w<=|m_a|+C_a now yield
\[
\|w\widehat h\|_2\le(B_a+C_a)\|h\|_2.
\tag{7}
\]
Since w>=1, (7) implies finite one-logarithm form energy and therefore h in D_a. Equation (1) annihilates compact smooth interior tests; the established density and continuity of the full native form extend that identity to every test in D_a. Thus h in K_a. The reverse inclusion follows from the already attached compact-action dictionary.

All subsequent finite-logarithm and subcritical Sobolev regularity theorems for K_a can now be applied to this same L2 solution, after the promotion, without assuming their domains in advance.

## Automatic derivative promotion

Let h in K_a have a global L2 derivative g=h'. Equivalently h belongs to H^1(R), with its zero extension understood globally. Compact support and H1 imply zero endpoint traces. Integration by parts gives
\[
M_-(g)=\tfrac12M_-(h),\qquad
M_+(g)=-\tfrac12M_+(h).
\tag{8}
\]
The frozen multiplier, including every fixed prime translation, commutes with distributional differentiation. Therefore
\[
m_a(D)g+p_g=\partial_x[m_a(D)h+p_h]=0
\quad\hbox{on }(-a,a).
\tag{9}
\]
The input g is supported L2; it is not presumed to be in D_a. The theorem just proved promotes g into D_a and K_a, with
\[
\|w\widehat g\|_2\le(B_a+C_a)\|g\|_2.
\tag{10}
\]
This removes the logarithmic derivative-domain premise from the preceding derivative-chain criterion whenever a global L2 derivative exists. An interior derivative with boundary delta terms does not satisfy the input premise.

## Sharper finite-dimensional regularity obstruction

Write r=dim K_a. If r>=1 and h in K_a also belongs to global H^r(R), all derivatives through order r are supported L2. Apply (8)-(10) successively: for j<r, h^{(j)} is globally H1, and its derivative is automatically promoted into K_a. Thus
\[
h,h',\ldots,h^{(r)}\in K_a.
\]
For nonzero h these r+1 vectors are independent: a linear relation transforms to P(2 pi i xi) Fourier(h)=0, and a nonzero polynomial has finitely many real zeros, so cannot support a nonzero L2 Fourier transform. Hence
\[
K_a\cap H^r(\mathbb R)=\{0\}.
\tag{11}
\]
This strengthens H^{r+epsilon} exclusion in the preceding note to H^r exclusion. For a one-dimensional kernel, a single nonzero globally H1 null vector is impossible. For r>1, (11) does not exclude an individual H1 null vector.

If the entire K_a is contained in H1(R), (9) and promotion make differentiation an endomorphism of this finite-dimensional space. Iterating gives arbitrarily long independent derivative chains for any nonzero vector, so K_a=0. The premise that the entire actual kernel is H1 has not been proved.

## What is still missing

Constructed Green syntheses have a global L2 derivative, but the retained full null equation and identification with such a synthesis remain unattached. The H1 Green membership theorem supplies coordinates for given H1 physical vectors; it does not put the entire actual kernel in H1 or prove its full mixed-null identity.

For an attached globally H1 full null witness, its derivative-domain membership is now automatic. Such a witness could coexist with a kernel of dimension greater than one; a kernel-dimension bound or regularity through that dimension would still be needed for (11). No dimension-one assertion is made here.

The established actual-null regularity remains H^s for every s<1/2. Nothing in this promotion proof reaches H1. No endpoint exclusion, selected-witness attachment, larger-window null extension, signed exponential Gaussian upper bound, or RH conclusion follows.

## Validation and custody

Analytic validation: the L2 Euler-pairing domination, exterior Carleman bound, endpoint-cutoff interpolation, full-domain density, both integration-by-parts pole signs, and Fourier-polynomial independence are explicit above. This is a reuse and strengthening of an existing analytic proof, not a new numerical certificate or a Lean result.

Pinned repository inputs at the base commit:
- ACTUAL_GAPLESS_RESIDUAL_REGULARITY_20261004: the H^{-1/4} endpoint-removability proof and actual Euler normalization.
- ENDPOINT_BOUNDARY_REGULARITY_20261005: the exterior norm bound 4 and the actual pole budget.
- ACTUAL_EXTERIOR_MOMENT_RIGIDITY_20261005: the exterior distribution dictionary.
- DERIVATIVE_CHAIN_REGULARITY_CEILING_20261006: the earlier sufficient derivative domain and independence argument.
- LOGARITHMIC_BOOTSTRAP_20261005: finite logarithmic regularity after lawful promotion.

Historical notes remain unchanged; the strengthened input and threshold are recorded additively. Numerical aperture frontier 81/100. F4 and FULL TRANSPORT CLOSED remain open. Lean and workflows unchanged; no new CI run.
