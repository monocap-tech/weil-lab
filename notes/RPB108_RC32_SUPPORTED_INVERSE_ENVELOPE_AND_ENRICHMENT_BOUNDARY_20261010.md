# RPB108 RC32 — supported inverse envelope and trial-enrichment boundary

2026-10-10. Branch research/rpb108-route-consolidation.
Recovered parent 3f91a9e59fea1467aff013b6157ec5165ab28cb1 (RC31).

## Result

At B=11/10 the canonical metric has the supported physical floor

    ||h||_D^2 >=(257/252)||h||_2^2.

Consequently the full Riesz response matrix for the eight physical
Legendre moments satisfies C<=(252/257)D. Substituting this into RC31
improves its actual computed collective residual envelope from
51/100 to 49/100 in the physical input metric.

A stronger floor 1017/997 is also proved below. It supplies an exact
diagnostic: the envelope using 252/257 has an unavoidable bound-matrix
floor 55/261369, independently of trial dimension. This is NOT a
lower bound on actual residuals. It proves why refining only the
finite solve cannot make that particular estimate arbitrarily small.

## Supported Fourier floor, with normalization

For supported f on [-B,B], Cauchy--Schwarz gives
|fhat(xi)|^2<=2B||f||_2^2 in RC24's Fourier convention.
Hence the mass in [-Omega,Omega] is <=4B Omega ||f||_2^2.
For 0<Omega<1/(4B), the logarithmic metric therefore satisfies

    ||f||_D^2 >=[1+(1-4B Omega)log(1+Omega/e)]||f||_2^2.

Indeed subtract the baseline log(e)=1, discard its nonnegative
contribution inside the frequency band, and use its monotone lower
bound outside. This is a bound on the full supported metric, with
no finite frequency discretization or omitted tail.

For x>=0, integration of 1/(1+t) on [0,x] gives
log(1+x)>=x/(1+x). If e<A, this yields

    lambda_A=1+(1-4B Omega)Omega/(A+Omega).

Take Omega=5/44; then 1-4B Omega=1/2. The rational upper bounds
e<11/4 and e<87/32 give respectively

    lambda_(11/4)=257/252,
    lambda_(87/32)=1017/997.

The exponential series through degree 8, with the remaining tail
bounded by (1/9!)/(1-1/10), certifies both e upper bounds.
The floors apply to all supported canonical vectors and hence all
trial spaces, including vectors with nonzero endpoint traces.

The inclusion has norm squared <=1/lambda_A. Taking the adjoint gives
C<=D/lambda_A. This is a positive metric statement, not a claim about
the original signed Weil form.

## Updated executed residual data

Retain RC31's actual trial response lower matrix L=J-EH.
Define U_rho=rho D-L, rho=252/257. Then its actual canonical
residual Gram obeys Z<=U_rho. Exact rational Schur tests verify

    0<=U_rho<=(49/100)D.

Approximate per-column canonical error upper displays are

    0.34561, 0.32227, 0.29610, 0.27506,
    0.26041, 0.24705, 0.24083, 0.23098.

They are bounds rather than evaluated errors. The certificate stores
the rational upper matrix; no square-root display is used in proof.

## Why this envelope cannot certify arbitrary accuracy

For ANY lawful trial frame, its variational response lower bound L
satisfies L<=C. The stronger supported floor gives C<=(997/1017)D.
Therefore the envelope with rho=252/257 necessarily obeys

    U_rho=rho D-L
      >=rho D-C
      >=[252/257-997/1017]D
      =(55/261369)D.

This bound-matrix floor exceeds (1/400)^2. Thus even exact trial
integration and arbitrarily many trial modes cannot make THIS
envelope establish a collective canonical error <=1/400 of physical
input norm. That number is an illustrative accuracy target, not an
assertion that it is RC23's Riesz-vector tolerance.

Using the stronger floor improves the generic upper bound too, but a
single uniform inverse-norm bound does not encode the actual low-mode
response. If exact Galerkin trials converge to full responses, the
generic envelope tends to rho D-C, while the actual error tends to zero.
The two quantities must not be confused. No obstruction to convergence
or accurate Riesz approximation is proved.

## Execution and next obligation

Run:
python scripts/validate_rpb108_rc32_supported_inverse_envelope.py

It loads RC30's certificate, recomputes RC31's exact solves, verifies
the Fourier-budget constants and e bounds, and tests all updated matrix
inequalities by exact rational Schur elimination. Local run: PASS.

The next useful computation is the attached physical residual
p_j-L_B v_j, retaining endpoint logarithms, or a response-specific
upper bound on C. Trial-space enrichment may help those computations,
but cannot by itself remove the looseness of the generic envelope.

Native original head/source positivity, aperture extension, RH/F4,
and Lean closure remain open. Other branches are unchanged.
