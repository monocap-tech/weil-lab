# NF459 — Real original 244D physical Christoffel endpoint and collar

**Status:** Original physical native computation submitted to focused CI. Numerical standing only after inspecting real output; no outcome presumed.

## Previous → Current → Next

**NF458:** Original selected J242 comprises 241 frequency/order polynomial-trigonometric jets at 67 centers (maximum order 13) and sinh(x/2), not orthogonal sine harmonics. Together with the actual n512/n513 exterior quotient, V has dimension 244. Accepted R+d12 gives ||P_V f||<3.4e-11. The endpoint K_V gate is sup_(B-1e-15,B) K_V<(4500/17)^2; if established this would trigger NF457's certified full two-sided T_collar<4.01e-31.

**NF459 method:** Native python-flint 0.8.0 at 4096 bits reconstructs original source rank SHA 9b9820a0... and the true full physical Gram H=J*J from the same integrator and basis as NF400. Its original near-orthonormal physical frame D is certified by row-sum |D^T H D-I|<1/100. The original raw n512/n513 physical sin probes are paired via C=J*U and F=U*U, transformed V=D^T C. Source-correlated two-by-two Schur S=F-V^T N^-1 V must be strictly positive definite, and its diagonals must overlap the accepted native original q512 and q513 quotient norms. This is not a numerical surrogate for the authentic selected space.

At a physical x, form original raw evaluation j(x) from every k-jet (x^k sin(2pi c x) for even k, x^k cos for odd k) and pole sinh(x/2), and raw sine evaluation u(x) for n512/n513. Compute

    e=D^T j(x);   z=N^-1 e;
    g=u(x)-V^T z;
    K_V(x,x)=e^T z + g^T S^-1 g.

Evaluate rigorously using original native real intervals at x=B, x=B-10^-15, AND on a single enclosing Arb ball covering the entire terminal collar, without extrapolating endpoints. The resulting full interval must be compared to the exact threshold. The original source/pole and entire selected physical frame are retained. Negative collar follows original odd parity. If the 1-ball interval loses correlation from cancellation, record a typed method stop rather than mark a pointwise check as whole-collar certification.

**Acceptance conditions:** Original rank SHA, true 241+pole source basis, authentic n512/n513 quotient source overlap, N near-normality, S SPD, outward K(B) and whole collar, and the strict original threshold. The focused Actions workflow uploads a typed success or fail-closed numerical receipt. Any source/interval failure leaves the full actual K bound open. This pass does not compute full T, NF404, W-ODD-NEG, operator domain, whole Weil or RH.

**Next:** If the whole original K collar passes, charge the actual original endpoint L2 budget and move to bulk T. If it does not, compute the actual original selected projection Pi(B) and its derivative or a correlation-preserving multibox collar evaluation, without repeating independent coarse jet box overestimates.
