# RPB108: prescribed arithmetic breaks both parity modulus orderings

Date: 2026-10-06. Source base: `56cb7ede95e8b2741b0e4cd31b010e7d859e8196`.
Definitions: [native parity modulus](../docs/TERMINOLOGY_RPB108_NATIVE_PARITY_MODULUS.md).
Lane: global/F4; no new aperture certificate.

## Result and limit

The actual full form has real supported logarithmic controls with Delta_p<0 in each parity sector. Thus the positive-kernel modulus proof for the shifted archimedean comparison cannot establish actual one-sign groundstates or actual kernel simplicity by extending its energy ordering to the prescribed primes and poles.

These are actual carrier vectors and actual energy differences, not actual null modes or negative-energy witnesses. The odd control lies inside the already certified a=1/2 window, where both energies are strictly positive. The even control at a=3/2 asserts no energy sign or positivity certificate. Neither control disproves a kernel-specific sign theorem at a hypothetical contact.

## Exact defect dictionary

For real h, the prescribed normalization is

\[
Q_a(h)=E0(h)-2\sum_n b_n I_{\ell_n}(h)
       +2M_-(h)M_+(h),\quad
I_\ell(h)=\int_{\mathbb R}h(x+\ell)h(x)\,dx,
\quad M_\pm(h)=\int h(x)e^{\pm x/2}\,dx.
\]

The quarter-line digamma energy from the preceding control is
\[
E0(h)=m0(0)\|h\|_2^2+
\tfrac12\iint k(|x-y|)|h(x)-h(y)|^2\,dx\,dy.
\]
For bounded interval-step profiles all these expressions are finite: their zero extensions have Fourier decay O(1/|xi|), hence belong to the logarithmic domain. The following identities also apply to real logarithmic profiles. To justify half-modulus domain preservation before subtracting energies, replace k by the bounded decreasing kernel min(k,N) in the archimedean energy. The half-plane computation below gives a nonnegative archimedean defect for both parities, because min(k(|x-y|),N)>=min(k(x+y),N). Monotone convergence as N increases bounds the half-modulus energy by the original energy and proves its logarithmic membership.

Let O(x,y) indicate opposite-sign pairs. Splitting into four physical half-planes gives
\[
\Delta_{arch}=4\int_0^a\int_0^a
 O(x,y)|f(x)f(y)|[k(|x-y|)+p k(x+y)]\,dx\,dy.
\tag{1}
\]
The singular diagonal has no contribution. In particular the odd archimedean ordering still holds, since k is decreasing and |x-y|<x+y. One may alternatively obtain odd domain preservation directly from this positive difference and the finite mass term.

The exact correlation split is
\[
I_\ell(h_p)=2\int_0^{(a-\ell)_+} f(x+\ell)f(x)\,dx
+p\int_{\max(0,\ell-a)}^{\min(\ell,a)}f(v)f(\ell-v)\,dv.
\]
Consequently
\[
\Delta_{prime,\ell}=8b_n\int_0^{(a-\ell)_+}
 O(x+\ell,x)|f(x+\ell)f(x)|\,dx
+4p b_n\int_{\max(0,\ell-a)}^{\min(\ell,a)}
 O(v,\ell-v)|f(v)f(\ell-v)|\,dv.
\tag{2}
\]

Put U_c=integral f_+ cosh(x/2), V_c=integral f_- cosh(x/2), and define U_s,V_s with sinh. The cross-pole dictionary gives Qpole(h_+)=8(integral f cosh)^2 and Qpole(h_-)=-8(integral f sinh)^2. Therefore
\[
\Delta_{pole,+}=-32U_cV_c,\qquad
\Delta_{pole,-}=32U_sV_s.
\tag{3}
\]
The reflected prime term competes with modulus in the odd sector; the pole term competes in the even sector. The pole cannot be replaced by independent positive squares.

## Odd actual control: one reflected prime overwhelms both positive defects

Set a=1/2, ell=log 2, eta=1/64. Let I,J have width eta and centers ell/3, 2ell/3, respectively; take f=eta^(-1/2)(1_I-1_J). The bounds 2/3<ell<7/10 put both intervals in (0,a). Only the n=2 prime is active, because log 2<1<log 3. No opposite-sign direct prime pair exists: its positive-half separation is ell/3 plus or minus eta, strictly smaller than ell. Reflection v -> ell-v maps I exactly to J. Thus the reflected opposite-pair integral in (2) is 2, and
\[
\Delta_{prime}=-8\log 2/\sqrt2.
\]

For s>0, k(s)<=1+1/(2s), using exp(-2s)<=1/(1+2s). On I times J, |x-y|>=ell/3-eta>=ell/4>1/6, so k(|x-y|)<4. Equation (1), with its two ordered rectangles and negative reflected arch term, gives Delta_arch<32 eta. Since sinh(x/2)<1 on (0,1/2), U_s,V_s<sqrt eta and Delta_pole<32 eta. Finally sqrt2<3/2 gives b_2>4/9, hence
\[
\Delta_-<64\eta-8b_2<1-32/9=-23/9.
\tag{4}
\]
Both full physical masses are 4. This is an exact negative energy difference inside a strictly positive actual window.

## Even actual control: avoid every prime cross pair and keep the pole defect

Set a=3/2. Let I,J have common width eta>0 and centers ell/2, 2ell. Their cross differences center at d=3ell/2 and cross sums at s=5ell/2. Neither d nor s is log n for an integer n: their exponentials are 2sqrt2 and 4sqrt2. There are finitely many active prime powers with log n<3. Choose eta smaller than the distance from d and s to every such log n, smaller than ell/8, and small enough that both intervals lie in (0,a). This is an exact positive finite gap, not a numerical prime enclosure.

With f=eta^(-1/2)(1_I-1_J), all opposite-sign integrals in (2) vanish. Same-sign prime products have zero defect. On I times J,
\[
|x-y|>11\ell/8>11/12,\qquad x+y>19\ell/8>19/12,
\]
so k(|x-y|)+k(x+y)<2+6/11+6/19=598/209. Equations (1) and (3), with cosh>=1, yield
\[
\Delta_+<8\eta(598/209)-32\eta
=-1904\eta/209<0.
\tag{5}
\]
Again both masses are 4. No actual endpoint, nullity, or sign of Q_a itself is inferred.

## Failed implication and smallest remaining theorem

Failed implication: actual reflection invariance plus the positive archimedean kernel -> full native energy decreases under half-modulus in each parity sector. Equations (4) and (5) disprove it on the actual carrier. Reflection still gives the certified even/odd split; it supplies no ordering within a parity block.

This obstruction belongs to endpoint exclusion. A kernel-specific assertion remains possible: at a nonnegative actual contact, every real null half-profile could satisfy Delta_p>=0 (and sufficient strictness or another independent kernel relation). Such an assertion needs the full null equation and arithmetic/source constraints; it is not a consequence of a universal energy ordering. If it did give one-dimensional parity kernels, that fact alone would still not supply global H1 or derivative invariance of the finite kernel. The already established regularity ceiling and archimedean control must still be addressed.

The minimal decisive obligation remains actual nonnegative-contact kernel exclusion (or an actual null H1/near-exponential action theorem that implies it). Retained packet attachment and same-vector enlarged transport are separate obligations from the global entry audit; none is discharged here. No fresh selected packet is identified with retained P,C,k.

## Custody and validation

Pinned inputs: ARCHIMEDEAN_CONTACT_CONTROL_20261006 (exact Euler/Laplace energy and its comparison limitation); ACTUAL_CORRELATION_POLES_20261004 (certified opposite-slot pole identity); CERTIFIED_PARITY_SCHUR_BLOCK_20261005 (actual reflection invariance and prime-source normalization); GLOBAL_F4_ENTRY_AUDIT_20261006 (separate endpoint, retained attachment and transport obligations). Source blob custody is in the manifest.

The rational script checks exponential bounds for log 2, sqrt2 and the constants, all two-point sign-defect identities, and finite-gap center irrationality via squared values. The finite-gap existence, domain membership, integral decompositions and exact inequalities above are analytic arguments; the script is not a Lean proof, null computation or eigenvalue certificate. No Lean/workflow change or new CI/axiom claim. F4 and FULL TRANSPORT CLOSED remain open.
