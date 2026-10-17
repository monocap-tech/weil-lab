# SM08 candidate — original variable signed-negative subband, coupled supported inverse

**Canonical mathematical obligation:** `W-ODD-NEG`, **OPEN**.  
**Parent:** merged SM07 (PR #135, research HEAD `8e39fd4f12d6f3c504d9d4f23ff95948b5608782`).  
**Standing:** candidate exact-rational five-source supported inverse. No theorem asserted until focused final-head Actions PASS. No entire negative-frequency, even-form, global bridge, or RH claim.

## 1. What new original frequency mass must be paid?

On the true physical odd Hilbert space \(H_o=L^2([-11/10,11/10])_{\rm odd}\), let \(A_o\) be the *original supported positive-frequency* operator of SM05/06 and \(\kappa=10^{-3}\). The SM06 signed negative original multiplier gave \(r(\xi)=(\kappa-m(\xi))_+\ge7/5\) on
\[
J=[729/200,741/200]=[3.645,3.705].
\]
The exact SM07 whole-interval seven-prime sign source gives \(m(\xi)<-2\) on
\[
J_1=[729/200,731/200]=[3.645,3.655]\subset J.
\]
Consequently, \(r(\xi)>7/5+3/5\) on \(J_1\). The original negative-frequency form is therefore at least
\[
T_{J,7/5}+T_{J_1,3/5},\qquad
T_{J,\delta}=2\delta\int_J|\sin(2\pi\xi\cdot)\rangle\langle\sin(2\pi\xi\cdot)|\,d\xi.
\]
These operators are *nested*, not disjoint: the extra \(3/5\) measures true variable spectral excess. They can be added because the original continuous spectral multiplier is additive and the negative part is a positive operator.

**Important direction:** the displayed sum is a *lower* suboperator of the whole original negative-frequency operator. Certifying its absorption is concrete progress, not an upper domination of the whole remaining negative spectrum.

## 2. Exact five-source reduction

For \(I=[c-r,c+r]\), put \(g_{I,0}=E_{[-1,1]}\,h_{c+ru}\) and \(g_{I,1}=3E_{[-1,1]}u\,h_{c+ru}\) where \(h_\xi(x)=\sin(2\pi\xi x)\).
On the actual odd physical support, the exact orthogonal Legendre decomposition is
\[
T_{I,\delta}=
4r\delta|g_{I,0}\rangle\langle g_{I,0}|
+\frac{4r\delta}{3}|g_{I,1}\rangle\langle g_{I,1}|
+R_{I,\ge2},\quad R_{I,\ge2}\succeq0.
\]
Choose
\[
V=(s,g_{J,0},g_{J,1},g_{J_1,0},g_{J_1,1}),\quad
W=\operatorname{diag}(2,21/125,7/125,3/250,1/250).
\]
The five-column covariance requires *all broad/narrow and pole cross terms*, including nearly redundant means. The earlier three-source Gershgorin row test is not reliable for this highly overlapping block.

The *same previously validated* original positive-frequency sixteen-feature reference is retained:
\[
A_o\succeq C_{16}=\kappa I+G\Gamma G^*.
\]
With \(H=G^*G, Q=G^*V, P=V^*V, M=\Gamma^{-1}+H/\kappa\), any rational dual trial \(Z\) gives the correct-sign **matrix Loewner upper bound**
\[
V^*A_o^{-1}V\preceq
U(Z)=\kappa^{-1}P-\kappa^{-2}(Q^*Z+Z^*Q-Z^*MZ).
\]
All objects are computed with *physical* original signed continuous-frequency Jensen means, original positive intervals, interval-enclosed signed Simpson error, and rational dual witnesses. Entrywise enclosures describe the entries of this explicit \(U(Z)\), **not** necessarily the entries of \(V^*A_o^{-1}V\).

The finite acceptance condition is equivalently **rational**:
\[
\boxed{\operatorname{diag}(\theta/W_i)-U(Z)\succ0},
\qquad \theta=993/1000.
\]
It is exactly the congruence of \(W^{1/2}U(Z)W^{1/2}\prec\theta I\), with no square-root rounding. The verifier computes rational midpoint intervals, bounds their full symmetric perturbation by the largest absolute radius row sum, and applies a **fraction-only LDL positive-pivot test** to the shifted rational matrix. Thus this test keeps cross-covariance rather than replacing it by an overly conservative absolute row sum of source overlaps.

## 3. Both *infinite* residuals paid without finite-mode truncation

For either interval, Taylor/Parseval proves the complete remainder
\[
0\preceq R_{I,\ge2}\preceq
\varepsilon_{I,\ge2}I,\quad
\varepsilon_{I,\ge2}=
\frac{\delta r^5(2\pi_{\rm hi})^4,2B^5}{25}.
\]
The certificate must pay \(\varepsilon_{J,\ge2}+\varepsilon_{J_1,\ge2}\) from \((1-\theta)\kappa\), rather than pretending the higher modes vanish.

**Scoped conditional result:** if the exact five-source rational LDL test passes, and if the two explicit tail inequalities pass, then
\[
\boxed{A_o-2|s\rangle\langle s|-T_{J,7/5}-T_{J_1,3/5}
\succeq\left[(1-\theta)\kappa-
\varepsilon_{J,\ge2}-\varepsilon_{J_1,\ge2}\right]I\succ0.}
\]
This would absorb the first rigorously selected piece of the **actual variable** signed negative multiplier, not merely the uniform SM06 component.

## 4. Custody and remaining obligation

Even a PASS does **not** upper-bound the original multiplier's remaining excess on \(J_1\) or \(J\), other negative-frequency intervals, or their infinite tails. For full W-ODD-NEG, certify an *upper* original negative-multiplier partition, then a coupled full supported inverse or an equivalent correctly transported native high-Schur gate. The proper sign direction is essential: inequalities \(m<\text{negative threshold}\) only establish **lower** negative mass.

Replay: `python scripts/validate_rpb108_sm08_coupled_excess.py`. Candidate results cannot be promoted until successful source and final-head GitHub Actions checks, manifest reconciliation, and independent mathematical scrutiny of inherited operator identifications.
