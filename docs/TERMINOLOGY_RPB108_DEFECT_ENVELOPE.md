# CC15 matrix defect-envelope terminology

| Term | Meaning |
| --- | --- |
| Original complement C | The unshifted physical F112 complement at a=21/20, with C >= c=699/1000. No boundedness of C is assumed. |
| Action columns Z | The same sixteen ORIGINAL complementary Legendre columns used by CC14. They lie in the operator domain, so CZ is in physical L2. |
| Inverse defect D_c | The bounded positive operator c^(-1)I-C^(-1). This symbol is distinct from the historical interval-length D in producer code. |
| Defect matrix J | Z*C D_c CZ = (CZ)*(CZ)/c-Z*CZ. It retains every mixed action and native-trial entry. |
| Defect source cross H | Z*C D_c B = (CZ)*B/c-Z*B, for the ORIGINAL source columns B. |
| Matrix defect envelope | C^(-1) <= c^(-1)I-D_c CZ J^(-1)(CZ)*D_c when J is positive definite. |
| Rational matrix credit | H*L+L*H-L*JL <= H*J^(-1)H, valid for every rational lift L. |
| Necessary pair gate | The restriction to NF71's exactly even weak direction w and CC13's physical degree-two quotient vector r. A successful pair lower does not certify the full even54 quotient. |
| Best-span obstruction | A certified negative UPPER value of A-G_B/c+H*J^(-1)H on one pair direction. It defeats this entire matrix envelope in this fixed action span. It is not negativity of the actual Weil form. |

The source Gram G_B=B*B and native form A are in the same physical metric. All original activated powers 2,3,4,5,7,8, both signed poles, all thirteen panels, and their errors remain. CC11's protected five-plane and codimension107 slice are preserved. No whole-even, whole-odd, non-stalling, RH/F4, full transport, or Lean closure is implied by these definitions.
