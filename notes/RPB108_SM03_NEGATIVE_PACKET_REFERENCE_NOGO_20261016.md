# RPB108 SM03 — genuine signed negative-frequency odd packet defeats the SI29 fourteen-feature reference

**Canonical obligation:** \`W-ODD-NEG\` (still OPEN).  
**Parent:** SM02 merged at \`3d5ab604ee13da24bb72f949be135291cb780af9\`.  
**Standing:** exact-rational *negative* feasibility verdict for **one specified lower-reference method**. This is neither negativity of the original Weil form nor failure of the complete positive operator \(A_o\).

## 1. Original signed object and a deliberately conservative candidate

On \(H_o=L^2([-11/10,11/10])_{\rm odd}\), SI11 and SM01 use the original seven-prime signed multiplier \(m\), \(\kappa=1/1000\), and
\[
a=\max(m,\kappa),\quad r=(\kappa-m)_+,\quad
Q_o=A_o-K_{{\rm freq},o}-2|s\rangle\langle s|.
\]
SI29's original physically supported 14-feature, true Jensen/Bessel reference is
\[
C_{14}=\kappa I+\sum_{j=1}^{14}\gamma_j|g_j\rangle\langle g_j|\preceq A_o,
\qquad C_{14,\star}=C_{14}-2|s\rangle\langle s|\preceq A_{\star,o}.
\]
It passed a **pole-only** inverse bound; its unknown ability to absorb the actual negative-frequency operator was specifically proposed for structural scrutiny in SM01.

A sufficient but not necessary route to \`W-ODD-NEG\` would be
\(C_{14,\star}\succeq K_{{\rm freq},o}\). SM03 tests precisely this route using a genuine signed negative Fourier interval.

## 2. Signed full-interval negative packet and an actual odd physical witness

Fix rational
\[
c_-=\frac{147}{40}=3.675,\quad \rho_-=\frac3{100}=0.03,\quad
J_-=[729/200,741/200]=[3.645,3.705],
\quad \delta_-=\frac75.
\]
The proof regression evaluates the **original** \(m(\xi)\) on every subcell of \(J_-\), not merely \(m(c_-)\): it uses (i) exact SI06 seven-prime cosine intervals and derivative bound \(<69\), (ii) a new rational *upper* digamma enclosure via its positive Euler series and integral remainder, and (iii) monotonicity of the archimedean part on \(\xi\ge0\). The signed result is
\[
\boxed{m(\xi)<-7/5\qquad(\xi\in J_-\cup(-J_-)).}
\]
The new archimedean upper bound is derived from
\[
\Re\psi(1/4+iy)-\log\pi
=-\gamma-\pi/2-3\log2-\log\pi
+\sum_{k\ge0}\frac{y^2}{(k+1/4)((k+1/4)^2+y^2)}
\]
with an explicit rigorous *upper* tail for \(k\ge N\),
\[
\sum_{k\ge N}f(k+1/4)
\le f(N+1/4)+\int_N^\infty f(t+1/4)dt,\quad
\int_N^\infty f(t+1/4)dt=\tfrac12\log(1+(y/(N+1/4))^2).
\]
The gamma constant lower bound and rational logarithm/π enclosures are imported from SI06.

Set the true physical odd Jensen vector
\[
g_-(x)=\frac1{2\rho_-}\int_{c_--\rho_-}^{c_-+\rho_-}
\sin(2\pi\xi x)\,d\xi
=\sin(2\pi c_-x)\operatorname{sinc}(2\pi\rho_-x).
\]
Since \(r(\xi)=\max(\kappa-m(\xi),0)>7/5\) on both bands, the **full original** negative-frequency operator satisfies the Loewner *minorant*
\[
\boxed{K_{{\rm freq},o}\succeq4\rho_-\delta_-|g_-\rangle\langle g_-|.}
\]
This is a physically supported continuous-frequency signed packet, not a toy band and not a single-frequency point mass.

## 3. Bounding the entire SI29 positive reference without a fitted inverse

Let \(h_\xi(x)=\sin(2\pi\xi x)\), \(N=\|h_{c_-}\|_2^2\) and \(e=(2\pi_{\rm hi}\rho_-B)^2/6\). Since the true sinc average obeys \(|g_--h_{c_-}|\le e\), 
\[
\|g_-\|_2^2\ge (1-e)^2N,\qquad \|g_-\|_2^2\le N.
\]
For every original SI29 positive frequency interval \(J_j=[c_j-\rho_j,c_j+\rho_j]\), define
\[
v_j=\sup_{\xi\in J_j}|\langle h_{c_-},h_\xi\rangle|+2Be.
\]
The validator rigorously encloses \(v_j\) by partitioning each positive window into 16 exact subcells, evaluating SI18's **supported sine Gram** at rational midpoints and paying the global Lipschitz derivative \(2\pi_{\rm hi}B^2\) on each half cell. For a degree-zero true Jensen mean \(|\langle g_-,g_j\rangle|\le v_j\); for a degree-one normalized Legendre moment \(|\langle g_-,g_j\rangle|\le(3/2)v_j\). These are whole-band upper bounds, **not** a Gaussian heuristic or midpoint-only evaluation.

Therefore
\[
\langle g_-, C_{14}g_-\rangle
\le \kappa N+\sum_{j=1}^{14}\gamma_j t_j^2v_j^2=:U,
\quad t_j=\begin{cases}1,&\deg j=0\\3/2,&\deg j=1,\end{cases}
\]
whereas
\[
\langle g_-,K_{{\rm freq},o}g_-\rangle
\ge4\rho_-\delta_-(1-e)^4 N^2=:L.
\]
The exact rational acceptance is \(0<U<L\), with deliberately weaker robust rational thresholds \(L>193/1000\), \(U<4/25\) and \(L-U>3/100\). The first 64-subcell version passed GitHub Actions run `38997855264` with stricter enclosures \(m_{J}^{\rm upper}<-1.4798698\), \(L>0.1935774\), \(U<0.1513254\) and \(L-U>0.0422520\); the current 16-subcell replay must independently establish the retained weaker rational thresholds. This deliberately discards the helpful *negative* pole term from the comparison and keeps all fourteen **positive** reference components, including the two original degree-one moments. No inverse, omitted cross Gram, or unknown \(A_o\) action is substituted.

## 4. Consequence: sparse-reference method-class no-go

Once the validator establishes \(L>U\), it proves
\[
\boxed{\langle g_-,(C_{14}-K_{{\rm freq},o})g_-\rangle<0.}
\]
Thus, a fortiori,
\[
C_{14,\star}-K_{{\rm freq},o}\not\succeq0,\qquad
R_o C_{14,\star}^{-1}R_o^*\not\preceq I
\]
(the last equivalence uses the strictly positive SI29 pole-absorbed reference).

**Crucial boundary:** \(A_o\succeq C_{14}\). Failure of the *lower* reference to dominate the negative continuum says **nothing** about whether the full **original** \(A_{\star,o}\) dominates it; the omitted positive-frequency contribution could rescue the inequality. This is not a negative Weil witness or a disproof of RH. It does, however, rigorously rule out spending more computation on the unchanged 14-feature reference as a sufficient complete certificate.

## 5. Next obligation-directed step

Stop treating \(C_{14,\star}^{-1}\) as a plausible final upper proxy for the entire frequency-negative BS operator. To advance \`W-ODD-NEG\`, either:

1. **Enrich the actual positive reference** with modes targeting the new packet \(g_-\) and certify an explicit simultaneous **pole plus negative-packet** inverse bound with the full signed residual; or
2. Use the original \(A_o\) supported response from native RC's smaller high-Schur decomposition, comparing true carriers and metrics rigorously.

Reproduction: \`python scripts/validate_rpb108_sm03_negative_packet_reference_nogo.py\`. This validator must pass on the final committed code before claiming the signed whole-interval and strict reference-defeat inequalities. No claimed full odd/even Weil positivity, Stage I, Lean RH bridge or RH result.
