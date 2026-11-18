import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_64 : neutralNF602SelectedCheck (64:Fin 242) = true := by decide +kernel
private theorem nf605_selected_65 : neutralNF602SelectedCheck (65:Fin 242) = true := by decide +kernel
private theorem nf605_selected_66 : neutralNF602SelectedCheck (66:Fin 242) = true := by decide +kernel
private theorem nf605_selected_67 : neutralNF602SelectedCheck (67:Fin 242) = true := by decide +kernel
private theorem nf605_selected_68 : neutralNF602SelectedCheck (68:Fin 242) = true := by decide +kernel
private theorem nf605_selected_69 : neutralNF602SelectedCheck (69:Fin 242) = true := by decide +kernel
private theorem nf605_selected_70 : neutralNF602SelectedCheck (70:Fin 242) = true := by decide +kernel
private theorem nf605_selected_71 : neutralNF602SelectedCheck (71:Fin 242) = true := by decide +kernel
private theorem nf605_selected_72 : neutralNF602SelectedCheck (72:Fin 242) = true := by decide +kernel
private theorem nf605_selected_73 : neutralNF602SelectedCheck (73:Fin 242) = true := by decide +kernel
private theorem nf605_selected_74 : neutralNF602SelectedCheck (74:Fin 242) = true := by decide +kernel
private theorem nf605_selected_75 : neutralNF602SelectedCheck (75:Fin 242) = true := by decide +kernel
private theorem nf605_selected_76 : neutralNF602SelectedCheck (76:Fin 242) = true := by decide +kernel
private theorem nf605_selected_77 : neutralNF602SelectedCheck (77:Fin 242) = true := by decide +kernel
private theorem nf605_selected_78 : neutralNF602SelectedCheck (78:Fin 242) = true := by decide +kernel
private theorem nf605_selected_79 : neutralNF602SelectedCheck (79:Fin 242) = true := by decide +kernel
private theorem nf605_selected_80 : neutralNF602SelectedCheck (80:Fin 242) = true := by decide +kernel
private theorem nf605_selected_81 : neutralNF602SelectedCheck (81:Fin 242) = true := by decide +kernel
private theorem nf605_selected_82 : neutralNF602SelectedCheck (82:Fin 242) = true := by decide +kernel
private theorem nf605_selected_83 : neutralNF602SelectedCheck (83:Fin 242) = true := by decide +kernel
private theorem nf605_selected_84 : neutralNF602SelectedCheck (84:Fin 242) = true := by decide +kernel
private theorem nf605_selected_85 : neutralNF602SelectedCheck (85:Fin 242) = true := by decide +kernel
private theorem nf605_selected_86 : neutralNF602SelectedCheck (86:Fin 242) = true := by decide +kernel
private theorem nf605_selected_87 : neutralNF602SelectedCheck (87:Fin 242) = true := by decide +kernel
private theorem nf605_selected_88 : neutralNF602SelectedCheck (88:Fin 242) = true := by decide +kernel
private theorem nf605_selected_89 : neutralNF602SelectedCheck (89:Fin 242) = true := by decide +kernel
private theorem nf605_selected_90 : neutralNF602SelectedCheck (90:Fin 242) = true := by decide +kernel
private theorem nf605_selected_91 : neutralNF602SelectedCheck (91:Fin 242) = true := by decide +kernel
private theorem nf605_selected_92 : neutralNF602SelectedCheck (92:Fin 242) = true := by decide +kernel
private theorem nf605_selected_93 : neutralNF602SelectedCheck (93:Fin 242) = true := by decide +kernel
private theorem nf605_selected_94 : neutralNF602SelectedCheck (94:Fin 242) = true := by decide +kernel
private theorem nf605_selected_95 : neutralNF602SelectedCheck (95:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard2 (j : Fin 242) (hlo : 64 ≤ j.val) (hhi : j.val < 96) : neutralNF602SelectedCheck j = true := by
  by_cases h80 : j.val < 80
  ·
    by_cases h72 : j.val < 72
    ·
      by_cases h68 : j.val < 68
      ·
        by_cases h66 : j.val < 66
        ·
          by_cases h65 : j.val < 65
          ·
            have hj : j = (⟨64,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 64
              omega)
            rw [hj]
            exact nf605_selected_64
          ·
            have hj : j = (⟨65,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 65
              omega)
            rw [hj]
            exact nf605_selected_65
        ·
          by_cases h67 : j.val < 67
          ·
            have hj : j = (⟨66,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 66
              omega)
            rw [hj]
            exact nf605_selected_66
          ·
            have hj : j = (⟨67,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 67
              omega)
            rw [hj]
            exact nf605_selected_67
      ·
        by_cases h70 : j.val < 70
        ·
          by_cases h69 : j.val < 69
          ·
            have hj : j = (⟨68,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 68
              omega)
            rw [hj]
            exact nf605_selected_68
          ·
            have hj : j = (⟨69,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 69
              omega)
            rw [hj]
            exact nf605_selected_69
        ·
          by_cases h71 : j.val < 71
          ·
            have hj : j = (⟨70,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 70
              omega)
            rw [hj]
            exact nf605_selected_70
          ·
            have hj : j = (⟨71,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 71
              omega)
            rw [hj]
            exact nf605_selected_71
    ·
      by_cases h76 : j.val < 76
      ·
        by_cases h74 : j.val < 74
        ·
          by_cases h73 : j.val < 73
          ·
            have hj : j = (⟨72,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 72
              omega)
            rw [hj]
            exact nf605_selected_72
          ·
            have hj : j = (⟨73,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 73
              omega)
            rw [hj]
            exact nf605_selected_73
        ·
          by_cases h75 : j.val < 75
          ·
            have hj : j = (⟨74,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 74
              omega)
            rw [hj]
            exact nf605_selected_74
          ·
            have hj : j = (⟨75,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 75
              omega)
            rw [hj]
            exact nf605_selected_75
      ·
        by_cases h78 : j.val < 78
        ·
          by_cases h77 : j.val < 77
          ·
            have hj : j = (⟨76,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 76
              omega)
            rw [hj]
            exact nf605_selected_76
          ·
            have hj : j = (⟨77,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 77
              omega)
            rw [hj]
            exact nf605_selected_77
        ·
          by_cases h79 : j.val < 79
          ·
            have hj : j = (⟨78,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 78
              omega)
            rw [hj]
            exact nf605_selected_78
          ·
            have hj : j = (⟨79,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 79
              omega)
            rw [hj]
            exact nf605_selected_79
  ·
    by_cases h88 : j.val < 88
    ·
      by_cases h84 : j.val < 84
      ·
        by_cases h82 : j.val < 82
        ·
          by_cases h81 : j.val < 81
          ·
            have hj : j = (⟨80,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 80
              omega)
            rw [hj]
            exact nf605_selected_80
          ·
            have hj : j = (⟨81,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 81
              omega)
            rw [hj]
            exact nf605_selected_81
        ·
          by_cases h83 : j.val < 83
          ·
            have hj : j = (⟨82,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 82
              omega)
            rw [hj]
            exact nf605_selected_82
          ·
            have hj : j = (⟨83,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 83
              omega)
            rw [hj]
            exact nf605_selected_83
      ·
        by_cases h86 : j.val < 86
        ·
          by_cases h85 : j.val < 85
          ·
            have hj : j = (⟨84,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 84
              omega)
            rw [hj]
            exact nf605_selected_84
          ·
            have hj : j = (⟨85,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 85
              omega)
            rw [hj]
            exact nf605_selected_85
        ·
          by_cases h87 : j.val < 87
          ·
            have hj : j = (⟨86,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 86
              omega)
            rw [hj]
            exact nf605_selected_86
          ·
            have hj : j = (⟨87,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 87
              omega)
            rw [hj]
            exact nf605_selected_87
    ·
      by_cases h92 : j.val < 92
      ·
        by_cases h90 : j.val < 90
        ·
          by_cases h89 : j.val < 89
          ·
            have hj : j = (⟨88,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 88
              omega)
            rw [hj]
            exact nf605_selected_88
          ·
            have hj : j = (⟨89,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 89
              omega)
            rw [hj]
            exact nf605_selected_89
        ·
          by_cases h91 : j.val < 91
          ·
            have hj : j = (⟨90,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 90
              omega)
            rw [hj]
            exact nf605_selected_90
          ·
            have hj : j = (⟨91,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 91
              omega)
            rw [hj]
            exact nf605_selected_91
      ·
        by_cases h94 : j.val < 94
        ·
          by_cases h93 : j.val < 93
          ·
            have hj : j = (⟨92,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 92
              omega)
            rw [hj]
            exact nf605_selected_92
          ·
            have hj : j = (⟨93,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 93
              omega)
            rw [hj]
            exact nf605_selected_93
        ·
          by_cases h95 : j.val < 95
          ·
            have hj : j = (⟨94,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 94
              omega)
            rw [hj]
            exact nf605_selected_94
          ·
            have hj : j = (⟨95,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 95
              omega)
            rw [hj]
            exact nf605_selected_95

#print axioms neutralNF605SelectedShard2

end WeilDefect
