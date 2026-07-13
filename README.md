# Moonlight Peaks Forschungswiki

Version **0.3.0**

Dieses Repository trennt vier Ebenen:

1. **Originalquellen** (`archive/`) – unverändert, damit nie etwas verloren geht.
2. **Beobachtungen** (`data/observations/`) – einzelne Aussagen mit Quellen und Forschungsstatus.
3. **Entitäten** (`data/entities/`) – konsolidierte Datensätze wie Seelentropfen, Getiere, Rezepte oder NPCs.
4. **Wiki-Seiten** (`docs/`) – lesbare Zusammenfassungen aus den Daten.

Die YAML-Dateien sind die maßgebliche Datenquelle. Markdown-Seiten dürfen daraus erzeugt oder redaktionell ergänzt werden.

## Statuswerte

- `confirmed`: bestätigt
- `probable`: wahrscheinlich
- `hypothesis`: Vermutung
- `unknown`: offen
- `corrected`: korrigierte frühere Angabe

## Versionsschema

Semantische Versionierung:

- Patch `0.2.1`: neue Datensätze oder kleine Korrekturen
- Minor `0.3.0`: neue Struktur, neue Kategorie oder größere Importstufe
- Major `1.0.0`: erste veröffentlichungsreife Fassung
