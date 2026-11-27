# V10B44 recovered frozen-coordinate replay

Derived V10B29 file SHA256: 1fea00167929e3f5312c16dcd680154a34ead4b8934a520c7a23fd60e79e8c5f
Parent frozen_coefficients.json SHA256 recorded by V10B29: bccbd53fd2e02cb887868f588ef7f8765e780086f7fabe748518d5685d7c7616
The original V10B19 archive was not accessible. The derived JSON was reconstructed from indexed Library text (377528 bytes), and its SHA256 matched the committed V10B29 conversion script's expectation.
Independent binomial conversion: 2560/2560 physical monomial coefficients PASS.
The following uses row-scaled normalized constraints, not the physical energy matrix.
Rows 0..14: v[j][i]/2^48. Row 15: sum_{k=0..9} 31/(31+4k)*c[k]*v[j][15+2k]/2^48.
Last-row entry reserve: 31*sum_i |v[j][i]|/2^48 * 10^-25, conditional on literal load enclosure and Legendre bound in L1 <= 1.
Exact rational comparison (decimal diagnostics below):
[
  {
    "N": 16,
    "minimumScaledRowMargin": 1.0675083127611842,
    "allPositive": true,
    "highRowMargin": 2.9837542236464962,
    "rowMargins": [
      1.0675083127611842,
      1.5216284673662273,
      1.577779959999134,
      1.7774022384143926,
      1.8845941200544303,
      2.031827194773733,
      2.1333939216498337,
      2.2550222321908713,
      2.348919676441927,
      2.4557170096123713,
      2.5437097634186365,
      2.6411032663778755,
      2.7248343429973403,
      2.8160082343219486,
      2.896737873723527,
      2.9837542236464962
    ],
    "highRowTotalReserve": 1.8925908781524286e-22,
    "minExceedsOne": true
  },
  {
    "N": 17,
    "minimumScaledRowMargin": 1.0675083127611842,
    "allPositive": true,
    "highRowMargin": 2.9837542236464993,
    "rowMargins": [
      1.0675083127611842,
      1.5216284673662273,
      1.577779959999134,
      1.7774022384143926,
      1.8845941200544303,
      2.031827194773733,
      2.1333939216498337,
      2.2550222321908713,
      2.348919676441927,
      2.4557170096123713,
      2.5437097634186365,
      2.6411032663778755,
      2.7248343429973403,
      2.8160082343219486,
      2.896737873723527,
      2.9837542236464993
    ],
    "highRowTotalReserve": 1.8925908781524286e-22,
    "minExceedsOne": true
  }
]
No native certification of optimized coverage or parent archive custody is asserted.
