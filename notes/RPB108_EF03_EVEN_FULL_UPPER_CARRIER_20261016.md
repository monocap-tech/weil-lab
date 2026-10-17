# RPB108 EF03 — full original signed-negative EVEN upper carrier and sharpened finite gate

**Obligation:** W-EVEN-FORM; explicit local focus while canonical W-ODD-NEG stays active.
**Parent:** current research head 750695af1403c8c72fdaa5cb7553722737773b98 (merged SM09); also includes the EF02 final-head verified artifacts from conflicting PR #138 on a fresh branch.
**Standing:** analytic original-even parity transplant of the SM09 all-frequency upper operator, together with a replayable exact-rational SI10 cover, rank, global infinite-tail and Young-budget certificate. **No finite true positive inverse Gram eigenvalue has been certified.**

## 1. Both signs of every original frequency, and the actual supported EVEN carrier

Let H_e=L²([-B,B])_even, B=11/10, κ=1/1000.
The original seven-prime archimedean signed multiplier is
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
 -2\sum_{n\in\{2,3,4,5,7,8,9\}}
 \frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n).
\]
Following EF01 and SI11, put \(a=\max(m,\kappa)\), \(r=(\kappa-m)_+\),
\[
Q_e=A_e-K_{\mathrm{neg},e},\qquad
A_e=Z^*\mathcal F^{-1}a\mathcal FZ|_{H_e}
      +2|c\rangle\langle c|,\quad c(x)=\cosh(x/2).
\]
The Fourier multiplier is **original signed**, the even pole is **positive**, and all operators are imposed on compact physical support. No unsupported pointwise inverse of a on the whole line is used.

Let \(U_+\) be SI10's 973 rational unresolved leaves grouped into 107 positive-frequency clusters. Its exact original signed lower enclosure proves \(r=0\) on the exterior, including [896,1200] and all |ξ|≥1200. On each positive-frequency unresolved leaf I, the original negative cap height \(h_I\) satisfies
\(r(\xi)\le \kappa+h_I\). Reflect the leaf to negative frequencies and set
\[
w(\xi)=\sum_{I\in U_+}(\kappa+h_I)\mathbf1_I(\xi)
\quad(\xi\ge0),\quad w(-\xi)=w(\xi).
\]
This upper envelope, unlike a lower negative-band packet, covers the **entire** unknown true negative multiplier \(r\):
\[
0\le r\le w,\quad
\int_{\mathbb R}w=M+\kappa W
=\frac{1204033883}{32000000}=37.62605884375.
\]
The κW correction is essential even when m is positive but less than κ.

With real even physical features \(h_\xi(x)=\cos(2\pi\xi x)\), the original true and cap negative operators satisfy
\[
0\preceq K_{\mathrm{neg},e}
=2\int_0^\infty r(\xi)|h_\xi\rangle\langle h_\xi|\,d\xi
\preceq
K_{\mathrm{cap},e}
=2\int_0^\infty w(\xi)|h_\xi\rangle\langle h_\xi|\,d\xi.
\]
All selected and unselected original negative-frequency bands are represented, including EF02's fifteen independently signed-negative even packets.

## 2. Correct finite EVEN Taylor space and full cross-coupled tail

For each certified positive-frequency cluster center c_j and SI08 Taylor order p_j(b), take the physical even derivative functions
\[
\partial_\xi^k \cos(2\pi\xi x)\big|_{\xi=c_j},\qquad 0\le k<p_j(b).
\]
Every derivative is even in x, including odd k (x sin term), so positive and negative mirrored clusters require one even column per order. Let E_{b,e} be their physical L² span and P its orthogonal projection. At b=24, the dimension ceiling is **890**; at b=20 it is 780; at b=32 it is 1075. These are dimension ceilings, not numerical finite matrices.

From SI08's whole-cluster Taylor remainder, for every ξ in every unresolved leaf
\[
\|(I-P)h_\xi\|_{H_e}\le\sqrt{2B}\,2^{-b}.
\]
Let R_cap be the true continuous weighted even analysis operator, \(R_{\rm cap}^*R_{\rm cap}=K_{\mathrm{cap},e}\).
The entire original reflected cap mass gives
\[
\boxed{\|R_{\mathrm{cap}}(I-P)\|^2
\le e_b^2:=2B(M+\kappa W)2^{-2b}.}
\]
Decompose R_cap into R_cap P and R_cap(I-P). For every τ>0 use the correct Young sign
\[
\|u+v\|^2\le(1+\tau)\|u\|^2+(1+\tau^{-1})\|v\|^2
\]
to pay **all** low/high cross couplings. Therefore, in actual even physical Loewner order,
\[
\boxed{K_{\mathrm{neg},e}\preceq K_{\mathrm{cap},e}
\preceq (1+\tau)PK_{\mathrm{cap},e}P+
\delta_b(I-P),}
\quad \delta_b=(1+\tau^{-1})e_b^2.
\]
This is an actual, finite-rank-plus-tiny-infinite-tail **operator upper bound** for the original signed negative part; it does *not* prove A_e dominates the upper bound.

## 3. A sharpened τ tradeoff and the exact finite supported test

EF01 instead estimated \(\|K-PKP\|\le4B(M+\kappa W)2^{-b}\), resulting at b=24 in relative \(\eta/\kappa<0.009868\). EF03's cap-plus-Young inequality is a **different, more conservative finite operator** but drastically improves the infinity-tail budget.

With b=24 and τ=1/65536, exact rational replay gives
\[
e_{24}^2=2B(M+\kappa W)\,2^{-48}
\approx2.940842\times10^{-13},
\]
\[
\boxed{\delta_{24}<1.93\times10^{-8},\qquad
\delta_{24}/\kappa<1.93\times10^{-5}.}
\]
In particular, the infinite complement is paid on the actual even supported carrier, including all cross contributions. The choice τ=1/65536 sharpens the finite coefficient compared with SM09's initial τ=1/1024 (which gives δ<3.015×10⁻¹⁰ but a larger 1+τ multiplier). It is a deliberate spectral slack trade, not monotonic improvement in both parameters.

Let \(U_b:\mathbb C^{d_{b,e}}\to H_e\) be **orthonormal physical synthesis** onto E_{b,e}, and set
\[
M_{\mathrm{cap},b}=U_b^*K_{\mathrm{cap},e}U_b,\qquad
G_b=U_b^*A_e^{-1}U_b.
\]
The cap matrix contains the **entire actual rational upper-weight continuum**, not just sampled frequencies. The actual supported inverse G_b retains all original positive Fourier effects and the favorable rank-one positive even pole.

Define
\(\Lambda_b=\lambda_{\max}(M_{\mathrm{cap},b}^{1/2}G_bM_{\mathrm{cap},b}^{1/2})\).
Since \(A_e\succeq\kappa I\), a sufficient **fully scoped** condition is
\[
\boxed{(1+\tau)\Lambda_b+\delta_b/\kappa\le1
\quad\Longrightarrow\quad Q_e\succeq0.}
\]
It follows by conjugating the Loewner upper bound by \(A_e^{-1/2}\):
the finite part has norm \((1+\tau)\Lambda_b\), and the infinite
residual costs at most δ_b/κ. Neither the missing finite matrix nor its spectral radius has been calculated, so this is a **conditional gate**, not a new full-even positivity theorem.

At b=24, τ=1/65536, the exact budget permits
\[
\Lambda_{24}<0.9999654\quad
\text{(numerical display of the exact rational threshold)}
\]
and the deliberately stronger **simple rational sufficient**
target \(\Lambda_{24}\le 0.99996\) satisfies the strict complete condition.
This is far less finite-eigenvalue slack than EF01's true negative finite operator criterion (~0.990132), **but it involves the bigger cap matrix**; neither criterion dominates the other without the actual G_b and cap eigenvalues.

The positive even pole has the exact supported inverse response
\[
A_e^{-1}=A_{0,e}^{-1}-
\frac{2|A_{0,e}^{-1}c\rangle\langle A_{0,e}^{-1}c|}
{1+2\langle c,A_{0,e}^{-1}c\rangle}.
\]
Dropping this favorable correction is a valid but potentially very wasteful *upper bound* for the inverse; it cannot be called equality. Any residual-based upper bound for G_b must include its positive \(E^*A_e^{-1}E\) term.

## 4. EF02 reconciliation, scope and next action

EF02's original signed-negative even 15-packet rank regression and the associated source note had final-head Actions PASS (EF02 39011589598, EF01 39011589607, governance 39011589579), but PR #138 could not merge once the shared research branch advanced; this reconciliation retains EF02's **identical validated source blobs** while introducing EF03 from current SM09 HEAD. EF02's \(\lambda_{15}(K_{\mathrm{neg},e})>0.0152526\) is a genuine obstruction only to scalar-floor-plus-rank≤14 positive *lower references*, not to the original full operator A_e.

**W-EVEN-FORM remains OPEN.** EF03's substantive result is a full-frequency, physical even Loewner upper cap with the entire infinite residual and mixed terms quantified. The remaining finite original supported cap inverse eigenvalue can fail; EF03 does not pretend to certify it.

**Next closure-oriented step:** actually compute or rigorously enclose \(M_{\mathrm{cap},b}\), \(G_b\) and **all cross-Grams**, or derive a smaller native RC even-carrier Schur with explicit domain/metric transport. The 890-dimensional cap is an explicit sufficient route, not a promise that its spectral threshold is attainable. Detect a cap-overestimate obstruction before performing a giant inverse search.

**Replay:** python3 scripts/validate_rpb108_ef03_even_full_upper_carrier.py. Its exact rational check verifies cover accounting, parity rank, δ and τ budgets, and a two-dimensional strict cross-sign regression. It does **not** execute the missing finite 890×890 supported inverse calculation or independently peer-review the analytic original-zeta identifications.
