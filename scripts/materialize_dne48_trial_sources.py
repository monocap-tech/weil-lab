#!/usr/bin/env python3
"""Append DNE47's exact even high trials to the frozen original source packet."""
from pathlib import Path
import json
from certify_dne39_signed_comparison import read
from materialize_dne44_joint_sources import run as prior

def run(cert_path,output):
 pp=output+'.prior';prior(cert_path,pp);packet,ph=read(pp);Path(pp).unlink();tp='notes/data/RPB108_DNE47_RESPONSE_TRIAL_GATE_20261010.json';t,th=read(tp);vp='notes/data/RPB108_DNE47_RESPONSE_TRIAL_VALIDATION_20261010.json';v,vh=read(vp);assert v['status']=='PASS' and v['certificate_sha256']==th and t['normalized_packet_sha256']==ph and packet['parity']=='even'
 cols=packet['columns']+[dict(indices=c['indices'],coefficients=c['coefficients'],exact_mass_squared=c['exact_mass_squared'],norm_upper='1') for c in t['physical_high_trial_columns']]
 out=dict(stage='DNE48',parity='even',columns=cols,column_labels=packet['column_labels']+['Y0','Y1','Y2'],native_matrix=packet['native_matrix'],input_sha256=packet['input_sha256']+[th,vh],prior_packet_sha256=ph,trial_path=tp,trial_sha256=th,trial_validation_path=vp,trial_validation_sha256=vh)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('47 exact source columns materialized',flush=True)
