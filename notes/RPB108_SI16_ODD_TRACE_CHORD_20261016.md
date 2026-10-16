# RPB108 SI16 — odd-only trace-concentration inverse bound and escape from the scalar-chord no-go

**Parent:** SI15 integrated at \`1fa9466a1d0f09e67cf46dc2128d6ff1d0e30a19\`.  
**Track:** Structural Investigation independent of RC334/335 original high signed Schur chain.  
**Scope:** a strictly stronger *certified upper bound for an actual original physically supported odd inverse quadratic response*. Not an evaluated inverse vector, a genuine new original operator residual trial, the full finite SI11 Birman–Schwinger matrix, Weil positivity, Stage I, F4, Lean, or RH.

## 1. Background: why SI14's >6.936 no-go need not apply here

SI11 decomposes the original CC27/RC312–313 Weil form \(Q=A-K\) with
\[
a(\xi)=\max\{m(\xi),\kappa\},\quad\kappa=1/1000,\qquad
A=Z^*\mathcal F^{-1}a\mathcal F Z+2|c\rangle\langle c|,\quad
c(x)=\cosh(x/2),
\]
in the **physical supported closed-form sense**, and negative odd pole \(2|s\rangle\langle s|\), \(s(x)=\sinh(x/2)\).

SI13 certified **the entire** positive-frequency interval \([0.22,0.38]\) and its reflection satisfy \(m(\xi)>7/5=1.4\), using the original signed seven-prime Fourier multiplier. SI14 aggregated three positive windows and proved an important no-go for the **unit-contraction scalar chord**
\[
(\kappa I+\delta T_J)^{-1}
\preceq\kappa^{-1}I-\frac{\delta}{\kappa(\kappa+\delta)}T_J
\quad\text{when }0\preceq T_J\preceq I.
\]
Even arbitrary positive windows do not make that **particular coarse chord bound** certify the required odd-pole Birman–Schwinger threshold \(\le1\). This does not obstruct a **strictly smaller spectral norm** \(\|T_J|_{H_{\rm odd}}\|<1\). SI16 exploits the compact-support/time-bandwidth information that SI14's comparison discarded.

SI15 independently established the first *genuine operator-domain odd trial* \(y=s/4800\) and complete original unprojected residual, but its conservative residual-upper \(\approx471.283\) did not outperform SI14's best \(<412.562\). SI16 refines the **inverse comparator**, not SI15's actual residual.

## 2. The new certified narrow signed positive-frequency window

Let \(B=11/10\) and the rational symmetric window
\[
J_+=[297/1000,303/1000]=[0.297,0.303],\qquad
J_-=-J_+,\qquad J=J_+\cup J_-.
\]
It lies **entirely inside SI13's independently certified signed-original positive interval**, so
\[
\boxed{m(\xi)>1.4=\kappa+\delta,\quad \delta=1399/1000,\qquad\xi\in J.}
\]
The SI16 exact-Fraction validator replays SI13's 128-subinterval all-frequency proof and explicitly requires \(m>7/5\), not merely a rounded sampled minimum.

Define the **physical time-limited frequency-concentration operator**
\[
T_J:=Z^*\mathcal F^{-1}\mathbf1_J\mathcal FZ\succeq0.
\]
It commutes with parity because \(J\) is reflection-symmetric. On the odd closed subspace \(H_o=\{f\in L^2([-B,B]):f(-x)=-f(x)\}\), positivity of the original signed multiplier and the original positive even pole give the **correct actual supported form comparison**
\[
\boxed{A_o\succeq\kappa I_o+\delta T_{J,o}.}
\]
No equality between compression and an unrestricted Fourier reciprocal is assumed.

## 3. Explicit odd time–bandwidth trace and strictly smaller spectral interval

The integral feature representation of \(T_J\) and the odd projection \(P_o\) yield its **exact** odd trace formula:
\[
\begin{aligned}
\operatorname{tr}_{H_o}(T_{J,o})
&=\int_J\|P_o e^{2\pi i\xi x}\|_{L^2([-B,B])}^{2}\,d\xi\\
&=\int_J\left(B-\frac{\sin(4\pi B\xi)}{4\pi\xi}\right)d\xi.
\end{aligned}
\]
In particular, using \(|\sin|\le1\), \(\pi>3\), the positive-frequency left endpoint \(l=297/1000\), and the *full symmetric* frequency measure \(4r\) with \(r=3/1000\),
\[
\boxed{
0\preceq T_{J,o}\preceq\tau I_o,\quad
\tau\le4r\left(B+\frac{1}{12l}\right)
<\frac{17}{1000}=0.017.
}
\]
This is a **support-sensitive odd-parity spectral bound**. The earlier SI13/SI14 chord paid \(T_J\preceq I\), losing nearly two orders of magnitude in the relevant norm.

For \(0\le t\le\tau\), the scalar inverse \(f(t)=(\kappa+\delta t)^{-1}\) is convex, so lies **below the secant between the actual endpoints \(0,\tau\)**:
\[
\boxed{
\frac{1}{\kappa+\delta t}
\le\frac1\kappa-
\frac{\delta}{\kappa(\kappa+\delta\tau)}t.
}
\]
The signed difference is explicitly nonnegative:
\[
\frac1\kappa-\frac{\delta t}{\kappa(\kappa+\delta\tau)}
-\frac1{\kappa+\delta t}
=\frac{\delta^2t(\tau-t)}
{\kappa(\kappa+\delta\tau)(\kappa+\delta t)}
\ge0.
\]
Thus, by inverse operator monotonicity on the **actual supported odd space** and spectral functional calculus for the positive compact \(T_{J,o}\),
\[
\boxed{
A_o^{-1}
\preceq\kappa^{-1}I_o-
\frac{\delta}{\kappa(\kappa+\delta\tau)}T_{J,o}.
}
\]
**This does not contradict SI14's scalar-chord no-go:** the old proof fixes the coarse unit spectral endpoint \(1\), while SI16 proves and pays the much smaller odd-sector endpoint \(\tau<0.017\).

## 4. Original odd Fourier energy on the entire narrow window

SI13's exact rational Fourier integral at \(\xi_0=3/10\) proved
\[
|\widehat{Zs}(3/10)|>541/1000,
\]
and the original physical first-moment derivative bound proved
\[
\left|\frac{d}{d\xi}\widehat{Zs}(\xi)\right|<2873/1000.
\]
These strict rational statements are **rechecked** by SI16 from SI06's Machin \(\pi\) enclosure and SI12's \(\sinh,\cosh\) Taylor intervals.

Every \(\xi\in J_\pm\) is within \(r=3/1000\) of its reflected center. Therefore
\[
|\widehat{Zs}(\xi)|
>\frac{541}{1000}-\frac{2873}{1000}\frac3{1000}
\quad(\xi\in J_+),
\]
and the same squared lower applies on \(J_-\). Consequently,
\[
\boxed{
\langle s,T_{J,o}s\rangle=
\int_J|\widehat{Zs}|^2
>E:=4r\left(\frac{541}{1000}
-\frac{2873}{1000}r\right)^2
>\frac{33}{10000}.
}
\]
The physical norm is \(\|s\|_2^2=\sinh B-B<235648/10^6\).

## 5. New actual odd inverse upper, not merely a rank bound

Combining the physically supported operator inequality with the exact original odd Fourier mass,
\[
\boxed{
2\langle s,A_o^{-1}s\rangle
<
\frac{2(\sinh B-B)}{\kappa}
-\frac{2\delta E}{\kappa(\kappa+\delta\tau)}
<78.
}
\]
Every displayed rational inequality is asserted in SI16's standard-library exact-Fraction validator; any reported decimal is only a human-readable display of its already paid rational bounds.

Comparison of certified **upper bounds on the same original inverse quadratic response**:

| Frontier | Bound on \(2\langle s,A^{-1}s\rangle\) | Mechanism |
|---|---:|---|
| SI12 | \(<471.295\) | scalar \(\kappa I\) floor, even pole has no odd action |
| SI13 | \(<413.753\) | one positive signed Fourier window with unit contraction |
| SI14 | \(<412.562\) | three certified positive windows with unit contraction |
| SI15 | \(<471.283\) | first genuine supported odd trial with **full native residual** |
| **SI16** | **\(<78\)** | **narrow window + rigorously certified odd time–bandwidth spectral norm** |

The SI16 upper remains far above the Birman–Schwinger threshold \(\le1\). It does **not** assert that the actual odd response is 78, has decreased from an earlier value, or corresponds to a negative Weil direction. The improvement is in what we can **rigorously certify** about the same fixed supported inverse.

## 6. Strategic consequence and SI17

This demonstrates that the **carrier/support constraints affect inverse upper bounds quantitatively**, not just qualitatively: the odd time-frequency concentration operator has trace/norm \(<0.017\), so the frequency-positive information can be exploited far more effectively than through the global unit-contraction chord.

A narrow window is not mathematically the whole story. The remaining task is to combine **multiple appropriately normalized odd local concentration directions**, or use an actual full residual in the stronger supported reference, and determine whether the odd inverse ceiling can approach \(1\). Directly applying SI15's weak \(\kappa I\) residual bound will not.

**SI17:** certify a finite collection of supported odd time-frequency concentration features with original signed multiplier positivity, and a correct joint spectral comparison that retains the small odd concentration norms. Alternatively construct a nontrivial genuinely supported odd trial with its original residual Gram and reference-inverse upper. Compare against RC334/335 and do not redirect Stage I until actual complete-form Schur or Birman–Schwinger margins are established.

No full original signed Weil positivity, Stage I closure, F4 bridge, complete Lean proof, or RH result is claimed.

## Replay

\`python scripts/validate_rpb108_si16_odd_trace_chord.py\` (uses SI06, SI12 and SI13 exact source routines). GitHub structural Actions should run all SI validators on the branch. The analytic operator inequalities use spectral calculus, parity projections, Plancherel and trace-class Bochner integration; regression asserts the fully explicit rational numeric margins but is not Lean formalization or independent mathematical peer review.
