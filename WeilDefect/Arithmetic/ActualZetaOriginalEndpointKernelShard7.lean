import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptChecks

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! Promote the individual NF603 kernel-only CI checks. All data and
arithmetic definitions are unchanged. The indexed theorem uses only
these local theorems and finite integer case distinctions. -/

private theorem nf605_selected_224 : neutralNF602SelectedCheck (224:Fin 242) = true := by decide +kernel
private theorem nf605_selected_225 : neutralNF602SelectedCheck (225:Fin 242) = true := by decide +kernel
private theorem nf605_selected_226 : neutralNF602SelectedCheck (226:Fin 242) = true := by decide +kernel
private theorem nf605_selected_227 : neutralNF602SelectedCheck (227:Fin 242) = true := by decide +kernel
private theorem nf605_selected_228 : neutralNF602SelectedCheck (228:Fin 242) = true := by decide +kernel
private theorem nf605_selected_229 : neutralNF602SelectedCheck (229:Fin 242) = true := by decide +kernel
private theorem nf605_selected_230 : neutralNF602SelectedCheck (230:Fin 242) = true := by decide +kernel
private theorem nf605_selected_231 : neutralNF602SelectedCheck (231:Fin 242) = true := by decide +kernel
private theorem nf605_selected_232 : neutralNF602SelectedCheck (232:Fin 242) = true := by decide +kernel
private theorem nf605_selected_233 : neutralNF602SelectedCheck (233:Fin 242) = true := by decide +kernel
private theorem nf605_selected_234 : neutralNF602SelectedCheck (234:Fin 242) = true := by decide +kernel
private theorem nf605_selected_235 : neutralNF602SelectedCheck (235:Fin 242) = true := by decide +kernel
private theorem nf605_selected_236 : neutralNF602SelectedCheck (236:Fin 242) = true := by decide +kernel
private theorem nf605_selected_237 : neutralNF602SelectedCheck (237:Fin 242) = true := by decide +kernel
private theorem nf605_selected_238 : neutralNF602SelectedCheck (238:Fin 242) = true := by decide +kernel
private theorem nf605_selected_239 : neutralNF602SelectedCheck (239:Fin 242) = true := by decide +kernel
private theorem nf605_selected_240 : neutralNF602SelectedCheck (240:Fin 242) = true := by decide +kernel
private theorem nf605_selected_241 : neutralNF602SelectedCheck (241:Fin 242) = true := by decide +kernel

theorem neutralNF605SelectedShard7 (j : Fin 242) (hlo : 224 ≤ j.val) (hhi : j.val < 242) : neutralNF602SelectedCheck j = true := by
  by_cases h233 : j.val < 233
  ·
    by_cases h228 : j.val < 228
    ·
      by_cases h226 : j.val < 226
      ·
        by_cases h225 : j.val < 225
        ·
          have hj : j = (⟨224,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 224
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_224
        ·
          have hj : j = (⟨225,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 225
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_225
      ·
        by_cases h227 : j.val < 227
        ·
          have hj : j = (⟨226,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 226
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_226
        ·
          have hj : j = (⟨227,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 227
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_227
    ·
      by_cases h230 : j.val < 230
      ·
        by_cases h229 : j.val < 229
        ·
          have hj : j = (⟨228,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 228
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_228
        ·
          have hj : j = (⟨229,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 229
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_229
      ·
        by_cases h231 : j.val < 231
        ·
          have hj : j = (⟨230,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 230
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_230
        ·
          by_cases h232 : j.val < 232
          ·
            have hj : j = (⟨231,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 231
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_231
          ·
            have hj : j = (⟨232,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 232
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_232
  ·
    by_cases h237 : j.val < 237
    ·
      by_cases h235 : j.val < 235
      ·
        by_cases h234 : j.val < 234
        ·
          have hj : j = (⟨233,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 233
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_233
        ·
          have hj : j = (⟨234,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 234
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_234
      ·
        by_cases h236 : j.val < 236
        ·
          have hj : j = (⟨235,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 235
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_235
        ·
          have hj : j = (⟨236,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 236
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_236
    ·
      by_cases h239 : j.val < 239
      ·
        by_cases h238 : j.val < 238
        ·
          have hj : j = (⟨237,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 237
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_237
        ·
          have hj : j = (⟨238,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 238
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_238
      ·
        by_cases h240 : j.val < 240
        ·
          have hj : j = (⟨239,by decide⟩ : Fin 242) := Fin.ext (by
            change j.val = 239
            omega)
          exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_239
        ·
          by_cases h241 : j.val < 241
          ·
            have hj : j = (⟨240,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 240
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_240
          ·
            have hj : j = (⟨241,by decide⟩ : Fin 242) := Fin.ext (by
              change j.val = 241
              omega)
            exact (congrArg neutralNF602SelectedCheck hj).trans nf605_selected_241

#print axioms neutralNF605SelectedShard7

end WeilDefect
