# RPB108: actual global positive kernel rigidity

Base: research 5fe9b63c707d6d8b3f763eaf1a217969103b39fd.

## Independent arithmetic input

H. M. Bui, B. Conrey and M. P. Young, “More than 41% of the zeros of the zeta function are on the critical line”, Acta Arithmetica 150 (2011), 35–64, Theorem 1.1, prove liminf N_0^*(T)/N(T)>=0.4058. N_0^* counts simple critical-line zeros. This uses a subset known to be simple; it does not assume all zeta zeros are simple.

Source checked: https://aimath.org/~kaur/publications/69.pdf, page 1, definitions and Theorem 1.1.

The actual zero count has leading term T/(2pi) log(T/(2pi e)), with an O(log T) error. A primary checked reference is E. Hasanalizade, Q. Shen and P.-J. Wong, “Counting zeros of the Riemann zeta function”, https://arxiv.org/abs/2107.06506, which gives an explicit error bound stronger than needed here.

Together these published results imply that the number of distinct critical-line ordinates gamma in (0,T) is at least c T log T for some c>0 and all sufficiently large T. Simple points supply independent observations directly. Raw multiplicity counts are not used to manufacture independent samples.

These are external analytic inputs, not theorems newly certified in this Lean repository.

## Minimal supported-transform uniqueness theorem

Let h be any complex L2 function supported in [-a,a], a>0, and
\[
F_h(z)=\int_{-a}^a h(x)e^{izx}\,dx.
\]
Then F_h is entire and
\[
|F_h(z)|\le\sqrt{2a}\|h\|_2 e^{a|\operatorname{Im}z|}
 \le\sqrt{2a}\|h\|_2e^{a|z|}.
\]
Differentiation under the finite-interval integral is lawful since every power of x is bounded there and h is L1 by Cauchy–Schwarz.

Suppose F_h vanishes at every actual critical-line ordinate. If it is nonzero, choose a center z_0 with F_h(z_0) nonzero. Jensen's formula on disks centered at z_0 gives at most O(R) zeros in the disk of radius R: each zero within R contributes at least log 2 to the Jensen sum at radius 2R, while the boundary logarithmic mean is at most a(|z_0|+2R)+log(sqrt(2a)||h||_2). Radii meeting zeros are handled by nearby radii and limits.

But the distinct critical ordinates in (0,T) are zeros lying within distance T+|z_0| of z_0, and their number is >>T log T. Contradiction. Thus F_h is identically zero. Fourier injectivity on L2 then gives h=0.

The proof uses only superlinear distinct critical sampling, not the numerical percentage or a conditioning floor.

## Actual positive kernel closes

At a critical-line zero, z=gamma is real, and the actual normalized positive coordinate is
\[
p_q=(F_h(\bar z)+F_h(z))/2=F_h(\gamma).
\]
Therefore vanishing full actual positive sampling forces h=0 by the preceding theorem.

Apply this on the actual closed source graph defined in ActualZetaSourceGraph.lean, whose first coordinate k lies in NeutralLogHilbertCarrier a and whose two lp2 coordinates satisfy the actual source dictionary. Its supported physical vector is h=neutralLogPhysical(k). The weighted reconstruction is injective: its Fourier transform is k divided by the everywhere nonzero square root logarithmic weight, so h=0 forces k=0. The certified canonical equivalence gives the same conclusion. Then every source coordinate is zero by the graph dictionary, so the whole graph vector is zero. In particular this holds on the smaller Green graph closure defined in ActualZetaGreenGraphClosure.lean; no density of Green lifts in the entire source graph is used.

Consequently, on the full actual source graph D, and on its Green graph closure,
\[
\boxed{\ker P=\{0\},\qquad \ker P\subseteq\ker B_s.}
\]
For any lawful raw whole-graph synthesis G into D,
\[
\boxed{\ker(PG)=\ker G.}
\]
The reverse inclusion is automatic; the forward follows from graph injectivity. In particular the full observation quotient and the synthesis quotient have the same algebraic equivalence relation on raw coefficients. Equal-ordinate copy redundancy is still quotiented, and multiplicity coordinates are retained for energy.

This extends to any lawful supported physical/source domain retaining this actual coordinate dictionary. It does not assert full graph density in an unrelated physical form domain or attach an unseen retained witness.

## What remains for the positive completion

Since P is injective on D, the algebraically induced map
\[
T_0:P(D)\to\ell^2,\qquad T_0(Pf)=B_sf
\]
is well-defined and linear. Its well-definedness is now an actual-zeta conclusion, rather than an unproved kernel premise.

The positive carrier is the completion of D with norm ||Pf||, identified canonically with closure(P(D)). This injectivity does not prove that T_0 extends boundedly to the completion. Such an extension with norm at most 1 is still equivalent to
\[
\|B_sf\|\le\|Pf\|\quad(f\in D).
\]
No unit bound, graph/source norm equivalence, stable physical reconstruction, or same-vector endpoint-null witness follows from Jensen uniqueness.

Thus the two carriers agree algebraically on the relevant range, but their completed normed structures cannot yet be identified. Further observational quotienting on D is unnecessary; the remaining WD-T10 obstruction is bounded unit gain. The positive completion may contain limits for which original physical/source custody has not been recovered.

## Relationship to finite escape and transport

Finite observation escape remains valid: any finite prefix can vanish on a nonzero packet. The new theorem says all infinite positive observations cannot simultaneously vanish on a nonzero supported graph vector. This is qualitative uniqueness, compatible with arbitrarily poor conditioning.

No actual off-line zero existence, background positivity, simplicity of all zeros, spectral operator-domain membership or full graph density is assumed. The external density theorem does not provide retained k membership, source quadratic/null identity or WD-T38 endpoint realization. FULL TRANSPORT CLOSED remains open.

## Validation boundary and cursor

This kernel theorem and its carrier consequences are analytic, not Lean formalized. The imported arithmetic inputs are explicitly named above. No Lean source/workflow changes or new CI claim; latest certified head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 5fe9b63, independent published simple-critical-zero density (Bui-Conrey-Young Theorem 1.1) and the actual zero-count asymptotic give distinct real critical ordinates >>T log T. A compact-support transform has exponential-type growth and only O(T) zeros unless identically zero. Therefore full actual positive sampling is injective on supported physical vectors, and on the concrete closed Green source graph P has zero kernel. For raw synthesis ker(PG)=ker G, and ker P subset ker B_s follows without background positivity. This closes qualitative actual-zeta kernel descent analytically using explicit external arithmetic input, not Lean certification or simplicity of all zeros. The positive completion need not preserve graph/source norm or extend the algebraically induced B map boundedly; the unit inequality remains unproved. WD-T38 retained membership/endpoint-null attachment remains independent. Next substantive target is bounded unit gain on the full positive range or a lawful WD-T38 constructor, not further qualitative kernel tests. No full graph density or operator-domain premise. FULL TRANSPORT CLOSED stays open; SOURCE remains off the critical path.
