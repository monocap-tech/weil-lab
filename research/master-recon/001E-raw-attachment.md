# MASTER-RECON-001E — Raw coefficient attachment and MTP-2 adjudication

2026-11-24. INVESTIGATE; ADOPT 0. Paper proof using classical full Weil explicit formula and 001D, not a Lean certificate. Previous investigations remain stayed.

## 1. Complete finite-off-axis model, with explicit metric

Let H be the actual multiplicity-weighted zero-evaluation Hilbert space in signature coordinates H_+ ⊕ H_-. One coordinate per distinct zero with sqrt(multiplicity) weight suffices; if copies per multiplicity are retained, use the fixed equal-copy analysis and corresponding orthogonal complement. For a conjugate pair of ordinates with equal multiplicity, the symmetric and antisymmetric coordinates are the unitary sum and difference divided by sqrt(2); real ordinates give positive channels. Use the conjugate pairing and Fourier sign consistently in the full explicit formula. Thus on original smooth compactly supported complex tests, with raw analysis A,
$$
W(f,h)=\langle J A f,A h\rangle,\quad J=I_+\oplus(-I_-),\quad
\|Af\|^2=W(f,f)+2\|A_-f\|^2.
$$
Assume finitely many off-critical-line zeros, so H_- is finite dimensional. This is a conditional branch, not an assertion that any such zeros exist. Use all negative channels in this model, not an arbitrary selected packet.

For t>0 define X_t as the zero-extended functions supported in [-t,t] with finite norm
$$
\|f\|_{\log}^2=(2\pi)^{-1}\int\log(2+|\xi|)|\hat f(\xi)|^2d\xi.
$$
Smooth tests supported strictly inside (-t,t) are dense: inward dilation tends strongly to identity in the weighted Fourier L² space (first for continuous compactly supported Fourier functions, then by uniform boundedness of dilations near 1 and density); mollification with radius below the resulting support gap converges by dominated convergence. X_t embeds compactly into L²: Fourier tails are uniformly small on its unit ball, and restriction to bounded Fourier frequencies of the Fourier transform of functions supported in [-t,t] is Hilbert-Schmidt. The physical form extends continuously on X_t by logarithmic Gamma growth and bounded fixed-window prime and pole operators.

Each of the finitely many negative channel evaluations is L² bounded on X_t by Cauchy-Schwarz over the compact window and the bounded complex exponential. Consequently
$$
\|f\|_{\log}^2-C_t\|f\|_2^2\le\|Af\|^2\le C'_t\|f\|_{\log}^2.
$$
The upper bound extends A by density to X_t. Every coordinate is still the original integral evaluation, since evaluation is continuous in L² on fixed support. The extensions are consistent on nested windows and polarization retains the original W identity. For distinct zeros, pairing uses equal multiplicities; if an archive uses a different metric, its isometric identification must be checked rather than presumed.

## 2. Remove the L² defect by 001D

First A is injective on X_t. If Af=0, take any larger T>t. The extended A_T has the same coordinate evaluations and A_T f=0. Thus W(f,h)=0 for all smooth h supported in (-T,T), equivalently Wf=0 there distributionally by the original physical form. By 001D (with c=t and epsilon=T-t), f=0. This avoids a distinct-zero counting lower bound.

Now suppose no positive lower bound for ||Af||/||f||_log exists. Choose f_n in X_t with norm_log=1 and Af_n->0. After taking a subsequence f_n converges weakly in X_t and strongly in L² to f. Boundedness of A gives Af=0, hence f=0. But the lower estimate then contradicts norm_log=1. Therefore
$$
b_t\|f\|_{\log}^2\le\|Af\|^2\le B_t\|f\|_{\log}^2,\quad b_t>0.
$$
The raw range R_t=A(X_t) is closed, and equals the closure of the raw analysis of original smooth supported tests.

## 3. Exact raw gap attachment

Define the raw gap space G_t=R_t^perp, equivalently the annihilator of all smooth tests supported in (-t,t) under the unweighted signature-coordinate Hilbert product. This is the distributional raw synthesis gap definition; if a historical Green synthesis is merely an injective transform of this distribution on the window, its kernel agrees. Exact equality to the historical selected/background regularized construction is NOT assumed.

For T>c, each R_t for c<t<T is a subspace of R_T. Injectivity of A_T ensures that a vector in their intersection has one and the same physical preimage supported in every [-t,t], hence in [-c,c]. Therefore intersection_{t>c}R_t=R_c, and closure union_{t>c}G_t=G_c. The decreasing-gap projections converge strongly to P_Gc from the right (increasing subspaces as t decreases). Compression to finite-dimensional H_- gives norm convergence. No separate right-jump assumption is necessary in this raw complete finite-exception model.

Let ell:H->H_- be the negative-coordinate projection and ell* its inclusion; Gamma_t=ell P_Gt ell*. For u in E=ker(Gamma_c-I/2), put v=P_Gc ell*u. Its negative coordinate is u/2, and ell*u-v=P_Rc ell*u has coordinates (-v_+,u/2). Hence
$$
Jv=v-\ell^*u=-P_{R_c}\ell^*u\in R_c.
$$
Closed range and injectivity give a unique k_u in X_c with Ak_u=Jv. Then JAk_u=v, and W(k_u,h)=<v,Ah>=0 for all h in X_c. Moreover A_-k_u=-u/2, so k_u=0 iff u=0. This is an exact linear injective physical realization, with the factor 1/2 accounted for. For t>c,
$$
v\in G_t\iff W(k_u,h)=0\ \forall h\in X_t
\iff Wk_u=0\text{ distributionally on }(-t,t).
$$
Thus 001D gives v in G_t iff u=0. The shell-loss compression is positive definite on nonzero E for every t>c. If Gamma_c>=I/2, 001A gives n_-(Gamma_t-I/2)=dim E for sufficiently close t>c. Raw complete finite-exception MTP-2 is equivalent to E=0, not to a persistence theorem for nonzero neutral directions.

## 4. First contact in this model

For y=Af in R_t,
$$
W(f,f)=\|y\|^2-2\|\ell y\|^2.
$$
Thus W_t>=0 iff ||ell P_Rt||²<=1/2 iff ell P_Rt ell*<=I/2 iff Gamma_t>=I/2 (ell ell*=I). At a genuine first-contact radius with positivity through c and negative tests in every larger window, the right norm convergence and finite-dimensionality imply E nonzero: otherwise Gamma_c>I/2 would persist for small t>c. Positivity through c follows from smaller-window positivity and inward smooth approximation; existence of a finite such c under a hypothetical off-line zero follows from the full Weil criterion and initial positivity. These are conditional implications, not a demonstration of any off-line zero. In this model MTP-2 would fail at first contact, exactly as required by such a hypothetical failure of RH; ruling it out is equivalent to excluding that contact rather than an independently easier continuation principle.

## 5. Critical scope warning: selected negative packet

If ell selects only M⊂H_- rather than all negative channels, write J_M=I-2 ell*ell. The projection argument then yields A k_u=J_M v, NOT necessarily Jv. Its corresponding form is
$$
W_M(f,h)=W(f,h)+2\langle A_{-,M^\perp}f,A_{-,M^\perp}h\rangle.
$$
Unselected negative coordinates are turned positive. This is not the original full signed translation-invariant Weil form; absolute squared off-axis evaluations in the changed channels need not be invariant under translations. Unless all negative channels are selected, or the unselected negative block is shown to vanish on the relevant mode and tests, 001D cannot be imported into that packet-specific argument. If an archive instead uses an indefinite background elimination, that metric and gap space must be separately identified; ordinary raw compression must not be substituted.

## 6. Adjudication

- 001D physical two-sided non-persistence: paper proved, unconditional for the stated physical operator.
- Complete raw finite-off-axis coefficient realization: paper proved using the classical full polarized explicit formula, with all negative channels selected.
- Complete raw finite-off-axis MTP-2: equivalent to absence of neutral space; nontrivial persistence impossible.
- Exact equality with every historical selected/regularized Green marker: OPEN. Historical source search recovered the physical adjoint identities but a direct GitHub fetch of historical checkpoint at 3d8a784bde4e31c173d4ac4d3b7b60dfc11e30bc returned 404.
- Infinite-exception branch, general MTP-1, neutral-space exclusion and RH: OPEN.
- Do not declare the full original packet-specific MTP-2 route falsified until its native marker is audited.

Recommend closing the complete-physical persistence subgate negatively and keeping the reconciliation open only for exact packet-specific typing/adjudication, or user-ordered stay. No release of other investigations.
