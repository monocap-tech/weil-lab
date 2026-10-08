# RPB108 complete source-shell gain terms (NF67)

| Term | Exact meaning |
| --- | --- |
| Common source ambient | Complete normalized original positive/negative divisor channels on a fixed finite aperture cap B; all ordinates and multiplicity copies retained. |
| V_a | Closed positive range P(D_a) inside the common positive source ambient; supports are included physically, so V_s is a subspace of V_t. |
| T_a | Original gain map P h ->N h on V_a. It is a restriction of T_B even without original positivity. |
| A_a | T_a T_a* on the entire common NEGATIVE source ambient; bounded positive operator, with norm g_a^2. |
| W_st | V_t intersect V_s^perp in positive-source inner product; not a physical shell or a finite source prefix. |
| K_st | T_t restricted to W_st; negative-source image of the exact source-orthogonal incoming shell. |
| Incoming cost B_st | K_st*(I-A_s)^(-1)K_st when g_s<1. Whole original positivity at t is equivalent to ||B_st||<1. |
| Critical output space | Spectral space of A_s above 1-eta. With a protected codimension-d complement it has dimension at most d, despite retaining all actual rows. |
| Critical leakage | E_s K_st into that output space; its inverse-defect-weighted Gram is the potentially amplified part of B_st. |
| Leakage estimate | An independent arithmetic bound on incoming output overlap relative to its OLD remaining defect. It is not implied by bounded sources or strip width. |

Proof, exact algebra controls and scope: [NF67 note](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_SHELL_GAIN_20261008.md). This criterion is for the ORIGINAL source gain, with no approximation defect or auxiliary channel.
