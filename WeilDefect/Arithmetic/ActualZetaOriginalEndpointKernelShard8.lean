import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_critical_0 : neutralNF602CriticalCheck (0:Fin 32) = true := by decide +kernel
private theorem nf605_critical_1 : neutralNF602CriticalCheck (1:Fin 32) = true := by decide +kernel
private theorem nf605_critical_2 : neutralNF602CriticalCheck (2:Fin 32) = true := by decide +kernel
private theorem nf605_critical_3 : neutralNF602CriticalCheck (3:Fin 32) = true := by decide +kernel
private theorem nf605_critical_4 : neutralNF602CriticalCheck (4:Fin 32) = true := by decide +kernel
private theorem nf605_critical_5 : neutralNF602CriticalCheck (5:Fin 32) = true := by decide +kernel
private theorem nf605_critical_6 : neutralNF602CriticalCheck (6:Fin 32) = true := by decide +kernel
private theorem nf605_critical_7 : neutralNF602CriticalCheck (7:Fin 32) = true := by decide +kernel
private theorem nf605_critical_8 : neutralNF602CriticalCheck (8:Fin 32) = true := by decide +kernel
private theorem nf605_critical_9 : neutralNF602CriticalCheck (9:Fin 32) = true := by decide +kernel
private theorem nf605_critical_10 : neutralNF602CriticalCheck (10:Fin 32) = true := by decide +kernel
private theorem nf605_critical_11 : neutralNF602CriticalCheck (11:Fin 32) = true := by decide +kernel
private theorem nf605_critical_12 : neutralNF602CriticalCheck (12:Fin 32) = true := by decide +kernel
private theorem nf605_critical_13 : neutralNF602CriticalCheck (13:Fin 32) = true := by decide +kernel
private theorem nf605_critical_14 : neutralNF602CriticalCheck (14:Fin 32) = true := by decide +kernel
private theorem nf605_critical_15 : neutralNF602CriticalCheck (15:Fin 32) = true := by decide +kernel
private theorem nf605_critical_16 : neutralNF602CriticalCheck (16:Fin 32) = true := by decide +kernel
private theorem nf605_critical_17 : neutralNF602CriticalCheck (17:Fin 32) = true := by decide +kernel
private theorem nf605_critical_18 : neutralNF602CriticalCheck (18:Fin 32) = true := by decide +kernel
private theorem nf605_critical_19 : neutralNF602CriticalCheck (19:Fin 32) = true := by decide +kernel
private theorem nf605_critical_20 : neutralNF602CriticalCheck (20:Fin 32) = true := by decide +kernel
private theorem nf605_critical_21 : neutralNF602CriticalCheck (21:Fin 32) = true := by decide +kernel
private theorem nf605_critical_22 : neutralNF602CriticalCheck (22:Fin 32) = true := by decide +kernel
private theorem nf605_critical_23 : neutralNF602CriticalCheck (23:Fin 32) = true := by decide +kernel
private theorem nf605_critical_24 : neutralNF602CriticalCheck (24:Fin 32) = true := by decide +kernel
private theorem nf605_critical_25 : neutralNF602CriticalCheck (25:Fin 32) = true := by decide +kernel
private theorem nf605_critical_26 : neutralNF602CriticalCheck (26:Fin 32) = true := by decide +kernel
private theorem nf605_critical_27 : neutralNF602CriticalCheck (27:Fin 32) = true := by decide +kernel
private theorem nf605_critical_28 : neutralNF602CriticalCheck (28:Fin 32) = true := by decide +kernel
private theorem nf605_critical_29 : neutralNF602CriticalCheck (29:Fin 32) = true := by decide +kernel
private theorem nf605_critical_30 : neutralNF602CriticalCheck (30:Fin 32) = true := by decide +kernel
private theorem nf605_critical_31 : neutralNF602CriticalCheck (31:Fin 32) = true := by decide +kernel

theorem neutralNF605CriticalShard8 (j : Fin 32) : neutralNF602CriticalCheck j = true := by
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
            have hj : j = (⟨0,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 0
              omega)
            rw [hj]
            exact nf605_critical_0
          ·
            have hj : j = (⟨1,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 1
              omega)
            rw [hj]
            exact nf605_critical_1
        ·
          by_cases h3 : j.val < 3
          ·
            have hj : j = (⟨2,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 2
              omega)
            rw [hj]
            exact nf605_critical_2
          ·
            have hj : j = (⟨3,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 3
              omega)
            rw [hj]
            exact nf605_critical_3
      ·
        by_cases h6 : j.val < 6
        ·
          by_cases h5 : j.val < 5
          ·
            have hj : j = (⟨4,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 4
              omega)
            rw [hj]
            exact nf605_critical_4
          ·
            have hj : j = (⟨5,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 5
              omega)
            rw [hj]
            exact nf605_critical_5
        ·
          by_cases h7 : j.val < 7
          ·
            have hj : j = (⟨6,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 6
              omega)
            rw [hj]
            exact nf605_critical_6
          ·
            have hj : j = (⟨7,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 7
              omega)
            rw [hj]
            exact nf605_critical_7
    ·
      by_cases h12 : j.val < 12
      ·
        by_cases h10 : j.val < 10
        ·
          by_cases h9 : j.val < 9
          ·
            have hj : j = (⟨8,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 8
              omega)
            rw [hj]
            exact nf605_critical_8
          ·
            have hj : j = (⟨9,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 9
              omega)
            rw [hj]
            exact nf605_critical_9
        ·
          by_cases h11 : j.val < 11
          ·
            have hj : j = (⟨10,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 10
              omega)
            rw [hj]
            exact nf605_critical_10
          ·
            have hj : j = (⟨11,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 11
              omega)
            rw [hj]
            exact nf605_critical_11
      ·
        by_cases h14 : j.val < 14
        ·
          by_cases h13 : j.val < 13
          ·
            have hj : j = (⟨12,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 12
              omega)
            rw [hj]
            exact nf605_critical_12
          ·
            have hj : j = (⟨13,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 13
              omega)
            rw [hj]
            exact nf605_critical_13
        ·
          by_cases h15 : j.val < 15
          ·
            have hj : j = (⟨14,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 14
              omega)
            rw [hj]
            exact nf605_critical_14
          ·
            have hj : j = (⟨15,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 15
              omega)
            rw [hj]
            exact nf605_critical_15
  ·
    by_cases h24 : j.val < 24
    ·
      by_cases h20 : j.val < 20
      ·
        by_cases h18 : j.val < 18
        ·
          by_cases h17 : j.val < 17
          ·
            have hj : j = (⟨16,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 16
              omega)
            rw [hj]
            exact nf605_critical_16
          ·
            have hj : j = (⟨17,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 17
              omega)
            rw [hj]
            exact nf605_critical_17
        ·
          by_cases h19 : j.val < 19
          ·
            have hj : j = (⟨18,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 18
              omega)
            rw [hj]
            exact nf605_critical_18
          ·
            have hj : j = (⟨19,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 19
              omega)
            rw [hj]
            exact nf605_critical_19
      ·
        by_cases h22 : j.val < 22
        ·
          by_cases h21 : j.val < 21
          ·
            have hj : j = (⟨20,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 20
              omega)
            rw [hj]
            exact nf605_critical_20
          ·
            have hj : j = (⟨21,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 21
              omega)
            rw [hj]
            exact nf605_critical_21
        ·
          by_cases h23 : j.val < 23
          ·
            have hj : j = (⟨22,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 22
              omega)
            rw [hj]
            exact nf605_critical_22
          ·
            have hj : j = (⟨23,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 23
              omega)
            rw [hj]
            exact nf605_critical_23
    ·
      by_cases h28 : j.val < 28
      ·
        by_cases h26 : j.val < 26
        ·
          by_cases h25 : j.val < 25
          ·
            have hj : j = (⟨24,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 24
              omega)
            rw [hj]
            exact nf605_critical_24
          ·
            have hj : j = (⟨25,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 25
              omega)
            rw [hj]
            exact nf605_critical_25
        ·
          by_cases h27 : j.val < 27
          ·
            have hj : j = (⟨26,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 26
              omega)
            rw [hj]
            exact nf605_critical_26
          ·
            have hj : j = (⟨27,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 27
              omega)
            rw [hj]
            exact nf605_critical_27
      ·
        by_cases h30 : j.val < 30
        ·
          by_cases h29 : j.val < 29
          ·
            have hj : j = (⟨28,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 28
              omega)
            rw [hj]
            exact nf605_critical_28
          ·
            have hj : j = (⟨29,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 29
              omega)
            rw [hj]
            exact nf605_critical_29
        ·
          by_cases h31 : j.val < 31
          ·
            have hj : j = (⟨30,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 30
              omega)
            rw [hj]
            exact nf605_critical_30
          ·
            have hj : j = (⟨31,by decide⟩ : Fin 32) := Fin.ext (by
              change j.val = 31
              omega)
            rw [hj]
            exact nf605_critical_31

theorem neutralNF605PoleCheck : neutralNF602PoleCheck = true := by decide +kernel
#print axioms neutralNF605PoleCheck

#print axioms neutralNF605CriticalShard8

end WeilDefect
