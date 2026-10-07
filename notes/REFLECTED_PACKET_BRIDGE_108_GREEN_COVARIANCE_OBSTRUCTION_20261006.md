# RPB108: raw Green regularity cannot identify a coercive effective synthesis

Date: 2026-10-06 (America/Los_Angeles). Source `e5676f2b230425fa874b07a0f9edcadb57a06093`.
Definitions: [Green covariance terminology](../docs/TERMINOLOGY_RPB108_GREEN_COVARIANCE_OBSTRUCTION.md).
Global/F4 lane; no aperture computation.

## Attachment result and limit

The raw convergent native Green synthesis cannot be identified, by a Hilbert unitary change of coefficients preserving the physical vector and canonical logarithmic metric, with the actual coercive effective synthesis. The earlier POSITIVE_CARRIER_EQUIVALENCE already proves that the raw quotient has a dense proper image and that its weaker energy completion recovers D_a. Those facts are reused. This pass strengthens the attachment obstruction to compact covariance, every finite-rank repair, and an operator-norm mismatch of at least one in the canonical normalization. It holds on the entire form domain, independently of the contact kernel:

\[
\boxed{T T^*+F_{\rm fin}\ \hbox{is not coercive on }D_a}
\tag{1}
\]
for every finite-rank self-adjoint correction \(F_{\rm fin}\), where \(T\) is the raw Green synthesis with its genuine shell l2 coefficient metric. The actual effective covariance \(G=A+R^*R\) is coercive. Thus \(PP^*=G\) cannot hold if the prescribed \(P\) is identified with this raw Green map, or a unitary coefficient reduction of it.

This is an obstruction to a proposed attachment route, not a defect in the historical morphology. Its \(P\) remains abstract; the repository does not identify it with the raw Green synthesis. The fresh actual effective construction explicitly uses a different closed positive-analysis carrier. A particular retained vector could still lie in the raw Green range, but that is an independent named-vector theorem.

Completing Green packets in the weaker logarithmic range metric can remove the surjectivity obstruction. Such completion necessarily admits vectors without H1 regularity when its physical range becomes all of \(D_a\). It cannot transfer the raw gradient bound unchanged.

## Primary source and quantitative regularity

The current Lean source defines T=neutralNativeGreenSynthesis and B=neutralNativeGradientSynthesis on NeutralNativeShellCoefficients, a genuine lp2 space. It proves square summability of both column families, convergence of both series, and

\[
\langle \partial_x\phi,Tu\rangle=-\langle\phi,Bu\rangle
\tag{2}
\]
for every Schwartz test and every raw l2 coefficient \(u\). The support theorem gives the same fixed physical support to both vectors. These source declarations were read at the recovered head; their existing certificates retain their historical scope.

Analytically, (2) means \(Tu\) is globally H1 with weak derivative \(Bu\), with zero extension understood globally. Put \(g_i=T e_i\). The existing square sums give
\[
L_a=\sum_i(\|g_i\|_2^2+\|g_i'\|_2^2)<\infty.
\]
Cauchy-Schwarz for the vector series yields
\[
\|Tu\|_{H^1}\le\sqrt{L_a}\|u\|_{\ell^2}.
\tag{3}
\]
The supported H1-to-logarithmic inclusion is bounded, using
\(\log(e+|\xi|)\le e+\xi^2\) and the Fourier derivative law. Thus T is a bounded map into the canonical domain \(H=D_a\), with
\[
\sum_i\|Te_i\|_H^2\le C_a L_a<\infty.
\tag{4}
\]
In particular it is Hilbert-Schmidt and compact. One can verify compactness without naming that class: truncate the coefficient columns to a finite set I; (3)-(4) give an operator-norm tail bound by the square root of the omitted column-norm sum.

All adjoints in (1) and (4) use the logarithmic Hilbert metric. A physical-L2 adjoint is not substituted. The boundedness and compactness consequences here are analytic; no new Lean theorem or axiom certificate is asserted.

There is also a general compactness statement not requiring square-summable columns. Any bounded linear P:V to D_a whose entire range lies in global H1 is bounded into supported H1 by the closed graph theorem: convergence in D_a implies physical L2 convergence, so an H1 limit must have the same physical realization. Supported H1 embeds compactly into D_a. Indeed a bounded H1 sequence has an L2-convergent subsequence on its fixed finite interval, and
\[
\int_{|\xi|>N}w(\xi)|\widehat h(\xi)|^2d\xi
\le \sup_{|\xi|>N}\frac{w(\xi)}{1+\xi^2}\|h\|_{H^1}^2
\]
makes the logarithmic Fourier tails uniformly small. Low-frequency logarithmic convergence follows from L2 convergence. Thus an everywhere-H1 bounded synthesis cannot be onto D_a even without the stronger raw column estimate.

## Coercivity and quotient obstruction

The domain D_a is infinite-dimensional: compact smooth functions in the interval supply arbitrarily many independent vectors. A compact self-adjoint operator on it cannot be bounded below by a positive scalar. For an orthonormal sequence \(h_n\), compactness gives
\[
\|(TT^*+F_{\rm fin})h_n\|_H\to0,
\]
whereas coercivity by beta would force its norm to be at least beta. This proves (1). It also shows that adding finitely many H1 columns, or any finite-rank correction, cannot repair the full covariance gate.

By contrast the already constructed actual effective synthesis S satisfies
\[
SS^*=G=A+R^*R\ge\beta I_H,\qquad S\hbox{ is invertible}.
\tag{5}
\]
Its surjectivity means it cannot have everywhere-H1 physical range. For example a nonzero interval indicator supported strictly inside (-a,a) belongs to D_a by its O(1/|xi|) Fourier decay and is not globally H1. It therefore has an S-preimage, whose synthesis cannot acquire H1 simply by calling the coefficient carrier a Green carrier.

A unitary coefficient change preserves covariance and compactness. Restricting T to (ker T) perpendicular, or using the standard Hilbert quotient of the raw l2 space, also preserves compactness. Neither operation turns (1) into (5). If T has infinite rank, its raw-quotient range is not closed; otherwise a compact injective operator onto an infinite-dimensional closed range would have a bounded inverse and make the identity compact. No totality claim about an arbitrary shell enumeration is needed for (1).

There is a stronger quantitative obstruction in the canonical normalization. The recovered native Fredholm identity is A=I+K_a with K_a compact. Since R has finite rank, G=I+K_G with K_G compact. For every compact operator L on D_a, an orthonormal sequence gives K_G h_n and L h_n tending to zero, so ||(G-L)h_n|| tends to one. Therefore
\[
\boxed{\|G-(TT^*+F_{\rm fin})\|\ge1.}
\tag{6}
\]
The constant one is tied to the current canonical logarithmic normalization of A=I+compact. This blocks operator-norm approximation of the covariance gate by raw Green covariances plus finite-rank repairs, even if the fixed physical coercivity certificate is tiny. Strong convergence of finite covariance approximations could still occur; it is not operator-norm convergence or the exact same-domain gate.

For a constructive tail statement, let T_I retain a finite set of raw columns. Choose a unit vector perpendicular to Ran T_I and Ran F_fin, possible since their joint span is finite-dimensional. Its Rayleigh value for TT*+F_fin is at most sum_{i not in I} ||Te_i||_H^2, which tends to zero. Thus the omitted rough carrier cannot be repaired by adding any fixed finite packet. No actual null mode is produced by these test vectors.

This complements PRESCRIBED_REDUCTION: that theorem constructs its quotient unitary only *after* PP*=G and PC=-R* have been attached. It cannot establish PP*=G for a raw Green map which violates (1).

## Completing packets: identify the norm before taking the limit

There are distinct limits, with distinct custody:

| Limit | Guaranteed physical information | Information not supplied by that limit alone |
| --- | --- | --- |
| Raw l2 coefficients, with the certified T and B | Same supported vector and global L2 derivative | Full retained native null equation |
| Derivative graph / H1 packet convergence | Supported H1 limit and derivative custody | Historical coefficient and covariance identity |
| Canonical logarithmic packet convergence | Supported logarithmic limit | H1 or a raw l2 preimage |
| Repository source graph convergence | Logarithmic coordinate and both full source coordinates | A derivative coordinate |

On the raw quotient, replace the coefficient norm by \(\|Tu\|_H\) and complete. T then extends isometrically onto the logarithmic closure of its physical range. If that closure is all H, the completed map is onto H. This is a new metric and completion, not the original raw l2 quotient metric. Its Hilbert adjoint, covariance and compensator must be computed in the new metric. The old raw covariance and unit-gain equations cannot simply be carried across.

The raw derivative map B cannot extend boundedly in this range metric when the completed physical range is all D_a. Otherwise every completion limit would have a physical L2 derivative by (2), placing all of D_a in H1, contradicted by the interval indicator.

An actual packet approximation makes the loss explicit. The H1 Green membership theorem proves finite actual critical Green columns dense in supported H1. Compact smooth tests are dense in D_a by the canonical domain construction. Approximate an interval indicator first by compact smooth vectors in D_a, then approximate each smooth vector by finite critical Green packets in H1. A diagonal choice of errors gives finite actual Green packets \(g_n\to h\) in D_a. Their derivative L2 norms cannot have a bounded subsequence: such a subsequence would have a weakly convergent derivative, and passing (2) against smooth tests would put the indicator in H1. Thus the derivative norms tend to infinity.

The recovered LOG_SAMPLING_GRAPH_DENSITY theorem already proves that both complete actual source analyses are bounded on D_a and that the source graph norm is equivalent to its logarithmic norm. Therefore these same finite actual Green packets also converge in the full source graph to the indicator's unique unchanged lift. That lift belongs to the actual Green graph closure, but its physical vector is not H1. This is an actual-carrier counterexample to Green graph closure membership -> H1, with every source coordinate retained. It asserts no full-null equation, contact or named shell-enumeration identity. The prior full graph density theorem is reused, not claimed anew.

Likewise the established actual positive-analysis isomorphism and local coercive effective covariance make their physical positive/background energy norms equivalent to the logarithmic norm. Completion in those norms cannot preserve a bounded derivative coordinate either. The positive completion is lawful for covariance realization; it does not transfer the raw Green derivative estimate.

## Exact diagonal control for the metric distinction

In the abstract sequence space H=l2, let T e_n=e_n/n and B e_n=e_n for n>=1. The raw image lies in the weighted derivative domain \(\{x:\sum n^2|x_n|^2<\infty\}\), and the raw covariance is diag(1/n^2), compact and noncoercive. Finite-coordinate covariance corrections leave its tail Rayleigh values unchanged.

Set \(x^{(N)}=\sum_{n=1}^N e_n/n\). These vectors converge in H to \(x=(1/n)_n\), but their raw preimages \(u^{(N)}=\sum_{n=1}^N e_n\) have squared norm N, as do \(B u^{(N)}\). The limit has no raw l2 preimage and no weighted derivative. Completing with the range norm produces x, while completing with the derivative graph norm does not. This is a control of metric/completion implications, not an actual divisor or endpoint example.

## Smallest remaining attachment theorem

The exact failed implication is:
\[
\hbox{fresh coercive effective packet or source/logarithmic completion}
\ \Longrightarrow\
\hbox{raw Green synthesis realization and its H1 regularity}.
\]
The whole-synthesis version is obstructed by (1); the named-vector version is not proved by completion.

A lawful named-vector theorem could instead prove \(k=Tu\) with a genuine raw l2 coefficient \(u\), or exhibit an actual derivative-graph limit for this same k. Separately attach its exact full native mixed null law. Only then does automatic derivative promotion apply. One H1 null vector still need not exclude a kernel of dimension greater than one; the recovered total/parity regularity ceilings specify the additional rank or higher-derivative requirement.

For prescribed P,C,k attachment, the same-domain full covariance and signed actual row dictionary remain the correct gates. A completed/background synthesis satisfying them must retain its actual metric and may have rough physical vectors. Proving those gates does not establish a Green range identity for k. Conversely a Green identity alone proves no native nullity or enlarged central cancellation.

This obstruction belongs primarily to retained attachment and to the proposed transfer of regularity into endpoint exclusion. The unchanged physical k is the object to attach. Changing coefficient norms can preserve it; differentiation and dilation change physical vectors. Endpoint full mixed nullity still cannot become same-vector enlarged full mixed nullity by completion or covariance reduction. F4 and FULL TRANSPORT CLOSED remain open.

## Custody and validation

Pinned source hashes and repeated exact diagonal controls are in notes/data/RPB108_GREEN_COVARIANCE_OBSTRUCTION_20261006.json. The controls check covariance tails, finite-rank corrections and coefficient/derivative norm growth; they do not certify an actual endpoint estimate. The proofs here are analytic consequences of the read native synthesis/weak-derivative/support declarations and actual domain results. No new Lean/compiler/workflow changes or axiom audit are claimed. Historical records are unchanged. Whole-domain positivity through 93/100 is preserved.
