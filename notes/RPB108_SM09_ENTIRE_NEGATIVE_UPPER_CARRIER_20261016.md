# SM09 — global original odd negative-frequency upper carrier (candidate)

**Canonical obligation:** `W-ODD-NEG` — OPEN.  
**Parent:** SM07 merged; SM08 five-source selected-variable-subband proposal is a *separate* draft, first coarse interval replay failed, stronger moment replay pending.  
**Standing:** candidate rigorous abstract Loewner upper decomposition, with exact rational global support, mass, Taylor-rank and residual verification. This does not establish the finite positive-vs-negative Schur gate.

## 1. Correct original signed **upper** spectral object

Let the original physical odd Hilbert space be
\[
H_o=L^2([-B,B])_{\rm odd},\ B=11/10,\quad \kappa=1/1000.
\]
Use the original seven-prime archimedean multiplier \(m(\xi)\) of SI06/SI10. With the reference scalar \(\kappa\), write
\[
m=\kappa+(m-\kappa)_+-(\kappa-m)_+,\qquad r=(\kappa-m)_+.
\]
The **entire original negative-frequency operator** on physical odd support is
\[
K_{\rm neg,o}=2\int_0^\infty r(\xi)|h_\xi\rangle\langle h_\xi|d\xi,
\quad h_\xi(x)=\sin(2\pi\xi x).
\]
The odd pole \(2|s\rangle\langle s|\) is a separate original negative rank-one term.

Reconstruct SI10's rigorous full-frequency *protected-positive* cover \(U\) as 973 unresolved dyadic leaves on positive frequencies, clustered into 107 intervals and reflected to negative frequencies. Outside \(U\cup(-U)\), the original multiplier satisfies \(m>\kappa\) on every real frequency, including the certified outer 896–1200 interval and the analytic tail beyond 1200.

On every unresolved leaf \(I=[l,r]\subset[0,896]\), SI10's outward rational lower bound \(m(\xi)\ge L_I\) and height \(h_I\ge(-L_I)_+\) give
\[
r(\xi)=(\kappa-m(\xi))_+\le\kappa+h_I.
\]
Define the global certified nonnegative **upper envelope** on positive frequencies
\[
w(\xi)=\sum_{I\in U_+}(\kappa+h_I)\mathbf 1_I(\xi).
\]
Then \(0\le r\le w\) pointwise on the entire nonnegative real axis, so the true full negative operator obeys
\[
\boxed{0\preceq K_{\rm neg,o}\preceq K_{\rm cap,o}:=
2\int_0^\infty w(\xi)|h_\xi\rangle\langle h_\xi|d\xi}.
\]
**This inequality has the correct direction for eventual W-ODD-NEG closure.** It covers every signed-negative band, not a selected negative *lower* subpacket.

If \(M\) and \(W\) denote SI10's exact outward caps for full reflected negative mass \(2\sum_I h_I|I|\) and full reflected cover width \(2\sum_I|I|\), the whole upper-envelope integral is exactly
\[
2\sum_I(\kappa+h_I)|I|=M+\kappa W.
\]
The accepted SI10 source values are \(M\le37.59565259375\) and \(W=30.40625\). The added \(\kappa W\) is **mandatory**: using only SI07's \(m_-\) would omit frequencies where \(0<m<\kappa\).

## 2. Physical odd finite-rank Taylor carrier

For each of the 107 positive-frequency connected clusters \(I_j=[a_j,b_j]\), let \(c_j=(a_j+b_j)/2\). Use SI08's exact rational Taylor order \(p_j(b)\) for which
\[
\frac{[(22/7)B(b_j-a_j)]^{p_j}}{p_j!}<2^{-b}.
\]
Let \(E_b\subset H_o\) be the span of the *physical odd* functions
\[
\partial_\xi^k\sin(2\pi\xi x)\big|_{\xi=c_j},
\qquad j=1,\ldots,107,\quad 0\le k<p_j(b),
\]
and \(P_b\) the **orthogonal projection** onto this span. Parity permits one real odd column per degree, rather than two mirrored complex exponentials. No infinite-line operator inverse and no fabricated bandlimited physical input is involved.

The Taylor polynomial belongs to \(E_b\), and \(\|h_\xi-\operatorname{Taylor}_{p_j-1}h_\xi\|_2\le\sqrt{2B}2^{-b}\) for each \(\xi\) in its cluster. Therefore
\[
\boxed{
\|R_{\rm cap}(I-P_b)\|^2
\le e_b^2:=2B(M+\kappa W)2^{-2b},
}
\]
where \(R_{\rm cap}^*R_{\rm cap}=K_{\rm cap,o}\).

## 3. Correct-sign full-continuum low/high coupling

For any \(\tau>0\), decompose
\(R_{\rm cap}f=R_{\rm cap}P_bf+R_{\rm cap}(I-P_b)f\)
and apply
\[
\|a+b\|^2\le(1+\tau)\|a\|^2+(1+\tau^{-1})\|b\|^2.
\]
Then **in physical odd Loewner order**,
\[
\boxed{
K_{\rm neg,o}\preceq K_{\rm cap,o}
\preceq (1+\tau)P_bK_{\rm cap,o}P_b
+(1+\tau^{-1})e_b^2(I-P_b).
}
\]
This bound pays **all omitted low/high cross terms** by an explicit Young penalty; it does not assert that the off-diagonal block vanishes. The finite compression \(P_bK_{\rm cap,o}P_b\) is PSD and well-defined as the exact *continuous, rational upper-weight* integral, though its finite matrix is not yet numerically certified against \(A_o\).

For the designated \(b=24\), \(\tau=1/1024\), the validator requires a rigorous rational global residual
\[
(1+\tau^{-1})e_{24}^2<10^{-9}.
\]
This is **the entire frequency-negative infinite complement**, not just the SM06 tail of one interval.

## 4. Exact remaining obligation, no false promotion

A sufficient next full-odd condition is the physical supported Loewner inequality
\[
\boxed{
A_o-2|s\rangle\langle s|
\succeq
(1+\tau)P_b K_{\rm cap,o}P_b
+(1+\tau^{-1})e_b^2(I-P_b).
}
\]
That compares the true positive original frequency operator (and original negative pole) against the **entire** certified upper bound. It is **not yet proved**. Its coupling is the next weighted supported finite inverse/Schur challenge; the positive operator must be treated on the exact original physical carrier. The high-part bound is easy at b=24, but the coupled finite block may be very large and may need native RC compression or a sharper envelope.

A successful SM09 validation would prove only the full-negative *upper carrier reduction* and its tiny global infinite tail, **not W-ODD-NEG, Stage I, whole Weil positivity, or RH**.

Replay: `python scripts/validate_rpb108_sm09_entire_negative_upper_carrier.py`. The validator inherits SI10's exact-rational whole-frequency cover, preserves original seven-prime sign data, and checks the residual and rank. Mathematical analytic implications and exact original-zeta identifications remain independently auditable questions.
