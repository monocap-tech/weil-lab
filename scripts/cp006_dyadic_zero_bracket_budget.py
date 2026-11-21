#!/usr/bin/env python3
"""CP006 rigorous Fraction dyadic zero-bracket localization BUDGET (not a zero proof).

Uses CP005's pinned manifest only for structural intake. Real membership of each
input row in an upstream Lean-certified zero batch is NOT checked by this file.
All numerical operations in the localization/tail bound use exact Fractions.
"""
import argparse
import csv
import hashlib
import json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

from cp005_formal_zero_roster_adapter import (
    ROOT_COUNT, H, RADII, CENTERS, E_QUAD_ALLOWANCE, EPS_MAX,
    E_tail, parse_manifest
)


def power_two(j):
    return F(2**j) if j >= 0 else F(1,2**(-j))


def dyadic_band(a):
    assert a>0
    j=a.numerator.bit_length()-a.denominator.bit_length()
    while a<power_two(j):
        j-=1
    while a>=power_two(j+1):
        j+=1
    assert power_two(j)<=a<power_two(j+1)
    return j


def band_caps(h, band):
    height=power_two(band)
    q=h*h*height*height
    return min(F(2),F(16)/q), h*min(F(1),F(20)/q)


def localization(r, band_sums):
    """Exact max row sum for all normalized 3x3 cosine-moment interval errors.

    band_sums: map int j -> sum of half-widths delta_k for all zero brackets
    whose lower ordinate a_k is in [2^j,2^(j+1)).
    """
    assert r in RADII
    hs=(H,H,r)
    row=[F(0) for _ in range(3)]
    for band,delta_sum in band_sums.items():
        assert isinstance(band,int) and delta_sum>=0
        caps=[band_caps(h,band) for h in hs]
        for i in range(3):
            Ai,Di=caps[i]
            for j in range(3):
                Aj,Dj=caps[j]
                d=abs(CENTERS[i]-CENTERS[j])
                L=F(25,24)*(hs[i]+hs[j])*(Di*Aj+Ai*Dj+d*Ai*Aj)
                row[i]+=delta_sum*L
    return max(row)


def uniform_localization(r,total_delta):
    hs=(H,H,r)
    return max(sum(total_delta*F(25,24)*(hs[i]+hs[j])*
                   (2*(hs[i]+hs[j])+4*abs(CENTERS[i]-CENTERS[j]))
                   for j in range(3)) for i in range(3))


def budget_report(band_sums):
    results={}
    total_delta=sum(band_sums.values(),F(0))
    for r in RADII:
        e=localization(r,band_sums)
        u=uniform_localization(r,total_delta)
        assert e<=u, "Adaptive dyadic bound cannot exceed uniform bound"
        tail=E_tail(r)
        total=tail+e+E_QUAD_ALLOWANCE
        results[str(r)]={
            "tail_upper":str(tail),
            "adaptive_ordinate_error":str(e),
            "unweighted_ordinate_error":str(u),
            "quadrature_allowance_unverified":str(E_QUAD_ALLOWANCE),
            "total_conditional_upper":str(total),
            "within_budget":bool(total<EPS_MAX),
        }
    return results


def selftest():
    assert dyadic_band(F(1,2))==-1
    assert dyadic_band(F(1))==0
    assert dyadic_band(F(1023))==9
    assert dyadic_band(F(1024))==10
    low={0:ROOT_COUNT*F(1,10**9)}
    hi={18:ROOT_COUNT*F(1,10**7)}
    broad={0:ROOT_COUNT*F(1,10**4)}
    for r in RADII:
        assert localization(r,low)==uniform_localization(r,low[0])
        assert localization(r,hi)<uniform_localization(r,hi[18])
        assert localization(r,broad)+E_tail(r)+E_QUAD_ALLOWANCE>EPS_MAX
        assert localization(r,low)+E_tail(r)+E_QUAD_ALLOWANCE<EPS_MAX
        print(f"r={r}: synthetic low-height equals prior uniform Lipschitz gate, "
              "synthetic high-height gains strict Fourier-decay allowance")
    print("CP006 exact-Fraction adaptive-band algebra and negative controls: PASS")
    print("No 1,748,002-row upstream zero-roster or Lean source interval mapping supplied")


def rational_field(s):
    s=s.strip()
    if not s or any(ch not in "+-0123456789/" for ch in s):
        raise ValueError("Endpoints must be canonical simple rational integer/fraction strings")
    f=F(s)
    return f


def read_roster(filename,meta,gram_lower):
    h=hashlib.sha256()
    bins=defaultdict(lambda:{"n":0,"delta":F(0),"max_delta":F(0)})
    last_hi=F(0)
    touching=0
    count=0
    with filename.open("rb") as file:
        for raw in file:
            h.update(raw)
            try:
                line=raw.decode("ascii").strip()
            except UnicodeError as exc:
                raise ValueError("Roster is not plain ASCII") from exc
            if not line or line.startswith("#"):
                raise ValueError("No blank/comment/header rows in canonical source roster")
            columns=next(csv.reader([line]))
            if len(columns)!=2:
                raise ValueError(f"Expected two ordinate rationals at row {count+1}")
            a,b=map(rational_field,columns)
            if not (0<last_hi<=a<=b<gram_lower):
                raise ValueError(f"Invalid or overlapping positive brackets at row {count+1}")
            if last_hi==a:
                touching+=1
            delta=(b-a)/2
            k=dyadic_band(a)
            bins[k]["n"]+=1
            bins[k]["delta"]+=delta
            bins[k]["max_delta"]=max(delta,bins[k]["max_delta"])
            last_hi=b
            count+=1
            if count>ROOT_COUNT:
                raise ValueError("More than the certified interval count")
    if count!=ROOT_COUNT:
        raise ValueError(f"Incomplete roster: {count} rows, require {ROOT_COUNT}")
    if h.hexdigest()!=meta["roster_sha256"]:
        raise ValueError("Exact roster hash disagrees with pinned manifest")
    bands={k:v["delta"] for k,v in bins.items()}
    counts=sum(v["n"] for v in bins.values())
    assert counts==ROOT_COUNT
    return bands,{str(k):{
        "count":v["n"],"total_halfwidth":str(v["delta"]),
        "max_halfwidth":str(v["max_delta"])
    } for k,v in sorted(bins.items())},touching


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--manifest",type=Path)
    p.add_argument("--roster",type=Path)
    p.add_argument("--report",type=Path)
    args=p.parse_args()
    if args.self_test:
        selftest()
    if bool(args.manifest)!=bool(args.roster):
        print("NOT_READY: both a source manifest and exact certified-interval roster are required")
        raise SystemExit(2)
    if args.roster:
        try:
            meta,gram_lo,gram_hi=parse_manifest(args.manifest)
            bands,details,touching=read_roster(args.roster,meta,gram_lo)
            errors=budget_report(bands)
            within=all(v["within_budget"] for v in errors.values())
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            print("NOT_READY:",exc)
            raise SystemExit(2)
        result={
            "status": "STRUCTURAL_BUDGET_WITHIN_THRESHOLD" if within else "BUDGET_EXCEEDED",
            "trust":"No Lean source interval correspondence, kernel axiom validation, or quadrature acceptance",
            "expected_root_count":ROOT_COUNT,
            "source_roster_sha256":meta["roster_sha256"],
            "touching_boundary_pairs":touching,
            "by_dyadic_band":details,
            "bounds":errors,
        }
        if args.report:
            args.report.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        print(result["status"])
        print(f"{ROOT_COUNT} exact rational rows; {len(bands)} dyadic bands, "
              f"shared adjacent boundaries={touching}")
        for r,v in errors.items():
            print(f"r={r}: conditional total=~{float(F(v['total_conditional_upper'])):.9f}, "
                  f"strict threshold={EPS_MAX}, met={v['within_budget']}")
        print("Provenance digests are metadata, not proof-to-exported-row verification.")
    if not args.self_test and args.roster is None:
        p.print_help()


if __name__=="__main__":
    main()
