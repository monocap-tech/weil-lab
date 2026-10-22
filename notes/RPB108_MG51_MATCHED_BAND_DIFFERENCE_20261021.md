# MG51 — Original full 24D matched MG48-to-MG50 band substitution audit

**Status: calculation and separate exact rational independent replay PROPOSED, no numerical conclusions accepted until Actions passes.** Parent MG50's new original 32-cell true Fourier measurement and complete-source original 864 exact matrices were independently accepted in [Actions #39727680095](https://github.com/monocap-tech/weil-lab/actions/runs/39727680095), but all four MG50 Gersh sufficient margins were worse than MG48 and MG43. The source frequency measurement was new and rigorous; the *bound* worsened on that specific sufficient criterion.

## Necessary matched-response experiment

MG48 estimates the original complete residual `U48=U_[0,4]+U_(|xi|>4)`.
MG50 estimates `U50=U_[0,4]+U_[4,8]+U_(|xi|>8)`.
Both are valid physical 24D Loewner uppers, preserving the original
23-adapted plus true sinh-pole channel, full seven-prime/digamma
multiplier and all original real frequencies.

Comparing MG48's BEST parameters to MG50's separately selected BEST
parameters confounds a change of measurement with a change of
Young allocations. MG51 therefore tests TWO matched grids per original
mesh/cutoff case: evaluate MG48-best parameters identically in both
methods, and evaluate MG50-best parameters identically in both methods.
This gives eight full 24D original exact rational matrix comparisons.

## Exact signed seven-term difference identity

For a fixed common genuine original B, kappa, M, eta, gamma, pole
profile, define `C0=I+2e_p b0^T B`,
`P0=C0-(kappa+M)B/2`. Let
`HLlo<=H_[4,8]<=HLup`,
`GLlo<=G_[4,8]<=GLup` be MG50's NEW certified physical band
moments, with `GLmid=(GLlo+GLup)/2` and
`E_L=(GLup-GLlo)/2>=0`. Then the exact difference of the two
otherwise-identical valid **COMPLETE** residual UPPER matrices is

```
U50-U48 =
   + U_direct_[4,8]
   - (1+gamma) C0^T HLlo C0
   + (1+gamma) kappa*M B^T HLup B
   + (1+gamma) [P0^T GLmid B + B^T GLmid P0]
   + (1+gamma) eta P0^T E_L P0
   + (1+gamma) eta^-1 B^T E_L B
   - (1+gamma^-1) HLlo_pp Wbase.
```

Here `Wbase` is the original PSD error profile normalized so the
pole fee on any omitted physical source mass bound `Hdup` is
`Hdup_pp Wbase`. MG48 and MG50 have identical original MG24
strong-tail `tau_2` term; it cancels in this **comparison**, but
is never removed from either actual complete residual certificate.

The two new G interval width charges are **PSD increases**, since
the MG50 whole-minus-measured G bounds use independent source
interval subtraction. The two signed mass terms, signed G center
and pole fee change need not be PSD. The NET difference is **not
presumed to have any Loewner sign**. Exactly seven matrices MUST sum
entrywise to the actual new minus old full24 upper for each of eight
matched response trials.

Check all arithmetic on the archived exact rational MG43 negative
conservative-source certificate vectors, and produce actual rational
positive and negative Rayleigh witnesses for the matrix difference
when available. A positive/negative difference witness is NOT a
physical original Weil operator eigenmode.

The independent script reconstructs each full original 24D UPPER using
the UNGROUPED original H/G multiplier polynomial, rechecks exact
entries for all seven signed delta matrices, original MG48/MG50
archived winners, and exact rational source rays. There is no new
Fourier integration here, nor new residual source certificate.

**Next frontier:** if new band interval subtraction is the dominant
penalty, use SAME-CELL local H/G/S covariance of the original
multiplier/source residual before separately reconstructing
independent whole-minus-measured envelopes. Do not merely increase
new-frequency grid size. The required acceptance is still a new
simultaneous original 24x24 complete-frequency Loewner UPPER and
exact positive 24D source lower; even that would leave original 470D
inverse, signed odd 51/56, independent Fourier/form/domain and
even/Weil/CC27/RH OPEN.
