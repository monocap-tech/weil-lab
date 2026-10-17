# RPB108 EF10 — integrate the physical Fourier amplitude cone, not a whole-cell minimum

**Obligation:** W-EVEN-FORM (Priority 2). The original W-ODD-NEG remains canonical and unchanged.

**Parent:** EF09 PR #157; exact rational run 39049775807 SUCCESS.
EF09 complete unchanged conservative-cap lower is
\(0.8724438013669181\). EF08 independently certified whole original
signed-positive operator **upper** \(0.877810281338208\) (the
reused safely rounded certificate is \(0.877811\)).
EF09 therefore remains **STILL_INCONCLUSIVE**, with conservative
separation lower \(-0.005367198633081902\).

## A structural, not brute-resolution, sharpening

The actual zero-extended supported cosine Fourier transform \(F\)
satisfies the independently established original global bound
\(|F'|\le D=2\pi_{\mathrm{up}}B^2\).
For any rational cell \([u,v]\), center \(q=(u+v)/2\), halfwidth
\(h=(v-u)/2\), and rigorously outward-rounded
\(a\le |F(q)|\), the reverse triangle inequality gives

\[
|F(\xi)|\ge \max(0,a-D|\xi-q|)\quad
(\xi\in[u,v]).
\]

Unlike EF09's whole-cell minimum,
we rigorously integrate its squared **triangular cone**:
\[
J(a,h,D)
=2\int_0^h \max(0,a-Dt)^2\,dt
=\begin{cases}
2(a^2h-aDh^2+D^2h^3/3),&a\ge Dh,\\
2a^3/(3D),&a<Dh.
\end{cases}
\]
Then \(2wJ(a,h,D)\) is an exact valid rational lower on the
**both-reflected-frequency** physical contribution of the same original
nonnegative cap weight \(w\).

EF10 keeps **exactly** EF09's 1024 [0,1] and 1936 [1,4]
subcells, corresponding to the original 256 and 121 signed-cap
weights respectively. Retain all 788 nonnegative high-frequency
original leaves with lower zero, not dropped from the operator.
Round each exact nonnegative charge DOWN to \(10^{-12}\), losing at
most \(2.96\times10^{-9}\) in the whole sum. The original full
cap-weight mass and the supported Fourier and pole definitions
are unchanged.

The final test compares this improved **cap** lower with the
**actual** original full positive-energy upper from EF08.

If cap lower exceeds \(0.877811\), this certifies a method-class
counterexample to domination by **the refined conservative cap**,
not negativity of the actual even Weil operator:
\[
K_{\mathrm{true},e}\preceq K_{\mathrm{cap},e}
\quad\not\Rightarrow\quad
K_{\mathrm{true},e}\not\preceq A_e.
\]
Do not promote a result about the cap to a result about true
\(K_{\mathrm{true},e}\).

If still overlapping, don't claim cap feasibility. An appropriate
next move is to switch to the *actual* original signed two-vector
operator or quantify the remaining local enclosures.

**Status:** candidate; final-head focused CI and obligation governance
required. Complete original even PSD, whole Weil, global bridge,
Lean original certificate and RH remain OPEN.
