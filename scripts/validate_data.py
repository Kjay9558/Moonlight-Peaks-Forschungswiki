from pathlib import Path
import sys, yaml, json
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data/entities/critters"
SCHEMA_PATH = ROOT / "schemas/entity.schema.json"
ALLOWED_STATUS = {"confirmed", "probable", "hypothesis", "unknown", "corrected"}

def main():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors, seen_ids, seen_names = [], {}, {}
    files = sorted(DATA_DIR.glob("*.yaml"))

    if not files:
        errors.append("Keine Getierdateien gefunden.")

    for path in files:
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.name}: YAML-Fehler: {exc}")
            continue

        for err in validator.iter_errors(record):
            where = "/".join(map(str, err.path)) or "<root>"
            errors.append(f"{path.name}: Schemafehler bei {where}: {err.message}")

        rid, name, status = record.get("id"), record.get("name"), record.get("status")
        if rid in seen_ids:
            errors.append(f"Doppelte ID {rid}: {seen_ids[rid]} und {path.name}")
        else:
            seen_ids[rid] = path.name

        nkey = str(name).casefold()
        if nkey in seen_names:
            errors.append(f"Doppelter Name {name}: {seen_names[nkey]} und {path.name}")
        else:
            seen_names[nkey] = path.name

        if status not in ALLOWED_STATUS:
            errors.append(f"{path.name}: ungültiger Status {status}")

        price = record.get("fields", {}).get("sale_price")
        if price is not None and (not isinstance(price, int) or price < 0):
            errors.append(f"{path.name}: sale_price muss eine nichtnegative Ganzzahl sein.")

        if status == "confirmed" and not record.get("source_refs"):
            errors.append(f"{path.name}: bestätigter Datensatz benötigt mindestens eine Quelle.")

        expected = rid.replace("critter-", "") + ".yaml" if rid else None
        if expected and path.name != expected:
            errors.append(f"{path.name}: Dateiname sollte {expected} sein.")

    if errors:
        print("Validierung fehlgeschlagen:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print(f"Validierung erfolgreich: {len(files)} Getierdatensätze.")

if __name__ == "__main__":
    main()
