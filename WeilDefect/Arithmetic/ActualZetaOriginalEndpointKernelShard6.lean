import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_192 : neutralNF602SelectedCheck (192:Fin 242) = true := by decide +kernel
private theorem nf605_selected_193 : neutralNF602SelectedCheck (193:Fin 242) = true := by decide +kernel
private theorem nf605_selected_194 : neutralNF602SelectedCheck (194:Fin 242) = true := by decide +kernel
private theorem nf605_selected_195 : neutralNF602SelectedCheck (195:Fin 242) = true := by decide +kernel
private theorem nf605_selected_196 : neutralNF602SelectedCheck (196:Fin 242) = true := by decide +kernel
private theorem nf605_selected_197 : neutralNF602SelectedCheck (197:Fin 242) = true := by decide +kernel
private theorem nf605_selected_198 : neutralNF602SelectedCheck (198:Fin 242) = true := by decide +kernel
private theorem nf605_selected_199 : neutralNF602SelectedCheck (199:Fin 242) = true := by decide +kernel
private theorem nf605_selected_200 : neutralNF602SelectedCheck (200:Fin 242) = true := by decide +kernel
private theorem nf605_selected_201 : neutralNF602SelectedCheck (201:Fin 242) = true := by decide +kernel
private theorem nf605_selected_202 : neutralNF602SelectedCheck (202:Fin 242) = true := by decide +kernel
private theorem nf605_selected_203 : neutralNF602SelectedCheck (203:Fin 242) = true := by decide +kernel
private theorem nf605_selected_204 : neutralNF602SelectedCheck (204:Fin 242) = true := by decide +kernel
private theorem nf605_selected_205 : neutralNF602SelectedCheck (205:Fin 242) = true := by decide +kernel
private theorem nf605_selected_206 : neutralNF602SelectedCheck (206:Fin 242) = true := by decide +kernel
private theorem nf605_selected_207 : neutralNF602SelectedCheck (207:Fin 242) = true := by decide +kernel
private theorem nf605_selected_208 : neutralNF602SelectedCheck (208:Fin 242) = true := by decide +kernel
private theorem nf605_selected_209 : neutralNF602SelectedCheck (209:Fin 242) = true := by decide +kernel
private theorem nf605_selected_210 : neutralNF602SelectedCheck (210:Fin 242) = true := by decide +kernel
private theorem nf605_selected_211 : neutralNF602SelectedCheck (211:Fin 242) = true := by decide +kernel
private theorem nf605_selected_212 : neutralNF602SelectedCheck (212:Fin 242) = true := by decide +kernel
private theorem nf605_selected_213 : neutralNF602SelectedCheck (213:Fin 242) = true := by decide +kernel
private theorem nf605_selected_214 : neutralNF602SelectedCheck (214:Fin 242) = true := by decide +kernel
private theorem nf605_selected_215 : neutralNF602SelectedCheck (215:Fin 242) = true := by decide +kernel
private theorem nf605_selected_216 : neutralNF602SelectedCheck (216:Fin 242) = true := by decide +kernel
private theorem nf605_selected_217 : neutralNF602SelectedCheck (217:Fin 242) = true := by decide +kernel
private theorem nf605_selected_218 : neutralNF602SelectedCheck (218:Fin 242) = true := by decide +kernel
private theorem nf605_selected_219 : neutralNF602SelectedCheck (219:Fin 242) = true := by decide +kernel
private theorem nf605_selected_220 : neutralNF602SelectedCheck (220:Fin 242) = true := by decide +kernel
private theorem nf605_selected_221 : neutralNF602SelectedCheck (221:Fin 242) = true := by decide +kernel
private theorem nf605_selected_222 : neutralNF602SelectedCheck (222:Fin 242) = true := by decide +kernel
private theorem nf605_selected_223 : neutralNF602SelectedCheck (223:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard6 (j : Fin 242) (hlo : 192 ≤ j.val) (hhi : j.val < 224) : neutralNF602SelectedCheck j = true := by
  by_cases h208 : j.val < 208
  ·
    by_cases h200 : j.val < 200
    ·
      by_cases h196 : j.val < 196
      ·
        by_cases h194 : j.val < 194
        ·
          by_cases h193 : j.val < 193
          ·
            have hj : j = (⟨192,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 192
              omega)
            rw [hj]
            exact nf605_selected_192
          ·
            have hj : j = (⟨193,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 193
              omega)
            rw [hj]
            exact nf605_selected_193
        ·
          by_cases h195 : j.val < 195
          ·
            have hj : j = (⟨194,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 194
              omega)
            rw [hj]
            exact nf605_selected_194
          ·
            have hj : j = (⟨195,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 195
              omega)
            rw [hj]
            exact nf605_selected_195
      ·
        by_cases h198 : j.val < 198
        ·
          by_cases h197 : j.val < 197
          ·
            have hj : j = (⟨196,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 196
              omega)
            rw [hj]
            exact nf605_selected_196
          ·
            have hj : j = (⟨197,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 197
              omega)
            rw [hj]
            exact nf605_selected_197
        ·
          by_cases h199 : j.val < 199
          ·
            have hj : j = (⟨198,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 198
              omega)
            rw [hj]
            exact nf605_selected_198
          ·
            have hj : j = (⟨199,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 199
              omega)
            rw [hj]
            exact nf605_selected_199
    ·
      by_cases h204 : j.val < 204
      ·
        by_cases h202 : j.val < 202
        ·
          by_cases h201 : j.val < 201
          ·
            have hj : j = (⟨200,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 200
              omega)
            rw [hj]
            exact nf605_selected_200
          ·
            have hj : j = (⟨201,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 201
              omega)
            rw [hj]
            exact nf605_selected_201
        ·
          by_cases h203 : j.val < 203
          ·
            have hj : j = (⟨202,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 202
              omega)
            rw [hj]
            exact nf605_selected_202
          ·
            have hj : j = (⟨203,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 203
              omega)
            rw [hj]
            exact nf605_selected_203
      ·
        by_cases h206 : j.val < 206
        ·
          by_cases h205 : j.val < 205
          ·
            have hj : j = (⟨204,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 204
              omega)
            rw [hj]
            exact nf605_selected_204
          ·
            have hj : j = (⟨205,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 205
              omega)
            rw [hj]
            exact nf605_selected_205
        ·
          by_cases h207 : j.val < 207
          ·
            have hj : j = (⟨206,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 206
              omega)
            rw [hj]
            exact nf605_selected_206
          ·
            have hj : j = (⟨207,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 207
              omega)
            rw [hj]
            exact nf605_selected_207
  ·
    by_cases h216 : j.val < 216
    ·
      by_cases h212 : j.val < 212
      ·
        by_cases h210 : j.val < 210
        ·
          by_cases h209 : j.val < 209
          ·
            have hj : j = (⟨208,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 208
              omega)
            rw [hj]
            exact nf605_selected_208
          ·
            have hj : j = (⟨209,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 209
              omega)
            rw [hj]
            exact nf605_selected_209
        ·
          by_cases h211 : j.val < 211
          ·
            have hj : j = (⟨210,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 210
              omega)
            rw [hj]
            exact nf605_selected_210
          ·
            have hj : j = (⟨211,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 211
              omega)
            rw [hj]
            exact nf605_selected_211
      ·
        by_cases h214 : j.val < 214
        ·
          by_cases h213 : j.val < 213
          ·
            have hj : j = (⟨212,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 212
              omega)
            rw [hj]
            exact nf605_selected_212
          ·
            have hj : j = (⟨213,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 213
              omega)
            rw [hj]
            exact nf605_selected_213
        ·
          by_cases h215 : j.val < 215
          ·
            have hj : j = (⟨214,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 214
              omega)
            rw [hj]
            exact nf605_selected_214
          ·
            have hj : j = (⟨215,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 215
              omega)
            rw [hj]
            exact nf605_selected_215
    ·
      by_cases h220 : j.val < 220
      ·
        by_cases h218 : j.val < 218
        ·
          by_cases h217 : j.val < 217
          ·
            have hj : j = (⟨216,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 216
              omega)
            rw [hj]
            exact nf605_selected_216
          ·
            have hj : j = (⟨217,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 217
              omega)
            rw [hj]
            exact nf605_selected_217
        ·
          by_cases h219 : j.val < 219
          ·
            have hj : j = (⟨218,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 218
              omega)
            rw [hj]
            exact nf605_selected_218
          ·
            have hj : j = (⟨219,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 219
              omega)
            rw [hj]
            exact nf605_selected_219
      ·
        by_cases h222 : j.val < 222
        ·
          by_cases h221 : j.val < 221
          ·
            have hj : j = (⟨220,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 220
              omega)
            rw [hj]
            exact nf605_selected_220
          ·
            have hj : j = (⟨221,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 221
              omega)
            rw [hj]
            exact nf605_selected_221
        ·
          by_cases h223 : j.val < 223
          ·
            have hj : j = (⟨222,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 222
              omega)
            rw [hj]
            exact nf605_selected_222
          ·
            have hj : j = (⟨223,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 223
              omega)
            rw [hj]
            exact nf605_selected_223

#print axioms neutralNF605SelectedShard6

end WeilDefect
