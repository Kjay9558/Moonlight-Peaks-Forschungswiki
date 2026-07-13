# Festgelegte Datenstruktur

## Grundentscheidung

Das Wiki verwendet **YAML als kanonische Datenbasis**, **Markdown für lesbare Seiten** und ein **unverändertes Quellenarchiv**.

YAML wurde gewählt, weil die Datensätze gut lesbar, mit Git vergleichbar und später problemlos um neue Felder erweiterbar sind. Jedes Objekt besitzt ein stabiles `id`-Feld. Neue Felder dürfen ergänzt werden, ohne vorhandene Datensätze umzubauen.

## Datenfluss

`Quelle → Beobachtung → konsolidierte Entität → Wiki-Seite`

### Quelle

Ein Chatturn, Screenshot, Video oder später eine externe Quelle. Quellen werden nie überschrieben.

### Beobachtung

Eine einzelne Aussage, zum Beispiel:

```yaml
- id: obs-honig-preis-001
  claim: Honig verkauft sich für 20 Gold.
  status: confirmed
  subject_refs: [item-honig]
  context:
    season: spring
    year: 1
  source_refs:
    - source_id: chat-export-2026-07-13
      turn: 214
```

### Entität

Der aktuelle konsolidierte Wissensstand:

```yaml
- id: item-honig
  name: Honig
  status: confirmed
  fields:
    sale_price: 20
    category: food
  source_refs:
    - source_id: chat-export-2026-07-13
      turn: 214
```

### Korrekturen

Falsche Angaben werden nicht still gelöscht. Eine neue Beobachtung erhält `supersedes`, und die Entität bekommt einen Eintrag in `history`.

## Erweiterbarkeit

Kategoriespezifische Werte liegen unter `fields`. Dadurch können später Wetter, Saison, Koordinaten, Qualität, Buffs, Beziehungen, Plattformunterschiede oder Spielversionen ergänzt werden, ohne das Grundschema zu brechen.
