import Mathlib.Data.Rat.Defs
import Mathlib.Data.List.Basic
import Mathlib.Tactic

namespace WeilDefect
/-!
NF545: FROZEN exact source signature of the original NF407/NF505
242 generator nodes, independently checked against the immutable
NF407 JSON by scripts/local_replay/verify_nf545_original_J242_exp_poly_signature.py.

For a frequency f and monomial order k:
  k EVEN: x^k * sin(2*pi*f*x)
  k ODD:  x^k * cos(2*pi*f*x).
The remaining index 241 is exactly sinh(x/2).

This does NOT formalize the analytic exponential-polynomial uniqueness
theorem or the weighted Gram positivity for these functions.
It formally checks the original source's distinct positive rational
frequency signature, group count, and all 241 oscillator indices.
-/

/-- Actual original 67 rational oscillator frequencies and contiguous
monomial multiplicities, without numerical rounding or reindexing. -/
def nf545OriginalSelectedFrequencyGroups : List (ℚ × ℕ) := [
  ((37/64 : ℚ), 14),
  ((211/128 : ℚ), 9),
  ((45/16 : ℚ), 9),
  ((117/32 : ℚ), 5),
  ((141/32 : ℚ), 6),
  ((45/8 : ℚ), 5),
  ((25/4 : ℚ), 4),
  ((929/128 : ℚ), 5),
  ((523/64 : ℚ), 4),
  ((1113/128 : ℚ), 4),
  ((295/32 : ℚ), 3),
  ((641/64 : ℚ), 4),
  ((1511/128 : ℚ), 4),
  ((1651/128 : ℚ), 4),
  ((1845/128 : ℚ), 4),
  ((1979/128 : ℚ), 4),
  ((2223/128 : ℚ), 5),
  ((641/32 : ℚ), 4),
  ((2777/128 : ℚ), 4),
  ((1477/64 : ℚ), 3),
  ((1513/64 : ℚ), 4),
  ((197/8 : ℚ), 3),
  ((437/16 : ℚ), 5),
  ((4071/128 : ℚ), 4),
  ((1135/32 : ℚ), 3),
  ((2305/64 : ℚ), 3),
  ((2501/64 : ℚ), 4),
  ((5721/128 : ℚ), 4),
  ((393/8 : ℚ), 1),
  ((815/16 : ℚ), 2),
  ((6645/128 : ℚ), 3),
  ((6839/128 : ℚ), 1),
  ((7229/128 : ℚ), 2),
  ((7567/128 : ℚ), 4),
  ((8499/128 : ℚ), 4),
  ((72 : ℚ), 3),
  ((4895/64 : ℚ), 4),
  ((10721/128 : ℚ), 4),
  ((5531/64 : ℚ), 2),
  ((12567/128 : ℚ), 3),
  ((6643/64 : ℚ), 4),
  ((14217/128 : ℚ), 3),
  ((7397/64 : ℚ), 3),
  ((15511/128 : ℚ), 2),
  ((16065/128 : ℚ), 2),
  ((8679/64 : ℚ), 3),
  ((18289/128 : ℚ), 4),
  ((297/2 : ℚ), 1),
  ((20853/128 : ℚ), 2),
  ((21785/128 : ℚ), 3),
  ((3001/16 : ℚ), 4),
  ((25855/128 : ℚ), 3),
  ((14039/64 : ℚ), 3),
  ((15787/64 : ℚ), 4),
  ((1143/4 : ℚ), 2),
  ((37295/128 : ℚ), 3),
  ((39141/128 : ℚ), 2),
  ((41365/128 : ℚ), 3),
  ((5287/16 : ℚ), 2),
  ((44861/128 : ℚ), 3),
  ((49863/128 : ℚ), 3),
  ((55583/128 : ℚ), 3),
  ((59653/128 : ℚ), 2),
  ((31575/64 : ℚ), 3),
  ((81437/128 : ℚ), 3),
  ((23681/32 : ℚ), 2),
  ((113013/128 : ℚ), 2)
]

/-- The old 242-dimensional source has 67 distinct oscillator
frequencies, not a substituted family. -/
theorem nf545OriginalFrequencyGroupCount :
    nf545OriginalSelectedFrequencyGroups.length = 67 := by
  decide

/-- The exact original rational oscillator frequencies are pairwise
different. This is the decisive characteristic-root-separation gate
for the exponential-polynomial independence argument. -/
theorem nf545OriginalFrequenciesPairwiseDistinct :
    (nf545OriginalSelectedFrequencyGroups.map Prod.fst).Nodup := by
  decide +kernel

/-- The original 67 oscillator blocks have EXACTLY 241 monomial
directions. The separate genuine sinh pole is index 241. -/
theorem nf545OriginalOscillatorDimension :
    (nf545OriginalSelectedFrequencyGroups.map Prod.snd).sum = 241 := by
  decide

/-- All frequency rationals are strictly positive, so their
± 2πi f characteristic roots are distinct and nonzero. -/
theorem nf545OriginalFrequenciesPositive :
    (nf545OriginalSelectedFrequencyGroups.map Prod.fst).Forall
       (fun f => (0 : ℚ) < f) := by
  decide +kernel

/-- All 67 original group multiplicities are positive; the exact
source script separately checks each k-block is 0,1,...,m-1. -/
theorem nf545OriginalBlockLengthsPositive :
    (nf545OriginalSelectedFrequencyGroups.map Prod.snd).Forall
       (fun m => 0 < m) := by
  decide

end WeilDefect
