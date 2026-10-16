# RPB108 SI21 — fourth independent original signed Jensen window

**Parent:** SI20 merged as `6e208e2a0f06c32ca234f1f32720e021df38fe80` (PR #115).  
**Track:** SI independent supported-frequency structural investigation; native RC high-Schur work stays primary and independent.  
**Scope:** one original physically supported odd-pole inverse **upper comparison only**. This is not the SI11 full signed Birman–Schwinger matrix, a proof of Weil positivity, Stage I, F4, Lean, or RH.

## New independent positive direction

Keep the exact three SI20 certified all-frequency windows, with centers `(3/10, 19/25, 6/5)`, radius `r=1/50`, and certified positive signed-multiplier margins `(27/10, 5/4, 17/20)`. Add the genuinely independent fourth positive-frequency window centered at

\[
c_4=33/20=1.65,\qquad J_4=[163/100,167/100],\qquad \delta_4=7/10.
\]

The unchanged SI06 original **signed** seven-prime cosine interval enclosures and SI13 monotone archimedean lower bounds are replayed on **128 cells for each of all four windows**, charging the whole-cell global Lipschitz bound `|p'|<69`. The validator must strictly prove `m(ξ)>κ+δ_j` throughout all four reflected windows, with `κ=1/1000`; numerical sample values do not count as certification.

For each window, use the **true** physical frequency-averaged sine feature
\[
g_j(x)=\sin(2\pi c_j x)\operatorname{sinc}(2\pi r x)
=\frac1{2r}\int_{c_j-r}^{c_j+r}\sin(2\pi \xi x)\,d\xi
\quad (|x|\le11/10).
\]
The exact Jensen/variance identity on the original odd physical Hilbert space yields
\[
A_o\succeq C_{o,4}
=\kappa I_o+\sum_{j=1}^4(4r\delta_j)|g_j\rangle\langle g_j|.
\]
The original positive floor is unchanged. Since the four windows are pairwise disjoint, this is an independently certified positive-frequency contribution, rather than merely splitting an old window.

## Full signed 4×4 physical inverse comparison

For the genuine physical Gram `H_{ij}=⟨g_i,g_j⟩` and original odd source overlaps `q_i=⟨g_i,s⟩`, let `Γ=diag(4rδ_j)` and `M=Γ^-1+H/κ`. The order-reversing inverse and Woodbury identity establish
\[
2\langle s,A_o^{-1}s\rangle
\le2\left(\frac{\|s\|^2}{\kappa}-\frac{q^*M^{-1}q}{\kappa^2}\right).
\]
The validator computes rigorous physical overlap intervals for **all sixteen Gram entries and all four source overlaps**. The true frequency-averaged functions remain in the operator theorem. Three-point Simpson quadrature is **only an interval-enclosure device**, with rigorous fourth-frequency-derivative remainder
\[
\tau\le(4\pi rB)^4/2880<3\cdot10^{-6},\quad B=11/10.
\]
All physical signed cross terms retain their actual signs; none are deleted or diagonally dominated by assumption.

For the exact rational variational witness `z`, with its midpoint approximation used **only to choose a candidate**, certify
\[
q^*M^{-1}q\ge 2z^*q-z^*Mz
\]
using outward intervals of the original physical quantities, and assert the **strict rational gate**
\[
\boxed{2\langle s,A_o^{-1}s\rangle<4.}
\]
This is stronger than SI20's certified `<5` **only if the entire new validator and CI run pass**. The independently established SI20 certificate remains replayed by the same workflow.

## Matrix-valued bridge toward the actual SI11 signed coupling

The fourth-window Loewner comparison is **not restricted to the pole**. Let G:C^4→H_o synthesize the four true physical features, and let V:C^d→H_o be any finite physically supported odd input synthesis map. Define D=G*V and the true input Gram N=V*V. Because inversion reverses the Loewner order, the same original-reference comparison gives the exact **matrix-valued** inequality

\[
\boxed{ V^*A_o^{-1}V\ \preceq\ V^*C_{o,4}^{-1}V
=\kappa^{-1}N-\kappa^{-2}D^*M^{-1}D.}
\]

Every off-diagonal entry in D matters. This gives a correct-sign supported upper bound for *all* finite odd input directions at once; it does not require independently solving the actual supported operator equation A_o y=v for each vector.

For example, restrict SI11's original positive compact negative operator to the **odd** physical sector, take its exact projected finite block K_{o,b}=V Σ V* ≥0, and retain an independently certified operator-norm remainder η_b. An explicit sufficient **odd-sector** test is

\[
\lambda_{\max}\!\left(
\Sigma^{1/2}[\kappa^{-1}N-\kappa^{-2}D^*M^{-1}D]
\Sigma^{1/2}\right)+\eta_b/\kappa\le1.
\]

This is a conditional transfer theorem, **not** a numerical BS spectral certificate. For a complete original-form conclusion, the even parity block, the physical negative-frequency couplings and sufficient residual bounds must also be certified. A dense SI11 matrix at dimension about 1561 may remain less efficient than RC's native high-Schur method. The rank-four reference is a reusable upper comparison, not a demonstrated computational shortcut.

## What SI21 does not establish

The SI11 full signed negative-frequency compact operator includes
\[
K=Z^*\mathcal F^{-1}(\kappa-m)_+\mathcal F Z+2|s\rangle\langle s|.
\]
Its true supported Birman–Schwinger norm and the associated matrix/cross-couplings are still uncomputed. The one-pole threshold `2⟨s,A_o^-1s⟩≤1` is **not** asserted; reaching it would not by itself control the rest of `K`.

The best next structural handoff is to transfer the four-direction positive Loewner reference into a correct-sign **matrix-valued** bound for physically supported negative-frequency input vectors, and compare its dimension and residual budget against RC's native high-Schur chain. SI11 gives a conditional finite matrix gate but no passing full signed inverse matrix certificate.

**Reproduce:** `python scripts/validate_rpb108_si21_odd_jensen_four.py`. All acceptance inequalities use `Fraction` exact rational arithmetic. The analytic operator argument is not a Lean proof or an independent peer-reviewed validation.
