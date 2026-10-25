# NF — Original 960-cell low12 source-only MG07 method-stop certificate

**October 24, 2026. Active W-ODD-NEG remains OPEN.** This is a shorter **complete-original source-ray** method-specific proof gate, not a proof of RH or universal signed odd positivity.

## Why low12 replaces low32

The previous original 2,240-cell gate integrates \(K_- -\tfrac{97}{100}A_\star\) over \([0,32]\), paying the positive multiplier tail beyond 32. There is no need to integrate all of \([12,32]\) if the original positive action on the ENTIRE \(|\xi|>12\) band can be paid using the already established true physical sine/sinh endpoint-decay estimate.

Use exactly the same original physical odd supported rays at \(B=11/10\), \(c=37/64\):
\[
u(x)=1_{[-B,B]}\sin(2\pi c x),\quad
s(x)=1_{[-B,B]}\sinh(x/2),\quad
f_d=12001u+16384s,\quad f_c=3013u+4096s.
\]
The true original Fourier multiplier is the complete signed seven-prime/digamma \(m(\xi)\). Define
\[
w(m)=(\kappa-m)_+-\tfrac{97}{100}\max(\kappa,m),\quad
A_\star=A_o-2ss^*,\quad A_o=\max(\kappa,m)(D).
\]
For any genuine original ray \(f\), the full method-test quadratic has the rigorous lower:
\[
\boxed{
\langle f,(K_--0.97A_\star)f\rangle
\ge 2\int_0^{12}w(m(\xi))|T_f(\xi)|^2\,d\xi
 -0.97\,T_{\rm Ao,>|12|}
 +0.97\cdot 2|\langle f,s\rangle|^2 .}
\]
The discarded high-negative \(K_-\) is nonnegative, and the remaining high-positive \(A_o\) term is paid completely.

## Exact global-curvature enclosure and true original Fourier packet

The original SM40 entire seven-prime curvature satisfies \(D_2<900\), and SM43A's entire quarter-digamma second derivative satisfies \(D_{\rm arch}<1400\). Thus the deliberately conservative constant \(D_{\rm original}=2300\) is a valid global curvature upper at **every** real frequency (no local curvature calculation is needed).

Partition \([0,1]\) into 256 cells of width \(1/256\), and \([1,12]\) into 704 cells of width \(1/64\), totaling **960 exact rational cells**. The original SI06 prime-phase and newly sharpened gamma/convex digamma 64-term exact endpoint intervals enclose both endpoint values of \(m\). For each cell of width \(h\),
\[
 |m(\xi)-m_*(\xi)|\le\varepsilon_I=
 \max(\text{endpoint interval radii})+\frac{2300h^2}{8}.
\]
The true original SI42 sine/sinh Fourier value and derivative at the rational midpoint are rationally enclosed. The entire real source curvature
\[
 |T_f''(\xi)|\le4\pi_{\rm up}^2
 \left(a\frac{2B^3}{3}
 +b\frac{2B^3}{3}\sinh(B/2)_{\rm up}\right)
\]
bounds the physical linearization error. Each cell's \(w(m_*)|T_*|^2\) is integrated exactly as an affine-times-quadratic polynomial. Every real multiplier and Fourier error is subtracted, and all cells are downward-rounded to exact Fractions. Cells crossing \(m=\kappa\) retain the strongest rigorously paid floor, two global affine minorants, and rational two-piece quartic antiderivative. Nothing is sampled for acceptance.

The true supported endpoint jump is retained. For \(L=12\),
\[
 \beta_L=\frac{|f(B)|_{\rm up}}{\pi_{\rm lo}}
 +\frac{2|f'(B)|_{\rm up}+\|f''\|_{1,\rm up}}
 {4\pi_{\rm lo}^2L},
\quad
\boxed{\int_{|\xi|>12}a_o(\xi)|\widehat f(\xi)|^2d\xi
 \le\frac{2\beta_{12}^2}{12}
 (18+\log_{\rm hi}12).}
\]
The original SI14 endpoint and SI12 hyperbolic certificates bound the direct ray by \(|f(B)|<425\), \(|f'(B)|<19200\), and the cap-selected ray by \(|f(B)|<97\), \(|f'(B)|<4850\). The whole original positive tail upper is less than **3,200,000** on the direct ray and **200,000** on the cap ray. The genuine original SI18 two-source Gram yields the exact lower for \(2|\langle f,s\rangle|^2\); no pole term is guessed.

## Independent local exact-rational arithmetic — status and limits

A separate local Python reimplementation of the original SI06 rational \(\pi,\log\), seven prime powers, quarter-digamma 64-term + new gamma/convex tail, SI42 source sine/sinh Fourier intervals and physical second derivative, **using the even more conservative GLOBAL \(2300\) multiplier curvature**, executed all 960 cells in approximately 29 seconds. Its independently calculated downward-rounded exact lowband lower sums were:

| Genuine ray | Local 960-cell lowband exact-rational lower | Conservative complete tail | Preliminary total strict lower |
|---|---:|---:|---:|
| \(f_d\) | \(-55,354,893.630107\) | \(<3,132,000\) | \(>+1,280,000\) |
| \(f_c\) | \(-3,468,035.032463\) | \(<193,000\) | \(>+84,000\) |

The above strict-margin displays are from the independent local implementation and rounded conservatively; **they are NOT yet the canonical repository acceptance artifact**. The original Python script, source-endpoint helper imports, and all exact rational identities must replay in GitHub Actions and be independently reviewed before promoting a formal theorem result. In particular, the local implementation uses a slightly different outward sine/cosine enclosure than SI06/SM42; the focused repository validator is the source of record for the final exact rational margins.

The **new canonical executable** is [960-cell original low12 verifier](../scripts/validate_rpb108_mg07_original_low12_960cell_stop.py), with an isolated [focused acceptance workflow](../.github/workflows/rpb108-mg07-original-low12-method-stop.yml), exact output at \`artifacts/mg07_true_original_low12_960cell.json\`, and a strict fail-closed one-ray positive assertion. Its low-frequency numerical computation has **not yet** been reported passing by CI.

If the original exact positive witness passes, the scoped mathematical conclusion is that the chosen source-only \(J_{470}\) Ritz/SM40-cap **sufficient** criterion fails on a genuine source ray: \(K_{\rm cap}\succeq K_-\) and the inherited exact SM40 source threshold \(\theta_{\rm SM40}<0.97\). It does **not** imply \(\langle f,W_of\rangle<0\), rule out SI29-augmented trial spaces, or prove universal original signed odd/even positivity, CC27/Weil or RH.

**Priority:** Verify this exact 960-cell artifact first, rather than accumulating further supporting tail certificates.
