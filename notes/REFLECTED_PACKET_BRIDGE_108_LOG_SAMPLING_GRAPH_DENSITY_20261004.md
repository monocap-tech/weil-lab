# RPB108: logarithmic sampling and fixed-window full graph density

Base: research 1f4e751f87e53cd5db7538010d54da8546b486ea.

## Carrier theorem

For each a>0 there is a finite C_a such that every complex L2 vector h supported in [-a,a] with logarithmic energy
\[
E_{\log}(h)=\int_{\mathbb R}\log(e+|\xi|)|\widehat h(\xi)|^2\,d\xi<\infty
\]
satisfies
\[
\sum_{q\ {\rm raw}}|F_h(z_q)|^2\le C_a E_{\log}(h),
\qquad F_h(z)=\int h(x)e^{izx}\,dx.
\]
Consequently every supported logarithmic vector has a unique complete actual source-graph lift. Physical projection identifies that graph with the logarithmic carrier by mutually bounded canonical maps, preserving the same vector and every source coordinate.

Moreover the actual Green graph closure equals the entire actual source graph at this fixed window. This equality is proved below, not assumed. The source/native quadratic and mixed identities already certified on the Green closure therefore extend analytically to the whole supported logarithmic domain.

## Independent arithmetic input: local count

Hasanalizade, Shen and Wong, Counting zeros of the Riemann zeta function, Corollary 1.2, give the actual N(T) main term with O(log T) error for T>=e:
https://arxiv.org/abs/2107.06506
https://arxiv.org/pdf/2107.06506

Subtracting at T and T+1 yields an O(log T) unit-window count. Conjugation handles negative heights; local finiteness absorbs the bounded central region. Thus for some finite A,
\[
\#\{q:t<\Re z_q\le t+1\}\le A\log(3+|t|)
\]
for every real t, including actual multiplicities. Here Re z_q is the actual ordinate. The standard zero-count convention counts multiplicities. No simplicity or spacing lower bound is used.

This is a stronger local estimate than the earlier dyadic count. Dyadic O(T log T) alone would not supply the argument below. The external published local input is explicit, rather than silently inferred from that weaker estimate. The vendored Def_Zeta23_RvM_LocalCount file documents the same desired local estimate but is a definitions module; it is not cited as a locally certified proof.

## Uniform strip evaluation from a reproducing kernel

Choose psi in C_c^\infty(R), equal to one on [-a,a]. For |y|<=1/2 define
\[
K_y(v)=\frac1{2\pi}\int\psi(x)e^{-yx}e^{ivx}\,dx.
\]
Two integrations by parts, and a direct bound for |v|<=1, give a finite D_a with
\[
|K_y(v)|\le D_a(1+|v|)^{-2}
\]
uniformly in this closed strip. All derivatives of psi(x)e^{-yx} through order two have uniformly bounded L1 norms because its support is fixed.

Fourier inversion applied to the smooth cutoff multiplier gives
\[
F_h(t+iy)=\int_{\mathbb R}F_h(s)K_y(t-s)\,ds.
\]
One justification first establishes the identity in L2 on the real axis for the transform of psi(x)e^{-yx}h(x). The convolution is continuous by the L2 translation estimate, and the physical transform is continuous because the product is compactly supported L1. The a.e. equality is therefore pointwise. The integral is absolutely convergent by Cauchy-Schwarz.

Writing r(v)=(1+|v|)^{-2}, with integral two, weighted Cauchy-Schwarz yields
\[
|F_h(t+iy)|^2
 \le 2D_a^2\int |F_h(s)|^2r(t-s)\,ds.
\]

## Summing over the full raw divisor

Fix s and let m=floor(s). Partition the ordinates into (j,j+1], j in Z, and write j=m+k. On that interval,
\[
r(t-s)\le9(1+|k|)^{-2},
\quad
\log(3+|j|)\le\log(3+|s|)+\log(2+|k|).
\]
The first inequality follows from |t-s|>=max(0,|k|-1); the stated factor nine is more than sufficient. The second follows from |j|<=|s|+1+|k| and
4+|s|+|k|<=(3+|s|)(2+|k|).

The local count and convergence of both series
\[
\sum_k(1+|k|)^{-2},\qquad
\sum_k\log(2+|k|)(1+|k|)^{-2}
\]
therefore prove
\[
\sum_q r(\Re z_q-s)\le C A\log(3+|s|)
\]
for an absolute finite C. Tonelli now sums the nonnegative strip bound:
\[
\sum_q|F_h(z_q)|^2
 \le 2D_a^2CA\int\log(3+|s|)|F_h(s)|^2\,ds.
\]
With s=-2pi xi, F_h(s)=Fourier(h)(xi). The weights log(3+2pi|xi|) and log(e+|xi|) are comparable, so this proves the carrier estimate. The change of variables contributes the finite factor 2pi. All repeated raw copies stay in the sum.

## The canonical graph is the logarithmic carrier

For the normalized actual pair coordinates p,n, partner reindexing gives
\[
\|p_h\|^2+\|n_h\|^2=\sum_q|F_h(z_q)|^2.
\]
Their unnormalized graph coordinates are sqrt(2)p,sqrt(2)n. Thus the lift L_a obeys
\[
E_{\log}(h)\le\|L_a h\|_{\rm graph}^2
 \le(1+2C_a)E_{\log}(h).
\]
The graph's coordinate equations force its samples to be precisely those of its physical vector. The sampling bound constructs those lp2 vectors for every logarithmic vector; hence the lift and physical projection are inverse maps. This resolves source summability on the full canonical supported domain without imposing H1 or spectral operator-domain membership.

The graph coordinates still supply custody and the exact energy bookkeeping. They impose no smaller analytic domain after this estimate.

## Fixed-window smooth density

For 1/2<=r<1 set h_r(x)=h(x/r). Its support lies in [-ra,ra], and
\[
\widehat h_r(\xi)=r\widehat h(r\xi).
\]
The dilation maps on weighted L2 are uniformly bounded near r=1:
\[
E_{\log}(h_r)
 =r\int w(\eta/r)|\widehat h(\eta)|^2\,d\eta
 \le(1+\log2)E_{\log}(h).
\]
Here w(eta/r)<=w(eta)+log2<=(1+log2)w(eta). They converge strongly to the identity: prove this for compactly supported continuous Fourier functions by dominated convergence, then extend using their density in weighted L2 and this uniform bound.

For each fixed r<1, convolve h_r with a compact smooth probability mollifier of radius epsilon<a(1-r). The result is C_c^\infty(-a,a). Its real Fourier multiplier has modulus at most one and tends pointwise to one, so dominated convergence gives logarithmic convergence to h_r. Choose r_j tending to one and epsilon_j small enough that the mollification error is below 1/j. This proves density of C_c^\infty(-a,a) in the supported logarithmic domain itself. No boundary trace regularity of h is assumed.

The newly proved sampling estimate upgrades this logarithmic convergence to whole source-graph convergence. Each smooth vector is H1_0(-a,a), so its lift belongs to the actual Green closure by the previous H1 theorem. Closedness now puts the lift of every logarithmic vector in that closure. Every graph vector is such a lift; hence full fixed-window graph density follows.

The H1 theorem uses the previously documented Bui-Conrey-Young distinct-critical-zero density input. This dependency remains, and is not replaced by a claim of simplicity of all zeros.

## What closes, and what remains

Every retained vector already identified with this supported logarithmic physical carrier now has an actual source-graph lift and Green-closure membership automatically. Source/native diagonal and polarized mixed forms agree on the entire domain. This removes both source-summability and graph-membership requirements from that identified vector.

An abstract WD-T38 construction still needs its same physical vector identified with this carrier and its retained quadratic or weak-null identity attached to the actual native form. Bounded sampling alone does not establish that identity.

The positive-energy quotient still has its own norm: the estimate above bounds S_+ and S_B by logarithmic energy, but does not prove
\[
\|S_B f\|\le\|S_+ f\|.
\]
The earlier injectivity result supplies ker S_+=0 on the actual domain, hence the kernel inclusion and algebraic factorization. A unit contraction on the positive completion still requires the displayed independent inequality. Upper sampling bounds do not supply an inverse sampling bound.

Nor does this theorem identify the inherited norm on the raw synthesis quotient lp2/ker G with the logarithmic or positive norm. Observational redundancy can be quotiented, but quotient topology and stability must be proved separately.

Enlargement preserves the same-vector source coordinates. It still does not prove weak-null vanishing against additional enlarged tests. FULL TRANSPORT CLOSED and F4 entry remain open.

## Validation and cursor

This theorem and its full-density consequence are analytic. The published local count is externally sourced; no claim is made that it has been instantiated on our raw carrier in Lean. No Lean source/workflow changes. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775. Those checks do not certify this new proof.

At 1f4e751, the actual unit-window zero count O(log(3+|t|)), sourced from Hasanalizade-Shen-Wong Corollary 1.2, and a compact cutoff reproducing kernel prove full raw-copy sampling bounded by supported logarithmic energy. Thus the actual source graph is canonically boundedly equivalent to the supported logarithmic carrier, with a unique same-vector lift for every logarithmic vector. Inward dilation and compact convolution prove fixed-window smooth density; the preceding H1 Green theorem then proves the entire actual source graph equals its Green closure. Source/native quadratic and mixed identities therefore hold on the full supported logarithmic domain. These are analytic deductions, not new Lean certification. An abstract WD-T38 witness still needs identification with this same physical logarithmic vector and its null identity; general WD-T10 unit domination and enlarged weak-null persistence remain open. No equivalence with the inherited raw-synthesis quotient norm or positive-energy completion is asserted without the needed lower bound. FULL TRANSPORT CLOSED and F4 entry remain open; SOURCE is off the critical path.
