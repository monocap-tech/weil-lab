# SM26 — Three-negative-direction obstruction in the COMPLETE original 890-column SI29-conditioned odd Schur

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM25 draft PR #206.**
This checkpoint gives an **actual original complete-negative-cap method obstruction** and a quantitative **negative-index lower bound on the old fourteen-feature SURROGATE Schur**. It **DOES NOT** establish a negative eigenvalue for the true original full positive odd operator \(A_o\), pole-conditioned \(A_*=A_o-2|s\rangle\langle s|\), or signed Weil form; it does **not** discharge PS36 whole-operator O1/O2. The correct next method needs additional ORIGINAL positive-frequency response, not further entrywise refinement of the unchanged SI29 C14 reference.

## 1. The two operators must never be conflated

On the true original physically supported odd carrier \(H_o=L^2([-11/10,11/10])_{\rm odd}\), define
\[
A_*=A_o-2|s\rangle\langle s|\succeq B_{14},
\qquad B_{14}=\kappa I+\sum_{i=1}^{14}\gamma_i |g_i\rangle\langle g_i|-2|s\rangle\langle s|,
\quad \kappa=1/1000.
\]
The actual original SI29 fourteen-feature reference has rank at most 14 ABOVE its scalar floor. The negative odd pole is **subtractive**, never a positive extra direction. The existing SI29 positive-floor and pole-response proof gives \(B_{14}\succeq \kappa_* I\), \(\kappa_*=33621/10^9\).

SM10's genuine ORIGINAL signed seven-prime negative-frequency operator and its whole-frequency Taylor **upper** obey
\[
0\preceq K_{\neg,o}
\preceq Q_{890}+\eta I,\quad
Q_{890}=U D U^*,\quad
D=(1+\tau)C\succ0,\quad\tau=1/1024,\quad 0<\eta<302/10^{12}<\kappa_*.
\]
\(U\) contains **ALL 890 original odd physical sine-Taylor columns**, and \(C\) is the original exact 107-block SPD moment covariance (not diagonalized or reduced to the first two). The true original acceptance uses
\[
\boxed{S_{890}^{\rm true}:=D^{-1}-U^*(A_*-\eta I)^{-1}U\succeq0.}
\]
This remains **OPEN**; SM25 computes only the first two source columns.

The unchanged fourteen-source **surrogate** is instead
\[
\boxed{S_{890}^{(14)}:=D^{-1}-U^*(B_{14}-\eta I)^{-1}U.}
\]
Even though its explicit full 890×890 entries have not been assembled, its **negative index can already be classified from below**, by a complete-operator min-max argument.

## 2. True original SM11 17-packet spectral lower, not 17 chosen point samples

SM11's exact continuous original seven-prime frequency windows and 17×17 physically supported signed Gram establish
\[
K_{\neg,o}\succeq \gamma GG^*,
\quad \gamma=2/125,\quad
G:\mathbb R^{17}\to H_o,\quad
G^*G\succ(4/5)I.
\]
All seventeen true functions are continuous-frequency Jensen packets, with **every one** of their physical signed cross-Gram entries paid. Their actual span \(V_{17}=\operatorname{ran}G\) is 17-dimensional. On all \(v\in V_{17}\),
\[
\boxed{\langle v,K_{\neg,o}v\rangle>
\gamma\frac45\|v\|^2
=\frac8{625}\|v\|^2.}
\]
Indeed the nonzero spectra of \(GG^*\) on \(\operatorname{ran}G\) and \(G^*G\) coincide, and the latter has certified lower eigenvalue \(>4/5\). This uses the **complete original negative-frequency operator** as the lower side, not a finite negative cap surrogate.

Let \(F_{14}=\operatorname{span}\{g_i:1\le i\le14\}\), and choose the actual **orthogonal intersection**
\[
T=V_{17}\cap F_{14}^{\perp}.
\]
By dimension counting \(\dim T\ge17-14=3\). For every \(v\in T\), the original reference positive rank-14 response vanishes, and the original negative odd pole can only lower \(B_{14}\):
\[
\langle v,B_{14}v\rangle
=\kappa\|v\|^2-2|\langle s,v\rangle|^2
\le\frac1{1000}\|v\|^2.
\]
Therefore, with **all** original negative frequencies included,
\[
\boxed{
\langle v,(B_{14}-K_{\neg,o})v\rangle
<-\biggl(\frac8{625}-\frac1{1000}\biggr)\|v\|^2
=-\frac{59}{5000}\|v\|^2,\quad v\in T.
}
\]
There are **at least three independent genuinely original odd physical test directions defeating the SI29 B14 full-negative dominance**. Nothing about the positive spectrum of the actual \(A_*\) on these directions has been decided.

## 3. NEW: transfer the obstruction through the FULL original SM10 negative-cap bound to the 890×890 surrogate Schur

Because \(K_{\neg,o}\preceq UDU^*+\eta I\), subtracting the actual **complete** original cap yields
\[
B_{14}-\eta I-UDU^*\preceq B_{14}-K_{\neg,o}.
\]
Hence the same full \(T\), without selecting two special negative-source columns, satisfies the strictly negative bound
\[
\boxed{
\langle v,(B_{14}-\eta I-UDU^*)v\rangle
<-\frac{59}{5000}\|v\|^2\quad\forall v\in T.
}
\]
This implies
\[
\boxed{\operatorname{ind}_{-}(B_{14}-\eta I-UDU^*)\ge3.}
\]

Now use the complete two-sided Schur inertia (Haynsworth/Sylvester congruence) of the self-adjoint block on \(H_o\oplus\mathbb R^{890}\),
\[
\mathcal B=
\begin{pmatrix}
B_{14}-\eta I&U\\ U^*&D^{-1}
\end{pmatrix}.
\]
Both diagonal reference factors \(B_{14}-\eta I\succ0\) and \(D^{-1}\succ0\) are genuinely strictly positive on their original domains, by SI29 and the 890 exact rational SM10 block SPD proof. Eliminating \(D^{-1}\) gives \(B_{14}-\eta I-UDU^*\), while eliminating \(B_{14}-\eta I\) gives the **entire 890-source coupled** \(S_{890}^{(14)}\). Bounded block congruences preserve negative inertia, including the infinite-dimensional positive first block, so
\[
\boxed{
\operatorname{ind}_{-}\!\left(
D^{-1}-U^*(B_{14}-\eta I)^{-1}U
\right)\ge3.
}
\]
**This is a genuine spectral classification of the entire fourteen-feature reference-conditioned 890-source surrogate**, without allocating the 890×890 Gram and without discarding a single original negative-cap covariance block or the \(\eta\) infinite residual. It does **not** transfer to \(S_{890}^{\rm true}\): since \(A_*\succeq B_{14}\), inverse order gives \(S_{890}^{\rm true}\succeq S_{890}^{(14)}\), so an indefinite **lower** surrogate cannot determine the sign of the true operator.

The simple rank argument requires no approximation of \(\lambda_{\min}(S_{890}^{(14)})\) in its 890 source-coordinate Euclidean norm: only its negative **index** is established. The \(-59/5000\) Rayleigh margin is on the original **physical operator**, not a numerical 890-matrix eigenvalue lower.

## 4. Architecture consequence under PS36 typed positivity

The SI29 \(C_{14}\)/\(B_{14}\) reference remains a sound **component** for original local inverse upper bounds (SM22–SM25). It is now an explicit **NO-GO** as a *sole complete-odd positivity preconditioner* for the exact full SM10 890-source cap: at least three negative surrogate Schur directions survive, even with exact arithmetic, perfect all-entry assembly, full off-diagonal retention, and the original \(\eta\) residual paid.

**SM27 acceptance-directed pivot:** increase the genuine original signed-positive reference's effective rank to at least seventeen independent directions in the relevant packet spectrum **or** incorporate original continuum positive multiplier coercivity not contained in \(B_{14}\), and prove its **complete** source/odd-pole Schur coupling. SM12's positive 33-source reference is *not automatically sufficient* (SM13 shows its standalone C33 fails on another original negative witness), so merely increasing feature count is not an acceptance certificate. Another viable route is to prove a direct full original \(A_*\)-inverse/complete odd Feshbach spectral upper without finite lower-reference closure, with original infinite residual. The actual \(S_{890}^{\rm true}\), PS36 O1/O2, even E1–E4, signed whole Weil, native CC27 D-Riesz, and RH remain **OPEN**.

**Repository custody:** \`research/obligations.json\` adds SM26 as a **method-obstruction** evidence with canonical W-ODD-NEG unchanged; no claim that the true original complete odd Weil form has three negative modes. \`scripts/validate_rpb108_sm26_full_cap_14_source_index_obstruction.py\` replays SM11's original 17-band source arithmetic, SM10 covariance rank/error, SI29's exact pole-conditioning/floor, the exact dimension/margin, a full finite-block rank-one/coupled Schur inertia countermodel, and fail-closed original odd sign. Mathematical audit independent of arithmetic/CI still required.

Replay: \`python3 scripts/validate_rpb108_sm26_full_cap_14_source_index_obstruction.py\`.
