#!/usr/bin/env python3
"""PR #355 descendant: portable provisional NF358--364 exact-rational replay.

This checks selected archived native output and mathematical algebra ONLY.
It does not recompute parent Arb native enclosures, review analytic lemmas,
or certify W-ODD-NEG/RH. NF356 enhanced-floor proof is NOT certified here.
"""
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile, urllib.request
from pathlib import Path
BASE = Path(__file__).resolve().parents[2]
DATA = BASE/'notes/data/provisional'
SCRIPTS = BASE/'scripts/local_replay'
URL = 'https://api.github.com/repos/monocap-tech/weil-lab/actions/artifacts/{id}/zip'
PARENTS = {
    'nf361-pr348-fourmode.zip': (12738593751,'735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968'),
    'pr350-certificate.zip': (12752629674,'3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09'),
    'pr355-exterior.zip': (12776684037,'f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'),
}
REPLAYS = [
    'nf358_residual_probe_replay.py',
    'nf359_energy_dual_entry.py',
    'nf360_energy_dual_242_preflight.py',
    'nf361_critical_transfer_no_go.py',
    'nf362_directional_neumann_gate.py',
    'nf363_critical_sine_tail_higher.py',
    'nf363_independent_tail_replay.py',
    'nf364_split_tail_exact.py',
    'nf364_independent_replay.py',
]
# Scripts which change a report regenerate the exact report carried in custody.
BASELINE_REPORTS = {
    'nf358_residual_probe_replay.py':'nf358_residual_probe_projection.json',
    'nf359_energy_dual_entry.py':'nf359_energy_dual_entry.json',
    'nf360_energy_dual_242_preflight.py':'nf360_energy_dual_242_report.json',
    'nf361_critical_transfer_no_go.py':'nf361_critical_transfer_no_go.json',
    'nf362_directional_neumann_gate.py':'nf362_directional_neumann_gate.json',
    'nf363_critical_sine_tail_higher.py':'nf363_critical_sine_tail_higher_report.json',
    'nf364_split_tail_exact.py':'nf364_split_tail_exact_report.json',
}
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for block in iter(lambda:f.read(1<<20), b''): h.update(block)
    return h.hexdigest()
def get_archive(name, work, offline):
    artifact, expected=PARENTS[name]
    p=work/name
    if offline:
        source=offline/name
        if not source.exists(): raise FileNotFoundError(f'{source} (offline parent required)')
        shutil.copyfile(source,p)
    elif not p.exists():
        token=os.environ.get('GITHUB_TOKEN')
        if not token: raise RuntimeError('GITHUB_TOKEN required for --download; use --offline DIR locally')
        req=urllib.request.Request(URL.format(id=artifact),headers={
            'Authorization':'Bearer '+token, 'Accept':'application/vnd.github+json',
            'X-GitHub-Api-Version':'2022-11-28','User-Agent':'weil-lab-custody-replay',
        })
        with urllib.request.urlopen(req, timeout=90) as r, open(p,'wb') as f: shutil.copyfileobj(r,f)
    actual=sha(p)
    if actual!=expected: raise AssertionError(f'PARENT {name} archive hash mismatch {actual} != {expected}')
    return {'name':name,'artifact_id':artifact,'sha256':actual,'bytes':p.stat().st_size}
def canon_report(p):
    return json.loads(p.read_text())
def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--offline',type=Path,help='directory with the three SHA-pinned GitHub artifact ZIPs')
    pa.add_argument('--work-dir',type=Path,help='scratch dir, preserved for auditing outputs')
    args=pa.parse_args()
    if args.work_dir:
        work=args.work_dir.resolve();work.mkdir(parents=True,exist_ok=True)
        cm=None
    else:
        cm=tempfile.TemporaryDirectory(prefix='weil-custody-');work=Path(cm.name)
    try:
        for f in DATA.glob('nf*.json'): shutil.copyfile(f,work/f.name)
        archives=[get_archive(name,work,args.offline) for name in PARENTS]
        env={**os.environ,'WEIL_CUSTODY_DATA_DIR':str(work)}
        checks=[]
        for script in REPLAYS:
            prior=BASELINE_REPORTS.get(script)
            original=canon_report(DATA/prior) if prior else None
            cmd=[sys.executable,str(SCRIPTS/script)]
            run=subprocess.run(cmd, cwd=BASE, env=env, text=True, capture_output=True,timeout=180)
            if run.returncode:
                print(run.stdout[-2500:],file=sys.stderr)
                print(run.stderr[-6000:],file=sys.stderr)
                raise RuntimeError(script+' FAILED '+str(run.returncode))
            if prior:
                actual=canon_report(work/prior)
                if actual!=original:
                    # Timing or machine-diagnostic values are not a substitute for exact identity.
                    keys=sorted(set(actual)^set(original) | {k for k in actual.keys() & original.keys() if actual[k]!=original[k]})
                    raise AssertionError(f'{script}: output diverged from staged report: {keys}')
            checks.append({'script':script,'status':'PASS', 'baseline_identical':bool(prior)})
            print('PASS',script,flush=True)
        report={'standing':'PROVISIONAL EXACT-RATIONAL REPLAY ONLY; NO NATIVE OR RH PROMOTION',
                'parent_sha256':archives,'checks':checks,'W-ODD-NEG':'OPEN',
                'native_Arb_recomputed':False,'NF356_floor_CI_certified':False}
        (work/'nf356_364_portable_replay_result.json').write_text(json.dumps(report,indent=2)+'\n')
        print('COMPLETE: '+str(len(checks))+' focused portable replays; no native or theorem promotion', flush=True)
    finally:
        if cm: cm.cleanup()
if __name__=='__main__': main()
