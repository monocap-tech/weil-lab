# SM19 — original SI29 fourteen-feature residual preconditioner for the complete odd Schur gate

**Active obligation:** W-ODD-NEG OPEN. **Parents:** SI29's supported original 14-feature pole certificate, SM10's full 890-column negative cap, SM17's top-eigenvalue criterion and SM18's exact forward residual identity. **Standing:** analytic, original-operator-attached **conditional** finite-data reduction plus exact Fraction matrix-sign regression. The 890-column original residual and inverse threshold have not been computed.

## 1. Replace the weak scalar error amplifier with an actual supported positive reference

Let \(H_o=L^2([-11/10,11/10])_{\rm odd}\) with the original seven-prime supported positive operator \(A_o\) and odd pole \(s(x)=\sinh(x/2)\). Set \(A_*=A_o-2|s\rangle\langle s|\). SI29 supplies the **actual original physically supported 14-column Jensen/Bessel positive reference**
\[
 C_{14}=\kappa I+G\Gamma G^*\preceq A_o,\qquad \kappa=1/1000,
\]
where the columns of \(G:\mathbb R^{14}\to H_o\) are the exact continuous-band physical source functions, \(\Gamma=\operatorname{diag}(\gamma_j)\succ0\) contains their original sign-positive weights, and the source/odd-pole physical Gram was rigorously enclosed (approximating these means by finite Simpson quadrature does not change the exact definition). SI29's rational inverse evaluation certifies
\[
2\langle s,C_{14}^{-1}s\rangle\le L=966379/10^6<1.
\]
Consequently the **original attached** minorant
\[
\boxed{B_{14}=C_{14}-2|s\rangle\langle s|\preceq A_*}
\]
is strictly coercive:
\[
B_{14}\succeq (1-L)C_{14}\succeq \kappa_*I,\quad
\kappa_*=\frac{33621}{10^9}.
\]
There is no assumption that \(B_{14}\) alone dominates the full original signed-negative frequency operator; SM03/SM13 show why sparse standalone domination is the wrong criterion.

Because inversion reverses Loewner order,
\[
\boxed{0<A_*^{-1}\preceq B_{14}^{-1}\preceq\kappa_*^{-1}I.}
\]
Thus **every** SM18 residual vector obtains an operator-level improvement (non-strict in directions invisible to the reference), never a worsening, by replacing the global scalar multiplier \(10^9/33621\) with \(B_{14}^{-1}\).

## 2. Exact low-rank Woodbury identity with the correct pole sign

Define exact physically supported Gram objects:
\[
S=G^*G\in\mathbb R^{14\times14},\quad
q=G^*s\in\mathbb R^{14},\quad
s_2=\langle s,s\rangle,\quad
K=\Gamma^{-1}+\kappa^{-1}S\succ0.
\]
Then
\[
C_{14}^{-1}=\kappa^{-1}I-\kappa^{-2}GK^{-1}G^*.
\]
Set
\[
\alpha=1-2(\kappa^{-1}s_2-\kappa^{-2}q^*K^{-1}q)>0.
\]
**Note that \(\alpha\) is the exact SI29 pole Schur denominator and the pole update is positive.**
\[
\boxed{B_{14}^{-1}=C_{14}^{-1}
+\frac2\alpha\,|C_{14}^{-1}s\rangle\langle C_{14}^{-1}s|.}
\]

For **any** original supported residual synthesis \(E:\mathbb R^{890}\to H_o\) from SM18, define
\[
D=E^*E\in\mathbb R^{890\times890},\qquad
F=G^*E\in\mathbb R^{14\times890},\qquad
t=E^*s\in\mathbb R^{890},\quad
z=\kappa^{-1}t-\kappa^{-2}F^*K^{-1}q.
\]
Then *every* mixed cross term is retained in the finite-data identity
\[
\boxed{E^*B_{14}^{-1}E=
\kappa^{-1}D-\kappa^{-2}F^*K^{-1}F
+\frac2\alpha zz^*.}
\]
The **negative** positive-feature Woodbury correction and the **positive** odd-pole correction cannot be discarded, sign-flipped or diagonally approximated.

## 3. Full original SM18 sufficient test, without an infinite operator inverse

Let \(U\) be SM10's original supported 890-source synthesis, \(C\succ0\) its actual rational 107-block moment matrix, and \(Y\) a proposed supported forward trial synthesis contained in \(\mathrm{Dom}(A_*)\). Set
\[
E=U-A_*Y,\qquad H_Y=U^*Y+Y^*U-Y^*A_*Y.
\]
SM18 gives
\[
U^*A_*^{-1}U=H_Y+E^*A_*^{-1}E
\preceq H_Y+E^*B_{14}^{-1}E.
\]
Therefore a verified **complete** original physical 890-column matrix inequality
\[
\boxed{
\frac{999}{1000}C^{-1}-H_Y
-\kappa^{-1}D+\kappa^{-2}F^*K^{-1}F
-\frac2\alpha zz^*\succeq0
}
\]
would, by SM10/SM17, establish W-ODD-NEG for the original supported odd form, with all 973 leaves and infinite error paid. This is **conditional**, and does not claim the full matrix inequality.

A practical implementation must enclose the true continuous SI29 source functions (not a naked Simpson proxy), all 890 actual \(E\)-columns, physical Grams \(D,F,t\), the source Gram \(S,q,s_2\), the entire finite-frequency original seven-prime multiplier, odd-pole coupling, and the original high-frequency \(a^2|\widehat{ZY}|^2\) tail for forward residuals. Rigorously formed *PSD* matrix enclosures are required: pointwise entrywise intervals alone do not imply an upper bound in Loewner order. Use exact Fraction matrix witnesses plus explicit norm/Gershgorin uncertainty inflation before any final PSD acceptance.

## 4. Scope and computational leverage

SI29's fourteen features provide a **real original-operator-attached preconditioner**. The calculation now requires the 890x890 residual Gram \(D\), a 14x890 source-to-residual Gram \(F\), one 890-vector pole overlap \(t\), and the fixed 14x14 supported Woodbury inverse, rather than relying on a single excessively small uniform coercivity floor. Unlike a C14-only negative-domination attempt, the **forward-action approximation \(Y\)** carries the missing positive response. The preconditioner is therefore not disqualified by the historical C14/C33 reference no-go, although the numerical residual gate could still be inconclusive.

The accompanying Python exact-rational two-dimensional prototype checks the correct pole sign, equality of the direct reference inverse and the finite-data Woodbury formula, full mixed-term Loewner order, and a **strict improvement** versus the scalar SM18 error coefficient. It is not a 890-column original test and does not prove full odd positivity.

**Next:** construct even the *first* actual nonzero original supported forward residual column with complete signed original source/frequency/tail enclosure, and transport \(D,F,t\) to certified 890-column blocks. Prefer an original attached trial Ritz basis rather than a sequence of abstract conditional identities. W-ODD-NEG, even/whole Weil, global RH bridge and RH remain OPEN.
