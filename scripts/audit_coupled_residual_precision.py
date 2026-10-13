"""Exact arithmetic audit of two recorded approximate matrices, not of zeta."""
from fractions import Fraction as F
from pathlib import Path
import json


def audit():
    path = Path(__file__).resolve().parents[1]/'notes/data/RPB108_COUPLED_RESIDUAL_PILOT_20261005.json'
    data = json.loads(path.read_text(),parse_float=F)
    a,b = data['results']
    differences = [abs(b['residual_gram'][n][n]-a['residual_gram'][n][n]) for n in range(8)]
    index = max(range(8),key=differences.__getitem__)
    discrepancy = differences[index]
    budget = F(1,10**6)
    assert discrepancy > F(4,10**5) > 2*budget
    return dict(status='exact audit of recorded approximations only',
                largest_diagonal_discrepancy_index=index,
                largest_diagonal_discrepancy=str(discrepancy),
                tested_operator_error_budget=str(budget),
                both_approximations_within_budget_impossible=True,
                at_least_one_operator_error_lower_bound=str(discrepancy/2),
                actual_residual_gram_enclosed=False,actual_schur_sign_certified=False)


if __name__ == '__main__':
    print(json.dumps(audit(),indent=2))
