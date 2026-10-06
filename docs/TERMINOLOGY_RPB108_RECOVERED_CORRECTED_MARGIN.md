# RPB-108 recovered Gram and stronger corrected margin terminology

- **Recovered complete Gram:** the unchanged 2026-10-05 full 84-source residual Gram, reconstructed from its pinned native and source inputs and matched byte for byte by SHA256 and Git blob hash.
- **Compact 80-digit Gram enclosure:** the symmetric full Gram encoded by its 3,570 lower-triangle intervals. Each original lower endpoint is rounded down and upper endpoint up on grid 10^(-80). This is an outward enclosure, not a lossless encoding; all mixed terms remain.
- **Corrected Schur margin:** tau such that Q84-(100/51)R84>=tau I, with the actual source-map error included through the certified correction delta. This pass certifies tau=10^(-18); the previous recorded corrected margin was 10^(-29).
- **Widened trace lift bound:** L=47/5, verified from L^2>(100/51)^2(trace_upper(compact Gram)+delta). This is a physical lift norm bound.
- **Updated full-domain coefficients:** mu=tau*c/[tau+c(1+L^2)], c=51/100, and kappa=mu/[10(mu+23)] from the inherited actual Garding inequality. Here mu=51/4557360000000000000100 and kappa=51/1048192800000000000023510.
- **Simple certified lower bounds:** physical 10^(-20) and logarithmic 4*10^(-23), both strictly below the respective exact coefficients.

The numerical aperture stays 81/100. No optimal margin, global endpoint exclusion, fixed historical packet attachment, F4 closure, FULL TRANSPORT CLOSED or Lean proof is claimed.
