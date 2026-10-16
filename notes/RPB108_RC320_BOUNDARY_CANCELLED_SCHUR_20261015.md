# RC320 — Endpoint-cancelled original signed P0/P2 high response and the first positive 2×2 Schur block

**Source:** original CC27 Weil form, identified as the bounded completed D-Riesz representative by RC313.  
**Parent:** merged RC319 at `b9441943e1e289453290c9ce46d75fd4e62ca405`.  
**Rank:** buffered 317-reference, with 122 even low modes and 195 odd low modes. The high complement is positive by inherited RC283/314.  
**Standing:** certificate establishes the **full high-eliminated Schur quadratic form on the two-dimensional span of P0 and P2**, *conditional on the inherited original-operator identification*. The other 120 even and 195 odd low coordinates and Stage I/F4/Lean/RH remain OPEN.

## Why the prior P2 estimate failed

RC319 showed a strictly positive original **low** P0/P2 2×2 block, but the P2 high source alone was too large for the global coercivity estimate. Its conservative Schur diagonal lower bound was negative (inconclusive). Directly bounding P0 and P2 as unrelated columns loses the decisive cancellation between their prime translation sources and their endpoint contributions.

The useful low basis is not (v0,v2), but (v0,w) with

$$
u_n(x)=\sqrt{\frac{2n+1}{2B}}P_n(x/B),\quad
D_n=H_n+s,\quad v_n=\frac{u_n}{\sqrt{D_n}},\quad B=11/10,
$$

$$
\alpha=\sqrt{\frac{5s}{s+3/2}},\qquad
w=v_2-\alpha v_0
=\frac{u_2-\sqrt5u_0}{\sqrt{s+3/2}}.
$$

This is an **invertible change of the two-dimensional low basis**; it does not remove or weaken the P0/P2 Schur positivity obligation.

Crucially, on the physical support,

$$
u_2-\sqrt5\,u_0=
\sqrt{\frac5{2B}}\,[P_2(x/B)-P_0(x/B)]
=\frac32\sqrt{\frac5{2B}}\left((x/B)^2-1\right).
$$

**It vanishes at both support endpoints.** Zero-extension therefore belongs to the first Sobolev space $H^1(\mathbb R)$ and creates **no support jumps** under translation.

## Fully paid original signed prime source

The seven prime powers contribute 14 zero-extended signed translations. For the polynomial P2−P0, the direct prime source is a continuous piecewise quadratic profile with 15 support segments. The new validator builds those 15 segments from the original RC313 signed formulas and computes their **complete** rational-center physical L2 norm by exact polynomial integration, retaining all overlap interference.

Its even Legendre coefficient, scaled as in RC318/319, is the **signed cancellation**

$$
A_n^{(w)}=A_n^{(2)}-A_n^{(0)},\quad n=0,2,\dots,510.
$$

All 256 values are reconstructed independently through the rational Legendre recurrence and compared with the all-segment Parseval norm. Thus

$$
E_{512+}^{\mathrm{prime,center}}
=\|K_{\mathrm{prime}}(u_2-\sqrt5u_0)\|_{2,\mathrm{center}}^2
-\sum_{\substack{0\le n<512\\ n\ \mathrm{even}}}
\frac{5|A_n^{(w)}|^2}{2n+1}
\ge0.
$$

Uncertain original $\log m$ and $\Lambda(m)/\sqrt m$ intervals are paid in the **entire physical source**. Unlike the P2-only case, the *actual* translation modulus here is bounded linearly in displacement:

$$
\|T_{\ell+\delta}f-T_{\ell}f\|_{L^2}
\le|\delta|\,\|f'\|_2,\qquad
\|f'\|_2=\frac{\sqrt{15}}B<\frac4B.
$$

The absence of the $O(\sqrt{|\delta|})$ boundary jump is a **structural cancellation**, not a numerical accident.

## Exact cancellation of the endpoint's dominant tail

The full RC311/312 logarithmic endpoint contribution from P2 minus P0 has an exact symbolic form for even $n\ge244$:

$$
E_{n2}-E_{n0}
=\frac{6(2n+1)}{n(n+1)(n-2)(n+3)}.
$$

Therefore the individual $O(1/n)$ endpoint tails cancel; the combined endpoint coefficients are $O(n^{-3})$. Its entire physical $n\ge512$ output is paid by the RC318 telescoping $P0$ endpoint norm and the factor $6/[(512-2)(512+3)]$.

RC46's 192-degree analytic regular-kernel polynomial acting on the quadratic source yields degree at most 195, so all projections onto the even high complement $n\ge244$ vanish exactly; only the inherited $L^\infty$ kernel remainder remains. The even signed-pole high tail has a separate uniformly paid Taylor/geometric upper bound.

The finite even high responses $n=244,246,\ldots,510$ are computed as the **actual combined signed** $(A_n^{(2)}-A_n^{(0)}+E_{n2}-E_{n0})$ before squaring. The complete $n\ge512$ high tail, source arithmetic, regular kernel and pole are all included in the final $D$-energy norm upper bound on $Tw$.

## Convert two scalar source estimates to a rigorous 2×2 Schur test

For the original even signed operator,

$$
N_0=\begin{pmatrix}B_{\mathrm{low}}&T^*\\ T&C\end{pmatrix},\quad
C\succeq\mu_e I,\qquad
S=B_{\mathrm{low}}-T^*C^{-1}T.
$$

RC318 already certifies a **strict positive** $S_{00}=\langle v_0,Sv_0\rangle$ lower bound. RC320 uses the exact native original low P0/P2 Gram from RC315/319 and the new full $Tw$ upper to prove:

$$
S_{ww}\ge \langle w,B_{\mathrm{low}}w\rangle
-\frac{\|Tw\|_D^2}{\mu_e}>0,
$$

$$
|S_{0w}|\le
|\langle v_0,B_{\mathrm{low}}w\rangle|
+\frac{\|Tv_0\|_D\,\|Tw\|_D}{\mu_e}.
$$

Finally, **all rational outward enclosures** must satisfy

$$
\boxed{S_{00}^{\rm lower}S_{ww}^{\rm lower}
-(|S_{0w}|^{\rm upper})^2>0}.
$$

The result certifies a positive full high-eliminated 2×2 Schur block **in the original signed operator**, not just the original low principal block. The original operator's positive high complement already includes **all infinite high modes**.

The exact-rational certificate gives the following conservative, outward-rounded numerical measurements for the transformed low basis:

| Quantity | Certified bound |
|---|---:|
| Physical prime source tail beyond degree 510, squared | < $3.961883\times10^{-8}$ |
| Complete high $D$ response norm $\|Tw\|_D$ | < $9.496304\times10^{-5}$ |
| Complete high $D$ response energy $\|Tw\|_D^2$ | < $9.017978\times10^{-9}$ |
| Full signed Schur $S_{00}$ | > $9.150876\times10^{-4}$ |
| Full signed Schur $S_{ww}$ | > $7.274724\times10^{-4}$ |
| Full signed Schur $\lvert S_{0w}\rvert$ | < $4.238605\times10^{-4}$ |
| **Full signed 2×2 Schur determinant** | **> $4.860433\times10^{-7}$** |

These bounds establish strict positive definiteness on the **whole two-dimensional $P_0/P_2$ low subspace after the entire infinite high complement has been eliminated**, under the pinned CC27/RC313 operator identification. All seven exact-rational input certificate blobs are pinned or independently checked as applicable. The determinant margin is a certificate margin, not an approximation to the actual determinant.

## Scope, reproducibility, and next cursor

The two-dimensional Schur block is only a subspace of the buffered rank-317 low reference. **Positivity on a principal subspace does not establish full even or odd positivity**. No inverse for all 317 low sources, full operator lower spectral bound, Stage I, Lean, F4 or RH follows.

**RC321:** extend boundary-cancelled high-source combinations to P4, P6, and higher even degrees, retaining all signed cross-covariance in a growing Loewner-positive Schur block. The remaining 120 even and 195 odd low coordinates need independent certification.

Exact regeneration and reverse order replay:

```bash
python scripts/validate_rpb108_rc320_boundary_cancelled_schur.py --output certificates/rpb108_rc320_boundary_cancelled_schur.json
python scripts/validate_rpb108_rc320_boundary_cancelled_schur.py --output certificates/rpb108_rc320_boundary_cancelled_schur.json --replay
```
