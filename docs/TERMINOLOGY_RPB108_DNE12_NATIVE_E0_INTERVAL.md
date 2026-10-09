# RPB108 DNE12 — complete constant-mode source-square interval terminology

**DNE12 source object:** At the fixed original Weil aperture a=53/50, let e0(x)=1/sqrt(2a) on (-a,a), zero-extended elsewhere. L_Q is the FULL original supported physical source action of CC56, containing the native digamma archimedean symbol, all active prime-power translations 2,3,4,5,7,8 with both orientations, and BOTH original Hermitian pole-source terms. Unlike H, L_Q has its original pole source.

**Exact even source quotient:** For x in [0,a), define S0(x)=sqrt(2a)*L_Qe0(x), so

    S0(x)=a0+J(a-x)+J(a+x)
          -sum_(n in {2,3,4,5,7,8}) c_n
             [1_(x+log n<a)+1_(x-log n>-a)]
          +8 sinh(a/2)cosh(x/2),

where a0=psi(1/4)-log pi=-gamma_E-pi/2-3log2-log pi, c_n=Lambda(n)/sqrt(n), and J(t)=atanh(exp(-t/2))+atan(exp(-t/2)). The full source-square is exactly ||L_Qe0||_2²=(1/a)int_0^a S0(x)^2 dx.

**Monotone prime panel:** On each positive-half subinterval not crossing an original prime translation cut, the archimedean part is strictly increasing, as d/dx[J(a-x)+J(a+x)]=j(a-x)-j(a+x)>0 for x>0. The positive even pole source is also increasing. The prime contribution is constant inside each native panel. Thus interval values at subpanel endpoints bound S0 and S0² on that entire subpanel.

**Directed interval computation:** Interval `mpmath.iv` arithmetic at 35 decimal working digits, with 60000 equally spaced subpanels over [0,a-10^-8], encloses the normalized interior integral strictly between 0.08342746 and 0.08450131. The first and last subpanel interval endpoints are rational and original prime translations are bracketed by outward interval logs.

**Endpoint analytical tail:** For t=a-x in (0,10^-8), use J(t)=-(1/2)log t+log2+pi/4-int_0^t r(s)ds and |r(s)|<5; all six prime terms contribute exactly -sum c_n. The remaining continuous source bounded in absolute value by10. Thus the normalized endpoint square is at most

    delta/a*[1/4*(L²+2L+2)+10*(L+1)+100],
    delta=10^-8, L=-log(delta),

less than 3.668*10^-6. This bound pays the unbounded endpoint logarithm; a bounded sampled value at x=a is NEVER used.

**Native e0 squared-source certificate:** Combining full interior and endpoint bounds gives

    0.0834 < ||L_Q e0||_2² < 0.0846.

This is a computational interval certificate, not an independently formalized Lean proof.

**E0 projection:** From the authenticated NF12/CC40 original Q(e0,e0) rational interval, 0.0015 < Q(e0,e0)^2 < 0.0017. Consequently the true physical source residual after projection onto only span{e0} has

    0.0817 < ||(I-|e0><e0|) L_Qe0||² < 0.0831.

The latter is NOT the residual after projecting out the other55 retained EVEN E112 modes, nor the NF21 58-mode compensated high-source Gram. These distinctions are mandatory.

**DNE12 status:** The fixed scalar source square is enclosed with original signed source covariance; full E112/58 source Gram, complete high inverse and DNE9 reflected null LMI remain open.
