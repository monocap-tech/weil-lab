import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBooleanClosure

namespace WeilDefect

/-!
NF676: isolate the executable original H/V row checks from the
signed-carrier, integer payment and row transport theorems.
The definitions are unchanged from NF673/NF674, and no data-dependent
Boolean proposition is assumed or certified by this module.
-/

def neutralNF673LowerHEntryCheck
    (M : NF622Moments) (p : NF625PaymentData) : Bool :=
  (List.finRange 242).all (fun i =>
    (List.finRange 242).all (fun j =>
      if j.val ≤ i.val then neutralNF625EntryHCheck M p i j else true))

def neutralNF673CenterSymmetryCheck (p : NF625PaymentData) : Bool :=
  (List.finRange 242).all (fun i =>
    (List.finRange 242).all (fun j =>
      decide (p.H0 i j = p.H0 j i)))

def neutralNF673MixedVEntryCheck
    (M : NF622Moments) (p : NF625PaymentData) : Bool :=
  (List.finRange 242).all (fun i =>
    (List.finRange 4).all (neutralNF625EntryVCheck M p i))

/-- The source-specific reduced interval receipt: H lower triangle,
exact symmetry of historical rational H centers, and all four
historical V columns. Its independent truth remains to be checked. -/
def neutralNF673EntryCheck
    (M : NF622Moments) (p : NF625PaymentData) : Bool :=
  (neutralNF673LowerHEntryCheck M p &&
    neutralNF673CenterSymmetryCheck p) &&
    neutralNF673MixedVEntryCheck M p

def neutralNF674LowerRow (M : NF622Moments) (p : NF625PaymentData)
    (i : Fin 242) : Bool :=
  (List.finRange 242).all (fun j =>
    if j.val ≤ i.val then neutralNF625EntryHCheck M p i j else true)

def neutralNF674CenterRow (p : NF625PaymentData)
    (i : Fin 242) : Bool :=
  (List.finRange 242).all (fun j => decide (p.H0 i j = p.H0 j i))

def neutralNF674MixedRow (M : NF622Moments) (p : NF625PaymentData)
    (i : Fin 242) : Bool :=
  (List.finRange 4).all (neutralNF625EntryVCheck M p i)

/-- The total certified numerical receipt is implemented as one
bounded row per original physical source, not a monolithic 242×242
Boolean normal form. -/
def neutralNF674OriginalRowCheck (M : NF622Moments)
    (p : NF625PaymentData) (i : Fin 242) : Bool :=
  (neutralNF674LowerRow M p i &&
    neutralNF674CenterRow p i) &&
    neutralNF674MixedRow M p i

end WeilDefect
