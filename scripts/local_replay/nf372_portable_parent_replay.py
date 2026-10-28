#!/usr/bin/env python3
"""NF372 portable GitHub CI replay from SHA-verified *extracted parent fields*.

The parent snapshots were extracted locally from the two complete, SHA256-pinned
original GitHub Actions ZIP artifacts. The original NF372 script independently
verified those complete archives in its local run. This portable CI checks the
exact bytes of each recorded field subset and replays the same Fraction gates,
but does NOT independently retrieve/revalidate original full parent archives.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / 'scripts'))
import nf372_exact_source_tail_and_generic_stop as original

PINS = {
    'PR355': 'abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770',
    'NF369': '3e73a12bbd70158a461d9722dc8fc499eee8d17baf0afc9090bac5d10165e7e8',
}
NAMES = {'PR355':'original_exterior_refined_mixed.json',
         'NF369':'nf369_actual_critical_quotient.json'}

def load_field_snapshot(path, archive_sha, member, member_sha=None):
    blob = Path(path).read_bytes()
    row = json.loads(blob)
    custody = row['custody']
    kind = custody['kind']
    assert kind in PINS
    assert hashlib.sha256(blob).hexdigest() == PINS[kind], kind
    assert custody['parent_original_archive_sha256'] == archive_sha
    assert custody['parent_original_json_sha256'] == member_sha
    assert custody['member'] == member == NAMES[kind]
    return row['data']

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--pr355',required=True)
    p.add_argument('--nf369',required=True)
    p.add_argument('--report',required=True)
    a=p.parse_args()
    original.read=load_field_snapshot
    sys.argv=['nf372_original.py','--pr355',a.pr355,'--nf369',a.nf369,'--report',a.report]
    original.main()
    print('PORTABLE PASS: matching original NF372 Fraction gates on pinned extracted fields')
    print('LIMIT: original full parent archive SHA verification is inherited from local source replay, NOT independently rerun by this portable CI')

if __name__=='__main__': main()
