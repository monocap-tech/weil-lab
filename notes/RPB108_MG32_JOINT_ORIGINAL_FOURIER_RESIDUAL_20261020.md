# MG32 — Direct joint original Fourier source residual covariance

October 20, 2026. Stacked on [MG31 #280](https://github.com/monocap-tech/weil-lab/pull/280). The accepted MG31 full family exact rational Rayleigh audit found a NEGATIVE direction of EACH of MG30's 36 **conservative** original 24D source residual LOWER CERTIFICATE matrices. That is a method failure, **not** a spectral negative direction for the true source residual or signed Weil operator. Coordinate changes cannot repair those particular 36 bound matrices; MG32 retains correlations discarded before forming a square.

## Exact source identity including true pole

Original supported 23 MG11 endpoint-adapted source functions plus the actual odd sinh pole make a 24-channel source map `F`. The physical SI10 Gram reconstructs `b=F*s`, with each true b_i contained in exact rational interval `b0_i ± eb_i`. For the true odd multiplier Ao with signed digamma + seven-prime terms, `Astar=Ao-2|s><s|` and any exact rational 24×24 response B,

```
 R=F-Astar F B,
 r(xi)=t(xi)[I-a_o(xi)B+2 e_p b^T B],
```

where t(xi) is the ENTIRE true original 23+pole Fourier vector and e_p selects the genuine pole channel. The source-residual covariance `R*R` is the integral of `r(xi)^T r(xi)`. This is **the same original source operator** as MG30/MG31; no invented Galerkin model.

## Direct joint residual on 32-cell contiguous [0,4] prefix

Reconstruct the accepted original MG29 source value v, slope d, and whole-cell Taylor source radii e on exactly 32 rational contiguous positive-frequency cells covering [0,4], both frequency signs. Source derivative/third/fourth errors are proved by the original MG29 procedure; check exact *sum of the 32-cell MG29 source radii* against separately accepted Actions #39440914565.

Each cell has actual original signed prime7/digamma positive multiplier interval [l,u], midpoint a0=(l+u)/2 and halfwidth da=(u-l)/2. Let `C0=I-a0 B+2e_p b0^T B`. For each residual source/output j,

```
 q0_j=sum_i v_i C0_ij,
 q1_j=sum_i d_i C0_ij,
 |r_j(xi)-q0_j-q1_j(xi-mid)|
    <= sum_i |C0_ij| e_i
       + da sum_i |B_ij| (|v_i|+h|d_i|+e_i)
       + 2 (|v_p|+h|d_p|+e_p)sum_i eb_i |B_ij|.
```

This is an exact all-cell original-source enclosure INCLUDING multiplier, the original physical pole and its b uncertainty INSIDE the residual before squaring. For each cell choose a rational sourcewise Young tau by minimizing the DIRECT residual upper trace. The familiar MG15 exact anisotropic PSD Young inequality then produces a complete coupled 24×24 **upper** for the original joint Fourier residual over the [0,4] prefix. This avoids separately paying errors to H_C,G_C,S_C and combining wide intervals after the fact.

## Entire original frequency tail — explicitly closed, not silently discarded

The prefix does not cover all real frequencies. Let `H_R=H-H_C`; the original physical Hup and directly replayed MG29 prefix HClo prove `0<=H_R<=Hup-HClo` in Loewner order. For cutoff Lambda=2^k, k=12/16, original global positive multiplier majorant `M_k=17+k(347/500)` and the pinned original SM41 **positive strong high-source tail** `tau2(k)` prove

```
 S_R = int_{outside prefix} a_o² t^T t
     <= M_k²(Hup-HClo)+tau2(k)I.
```

On the omitted frequencies write r=(t C)-(a_o t B), with `C=I+2e_p b^T B`. Exact two-component Young bounds imply for any beta>0

```
 r^T r <=(1+beta) (t C)^T(t C)
          +(1+1/beta)(a_o t B)^T(a_o t B).
```

To pay uncertainty in the true original b, use C0 from b0 and nested gamma Young. The error ΔC=2 e_p (b-b0)^T B satisfies

```
 ΔC^T H_R ΔC <=4 (Hup-HClo)_pp
      sum_j (sum_i eb_i |B_ij|)^2 I.
```

The formula yields an explicit complete-original-frequency 24×24 upper Rupper = Rprefix_upper + Rremaining_upper. At each cutoff, test the same **accepted MG30 scalar and best nonscalar rational B** against strict Gershgorin of `Hlo-Rupper`. This is a rigorous sufficient original 24D one-step criterion; no claim of sharpness in the omitted-frequency Young complement.

## Acceptance and limitations

MG32 must pass calculation-bearing Actions and separate exact rational no-promotion checks; report measured prefix direct residual trace, complement trace, complete residual trace, and strict original source residual margin. Even a smaller prefix upper does NOT automatically mean the total bound is useful; record whether the omitted-frequency envelope dominates. The 24D source space is not known invariant for the original operator, so even a passing source test is **not** an all-470 inverse or signed 51/56 negative cap. Original Fourier/form-domain identification and complete odd/even/Weil/CC27/RH remain OPEN.

If MG32’s full-frequency residual still fails, advance by sharper *joint omitted-frequency* treatment (e.g. actual MG24 disjoint nonflat panels plus MG29 prefix, or broad adaptive lowband), not by attempting another congruence on MG31’s proven-negative conservative matrices.

**CI pending.**
