# RPB108: actual two-column off-line pairwise gain obstruction

Base: research 663be46e074cc9c7875b64782d90baff2dd944ef.

## Minimal theorem

For every \(a>0\) and every actual open-strip zeta zero point \(\rho\) with \(\operatorname{Re}\rho\ne1/2\), there is an explicit finite actual Green coefficient vector v, supported on one copy of \(\rho\) and one copy of its actual partner \(1-\bar\rho\), such that its unchanged physical vector \(h=G_{\rm physical}v\) satisfies
\[
F_h(\bar z)=1,\qquad F_h(z)=-1,\qquad z=-i(\rho-\tfrac12).
\]
Here \(F_h(w)=\int_{-a}^{a}h(x)e^{iwx}\,dx\). The normalized plus coordinates vanish at every copy of these two points, while the normalized minus coordinates are 1 at \(\rho\) and -1 at its partner.

The theorem is parameterized by an actual off-line point. It does not assert that one exists. It constructs a lawful finite Green packet, not a retained WD-T38 witness.

## Explicit constructor and proof

Let \(z_1=z\), \(z_2=\bar z\). These are distinct because the ordinate imaginary part is \(1/2-\operatorname{Re}\rho\). Both are actual zero-point ordinates by the certified partner symmetry, and their Green denominators are nonzero by the actual open-strip theorem.

Write \(g_1,g_2\) for their explicit endpoint-corrected Dirichlet Green columns on \([-a,a]\). Define
\[
\mathcal E(u,v)=\int_{-a}^{a}\overline{u'}v'\,dx
 +\tfrac14\int_{-a}^{a}\bar u v\,dx,\quad
H_{ij}=\mathcal E(g_i,g_j).
\]
All these integrals are ordinary integrals of explicit smooth columns. The existing Lean theorem dirichletProblemOneColumn_green_mixed gives
\[
H_{ij}=\int_{-a}^{a}\overline{e^{-iz_i x}}g_j(x)\,dx
      =F_{g_j}(\bar z_i).
\]
Endpoints vanish, so integration by parts has no boundary term. No spectral operator-domain premise is used.

The two Green columns are linearly independent. A zero finite L2 combination is continuous and hence zero throughout the interior interval. Apply the pointwise differential expression \(-d^2/dx^2+1/4\) to obtain a zero combination of \(e^{-iz_1x},e^{-iz_2x}\). Distinct-frequency exponential independence, already proved and specialized to actual source modes in Lean, forces both coefficients to vanish.

H is therefore Hermitian positive definite: for a nonzero coefficient pair c,
\[
c^\ast Hc=\mathcal E(c_1g_1+c_2g_2,c_1g_1+c_2g_2)>0,
\]
because the physical L2 term is strictly positive. Set
\[
d_1=H_{11}>0,\quad d_2=H_{22}>0,\quad C=H_{12},\quad
D=d_1d_2-|C|^2>0.
\]
D>0 follows by applying positivity to \(g_2-(C/d_1)g_1\), nonzero by independence; its energy is \(d_2-|C|^2/d_1>0\).

Choose
\[
c_1=(d_2+C)/D,\qquad c_2=-(d_1+\bar C)/D.
\]
Direct multiplication gives \(H(c_1,c_2)^t=(1,-1)^t\). Thus \(h=c_1g_1+c_2g_2\) has the claimed evaluations.

Choose lawful copy index 0 in each nonempty actual multiplicity fiber and set
\[
v=c_1e_{(\rho,0)}+c_2e_{(1-\bar\rho,0)}.
\]
Its actual whole Green graph lift exists by the certified constructor. Its physical coordinate is exactly h by synthesis linearity and the certified single-coordinate formula. Both full source coordinates belong to this unchanged vector. No unproved full-graph membership or new source quadratic premise is used.

The certified dictionary now gives plus \((1+(-1))/2=0\) and minus \((1-(-1))/2=1\) at the first point. Partner symmetry gives plus 0 and minus -1 at the second.

## Exact pairwise obstruction

Retain only the plus coordinates and unselected minus coordinates of these two fibers, calling the restricted maps \(P_{\rm orbit}\) and \(B_{\rm orbit,s}\). If at least one orbit copy is unselected,
\[
P_{\rm orbit}Gv=0,\qquad B_{\rm orbit,s}Gv\ne0.
\]
Local kernel inclusion fails. No finite C can make
\[
\|B_{\rm orbit,s}Gv\|\le C\|P_{\rm orbit}Gv\|
\]
hold for every actual finite Green packet. Thus a pairwise contraction or any finite pairwise gain bound is unavailable on an actual unselected off-line orbit.

The global positive operator retains all actual zero coordinates. This restricted failure does not prove failure of global kernel inclusion.

## Remaining global sign test on this exact packet

Let m be the common actual multiplicity, k the selected raw copies across the two fibers, and \(r=2m-k\). This orbit contributes exactly -r to the background form. The complete same-vector form is
\[
Q_{B,s}(Gv)=-r+Q_{\rm rest}(Gv),
\]
where Q_rest includes every other actual zero copy with unchanged selection and normalization. The complete series converges by certified Green source summability, so removing a finite orbit is lawful.

Global positivity on this packet requires \(Q_{\rm rest}(Gv)\ge r\). A strict inequality \(Q_{\rm rest}(Gv)<r\) would certify a lawful finite negative packet. Neither comparison is established.

A successful unit estimate must use observations at other zero points or another global signed estimate. Compact support, small off-line displacement, finite independence and partner symmetry do not force a same-orbit plus/minus estimate. The inverse-Gram coefficients need not be uniformly bounded as the ordinates approach one another; no conditioning floor is asserted.

## Formalization and validation boundary

This interpolation and pairwise obstruction are analytic proofs, not newly Lean formalized. They use the certified mixed Green law, actual partner/nonresonance facts, finite source independence, finite synthesis custody and normalized coordinate dictionary. A numerical complex-matrix multiplication checked the displayed inverse formula only; it is not a zero or sign certificate.

No Lean source or workflow changes here. The latest certified Lean head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125 / job 111535430775: Lean 4.34.0, isolated 9178/full 9205 jobs, five standard-axiom audits. No CI certification is claimed for this new analytic constructor.

No actual off-line point existence, retained source/null membership, full graph density, simplicity, spectral operator-domain membership or background positivity is assumed. FULL TRANSPORT CLOSED remains open.

## Updated cursor/residue

At 663be46, an analytic two-column constructor proves that any actual off-line partner pair admits a lawful finite Green packet with evaluations F(conj z)=1 and F(z)=-1. Orbit plus coordinates vanish and minus coordinates are +/-1 on the same full graph vector. If any orbit copy is unselected, orbit-local kernel inclusion and every finite pairwise gain bound fail. Global positive observations at other zero points remain. The orbit contributes -r, r=2m-k, and the outstanding test on this exact packet is Q_rest >= r (global compensation) or Q_rest < r (finite negative certificate). Neither is established. The constructor and obstruction are analytic proofs, not Lean formalizations; no source/workflow changes or new CI claim. No actual off-line zero existence, conditioning floor, retained source/null membership, full graph density or background positivity is assumed. Next substantive work must control the complementary zero contribution on this unchanged packet or prove a global same-vector sampling budget; do not seek a per-orbit contraction. WD-T38 attachment remains independent. FULL TRANSPORT CLOSED is open; SOURCE stays off the critical path.
