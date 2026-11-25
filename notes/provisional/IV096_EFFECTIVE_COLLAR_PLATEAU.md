# IV096: effective collar plateau — mathematical construction, not a Lean receipt

Use c=1099/1000, p=1/8000, q=1/4000, h=1/2000.
Let b be the real Mathlib ContDiffBump centered at zero, inner radius p, outer radius q. Let rho=b/(integral b). Define

    s(x) = integral from x-c-h to x-c+h of rho(t) dt

and embed real values into C. The function is C-infinity by the fundamental theorem of calculus and smoothness of rho, and compactly supported inside the original right collar since h+q=3/4000<1/1000. It is exactly one on |x-c|<=h-q=1/4000. Since b>=0 and b=1 on [-p,p], integral b>=2p=1/4000; 0<=rho<=4000. The derivative is rho(x-c+h)-rho(x-c-h), so its absolute value is at most 4000 (not 8000), and it vanishes outside the closed support interval. Hence

    mass = integral |s|^2 >= 1/2000
    derivative energy <= 4000^2 * (3/2000) = 24000
    derivative energy / mass <= 48000000.

The exact arithmetic clearance at N=20000 is
    5 * 48000000 = 240000000 < 20001^2 = 400040001.
Thus the IV096 receiver would give the finite 1/5 physical mass margin at M=10 for all N>=20000. The original NF600 margin is 2/5.

Status: the concrete plateau definition, smoothness, support, derivative bound and integral bounds are mathematical derivations recorded here, not yet Lean declarations or native receipts. IV096 formalizes the smooth-carrier quantitative tail and numerical receiver separately. The earlier IV095 existential bump is not automatically this plateau. No global positivity, Green attachment or RH conclusion.
