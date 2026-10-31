# EF23 — Exact original signed arithmetic mixed sparsification: only n=2,5,7 survive

**2026-10-31. Canonical W-EVEN-FORM OPEN.** Parent [EF22 draft PR #403](https://github.com/monocap-tech/weil-lab/pull/403), final source and manifest [Actions #41221940116](https://github.com/monocap-tech/weil-lab/actions/runs/41221940116) SUCCESS. Original arithmetic energy identity q_prime(f,f)=0 certified by 13,139 exact prime translation nonoverlaps, and exact source cutoff decomposition shows only two partial original n2 bells, whose signed mixed contribution lies in (1.535080666e-6,1.535339746e-6). Full signed M and arch E upper remain OPEN.

## Exact additional original operator reduction — four prime-power mixed channels vanish

Use the **unchanged** original source e(x)=1_{[-B,B]}(x)cos(2pi c0 x), c0=37/64, B=11/10, and unchanged original EF21/EF22 true even F469 test f=F_h psi, h=1/2048, r=1/65536, a=B-ln2+469h. The actual 1,878 bell centers are s*a-k*h, s=±1, k=-469,...,469. For sigma=+ the genuine source shift e(x+ln n) is present in the original physical test support precisely when x < t_n=B-ln n; the opposite endpoint lies outside every f bell for the full original n-set. Sigma=- is its exact parity mirror.

An exact original SI06 Fraction logarithm interval source verifier classifies ALL 13,146 (n,s,k) bell/cutoff interactions. The complete table for sigma=+ is:

| Original n | Negative-center bells fully inside | Positive-center bells fully inside | Partial bells |
| --- | ---: | ---: | ---: |
| 2 | 939 | 0 | 1 extreme k=+469 |
| 3 | 939 | 0 | 0 |
| 4 | 939 | 0 | 0 |
| 5 | 728 (k=-258..469) | 0 | 0 |
| 7 | 39 (k=431..469) | 0 | 0 |
| 8 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 |

For n=3,4, the entire negative-center FIR lattice lies inside the untruncated original source shift, and the entire positive-center lattice is outside. The exact source-frequency root S_h(c0)=0 (because c0 is literally the first native original 107-cluster center, with p0>=1) kills the whole included lattice's cosine sum: **q_prime,3(e,f)=q_prime,4(e,f)=0 EXACTLY**. For n=8,9 neither lattice enters the source shifted support, so **q_prime,8(e,f)=q_prime,9(e,f)=0 EXACTLY**. This is actual original operator support+frequency cancellation, not replacement by a cap or dropping four difficult terms.

The n=2 half bell is already a genuine numerical original signed source contribution >1.5e-6 (native parent CI accepted).

## Two remaining signed original arithmetic channels — finite edge coefficients

For each authentic original n and retained (whole) negative-center bell, the true physical cosine-six integral is

H_r(c0) cos[omega*(ln n - a - k*h)], omega=2*pi*c0,

with exact original H_r(c0)>0 (from EF21's cancellation-free Fourier identity). Write FIR Laurent coefficients A_k=A_-k real and exact; S_h(c0)=sum_{k=-469}^{469} A_k exp(-i*omega*k*h)=0. The sigma=+ and parity-mirrored sigma=- contributions combine into

q_prime,n(e,f)=-w_n H_r(c0) Re{exp[i*omega*(ln n-a)] sum_{k in K_n} A_k exp(-i*omega*k*h)},

where w_n is the genuine original n-th prime-power weight, and K_n is the **exact included** coefficient set from the table. This formula is for **unclipped** n=5,7 only; n2 requires the inherited genuine half-bell formula.

For n=5, the naive exact sum has 728 coefficients k=-258,...,469. The original source root S_h(c0)=0 gives the exact alternate evaluation

sum_{k=-258}^{469} A_k exp(-i*omega*k*h)
  = -sum_{k=-469}^{-259} A_k exp(-i*omega*k*h).

Thus the n=5 signed mixed contribution is a **211-term edge sum**, not a 728-term cancellation. For n=7 it is directly a **39-term edge sum** k=431,...,469. ## A second exact compression: compute ONLY 211 source-edge coefficients

No signs of the two remaining sums are asserted without original outward high-precision trigonometric and coefficient interval arithmetic. The counts 211 and 39 are an *information/computational reduction*, not yet a numerical certificate.

Moreover, we can obtain ALL necessary edge coefficients without constructing or convolving the entire 939-coefficient Laurent filter. Put theta_j=2*pi*h*c_j, u_j=cos(theta_j), and set

  G(t)=prod_(j=1)^107 (1-2*u_j*t+t²)^p_j = sum_(l=0)^938 a_l*t^l.

Since z^469*S_h(z)=G(z) and G is self-reciprocal, the extreme FIR coefficients satisfy

  A_{-469+l}=A_{469-l}=a_l.

Write s_m=sum_j p_j*cos(m*theta_j), an original source-specific Chebyshev moment (cos(m*theta_j)=T_m(u_j)). Taking the logarithmic derivative of G gives the **exact Newton-Chebyshev recurrence**

  a_0=1,
  l*a_l = -2*sum_(m=1)^l s_m*a_(l-m),   l>=1.

Thus both surviving arithmetic edge calculations require **only a0,...,a210**, a 211-entry prefix and 211 authentic source moments. The n=7 term requires only a0,...,a38. No 939-wide convolution, 469-by-469 Gram, or infinite complement inverse is needed for these two finite original arithmetic contributions. The source code proves this formal algebra via an exact Fraction rational-Chebyshev toy regression and verifies the actual original SI10 centers/order counts; the toy coefficients are NEVER substituted for original numerical evidence.

These are precisely the two signed finite sums, with omega=2*pi*c0:

  M5 = +w5*H_r(c0)*Re[exp(i*omega*(ln5-a+469h))*
            sum_(l=0)^210 a_l exp(-i*omega*l*h)],

  M7 = -w7*H_r(c0)*Re[exp(i*omega*(ln7-a-469h))*
            sum_(l=0)^38 a_l exp(+i*omega*l*h)].

The first source phase simplifies to ln5-a+469h=ln10-B, since a=B-ln2+469h. Every term retains the original seven-prime/power weight convention and original source phase.

**Conditioning qualification:** because G is the product of 938 complex unit-circle root factors, the loose envelope |a_l|<=binomial(938,l) permits |a210| up to over 10^215 and |a38| over 10^67. Those are merely **worst-case absolute upper bounds**, not measured native coefficient magnitudes; they demonstrate why naive interval coefficient propagation or a low-precision signed sum cannot be certified. EF24 must implement rigorously scaled trig moment/recurrence intervals and count cancellation losses before claiming a signed M5/M7 interval.



**Original arithmetic identity now:**

  M_prime=q_prime(e,f)=M_2+M_5+M_7,

  M_3=M_4=M_8=M_9=0 EXACTLY,

while q_prime(f,f)=0 EXACTLY from EF22. Thus the full original pole-free signed Schur test is now

  M=q_arch(e,f)+M_2+M_5+M_7,
  E=q_arch(f,f).

## Correct next gate, no theorem promotion

**EF24 acceptance:** Certify an honest source-pinned outward interval for the two edge-coefficient/trig sums M_5 and M_7 using the 211-step exact Chebyshev-Newton recurrence, stable signed high precision and error budgets; measure the ORIGINAL arch mixed and arch energy upper with a common normalization, or give a proved conditioning/precision METHOD STOP. Potential method: interval polynomial recurrence for A_k with explicit sign and cosine error; adapt to edge coefficients k>=259 and k>=431; avoid evaluating the whole 469-by-469 Gram or another thin jump localization. The point-source n2 certificate alone must NOT be treated as the whole M sign.

All original source physical/form-domain analytic review obligations remain OPEN; complete signed even 469D Schur PSD, paused odd, whole Weil and RH OPEN. Additive draft custody; no merge.
