import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_160 : neutralNF602SelectedCheck (160:Fin 242) = true := by decide +kernel
private theorem nf605_selected_161 : neutralNF602SelectedCheck (161:Fin 242) = true := by decide +kernel
private theorem nf605_selected_162 : neutralNF602SelectedCheck (162:Fin 242) = true := by decide +kernel
private theorem nf605_selected_163 : neutralNF602SelectedCheck (163:Fin 242) = true := by decide +kernel
private theorem nf605_selected_164 : neutralNF602SelectedCheck (164:Fin 242) = true := by decide +kernel
private theorem nf605_selected_165 : neutralNF602SelectedCheck (165:Fin 242) = true := by decide +kernel
private theorem nf605_selected_166 : neutralNF602SelectedCheck (166:Fin 242) = true := by decide +kernel
private theorem nf605_selected_167 : neutralNF602SelectedCheck (167:Fin 242) = true := by decide +kernel
private theorem nf605_selected_168 : neutralNF602SelectedCheck (168:Fin 242) = true := by decide +kernel
private theorem nf605_selected_169 : neutralNF602SelectedCheck (169:Fin 242) = true := by decide +kernel
private theorem nf605_selected_170 : neutralNF602SelectedCheck (170:Fin 242) = true := by decide +kernel
private theorem nf605_selected_171 : neutralNF602SelectedCheck (171:Fin 242) = true := by decide +kernel
private theorem nf605_selected_172 : neutralNF602SelectedCheck (172:Fin 242) = true := by decide +kernel
private theorem nf605_selected_173 : neutralNF602SelectedCheck (173:Fin 242) = true := by decide +kernel
private theorem nf605_selected_174 : neutralNF602SelectedCheck (174:Fin 242) = true := by decide +kernel
private theorem nf605_selected_175 : neutralNF602SelectedCheck (175:Fin 242) = true := by decide +kernel
private theorem nf605_selected_176 : neutralNF602SelectedCheck (176:Fin 242) = true := by decide +kernel
private theorem nf605_selected_177 : neutralNF602SelectedCheck (177:Fin 242) = true := by decide +kernel
private theorem nf605_selected_178 : neutralNF602SelectedCheck (178:Fin 242) = true := by decide +kernel
private theorem nf605_selected_179 : neutralNF602SelectedCheck (179:Fin 242) = true := by decide +kernel
private theorem nf605_selected_180 : neutralNF602SelectedCheck (180:Fin 242) = true := by decide +kernel
private theorem nf605_selected_181 : neutralNF602SelectedCheck (181:Fin 242) = true := by decide +kernel
private theorem nf605_selected_182 : neutralNF602SelectedCheck (182:Fin 242) = true := by decide +kernel
private theorem nf605_selected_183 : neutralNF602SelectedCheck (183:Fin 242) = true := by decide +kernel
private theorem nf605_selected_184 : neutralNF602SelectedCheck (184:Fin 242) = true := by decide +kernel
private theorem nf605_selected_185 : neutralNF602SelectedCheck (185:Fin 242) = true := by decide +kernel
private theorem nf605_selected_186 : neutralNF602SelectedCheck (186:Fin 242) = true := by decide +kernel
private theorem nf605_selected_187 : neutralNF602SelectedCheck (187:Fin 242) = true := by decide +kernel
private theorem nf605_selected_188 : neutralNF602SelectedCheck (188:Fin 242) = true := by decide +kernel
private theorem nf605_selected_189 : neutralNF602SelectedCheck (189:Fin 242) = true := by decide +kernel
private theorem nf605_selected_190 : neutralNF602SelectedCheck (190:Fin 242) = true := by decide +kernel
private theorem nf605_selected_191 : neutralNF602SelectedCheck (191:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard5 (j : Fin 242) (hlo : 160 ≤ j.val) (hhi : j.val < 192) : neutralNF602SelectedCheck j = true := by
  by_cases h176 : j.val < 176
  ·
    by_cases h168 : j.val < 168
    ·
      by_cases h164 : j.val < 164
      ·
        by_cases h162 : j.val < 162
        ·
          by_cases h161 : j.val < 161
          ·
            have hj : j = (⟨160,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 160
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_160
          ·
            have hj : j = (⟨161,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 161
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_161
        ·
          by_cases h163 : j.val < 163
          ·
            have hj : j = (⟨162,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 162
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_162
          ·
            have hj : j = (⟨163,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 163
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_163
      ·
        by_cases h166 : j.val < 166
        ·
          by_cases h165 : j.val < 165
          ·
            have hj : j = (⟨164,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 164
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_164
          ·
            have hj : j = (⟨165,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 165
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_165
        ·
          by_cases h167 : j.val < 167
          ·
            have hj : j = (⟨166,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 166
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_166
          ·
            have hj : j = (⟨167,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 167
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_167
    ·
      by_cases h172 : j.val < 172
      ·
        by_cases h170 : j.val < 170
        ·
          by_cases h169 : j.val < 169
          ·
            have hj : j = (⟨168,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 168
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_168
          ·
            have hj : j = (⟨169,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 169
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_169
        ·
          by_cases h171 : j.val < 171
          ·
            have hj : j = (⟨170,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 170
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_170
          ·
            have hj : j = (⟨171,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 171
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_171
      ·
        by_cases h174 : j.val < 174
        ·
          by_cases h173 : j.val < 173
          ·
            have hj : j = (⟨172,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 172
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_172
          ·
            have hj : j = (⟨173,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 173
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_173
        ·
          by_cases h175 : j.val < 175
          ·
            have hj : j = (⟨174,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 174
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_174
          ·
            have hj : j = (⟨175,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 175
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_175
  ·
    by_cases h184 : j.val < 184
    ·
      by_cases h180 : j.val < 180
      ·
        by_cases h178 : j.val < 178
        ·
          by_cases h177 : j.val < 177
          ·
            have hj : j = (⟨176,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 176
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_176
          ·
            have hj : j = (⟨177,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 177
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_177
        ·
          by_cases h179 : j.val < 179
          ·
            have hj : j = (⟨178,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 178
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_178
          ·
            have hj : j = (⟨179,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 179
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_179
      ·
        by_cases h182 : j.val < 182
        ·
          by_cases h181 : j.val < 181
          ·
            have hj : j = (⟨180,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 180
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_180
          ·
            have hj : j = (⟨181,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 181
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_181
        ·
          by_cases h183 : j.val < 183
          ·
            have hj : j = (⟨182,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 182
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_182
          ·
            have hj : j = (⟨183,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 183
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_183
    ·
      by_cases h188 : j.val < 188
      ·
        by_cases h186 : j.val < 186
        ·
          by_cases h185 : j.val < 185
          ·
            have hj : j = (⟨184,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 184
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_184
          ·
            have hj : j = (⟨185,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 185
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_185
        ·
          by_cases h187 : j.val < 187
          ·
            have hj : j = (⟨186,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 186
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_186
          ·
            have hj : j = (⟨187,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 187
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_187
      ·
        by_cases h190 : j.val < 190
        ·
          by_cases h189 : j.val < 189
          ·
            have hj : j = (⟨188,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 188
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_188
          ·
            have hj : j = (⟨189,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 189
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_189
        ·
          by_cases h191 : j.val < 191
          ·
            have hj : j = (⟨190,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 190
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_190
          ·
            have hj : j = (⟨191,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 191
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_191

#print axioms neutralNF605SelectedShard5

end WeilDefect
