# NF365 — Exact form projection retyping before the positive exterior solve

Status: bounded mathematical correction (analytic, not native-CI). Unchanged original J242, W=A_star-Kminus. W-ODD-NEG and RH OPEN.

Let A=A_star>=kappa_star I>0, let a be the complete closed positive form on the supported odd Hilbert H, J=J242 finite dimensional in D(a), F=J^perp, P the physical projection, Q=I-P. Let H_F be the positive operator associated with the restricted form a|F. Its Riesz equation defines for any f in D(a) the unique v_f in F∩D(a) such that

  a(v_f,z)=a(f,z) for all z in F∩D(a).

Set e_f=f-v_f. Then a(e_f,F)=0, so e_f lies in the A-energy-dual finite subspace A^-1 J. If f=p+q with p=Pf, q=Qf, the form-domain invariance of P implies

  v_f=q+v_p,     e_f=p-v_p.                      (1)

The energy-dual component depends ONLY on the physical selected projection p, not the physical residual q. If p is in Dom(A), the true exterior forcing is QAp and

  v_p=H_F^-1 QAp.                                (2)

Given a trial y in the exterior form domain, define the matched residual functional R_y(z)=a(p-y,z). The exact error identity is

  a(v_p-y,v_p-y)=||R_y||^2_{(F,a)^*}.             (3)

If Q A(p-y) has a strong physical representative, the inherited positive exterior floor H_F>=kappa_star yields the sufficient bound

  a(v_p-y,v_p-y)<=||Q A(p-y)||²/kappa_star.      (4)

Finite probe tests alone only lower-bound the complete dual residual norm.

## No-go for physical-closeness substitution

For N>0 use the exactly positive definite two-by-two example

  A_N=[[N²+2,N],[N,2]],   J=span(e1), F=span(e2).

Since A_N-I=[[N²+1,N],[N,1]] has determinant 1 and positive first diagonal, A_N>=I. Yet f=e1 lies EXACTLY in J, so Qf=0, while v_f=(N/2)e2 and e_f=e1-(N/2)e2, arbitrarily far from the physical projection. The old tiny physical quotient residuals cannot certify a tiny A-energy correction.

## Computational consequence

NF363/364 high-frequency bounds on the original critical f_i remain valid, but they cannot be silently used for p_i=Pf_i. Compute p_i using the accepted physical J242 frame, and certify its own endpoint/Fourier tail and a correlated selected-space approximation of A p_i; only then attempt the first matched positive exterior solve. The strong-action pole cancellation Qs=0 is valid but does not make Q A_o s vanish.


## Equivalent matched implementation (important correction)

It is **not mandatory** to compute the positive forcing from p=Pf rather than from the original f. The original-source solve remains valid if its exterior trial includes the physical quotient exactly. For any exterior trial y_p, put y_f=q+y_p, with q=Qf. Then

  a(f-y_f,z) = a(p-y_p,z)  for every z in F∩D(a),

so their complete matched residual functionals, energy error and certificates are **identical**. In particular, original f high-frequency estimates remain useful when they control the actual matched residual of f-y_f. What is invalid is treating the tiny L² norm of q as permission to omit q from the trial or to transfer f's Fourier-tail bound automatically to p.

The correct bounded feasibility comparison is between two *matched* candidates: (i) certify Q A(f-y_f) for an explicitly fixed y_f∈F, or (ii) certify Q A(p-y_p) for an explicitly fixed y_p∈F, with y_f=q+y_p. Choose the representation with the better correlated analytic/error budget; neither establishes a bound without whole-frequency residual control.

STOP: No new directions, no 242-dimensional inverse, no signed sign inference, no upgrade of original realization/CI status. Next: one actual projected p_i and a matched residual criterion, with all positive/negative source and infinite complement terms retained.
