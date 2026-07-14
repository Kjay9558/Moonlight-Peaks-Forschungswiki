# Beobachtungsschema

## Zweck

Eine Beobachtung ist die kleinste eigenständig belegbare Forschungsaussage. Sie wird aus einer Originalquelle abgeleitet und bildet die Grundlage für konsolidierte Entitäten.

## Speicherort

```text
data/observations/<kategorie>/<beobachtungs-id>.yaml
```

Beispiele:

```text
data/observations/seelentropfen/obs-journal-2026-day-017-001.yaml
data/observations/quests/obs-journal-2026-day-018-014.yaml
```

## Minimales Schema

```yaml
schema_version: 1
id: obs-journal-2026-day-017-001
type: soul_drop_found
status: confirmed
source:
  source_id: journal-2026-day-017
  issue: 10
  entry: 1
  media: []
observed_at:
  game_day: 17
  season: Frühling
  year: 1
  game_time: null
subject:
  entity_type: soul_drop
  entity_id: null
facts:
  location: Heulender Sumpf
  color: blau
notes: null
created_at: 2026-07-14
```

## Pflichtfelder

- `schema_version`: Version des Schemas.
- `id`: weltweit eindeutige Beobachtungskennung.
- `type`: Art der Beobachtung.
- `status`: Forschungsstatus.
- `source.source_id`: stabile Kennung der Originalquelle.
- `subject.entity_type`: betroffene Entitätsklasse.
- `facts`: beobachtete strukturierte Werte.
- `created_at`: Datum der Übernahme.

## Kennungen

Empfohlenes Muster:

```text
obs-<quellentyp>-<jahr>-day-<tag>-<laufnummer>
```

Beispiel:

```text
obs-journal-2026-day-017-001
```

Kennungen werden nach ihrer Veröffentlichung nicht wiederverwendet.

## Statuswerte

- `confirmed`: direkt und ausreichend belegt.
- `probable`: wahrscheinlich, aber nicht vollständig belegt.
- `hypothesis`: Vermutung oder geplante Prüfung.
- `unknown`: Aussage vorhanden, Einordnung noch offen.
- `corrected`: frühere Angabe wurde durch eine spätere Beobachtung korrigiert.

Optional können zusätzlich verwendet werden:

- `disputed`: mehrere Quellen widersprechen sich.
- `duplicate`: Beobachtung bildet denselben Sachverhalt wie eine andere Beobachtung ab.
- `invalid`: Quelle wurde falsch interpretiert; Datensatz bleibt historisch erhalten.

## Quellenverweis

```yaml
source:
  source_id: journal-2026-day-017
  issue: 10
  entry: 4
  quote: null
  media:
    - screenshot-013
    - screenshot-014
```

Der Quellenverweis muss konkret genug sein, um die Beobachtung im Archiv wiederzufinden.

## Beobachtungszeit

```yaml
observed_at:
  real_date: 2026-07-14
  game_day: 17
  season: Frühling
  year: 1
  game_time: "23:40"
```

Unbekannte Werte werden als `null` gespeichert und nicht geraten.

## Gegenstand

```yaml
subject:
  entity_type: vampster
  entity_id: vampster-echohoehle-05
```

Ist die genaue Entität unbekannt, bleibt `entity_id: null`. Die Beobachtung bleibt trotzdem gültig.

## Fakten

`facts` enthält nur Werte, die zur jeweiligen Beobachtungsart gehören.

Beispiel Seelentropfen:

```yaml
facts:
  location: Heulender Sumpf
  color: blau
  compendium_number: 13
  total_collection_count: 53
```

Beispiel Verkaufswert:

```yaml
facts:
  item: Mokka
  quality: grau
  energy: 5
  sell_price: 570
  currency: G
```

Beispiel Questfortschritt:

```yaml
facts:
  quest: Stall kaufen
  previous_state: Stall noch nicht gekauft
  new_state: Stall gekauft
```

## Korrekturen

Eine Korrektur wird nicht durch Löschen der früheren Beobachtung umgesetzt.

Frühere Beobachtung:

```yaml
status: corrected
corrected_by: obs-journal-2026-day-017-009
```

Neue Beobachtung:

```yaml
status: confirmed
corrects:
  - obs-journal-2026-day-017-001
facts:
  total_collection_count: 53
```

## Unsicherheit

Unsicherheit wird explizit gespeichert:

```yaml
uncertainty:
  fields:
    compendium_number: unbekannt
  reason: Nummer war im verfügbaren Material nicht lesbar
```

Es ist unzulässig, unbekannte Werte aus Gewohnheit oder externem Vorwissen zu ergänzen, ohne dafür eine Quelle anzulegen.

## Medien

```yaml
media:
  - id: screenshot-013
    type: image
    filename: null
    description: Kompendium zeigt Nummer 13
  - id: video-001
    type: video
    filename: 1000139807.mp4
    description: Tagesabschluss
```

## Duplikate

Automatisch erkannte mögliche Duplikate werden nur markiert:

```yaml
possible_duplicates:
  - obs-journal-2026-day-017-004
```

Eine Zusammenführung erfolgt erst nach Prüfung.

## Validierungsregeln

- `id` muss eindeutig sein.
- `source.source_id` darf nicht fehlen.
- `status` muss einem erlaubten Wert entsprechen.
- unbekannte Werte werden `null`, nicht leere Platzhaltertexte, sofern das Feld strukturiert ist.
- Korrekturverweise müssen auf existierende Beobachtungen zeigen.
- Eine Beobachtung darf mehrere Fakten enthalten, wenn sie durch denselben Forschungsvorgang gemeinsam belegt wurden.
- Mehrere unabhängige Sachverhalte werden in getrennte Beobachtungen aufgeteilt.

## Trennregel

Eine neue Beobachtung wird angelegt, wenn mindestens eines davon zutrifft:

- anderer Forschungsvorgang,
- andere Quelle,
- anderer Gegenstand,
- unabhängiger Forschungsstatus,
- eigene Korrekturhistorie erforderlich.

## Ziel

Das Schema soll automatische Verarbeitung ermöglichen, ohne die wissenschaftliche Nachvollziehbarkeit zu verlieren. Jede Beobachtung bleibt klein, quellengestützt, korrigierbar und maschinenlesbar.
