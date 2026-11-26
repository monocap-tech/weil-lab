import WeilDefect.Arithmetic.ActualZetaIV141OriginalBKDictionary
import WeilDefect.Arithmetic.ActualZetaIV142BKData

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap

/-- The exact integer arrays generated from the authenticated BK archive.
These are the unprojected TN columns; no numerical approximation of
trigonometric values or projection coefficients is introduced here. -/
def neutralIV142EvenRaw (i : Fin 121) : RealComplexL2 :=
  neutralIV141RawColumn (m := 5081) false
    (fun j => BKData.evenMode[j.val]!.toNat)
    (fun j => BKData.evenWeight[j.val]!.toNat)
    (fun j l => BKData.evenE[j.val*121+l.val]!) i

def neutralIV142OddRaw (i : Fin 119) : RealComplexL2 :=
  neutralIV141RawColumn (m := 5143) true
    (fun j => BKData.oddMode[j.val]!.toNat)
    (fun j => BKData.oddWeight[j.val]!.toNat)
    (fun j l => BKData.oddE[j.val*119+l.val]!) i

def neutralIV142RawBank (i : Fin 240) : RealComplexL2 :=
  if h : i.val < 121 then neutralIV142EvenRaw ⟨i.val,h⟩
  else neutralIV142OddRaw ⟨i.val-121,by omega⟩

def neutralIV142ProjectedBank (i : Fin 240) : RealComplexL2 :=
  neutralIV141ProjectedColumn (decide (121 ≤ i.val)) (neutralIV142RawBank i)

theorem neutralIV142Bank_pair (i : Fin 240) (f : RealComplexL2)
    (hp : sourceWindowMoment 2 (1/2) f = 0)
    (hm : sourceWindowMoment 2 (-(1/2)) f = 0) :
    inner ℂ (neutralIV142ProjectedBank i) f =
      inner ℂ (neutralIV142RawBank i) f :=
  neutralIV141Projected_pair _ _ f hp hm

theorem neutralIV142Bank_null_iff (f : RealComplexL2)
    (hp : sourceWindowMoment 2 (1/2) f = 0)
    (hm : sourceWindowMoment 2 (-(1/2)) f = 0) :
    (∀ i : Fin 240, inner ℂ (neutralIV142ProjectedBank i) f = 0) ↔
      (∀ i : Fin 240, inner ℂ (neutralIV142RawBank i) f = 0) := by
  simp only [neutralIV142Bank_pair _ f hp hm]

theorem neutralIV142Head_dim_le (k : ℕ) (hk : 0 < k) :
    Module.finrank ℂ (LinearMap.range
      ((neutralIV139Map k hk neutralIV142RawBank).comp (neutralIV129Complement k hk).subtype)) ≤
      242+k := by
  simpa using neutralIV139Head_dim_le k hk neutralIV142RawBank

#print axioms neutralIV142Bank_pair
#print axioms neutralIV142Bank_null_iff
#print axioms neutralIV142Head_dim_le

end
end WeilDefect
