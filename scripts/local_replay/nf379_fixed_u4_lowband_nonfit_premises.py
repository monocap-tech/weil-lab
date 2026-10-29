#!/usr/bin/env python3
"""NF379: SHA-pinned exact premises for the FIXED original u4 lowband no-perfect-fit lemma.

Checks only the archived certified intervals and finite-dimensional source
inventory. Entire-function uniqueness is proved in the companion note.
Does not integrate a signed continuum or establish a quantitative residual.
"""
import argparse, hashlib, json
from fractions import Fraction as Q
from pathlib import Path

PARENT_GIT_BLOB="94b4825b63d72e8a8f07f8693359ad11043092c0"
RANK_SHA="9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2"
SOURCE_SHA="abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770"
NF369_SHA="3e73a12bbd70158a461d9722dc8fc499eee8d17baf0afc9090bac5d10165e7e8"

def check(path):
 raw=Path(path).read_bytes()
 blob_sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
 assert blob_sha==PARENT_GIT_BLOB,("native original report custody mismatch",blob_sha)
 report=json.loads(raw)
 assert report["status"]=="CERTIFIED_ORIGINAL_QWITNESS_AND_SIGNED_LOWBAND_POINT_SAMPLES_ONLY"
 assert report["working_precision_bits"]==4096
 assert report["original_selected_count"]==242
 assert report["original_critical_count"]==4
 assert report["original_rank_sha256"]==RANK_SHA
 assert report["original_source_sha256"]==SOURCE_SHA
 assert report["original_nf369_fields_sha256"]==NF369_SHA
 entry=next(x for x in report["actual_original_signed_point_samples"] if x["frequency"]=="1/4")
 m_lo,m_hi=map(Q,entry["signed_m_interval"])
 u_lo,u_hi=(int(x) for x in entry["original_u4_Fourier_sine_amplitude_units_1e320"])
 assert Q(0)<m_lo<=m_hi
 assert 0<u_lo<=u_hi
 assert Q(1,4)<2**20
 assert report["full_original_lowband_H_i_norm_computed"] is False
 assert report["whole_four_direction_residual_certified"] is False
 return dict(
  standing="CERTIFIED_ARCHIVED_NONZERO_SOURCE_PREMISES_PLUS_ANALYTIC_FINITE_FIT_EXCLUSION",
  native_original_git_blob_sha1=blob_sha,
  original_input_rank_sha256=RANK_SHA,
  original_input_source_sha256=SOURCE_SHA,
  original_nf369_sha256=NF369_SHA,
  cutoff=2**20,
  nonzero_original_frequency="1/4",
  original_signed_multiplier_interval=[str(m_lo),str(m_hi)],
  original_u4_sine_amplitude_units_1e320=[str(u_lo),str(u_hi)],
  analytic_proof="Bandlimited entire continuation plus no nonzero finite real exponential-polynomial combination belongs to L2(R).",
  conditional_original_real_frequency_symbol_continuity=True,
  conclusion="fixed original g4_low is not in J242+span(E4), so its physical unfitted residual has strictly positive norm",
  numeric_normalized_residual_lower_certified=False,
  actual_signed_lowband_continuum_integral_computed=False,
  one_specific_annulus_selected=False,
  NF375_direction_four_method_stopped=False,
  external_method_promoted=False,
  W_ODD_NEG="OPEN",RH="OPEN")

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--native",required=True)
 p.add_argument("--output",required=True)
 a=p.parse_args()
 x=check(a.native)
 out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(x,sort_keys=True,indent=2)+"\n")
 print("NF379 archived original u4 nonzero spectral input PASS; no residual threshold decided")
