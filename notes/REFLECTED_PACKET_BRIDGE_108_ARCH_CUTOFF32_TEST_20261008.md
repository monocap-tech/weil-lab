# RPB108 NF64: 32-term compact gains fail on actual physical witnesses

Date: 2026-10-08 UTC (2026-10-07 Pacific). Recovered head 76a2ef43f9495d2a076fd1e0e472c7645e681f49.

The concrete 32-term candidate is now rigorously tested and rejected. Two explicit rational physical vectors prove Q_32 negative: at the certified-positive ORIGINAL aperture a=1 and at a=21/20. This is a failure of the finite archimedean LOWER form, not of the original Weil form. It preserves NF63's convergence theorem while showing that its positive background alone is far from the full sign.

Definitions: [cutoff witnesses](../docs/TERMINOLOGY_RPB108_ARCH_CUTOFF_WITNESS.md) and [finite archimedean forms](../docs/TERMINOLOGY_RPB108_ARCHIMEDEAN_CUTOFF.md). Exact coefficients are in ARCH_CUTOFF32_WITNESSES; the rational interval certificate uses no floating arithmetic.

## 1. Physical vectors and exact arithmetic

At each aperture divide [-a,a] into 128 cells of width d=2a/128. The vector is the real step function h=w_i on cell i, with every w_i an integer divided by 10^6. The saved integers are the definition of h. Its physical mass is d sum_i w_i^2. Values are exactly odd at a=1 and exactly even at a=21/20. Discovery used floating finite restrictions; the certificate independently recomputes the physical form on the resulting RATIONAL functions.

Every such step function belongs to the canonical logarithmic domain: its zero extension has finitely many jumps and Fourier decay O(1/|xi|). Therefore the original complete source identity and the aperture-one certificate apply to the first vector. No H0^1 assumption is made.

Let b_k=sum_{i=0}^{127-k}w_i w_(i+k) be the **cell correlation coefficients**. For a positive shift s/d=m+f, 0<=f<1,

    C_h(s)=d[(1-f)b_m+f b_(m+1)].

The logarithm intervals prove the integer m without crossing a cell boundary. For each active prime power n the original contribution is -2 Lambda(n)/sqrt(n) C_h(log n). At a=1 the dictionary is 2,3,4,5,7; at 21/20 it also contains 8. Lambda(4)=Lambda(8)=log(2), both orientations are retained, and 9 is inactive. No source prefix or smearing is used.

For q_j=j+1/4, alpha=2q_j and t=exp(-alpha d), the matrix of K_j in the normalized cell-indicator basis has Toeplitz row

    k_0=2/alpha-2(1-t)/(alpha^2 d),
    k_r=(1-t)^2 t^(r-1)/(alpha^2 d), r>=1.

Thus its exact physical quadratic form is

    <K_j h,h>=d[k_0 b_0+2sum_{r>=1}k_r b_r].

The archimedean cutoff is L_32 mass minus the sum of these 32 forms. The ORIGINAL pole is computed independently from

    M_plus=sum_i 2w_i[exp(right_i/2)-exp(left_i/2)],
    M_minus=sum_i 2w_i[exp(-left_i/2)-exp(-right_i/2)],
    Q_pole=2 M_plus M_minus.

This is exactly 2|cosh><cosh|-2|sinh><sinh| on real vectors, not a PSD replacement. The odd witness has only the negative slot; the even witness has only the positive slot. The latter therefore rejects an explanation that all cutoff failure comes from dropping the positive pole.

## 2. Exact outward certificate

The certificate uses rational interval operations with outward rounding to a 10^-40 grid. Logarithms use the positive atanh series and a proved geometric tail. Square roots use integer squares. Exponentials use the positive Taylor series with geometric tail, and reciprocals for negative arguments. Arguments here have absolute value at most two. Pi uses the alternating Machin series. The exact digamma constant is

    m00=-gamma-pi/2-3log(2)-log(pi).

Euler's constant is enclosed by H_4096-log(4096)-1/4096 <=gamma<=H_4096-log(4096). The elementary harmonic/integral bounds suffice for the negative margins; no uncertified decimal gamma value is imported. Every rational rounding and series allowance remains in the final form interval.

The saved complete certificates prove:

| Aperture | Parity | Exact physical mass | Strict cutoff Rayleigh upper bound |
| --- | --- | --- | --- |
| 1 | odd | 31999998475473/32000000000000 | Q_32/mass < -49/1000 |
| 21/20 | even | 128000018228103/128000000000000 | Q_32/mass < -59/1000 |

The full rational form enclosures are stored in ARCH_CUTOFF32_VALIDATION. These are actual physical cutoff signs, not floating eigenvalues interpreted as operator eigenvalues. Since Q_N increases in N, neither window can have a whole-space positive cutoff for any N<=32.

## 3. The exact compact gain exceeds one, despite a positive background

Use the existing JOINT original prime bounds 77937/40000 at a=1 and 1063939/500000 at 21/20. The constant enclosure and exact harmonic sum recheck L_32-B>157/1000 at both windows. Thus the NF63 background F_32 is genuinely positive, and its compact gain g_32 is lawful.

The same interval calculation gives L_32<5/2, B<11/5, sinh(a)<13/10 and

    ||F_32||<=L_32+B+2(a+sinh(a))<10.

For each saved witness, D_32=F_32-Q_32 gives

    <D_32 h,h>/<F_32 h,h>
       =1-Q_32(h)/<F_32 h,h> >1+target/10.

This quotient is a lower test for the normalized compact operator, through the vector F_32^(1/2)h. Consequently

    g_32(1)>10049/10000,
    g_32(21/20)>10059/10000.

The full compact criterion therefore FAILS, not merely its presently missing upper certificate. This does not bound the ORIGINAL source gain from below by one: g_32 belongs to a lower comparison form with omitted positive archimedean energy.

## 4. Genuine original-positive control and source identity

The recovered aperture-one certificate proves on the whole canonical domain

    Q_original(h)>=4*10^-32 ||h||_2^2,
    Q_original(h)>=2*10^-34 E_log(h).

In particular the saved odd witness has strictly POSITIVE original energy. Yet Q_32(h)<-49/1000 mass. Its omitted positive archimedean tail satisfies

    Q_original(h)-Q_32(h)
       >[49/1000+4*10^-32] mass.

Hence that tail is materially needed even at the certified anchor. The original complete identity Q_original=||P_a h||^2-||N_a h||^2 is retained; Q_32 is not assigned an actual-divisor source dictionary. The existing original source gain stays strictly below one at a=1 while the cutoff compact gain is strictly above one. This is a genuine ORIGINAL positive control, not an artificial shifted operator.

At 21/20 no original sign is claimed for its even witness. A negative lower comparison value cannot prove a negative original value. All original eigenlevel mass shifts remain explicit; subtracting a positive mu would lower each cutoff by mu mass, rather than turning this calculation into original nullity.

## 5. Resolution warning and next target

A floating resolution probe showed positive 128-cell finite restrictions for some larger cutoffs, while finer restrictions found negative trial directions. These observations are discovery diagnostics only, not sign certificates. They are consistent with the variational fact that a fixed finite restriction gives an UPPER test for the whole lowest level. Recompute and rigorously enclose a candidate vector before using any such negative observation; a positive finite restriction requires a complete complement certificate.

Stop N=32 as a positivity candidate at these windows. Do not retire NF63's whole ordered framework: its convergence proof guarantees an eventually positive cutoff at every strictly positive ORIGINAL window, including a=1, but gives no practical cutoff size from the unknown true gap. The anchor's tiny conservative lower margin is not an estimate of the true eigenvalue or a necessary complexity bound.

Any next compact-gain upper test must use a larger N and a proved whole-space remainder. Increasing only the cell count cannot repair a genuinely negative Q_32. Increasing only N and displaying a positive finite matrix cannot settle the whole-space gain either. No paused aperture experiment, old 112-vector Schur data or coupled continuation cursor is modified.

This NF supplies two rigorously negative ORIGINAL-arithmetic cutoff witnesses and two strict cutoff-gain lower bounds, with an original-positive anchor control. It supplies no new original gain bound, aperture extension, first-contact exclusion, RH, F4, full transport or Lean result. Reproduce with python scripts/certify_native_arch_cutoff32_witnesses.py. Exact source pins, witness file hash and result custody accompany the publication; the original anchor certificate is reused, not recomputed or relabeled.
