# Terminology registry — GERM-81 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with GERM-80, the pre-65 refold, and GERM-73's correction of GERM-72. Historical definitions are not rewritten.

## Post-chi7 excess and retained sections

The new parameter is `t=e-e80=delta-chi7`, where `delta=e-e76`. It is not the physical argument of the scalar profile. Retain `sigma=sigma8`, `rho=rho9=psi7-3sigma`, `c=c10=sigma-rho`, and `omega10=sigma-10c`.

The theorem range is `0<t<=sigma8`. The sixth, seventh, eighth, and ninth maps have their own distinct formula ranges; no name implies a common unrestricted scope.

## GERM-81 matrix namespace

The sixth atoms are `A19=B14,19`, `E19=B15,19`, and `E20=B15,20`. E19 is the newly admitted GERM-80 stopping atom.

The downstream names below are **GERM-81-local**. In particular, repeated labels U0, U1, V0, V1, P, Q, R, S are not assertions that the earlier matrices with those labels remain unchanged. Products act rightmost first; the verifier stores chronological words.

| Name | Chronological source word |
| --- | --- |
| U0 | E20,E20,A19 |
| U1 | E20,E20,E19 |
| V0 | E20,E20,A19,E20,A19 |
| V1 | E20,E20,E19,E20,A19 |
| A0, A1 | V0,U0 and V1,U0 |
| B0, B1 | V0,U0,U0 and V1,U0,U0 |
| P, Q | A0,B0,B0 and A1,B0,B0 |
| R, S | A0,B0,B0,B0 and A1,B0,B0,B0 |

Thus U/V mean seventh nonwrap/wrap, A/B mean eighth return lengths two/three, and the subscript is the initial source bit relative to `(0,t)`. At the ninth level P/Q have length three and R/S length four; Q/S have interior initial source.

The unchanged tenth section is `(0,c10)` in the ninth coordinate, with physical field `W(t0+y)` and `t0=h-beta+gamma-xi+2eta7`. No section coordinate is silently identified with the physical coordinate.

## One-chart complete-return library

Low parameter range: `R^(N-1) P` or `R^(N-1) Q`. High parameter range: `S^s R^(N-s-1) Q`, for `N=10,11`, `0<=s<N`. There are 23 distinct words, with 25 parameter-domain cells because two words are shared.

The chart is `C81=[[1,1],[-8/5,8]]`; its factor 75 applies per complete tenth return only. Overall signs are retained in the recurrence.

The next changed ninth word is `B1 B0^2 A1`, chronologically A1,B0,B0,B1. Its source domain must be proved separately above `t=sigma8`; it is not the old S matrix.
