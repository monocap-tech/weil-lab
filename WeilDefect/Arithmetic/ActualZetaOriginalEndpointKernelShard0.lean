import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_0 : neutralNF602SelectedCheck (0:Fin 242) = true := by decide +kernel
private theorem nf605_selected_1 : neutralNF602SelectedCheck (1:Fin 242) = true := by decide +kernel
private theorem nf605_selected_2 : neutralNF602SelectedCheck (2:Fin 242) = true := by decide +kernel
private theorem nf605_selected_3 : neutralNF602SelectedCheck (3:Fin 242) = true := by decide +kernel
private theorem nf605_selected_4 : neutralNF602SelectedCheck (4:Fin 242) = true := by decide +kernel
private theorem nf605_selected_5 : neutralNF602SelectedCheck (5:Fin 242) = true := by decide +kernel
private theorem nf605_selected_6 : neutralNF602SelectedCheck (6:Fin 242) = true := by decide +kernel
private theorem nf605_selected_7 : neutralNF602SelectedCheck (7:Fin 242) = true := by decide +kernel
private theorem nf605_selected_8 : neutralNF602SelectedCheck (8:Fin 242) = true := by decide +kernel
private theorem nf605_selected_9 : neutralNF602SelectedCheck (9:Fin 242) = true := by decide +kernel
private theorem nf605_selected_10 : neutralNF602SelectedCheck (10:Fin 242) = true := by decide +kernel
private theorem nf605_selected_11 : neutralNF602SelectedCheck (11:Fin 242) = true := by decide +kernel
private theorem nf605_selected_12 : neutralNF602SelectedCheck (12:Fin 242) = true := by decide +kernel
private theorem nf605_selected_13 : neutralNF602SelectedCheck (13:Fin 242) = true := by decide +kernel
private theorem nf605_selected_14 : neutralNF602SelectedCheck (14:Fin 242) = true := by decide +kernel
private theorem nf605_selected_15 : neutralNF602SelectedCheck (15:Fin 242) = true := by decide +kernel
private theorem nf605_selected_16 : neutralNF602SelectedCheck (16:Fin 242) = true := by decide +kernel
private theorem nf605_selected_17 : neutralNF602SelectedCheck (17:Fin 242) = true := by decide +kernel
private theorem nf605_selected_18 : neutralNF602SelectedCheck (18:Fin 242) = true := by decide +kernel
private theorem nf605_selected_19 : neutralNF602SelectedCheck (19:Fin 242) = true := by decide +kernel
private theorem nf605_selected_20 : neutralNF602SelectedCheck (20:Fin 242) = true := by decide +kernel
private theorem nf605_selected_21 : neutralNF602SelectedCheck (21:Fin 242) = true := by decide +kernel
private theorem nf605_selected_22 : neutralNF602SelectedCheck (22:Fin 242) = true := by decide +kernel
private theorem nf605_selected_23 : neutralNF602SelectedCheck (23:Fin 242) = true := by decide +kernel
private theorem nf605_selected_24 : neutralNF602SelectedCheck (24:Fin 242) = true := by decide +kernel
private theorem nf605_selected_25 : neutralNF602SelectedCheck (25:Fin 242) = true := by decide +kernel
private theorem nf605_selected_26 : neutralNF602SelectedCheck (26:Fin 242) = true := by decide +kernel
private theorem nf605_selected_27 : neutralNF602SelectedCheck (27:Fin 242) = true := by decide +kernel
private theorem nf605_selected_28 : neutralNF602SelectedCheck (28:Fin 242) = true := by decide +kernel
private theorem nf605_selected_29 : neutralNF602SelectedCheck (29:Fin 242) = true := by decide +kernel
private theorem nf605_selected_30 : neutralNF602SelectedCheck (30:Fin 242) = true := by decide +kernel
private theorem nf605_selected_31 : neutralNF602SelectedCheck (31:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard0 (j : Fin 242) (hlo : 0 ≤ j.val) (hhi : j.val < 32) : neutralNF602SelectedCheck j = true := by
  by_cases h16 : j.val < 16
  ·
    by_cases h8 : j.val < 8
    ·
      by_cases h4 : j.val < 4
      ·
        by_cases h2 : j.val < 2
        ·
          by_cases h1 : j.val < 1
          ·
            have hj : j = (⟨0,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 0
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_0
          ·
            have hj : j = (⟨1,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 1
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_1
        ·
          by_cases h3 : j.val < 3
          ·
            have hj : j = (⟨2,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 2
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_2
          ·
            have hj : j = (⟨3,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 3
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_3
      ·
        by_cases h6 : j.val < 6
        ·
          by_cases h5 : j.val < 5
          ·
            have hj : j = (⟨4,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 4
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_4
          ·
            have hj : j = (⟨5,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 5
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_5
        ·
          by_cases h7 : j.val < 7
          ·
            have hj : j = (⟨6,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 6
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_6
          ·
            have hj : j = (⟨7,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 7
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_7
    ·
      by_cases h12 : j.val < 12
      ·
        by_cases h10 : j.val < 10
        ·
          by_cases h9 : j.val < 9
          ·
            have hj : j = (⟨8,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 8
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_8
          ·
            have hj : j = (⟨9,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 9
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_9
        ·
          by_cases h11 : j.val < 11
          ·
            have hj : j = (⟨10,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 10
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_10
          ·
            have hj : j = (⟨11,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 11
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_11
      ·
        by_cases h14 : j.val < 14
        ·
          by_cases h13 : j.val < 13
          ·
            have hj : j = (⟨12,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 12
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_12
          ·
            have hj : j = (⟨13,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 13
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_13
        ·
          by_cases h15 : j.val < 15
          ·
            have hj : j = (⟨14,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 14
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_14
          ·
            have hj : j = (⟨15,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 15
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_15
  ·
    by_cases h24 : j.val < 24
    ·
      by_cases h20 : j.val < 20
      ·
        by_cases h18 : j.val < 18
        ·
          by_cases h17 : j.val < 17
          ·
            have hj : j = (⟨16,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 16
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_16
          ·
            have hj : j = (⟨17,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 17
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_17
        ·
          by_cases h19 : j.val < 19
          ·
            have hj : j = (⟨18,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 18
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_18
          ·
            have hj : j = (⟨19,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 19
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_19
      ·
        by_cases h22 : j.val < 22
        ·
          by_cases h21 : j.val < 21
          ·
            have hj : j = (⟨20,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 20
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_20
          ·
            have hj : j = (⟨21,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 21
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_21
        ·
          by_cases h23 : j.val < 23
          ·
            have hj : j = (⟨22,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 22
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_22
          ·
            have hj : j = (⟨23,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 23
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_23
    ·
      by_cases h28 : j.val < 28
      ·
        by_cases h26 : j.val < 26
        ·
          by_cases h25 : j.val < 25
          ·
            have hj : j = (⟨24,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 24
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_24
          ·
            have hj : j = (⟨25,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 25
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_25
        ·
          by_cases h27 : j.val < 27
          ·
            have hj : j = (⟨26,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 26
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_26
          ·
            have hj : j = (⟨27,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 27
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_27
      ·
        by_cases h30 : j.val < 30
        ·
          by_cases h29 : j.val < 29
          ·
            have hj : j = (⟨28,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 28
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_28
          ·
            have hj : j = (⟨29,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 29
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_29
        ·
          by_cases h31 : j.val < 31
          ·
            have hj : j = (⟨30,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 30
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_30
          ·
            have hj : j = (⟨31,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 31
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_31

#print axioms neutralNF605SelectedShard0

end WeilDefect
