"""Lossless common-denominator and common-tail encoding of quantized sources."""
from copy import deepcopy
from fractions import Fraction as F


def expand_sources(encoded):
    result=deepcopy(encoded)
    if result.get('coefficient_encoding')!='integer numerators with common decimal denominator and row tail':
        raise ValueError('Unsupported source encoding')
    denominator=10**result['coefficient_grid_digits']
    for row in result['rows']:
        tail=row.pop('common_high_degree_numerators')
        for panel in row['panels']:
            numbers=panel.pop('low_degree_numerators')+tail
            panel['coefficients']=[str(F(n,denominator)) for n in numbers]
    del result['coefficient_encoding']
    return result


def compact_sources(result):
    encoded=deepcopy(result);denominator=10**result['coefficient_grid_digits']
    for row in encoded['rows']:
        cut=row['degree']+1
        numbers=[]
        for panel in row['panels']:
            values=[F(c)*denominator for c in panel.pop('coefficients')]
            assert all(x.denominator==1 for x in values)
            numbers.append([int(x) for x in values])
        tail=numbers[0][cut:]
        assert all(n[cut:]==tail for n in numbers)
        row['common_high_degree_numerators']=tail
        for panel,n in zip(row['panels'],numbers):panel['low_degree_numerators']=n[:cut]
    encoded['coefficient_encoding']='integer numerators with common decimal denominator and row tail'
    assert expand_sources(encoded)==result
    return encoded
