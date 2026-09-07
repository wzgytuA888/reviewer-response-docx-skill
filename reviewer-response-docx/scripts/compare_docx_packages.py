#!/usr/bin/env python3
"""Check clean/marked accepted text and optional tracked accepted text."""
from __future__ import annotations
import argparse, re, sys, zipfile
from pathlib import Path
from lxml import etree

NS={"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main","m":"http://schemas.openxmlformats.org/officeDocument/2006/math"}
def xml(path):
    with zipfile.ZipFile(path) as z:return etree.fromstring(z.read("word/document.xml"))
def visible(root, accept=False):
    root=etree.fromstring(etree.tostring(root))
    if accept:
        for p in root.xpath("//w:p[w:pPr/w:rPr/w:del]",namespaces=NS):p.getparent().remove(p)
        for e in root.xpath("//w:del",namespaces=NS):e.getparent().remove(e)
    return re.sub(r"\s+"," ","".join(root.xpath("//w:t/text()|//m:t/text()",namespaces=NS))).strip()
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--clean",type=Path,required=True);ap.add_argument("--marked",type=Path,required=True);ap.add_argument("--tracked",type=Path)
    a=ap.parse_args();clean=visible(xml(a.clean));marked=visible(xml(a.marked));ok=clean==marked
    print("clean_marked_text_identical:",ok)
    if a.tracked:
        same=clean==visible(xml(a.tracked),True);print("tracked_accepted_text_identical:",same);ok &= same
    return 0 if ok else 1
if __name__=="__main__":sys.exit(main())
