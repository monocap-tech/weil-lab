# RPB108: actual Green density in supported Dirichlet H1

Base: research 33e0d48f9236fe00d9a1d6c8fa3194457a3837bb.

## Minimal membership theorem

For every a>0, every complex h in H1_0(-a,a), extended by zero outside the window, has its actual logarithmic physical coordinate and both complete actual-divisor source coordinates in the actual Green graph closure. In particular every compact smooth test supported in (-a,a) belongs lawfully.

This is proved density in H1 and a consequent graph inclusion. It is not density of the Green range in the entire source graph or the entire canonical logarithmic domain. It does not establish H1 membership for an unseen retained k.

## Energy-totality of actual critical columns

Equip H1_0(-a,a) with the equivalent complete Dirichlet energy norm
\[
E(h,h)=\|h'\|_2^2+\tfrac14\|h\|_2^2.
\]
For every actual critical-line zero rho=1/2+i gamma, let g_gamma be the explicit endpoint-zero Green solution of
\[
-g_\gamma''+\tfrac14g_\gamma=e^{-i\gamma x}.
\]
The actual nonresonance results make this column lawful. Integration by parts against any H1_0 vector gives
\[
E(g_\gamma,h)=\int_{-a}^a e^{i\gamma x}h(x)\,dx=F_h(\gamma).
\]
The boundary term vanishes by the H1 zero trace. Equivalently extend the smooth-test identity by H1 density; g_gamma and its derivatives are explicit smooth functions.

If h is orthogonal to every such column, F_h vanishes on every actual critical-line ordinate. The distinct critical-sampling theorem established in the preceding global-kernel record gives h=0: published simple-critical-zero density supplies >>T log T distinct real zeros, while a nonzero compact-support transform has O(T) zeros by Jensen.

Thus the orthogonal complement of the actual critical Green span is zero. The Hilbert orthogonal-complement theorem proves that its finite span is dense in H1_0. For each h choose finite actual critical-column packets h_j with E(h_j-h,h_j-h)->0. One lawful raw copy per distinct point suffices; no multiplicity duplication supplies extra density.

External arithmetic input remains Bui-Conrey-Young Theorem 1.1 together with the actual zero-count asymptotic, explicitly sourced in REFLECTED_PACKET_BRIDGE_108_GLOBAL_POSITIVE_KERNEL_20261004.md. No simplicity of all zeros is assumed.

## H1 convergence preserves the whole source graph

The graph inclusion requires a norm estimate, not physical convergence alone. For a general H1_0 vector h, endpoint-zero integration by parts gives
\[
iwF_h(w)=-\int_{-a}^a h'(x)e^{iwx}\,dx.
\]
This sign is immaterial to the norm estimate. On the actual strip, |Im z_q|<=1/2, so
\[
|F_h(z_q)|^2\le2ae^a\|h\|_2^2
\]
at every point. For height |Im rho_q|>=1 the derivative estimate yields
\[
|F_h(z_q)|^2\le8ae^a\|h'\|_2^2(1+|\operatorname{Im}\rho_q|)^{-2}.
\]
These repeat the certified Green sampling argument for arbitrary H1 vectors; the general extension is analytic, not newly Lean certified.

Let M be the finite number of raw copies of height <1 and W the full summable quadratic height weight. Summing gives
\[
\sum_q|F_h(z_q)|^2
 \le2ae^a M\|h\|_2^2+8ae^a W\|h'\|_2^2.
\]
Partner invariance supplies the same bound for conjugate samples. With normalized p,n,
\[
\sum_q(|p_q|^2+|n_q|^2)
 =\sum_q|F_h(z_q)|^2,
\]
by the parallelogram identity and actual divisor partner reindexing. Hence both full analyses are bounded maps from H1_0 to raw-copy lp2. Selection and background projections preserve convergence too.

For the logarithmic coordinate k_h=sqrt(weight) Fourier(h), the certified scalar bound weight(xi)<=exp(1)+xi^2 and Plancherel/derivative identity give
\[
\|k_h\|_{\log}^2
 \le e\|h\|_2^2+(2\pi)^{-2}\|h'\|_2^2.
\]
Thus h_j->h in H1 implies logarithmic coordinate convergence and convergence of both full source coordinates. Each h_j is the physical coordinate of a lawful finite actual Green lift. Their whole source graph vectors converge to the graph vector of h. By definition of the actual Green graph closure, this limit belongs to it.

No inverse sampling bound, background positivity, spectral operator-domain membership or full graph density is used.

## Source/native identity on this proved class

The already certified Green-closure mixed and quadratic identities now apply to the graph lift of every H1_0 vector. In particular the actual source quadratic equals the canonical native Weil multiplier/cross-pole form on these vectors, and the mixed identity holds on two such vectors.

Every compact smooth test supported strictly inside the window is H1_0, so it is a lawful graph test with both actual source coordinates. If an actual weak null identity is later attached to a witness in the Green closure, these tests are available for deriving compact-test cancellation. This theorem supplies test membership; it supplies neither the witness membership/null identity nor enlarged-window persistence.

A merely logarithmic retained vector need not be H1. The new theorem cannot be used to silently upgrade its regularity.

## Validation and cursor

This density, arbitrary-H1 sampling extension and graph membership are analytic proofs. They use previously named external critical-zero density and existing actual Green/source/count identities. No Lean source/workflow changed and no new CI claim. Latest certified head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 33e0d48, distinct critical sampling rigidity proves that actual critical-line Dirichlet Green columns span H1_0(-a,a) densely in Dirichlet energy. Explicit arbitrary-H1 integration by parts identifies the energy pairing with compact evaluation. Finite low-height counts and the reciprocal-square sampling estimate bound the full actual source maps in H1; the Fourier log weight bound controls the logarithmic coordinate. Hence every supported Dirichlet H1 vector, including compact smooth tests, has its unchanged full source graph lift in the actual Green graph closure, and inherits the certified source/native identity. This is a new analytic membership theorem, not full graph density or retained-k regularity. Uses the external critical-simple-zero density already documented; no new Lean/workflow or CI claim. Short-window contraction remains scoped to a<=0.8; general unit domination and same-vector WD-T38 witness membership/null attachment remain open. Next use lawful compact-test membership when attaching an actual weak null witness; do not assume the retained witness is H1. FULL TRANSPORT CLOSED and F4 entry remain open; SOURCE is off the critical path.
