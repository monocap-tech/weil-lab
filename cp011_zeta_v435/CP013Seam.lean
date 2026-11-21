module

public import CP013RSOnly
public import Zeta.Zeros.Certificates.EulerMaclaurin.Batch0001

/-!
CP013: preserve original zero-method provenance at the source seam.
The original first 52 Euler zero intervals and the newly reconstructed
original 1,747,950 RS-only batch form a certified 1,748,002 interval
bundle. The proof below cites original source BATCH certificates ONLY.
It does NOT assert that an external source row's decimals identify an
individual interval in Classical.choose's abstract source bundle.

This is a kernel SOURCE CANDIDATE; actual v4.35 build/axiom receipt pending.
-/ 

@[expose] public section

namespace CP013Seam

open Zeta.Certificates

/-- The first 52 original low-height Euler certificates, ending 149.500. -/
theorem first52Euler :
    BatchSpec 52 1000 1000 149500 1000 :=
  Zeta.Certificates.EulerMaclaurin.Batch0001.batch

/-- All 1,747,950 original high-height Riemann-Siegel zero certificates,
beginning at exactly 149.500, split away from the Euler method. -/
theorem allRS :
    BatchSpec 1747950 149500 1000 1000449286 1000 :=
  CP013RSOnly.all_original_RS_only

/-- Reassemble original certified zero intervals using the EXPLICIT
52-Euler / 1,747,950-RS seam. The two source intervals meet exactly at
149.500; the original BatchSpec.append proves the seam and count. -/
theorem allOriginalSplit :
    BatchSpec 1748002 1000 1000 1000449286 1000 :=
  BatchSpec.append first52Euler allRS rfl rfl rfl

/-- The certified original high-height RS-only bundle count is exact.
This is not a new zero enumeration and makes no source-row index claim. -/
theorem rsOnlyLength :
    allRS.bundle.intervals.length = 1747950 :=
  allRS.bundle_length

/-- The certified original first-52 low-height Euler bundle count is exact. -/
theorem eulerOnlyLength :
    first52Euler.bundle.intervals.length = 52 :=
  first52Euler.bundle_length

end CP013Seam

#print axioms CP013Seam.allOriginalSplit
#print axioms CP013Seam.rsOnlyLength
#print axioms CP013Seam.eulerOnlyLength
