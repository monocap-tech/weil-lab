# RPB108: vanishing horizontal contours leave an actual vertical-bulk obstruction

Date: 2026-10-07 UTC. Recovered live head 569005007b2bb267a44794ee60f33d15b6a9e11c and its current cursor.
Definitions: [good-height contour reduction](../docs/TERMINOLOGY_RPB108_GOOD_HEIGHT_CONTOUR.md).
Category: actual sharp-head arithmetic / contour framework. Analytic, not Lean-certified.

## Result

For every finite family F in D_a there is an unbounded sequence T_n of actual good ordinates such that BOTH outer horizontal contour integrals for the first-height holomorphic quadratic weight tend to zero. Moreover

    S_F(T_n)-B_F(T_n) -> a finite real constant.

For an actual nonzero unshifted contact kernel, the already proved sharp/log theorem therefore gives

    B_K(T_n)/log T_n -> (2/pi)Lambda_K>0.

The horizontal-edge theorem is proved below without nullity. Hence it also holds for the pinned actual rough positive eigenmode, whose vertical bulk has the same strictly positive normalized limit. It does not supply bounded sharp returns. This proves a precise failure of the candidate inference: good ordinates + vanishing horizontal edges + actual source range -> bounded/sublogarithmic sharp subsequence.

The contour path has one fewer analytic error term to control, but the global dependency graph is unchanged. The missing actual arithmetic theorem remains liminf S_K/log T<=0; on this lawful contour sequence it would suffice to prove a nonpositive vertical-bulk liminf USING the exact unshifted mixed-null equation. That sign is not proved here. No endpoint-regularity, compactness or Abel-transfer investigation is restarted.

## 1. Holomorphic residue weight and a bounded transverse correction

Write rho=1/2+beta+i theta, using the transverse orientation compatible with z=theta+i beta. Reversing that orientation merely relabels the functional-equation pair. The previously registered raw convention gives

    H_h(rho)=p_rho+n_rho,
    conjugate(H_h(1-conjugate(rho)))=conjugate(p_rho-n_rho),
    W_h(rho)=d_rho+2i Im(n_rho conjugate(p_rho)),
    d_rho=|p_rho|^2-|n_rho|^2.

Consequently Re W_h(rho)=d_rho and |W_h(rho)|<=v_rho=|p_rho|^2+|n_rho|^2. These identities include every raw multiplicity copy, with no auxiliary rows.

On the positive rectangle (1-c,c) x (t0,T), use f_+(s)=r(s)W_F(s)A(s). On the negative rectangle (1-c,c) x (-T,-t0), use f_-(s)=-r(s)W_F(s)A(s). Both contours have positive orientation. xi is entire; the only enclosed poles of A are actual nontrivial zeros, each with residue its multiplicity. There are no pole or trivial-zero residues for xi. Local zero counting makes each rectangle finite. At an actual zero,

    Re[sign(theta) r(rho) W_F(rho)]
       =|theta| Re W_F(rho)+sign(theta) beta Im W_F(rho).

Thus the sum of real contour residues is S_F(T) minus the fixed low head, plus

    E_F(T)=sum_(t0<|theta|<T) sign(theta) beta Im W_F(rho).

The accepted |beta|<=3/8 and complete base source square summability give

    sum |beta Im W_F(rho)| <=(3/8) sum_h ||Gamma h||^2<infinity.

Therefore E_F(T) converges absolutely to a finite constant. This correction cannot change a logarithmic coefficient. No full mixed-null assumption has been used, and no infinite residue interchange has been made.

## 2. Weighted strip energy is integrable

For sigma in [1-c,c]=[-1/2,3/2], H_h(sigma+it) is the ordinary Fourier transform, up to the registered frequency normalization/sign, of e^((sigma-1/2)x)h(x). Multiplication by these smooth bounded factors on the fixed compact support is uniformly bounded on D_a. One direct proof uses a smooth compact cutoff equal to one on [-a,a]: its weighted Fourier convolution kernel has uniformly bounded Schwartz seminorms, and log(e+|xi+eta|)<=log(e+|xi|)+log(e+|eta|). Weighted Young then bounds the logarithmic Fourier norm uniformly over sigma.

Plancherel, Tonelli and the finite family sum therefore prove

    integral_2^infinity log T L_F(T)dT<infinity.

This is canonical form energy, not derivative regularity, a zero-density improvement or a critical source-moment estimate. W_F on a horizontal edge satisfies

    integral_(1-c)^c (|W_F(sigma+iT)|+|W_F(sigma-iT)|)d sigma
       <= L_F(T),

by |ab|<=(|a|^2+|b|^2)/2 and sigma-reflection of the second factor.

## 3. Actual good heights with enough measure for simultaneous selection

Primary source: Kiran S. Kedlaya, [Notes on analytic number theory, chapter 9](https://kskedlaya.org/ant/chap-von-mangoldt.html), Lemmas 9.4 and 9.6. They supply the O(log T) unit-interval zero count and the local expansion of zeta'/zeta by nearby zeros, uniformly for -1<=sigma<=2. Multiplicities are retained. No RH hypothesis is used.

This audit needs a positive-MEASURE set of good heights, not merely one preselected point in each unit interval. In [m,m+1], there are at most C log m relevant ordinates in [m-1,m+2]. Removing intervals of radius eta/log m around them removes at most 2C eta measure. Choose eta small so this is <=1/2. Ordinates farther away cannot obstruct the resulting separation. Using comparable logarithms gives a fixed positive separation constant eta' and a measurable E with |E intersect [m,m+1]|>=1/2 for all large m. Conjugation gives simultaneous avoidance at -T.

The local expansion now gives |zeta'/zeta(sigma +/- iT)|=O(log^2 T) on E throughout our horizontal strip. The elementary completed-factor logarithmic derivatives add O(log T) by Stirling; hence |A|=O(log^2 T) there as well. Our strip [-1/2,3/2] is within the cited [-1,2] range.

Since E has that uniform measure,

    integral_E dT/(T log T)=infinity.

If liminf_(T in E ->infinity) T log^2 T L_F(T)>0, the weighted strip integral in section 2 would dominate a positive multiple of this divergent integral. Contradiction. Choose successively T_n in E tending to infinity with

    T_n log^2 T_n L_F(T_n)->0.

This selection is for the WHOLE finite family at once. It does not assume pointwise Fourier decay at a previously chosen arithmetic sequence. Each outer horizontal integral has magnitude O(T_n log^2 T_n L_F(T_n)), so it tends to zero. This closes the horizontal contour estimate rigorously.

## 4. Exact vertical reduction and the unresolved sign

For every h, W_h(1-conjugate(s))=conjugate(W_h(s)), while the completed functional equation gives A(1-conjugate(s))=-conjugate(A(s)) and r(1-conjugate(s))=conjugate(r(s)). Thus on each rectangle the downward left vertical edge and upward right vertical edge combine to twice the real part of the right-edge integrand. Parameterizing the positive and negative right sides gives EXACTLY B_F(T) in the registry, with coefficient 1/pi. No real-vector or conjugation-invariance assumption on F is needed.

The two inner horizontal edges at +/-t0 are fixed finite integrals. Let their combined real contribution be I_F and the fixed low sharp head be S_low. The finite residue identity is

    S_F(T)=B_F(T)+outer_horizontal(T)+I_F+S_low-E_F(T).

At T_n, the horizontal contribution tends to zero and E_F converges. This proves the stated finite-limit difference.

On Re s=c=3/2 one may also use the absolutely convergent prime series

    A(s)=1/s+1/(s-1)-(log pi)/2+psi(s/2)/2
            -sum_(n>=2) Lambda(n)n^(-s).

For each finite T, compactness of the integration interval and absolute convergence justify this substitution and termwise integration. This displays an actual prime/gamma vertical integral, not a generic density statistic. It gives no sign: the entire weight W_F is not positive on the shifted line, and the height factor is not an admissible unchanged physical null test.

Full unshifted mixed-nullity says Gamma*J Gamma h=0 on the same supported carrier. It does not say W_F(rho)=0 at every zero or that the vertical integral is zero. The previously pinned source-graph obstruction already rules out silently using a nonzero finite height packet as a supported physical null test; we consume that result rather than re-investigate it. A new unshifted-null cancellation for this vertical integral would still have to be proved and audited against mu h. Neither good-height selection, the functional equation nor the seven-eighths strip supplies it.

## 5. Required controls and custody

| Control | Outcome |
|---|---|
| Actual rough positive eigenmode | Belongs to D_a and the ACTUAL source range, so the same cap-vanishing sequence and finite transverse correction apply. Its proved positive sharp/log slope forces positive vertical/log slope on every selected sequence. This decisively rejects cap-vanishing as an exclusion mechanism. Its interior residual mu h remains nonzero. |
| Artificial compact-good-row logarithmic control | Has positive slope but no actual xi residue interpretation. It cannot be used to assert the contour identity; it continues to refute generic compactness/density arguments. |
| Fixed finite actual restoration | Alters the sharp head by a bounded constant. The correction is absolutely summable and finite restoration cannot change the normalized logarithmic obstruction. No restored effective background is renamed actual null. |
| Two-row comparison contact | Its auxiliary rows are not xi zeros. The actual component admits the contour identity, but the added rows must be kept separately; no augmented mixed-null equation is substituted for the unshifted actual one. |

Internal source blobs and the primary external locations are pinned in the companion JSON. The companion exact rational checks test the complex residue/transverse-correction sign, vertical reflection/orientation, logarithmic critical selection budgets, and rejection of horizontal-vanishing-to-bounded-bulk. They do not certify an actual arithmetic sign theorem. The infinite selection and contour proofs are analytic, not Lean formalizations.

No bounded-above sharp sequence, nonpositive actual liminf, global endpoint exclusion or F4 closure is claimed. The global graph and smallest arithmetic theorem remain unchanged. The candidate contour path now has vanishing horizontal edges and a convergent transverse correction available; its vertical-bulk sign remains the independent unshifted arithmetic task.
