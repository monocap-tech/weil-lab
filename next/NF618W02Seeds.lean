import WeilDefect.Arithmetic.NF618W02RootAttachmentCandidate
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFastMomentTable

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

def nf618W02Pi : NF591Ball := neutralNF592PiBall neutralNF616Q neutralNF616AtanN
def nf618W02Seed : NF591Rect := neutralNF593Phase nf618W02Pi (1/1408) neutralNF616Q neutralNF616ExpN
def nf618W02Quarter : NF591Rect := ⟨⟨0,0⟩,⟨1,0⟩⟩
def nf618W02Real (h : ℚ) : NF591Rect := neutralNF621RealEndpoint h neutralNF616Q neutralNF616ExpN

theorem nf618W02Pi_sound : nf618W02Pi.Contains Real.pi := neutralNF616Pi_sound

theorem nf618W02Seed_sound : nf618W02Seed.Contains (nf618HybridPhase (1/1408)) := by
  unfold nf618W02Seed
  rw [neutralNF593Phase_eq]
  exact neutralNF592PhaseBall_sound nf618W02Pi nf618W02Pi_sound (1/1408)
    neutralNF616Q neutralNF616ExpN neutralNF616Q_pos (by decide +kernel) neutralNF616ExpFee

theorem nf618W02Quarter_sound : nf618W02Quarter.Contains (nf618HybridPhase (5/22)) := by
  have he : nf618HybridPhase (5/22) = Complex.I := by
    unfold nf618HybridPhase
    rw [show Complex.I * ((2*Real.pi*((5/22:ℚ):ℝ):ℝ):ℂ) * (11/10) =
        (Real.pi:ℂ)/2 * Complex.I by push_cast; ring]
    first | exact Complex.exp_pi_div_two_mul_I | simp [Complex.exp_mul_I, Complex.cos_pi_div_two, Complex.sin_pi_div_two]
  rw [he]
  norm_num [nf618W02Quarter, NF591Rect.Contains, NF591Ball.Contains]

theorem nf618W02Real_sound (h : ℚ) (hh : |h| ≤ 1) :
    (nf618W02Real h).Contains (Complex.exp ((h:ℂ)*(11/10))) := by
  unfold nf618W02Real
  rw [neutralNF621RealEndpoint_eq]
  exact neutralNF615RealEndpoint_sound h hh neutralNF616Q neutralNF616ExpN
    neutralNF616Q_pos (by decide +kernel) neutralNF616ExpFee

#print axioms nf618W02Pi_sound
#print axioms nf618W02Seed_sound
#print axioms nf618W02Quarter_sound
#print axioms nf618W02Real_sound
end WeilDefect
