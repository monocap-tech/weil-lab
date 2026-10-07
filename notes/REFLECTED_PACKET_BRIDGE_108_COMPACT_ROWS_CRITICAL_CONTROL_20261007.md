# RPB108: compact good rows can carry a divergent critical moment

Date: 2026-10-07 UTC. Recovered global head 3561b09df97ffd10ceb6ac328ae7e85831a17a2b; publication incorporates the newer concurrent aperture head.
Definitions: [compact rows and the physical control](../docs/TERMINOLOGY_RPB108_COMPACT_ROWS_CRITICAL_CONTROL.md).
Category: endpoint exclusion obstruction. Analytic supported-profile control; not an actual null vector, arithmetic certificate or Lean proof.

## Result and failed implication

The NF23 decomposition retains the EXACT actual equation

    <P0 h,P0 v>=<N_good h,N_good v>+<N_exc h,N_exc v>

for every canonical v at a hypothetical actual contact. It does not justify replacing the good term by a critically bounded error. This pass disproves that replacement from compactness and the available upper count statistics alone: a single supported physical vector has all subcritical logarithmic Sobolev norms finite, but its critical negative moment diverges on a compact, eventually entirely GOOD artificial row map. There need be no exceptional high rows at all.

The control uses the same sinh/cosh profiles and the improved transverse bound 3/8. It satisfies much stronger cumulative transverse sparsity than the imported density estimate. Unlike a freely assigned coefficient sequence, every observation below comes from the same physical vector. It does NOT satisfy the actual full-native null equation. Thus this is an obstruction to a compact-row inference, not a counterexample to actual endpoint exclusion.

## 1. One supported physical series

Use the registered triangle f, heights H_j and coefficients c_j. The support lies inside any a>3/16. Since sum c_j<2, h=sum c_j exp(-iH_j x)f converges absolutely in physical L2. The triangle belongs to H^s for s<3/2. For every 0<=s<1/2 its modulations satisfy

    ||exp(-iH_j x)f||_(H^s_log)
        <=C_s H_j^s sqrt(log(e+H_j)).

Here H^s_log means Fourier square weight (1+|xi|)^(2s)log(e+|xi|); fixed 2pi rescaling changes constants. This estimate follows from the Fourier weight inequality and the triangle's H^(s+delta) norm for small delta>0. Consequently the sum of weighted norms is bounded by

    C_s sum_j H_j^(s-1/2) sqrt(log(e+H_j)/j)<infinity.

Thus h lies in the canonical logarithmic domain and every subcritical space supplied by the null bootstrap. No endpoint regularity is inserted.

## 2. Cross-frequency cancellation is bounded, not assumed absent

Let b=3/8 and g_-=f sinh(bx), g_+=f cosh(bx). Their distributional second derivatives have total variation at most 100. Indeed TV(f'')=64, integral |f'|=2, integral f=1/16, and 0<bx<=9/128. The geometric even/odd series bounds give cosh(bx)<9/8 and sinh(bx)<1/8. The product formula bounds either second derivative by 64*(9/8)+4*b*(9/8)+b^2*(9/8)/16<100. Integration by parts in distributions therefore gives

    |F_(g_+)(u)|, |F_(g_-)(u)| <=100/|u|^2, u!=0.

At height H_j the dominant term in n_j is c_j integral g_-. Its real value is at least c_j*(3/2048), since sinh(bx)>=bx, x>=1/16 and integral f=1/16. Other frequencies have total absolute contribution at most

    400 H_j^(-2) sum_(i<j)c_i
      +400 sum_(i>j) H_i^(-5/2)
    <=1600 H_j^(-2).

The gaps are at least half the larger height; sum c_i<2 and the repeated squaring bounds the later series. Since H_1=2^32, H_j>=H_1^j and sqrt(j)<=2^j, this error divided by c_j is at most

    3200/2^48 < 3/4096.

No cancellation between different packets can remove the dominant negative observation. Therefore

    |n_j(h)| >=(3/4096)c_j,
    sum_j H_j |n_j(h)|^2 >=(9/16777216)sum_j 1/j=infinity.   (1)

Exactly the same cross-frequency estimates show |p_j|>=c_j/32 and |n_j|<=c_j/64: integral g_+>=1/16, integral g_-<=1/128 and the above error is smaller than 1/128. Hence each signed difference is at least (3/4096)c_j^2, and its sharp critical signed sum also tends to +infinity. No neutral norm balance or full mixed nullity is asserted for this control.

## 3. These rows are compact good rows, not exceptional rows

Each occupied unit bin contains a single beta^2=9/64. Its normalized transverse mass is (9/64)/log(e+H_j), tending uniformly to zero. The same local sampling/sinh-series proof as NF23 applies to these profiles and proves their unweighted negative analysis compact on the supported logarithmic domain. Moreover that mass is eventually below 1/log log(e^e+H_j), so the exceptional high-row set is EMPTY.

The transverse count through T is O(log log T), with at most one copy per occupied bin. This meets the previous local upper count and cumulative second-count upper bounds. Reflection and sign partners change only fixed constants and preserve compactness, sparsity and (1). These statements concern upper statistics, not the actual divisor's explicit formula or total zero-count asymptotic.

Thus even full negative compactness and subcritical regularity of one supported physical vector cannot give a critical negative moment bound. In particular an estimate only on N_exc, even one setting it identically to zero, would not dispose of the critical good-row term. Compactness controls an unweighted tail; multiplication by height is unbounded and destroys that inference.

## Actual contact equation and smallest remaining theorem

On actual K, the exact equation above relates ALL canonical tests, not merely <P0h,P0h>=||N0h||^2. It is still the missing zero-specific information. The preceding control cannot be inserted into that equation. Nor can the actual positive-eigenvalue control be declared null: its residual is mu<h,v>.

To close the endpoint using the decomposition, one must establish a bound on the COMPLETE signed source-height graph error on the whole actual zero-contact kernel, retaining both good and exceptional channels, or another zero-specific estimate implying its critical positive-source trace is finite. NF17 then promotes the whole kernel into H1 and the derivative-chain contradiction excludes contact. The arithmetic estimate remains unproved. No additional generic compactness theorem can supply it; a proposed proof must use the unshifted actual full mixed equation in a way that fails for the shifted positive mode.

This is an endpoint-exclusion obstruction, not retained attachment or null transport. It strengthens the prior rare-cluster control by eliminating exceptional high bins and enforcing physical coherence of all observed coefficients. It does not change the closed critical-promotion theorem or claim new arithmetic regularity.

## Source custody and validation

Pinned repository inputs at 3561b09df97ffd10ceb6ac328ae7e85831a17a2b:
- LOCAL_TRANSVERSE_COMPACTNESS_20261007: e3dfe9f4c356f7d5ed2364f0f7c8dc99ec39ef61.
- TRANSVERSE_DENSITY_SAMPLING_20261007: c9950fafef341ee66f62a5b1ab21013ebfd3a716.
- SOURCE_HEIGHT_GRAPH_ERROR_20261007: b968aa0a3c5eb5ba680ee0251692e24853dadd74.
- CRITICAL_RECIPROCAL_PROMOTION_20261007: 9983be22ab58e926b5e15127f8feaf53d43329e0.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.

No new external theorem imported. The companion rational check verifies triangle constants, exponential brackets, the uniform cross-error margin, coefficient/signed margins and harmonic block divergence bounds. It does not test actual zeros or certify the infinite-dimensional analytic proof. No Lean executable/build/axiom audit. Canonical cursor and definitions updated additively; concurrent aperture work preserved. Endpoint, retained attachment, same-vector enlarged transport and F4 remain open.
