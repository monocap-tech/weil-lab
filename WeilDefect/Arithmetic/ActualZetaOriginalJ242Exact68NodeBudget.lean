import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialSourceNodes
import WeilDefect.Arithmetic.ActualZetaOriginalJ242HermiteDegreeObstruction
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF565 — the EXACT 68-node weighted interpolation ledger of
the historical original NF407 J242 source, not a generic
242-node interpolation hypothesis.

Each original rational oscillator block (f,m) contributes
one real squared frequency (2π)²f² with weight m. The ONE
last true sinh pole contributes the negative node -1/4
with weight 1. The frequencies are never approximated
numerically and none of the original multiplicities are
modified. All values are computed from the NF545 frozen
rational-frequency block table.
-/

/-- Genuine ORIGINAL real squared oscillator nodes paired with
their exact positive integer Hermite multiplicities. -/
def neutralNF565Actual67WeightedSquaredNodes : List (ℝ × ℕ) :=
  nf545OriginalSelectedFrequencyGroups.map fun g =>
    (((2 * Real.pi) ^ 2 * ((g.1 ^ 2 : ℚ) : ℝ)), g.2)

/-- The exact full weighted 68-node source: 67 positive real
oscillator squares, and ONE genuine separate sinh-pole -1/4. -/
def neutralNF565Actual68WeightedNodes : List (ℝ × ℕ) :=
  neutralNF565Actual67WeightedSquaredNodes ++ [(-(1 / 4 : ℝ), 1)]

/-- No oscillator is lost or duplicated: the unchanged true
original 68-node ledger has 67+1 entries. -/
theorem neutralNF565Actual68WeightedNodes_length :
    neutralNF565Actual68WeightedNodes.length = 68 := by
  simp [neutralNF565Actual68WeightedNodes,
    neutralNF565Actual67WeightedSquaredNodes,
    nf545OriginalFrequencyGroupCount]

/-- Source-custody equality: the 67 weighted oscillator node
first-coordinates are exactly the 67 real squared nodes already
independently proved distinct in NF557. -/
theorem neutralNF565Actual67WeightedSquaredNodes_fst :
    neutralNF565Actual67WeightedSquaredNodes.map Prod.fst =
      neutralNF557OriginalRealSquaredNodes := by
  simp [neutralNF565Actual67WeightedSquaredNodes,
    neutralNF557OriginalRealSquaredNodes,
    neutralNF557OriginalRationalSquareNodes, List.map_map,
    Function.comp_def]

/-- Exact distinctness of ALL genuine real source nodes,
including the negative pole separated by sign from all
the positive/zero real oscillator squares. -/
theorem neutralNF565Actual68WeightedNodes_nodup :
    (neutralNF565Actual68WeightedNodes.map Prod.fst).Nodup := by
  let l : List ℝ :=
    neutralNF565Actual67WeightedSquaredNodes.map Prod.fst
  have hn : l.Nodup := by
    simpa only [l, neutralNF565Actual67WeightedSquaredNodes_fst]
      using neutralNF557OriginalRealSquaredNodes_nodup
  have hsep : (-(1 / 4 : ℝ)) ∉ l := by
    intro hx
    have hxm :
        (-(1 / 4 : ℝ)) ∈
          (nf545OriginalSelectedFrequencyGroups.map fun g =>
            (2 * Real.pi) ^ 2 * ((g.1 ^ 2 : ℚ) : ℝ)) := by
      simpa only [l, neutralNF565Actual67WeightedSquaredNodes,
        List.map_map, Function.comp_def] using hx
    obtain ⟨g, hg, hval⟩ := List.mem_map.mp hxm
    have hnonn : 0 ≤
        (2 * Real.pi) ^ 2 * ((g.1 ^ 2 : ℚ) : ℝ) := by
      have hq : (0 : ℚ) ≤ g.1 ^ 2 := sq_nonneg _
      exact mul_nonneg (sq_nonneg _) (by exact_mod_cast hq)
    nlinarith
  have hc : ((-(1 / 4 : ℝ)) :: l).Nodup :=
    List.nodup_cons.mpr ⟨hsep, hn⟩
  have happend : (l ++ [-(1 / 4 : ℝ)]).Nodup :=
    (List.nodup_append_comm).mpr (by simpa using hc)
  simpa only [neutralNF565Actual68WeightedNodes,
    List.map_append, List.map_cons, List.map_nil] using happend

/-- EXACT source Hermite multiplicity budget: authentic original
241 oscillator monomial rows plus genuine sinh pole one. -/
theorem neutralNF565Actual68WeightedNodes_budget :
    (neutralNF565Actual68WeightedNodes.map Prod.snd).sum = 242 := by
  simp [neutralNF565Actual68WeightedNodes,
    neutralNF565Actual67WeightedSquaredNodes,
    List.map_append, List.map_map, Function.comp_def,
    nf545OriginalOscillatorDimension]

end
end WeilDefect
