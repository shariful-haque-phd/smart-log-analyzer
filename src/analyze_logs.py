import argparse, collections, json, re
from pathlib import Path

LEVEL_RE=re.compile(r"\b(DEBUG|INFO|WARN|WARNING|ERROR|CRITICAL|FATAL)\b",re.I)
UUID_RE=re.compile(r"\b[0-9a-f]{8}-[0-9a-f-]{27,}\b",re.I)
IP_RE=re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
TS_RE=re.compile(r"\b\d{4}-\d{2}-\d{2}[T ][0-9:.+-Z]+\b")
NUM_RE=re.compile(r"\b\d+\b")

def normalize(line):
    s=TS_RE.sub("<TIMESTAMP>",line)
    s=UUID_RE.sub("<UUID>",s)
    s=IP_RE.sub("<IP>",s)
    s=NUM_RE.sub("<N>",s)
    return re.sub(r"\s+"," ",s).strip()

def analyze(lines):
    groups={}
    levels=collections.Counter()
    for raw in lines:
        m=LEVEL_RE.search(raw)
        level=(m.group(1).upper() if m else "UNKNOWN").replace("WARNING","WARN")
        levels[level]+=1
        key=normalize(raw)
        g=groups.setdefault(key,{"count":0,"levels":collections.Counter(),"examples":[]})
        g["count"]+=1; g["levels"][level]+=1
        if len(g["examples"])<3: g["examples"].append(raw.rstrip())
    items=[]
    for template,g in groups.items():
        items.append({"template":template,"count":g["count"],"levels":dict(g["levels"]),"examples":g["examples"]})
    items.sort(key=lambda x:x["count"],reverse=True)
    return {"level_counts":dict(levels),"groups":items}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("log"); ap.add_argument("--top",type=int,default=20); a=ap.parse_args()
    result=analyze(Path(a.log).read_text(errors="replace").splitlines())
    result["groups"]=result["groups"][:a.top]
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
