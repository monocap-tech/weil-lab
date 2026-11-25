"""Source-only check of F41 aggregation candidate: not a Lean proof."""
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def expected(i):
    rr=f'{i:03d}'
    if i<8:return ('WeilDefect.Generated.NF702Inputs.Attach'+rr,'nf702Attach'+rr+'ActualPayment')
    if i<48:return ('WeilDefect.Generated.NF707.Attach'+rr,'nf707Attach'+rr+'ActualPayment')
    k=f'{2*i-93:03d}'
    return (f'WeilDefect.Generated.F41{k}.Attach{rr}',f'f41{k}Attach{rr}ActualPayment')
def validate(plan,source):
    rows=plan['rows']
    assert plan['schema']=='F41-aggregate-source-plan-v1'
    assert [r['row'] for r in rows]==list(range(242))
    assert [(r['module'],r['theorem']) for r in rows]==[expected(i) for i in range(242)]
    assert len(set(r['module'] for r in rows))==len(set(r['theorem'] for r in rows))==242
    assert re.findall(r'^import (WeilDefect\.Generated\.\S+)$',source,re.M)==[r['module'] for r in rows]
    assert re.findall(r'^  · exact (\w+)$',source,re.M)==[r['theorem'] for r in rows]
    assert 'neutralNF674Rows_imply_original_entry _ _ f41OriginalAllRows' in source
    assert 'neutralNF674Rows_sound _ _ hM f41OriginalAllRows' in source
    assert 'hM : neutralNF624AllMomentsSound' in source
    assert plan['bank']=='neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank)'
    assert plan['payment']=='nf702OriginalInputs.payment'
    assert source.count(plan['bank'])==3
    assert not re.search(r'\b(sorry|admit|axiom)\s',source)
def main():
    plan=json.loads((ROOT/'plan.json').read_text())
    source=(ROOT/'AllRows.lean.in').read_text()
    validate(plan,source)
    tests=[source.replace('  · exact nf702Attach000ActualPayment\n','',1),
           source.replace('nf707Attach008ActualPayment','nf707Attach009ActualPayment'),
           source.replace('import WeilDefect.Generated.F41003.Attach048','import WeilDefect.Generated.F41005.Attach049'),
           source.replace('hM : neutralNF624AllMomentsSound','hM : True'),
           source.replace('neutralNF674Rows_imply_original_entry','neutralNF674Rows_sound')]
    for bad in tests:
        try:validate(plan,bad)
        except AssertionError:pass
        else:raise AssertionError('bad aggregation candidate accepted')
    print('242 exact import/theorem routes, 5 source mutations rejected; no Lean')
if __name__=='__main__':main()
