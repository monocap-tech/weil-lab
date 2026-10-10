#!/usr/bin/env python3
"""Recover exact source ordering and native map from the audited DNE49 packet."""
from pathlib import Path
import json
from certify_dne39_signed_comparison import read

def run(cert_path,output):
 gp='notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64';vp='notes/data/RPB108_DNE49_COMPLETE_PACKET_VALIDATION_20261010.json';g,gh=read(gp);v,vh=read(vp);cert,ch=read(cert_path);assert v['status']=='PASS' and v['certificate_sha256']==gh
 r=next(r for r in g['rows'] if r['parity']==cert['parity']);assert r['certificate_path']==cert_path and r['certificate_sha256']==ch
 cols=r['columns'][:44]+r['high_trial_columns']+r['columns'][44:];out=dict(stage='DNE50',parity=r['parity'],columns=cols,column_labels=r['source_column_labels'],native_matrix=r['native_matrix'],native_to_source=r['native_to_source'],trial_source_indices=r['trial_source_indices'],reused_source_count=r['reused_source_count'],input_sha256=[gh,vh],gate_path=gp,gate_sha256=gh,gate_validation_path=vp,gate_validation_sha256=vh)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(r['parity'],len(cols),'complete exact source columns',flush=True)
