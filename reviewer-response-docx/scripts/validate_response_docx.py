#!/usr/bin/env python3
"""Validate visible formatting and pending-state conventions in a response DOCX."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from docx import Document

RED = "C00000"

def color(run):
    value = run.font.color.rgb
    return str(value) if value else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("response", type=Path)
    ap.add_argument("--json", type=Path)
    args = ap.parse_args()
    doc = Document(args.response)
    findings=[]; responses=revisions=pending=0
    for i,p in enumerate(doc.paragraphs,1):
        t=p.text.strip()
        if t == "Response":
            responses += 1
            if not any(r.bold for r in p.runs): findings.append(f"P{i}: Response label is not bold")
        if t == "Revision":
            revisions += 1
            if not any(color(r)==RED and r.bold for r in p.runs): findings.append(f"P{i}: Revision label is not bold red")
        if "AUTHOR WORKING NOTE" in t or "AUTHOR_INPUT_NEEDED" in t:
            pending += 1
            if not any(color(r)==RED for r in p.runs): findings.append(f"P{i}: pending label is not red")
        if t.startswith("(") and ("Manuscript" in t or "Supplement" in t):
            if not any(r.bold for r in p.runs): findings.append(f"P{i}: location line is not bold")
    if responses == 0: findings.append("No Response labels found")
    if revisions == 0: findings.append("No Revision labels found")
    result={"file":str(args.response),"response_labels":responses,"revision_labels":revisions,"pending_labels":pending,"findings":findings,"passed":not findings}
    if args.json: args.json.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not findings else 1

if __name__ == "__main__": sys.exit(main())
