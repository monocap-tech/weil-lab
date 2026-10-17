# SM07 — actual original signed-multiplier excess: why SM06's scalar floor is insufficient

**Active obligation:** W-ODD-NEG, remains OPEN.  
**Parent:** SM06 merged PR #134 (head \`fb1eeb350c6ecc8acf277733d65ce046f4d32289\`).  
**Standing:** focused exact-rational signed original whole-subinterval and physical odd Jensen certificate PASSED (GitHub Actions run `39006091643`, source `d07e75336a9a`). Final-head integration and independent peer review remain distinct. No original Weil negativity or RH counterexample is asserted.

## 1. Which continuum remains after SM06?

SM06 has certified on the original physically supported odd Hilbert space
\[
A_{\rm rem}:=A_o-2|s\rangle\langle s|-T_{J,7/5}
\succeq 5.6440\cdot10^{-5}I,\quad
J=[3.645,3.705],\quad
T_{J,\delta}=2\delta\int_J|h_\xi\rangle\langle h_\xi|d\xi,
\quad h_\xi(x)=\sin(2\pi\xi x).
\]
But the true seven-prime negative-frequency spectral multiplier is \(r(\xi)=(\kappa-m(\xi))_+\), \(\kappa=1/1000\). The exact remaining operator
\[
E:=K_{{\rm freq},o}-T_{J,7/5}\succeq0
\]
includes *both* the excess \(r(\xi)-7/5\) on \(J\) and all negative frequencies outside \(J\). SM06 did not bound \(E\).

## 2. A new, genuinely variable-signed source lower bound

Take a rational **subwindow**
\[
J_1=[729/200,731/200]=[3.645,3.655]\subset J.
\]
A dedicated 16-cell exact rational replay of the original **complete seven-prime signed multiplier** uses SM03's decreasing positive digamma Euler-series tail upper, SI06's exact trigonometric prime intervals, and the globally paid derivative bound \(69\) on *every rational subcell*. It checks
\[
\boxed{m(\xi)<-2\quad\forall\xi\in J_1.}
\]
Consequently, \(r(\xi)-7/5>3/5\) throughout \(J_1\).

The actual continuous-frequency odd Jensen source
\[
g_1(x)=\frac1{2\rho}\int_{c-\rho}^{c+\rho}\sin(2\pi\xi x)d\xi
=\sin(2\pi c x)\operatorname{sinc}(2\pi\rho x),\quad
c=73/20,\quad \rho=1/200
\]
gives the physically supported PSD minorant
\[
\boxed{E\succeq4\rho\,(3/5)|g_1\rangle\langle g_1|
=\frac3{250}|g_1\rangle\langle g_1|.}
\]
Here no point-frequency atom is substituted for a continuous band. The whole *signed* subband has been verified and Jensen's Loewner inequality applies to the actual physical odd sine functions.

SI18's exact rational odd sine Gram and a uniform sinc-to-center error yield
\[
\|g_1\|_2^2\ge(1-e)^2\|\sin(2\pi c x)\|_2^2_{\rm lo}>1,
\quad
e=\frac{(2\pi_{\rm hi}\rho B)^2}{6}.
\]
Thus
\[
\boxed{\|E\|>\frac3{250}\cdot1=\frac3{250}=0.012.}
\]

## 3. Precise meaning of the obstruction

SM06's **reported** positive scalar floor is \(L=5.6440\cdot10^{-5}\). SM07's verified bound would give
\[
\|E\|>0.012>100L.
\]
Therefore **\(E\not\preceq LI\)**. It is logically impossible to absorb the true variable negative-frequency excess *by that reported scalar floor alone*, with no other information.

**What this does not prove:** the actual conditioned positive operator \(A_{\rm rem}\) can be much larger than \(LI\) in selected frequency directions. Consequently \(E\not\preceq LI\) does **not** imply \(E\not\preceq A_{\rm rem}\). This is **not** evidence for a negative original Weil vector or a contradiction of RH. It rigorously prevents another method misstep: simply shrinking the residual norm without exploiting the frequency-dependent operator geometry cannot finish the odd-sector gate.

## 4. Next obligation-directed work

Compute an actual **weighted supported inverse/covariance** response for \(E\), retaining its overlap with the already absorbed odd pole and constant-weight band. In particular, prioritize original multiplier-weighted Legendre means on a certified partition of \(J\), together with all other disjoint negative subbands and a full infinite residual. The existing 16-feature positive reference may need to be enriched to accommodate this genuinely nonuniform signed packet. No stage/status promotion beyond this precise obstruction.

Replay: \`python scripts/validate_rpb108_sm07_true_multiplier_excess_nogo.py\`. Exact rational replay, inherited original operator identification and independent peer review are distinct requirements.

## 5. Accepted source replay

GitHub Actions focused run `39006091643` returned exact rational assertions for:

- Whole original seven-prime signed upper on every point of (J_1): (m(\xi)<-2.1226920<-2).
- True original physically supported odd Jensen norm squared (\|g_1\|_2^2>1.0954784).
- Original remaining variable-frequency operator norm (\|E\|>0.0131457).
- The SM06 reported constant-coercivity floor is (5.644\times10^{-5}), so (\|E\|>230L).

The theorem is a *method-class obstruction to paying the remainder from the scalar floor*, not a negativity claim about the full conditioned positive operator. Final CI replay must pass for canonical integration.
