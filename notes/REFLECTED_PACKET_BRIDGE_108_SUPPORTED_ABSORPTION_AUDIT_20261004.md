# RPB108: supported logarithmic absorption audit

Base: research `80986170797e25016471950c1634f748242ce671`.

## Definitions

Use the cycle-frequency Fourier convention \(\widehat f(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx\). Write \(w(\xi)=\log(e+|\xi|)\), \(m(f)=\|f\|_2^2\), and \(L(f)=\int w(\xi)|\widehat f(\xi)|^2\,d\xi\). The canonical domain consists of L2 functions supported almost everywhere in \([-a,a]\) with finite L. Let \(K_a=E_a+P_a\) be the existing native Gårding mass-error coefficient; \(P_a\ge0\).

A whole-canonical-domain absorption coefficient is a real \(\theta\) satisfying \(m(f)\le\theta L(f)\) for every f in that domain. The direct absorption budget is \(K_a\theta\le1\). This coefficient is different from a coefficient restricted to the certified Green range.

## A concrete support-sensitive estimate (analytic proof)

For \(a>0\), \(0<R\le1/(4a)\), and every canonical-domain f,
\[
L(f)\ge \left[1+(1-4aR)\bigl(\log(e+R)-1\bigr)\right]m(f).
\]

Proof. Compact support and Cauchy–Schwarz give \(\|f\|_1\le\sqrt{2a}\|f\|_2\). Hence the ordinary Fourier integral is defined and satisfies \(|\widehat f(\xi)|^2\le2a\,m(f)\) everywhere. This representative agrees almost everywhere with the L2 Fourier transform. The mass in \([-R,R]\) is therefore at most \(4aR\,m(f)\). Plancherel gives total Fourier mass m(f). On the complement, \(w(\xi)-1\ge\log(e+R)-1\ge0\), and everywhere \(w-1\ge0\). Thus
\[
L(f)-m(f)\ge(\log(e+R)-1)\int_{|\xi|>R}|\widehat f(\xi)|^2\,d\xi
\ge(\log(e+R)-1)(1-4aR)m(f).
\]
All integrals converge by the canonical domain hypothesis. The zero vector is included.

Taking \(R=1/(8a)\) gives the explicit improvement
\[
m(f)\le\theta_a L(f),\qquad
\theta_a=\left[1+\tfrac12\log\!\left(1+\frac1{8ae}\right)\right]^{-1}<1.
\]
This proves a support improvement; it does not certify the required budget for the actual K.

## Explicit whole-domain obstruction (analytic proof)

For every \(a>0\), define the lawful test
\[
f_a(x)=
\begin{cases}
\cos(\pi x/(2a)),&|x|\le a,\\
0,&|x|>a.
\end{cases}
\]
Its endpoint values vanish. The extension lies in H1: its weak first derivative is the piecewise ordinary derivative, with no endpoint delta because the function is continuous there. Direct integration gives
\[
m(f_a)=a,\qquad
\|f_a'\|_2^2=\frac{\pi^2}{4a}.
\]
The Fourier derivative identity and Plancherel yield
\[
\int\xi^2|\widehat f_a(\xi)|^2\,d\xi=\frac1{16a}.
\]
Since \(\log(e+t)=1+\log(1+t/e)\le1+t/e\) for \(t\ge0\), Cauchy–Schwarz gives
\[
0<L(f_a)\le a+\frac1e
\left(\int|\widehat f_a|^2\right)^{1/2}
\left(\int\xi^2|\widehat f_a|^2\right)^{1/2}
=a+\frac1{4e}.
\]
In particular f_a is nonzero and belongs to the canonical logarithmic domain, without assuming spectral operator-domain membership.

Every whole-domain absorption coefficient must consequently satisfy
\[
\theta\ge\frac{m(f_a)}{L(f_a)}
\ge\frac1{1+1/(4ae)}.
\]
The first inequality also implies \(\theta>0\).

The actual zero-frequency special value now proves in Lean
\[
M_a(0)<-2,\quad E_a>3,\quad K_a>3.
\]
Indeed, the nonnegative prime sum can be discarded; Euler's constant exceeds 1/2, pi exceeds 3, and both logarithms are positive. Every uniform absolute envelope C then satisfies \(C\ge w(0)-M_a(0)>3\).

It follows that for every \(a\ge1/(8e)\), every whole-domain absorption coefficient obeys
\[
K_a\theta>1.
\]
Proof: \(1+1/(4ae)\le3\), so \(\theta\ge1/3\), and \(K_a>3\). Therefore **no whole-canonical-domain mass-to-log comparison can meet the direct absorption budget on these windows**, even if its constant is optimized. This concerns the existing absolute-error route, not the sign of the native or background quadratic.

## Carrier custody and exact remaining input

The cosine is a legitimate canonical-domain test. It is NOT proved to lie in the certified Green graph range or its graph completion, and it is NOT a retained source/null witness. No full graph density is assumed. The whole-domain impossibility therefore does not rule out a stronger mass comparison restricted to the actual Green range, support-sensitive signed cancellation, or a direct background-form estimate including the nonnegative selected term.

The low-band estimate is valid for all canonical-domain physical vectors, hence applies to actual Green physical coordinates by their existing membership theorem. It improves mass control but supplies no checked actual K budget. To close WD-T10 one still needs the unshifted same-vector background domination estimate, equivalently the certified finite-packet PSD condition, or a lawful negative packet to refute it.

## Formalization and validation boundary

The four new scalar/constant inequalities are Lean-certified in the existing ActualZetaNativeSymbolSign module. The support-sensitive low-band estimate and the supported cosine obstruction above are fully stated analytic proofs; they have not been formalized in Lean. No CI result is claimed for those analytic arguments.

Lean 4.34.0; exact tested scalar-code head `fce762b78844245516a0fa1d2da60cb24dbe7e0b`. [Actions run 37234901763](https://github.com/monocap-tech/weil-lab/actions/runs/37234901763) / job `111531957486` passed isolated 9176/full 9203 build jobs. Four scalar/constant theorem audits use exactly `[propext, Classical.choice, Quot.sound]`; unfinished/project-axiom and sorryAx gates passed. Tested source fetched and matched byte-for-byte. Restored native-envelope cache and saved `rpb108-actual-supported-absorption-verified-v1`. The support-band and cosine arguments above are not Lean-certified.

## Updated cursor/residue

At 8098617, the actual scalar deficit is strengthened to M_a(0) < -2 and every uniform absolute logarithmic envelope constant exceeds 3; canonical E_a and Gårding K_a exceed 3. An analytic support-band proof gives explicit improved mass control theta_a < 1 on the canonical domain. An explicit supported cosine H1 test proves that every whole-domain mass-to-log coefficient theta is at least 1/(1+1/(4ae)); hence for a >= 1/(8e), K_a theta > 1. The existing absolute-error absorption route cannot close on the entire canonical domain on those windows, even with optimal theta. The cosine has no proved Green graph membership and no retained source/null custody, so this does not obstruct a Green-range-specific estimate or decide background sign. Support-band and cosine arguments are analytic proofs, not Lean-certified; only four new scalar/constant inequalities are formalized. Next independent input: an actual Green-range support-sensitive integrated background estimate retaining pole and selected terms, or a certified finite negative packet. No full graph density, zero simplicity, spectral operator-domain membership or background positivity is assumed. FULL TRANSPORT CLOSED remains open; SOURCE stays off the critical path.
