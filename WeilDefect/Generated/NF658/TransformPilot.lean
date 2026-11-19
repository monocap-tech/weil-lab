import WeilDefect.Generated.NF658.WitnessData

namespace WeilDefect

/-! NF658: two genuine transformed matrix coefficient gates.
They are not definitions of positivity; the calculated entries are
expanded from the 15-by-15 fixed integer K,C,E witness matrices. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

def nf658Get (a : Array (Array ℤ)) (i j : Fin 15) : ℤ :=
  (a[i.val]!).getD j.val 0

def nf658TransformedCenter (i j : Fin 15) : ℤ :=
  ∑ p : Fin 15, ∑ q : Fin 15,
    nf658Get nf658Kints i p * nf658Get nf658Kints j q *
      nf658Get nf658Centers p q

def nf658TransformedRadius (i j : Fin 15) : ℤ :=
  ∑ p : Fin 15, ∑ q : Fin 15,
    |nf658Get nf658Kints i p * nf658Get nf658Kints j q| *
      nf658Get nf658Radii p q

theorem nf658FirstCenterGate :
    nf658TransformedCenter 0 0 =
      963650588534595603228554970828031809219155904982945144301490058400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 := by
  decide +kernel

theorem nf658FirstRadiusGate :
    nf658TransformedRadius 0 0 =
      100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 := by
  decide +kernel

theorem nf658PoleCenterGate :
    nf658TransformedCenter 14 14 =
      494206527065547785715918992509177881788981222281686925696311926382610845016444783996866888840121655109141343950778635087139291379439311696630596121 := by
  decide +kernel

theorem nf658PoleRadiusGate :
    nf658TransformedRadius 14 14 =
      10548298217110413776782671990280314933492250670889478207367191704762579122039329902202119641647012133217988200768050450871406245904 := by
  decide +kernel

#print axioms nf658PoleCenterGate
#print axioms nf658PoleRadiusGate

end WeilDefect
