import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_32 : neutralNF602SelectedCheck (32:Fin 242) = true := by decide +kernel
private theorem nf605_selected_33 : neutralNF602SelectedCheck (33:Fin 242) = true := by decide +kernel
private theorem nf605_selected_34 : neutralNF602SelectedCheck (34:Fin 242) = true := by decide +kernel
private theorem nf605_selected_35 : neutralNF602SelectedCheck (35:Fin 242) = true := by decide +kernel
private theorem nf605_selected_36 : neutralNF602SelectedCheck (36:Fin 242) = true := by decide +kernel
private theorem nf605_selected_37 : neutralNF602SelectedCheck (37:Fin 242) = true := by decide +kernel
private theorem nf605_selected_38 : neutralNF602SelectedCheck (38:Fin 242) = true := by decide +kernel
private theorem nf605_selected_39 : neutralNF602SelectedCheck (39:Fin 242) = true := by decide +kernel
private theorem nf605_selected_40 : neutralNF602SelectedCheck (40:Fin 242) = true := by decide +kernel
private theorem nf605_selected_41 : neutralNF602SelectedCheck (41:Fin 242) = true := by decide +kernel
private theorem nf605_selected_42 : neutralNF602SelectedCheck (42:Fin 242) = true := by decide +kernel
private theorem nf605_selected_43 : neutralNF602SelectedCheck (43:Fin 242) = true := by decide +kernel
private theorem nf605_selected_44 : neutralNF602SelectedCheck (44:Fin 242) = true := by decide +kernel
private theorem nf605_selected_45 : neutralNF602SelectedCheck (45:Fin 242) = true := by decide +kernel
private theorem nf605_selected_46 : neutralNF602SelectedCheck (46:Fin 242) = true := by decide +kernel
private theorem nf605_selected_47 : neutralNF602SelectedCheck (47:Fin 242) = true := by decide +kernel
private theorem nf605_selected_48 : neutralNF602SelectedCheck (48:Fin 242) = true := by decide +kernel
private theorem nf605_selected_49 : neutralNF602SelectedCheck (49:Fin 242) = true := by decide +kernel
private theorem nf605_selected_50 : neutralNF602SelectedCheck (50:Fin 242) = true := by decide +kernel
private theorem nf605_selected_51 : neutralNF602SelectedCheck (51:Fin 242) = true := by decide +kernel
private theorem nf605_selected_52 : neutralNF602SelectedCheck (52:Fin 242) = true := by decide +kernel
private theorem nf605_selected_53 : neutralNF602SelectedCheck (53:Fin 242) = true := by decide +kernel
private theorem nf605_selected_54 : neutralNF602SelectedCheck (54:Fin 242) = true := by decide +kernel
private theorem nf605_selected_55 : neutralNF602SelectedCheck (55:Fin 242) = true := by decide +kernel
private theorem nf605_selected_56 : neutralNF602SelectedCheck (56:Fin 242) = true := by decide +kernel
private theorem nf605_selected_57 : neutralNF602SelectedCheck (57:Fin 242) = true := by decide +kernel
private theorem nf605_selected_58 : neutralNF602SelectedCheck (58:Fin 242) = true := by decide +kernel
private theorem nf605_selected_59 : neutralNF602SelectedCheck (59:Fin 242) = true := by decide +kernel
private theorem nf605_selected_60 : neutralNF602SelectedCheck (60:Fin 242) = true := by decide +kernel
private theorem nf605_selected_61 : neutralNF602SelectedCheck (61:Fin 242) = true := by decide +kernel
private theorem nf605_selected_62 : neutralNF602SelectedCheck (62:Fin 242) = true := by decide +kernel
private theorem nf605_selected_63 : neutralNF602SelectedCheck (63:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard1 (j : Fin 242) (hlo : 32 ≤ j.val) (hhi : j.val < 64) : neutralNF602SelectedCheck j = true := by
  by_cases h48 : j.val < 48
  ·
    by_cases h40 : j.val < 40
    ·
      by_cases h36 : j.val < 36
      ·
        by_cases h34 : j.val < 34
        ·
          by_cases h33 : j.val < 33
          ·
            have hj : j = (⟨32,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 32
              omega)
            rw [hj]
            exact nf605_selected_32
          ·
            have hj : j = (⟨33,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 33
              omega)
            rw [hj]
            exact nf605_selected_33
        ·
          by_cases h35 : j.val < 35
          ·
            have hj : j = (⟨34,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 34
              omega)
            rw [hj]
            exact nf605_selected_34
          ·
            have hj : j = (⟨35,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 35
              omega)
            rw [hj]
            exact nf605_selected_35
      ·
        by_cases h38 : j.val < 38
        ·
          by_cases h37 : j.val < 37
          ·
            have hj : j = (⟨36,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 36
              omega)
            rw [hj]
            exact nf605_selected_36
          ·
            have hj : j = (⟨37,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 37
              omega)
            rw [hj]
            exact nf605_selected_37
        ·
          by_cases h39 : j.val < 39
          ·
            have hj : j = (⟨38,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 38
              omega)
            rw [hj]
            exact nf605_selected_38
          ·
            have hj : j = (⟨39,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 39
              omega)
            rw [hj]
            exact nf605_selected_39
    ·
      by_cases h44 : j.val < 44
      ·
        by_cases h42 : j.val < 42
        ·
          by_cases h41 : j.val < 41
          ·
            have hj : j = (⟨40,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 40
              omega)
            rw [hj]
            exact nf605_selected_40
          ·
            have hj : j = (⟨41,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 41
              omega)
            rw [hj]
            exact nf605_selected_41
        ·
          by_cases h43 : j.val < 43
          ·
            have hj : j = (⟨42,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 42
              omega)
            rw [hj]
            exact nf605_selected_42
          ·
            have hj : j = (⟨43,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 43
              omega)
            rw [hj]
            exact nf605_selected_43
      ·
        by_cases h46 : j.val < 46
        ·
          by_cases h45 : j.val < 45
          ·
            have hj : j = (⟨44,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 44
              omega)
            rw [hj]
            exact nf605_selected_44
          ·
            have hj : j = (⟨45,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 45
              omega)
            rw [hj]
            exact nf605_selected_45
        ·
          by_cases h47 : j.val < 47
          ·
            have hj : j = (⟨46,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 46
              omega)
            rw [hj]
            exact nf605_selected_46
          ·
            have hj : j = (⟨47,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 47
              omega)
            rw [hj]
            exact nf605_selected_47
  ·
    by_cases h56 : j.val < 56
    ·
      by_cases h52 : j.val < 52
      ·
        by_cases h50 : j.val < 50
        ·
          by_cases h49 : j.val < 49
          ·
            have hj : j = (⟨48,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 48
              omega)
            rw [hj]
            exact nf605_selected_48
          ·
            have hj : j = (⟨49,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 49
              omega)
            rw [hj]
            exact nf605_selected_49
        ·
          by_cases h51 : j.val < 51
          ·
            have hj : j = (⟨50,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 50
              omega)
            rw [hj]
            exact nf605_selected_50
          ·
            have hj : j = (⟨51,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 51
              omega)
            rw [hj]
            exact nf605_selected_51
      ·
        by_cases h54 : j.val < 54
        ·
          by_cases h53 : j.val < 53
          ·
            have hj : j = (⟨52,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 52
              omega)
            rw [hj]
            exact nf605_selected_52
          ·
            have hj : j = (⟨53,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 53
              omega)
            rw [hj]
            exact nf605_selected_53
        ·
          by_cases h55 : j.val < 55
          ·
            have hj : j = (⟨54,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 54
              omega)
            rw [hj]
            exact nf605_selected_54
          ·
            have hj : j = (⟨55,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 55
              omega)
            rw [hj]
            exact nf605_selected_55
    ·
      by_cases h60 : j.val < 60
      ·
        by_cases h58 : j.val < 58
        ·
          by_cases h57 : j.val < 57
          ·
            have hj : j = (⟨56,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 56
              omega)
            rw [hj]
            exact nf605_selected_56
          ·
            have hj : j = (⟨57,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 57
              omega)
            rw [hj]
            exact nf605_selected_57
        ·
          by_cases h59 : j.val < 59
          ·
            have hj : j = (⟨58,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 58
              omega)
            rw [hj]
            exact nf605_selected_58
          ·
            have hj : j = (⟨59,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 59
              omega)
            rw [hj]
            exact nf605_selected_59
      ·
        by_cases h62 : j.val < 62
        ·
          by_cases h61 : j.val < 61
          ·
            have hj : j = (⟨60,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 60
              omega)
            rw [hj]
            exact nf605_selected_60
          ·
            have hj : j = (⟨61,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 61
              omega)
            rw [hj]
            exact nf605_selected_61
        ·
          by_cases h63 : j.val < 63
          ·
            have hj : j = (⟨62,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 62
              omega)
            rw [hj]
            exact nf605_selected_62
          ·
            have hj : j = (⟨63,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 63
              omega)
            rw [hj]
            exact nf605_selected_63

#print axioms neutralNF605SelectedShard1

end WeilDefect
