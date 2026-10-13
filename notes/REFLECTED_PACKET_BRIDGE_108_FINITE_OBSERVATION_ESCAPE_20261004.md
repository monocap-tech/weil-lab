# RPB108: finite observation escape on actual Green packets

Base: research 5444cf38d66ecf4b493f3efc41a0870403f06650.

## Theorem and scope

Fix a>0 and a supplied actual off-line zeta orbit {rho, 1-conjugate(rho)} with r>0 unselected multiplicity copies. For every finite set K of actual zero points there is a lawful finite actual Green packet w_K such that:

1. Every normalized positive coordinate over K and the target orbit is zero.
2. Every normalized negative coordinate on the target orbit is +1 or -1, with total unselected energy r.
3. Both normalized coordinates vanish at every other point in the finite partner-closed hull Lambda of K and the target orbit.
4. On this unchanged full graph/source vector,
   \[
   Q_{B,s}(w_K)=-r+Q_{\mathrm{tail},\Lambda}(w_K).
   \]

Consequently no finite set of positive samples controls the global unselected negative norm by any finite gain constant on the full finite actual Green domain. This is conditional on a supplied actual unselected off-line orbit. It asserts neither that such an orbit exists nor that global positive observations fail to control the negative ones.

## Finite Green interpolation proof

Close K and the target orbit under the actual partner involution. Lambda is finite, and partner symmetry preserves actual zero membership. Enumerate its distinct actual ordinates z_1,...,z_N. Actual ordinate injectivity and the certified nonresonance facts give distinct, lawful Green columns g_1,...,g_N.

Their Dirichlet-energy Gram matrix is
\[
H_{ij}=\mathcal E(g_i,g_j)=F_{g_j}(\bar z_i),\qquad
\mathcal E(u,v)=\int\overline{u'}v'+\tfrac14\int\bar u v.
\]
Finite independence is obtained exactly as in the two-column proof: a vanishing finite L2 combination is zero pointwise in the interior; apply the explicit differential expression -d^2/dx^2+1/4; distinct exponential independence forces every coefficient to vanish. Hence H is Hermitian positive definite and invertible.

For arbitrary prescribed evaluation values t_i=F_h(bar z_i), set c=H^{-1}t and h=sum_i c_i g_i. Then Hc=t, proving interpolation at every point of Lambda. Choose the t_i corresponding to
\[
F_h(\bar z)=1,\qquad F_h(z)=-1
\]
on the target orbit, and zero at every other point. Partner closure ensures that both evaluations used by the plus/minus dictionary are prescribed at every inspected point.

Use copy index 0 in each actual multiplicity fiber to synthesize these coefficients into one finite raw vector v_K. Its certified actual whole graph lift w_K has physical coordinate h and the unchanged full positive and negative source coordinates. Repeating values across multiplicity copies changes energy counts, not the interpolation matrix dimension.

The normalized dictionary p=(F_h(bar z)+F_h(z))/2 and n=(F_h(bar z)-F_h(z))/2 gives p=0 throughout Lambda, n=+1,-1 on the target pair, and n=0 elsewhere in Lambda. If m is the common orbit multiplicity and k selected copies across its two fibers, r=2m-k>0. Summability permits subtraction of these finitely many fibers from the complete background series, proving the displayed tail decomposition.

All operations use explicit finite smooth Green columns and the certified whole graph constructor. No spectral operator-domain or full graph density premise is introduced.

## Exact global requirement

Let P_K restrict the global positive analysis to the finite point set K, retaining its raw multiplicity coordinates. Let B_s be the complete unselected negative analysis. The constructed packet satisfies
\[
\|P_Kw_K\|=0,\qquad \|B_sw_K\|^2\ge r>0.
\]
Thus ker(P_K) is not contained in ker(B_s), and no finite C satisfies
\[
\|B_sw\|\le C\|P_Kw\|
\]
for every lawful finite actual Green packet.

If the global WD-T10 unit budget holds, then on this packet it necessarily gives the stronger complementary signed inequality
\[
\|P_{\Lambda^c}w_K\|^2
-\|B_{s,\Lambda^c}w_K\|^2\ge r.
\]
In particular the complementary positive energy must be at least r. A certified strict signed deficit below r on one fixed packet would give a finite negative certificate.

This necessity does not establish compensation or a deficit. It shows that a finite observation prefix cannot by itself supply the required factorization.

## Why increasing the cutoff does not settle the sign

For a fixed packet, certified source summability makes its tail tend to zero as finite sets exhaust all actual points. Here the interpolation packet changes with Lambda. Summability of each w_K does not imply uniform tail decay for this varying family.

The exact physical Dirichlet energy is
\[
\mathcal E(h,h)=t^\ast H^{-1}t.
\]
For these prescribed +/-1 and zero data, no uniform bound on this inverse-Gram expression has been proved. Scaling h to bound its energy also scales the target negative energy r; the fixed lower bound disappears if the energy grows. There is no contradiction between finite interpolation and a possible global sampling inequality.

An exhaustion argument therefore needs a new quantitative estimate controlling interpolation conditioning and the complementary signed energy together. Finite distinct-point independence, raw multiplicity, and pointwise tail convergence alone provide no such estimate. No limiting nonzero packet or retained WD-T38 witness is constructed.

## Validation boundary

This theorem and energy identity are analytic proofs, not new Lean formalizations. They extend the certified mixed Green law, actual partner/nonresonance facts, finite exponential independence, finite synthesis custody and normalized coordinate dictionary. No Lean source or workflow changed.

The latest certified Lean head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125 / job 111535430775. Its passing results do not certify this new interpolation theorem.

No actual off-line orbit existence, uniform conditioning, global background positivity, zero simplicity, full graph density, spectral operator-domain membership or retained source/null attachment is assumed. FULL TRANSPORT CLOSED remains open.

## Cursor/residue

At 5444cf3, finite actual Green interpolation is proved analytically on any finite partner-closed set of distinct actual zero points. Given an actual off-line orbit with r>0 unselected copies, assign antisymmetric values +/-1 there and zero values at all other inspected points. The resulting finite Green packet has zero positive samples throughout the inspected set, orbit negative energy r, and exact background Q=-r+Q_tail outside that set. Every finite-prefix positive gain bound fails on the full finite Green domain; global domination remains undecided and requires complementary signed tail compensation >=r for each such unchanged packet. Enlarging the inspected set changes the inverse-Gram packet; no bounded energy or vanishing-tail limit is inferred. The new proof is analytic, not Lean formalized. Next input is a global sampling/sign estimate with interpolation conditioning controlled, or one rigorous strict tail deficit on a fixed packet. No actual off-line existence, retained source/null attachment, full graph density, simplicity, spectral operator-domain membership or background positivity is assumed. WD-T38 remains independent; FULL TRANSPORT CLOSED stays open; SOURCE is off the critical path.
