# MG49 — Exact original complete-source joint covariance loss audit

**Status:** Implementation committed. No MG49 results accepted until independent Actions CI passes.

## Motivation and inherited verified result

MG48 passed original full24 exact rational 864-matrix construction and a distinct
independent replay in [Actions #39685179933](https://github.com/monocap-tech/weil-lab/actions/runs/39685179933).
Its new valid original joint multiplier moment bound

```
S_D <= (kappa+M_k) G_D - kappa*M_k H_D + tau2_k I
```

yielded signed sufficient Gersh margins -23.9349003598, -24.5654207178,
-23.3104401617, -24.0860150298 for original 16/k12, 16/k16, 32/k12,
32/k16. Each is worse than the independently validated MG43 whole-source
margin -1.3146427911, -1.4906207885, -1.1941733535, -1.3130469460.
Thus MG43 remains selected; no original 24D contraction.

## What this audit actually computes

MG49 is a *certificate accounting diagnostic* on EXACT original SI10/MG11
23-adapted + true-sinh-pole 24D source, complete archimedean/digamma
seven-prime Fourier multiplier, all frequencies. For each original
mesh/cutoff, take MG48's best **valid** full24 residual upper
`U48=U_measured+U_omitted`, and independently reconstruct its eight exact
rational summands:

```
U_measured
(1+gamma) C0^T H_D,upper C0
-(1+gamma) kappa*M_k B^T H_D,lower B
(1+gamma) tau2_k B^T B
-(1+gamma)(P0^T Gc B+B^T Gc P0)
(1+gamma) eta P0^T E_G P0
(1+gamma) eta^-1 B^T E_G B
(1+gamma^-1) W_pole
```

Here P0=C0-(kappa+M_k)B/2, Gc=(L_G+U_G)/2 and
E_G=(U_G-L_G)/2>=0. This is **not an approximation** to the
accepted MG48 matrix: their sum must equal every exact rational entry of
MG48's archived new best complete-source upper. A separately written
independent verifier checks the same equality against its own
ungrouped polynomial derivation and exact arithmetic.

For every original mesh/cutoff, import the **existing exact rational
negative witness of the accepted conservative MG43 source lower**,
not a hypothetical spectral eigenvector of the original operator.
Evaluate the individual signed source-ray charges, the full MG48 vs
MG43 ray difference, and how large a reduction of the MG48 residual
upper is at least required to make *that particular ray* nonnegative.

Positive-fee ranks are only accounts of this particular valid
certificate in the chosen coordinate basis and selected B. The
counterfactual removal of the two mixed-moment Young fees, the pole
uncertainty or the high-frequency tail is recorded **only** to diagnose
relative accounting pressure. The removed-fee expressions are
**NOT Loewner upper bounds** and are **NOT physical counterexamples
or valid contraction certificates**.

## Subsequent frontier

Once the exact ray accounting is independently accepted, prioritize
new **genuine physical locally correlated** source/multiplier
information on the omitted finite frequency region where the tested
certificate actually loses its margin. A source-ray improvement is not
automatically a simultaneous 24D improvement; independent full-source
matrix Loewner acceptance remains compulsory. Do not mechanically
iterate MG47 moment subtraction or MG48 global moment interpolation.

Even an eventual original 24D source contraction would not establish
original 470D inverse, signed 51/56, independent Fourier/form/domain,
even/Weil/CC27 or RH. All remain OPEN.
