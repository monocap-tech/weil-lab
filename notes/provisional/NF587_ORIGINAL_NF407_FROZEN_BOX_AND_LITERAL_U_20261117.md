# NF587 — frozen NF407 native coefficient box and literal original U

Stacked on NF586 #617. New Lean proof scripts and independent new Arb replay pending.

## Fresh verified receipts

NF586-head run 44110451033 job 134134278957, and run 44110447813 job 134134269847, both accepted the entire NF584 logarithmic mass and proper interval complex integration-by-parts module. The second split module failed on const-sub elaboration, a cast of inverse and the |* lexer. Repairs in NF587 use the pinned HasDerivAt.const_sub API, push casts on the goal and whitespace. Twisted derivative still failed; direct const_sub repair also committed. Other NF586 jobs were running at inspection.

## Actual original source custody

Fetched 370586 bytes of the exact NF407 physical coefficient JSON; SHA256 recomputed independently from fetched bytes:
0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce.
Matches NF493/NF494/NF577 historical source. SHA implementation self-tested with abc. Exported ALL 242 selected primitive midpoint/radius pairs and ALL 4 critical pairs losslessly as integer mantissa/exponent pairs in four chunk modules and a frozen data module. All four critical shapes preserve their exact 32 rational sine coefficients and exact sinh coefficient. Re-fetched committed Lean tables and independently compared all 246 pairs, all 241 node pairs, 32 frequencies, 128 sine coefficients, 4 pole coefficients, and the last true selected sinh pole. Exact source nodes agree with expansion of the authentic 67 NF545 oscillator groups. Unique grouped oscillator modes =273. These operational checks passed; no local Lean compiler used.

New Lean source-binding candidate defines
U_{a,b}(x)=sum_{j<242} a_j j_j(x)+sum_{r<4} b_r K_r(x),
with K_r the actual critical sine/sinh shapes. a,b may be ANY real coefficient choices in the frozen primitive box, not only the dyadic midpoints. Regularity and derivative continuity are independent of the choice. The corrected-carrier wrapper substitutes this literal U, uses its actual derivative, and requires a uniform box collar-bound certificate plus membership of the chosen source in that box. This does not prove that the exact original correlated solve is in the archived box.

## Source envelope

Fresh exact BigInt rational checks: every primitive midpoint absolute value plus radius <10^143; all critical shape coefficients <=1 in absolute value; radii nonnegative. Coarse complex disc bound: for |d|<=1/25, |B-d|<2; f<883, k<=13, |Im(2*pi*f*(B-d))|<283 using pi<4. Complex sin/cos have norm <=exp(|Im|)<3^283; the sinh pole is <3. At most 242+4*(32+1)=374 primitive summands. Exact integer arithmetic verifies 400*10^143*2^13*3^283<10^400. Thus the inherited Cauchy majorant follows analytically from the full original box, without relying on rounded samples. Formal complex-analytic majorant and Taylor bridge still open.

Replayed NF494 raw archive using exact Fraction arithmetic in the active runtime; source SHA and raw archive SHA agree. All 400 intervals yield
M0 <= 1.9659655557684862e-7 <2e-7,
M1 <= 0.0006957098822919963 <7e-4,
U(B) upper <= -1.16798644909683e-11.
The inherited Cauchy tail0 and derivative tail1 are approximately 4.0764e-121 and 8.1539e-116. This is a fresh arithmetic replay of the existing interval evidence, not a fresh Arb recomputation.

New independent replay script uses full primitive interval balls directly (not midpoint+assumed radius fee) and computes normalized Taylor coefficients v_n=[d^n]U(B-d)*delta^n, all 400, at 4096 bits. It compares exact outward rational mass and derivative sums against the historical bounds. Full source input is audited independently using Python SHA256/Fraction before the numeric run. CI pending: python-flint not installed locally. No claims about its outcome yet.

## Disposition

Source representation/data alignment now operationally established and literal source family introduced in Lean. Not yet formal certification of the uniform U/U' inequalities or original correlated-solve coefficient custody; numerical intervals are not Lean proof terms. NF586 correction and full endpoint graph still compiler-pending. No main merge. Full signed Weil coercivity, W_ODD_NEG, RH OPEN.
