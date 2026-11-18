import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_128 : neutralNF602SelectedCheck (128:Fin 242) = true := by decide +kernel
private theorem nf605_selected_129 : neutralNF602SelectedCheck (129:Fin 242) = true := by decide +kernel
private theorem nf605_selected_130 : neutralNF602SelectedCheck (130:Fin 242) = true := by decide +kernel
private theorem nf605_selected_131 : neutralNF602SelectedCheck (131:Fin 242) = true := by decide +kernel
private theorem nf605_selected_132 : neutralNF602SelectedCheck (132:Fin 242) = true := by decide +kernel
private theorem nf605_selected_133 : neutralNF602SelectedCheck (133:Fin 242) = true := by decide +kernel
private theorem nf605_selected_134 : neutralNF602SelectedCheck (134:Fin 242) = true := by decide +kernel
private theorem nf605_selected_135 : neutralNF602SelectedCheck (135:Fin 242) = true := by decide +kernel
private theorem nf605_selected_136 : neutralNF602SelectedCheck (136:Fin 242) = true := by decide +kernel
private theorem nf605_selected_137 : neutralNF602SelectedCheck (137:Fin 242) = true := by decide +kernel
private theorem nf605_selected_138 : neutralNF602SelectedCheck (138:Fin 242) = true := by decide +kernel
private theorem nf605_selected_139 : neutralNF602SelectedCheck (139:Fin 242) = true := by decide +kernel
private theorem nf605_selected_140 : neutralNF602SelectedCheck (140:Fin 242) = true := by decide +kernel
private theorem nf605_selected_141 : neutralNF602SelectedCheck (141:Fin 242) = true := by decide +kernel
private theorem nf605_selected_142 : neutralNF602SelectedCheck (142:Fin 242) = true := by decide +kernel
private theorem nf605_selected_143 : neutralNF602SelectedCheck (143:Fin 242) = true := by decide +kernel
private theorem nf605_selected_144 : neutralNF602SelectedCheck (144:Fin 242) = true := by decide +kernel
private theorem nf605_selected_145 : neutralNF602SelectedCheck (145:Fin 242) = true := by decide +kernel
private theorem nf605_selected_146 : neutralNF602SelectedCheck (146:Fin 242) = true := by decide +kernel
private theorem nf605_selected_147 : neutralNF602SelectedCheck (147:Fin 242) = true := by decide +kernel
private theorem nf605_selected_148 : neutralNF602SelectedCheck (148:Fin 242) = true := by decide +kernel
private theorem nf605_selected_149 : neutralNF602SelectedCheck (149:Fin 242) = true := by decide +kernel
private theorem nf605_selected_150 : neutralNF602SelectedCheck (150:Fin 242) = true := by decide +kernel
private theorem nf605_selected_151 : neutralNF602SelectedCheck (151:Fin 242) = true := by decide +kernel
private theorem nf605_selected_152 : neutralNF602SelectedCheck (152:Fin 242) = true := by decide +kernel
private theorem nf605_selected_153 : neutralNF602SelectedCheck (153:Fin 242) = true := by decide +kernel
private theorem nf605_selected_154 : neutralNF602SelectedCheck (154:Fin 242) = true := by decide +kernel
private theorem nf605_selected_155 : neutralNF602SelectedCheck (155:Fin 242) = true := by decide +kernel
private theorem nf605_selected_156 : neutralNF602SelectedCheck (156:Fin 242) = true := by decide +kernel
private theorem nf605_selected_157 : neutralNF602SelectedCheck (157:Fin 242) = true := by decide +kernel
private theorem nf605_selected_158 : neutralNF602SelectedCheck (158:Fin 242) = true := by decide +kernel
private theorem nf605_selected_159 : neutralNF602SelectedCheck (159:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard4 (j : Fin 242) (hlo : 128 ≤ j.val) (hhi : j.val < 160) : neutralNF602SelectedCheck j = true := by
  by_cases h144 : j.val < 144
  ·
    by_cases h136 : j.val < 136
    ·
      by_cases h132 : j.val < 132
      ·
        by_cases h130 : j.val < 130
        ·
          by_cases h129 : j.val < 129
          ·
            have hj : j = (⟨128,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 128
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_128
          ·
            have hj : j = (⟨129,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 129
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_129
        ·
          by_cases h131 : j.val < 131
          ·
            have hj : j = (⟨130,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 130
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_130
          ·
            have hj : j = (⟨131,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 131
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_131
      ·
        by_cases h134 : j.val < 134
        ·
          by_cases h133 : j.val < 133
          ·
            have hj : j = (⟨132,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 132
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_132
          ·
            have hj : j = (⟨133,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 133
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_133
        ·
          by_cases h135 : j.val < 135
          ·
            have hj : j = (⟨134,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 134
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_134
          ·
            have hj : j = (⟨135,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 135
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_135
    ·
      by_cases h140 : j.val < 140
      ·
        by_cases h138 : j.val < 138
        ·
          by_cases h137 : j.val < 137
          ·
            have hj : j = (⟨136,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 136
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_136
          ·
            have hj : j = (⟨137,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 137
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_137
        ·
          by_cases h139 : j.val < 139
          ·
            have hj : j = (⟨138,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 138
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_138
          ·
            have hj : j = (⟨139,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 139
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_139
      ·
        by_cases h142 : j.val < 142
        ·
          by_cases h141 : j.val < 141
          ·
            have hj : j = (⟨140,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 140
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_140
          ·
            have hj : j = (⟨141,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 141
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_141
        ·
          by_cases h143 : j.val < 143
          ·
            have hj : j = (⟨142,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 142
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_142
          ·
            have hj : j = (⟨143,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 143
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_143
  ·
    by_cases h152 : j.val < 152
    ·
      by_cases h148 : j.val < 148
      ·
        by_cases h146 : j.val < 146
        ·
          by_cases h145 : j.val < 145
          ·
            have hj : j = (⟨144,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 144
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_144
          ·
            have hj : j = (⟨145,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 145
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_145
        ·
          by_cases h147 : j.val < 147
          ·
            have hj : j = (⟨146,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 146
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_146
          ·
            have hj : j = (⟨147,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 147
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_147
      ·
        by_cases h150 : j.val < 150
        ·
          by_cases h149 : j.val < 149
          ·
            have hj : j = (⟨148,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 148
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_148
          ·
            have hj : j = (⟨149,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 149
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_149
        ·
          by_cases h151 : j.val < 151
          ·
            have hj : j = (⟨150,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 150
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_150
          ·
            have hj : j = (⟨151,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 151
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_151
    ·
      by_cases h156 : j.val < 156
      ·
        by_cases h154 : j.val < 154
        ·
          by_cases h153 : j.val < 153
          ·
            have hj : j = (⟨152,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 152
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_152
          ·
            have hj : j = (⟨153,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 153
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_153
        ·
          by_cases h155 : j.val < 155
          ·
            have hj : j = (⟨154,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 154
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_154
          ·
            have hj : j = (⟨155,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 155
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_155
      ·
        by_cases h158 : j.val < 158
        ·
          by_cases h157 : j.val < 157
          ·
            have hj : j = (⟨156,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 156
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_156
          ·
            have hj : j = (⟨157,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 157
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_157
        ·
          by_cases h159 : j.val < 159
          ·
            have hj : j = (⟨158,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 158
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_158
          ·
            have hj : j = (⟨159,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 159
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_159

#print axioms neutralNF605SelectedShard4

end WeilDefect
