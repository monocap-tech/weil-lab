# RPB108 EF06 — original signed local even-cap sharpening

**Obligation:** W-EVEN-FORM (scoped); canonical W-ODD-NEG unchanged.  
**Parent:** merged EF05 PR #146, head d763297f9c98a72656222162fc60d6ad0445ff88.  
**Standing:** candidate explicit original signed local majorant. Focused final-head exact-rational validation required. Does not prove whole even-form positivity or RH.

## Why

EF05 certified on the physical even function \(f(x)=\cos(2\pi(19/25)x)\) that the old full SI10 conservative *upper cap* has energy \(>4.415423238009\), while the original positive operator has energy \(<2.639461066813\). Therefore the old **sufficient upper-cap** Schur cannot succeed. No negative witness against the true signed Weil form was established.

The old SI10 cover kept the archimedean lower bound for the integer 0 fixed across \([0,1]\), discarding its certified growth, and charged the signed-prime derivative across entire width \(1/64\).

## New signed envelope on [0,1] (full original elsewhere)

Keep the exact SI10/SM10 all-real protected-positive cover: 973 positive-half unresolved leaves, 107 clusters, and all seven original signed prime powers. The 64 old dyadic unresolved leaves covering \([0,1]\) each have width \(1/64\) and certified cap \(w_I=h_I+\kappa\), where \(\kappa=10^{-3}\).

Split each into four subcells \([a,b]\) of width \(1/256\). Evaluate SI07's exact rational 64-term Euler-plus-integral-tail archimedean **lower** at the **original leaf rational left endpoint** \(l\), rather than 0. With \(y=(333/106)l<\pi l\), the same monotone digamma formula remains a lower bound for all \(\xi\ge l\). At each subcell midpoint \(q\), SI06's original entire signed-prime interval \(p_{\rm low}(q)\) and global \(|p'|\le69\) give
\[
m(\xi)\ge L_{[a,b]}:=
\operatorname{arch}_{\rm low}(l)+p_{\rm low}(q)-69(b-a)/2,\quad \xi\in[a,b].
\]
Define the refined nonnegative upper weight by exact rational outward ceiling
\[
\boxed{w_{\rm new}([a,b])
=\min\{w_I,\ \lceil(\kappa-L_{[a,b]})_+\rceil_{10^{-6}}\}.}
\]
Outside \([0,1]\), **retain the original certified old upper cap unchanged**. Because both the old and local new weights dominate the true \(r=(\kappa-m)_+\), their pointwise minimum does too:
\[
0\preceq K_{\mathrm{true},e}
\preceq K_{\mathrm{cap,new},e}
\preceq K_{\mathrm{cap,old},e}.
\]
The full original signed operator and physical domain are unchanged. The new weight may fall below \(\kappa\) or to zero and is therefore integrated as a weight directly, not forced into the old \(h+\kappa\) parameterization.

## Mandatory same-vector physical feasibility pilot

Use EF05's **identical** physical even \(f(x)=\cos(2\pi(19/25)x)\) with the full exact zero-extended Fourier transform. The old \([0,1]\) cap contribution is rigorously **lower-bounded** using all 64 old SI10 leaves, lower-rounded rational center amplitudes and full midpoint derivative errors. The new \([0,1]\) cap contribution is **upper-bounded** on every one of 256 refined subcells by
\[
2\sum_{[a,b]\subset[0,1]} w_{\rm new}[a,b](b-a)
\bigl(|\widehat{Zf}((a+b)/2)|_{\rm up}
+\pi_{\rm up} B^2 (b-a)\bigr)^2_{\rm up}.
\]
Nothing in the \([0,1]\) band is discarded. Acceptance targets are old lower \(>4.415\), new upper \(<1.5\), and proven local drop \(>2.9\).

**This is NOT a full-global feasibility test.** The other original unresolved bands still contribute, and even a successful \([0,1]\) refinement cannot establish \(A_e\succeq K_{\rm cap,new,e}\).

## Full signed operator, moments and tail

Subdivisions do not change original 107 cluster endpoints, 890 physically supported even cosine-Taylor source directions, or their SI08 remainder orders. The new exact rational Hankel moment block on each affected cluster is
\[
C^{(j)}_{k\ell}=2\sum_{[a,b]\subset J_j}
w_{\rm new}[a,b]\frac{(b-c_j)^{k+\ell+1}-(a-c_j)^{k+\ell+1}}{k+\ell+1}.
\]
Changed blocks have strict rational LDL positive pivots; unchanged blocks retain EF04 exact certificates. If \(M_{\rm new}=\int w_{\rm new}<M_{\rm old}=1204033883/32000000\), then for \(b=24\), \(\tau=2^{-16}\), all original signed negative frequencies and every low/high cross term are paid by the operator Young inequality:
\[
K_{\rm true,e}\preceq(1+\tau)U C_{\rm new}U^*+\eta_{\rm new}I,\quad
\eta_{\rm new}=(1+\tau^{-1})\,2B M_{\rm new}\,2^{-48}<1.93\times10^{-8}.
\]
The 890-source positive-vs-negative inverse/Schur matrix remains **uncertified**.

## Decision and next step

If the exact replay succeeds, accept EF06 **only as a local genuine signed upper-envelope improvement** with the original full global tail preserved. EF07 should next bound the **entire** new cap energy on the same EF05 witness, including leaves outside [0,1], and obtain a full original \(A_e\) energy **lower** before investing in an inverse. If the new cap still dominates \(A_e\), sharpen the offending cells or prove a native RC carrier transport.

Replay command: python3 scripts/validate_rpb108_ef06_local_even_signed_cap.py

**W-EVEN-FORM, full original Weil, global bridge and RH OPEN.** Final-head exact-rational regression is mathematical evidence for stated inequalities, not independent peer review or a Lean attachment.
