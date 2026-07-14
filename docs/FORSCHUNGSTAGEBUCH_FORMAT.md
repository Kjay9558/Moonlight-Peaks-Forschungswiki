# Format für Forschungstagebücher

## Zweck

Ein Forschungstagebuch ist die vollständige, unveränderte Forschungsakte eines Spieltags. Es dient als Primärquelle für spätere Beobachtungen, Entitäten und Wiki-Seiten.

## Dateiname

```text
archive/forschungstagebuecher/JJJJ/tag-XXX-issue-NNN.md
```

Beispiel:

```text
archive/forschungstagebuecher/2026/tag-017-issue-010.md
```

## Kopfbereich

Jede Datei beginnt mit YAML-Frontmatter:

```yaml
---
schema_version: 1
source_id: journal-2026-day-017
issue: 10
day: 17
season: Frühling
year: 1
game: Moonlight Peaks
platform: Switch 2
researcher: Kjay9558
created_at: 2026-07-14
status: archived
contains:
  screenshots: 0
  videos: 0
  observations: 0
---
```

### Pflichtfelder

- `schema_version`: Version dieses Formats.
- `source_id`: stabile, eindeutige Quellenkennung.
- `day`: Spieltag.
- `game`: Spielname.
- `created_at`: Datum der Archivierung.
- `status`: Zustand der Quelle.

### Statuswerte

- `draft`: Forschungsakte wird noch zusammengestellt.
- `archived`: vollständig archiviert.
- `supplemented`: durch eine spätere Quelle ergänzt.
- `superseded`: als technische Datei ersetzt; Inhalt bleibt historisch erhalten.

## Empfohlene Gliederung

```markdown
# Forschungstagebuch Tag X

## Quellenkontext

## Chronologischer Verlauf

## Strukturierte Beobachtungen

## Korrekturen und Präzisierungen

## Offene Fragen

## Medien

## Abschlussstand
```

## Quellenkontext

Dieser Abschnitt nennt den Ursprung und bekannte Rahmenbedingungen:

- Chat oder Importquelle,
- Spielversion, sofern bekannt,
- Plattform,
- Datum,
- Besonderheiten wie Bugs oder abweichende Zählweisen.

## Chronologischer Verlauf

Der Verlauf bewahrt die Reihenfolge der Forschung. Jede Station sollte nach Möglichkeit enthalten:

```markdown
### Eintrag 001

- Zeitpunkt im Spiel: unbekannt
- Ort: Heulender Sumpf
- Handlung: Seelentropfen aufgenommen
- Ergebnis: blauer Seelentropfen
- Medien: screenshot-001 bis screenshot-003
- Notiz: zunächst als 51. Gesamtfund bezeichnet
```

Regeln:

- Einträge werden nicht nachträglich umsortiert.
- Korrekturen werden als spätere Einträge dokumentiert.
- Unbekannte Werte werden ausdrücklich als `unbekannt` markiert.
- Fehlende Angaben führen nicht zum Entfernen des Eintrags.

## Strukturierte Beobachtungen

Jede erkannte Beobachtung erhält einen eigenen Block:

```markdown
### OBS-journal-2026-day-017-001

- Typ: Seelentropfen-Fund
- Entität: unbekannt
- Ort: Heulender Sumpf
- Farbe: blau
- Kompendium: unbekannt
- Gesamtzählung: 51
- Status: corrected
- Quelle: Eintrag 001
- Medien: screenshot-001 bis screenshot-003
```

Die Blöcke dienen der späteren automatischen Extraktion. Sie ersetzen nicht den chronologischen Verlauf.

## Korrekturen und Präzisierungen

Korrekturen nennen immer:

- die frühere Angabe,
- die neue Angabe,
- den Grund, soweit bekannt,
- die betroffene Beobachtung.

Beispiel:

```markdown
- `OBS-journal-2026-day-017-001`: Gesamtzählung 51 wurde auf 53 korrigiert.
```

## Offene Fragen

Jede offene Frage soll so konkret wie möglich formuliert sein:

```markdown
- Welche Kompendium-Nummer gehört zum Fund aus Eintrag 008?
- Gehören zwei Screenshots zum selben oder zu verschiedenen Seelentropfen?
```

Offene Fragen dürfen später automatisch in `research/offene-fragen/` übernommen werden.

## Medien

Medien werden in ihrer ursprünglichen Reihenfolge aufgeführt:

```markdown
### Screenshots

| Referenz | Datei | Zugehörige Einträge | Beschreibung |
|---|---|---|---|
| screenshot-001 | unbekannt | 001 | Fundort im Heulenden Sumpf |

### Videos

| Referenz | Datei | Zugehörige Einträge | Beschreibung |
|---|---|---|---|
| video-001 | 1000139807.mp4 | Abschluss | Aufzeichnung vom Ende des Tages |
```

Wenn eine Datei nicht im Repository gespeichert werden kann, bleibt mindestens ihr Originalname erhalten.

## Abschlussstand

Der Abschlussstand fasst nur den dokumentierten Zustand am Ende des Tages zusammen. Er ersetzt keine Einzelbeobachtungen.

Empfohlene Angaben:

- Geld,
- Energie,
- Gesamtzählungen,
- Queststände,
- neu freigeschaltete Inhalte,
- bekannte offene Fragen,
- Fokus für den nächsten Tag.

## Vollständigkeitsregel

Eine Forschungsakte gilt als vollständig, wenn alle im Chat vorhandenen Informationen übernommen wurden. Sie muss nicht inhaltlich vollständig erforscht sein. Ein Datensatz mit unbekanntem Ort oder unbekannter Nummer ist eine gültige Quelle.
