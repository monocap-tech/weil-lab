# SM14 — full original positive continuum responds to the SM13 odd witness

**Active obligation:** W-ODD-NEG remains OPEN.
**Parents:** SM10 full negative cap; SM11 rank-16 reference exclusion; SM12 genuine 33-feature positive reference; SM13 actual physical witness g_14.42 where C33 fails.

## Exact proposed result

SM13's witness is the true supported odd Jensen mean
\(g(x)=\sin(2\pi (721/50)x)\operatorname{sinc}(2\pi x/100)\)
on \([-11/10,11/10]\). The C33 response to this packet is less than 0.00381, although the full positive operator \(A_o\) contains the entire original sign-positive continuum.

SM14 selects **thirteen new disjoint real-frequency intervals** of radius \(3/200\), centered at
14.06, 14.10, 14.14, 14.18, 14.22, 14.26,
14.56, 14.60, 14.64, 14.68, 14.72, 14.76, 14.80.
They are separated from the SM13 negative packet and all 33 previously selected positive frequency windows, so no signed frequency contribution is counted twice.

For each center \(d\), certify on **every real frequency** in the entire rational interval \([d-r,d+r]\) that the inherited **original** seven-prime signed multiplier satisfies
\[
m(\xi)>\kappa+\delta_d,\quad \kappa=1/1000,
\]
with independently checked rational margins
\(\delta=(4,4,4,3,2,1,1,2,3,3,3,3,2)\).
The eight rational subcell bounds use the original signed archimedean lower endpoint and the full seven-prime phase enclosure plus the 69-Lipschitz derivative uncertainty.

Let \(p_d(x)=\sin(2\pi dx)\operatorname{sinc}(2\pi rx)\) be the **true** physical positive Jensen mean. The original Fourier representation gives a genuine Loewner **lower**, never an upper, contribution
\[
A_o\succeq \kappa I+\sum_d 4r\delta_d\,|p_d\rangle\langle p_d|.
\]
The exact supported physical sine Gram \(G_{c,d}\) and sinc perturbations \(e(r)=(2\pi_{\rm hi}rB)^2/6\) imply
\[
|\langle g,p_d\rangle|\ge
\big(|G_{c,d}|_{\rm lower}-2B(e(1/100)+e(r))\big)_+.
\]
Consequently, using **only rational certified lower inequalities**,
\[
\langle g,A_o g\rangle
\ge\kappa\|g\|_{\rm lower}^2+
\sum_d4r\delta_d|\langle g,p_d\rangle|_{\rm lower}^2.
\]
SM14 tests a positive original continuum response strictly above \(1/2\) on the **same actual supported odd witness** where C33 gave an upper response below 0.00381.

### Mathematical scope and limitations

This is a **positive quadratic response of A_o on one physical direction**, not a dominance certificate over the negative-frequency operator. The true original \(K_{\mathrm{neg},o}\) quadratic was only **lower** bounded at that direction in SM13. SM14 **does not provide an upper bound for Kneg** on that direction, cannot establish even a signed positive Rayleigh witness (let alone universal odd positivity), and does not include the negative odd pole.

Even if its strict \(>1/2\) target passes, **W-ODD-NEG and RH remain OPEN**. The next logical step is to certify the complete original negative signed multiplier integral **upper** on this same physical witness, then extend to a coupled finite positive-versus-negative inverse over all SM10 Taylor sources and the odd pole. Existing native RC high-Schur needs explicit original physical carrier transport.

**Reproduction:** \`python scripts/validate_rpb108_sm14_continuum.py\`.
**Standing:** scoped mathematical proposal until focused exact-original GitHub Actions and final-head replays pass; original Weil identification requires independent expert audit.

## Certified source-head replay

Focused [Actions run 39016451490](https://github.com/monocap-tech/weil-lab/actions/runs/39016451490) **PASSED** using exact rational accepting comparisons.

On the actual odd physical \(g_{721/50}\), with all selected bands disjoint from C33:
\[
\sum_{j=1}^{13}4r\delta_j|\langle g,p_j\rangle|^2
>0.6666741285676513,
\qquad
\langle g,A_o g\rangle>0.6677778141467603.
\]

The smallest certified original signed multiplier lower over the complete thirteen intervals was \(m(\xi)>1.1094660777955563\), and each interval exceeded its own prescribed \(\kappa+\delta_j\). The C33 response upper on the **same** physical test was \(0.003806383032591049\). These figures display rational bound endpoints and are *not floating-point proof decisions*.

This recovers positive original continuum mass omitted by the specific C33 lower reference. The result supplies **no upper on the entire original \(K_{\mathrm{neg},o}\)** and cannot infer that the actual signed form is positive on \(g\). A fully coupled original positive-vs-negative Schur and odd pole absorption remain outstanding.
