# RPB108: strict enlargement puts the actual source graph in the Green closure

Base: research 30706af4ccf2c27f63d0a974fa1292e99fc263d5.

## Theorem

Let 0<a<b. Let f be an element of the complete actual-zeta source graph at window a, with physical vector h, logarithmic coordinate k_h, and both complete raw-copy source vectors. Then its support-preserving inclusion J_ab f into the source graph at b belongs to the actual Green graph closure at b.

J_ab preserves h, the globally weighted Fourier coordinate k_h, every positive and negative source sample, their multiplicity-weighted energies, and every fixed selected-background projection. In the whole Hilbert graph norm this inclusion is isometric. Only the support constraint changes. This is strict-enlargement membership; no equality between the full source graph and Green closure at a fixed window is asserted.

The proof uses the H1 Green-membership theorem of the preceding record. In particular its documented external distinct-critical-zero density input remains in force. No additional arithmetic theorem is introduced here.

## Source-graph inclusion and raw samples

The physical logarithmic carrier is a closed support subspace of the same global weighted Fourier Hilbert space. A vector supported in [-a,a] is also supported in [-b,b], with the same weighted Fourier coordinate. Source evaluation is the compact physical transform
\[
F_h(z)=\int h(x)e^{izx}\,dx.
\]
Window-dependent Riesz representatives represent this same functional on the corresponding supported space. Consequently the whole source-graph coordinate identities are preserved on inclusion.

For actual ordinates z_q, write
\[
p_q=\tfrac12(F_h(\bar z_q)+F_h(z_q)),\qquad
n_q=\tfrac12(F_h(\bar z_q)-F_h(z_q)).
\]
The graph uses sqrt(2) times these normalized coordinates. Thus source-graph membership implies that the raw sequence u_q=F_h(z_q)=p_q-n_q belongs to lp2. Conversely, partner reindexing and the parallelogram identity give
\[
\sum_q(|p_q|^2+|n_q|^2)=\sum_q|u_q|^2.
\]
All sums count actual divisor copies. Equal-ordinate copies remain energy weights, not independent observations.

## A smooth approximation controlled in the entire graph norm

Choose a nonnegative real smooth mollifier phi supported in [-1,1] with integral one. Set phi_epsilon(x)=epsilon^{-1}phi(x/epsilon) and h_epsilon=h*phi_epsilon. Take 0<epsilon<b-a tending to zero.

Compactly supported L2 h is L1. Convolution is smooth, and
\[
\operatorname{supp}h_\epsilon\subseteq[-a-\epsilon,a+\epsilon]\subset(-b,b).
\]
In particular h_epsilon is H1_0(-b,b). It therefore has a lawful actual source-graph lift in the Green closure at b by the preceding theorem.

Fubini, justified by compact supports and absolute integrability, gives
\[
F_{h_\epsilon}(z)=F_h(z)M_\epsilon(z),\qquad
M_\epsilon(z)=\int\phi(t)e^{i\epsilon zt}\,dt.
\]
For every fixed complex z, M_epsilon(z) tends to one. On the actual strip |Im z_q|<=1/2,
\[
|M_\epsilon(z_q)|\le e^{\epsilon/2}.
\]
Fix epsilon_0<b-a and restrict epsilon<=epsilon_0. Then
\[
|F_{h_\epsilon-h}(z_q)|^2
 \le(1+e^{\epsilon_0/2})^2|u_q|^2.
\]
The right side is summable over raw copies. Dominated convergence for the counting measure proves
\[
\sum_q|F_{h_\epsilon-h}(z_q)|^2\longrightarrow0.
\]
The partner identity above now proves convergence of both complete positive and negative source vectors, including the graph's sqrt(2) normalization. Every fixed selected projection converges as well. Individual coordinate convergence alone would not have sufficed; the uniform strip bound supplies the missing summable majorant.

For the physical coordinate use the Fourier convention already fixed in the repository. The convolution multiplier is
\[
m_\epsilon(\xi)=\int\phi(t)e^{-2\pi i\epsilon\xi t}\,dt,
\]
with |m_epsilon(xi)|<=1 and pointwise limit one. Writing w for the global logarithmic weight,
\[
\|k_{h_\epsilon}-k_h\|^2
 =\int w(\xi)|\widehat h(\xi)|^2|m_\epsilon(\xi)-1|^2\,d\xi
 \longrightarrow0
\]
by dominated convergence with majorant 4w|Fourier(h)|^2, integrable by the given logarithmic membership. No H1 bound for h is used.

Thus the lifts of h_epsilon converge to J_ab f in the full Hilbert source-graph norm. Since the Green graph closure at b is closed, J_ab f belongs to it. This proves the theorem.

## Consequences and the exact remaining distinction

The certified source/native mixed and quadratic identities on the Green closure at b now apply to every strictly smaller-window source-graph vector after inclusion. In particular such a vector can be paired lawfully with every compact smooth test in (-b,b). Its physical vector and source energies in these identities are unchanged.

If a retained witness has already been attached to the actual source graph at a, no additional H1 regularity or Green-range constructor is needed merely to place it in the Green closure at any b>a. This also works with arbitrarily small positive enlargement.

This does not attach an abstract WD-T38 vector to the actual source graph. That requires both raw source summability and the same-vector coordinate dictionary. The theorem cannot manufacture these from retained logarithmic energy alone.

It also does not extend a weak-null identity to new tests. If the mixed form vanishes against the old test space, inclusion preserves those old equalities, but says nothing about additional tests in the larger window. Membership makes the enlarged pairing well-defined; enlarged central cancellation remains an independent assertion. Similarly, no background positivity or unit bound for WD-T10 follows from graph membership.

Any source relation expressed only through the unchanged coordinates is preserved. A weak-null statement quantified over a window-dependent test domain requires its own persistence proof.

## Validation and cursor

This is an analytic proof, using the previous H1 theorem and the actual source dictionary. No Lean source or workflow changes. Existing Actions certification at cb92c1b4dfca298cbc79d5b7d25598ea370236bf (run 37236113125, job 111535430775) does not certify this new analytic theorem.

At 30706af, every complete actual source-graph vector supported in [-a,a] embeds with unchanged logarithmic coordinate and full raw-copy source coordinates into the actual Green graph closure for every b>a. Compact convolution gives H1_0(-b,b) approximants; bounded entire mollifier multipliers converge in the full sample lp2 norm and the weighted logarithmic norm. This removes Green-closure membership as an extra requirement for an already attached actual source-graph witness after strict enlargement, without retained H1 regularity or fixed-window full graph density. Actual source-graph attachment from abstract WD-T38, general WD-T10 unit domination, and enlarged-window weak-null/cancellation persistence remain independent and open. Analytic proof using the previous H1 membership theorem; Lean/workflow unchanged. FULL TRANSPORT CLOSED and F4 entry remain open; SOURCE is off the critical path.
