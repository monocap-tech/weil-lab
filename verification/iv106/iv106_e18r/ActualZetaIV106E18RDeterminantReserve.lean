import WeilDefect.Arithmetic.ActualZetaIV106E18QLiteralRank

namespace WeilDefect
noncomputable section
open Filter
open scoped Topology BigOperators

/-- Keep the actual fixed-tuple lower bound, not just positivity, when
passing from finite truncations to the literal infinite matrix. -/
theorem neutralIV106E18RReserve (k : ℕ) (W X Y : ℕ → ℝ)
    (hw : ∀ n, 0 ≤ W n) (hx : StrictMono X) (hy : StrictAnti Y)
    (A : Matrix (Fin k) (Fin k) ℝ)
    (hs : ∀ i j, HasSum (fun n : ℕ => W n*Y n^i.val*X n^j.val) (A i j)) :
    neutralIV106E18PMinor W X Y (fun i : Fin k => i.val+1) ≤
      (Nat.factorial k:ℝ)*(neutralIV106E18POrient k*A.det) := by
  have ht : Tendsto (fun N => neutralIV106E18PPartial k N W X Y) atTop (𝓝 A) := by
    apply tendsto_pi_nhds.mpr
    intro i
    apply tendsto_pi_nhds.mpr
    intro j
    exact (hs i j).tendsto_sum_nat
  have hd : Tendsto (fun N => (neutralIV106E18PPartial k N W X Y).det)
      atTop (𝓝 A.det) := (continuous_id.matrix_det.continuousAt.tendsto).comp ht
  have hlim : Tendsto (fun N => (Nat.factorial k:ℝ)*
      (neutralIV106E18POrient k*(neutralIV106E18PPartial k N W X Y).det))
      atTop (𝓝 ((Nat.factorial k:ℝ)*(neutralIV106E18POrient k*A.det))) :=
    tendsto_const_nhds.mul (tendsto_const_nhds.mul hd)
  exact le_of_tendsto hlim (eventually_atTop.mpr ⟨k+1,fun N hN =>
    neutralIV106E18PFixed_lower k N W X Y hw hx hy hN⟩)

theorem neutralIV106E18RLiteral_reserve (k : ℕ) (hk : 0 < k) (hk34 : k ≤ 34) :
    neutralIV106E18PMinor (neutralIV106E18OW k hk) neutralIV106E18OX
      (neutralIV106E18OY k) (fun i : Fin k => i.val+1) ≤
        (Nat.factorial k:ℝ)*(neutralIV106E18POrient k*(neutralIV106E18OMatrix k hk).det) := by
  apply neutralIV106E18RReserve
  · intro n
    by_cases hn : n = 0
    · rw [hn,neutralIV106E18OW_zero]
    · exact (neutralIV106E18OW_pos k hk n (Nat.pos_of_ne_zero hn)).le
  · exact neutralIV106E18OX_strict
  · exact neutralIV106E18OY_strict k hk
  · exact neutralIV106E18OMatrix_series k hk hk34

/-- A rational product enclosure for the retained tuple propagates directly
through the determinant reserve, independent of the bump evaluation. -/
theorem neutralIV106E18RProduct_lower {k : ℕ} (W X Y : ℕ → ℝ)
    (w : Fin k → ℝ) (d : Fin k → Fin k → ℝ)
    (hw0 : ∀ i, 0 ≤ w i) (hw : ∀ i, w i ≤ W (i.val+1))
    (hd0 : ∀ i j, i < j → 0 ≤ d i j)
    (hd : ∀ i j, i < j → d i j ≤
      (Y (i.val+1)-Y (j.val+1))*(X (j.val+1)-X (i.val+1))) :
    (∏ i, w i)*(∏ i : Fin k, ∏ j ∈ Finset.Ioi i, d i j) ≤
      neutralIV106E18PMinor W X Y (fun i : Fin k => i.val+1) := by
  unfold neutralIV106E18PMinor
  apply mul_le_mul
  · exact Finset.prod_le_prod (fun i _ => hw0 i) (fun i _ => hw i)
  · apply Finset.prod_le_prod
    · intro i hi
      exact Finset.prod_nonneg fun j hj => hd0 i j (Finset.mem_Ioi.mp hj)
    · intro i hi
      exact Finset.prod_le_prod (fun j hj => hd0 i j (Finset.mem_Ioi.mp hj))
        (fun j hj => hd i j (Finset.mem_Ioi.mp hj))
  · exact Finset.prod_nonneg fun i _ =>
      Finset.prod_nonneg fun j hj => hd0 i j (Finset.mem_Ioi.mp hj)
  · exact Finset.prod_nonneg fun i _ => (hw0 i).trans (hw i)

#print axioms neutralIV106E18RReserve
#print axioms neutralIV106E18RLiteral_reserve
#print axioms neutralIV106E18RProduct_lower
end
end WeilDefect
