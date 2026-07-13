from pathlib import Path
import yaml
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data/entities/critters"
OUT_DIR = ROOT / "docs/reference/generated"
DETAIL_DIR = OUT_DIR / "getiere"

STATUS_LABELS = {
    "confirmed": "✅ bestätigt",
    "probable": "🟡 wahrscheinlich",
    "hypothesis": "🧪 Vermutung",
    "unknown": "❓ offen",
    "corrected": "🛠️ korrigiert",
}

def load_records():
    records = []
    for path in sorted(DATA_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data:
            records.append(data)
    return records

def safe(value, fallback="–"):
    return fallback if value is None or value == "" else str(value)

def join(values, fallback="–"):
    return ", ".join(str(v) for v in values) if values else fallback

def write_detail(record):
    fields = record.get("fields", {})
    slug = record["id"].replace("critter-", "")
    lines = [
        f"# {record['name']}",
        "",
        f"**Status:** {STATUS_LABELS.get(record.get('status'), record.get('status', '–'))}",
        "",
        "## Daten",
        "",
        f"- Verkaufspreis: **{safe(fields.get('sale_price'))} G**",
        f"- Beobachtete Fundorte: {join(fields.get('locations_observed', []))}",
        f"- Beobachtete Uhrzeiten: {join(fields.get('times_observed', []), 'nicht genauer dokumentiert')}",
        f"- Beobachtete Jahreszeiten: {join(fields.get('seasons_observed', []))}",
    ]
    if fields.get("conditions_observed"):
        lines += ["", "## Beobachtete Bedingungen", ""]
        lines += [f"- {x}" for x in fields["conditions_observed"]]
    if record.get("notes"):
        lines += ["", "## Hinweise", "", record["notes"]]
    if record.get("history"):
        lines += ["", "## Änderungshistorie", ""]
        for h in record["history"]:
            lines.append(
                f"- `{h.get('field', h.get('change', 'Feld'))}`: "
                f"{h.get('old_value', h.get('old', '–'))} → "
                f"{h.get('new_value', h.get('new', '–'))} "
                f"({h.get('reason', 'ohne Begründung')})"
            )
    lines += ["", "## Quellen", ""]
    for src in record.get("source_refs", []):
        note = src.get("note", "")
        lines.append(f"- `{src.get('source_id', 'unbekannt')}`{': ' + note if note else ''}")
    (DETAIL_DIR / f"{slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

def write_overview(records):
    ordered = sorted(records, key=lambda r: (-r.get("fields", {}).get("sale_price", -1), r["name"].casefold()))
    lines = [
        "# Getiere",
        "",
        f"**Erfasste Arten:** {len(records)} / 95",
        "",
        "> Uhrzeiten sind Beobachtungszeiten und keine automatisch bestätigten Spawnzeiten.",
        "",
        "## Übersicht nach Verkaufspreis",
        "",
        "| Getier | Verkauf | Fundorte | Uhrzeiten | Status |",
        "|---|---:|---|---|---|",
    ]
    for r in ordered:
        f = r.get("fields", {})
        slug = r["id"].replace("critter-", "")
        lines.append(
            f"| [{r['name']}](getiere/{slug}.md) | {safe(f.get('sale_price'))} G | "
            f"{join(f.get('locations_observed', []))} | "
            f"{join(f.get('times_observed', []), 'nicht genauer dokumentiert')} | "
            f"{STATUS_LABELS.get(r.get('status'), r.get('status', '–'))} |"
        )
    (OUT_DIR / "getiere.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

def write_by_location(records):
    groups = defaultdict(list)
    for r in records:
        for loc in r.get("fields", {}).get("locations_observed", []) or ["Unbekannt"]:
            groups[loc].append(r)
    lines = ["# Getiere nach Fundort", ""]
    for loc in sorted(groups, key=str.casefold):
        lines += [f"## {loc}", ""]
        for r in sorted(groups[loc], key=lambda x: x["name"].casefold()):
            slug = r["id"].replace("critter-", "")
            lines.append(f"- [{r['name']}](getiere/{slug}.md) — {r.get('fields', {}).get('sale_price', '–')} G")
        lines.append("")
    (OUT_DIR / "getiere-nach-gebiet.md").write_text("\n".join(lines), encoding="utf-8")

def main():
    DETAIL_DIR.mkdir(parents=True, exist_ok=True)
    for old in DETAIL_DIR.glob("*.md"):
        old.unlink()
    records = load_records()
    for record in records:
        write_detail(record)
    write_overview(records)
    write_by_location(records)
    print(f"{len(records)} Getierdatensätze generiert.")

if __name__ == "__main__":
    main()
