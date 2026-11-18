import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_96 : neutralNF602SelectedCheck (96:Fin 242) = true := by decide +kernel
private theorem nf605_selected_97 : neutralNF602SelectedCheck (97:Fin 242) = true := by decide +kernel
private theorem nf605_selected_98 : neutralNF602SelectedCheck (98:Fin 242) = true := by decide +kernel
private theorem nf605_selected_99 : neutralNF602SelectedCheck (99:Fin 242) = true := by decide +kernel
private theorem nf605_selected_100 : neutralNF602SelectedCheck (100:Fin 242) = true := by decide +kernel
private theorem nf605_selected_101 : neutralNF602SelectedCheck (101:Fin 242) = true := by decide +kernel
private theorem nf605_selected_102 : neutralNF602SelectedCheck (102:Fin 242) = true := by decide +kernel
private theorem nf605_selected_103 : neutralNF602SelectedCheck (103:Fin 242) = true := by decide +kernel
private theorem nf605_selected_104 : neutralNF602SelectedCheck (104:Fin 242) = true := by decide +kernel
private theorem nf605_selected_105 : neutralNF602SelectedCheck (105:Fin 242) = true := by decide +kernel
private theorem nf605_selected_106 : neutralNF602SelectedCheck (106:Fin 242) = true := by decide +kernel
private theorem nf605_selected_107 : neutralNF602SelectedCheck (107:Fin 242) = true := by decide +kernel
private theorem nf605_selected_108 : neutralNF602SelectedCheck (108:Fin 242) = true := by decide +kernel
private theorem nf605_selected_109 : neutralNF602SelectedCheck (109:Fin 242) = true := by decide +kernel
private theorem nf605_selected_110 : neutralNF602SelectedCheck (110:Fin 242) = true := by decide +kernel
private theorem nf605_selected_111 : neutralNF602SelectedCheck (111:Fin 242) = true := by decide +kernel
private theorem nf605_selected_112 : neutralNF602SelectedCheck (112:Fin 242) = true := by decide +kernel
private theorem nf605_selected_113 : neutralNF602SelectedCheck (113:Fin 242) = true := by decide +kernel
private theorem nf605_selected_114 : neutralNF602SelectedCheck (114:Fin 242) = true := by decide +kernel
private theorem nf605_selected_115 : neutralNF602SelectedCheck (115:Fin 242) = true := by decide +kernel
private theorem nf605_selected_116 : neutralNF602SelectedCheck (116:Fin 242) = true := by decide +kernel
private theorem nf605_selected_117 : neutralNF602SelectedCheck (117:Fin 242) = true := by decide +kernel
private theorem nf605_selected_118 : neutralNF602SelectedCheck (118:Fin 242) = true := by decide +kernel
private theorem nf605_selected_119 : neutralNF602SelectedCheck (119:Fin 242) = true := by decide +kernel
private theorem nf605_selected_120 : neutralNF602SelectedCheck (120:Fin 242) = true := by decide +kernel
private theorem nf605_selected_121 : neutralNF602SelectedCheck (121:Fin 242) = true := by decide +kernel
private theorem nf605_selected_122 : neutralNF602SelectedCheck (122:Fin 242) = true := by decide +kernel
private theorem nf605_selected_123 : neutralNF602SelectedCheck (123:Fin 242) = true := by decide +kernel
private theorem nf605_selected_124 : neutralNF602SelectedCheck (124:Fin 242) = true := by decide +kernel
private theorem nf605_selected_125 : neutralNF602SelectedCheck (125:Fin 242) = true := by decide +kernel
private theorem nf605_selected_126 : neutralNF602SelectedCheck (126:Fin 242) = true := by decide +kernel
private theorem nf605_selected_127 : neutralNF602SelectedCheck (127:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard3 (j : Fin 242) (hlo : 96 ≤ j.val) (hhi : j.val < 128) : neutralNF602SelectedCheck j = true := by
  by_cases h112 : j.val < 112
  ·
    by_cases h104 : j.val < 104
    ·
      by_cases h100 : j.val < 100
      ·
        by_cases h98 : j.val < 98
        ·
          by_cases h97 : j.val < 97
          ·
            have hj : j = (⟨96,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 96
              omega)
            rw [hj]
            exact nf605_selected_96
          ·
            have hj : j = (⟨97,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 97
              omega)
            rw [hj]
            exact nf605_selected_97
        ·
          by_cases h99 : j.val < 99
          ·
            have hj : j = (⟨98,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 98
              omega)
            rw [hj]
            exact nf605_selected_98
          ·
            have hj : j = (⟨99,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 99
              omega)
            rw [hj]
            exact nf605_selected_99
      ·
        by_cases h102 : j.val < 102
        ·
          by_cases h101 : j.val < 101
          ·
            have hj : j = (⟨100,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 100
              omega)
            rw [hj]
            exact nf605_selected_100
          ·
            have hj : j = (⟨101,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 101
              omega)
            rw [hj]
            exact nf605_selected_101
        ·
          by_cases h103 : j.val < 103
          ·
            have hj : j = (⟨102,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 102
              omega)
            rw [hj]
            exact nf605_selected_102
          ·
            have hj : j = (⟨103,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 103
              omega)
            rw [hj]
            exact nf605_selected_103
    ·
      by_cases h108 : j.val < 108
      ·
        by_cases h106 : j.val < 106
        ·
          by_cases h105 : j.val < 105
          ·
            have hj : j = (⟨104,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 104
              omega)
            rw [hj]
            exact nf605_selected_104
          ·
            have hj : j = (⟨105,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 105
              omega)
            rw [hj]
            exact nf605_selected_105
        ·
          by_cases h107 : j.val < 107
          ·
            have hj : j = (⟨106,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 106
              omega)
            rw [hj]
            exact nf605_selected_106
          ·
            have hj : j = (⟨107,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 107
              omega)
            rw [hj]
            exact nf605_selected_107
      ·
        by_cases h110 : j.val < 110
        ·
          by_cases h109 : j.val < 109
          ·
            have hj : j = (⟨108,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 108
              omega)
            rw [hj]
            exact nf605_selected_108
          ·
            have hj : j = (⟨109,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 109
              omega)
            rw [hj]
            exact nf605_selected_109
        ·
          by_cases h111 : j.val < 111
          ·
            have hj : j = (⟨110,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 110
              omega)
            rw [hj]
            exact nf605_selected_110
          ·
            have hj : j = (⟨111,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 111
              omega)
            rw [hj]
            exact nf605_selected_111
  ·
    by_cases h120 : j.val < 120
    ·
      by_cases h116 : j.val < 116
      ·
        by_cases h114 : j.val < 114
        ·
          by_cases h113 : j.val < 113
          ·
            have hj : j = (⟨112,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 112
              omega)
            rw [hj]
            exact nf605_selected_112
          ·
            have hj : j = (⟨113,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 113
              omega)
            rw [hj]
            exact nf605_selected_113
        ·
          by_cases h115 : j.val < 115
          ·
            have hj : j = (⟨114,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 114
              omega)
            rw [hj]
            exact nf605_selected_114
          ·
            have hj : j = (⟨115,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 115
              omega)
            rw [hj]
            exact nf605_selected_115
      ·
        by_cases h118 : j.val < 118
        ·
          by_cases h117 : j.val < 117
          ·
            have hj : j = (⟨116,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 116
              omega)
            rw [hj]
            exact nf605_selected_116
          ·
            have hj : j = (⟨117,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 117
              omega)
            rw [hj]
            exact nf605_selected_117
        ·
          by_cases h119 : j.val < 119
          ·
            have hj : j = (⟨118,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 118
              omega)
            rw [hj]
            exact nf605_selected_118
          ·
            have hj : j = (⟨119,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 119
              omega)
            rw [hj]
            exact nf605_selected_119
    ·
      by_cases h124 : j.val < 124
      ·
        by_cases h122 : j.val < 122
        ·
          by_cases h121 : j.val < 121
          ·
            have hj : j = (⟨120,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 120
              omega)
            rw [hj]
            exact nf605_selected_120
          ·
            have hj : j = (⟨121,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 121
              omega)
            rw [hj]
            exact nf605_selected_121
        ·
          by_cases h123 : j.val < 123
          ·
            have hj : j = (⟨122,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 122
              omega)
            rw [hj]
            exact nf605_selected_122
          ·
            have hj : j = (⟨123,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 123
              omega)
            rw [hj]
            exact nf605_selected_123
      ·
        by_cases h126 : j.val < 126
        ·
          by_cases h125 : j.val < 125
          ·
            have hj : j = (⟨124,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 124
              omega)
            rw [hj]
            exact nf605_selected_124
          ·
            have hj : j = (⟨125,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 125
              omega)
            rw [hj]
            exact nf605_selected_125
        ·
          by_cases h127 : j.val < 127
          ·
            have hj : j = (⟨126,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 126
              omega)
            rw [hj]
            exact nf605_selected_126
          ·
            have hj : j = (⟨127,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 127
              omega)
            rw [hj]
            exact nf605_selected_127

#print axioms neutralNF605SelectedShard3

end WeilDefect
