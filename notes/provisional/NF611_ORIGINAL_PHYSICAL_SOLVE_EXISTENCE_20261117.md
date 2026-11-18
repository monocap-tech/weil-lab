# NF611 — exact transformed physical solve existence from the residual row test

Stacked on NF610 #641, head 5f6548ef. At initial inspection NF610 run 44223274315 was queued; no new gamma/pole/prime/physical dictionary acceptance is claimed.

Let A=D^T H D and b=D^T V w be the literal unweighted historical physical system. The accepted NF606 residual estimate was conditional on an exact transformed solution. This extra hypothesis is mathematically redundant: if Ax=Az, use the same residual estimate with y=x, y0=z, rhs=Ax and r=0. Every |x_i-z_i| is at most 0, giving injectivity. As the linear operator is an endomorphism of the finite-dimensional real vector space R^242, injectivity implies surjectivity. Thus for every rhs there exists exactly one real transformed solution. The same actual row bounds, rhs residual and frame payment inequalities imply its selected coordinates lie in the frozen box. No interval LU theorem, matrix inverse evaluation or additional row bound is required.

New theorem candidates independently establish the finite-dimensional existence/uniqueness result and a physical corrected-margin transfer that asserts existence of the solution, its box membership, graph, and smooth real odd moment-matching sequence. Local smooth coercivity remains an explicit premise c>d>0. The frame remains a parameter; identifying it with the historical exact dyads and attaching actual analytic H,V enclosures to the Arb row evidence are still necessary. This does not by itself establish original untransformed system equivalence for an arbitrary D or close global Weil positivity/RH.

NF606 real residual and NF608 conditional strict margin are previously accepted. New NF611 declarations await compiler and axiom audit; no local build, new Arb replay, or main merge.
