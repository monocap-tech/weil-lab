# RPB108: a fresh actual first-contact null constructor

Base: research e130cd0a47c600285787943a588b2bdfbcabd29f.

## Result and prerequisite

The actual native Weil forms admit a concrete first-contact construction on the correct logarithmic carrier. If a lawful actual negative vector is supplied at some window a_1>0.8, the construction produces an endpoint a_* in (0.8,a_1) and a nonzero actual logarithmic vector h_* supported in [-a_*,a_*] such that:

- the actual native form is nonnegative on the entire endpoint domain;
- its mixed pairing with h_* vanishes against every vector in that domain;
- h_* has its unchanged complete actual positive and negative source coordinates;
- full-negative analysis factors through positive analysis by an actual contraction attaining unit gain on h_*.

This is an analytic constructor theorem for the actual forms. It does not assume a retained witness's membership or null equation; it constructs a fresh vector if the negative input is present. No actual negative vector, finite endpoint, or false-RH zero is asserted to exist here.

The prerequisite is a physical h_1 in the canonical supported logarithmic domain at a_1, with the actual native quadratic strictly negative. A formally named negative field or unattached abstract quadratic is insufficient. A smooth actual test with rigorously negative native energy would suffice.

## One fixed domain for the varying windows

Use the Hilbert domain H=D_1 of logarithmic-energy vectors supported in [-1,1]. For a>0 define physical L2 dilation
\[
(U_a h)(x)=a^{-1/2}h(x/a).
\]
It maps H bijectively onto D_a. Its Fourier transform is sqrt(a) Fourier(h)(a xi), and the transported logarithmic energy is
\[
E_{\log}(U_a h)=\int w(\eta/a)|\widehat h(\eta)|^2\,d\eta.
\]
For a in any compact positive interval these weights are uniformly equivalent to w(eta)=log(e+|eta|). Thus the pulled-back native mixed form
\[
q_a(f,g)=Q_a(U_a f,U_a g)
\]
is a bounded Hermitian form on the same H. Let A(a) be its bounded self-adjoint Riesz operator. This is a bounded form operator; no physical spectral operator-domain assumption is made.

In Fourier coordinates its archimedean multiplier is
\[
m_a(\eta)=\operatorname{arch}(2\pi\eta/a).
\]
The fixed-window prime multiplier terms become cos(2pi eta log(n)/a). The physical pole moments become
\[
M_\pm(U_a h)=\sqrt a\int_{-1}^1 h(t)e^{\pm at/2}\,dt.
\]
These formulas keep both complex mixed slots and the existing pole normalization; no even/real restriction is introduced.

## Identity plus compact remainder

The certified native logarithmic symbol bound gives, uniformly on compact positive a intervals,
\[
|m_a(\eta)-w(\eta)|\le C.
\]
Indeed apply the archimedean/log bound at eta/a, then bound |w(eta/a)-w(eta)| by a compact-interval constant.

The Fourier correction therefore has mixed bound C||f||_2||g||_2. Its form operator on H is J^* F^{-1} M_{m_a-w} F J, where J:H -> L2 is the compact physical embedding proved in the previous record. Hence it is compact. Every prime cosine term is likewise a bounded physical L2 translation pairing compressed through J, and so is compact. The pole part is finite rank.

Consequently
\[
A(a)=I_H+K(a),\qquad K(a)\ \hbox{compact and self-adjoint}.
\]
The actual negative index and nullity at each fixed window are therefore finite. This is a derived fixed-window fact, not a globally finite defect-index assumption.

## Norm continuity, including prime thresholds

For the archimedean part, a -> m_a(eta) is pointwise continuous. Uniform compact-interval bounds on m_a-w give
\[
\frac{|m_a(\eta)-m_b(\eta)|}{w(\eta)}
 \le\frac{2C}{w(\eta)}
\]
in the tail. The right side tends uniformly to zero as |eta| tends to infinity. On each bounded eta interval, joint continuity gives uniform convergence as b->a. Thus the supremum of this ratio tends to zero, which proves norm continuity of the archimedean form operators on H. No digamma derivative estimate is required.

Choose a bounded positive interval of a values. Only finitely many prime powers with log(n)<=2 max(a) can contribute. On H, the cosine term is the symmetric translation compression
\[
\frac12J^*(\tau_{\log(n)/a}+\tau_{-\log(n)/a})J.
\]
Translations are strongly continuous and uniformly bounded on physical L2. Since J is compact, their action on J's unit-ball image is uniformly continuous: approximate that compact image by finitely many vectors and apply strong continuity to those vectors. Therefore each compressed term is norm-continuous in a.

If log(n)/a>=2, the two supported physical slots have disjoint interiors, and their translation pairing is zero. This includes equality: overlap at an endpoint has measure zero. Hence the omitted terms below an activation threshold are already zero as forms, and at the threshold the newly included form is zero. The finite right-limit prime index changes introduce no jump. One may use the fixed larger finite sum throughout the interval, with these zero compressions included.

The pole functionals depend continuously on a in L2(-1,1), as does sqrt(a), so their finite-rank mixed operator is norm-continuous. We have proved
\[
a\longmapsto A(a)
\]
continuous in operator norm.

## Strict initial positivity

At a_0=0.8, the previously documented external short-window positivity gives Q_a0(h)>=delta||h||_2^2, delta>0, on the actual domain. Combining with the native Gårding bound yields
\[
E_{\log}(h)\le(1+K_{a_0}/\delta)Q_{a_0}(h).
\]
Uniform equivalence under U_a0 therefore gives A(a_0)>=c I_H for some c>0.

This uses the earlier externally sourced Zhu short-window result, with its documented normalization and analytic validation limits. No larger support claim from that preprint is used. Alternatively any independently established strictly coercive starting window can replace a_0.

## First contact is attained

Define the continuous lower spectral bound
\[
\lambda(a)=\inf_{\|f\|_H=1}\langle f,A(a)f\rangle.
\]
Its continuity follows from |lambda(a)-lambda(b)|<=||A(a)-A(b)||. The lawful negative input gives lambda(a_1)<0, while lambda(a_0)>0.

Set
\[
a_*=\inf\{a\in[a_0,a_1]:\lambda(a)<0\}.
\]
Norm continuity gives a_0<a_*<a_1, lambda(a_*)=0, and A(a_*)>=0. The infimum set is nonempty by the actual negative input. If no negative input exists, this construction does not assert that set nonempty.

To prove attainment directly, choose unit f_j with q_a*(f_j,f_j)->0. Positivity implies
\[
\|A(a_*)f_j\|^2
 \le\|A(a_*)\|\langle f_j,A(a_*)f_j\rangle\longrightarrow0.
\]
Since K(a_*) is compact, pass to a subsequence for which K(a_*)f_j converges strongly. From A=I+K it follows that
\[
f_j=A(a_*)f_j-K(a_*)f_j
\]
converges strongly to a unit f_*. Continuity gives A(a_*)f_*=0.

Put h_*=U_a* f_*. This is a nonzero actual logarithmic physical vector supported in the endpoint window. The previously proved canonical source lift and full graph density attach its actual samples automatically. Moreover
\[
Q_{a_*}(g,h_*)=0\quad\text{for every }g\in D_{a_*}.
\]
In particular this is genuine native weak cancellation against every compact smooth test strictly inside the endpoint window. It is not merely a zero diagonal value.

## Actual contraction and unit-gain vector at this endpoint

Use full normalized analyses P,N at a_*, without a selected negative removal. Full-domain source/native equality gives
\[
\|Pg\|^2-\|Ng\|^2=Q_{a_*}(g)\ge0.
\]
The previous positive carrier theorem makes P a bounded isomorphism onto its closed range. Define T=N P^{-1} there. This is the actual contraction ||T||<=1, not an abstract contraction supplied as a field.

For k_*=Ph_* we have k_*!=0 by actual positive injectivity, and
\[
\|Tk_*\|=\|k_*\|.
\]
Since I-T^*T is positive, equality of its quadratic at k_* gives
\[
T^*Tk_*=k_*.
\]
The mixed null equation is also the actual source covariance identity
\[
(P^*P-N^*N)h_*=0
\]
on the canonical logarithmic form domain. All these coordinates belong to the same h_*.

If a selected-background variant removes negative coordinates, its contraction still follows at this endpoint since ||B g||<=||N g||<=||P g||. Unit gain for B on this same vector requires the removed selected energy to vanish; that condition is not asserted. Thus this is a fresh full-source endpoint constructor, not an automatic instantiation of every historical selected record.

## What this does and does not discharge

The historical concrete-constructor gap has a fresh analytic route: a lawful actual negative vector produces an actual endpoint weak-null vector, with source/native custody and full-source WD-T10 unit contraction at that endpoint. No raw synthesis preimage, retained H1 regularity, or unbounded physical operator-domain membership is needed.

The supplied negative vector is still an independent prerequisite. Neither the finite-packet interpolation records nor raw copy counting have supplied one. This record does not declare an actual endpoint instantiated without it, and does not recover the historically retained record by renaming its fields.

The weak-null identity is proved on the endpoint test domain. Inclusion into a larger carrier preserves source coordinates but does not give vanishing against newly admitted tests. Enlarged cancellation/persistence remains open.

The native mixed compact-test identity here is not automatically a typed frozenWeilCompactAction statement if that statement requires an additional temperate-symbol premise or carrier dictionary. Those premises must be discharged in their own right; this proof does not infer all symbol derivatives from a zeroth-order log bound. Boundary-removal hypotheses are not supplied silently.

No global selected-background unit bound beyond the existing scope is claimed. FULL TRANSPORT CLOSED and F4 entry remain open.

## Validation and cursor

Analytic proof. It uses the preceding actual source/logarithmic carrier results and the previously documented short-window positivity input. No Lean source/workflow changes, no numerical endpoint, and no new CI claim. Existing certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At e130cd0, the actual native Weil forms, pulled back by physical L2 dilation to one supported logarithmic domain, form a norm-continuous self-adjoint family A(a)=I+compact. Prime support thresholds create no form jump: the threshold translation compression is zero and compact physical embedding upgrades strong translation continuity to form-operator norm continuity. If a lawful larger-window negative vector is supplied, the first nonpositive boundary after the certified short positive window has nonzero attained kernel. Its actual physical logarithmic vector has full source custody, Q=P^2-N^2>=0 on that endpoint domain, all native mixed pairings zero, and a unit-gain vector for the actual contraction T=N P^{-1}. This is a fresh analytic actual endpoint constructor, not recovery of the historically retained record and not an assertion that actual negativity exists. Without a negative vector the endpoint is not asserted finite. General selected-background domination and enlarged weak-null persistence remain open; no frozen-action temperate/domain premise or boundary-removal hypothesis is silently supplied. Lean unchanged; FULL TRANSPORT CLOSED and F4 entry remain open.
