# MG39 — Original-source uniform scalar feasibility across full-frequency moments

October 20, 2026. Stacked on [MG38 #287](https://github.com/monocap-tech/weil-lab/pull/287). The MG38 original-source Actions #39508270844 and its final-head #39508452145 passed: the complete original MG30 scalar source residual bound is Loewner-tighter than the MG36 direct-band upper, but all tested accepted scalar/nonscalar source contraction criteria remain nonpositive. MG37 exact original data also ruled out merely tuning Young parameters in the frozen remainder method.

## New analytical obligation — entire scalar family, not sampled t

The true 24-channel source basis is **the actual SI10 physical 25 generator system, projected through MG11's 23 adapted dual-boundary source functions plus the genuine sinh pole**, with original seven-prime/digamma Fourier multiplier and complete real frequencies, high tails and pole corrections.

For any positive scalar response `B=tI` with t>=0, independently accepted original source moments prove

```
R*R <= Hup -2t LG +t² US,
A(t)=Hlo-[Hup-2t LG+t² US].
```

MG24 and MG29 provide **two distinct** complete-original-frequency valid Loewner lower matrices LG and upper matrices US on exactly the same physical source space. Rather than choosing one matrix or entrywise max/min, for rational or real `lambda in [0,1]` the pairs

```
LG(lambda)=(1-lambda)LG24+lambda LG29,
US(lambda)=(1-lambda)US24+lambda US29
```

remain Loewner-valid as convex combinations. This never invents a matrix 'Loewner join' or an invalid entrywise intersection.

For a nonzero **exact rational source direction** v, the matrix sufficient positivity expression reduces to an exact scalar quadratic

```
q_v(t,lambda) =
 -d + 2t b(lambda) -t² c(lambda),
 d=2Herr||v||²>0,
 b(lambda)=v^T LG(lambda) v,
 c(lambda)=v^T US(lambda) v>=0.
```

If b<=0, the maximum over t>=0 equals -d. If b>0 and c>0, the maximum is `-d+b²/c`, at t=b/c. If c=0 and b>0, the direction cannot certify a uniform strict negative bound. MG39 checks the sign with exact Fraction and never infers it from a floating eigenvalue.

**Continuum λ proof:** For any fixed v and t, q_v is affine in lambda. Hence if the exact supremum in t>=0 is strictly negative at both endpoints of an interval of lambda, the same fixed v gives `q_v(t,lambda)<0` for **every t>=0 and every lambda inside**. Separate rational witnesses can cover a finite interval partition of the ENTIRE continuum [0,1]; if each interval is witnessed, this certifies a genuine **no-go for all scalar t and all convex MG24/MG29 Loewner-moment mixes** on that original cutoff/mesh. The direction may differ by interval; a single global v is not required.

MG39 proposes candidate source directions using exact coordinate/paired source vectors and rationalized approximate eigenvectors (numerical eigensolvers are never used to decide a sign). Start with 16 equal lambda subintervals, then 64 if necessary. If any remain without a rational uniform witness, report INCONCLUSIVE for those intervals and do **not** claim continuum-wide exclusion.

## Independent original acceptance

Pinned data-bearing GitHub Actions: MG24 #39378465438, MG29 #39440914565, MG30 #39442984941; original k12/k16 and MG29 16/32-cell already proven complete-frequency source brackets. Verify original MG30 scalar t exact Gershgorin certificate matches independently, all source mixed pole corrections retained, and independently replay EVERY claimed rational directional b,c,d and strict endpoint inequality from original stored moment matrices.

**Passing a uniform-direction negativity test means only that the chosen original conservative source residual *certificate matrix* cannot be positive for any scalar response t in this particular moment-convex family. It does NOT prove the real signed operator or actual residual has any negative direction, does not exclude nonscalar B or improved correlated moments, does not classify the 470-source strong inverse or the signed 51/56 negative cap, and has no implication settling RH.**

If scalar uniformly excluded, the next frontier should improve *correlations in the actual original first/second source moment enclosure*, or construct independently certified nonscalar response witnesses, rather than repeat scalar sampling or direct-band Young refinements.

**MG39 CI: PENDING.**
