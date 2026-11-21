module

public import Zeta.Zeros.Certificates.Groups.Level1.Group0001
import Zeta.Zeros.Certificates.Groups.Level1.Group0002
import Zeta.Zeros.Certificates.Groups.Level1.Group0003
import Zeta.Zeros.Certificates.Groups.Level1.Group0004
import Zeta.Zeros.Certificates.Groups.Level1.Group0005
import Zeta.Zeros.Certificates.Groups.Level1.Group0006
import Zeta.Zeros.Certificates.Groups.Level1.Group0007
import Zeta.Zeros.Certificates.Groups.Level1.Group0008
import Zeta.Zeros.Certificates.Groups.Level1.Group0009
import Zeta.Zeros.Certificates.Groups.Level1.Group0010
import Zeta.Zeros.Certificates.Groups.Level1.Group0011
import Zeta.Zeros.Certificates.Groups.Level1.Group0012
import Zeta.Zeros.Certificates.Groups.Level1.Group0013
import Zeta.Zeros.Certificates.Groups.Level1.Group0014
import Zeta.Zeros.Certificates.Groups.Level1.Group0015
import Zeta.Zeros.Certificates.Groups.Level1.Group0016
import Zeta.Zeros.Certificates.Groups.Level1.Group0017
import Zeta.Zeros.Certificates.Groups.Level1.Group0018
import Zeta.Zeros.Certificates.Groups.Level1.Group0019
import Zeta.Zeros.Certificates.Groups.Level1.Group0020
import Zeta.Zeros.Certificates.Groups.Level1.Group0021
import Zeta.Zeros.Certificates.Groups.Level1.Group0022
import Zeta.Zeros.Certificates.Groups.Level1.Group0023
import Zeta.Zeros.Certificates.Groups.Level1.Group0024
import Zeta.Zeros.Certificates.Groups.Level1.Group0025
import Zeta.Zeros.Certificates.Groups.Level1.Group0026
import Zeta.Zeros.Certificates.Groups.Level1.Group0027
import Zeta.Zeros.Certificates.Groups.Level1.Group0028
import Zeta.Zeros.Certificates.Groups.Level1.Group0029
import Zeta.Zeros.Certificates.Groups.Level1.Group0030
import Zeta.Zeros.Certificates.Groups.Level1.Group0031
import Zeta.Zeros.Certificates.Groups.Level1.Group0032
import Zeta.Zeros.Certificates.Groups.Level1.Group0033
import Zeta.Zeros.Certificates.Groups.Level1.Group0034
import Zeta.Zeros.Certificates.Groups.Level1.Group0035
import Zeta.Zeros.Certificates.Groups.Level1.Group0036
import Zeta.Zeros.Certificates.Groups.Level1.Group0037
import Zeta.Zeros.Certificates.Groups.Level1.Group0038
import Zeta.Zeros.Certificates.Groups.Level1.Group0039
import Zeta.Zeros.Certificates.Groups.Level1.Group0040
import Zeta.Zeros.Certificates.Groups.Level1.Group0041
import Zeta.Zeros.Certificates.Groups.Level1.Group0042
import Zeta.Zeros.Certificates.Groups.Level1.Group0043
import Zeta.Zeros.Certificates.Groups.Level1.Group0044
import Zeta.Zeros.Certificates.Groups.Level1.Group0045
import Zeta.Zeros.Certificates.Groups.Level1.Group0046
import Zeta.Zeros.Certificates.Groups.Level1.Group0047
import Zeta.Zeros.Certificates.Groups.Level1.Group0048
import Zeta.Zeros.Certificates.Groups.Level1.Group0049
import Zeta.Zeros.Certificates.Groups.Level1.Group0050
import Zeta.Zeros.Certificates.Groups.Level1.Group0051
import Zeta.Zeros.Certificates.Groups.Level1.Group0052
import Zeta.Zeros.Certificates.Groups.Level1.Group0053
import Zeta.Zeros.Certificates.Groups.Level1.Group0054
import Zeta.Zeros.Certificates.Groups.Level1.Group0055
import Zeta.Zeros.Certificates.Groups.Level1.Group0056
import Zeta.Zeros.Certificates.Groups.Level1.Group0057
import Zeta.Zeros.Certificates.Groups.Level1.Group0058
import Zeta.Zeros.Certificates.Groups.Level1.Group0059
import Zeta.Zeros.Certificates.Groups.Level1.Group0060
import Zeta.Zeros.Certificates.Groups.Level1.Group0061
import Zeta.Zeros.Certificates.Groups.Level1.Group0062
import Zeta.Zeros.Certificates.Groups.Level1.Group0063
import Zeta.Zeros.Certificates.Groups.Level1.Group0064
import Zeta.Zeros.Certificates.Groups.Level1.Group0065
import Zeta.Zeros.Certificates.Groups.Level1.Group0066
import Zeta.Zeros.Certificates.Groups.Level1.Group0067
import Zeta.Zeros.Certificates.Groups.Level1.Group0068
import Zeta.Zeros.Certificates.Groups.Level1.Group0069
import Zeta.Zeros.Certificates.Groups.Level1.Group0070

/-!
CP013 original-source RS-ONLY certificate reconstruction.
Upstream frozen smmercuri/zeta 1e6 original SHA:
c06b4e13d9c847e50a32c3d738271cbad62ae9f3.
Reconstructed by source-signature audit of group0001 (Git blob
12263d2f09d5a69c489c29c63940829e2c7211dc)
and Certificates.lean (Git blob
54fce07cbc5bf0913ceccb108cbf73f1227857c0).

Uses ONLY the original already-certified, imported individual RS batch
theorems and group2..70 theorems; NO re-evaluation of Hardy Z or
invented numerical source intervals. There are 1,747,950 RS roots in
their own certified ordered bundle starting at 149.5 and ending at
1,000,449.286. This is a source PROOF CANDIDATE until ACTUAL Lean
v4.35 kernel .olean and axiom receipts pass; it is not a refined roster.
-/

@[expose] public section
namespace CP013RSOnly
open Zeta.Certificates

/-- First 200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0001 : BatchSpec 200 149500 1000 474603 1000 :=
  Zeta.Certificates.RiemannSiegel.Batch0001.batch

/-- First 400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0002 : BatchSpec 400 149500 1000 748976 1000 :=
  BatchSpec.append upToRS0001 Zeta.Certificates.RiemannSiegel.Batch0002.batch rfl rfl rfl

/-- First 600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0003 : BatchSpec 600 149500 1000 1004192 1000 :=
  BatchSpec.append upToRS0002 Zeta.Certificates.RiemannSiegel.Batch0003.batch rfl rfl rfl

/-- First 800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0004 : BatchSpec 800 149500 1000 1246504 1000 :=
  BatchSpec.append upToRS0003 Zeta.Certificates.RiemannSiegel.Batch0004.batch rfl rfl rfl

/-- First 1000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0005 : BatchSpec 1000 149500 1000 1480141 1000 :=
  BatchSpec.append upToRS0004 Zeta.Certificates.RiemannSiegel.Batch0005.batch rfl rfl rfl

/-- First 1200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0006 : BatchSpec 1200 149500 1000 1706928 1000 :=
  BatchSpec.append upToRS0005 Zeta.Certificates.RiemannSiegel.Batch0006.batch rfl rfl rfl

/-- First 1400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0007 : BatchSpec 1400 149500 1000 1928919 1000 :=
  BatchSpec.append upToRS0006 Zeta.Certificates.RiemannSiegel.Batch0007.batch rfl rfl rfl

/-- First 1600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0008 : BatchSpec 1600 149500 1000 2146286 1000 :=
  BatchSpec.append upToRS0007 Zeta.Certificates.RiemannSiegel.Batch0008.batch rfl rfl rfl

/-- First 1800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0009 : BatchSpec 1800 149500 1000 2359934 1000 :=
  BatchSpec.append upToRS0008 Zeta.Certificates.RiemannSiegel.Batch0009.batch rfl rfl rfl

/-- First 2000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0010 : BatchSpec 2000 149500 1000 2570361 1000 :=
  BatchSpec.append upToRS0009 Zeta.Certificates.RiemannSiegel.Batch0010.batch rfl rfl rfl

/-- First 2200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0011 : BatchSpec 2200 149500 1000 2777958 1000 :=
  BatchSpec.append upToRS0010 Zeta.Certificates.RiemannSiegel.Batch0011.batch rfl rfl rfl

/-- First 2400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0012 : BatchSpec 2400 149500 1000 2983035 1000 :=
  BatchSpec.append upToRS0011 Zeta.Certificates.RiemannSiegel.Batch0012.batch rfl rfl rfl

/-- First 2600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0013 : BatchSpec 2600 149500 1000 3185847 1000 :=
  BatchSpec.append upToRS0012 Zeta.Certificates.RiemannSiegel.Batch0013.batch rfl rfl rfl

/-- First 2800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0014 : BatchSpec 2800 149500 1000 3386605 1000 :=
  BatchSpec.append upToRS0013 Zeta.Certificates.RiemannSiegel.Batch0014.batch rfl rfl rfl

/-- First 3000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0015 : BatchSpec 3000 149500 1000 3585487 1000 :=
  BatchSpec.append upToRS0014 Zeta.Certificates.RiemannSiegel.Batch0015.batch rfl rfl rfl

/-- First 3200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0016 : BatchSpec 3200 149500 1000 3782644 1000 :=
  BatchSpec.append upToRS0015 Zeta.Certificates.RiemannSiegel.Batch0016.batch rfl rfl rfl

/-- First 3400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0017 : BatchSpec 3400 149500 1000 3977721 1000 :=
  BatchSpec.append upToRS0016 Zeta.Certificates.RiemannSiegel.Batch0017.batch rfl rfl rfl

/-- First 3600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0018 : BatchSpec 3600 149500 1000 4172292 1000 :=
  BatchSpec.append upToRS0017 Zeta.Certificates.RiemannSiegel.Batch0018.batch rfl rfl rfl

/-- First 3800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0019 : BatchSpec 3800 149500 1000 4364995 1000 :=
  BatchSpec.append upToRS0018 Zeta.Certificates.RiemannSiegel.Batch0019.batch rfl rfl rfl

/-- First 4000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0020 : BatchSpec 4000 149500 1000 4556407 1000 :=
  BatchSpec.append upToRS0019 Zeta.Certificates.RiemannSiegel.Batch0020.batch rfl rfl rfl

/-- First 4200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0021 : BatchSpec 4200 149500 1000 4746605 1000 :=
  BatchSpec.append upToRS0020 Zeta.Certificates.RiemannSiegel.Batch0021.batch rfl rfl rfl

/-- First 4400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0022 : BatchSpec 4400 149500 1000 4935659 1000 :=
  BatchSpec.append upToRS0021 Zeta.Certificates.RiemannSiegel.Batch0022.batch rfl rfl rfl

/-- First 4600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0023 : BatchSpec 4600 149500 1000 5123633 1000 :=
  BatchSpec.append upToRS0022 Zeta.Certificates.RiemannSiegel.Batch0023.batch rfl rfl rfl

/-- First 4800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0024 : BatchSpec 4800 149500 1000 5310583 1000 :=
  BatchSpec.append upToRS0023 Zeta.Certificates.RiemannSiegel.Batch0024.batch rfl rfl rfl

/-- First 5000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0025 : BatchSpec 5000 149500 1000 5496562 1000 :=
  BatchSpec.append upToRS0024 Zeta.Certificates.RiemannSiegel.Batch0025.batch rfl rfl rfl

/-- First 5200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0026 : BatchSpec 5200 149500 1000 5681847 1000 :=
  BatchSpec.append upToRS0025 Zeta.Certificates.RiemannSiegel.Batch0026.batch rfl rfl rfl

/-- First 5400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0027 : BatchSpec 5400 149500 1000 5865789 1000 :=
  BatchSpec.append upToRS0026 Zeta.Certificates.RiemannSiegel.Batch0027.batch rfl rfl rfl

/-- First 5600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0028 : BatchSpec 5600 149500 1000 6049119 1000 :=
  BatchSpec.append upToRS0027 Zeta.Certificates.RiemannSiegel.Batch0028.batch rfl rfl rfl

/-- First 5800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0029 : BatchSpec 5800 149500 1000 6231645 1000 :=
  BatchSpec.append upToRS0028 Zeta.Certificates.RiemannSiegel.Batch0029.batch rfl rfl rfl

/-- First 6000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0030 : BatchSpec 6000 149500 1000 6413398 1000 :=
  BatchSpec.append upToRS0029 Zeta.Certificates.RiemannSiegel.Batch0030.batch rfl rfl rfl

/-- First 6200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0031 : BatchSpec 6200 149500 1000 6594411 1000 :=
  BatchSpec.append upToRS0030 Zeta.Certificates.RiemannSiegel.Batch0031.batch rfl rfl rfl

/-- First 6400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0032 : BatchSpec 6400 149500 1000 6774712 1000 :=
  BatchSpec.append upToRS0031 Zeta.Certificates.RiemannSiegel.Batch0032.batch rfl rfl rfl

/-- First 6600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0033 : BatchSpec 6600 149500 1000 6954777 1000 :=
  BatchSpec.append upToRS0032 Zeta.Certificates.RiemannSiegel.Batch0033.batch rfl rfl rfl

/-- First 6800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0034 : BatchSpec 6800 149500 1000 7133286 1000 :=
  BatchSpec.append upToRS0033 Zeta.Certificates.RiemannSiegel.Batch0034.batch rfl rfl rfl

/-- First 7000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0035 : BatchSpec 7000 149500 1000 7311607 1000 :=
  BatchSpec.append upToRS0034 Zeta.Certificates.RiemannSiegel.Batch0035.batch rfl rfl rfl

/-- First 7200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0036 : BatchSpec 7200 149500 1000 7489758 1000 :=
  BatchSpec.append upToRS0035 Zeta.Certificates.RiemannSiegel.Batch0036.batch rfl rfl rfl

/-- First 7400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0037 : BatchSpec 7400 149500 1000 7666428 1000 :=
  BatchSpec.append upToRS0036 Zeta.Certificates.RiemannSiegel.Batch0037.batch rfl rfl rfl

/-- First 7600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0038 : BatchSpec 7600 149500 1000 7842968 1000 :=
  BatchSpec.append upToRS0037 Zeta.Certificates.RiemannSiegel.Batch0038.batch rfl rfl rfl

/-- First 7800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0039 : BatchSpec 7800 149500 1000 8018952 1000 :=
  BatchSpec.append upToRS0038 Zeta.Certificates.RiemannSiegel.Batch0039.batch rfl rfl rfl

/-- First 8000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0040 : BatchSpec 8000 149500 1000 8193959 1000 :=
  BatchSpec.append upToRS0039 Zeta.Certificates.RiemannSiegel.Batch0040.batch rfl rfl rfl

/-- First 8200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0041 : BatchSpec 8200 149500 1000 8369321 1000 :=
  BatchSpec.append upToRS0040 Zeta.Certificates.RiemannSiegel.Batch0041.batch rfl rfl rfl

/-- First 8400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0042 : BatchSpec 8400 149500 1000 8543737 1000 :=
  BatchSpec.append upToRS0041 Zeta.Certificates.RiemannSiegel.Batch0042.batch rfl rfl rfl

/-- First 8600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0043 : BatchSpec 8600 149500 1000 8717662 1000 :=
  BatchSpec.append upToRS0042 Zeta.Certificates.RiemannSiegel.Batch0043.batch rfl rfl rfl

/-- First 8800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0044 : BatchSpec 8800 149500 1000 8891108 1000 :=
  BatchSpec.append upToRS0043 Zeta.Certificates.RiemannSiegel.Batch0044.batch rfl rfl rfl

/-- First 9000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0045 : BatchSpec 9000 149500 1000 9063657 1000 :=
  BatchSpec.append upToRS0044 Zeta.Certificates.RiemannSiegel.Batch0045.batch rfl rfl rfl

/-- First 9200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0046 : BatchSpec 9200 149500 1000 9236187 1000 :=
  BatchSpec.append upToRS0045 Zeta.Certificates.RiemannSiegel.Batch0046.batch rfl rfl rfl

/-- First 9400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0047 : BatchSpec 9400 149500 1000 9408275 1000 :=
  BatchSpec.append upToRS0046 Zeta.Certificates.RiemannSiegel.Batch0047.batch rfl rfl rfl

/-- First 9600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0048 : BatchSpec 9600 149500 1000 9579935 1000 :=
  BatchSpec.append upToRS0047 Zeta.Certificates.RiemannSiegel.Batch0048.batch rfl rfl rfl

/-- First 9800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0049 : BatchSpec 9800 149500 1000 9751603 1000 :=
  BatchSpec.append upToRS0048 Zeta.Certificates.RiemannSiegel.Batch0049.batch rfl rfl rfl

/-- First 10000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0050 : BatchSpec 10000 149500 1000 9922434 1000 :=
  BatchSpec.append upToRS0049 Zeta.Certificates.RiemannSiegel.Batch0050.batch rfl rfl rfl

/-- First 10200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0051 : BatchSpec 10200 149500 1000 10092867 1000 :=
  BatchSpec.append upToRS0050 Zeta.Certificates.RiemannSiegel.Batch0051.batch rfl rfl rfl

/-- First 10400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0052 : BatchSpec 10400 149500 1000 10262910 1000 :=
  BatchSpec.append upToRS0051 Zeta.Certificates.RiemannSiegel.Batch0052.batch rfl rfl rfl

/-- First 10600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0053 : BatchSpec 10600 149500 1000 10432574 1000 :=
  BatchSpec.append upToRS0052 Zeta.Certificates.RiemannSiegel.Batch0053.batch rfl rfl rfl

/-- First 10800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0054 : BatchSpec 10800 149500 1000 10601866 1000 :=
  BatchSpec.append upToRS0053 Zeta.Certificates.RiemannSiegel.Batch0054.batch rfl rfl rfl

/-- First 11000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0055 : BatchSpec 11000 149500 1000 10770585 1000 :=
  BatchSpec.append upToRS0054 Zeta.Certificates.RiemannSiegel.Batch0055.batch rfl rfl rfl

/-- First 11200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0056 : BatchSpec 11200 149500 1000 10939370 1000 :=
  BatchSpec.append upToRS0055 Zeta.Certificates.RiemannSiegel.Batch0056.batch rfl rfl rfl

/-- First 11400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0057 : BatchSpec 11400 149500 1000 11107597 1000 :=
  BatchSpec.append upToRS0056 Zeta.Certificates.RiemannSiegel.Batch0057.batch rfl rfl rfl

/-- First 11600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0058 : BatchSpec 11600 149500 1000 11275483 1000 :=
  BatchSpec.append upToRS0057 Zeta.Certificates.RiemannSiegel.Batch0058.batch rfl rfl rfl

/-- First 11800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0059 : BatchSpec 11800 149500 1000 11443037 1000 :=
  BatchSpec.append upToRS0058 Zeta.Certificates.RiemannSiegel.Batch0059.batch rfl rfl rfl

/-- First 12000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0060 : BatchSpec 12000 149500 1000 11609847 1000 :=
  BatchSpec.append upToRS0059 Zeta.Certificates.RiemannSiegel.Batch0060.batch rfl rfl rfl

/-- First 12200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0061 : BatchSpec 12200 149500 1000 11777173 1000 :=
  BatchSpec.append upToRS0060 Zeta.Certificates.RiemannSiegel.Batch0061.batch rfl rfl rfl

/-- First 12400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0062 : BatchSpec 12400 149500 1000 11943767 1000 :=
  BatchSpec.append upToRS0061 Zeta.Certificates.RiemannSiegel.Batch0062.batch rfl rfl rfl

/-- First 12600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0063 : BatchSpec 12600 149500 1000 12110055 1000 :=
  BatchSpec.append upToRS0062 Zeta.Certificates.RiemannSiegel.Batch0063.batch rfl rfl rfl

/-- First 12800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0064 : BatchSpec 12800 149500 1000 12276041 1000 :=
  BatchSpec.append upToRS0063 Zeta.Certificates.RiemannSiegel.Batch0064.batch rfl rfl rfl

/-- First 13000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0065 : BatchSpec 13000 149500 1000 12441731 1000 :=
  BatchSpec.append upToRS0064 Zeta.Certificates.RiemannSiegel.Batch0065.batch rfl rfl rfl

/-- First 13200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0066 : BatchSpec 13200 149500 1000 12607132 1000 :=
  BatchSpec.append upToRS0065 Zeta.Certificates.RiemannSiegel.Batch0066.batch rfl rfl rfl

/-- First 13400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0067 : BatchSpec 13400 149500 1000 12772247 1000 :=
  BatchSpec.append upToRS0066 Zeta.Certificates.RiemannSiegel.Batch0067.batch rfl rfl rfl

/-- First 13600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0068 : BatchSpec 13600 149500 1000 12937083 1000 :=
  BatchSpec.append upToRS0067 Zeta.Certificates.RiemannSiegel.Batch0068.batch rfl rfl rfl

/-- First 13800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0069 : BatchSpec 13800 149500 1000 13101643 1000 :=
  BatchSpec.append upToRS0068 Zeta.Certificates.RiemannSiegel.Batch0069.batch rfl rfl rfl

/-- First 14000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0070 : BatchSpec 14000 149500 1000 13265934 1000 :=
  BatchSpec.append upToRS0069 Zeta.Certificates.RiemannSiegel.Batch0070.batch rfl rfl rfl

/-- First 14200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0071 : BatchSpec 14200 149500 1000 13430165 1000 :=
  BatchSpec.append upToRS0070 Zeta.Certificates.RiemannSiegel.Batch0071.batch rfl rfl rfl

/-- First 14400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0072 : BatchSpec 14400 149500 1000 13593724 1000 :=
  BatchSpec.append upToRS0071 Zeta.Certificates.RiemannSiegel.Batch0072.batch rfl rfl rfl

/-- First 14600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0073 : BatchSpec 14600 149500 1000 13757232 1000 :=
  BatchSpec.append upToRS0072 Zeta.Certificates.RiemannSiegel.Batch0073.batch rfl rfl rfl

/-- First 14800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0074 : BatchSpec 14800 149500 1000 13920488 1000 :=
  BatchSpec.append upToRS0073 Zeta.Certificates.RiemannSiegel.Batch0074.batch rfl rfl rfl

/-- First 15000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0075 : BatchSpec 15000 149500 1000 14083495 1000 :=
  BatchSpec.append upToRS0074 Zeta.Certificates.RiemannSiegel.Batch0075.batch rfl rfl rfl

/-- First 15200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0076 : BatchSpec 15200 149500 1000 14245852 1000 :=
  BatchSpec.append upToRS0075 Zeta.Certificates.RiemannSiegel.Batch0076.batch rfl rfl rfl

/-- First 15400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0077 : BatchSpec 15400 149500 1000 14408782 1000 :=
  BatchSpec.append upToRS0076 Zeta.Certificates.RiemannSiegel.Batch0077.batch rfl rfl rfl

/-- First 15600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0078 : BatchSpec 15600 149500 1000 14571068 1000 :=
  BatchSpec.append upToRS0077 Zeta.Certificates.RiemannSiegel.Batch0078.batch rfl rfl rfl

/-- First 15800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0079 : BatchSpec 15800 149500 1000 14733122 1000 :=
  BatchSpec.append upToRS0078 Zeta.Certificates.RiemannSiegel.Batch0079.batch rfl rfl rfl

/-- First 16000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0080 : BatchSpec 16000 149500 1000 14895249 1000 :=
  BatchSpec.append upToRS0079 Zeta.Certificates.RiemannSiegel.Batch0080.batch rfl rfl rfl

/-- First 16200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0081 : BatchSpec 16200 149500 1000 15056141 1000 :=
  BatchSpec.append upToRS0080 Zeta.Certificates.RiemannSiegel.Batch0081.batch rfl rfl rfl

/-- First 16400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0082 : BatchSpec 16400 149500 1000 15217517 1000 :=
  BatchSpec.append upToRS0081 Zeta.Certificates.RiemannSiegel.Batch0082.batch rfl rfl rfl

/-- First 16600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0083 : BatchSpec 16600 149500 1000 15379076 1000 :=
  BatchSpec.append upToRS0082 Zeta.Certificates.RiemannSiegel.Batch0083.batch rfl rfl rfl

/-- First 16800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0084 : BatchSpec 16800 149500 1000 15540016 1000 :=
  BatchSpec.append upToRS0083 Zeta.Certificates.RiemannSiegel.Batch0084.batch rfl rfl rfl

/-- First 17000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0085 : BatchSpec 17000 149500 1000 15700744 1000 :=
  BatchSpec.append upToRS0084 Zeta.Certificates.RiemannSiegel.Batch0085.batch rfl rfl rfl

/-- First 17200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0086 : BatchSpec 17200 149500 1000 15861261 1000 :=
  BatchSpec.append upToRS0085 Zeta.Certificates.RiemannSiegel.Batch0086.batch rfl rfl rfl

/-- First 17400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0087 : BatchSpec 17400 149500 1000 16021571 1000 :=
  BatchSpec.append upToRS0086 Zeta.Certificates.RiemannSiegel.Batch0087.batch rfl rfl rfl

/-- First 17600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0088 : BatchSpec 17600 149500 1000 16181676 1000 :=
  BatchSpec.append upToRS0087 Zeta.Certificates.RiemannSiegel.Batch0088.batch rfl rfl rfl

/-- First 17800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0089 : BatchSpec 17800 149500 1000 16341581 1000 :=
  BatchSpec.append upToRS0088 Zeta.Certificates.RiemannSiegel.Batch0089.batch rfl rfl rfl

/-- First 18000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0090 : BatchSpec 18000 149500 1000 16501286 1000 :=
  BatchSpec.append upToRS0089 Zeta.Certificates.RiemannSiegel.Batch0090.batch rfl rfl rfl

/-- First 18200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0091 : BatchSpec 18200 149500 1000 16660796 1000 :=
  BatchSpec.append upToRS0090 Zeta.Certificates.RiemannSiegel.Batch0091.batch rfl rfl rfl

/-- First 18400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0092 : BatchSpec 18400 149500 1000 16820112 1000 :=
  BatchSpec.append upToRS0091 Zeta.Certificates.RiemannSiegel.Batch0092.batch rfl rfl rfl

/-- First 18600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0093 : BatchSpec 18600 149500 1000 16979237 1000 :=
  BatchSpec.append upToRS0092 Zeta.Certificates.RiemannSiegel.Batch0093.batch rfl rfl rfl

/-- First 18800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0094 : BatchSpec 18800 149500 1000 17138173 1000 :=
  BatchSpec.append upToRS0093 Zeta.Certificates.RiemannSiegel.Batch0094.batch rfl rfl rfl

/-- First 19000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0095 : BatchSpec 19000 149500 1000 17296924 1000 :=
  BatchSpec.append upToRS0094 Zeta.Certificates.RiemannSiegel.Batch0095.batch rfl rfl rfl

/-- First 19200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0096 : BatchSpec 19200 149500 1000 17455490 1000 :=
  BatchSpec.append upToRS0095 Zeta.Certificates.RiemannSiegel.Batch0096.batch rfl rfl rfl

/-- First 19400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0097 : BatchSpec 19400 149500 1000 17613875 1000 :=
  BatchSpec.append upToRS0096 Zeta.Certificates.RiemannSiegel.Batch0097.batch rfl rfl rfl

/-- First 19600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0098 : BatchSpec 19600 149500 1000 17772081 1000 :=
  BatchSpec.append upToRS0097 Zeta.Certificates.RiemannSiegel.Batch0098.batch rfl rfl rfl

/-- First 19800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0099 : BatchSpec 19800 149500 1000 17930110 1000 :=
  BatchSpec.append upToRS0098 Zeta.Certificates.RiemannSiegel.Batch0099.batch rfl rfl rfl

/-- First 20000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0100 : BatchSpec 20000 149500 1000 18087965 1000 :=
  BatchSpec.append upToRS0099 Zeta.Certificates.RiemannSiegel.Batch0100.batch rfl rfl rfl

/-- First 20200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0101 : BatchSpec 20200 149500 1000 18245646 1000 :=
  BatchSpec.append upToRS0100 Zeta.Certificates.RiemannSiegel.Batch0101.batch rfl rfl rfl

/-- First 20400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0102 : BatchSpec 20400 149500 1000 18403157 1000 :=
  BatchSpec.append upToRS0101 Zeta.Certificates.RiemannSiegel.Batch0102.batch rfl rfl rfl

/-- First 20600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0103 : BatchSpec 20600 149500 1000 18560499 1000 :=
  BatchSpec.append upToRS0102 Zeta.Certificates.RiemannSiegel.Batch0103.batch rfl rfl rfl

/-- First 20800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0104 : BatchSpec 20800 149500 1000 18717281 1000 :=
  BatchSpec.append upToRS0103 Zeta.Certificates.RiemannSiegel.Batch0104.batch rfl rfl rfl

/-- First 21000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0105 : BatchSpec 21000 149500 1000 18875076 1000 :=
  BatchSpec.append upToRS0104 Zeta.Certificates.RiemannSiegel.Batch0105.batch rfl rfl rfl

/-- First 21200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0106 : BatchSpec 21200 149500 1000 19031532 1000 :=
  BatchSpec.append upToRS0105 Zeta.Certificates.RiemannSiegel.Batch0106.batch rfl rfl rfl

/-- First 21400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0107 : BatchSpec 21400 149500 1000 19188218 1000 :=
  BatchSpec.append upToRS0106 Zeta.Certificates.RiemannSiegel.Batch0107.batch rfl rfl rfl

/-- First 21600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0108 : BatchSpec 21600 149500 1000 19344745 1000 :=
  BatchSpec.append upToRS0107 Zeta.Certificates.RiemannSiegel.Batch0108.batch rfl rfl rfl

/-- First 21800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0109 : BatchSpec 21800 149500 1000 19501114 1000 :=
  BatchSpec.append upToRS0108 Zeta.Certificates.RiemannSiegel.Batch0109.batch rfl rfl rfl

/-- First 22000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0110 : BatchSpec 22000 149500 1000 19657328 1000 :=
  BatchSpec.append upToRS0109 Zeta.Certificates.RiemannSiegel.Batch0110.batch rfl rfl rfl

/-- First 22200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0111 : BatchSpec 22200 149500 1000 19813388 1000 :=
  BatchSpec.append upToRS0110 Zeta.Certificates.RiemannSiegel.Batch0111.batch rfl rfl rfl

/-- First 22400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0112 : BatchSpec 22400 149500 1000 19969295 1000 :=
  BatchSpec.append upToRS0111 Zeta.Certificates.RiemannSiegel.Batch0112.batch rfl rfl rfl

/-- First 22600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0113 : BatchSpec 22600 149500 1000 20125051 1000 :=
  BatchSpec.append upToRS0112 Zeta.Certificates.RiemannSiegel.Batch0113.batch rfl rfl rfl

/-- First 22800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0114 : BatchSpec 22800 149500 1000 20281047 1000 :=
  BatchSpec.append upToRS0113 Zeta.Certificates.RiemannSiegel.Batch0114.batch rfl rfl rfl

/-- First 23000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0115 : BatchSpec 23000 149500 1000 20436118 1000 :=
  BatchSpec.append upToRS0114 Zeta.Certificates.RiemannSiegel.Batch0115.batch rfl rfl rfl

/-- First 23200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0116 : BatchSpec 23200 149500 1000 20591432 1000 :=
  BatchSpec.append upToRS0115 Zeta.Certificates.RiemannSiegel.Batch0116.batch rfl rfl rfl

/-- First 23400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0117 : BatchSpec 23400 149500 1000 20746601 1000 :=
  BatchSpec.append upToRS0116 Zeta.Certificates.RiemannSiegel.Batch0117.batch rfl rfl rfl

/-- First 23600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0118 : BatchSpec 23600 149500 1000 20901626 1000 :=
  BatchSpec.append upToRS0117 Zeta.Certificates.RiemannSiegel.Batch0118.batch rfl rfl rfl

/-- First 23800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0119 : BatchSpec 23800 149500 1000 21056123 1000 :=
  BatchSpec.append upToRS0118 Zeta.Certificates.RiemannSiegel.Batch0119.batch rfl rfl rfl

/-- First 24000 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0120 : BatchSpec 24000 149500 1000 21211254 1000 :=
  BatchSpec.append upToRS0119 Zeta.Certificates.RiemannSiegel.Batch0120.batch rfl rfl rfl

/-- First 24200 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0121 : BatchSpec 24200 149500 1000 21365473 1000 :=
  BatchSpec.append upToRS0120 Zeta.Certificates.RiemannSiegel.Batch0121.batch rfl rfl rfl

/-- First 24400 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0122 : BatchSpec 24400 149500 1000 21520327 1000 :=
  BatchSpec.append upToRS0121 Zeta.Certificates.RiemannSiegel.Batch0122.batch rfl rfl rfl

/-- First 24600 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0123 : BatchSpec 24600 149500 1000 21674659 1000 :=
  BatchSpec.append upToRS0122 Zeta.Certificates.RiemannSiegel.Batch0123.batch rfl rfl rfl

/-- First 24800 authentic original RS rows, WITHOUT the first 52 Euler rows. -/
theorem upToRS0124 : BatchSpec 24800 149500 1000 21828855 1000 :=
  BatchSpec.append upToRS0123 Zeta.Certificates.RiemannSiegel.Batch0124.batch rfl rfl rfl

/-- Original RS-only prefix through source group 0002; zero 1..52 excluded. -/
theorem upToGroup0002 : BatchSpec 49800 149500 1000 40327924 1000 :=
  BatchSpec.append upToRS0124 Zeta.Certificates.Groups.Level1.Group0002.group rfl rfl rfl

/-- Original RS-only prefix through source group 0003; zero 1..52 excluded. -/
theorem upToGroup0003 : BatchSpec 74800 149500 1000 57862857 1000 :=
  BatchSpec.append upToGroup0002 Zeta.Certificates.Groups.Level1.Group0003.group rfl rfl rfl

/-- Original RS-only prefix through source group 0004; zero 1..52 excluded. -/
theorem upToGroup0004 : BatchSpec 99800 149500 1000 74822148 1000 :=
  BatchSpec.append upToGroup0003 Zeta.Certificates.Groups.Level1.Group0004.group rfl rfl rfl

/-- Original RS-only prefix through source group 0005; zero 1..52 excluded. -/
theorem upToGroup0005 : BatchSpec 124800 149500 1000 91377303 1000 :=
  BatchSpec.append upToGroup0004 Zeta.Certificates.Groups.Level1.Group0005.group rfl rfl rfl

/-- Original RS-only prefix through source group 0006; zero 1..52 excluded. -/
theorem upToGroup0006 : BatchSpec 149800 149500 1000 107622802 1000 :=
  BatchSpec.append upToGroup0005 Zeta.Certificates.Groups.Level1.Group0006.group rfl rfl rfl

/-- Original RS-only prefix through source group 0007; zero 1..52 excluded. -/
theorem upToGroup0007 : BatchSpec 174800 149500 1000 123619988 1000 :=
  BatchSpec.append upToGroup0006 Zeta.Certificates.Groups.Level1.Group0007.group rfl rfl rfl

/-- Original RS-only prefix through source group 0008; zero 1..52 excluded. -/
theorem upToGroup0008 : BatchSpec 199800 149500 1000 139409432 1000 :=
  BatchSpec.append upToGroup0007 Zeta.Certificates.Groups.Level1.Group0008.group rfl rfl rfl

/-- Original RS-only prefix through source group 0009; zero 1..52 excluded. -/
theorem upToGroup0009 : BatchSpec 224800 149500 1000 155021681 1000 :=
  BatchSpec.append upToGroup0008 Zeta.Certificates.Groups.Level1.Group0009.group rfl rfl rfl

/-- Original RS-only prefix through source group 0010; zero 1..52 excluded. -/
theorem upToGroup0010 : BatchSpec 249800 149500 1000 170479656 1000 :=
  BatchSpec.append upToGroup0009 Zeta.Certificates.Groups.Level1.Group0010.group rfl rfl rfl

/-- Original RS-only prefix through source group 0011; zero 1..52 excluded. -/
theorem upToGroup0011 : BatchSpec 274800 149500 1000 185801296 1000 :=
  BatchSpec.append upToGroup0010 Zeta.Certificates.Groups.Level1.Group0011.group rfl rfl rfl

/-- Original RS-only prefix through source group 0012; zero 1..52 excluded. -/
theorem upToGroup0012 : BatchSpec 299800 149500 1000 201001000 1000 :=
  BatchSpec.append upToGroup0011 Zeta.Certificates.Groups.Level1.Group0012.group rfl rfl rfl

/-- Original RS-only prefix through source group 0013; zero 1..52 excluded. -/
theorem upToGroup0013 : BatchSpec 324800 149500 1000 216090565 1000 :=
  BatchSpec.append upToGroup0012 Zeta.Certificates.Groups.Level1.Group0013.group rfl rfl rfl

/-- Original RS-only prefix through source group 0014; zero 1..52 excluded. -/
theorem upToGroup0014 : BatchSpec 349800 149500 1000 231079819 1000 :=
  BatchSpec.append upToGroup0013 Zeta.Certificates.Groups.Level1.Group0014.group rfl rfl rfl

/-- Original RS-only prefix through source group 0015; zero 1..52 excluded. -/
theorem upToGroup0015 : BatchSpec 374800 149500 1000 245977067 1000 :=
  BatchSpec.append upToGroup0014 Zeta.Certificates.Groups.Level1.Group0015.group rfl rfl rfl

/-- Original RS-only prefix through source group 0016; zero 1..52 excluded. -/
theorem upToGroup0016 : BatchSpec 399800 149500 1000 260789123 1000 :=
  BatchSpec.append upToGroup0015 Zeta.Certificates.Groups.Level1.Group0016.group rfl rfl rfl

/-- Original RS-only prefix through source group 0017; zero 1..52 excluded. -/
theorem upToGroup0017 : BatchSpec 424800 149500 1000 275523310 1000 :=
  BatchSpec.append upToGroup0016 Zeta.Certificates.Groups.Level1.Group0017.group rfl rfl rfl

/-- Original RS-only prefix through source group 0018; zero 1..52 excluded. -/
theorem upToGroup0018 : BatchSpec 449800 149500 1000 290183223 1000 :=
  BatchSpec.append upToGroup0017 Zeta.Certificates.Groups.Level1.Group0018.group rfl rfl rfl

/-- Original RS-only prefix through source group 0019; zero 1..52 excluded. -/
theorem upToGroup0019 : BatchSpec 474800 149500 1000 304774757 1000 :=
  BatchSpec.append upToGroup0018 Zeta.Certificates.Groups.Level1.Group0019.group rfl rfl rfl

/-- Original RS-only prefix through source group 0020; zero 1..52 excluded. -/
theorem upToGroup0020 : BatchSpec 499800 149500 1000 319301797 1000 :=
  BatchSpec.append upToGroup0019 Zeta.Certificates.Groups.Level1.Group0020.group rfl rfl rfl

/-- Original RS-only prefix through source group 0021; zero 1..52 excluded. -/
theorem upToGroup0021 : BatchSpec 524800 149500 1000 333768072 1000 :=
  BatchSpec.append upToGroup0020 Zeta.Certificates.Groups.Level1.Group0021.group rfl rfl rfl

/-- Original RS-only prefix through source group 0022; zero 1..52 excluded. -/
theorem upToGroup0022 : BatchSpec 549800 149500 1000 348176925 1000 :=
  BatchSpec.append upToGroup0021 Zeta.Certificates.Groups.Level1.Group0022.group rfl rfl rfl

/-- Original RS-only prefix through source group 0023; zero 1..52 excluded. -/
theorem upToGroup0023 : BatchSpec 574800 149500 1000 362531514 1000 :=
  BatchSpec.append upToGroup0022 Zeta.Certificates.Groups.Level1.Group0023.group rfl rfl rfl

/-- Original RS-only prefix through source group 0024; zero 1..52 excluded. -/
theorem upToGroup0024 : BatchSpec 599800 149500 1000 376834143 1000 :=
  BatchSpec.append upToGroup0023 Zeta.Certificates.Groups.Level1.Group0024.group rfl rfl rfl

/-- Original RS-only prefix through source group 0025; zero 1..52 excluded. -/
theorem upToGroup0025 : BatchSpec 624800 149500 1000 391087867 1000 :=
  BatchSpec.append upToGroup0024 Zeta.Certificates.Groups.Level1.Group0025.group rfl rfl rfl

/-- Original RS-only prefix through source group 0026; zero 1..52 excluded. -/
theorem upToGroup0026 : BatchSpec 649800 149500 1000 405294673 1000 :=
  BatchSpec.append upToGroup0025 Zeta.Certificates.Groups.Level1.Group0026.group rfl rfl rfl

/-- Original RS-only prefix through source group 0027; zero 1..52 excluded. -/
theorem upToGroup0027 : BatchSpec 674800 149500 1000 419456216 1000 :=
  BatchSpec.append upToGroup0026 Zeta.Certificates.Groups.Level1.Group0027.group rfl rfl rfl

/-- Original RS-only prefix through source group 0028; zero 1..52 excluded. -/
theorem upToGroup0028 : BatchSpec 699800 149500 1000 433575123 1000 :=
  BatchSpec.append upToGroup0027 Zeta.Certificates.Groups.Level1.Group0028.group rfl rfl rfl

/-- Original RS-only prefix through source group 0029; zero 1..52 excluded. -/
theorem upToGroup0029 : BatchSpec 724800 149500 1000 447652875 1000 :=
  BatchSpec.append upToGroup0028 Zeta.Certificates.Groups.Level1.Group0029.group rfl rfl rfl

/-- Original RS-only prefix through source group 0030; zero 1..52 excluded. -/
theorem upToGroup0030 : BatchSpec 749800 149500 1000 461691110 1000 :=
  BatchSpec.append upToGroup0029 Zeta.Certificates.Groups.Level1.Group0030.group rfl rfl rfl

/-- Original RS-only prefix through source group 0031; zero 1..52 excluded. -/
theorem upToGroup0031 : BatchSpec 774800 149500 1000 475691485 1000 :=
  BatchSpec.append upToGroup0030 Zeta.Certificates.Groups.Level1.Group0031.group rfl rfl rfl

/-- Original RS-only prefix through source group 0032; zero 1..52 excluded. -/
theorem upToGroup0032 : BatchSpec 799800 149500 1000 489654994 1000 :=
  BatchSpec.append upToGroup0031 Zeta.Certificates.Groups.Level1.Group0032.group rfl rfl rfl

/-- Original RS-only prefix through source group 0033; zero 1..52 excluded. -/
theorem upToGroup0033 : BatchSpec 824800 149500 1000 503583371 1000 :=
  BatchSpec.append upToGroup0032 Zeta.Certificates.Groups.Level1.Group0033.group rfl rfl rfl

/-- Original RS-only prefix through source group 0034; zero 1..52 excluded. -/
theorem upToGroup0034 : BatchSpec 849800 149500 1000 517477710 1000 :=
  BatchSpec.append upToGroup0033 Zeta.Certificates.Groups.Level1.Group0034.group rfl rfl rfl

/-- Original RS-only prefix through source group 0035; zero 1..52 excluded. -/
theorem upToGroup0035 : BatchSpec 874800 149500 1000 531339161 1000 :=
  BatchSpec.append upToGroup0034 Zeta.Certificates.Groups.Level1.Group0035.group rfl rfl rfl

/-- Original RS-only prefix through source group 0036; zero 1..52 excluded. -/
theorem upToGroup0036 : BatchSpec 899800 149500 1000 545168808 1000 :=
  BatchSpec.append upToGroup0035 Zeta.Certificates.Groups.Level1.Group0036.group rfl rfl rfl

/-- Original RS-only prefix through source group 0037; zero 1..52 excluded. -/
theorem upToGroup0037 : BatchSpec 924800 149500 1000 558967666 1000 :=
  BatchSpec.append upToGroup0036 Zeta.Certificates.Groups.Level1.Group0037.group rfl rfl rfl

/-- Original RS-only prefix through source group 0038; zero 1..52 excluded. -/
theorem upToGroup0038 : BatchSpec 949800 149500 1000 572736694 1000 :=
  BatchSpec.append upToGroup0037 Zeta.Certificates.Groups.Level1.Group0038.group rfl rfl rfl

/-- Original RS-only prefix through source group 0039; zero 1..52 excluded. -/
theorem upToGroup0039 : BatchSpec 974800 149500 1000 586476793 1000 :=
  BatchSpec.append upToGroup0038 Zeta.Certificates.Groups.Level1.Group0039.group rfl rfl rfl

/-- Original RS-only prefix through source group 0040; zero 1..52 excluded. -/
theorem upToGroup0040 : BatchSpec 999800 149500 1000 600188819 1000 :=
  BatchSpec.append upToGroup0039 Zeta.Certificates.Groups.Level1.Group0040.group rfl rfl rfl

/-- Original RS-only prefix through source group 0041; zero 1..52 excluded. -/
theorem upToGroup0041 : BatchSpec 1024800 149500 1000 613873576 1000 :=
  BatchSpec.append upToGroup0040 Zeta.Certificates.Groups.Level1.Group0041.group rfl rfl rfl

/-- Original RS-only prefix through source group 0042; zero 1..52 excluded. -/
theorem upToGroup0042 : BatchSpec 1049800 149500 1000 627531831 1000 :=
  BatchSpec.append upToGroup0041 Zeta.Certificates.Groups.Level1.Group0042.group rfl rfl rfl

/-- Original RS-only prefix through source group 0043; zero 1..52 excluded. -/
theorem upToGroup0043 : BatchSpec 1074800 149500 1000 641164309 1000 :=
  BatchSpec.append upToGroup0042 Zeta.Certificates.Groups.Level1.Group0043.group rfl rfl rfl

/-- Original RS-only prefix through source group 0044; zero 1..52 excluded. -/
theorem upToGroup0044 : BatchSpec 1099800 149500 1000 654771698 1000 :=
  BatchSpec.append upToGroup0043 Zeta.Certificates.Groups.Level1.Group0044.group rfl rfl rfl

/-- Original RS-only prefix through source group 0045; zero 1..52 excluded. -/
theorem upToGroup0045 : BatchSpec 1124800 149500 1000 668354518 1000 :=
  BatchSpec.append upToGroup0044 Zeta.Certificates.Groups.Level1.Group0045.group rfl rfl rfl

/-- Original RS-only prefix through source group 0046; zero 1..52 excluded. -/
theorem upToGroup0046 : BatchSpec 1149800 149500 1000 681913800 1000 :=
  BatchSpec.append upToGroup0045 Zeta.Certificates.Groups.Level1.Group0046.group rfl rfl rfl

/-- Original RS-only prefix through source group 0047; zero 1..52 excluded. -/
theorem upToGroup0047 : BatchSpec 1174800 149500 1000 695449732 1000 :=
  BatchSpec.append upToGroup0046 Zeta.Certificates.Groups.Level1.Group0047.group rfl rfl rfl

/-- Original RS-only prefix through source group 0048; zero 1..52 excluded. -/
theorem upToGroup0048 : BatchSpec 1199800 149500 1000 708963016 1000 :=
  BatchSpec.append upToGroup0047 Zeta.Certificates.Groups.Level1.Group0048.group rfl rfl rfl

/-- Original RS-only prefix through source group 0049; zero 1..52 excluded. -/
theorem upToGroup0049 : BatchSpec 1224800 149500 1000 722453925 1000 :=
  BatchSpec.append upToGroup0048 Zeta.Certificates.Groups.Level1.Group0049.group rfl rfl rfl

/-- Original RS-only prefix through source group 0050; zero 1..52 excluded. -/
theorem upToGroup0050 : BatchSpec 1249800 149500 1000 735923785 1000 :=
  BatchSpec.append upToGroup0049 Zeta.Certificates.Groups.Level1.Group0050.group rfl rfl rfl

/-- Original RS-only prefix through source group 0051; zero 1..52 excluded. -/
theorem upToGroup0051 : BatchSpec 1274800 149500 1000 749372553 1000 :=
  BatchSpec.append upToGroup0050 Zeta.Certificates.Groups.Level1.Group0051.group rfl rfl rfl

/-- Original RS-only prefix through source group 0052; zero 1..52 excluded. -/
theorem upToGroup0052 : BatchSpec 1299800 149500 1000 762800165 1000 :=
  BatchSpec.append upToGroup0051 Zeta.Certificates.Groups.Level1.Group0052.group rfl rfl rfl

/-- Original RS-only prefix through source group 0053; zero 1..52 excluded. -/
theorem upToGroup0053 : BatchSpec 1324800 149500 1000 776207751 1000 :=
  BatchSpec.append upToGroup0052 Zeta.Certificates.Groups.Level1.Group0053.group rfl rfl rfl

/-- Original RS-only prefix through source group 0054; zero 1..52 excluded. -/
theorem upToGroup0054 : BatchSpec 1349800 149500 1000 789595878 1000 :=
  BatchSpec.append upToGroup0053 Zeta.Certificates.Groups.Level1.Group0054.group rfl rfl rfl

/-- Original RS-only prefix through source group 0055; zero 1..52 excluded. -/
theorem upToGroup0055 : BatchSpec 1374800 149500 1000 802964832 1000 :=
  BatchSpec.append upToGroup0054 Zeta.Certificates.Groups.Level1.Group0055.group rfl rfl rfl

/-- Original RS-only prefix through source group 0056; zero 1..52 excluded. -/
theorem upToGroup0056 : BatchSpec 1399800 149500 1000 816314348 1000 :=
  BatchSpec.append upToGroup0055 Zeta.Certificates.Groups.Level1.Group0056.group rfl rfl rfl

/-- Original RS-only prefix through source group 0057; zero 1..52 excluded. -/
theorem upToGroup0057 : BatchSpec 1424800 149500 1000 829645614 1000 :=
  BatchSpec.append upToGroup0056 Zeta.Certificates.Groups.Level1.Group0057.group rfl rfl rfl

/-- Original RS-only prefix through source group 0058; zero 1..52 excluded. -/
theorem upToGroup0058 : BatchSpec 1449800 149500 1000 842958736 1000 :=
  BatchSpec.append upToGroup0057 Zeta.Certificates.Groups.Level1.Group0058.group rfl rfl rfl

/-- Original RS-only prefix through source group 0059; zero 1..52 excluded. -/
theorem upToGroup0059 : BatchSpec 1474800 149500 1000 856254073 1000 :=
  BatchSpec.append upToGroup0058 Zeta.Certificates.Groups.Level1.Group0059.group rfl rfl rfl

/-- Original RS-only prefix through source group 0060; zero 1..52 excluded. -/
theorem upToGroup0060 : BatchSpec 1499800 149500 1000 869531970 1000 :=
  BatchSpec.append upToGroup0059 Zeta.Certificates.Groups.Level1.Group0060.group rfl rfl rfl

/-- Original RS-only prefix through source group 0061; zero 1..52 excluded. -/
theorem upToGroup0061 : BatchSpec 1524800 149500 1000 882792495 1000 :=
  BatchSpec.append upToGroup0060 Zeta.Certificates.Groups.Level1.Group0061.group rfl rfl rfl

/-- Original RS-only prefix through source group 0062; zero 1..52 excluded. -/
theorem upToGroup0062 : BatchSpec 1549800 149500 1000 896036501 1000 :=
  BatchSpec.append upToGroup0061 Zeta.Certificates.Groups.Level1.Group0062.group rfl rfl rfl

/-- Original RS-only prefix through source group 0063; zero 1..52 excluded. -/
theorem upToGroup0063 : BatchSpec 1574800 149500 1000 909264296 1000 :=
  BatchSpec.append upToGroup0062 Zeta.Certificates.Groups.Level1.Group0063.group rfl rfl rfl

/-- Original RS-only prefix through source group 0064; zero 1..52 excluded. -/
theorem upToGroup0064 : BatchSpec 1599800 149500 1000 922475651 1000 :=
  BatchSpec.append upToGroup0063 Zeta.Certificates.Groups.Level1.Group0064.group rfl rfl rfl

/-- Original RS-only prefix through source group 0065; zero 1..52 excluded. -/
theorem upToGroup0065 : BatchSpec 1624800 149500 1000 935671121 1000 :=
  BatchSpec.append upToGroup0064 Zeta.Certificates.Groups.Level1.Group0065.group rfl rfl rfl

/-- Original RS-only prefix through source group 0066; zero 1..52 excluded. -/
theorem upToGroup0066 : BatchSpec 1649800 149500 1000 948851249 1000 :=
  BatchSpec.append upToGroup0065 Zeta.Certificates.Groups.Level1.Group0066.group rfl rfl rfl

/-- Original RS-only prefix through source group 0067; zero 1..52 excluded. -/
theorem upToGroup0067 : BatchSpec 1674800 149500 1000 962015516 1000 :=
  BatchSpec.append upToGroup0066 Zeta.Certificates.Groups.Level1.Group0067.group rfl rfl rfl

/-- Original RS-only prefix through source group 0068; zero 1..52 excluded. -/
theorem upToGroup0068 : BatchSpec 1699800 149500 1000 975165236 1000 :=
  BatchSpec.append upToGroup0067 Zeta.Certificates.Groups.Level1.Group0068.group rfl rfl rfl

/-- Original RS-only prefix through source group 0069; zero 1..52 excluded. -/
theorem upToGroup0069 : BatchSpec 1724800 149500 1000 988299612 1000 :=
  BatchSpec.append upToGroup0068 Zeta.Certificates.Groups.Level1.Group0069.group rfl rfl rfl

/-- Original RS-only prefix through source group 0070; zero 1..52 excluded. -/
theorem upToGroup0070 : BatchSpec 1747950 149500 1000 1000449286 1000 :=
  BatchSpec.append upToGroup0069 Zeta.Certificates.Groups.Level1.Group0070.group rfl rfl rfl

/-- All 1,747,950 ORIGINAL source-certified RS intervals, source method only.
Their first lower ordinate is 149.500; last right ordinate is 1000449.286.
This theorem does NOT expose indexed numerical row endpoints,
and does NOT yet assert a certified count N(149.5)=52. -/
theorem all_original_RS_only : BatchSpec 1747950 149500 1000 1000449286 1000 :=
  upToGroup0070

end CP013RSOnly

#print axioms CP013RSOnly.all_original_RS_only
