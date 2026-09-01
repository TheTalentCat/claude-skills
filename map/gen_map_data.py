"""Generate skills-map-data.json for the 3D liquid skills map."""
import json, os, re, subprocess, sys

SKILLS_DIR = os.path.expanduser("~/.claude/skills")
REF_HTML = os.path.expanduser("~/claude-skills-reference.html")
REPO = os.path.expanduser("~/claude-skills")
OUT = os.path.expanduser("~/skills-map-data.json")

# ---- 1. collect installed skills + descriptions ----
skills = {}
for name in sorted(os.listdir(SKILLS_DIR)):
    p = os.path.join(SKILLS_DIR, name, "SKILL.md")
    if not os.path.isfile(p):
        continue
    try:
        text = open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    desc = ""
    mode = "auto"
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if m:
        fm = m.group(1)
        dm = re.search(r"^description:\s*(.*(?:\n[ \t]+.*)*)", fm, re.M)
        if dm:
            desc = re.sub(r"\s+", " ", dm.group(1)).strip()
            desc = re.sub(r"^[>|][-+]?\s*", "", desc)
        if re.search(r"^disable-model-invocation:\s*true", fm, re.M):
            mode = "manual"
        elif re.search(r"PROACTIVELY|MUST BE USED|always apply|Must always apply", desc, re.I):
            mode = "proactive"
    skills[name] = {"id": name, "desc": desc[:400], "mode": mode}

# ---- 2. pack assignment ----
# a) persistent registry (primary source; self-maintained below)
PACKS_JSON = os.path.expanduser("~/claude-skills/map/packs.json")
pack = {}
if os.path.isfile(PACKS_JSON):
    pack.update(json.load(open(PACKS_JSON, encoding="utf-8")))

# b) later commits in the claude-skills repo: commit subject -> pack label
COMMIT_PACKS = [
    ("game theory", "game-theory"),
    ("marketingskills", "marketing"),
    ("marketing skills", "marketing"),
    ("pstack", "pstack"),
    ("advisors", "advisors"),
]
try:
    log = subprocess.run(
        ["git", "-C", REPO, "log", "--diff-filter=A", "--name-only",
         "--pretty=format:@@%s"],
        capture_output=True, text=True, check=True).stdout
    current = None
    for line in log.splitlines():
        if line.startswith("@@"):
            subj = line[2:].lower()
            current = None
            for key, label in COMMIT_PACKS:
                if key in subj:
                    current = label
                    break
        elif current and line.startswith("skills/"):
            parts = line.split("/")
            if len(parts) >= 2:
                pack.setdefault(parts[1], current)
except Exception as e:
    print("git log failed:", e, file=sys.stderr)

# c) known packs not covered above
EXTRA = {
    "hyperframes-pack": ["embedded-captions","faceless-explainer","general-video",
        "graphic-overlays","hyperframes-animation","hyperframes-core",
        "hyperframes-creative","motion-graphics","pr-to-video",
        "product-launch-video","slideshow","website-to-video"],
    "gstack": ["diagram","spec"],
    "research": ["deep-research","academic-paper","academic-paper-reviewer","academic-pipeline"],
}
for label, names in EXTRA.items():
    for n in names:
        pack.setdefault(n, "hyperframes" if label == "hyperframes-pack" else label)

for name, s in skills.items():
    s["pack"] = pack.get(name, "misc")

# write resolved packs back so new skills only need assigning once
if os.path.isdir(os.path.dirname(PACKS_JSON)):
    json.dump({n: s["pack"] for n, s in skills.items()},
              open(PACKS_JSON, "w", encoding="utf-8"),
              ensure_ascii=False, indent=0, sort_keys=True)

# ---- 3. edges from description cross-references ----
names = set(skills)
edges = set()
# only match distinctive names to avoid false positives on words like "design","image","how"
def distinctive(n):
    return "-" in n or len(n) >= 9
safe_names = [n for n in names if distinctive(n)]
pat_cache = {n: re.compile(r"(?:(?<=[\s(/'\"`])|^)" + re.escape(n) + r"(?=[\s.,;:)'\"`]|$)") for n in safe_names}
see_pat = re.compile(r"see /?([a-z0-9-]+)")

for name, s in skills.items():
    d = s["desc"].lower()
    if not d:
        continue
    for other in safe_names:
        if other == name:
            continue
        if pat_cache[other].search(d):
            edges.add(tuple(sorted((name, other))))
    for m in see_pat.finditer(d):
        t = m.group(1)
        if t in names and t != name:
            edges.add(tuple(sorted((name, t))))

# ---- 3b. merge ELI5 summaries if present ----
ELI5 = os.path.expanduser("~/claude-skills/map/eli5.json")
if os.path.isfile(ELI5):
    eli5 = json.load(open(ELI5, encoding="utf-8"))
    for name, s in skills.items():
        if name in eli5:
            s["eli5"] = eli5[name]

nodes = sorted(skills.values(), key=lambda s: (s["pack"], s["id"]))
links = [{"source": a, "target": b, "kind": "ref"} for a, b in sorted(edges)]

packs = sorted({s["pack"] for s in nodes})
data = {"nodes": nodes, "links": links, "packs": packs}
json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
print(f"nodes={len(nodes)} ref-links={len(links)} packs={len(packs)}")
from collections import Counter
print(Counter(s['pack'] for s in nodes).most_common())
