# Architektur des Moonlight-Peaks-Forschungswikis

## Ziel

Das Repository bildet einen nachvollziehbaren Weg von der ursprünglichen Forschung bis zur veröffentlichten Wiki-Seite ab. Jede veröffentlichte Aussage soll bis zu ihrer Quelle zurückverfolgt werden können.

```text
Forschungstagebuch
    ↓
Archivquelle
    ↓
Beobachtung
    ↓
Entität
    ↓
Wiki-Seite
```

## Ebenen

### 1. Originalquellen

Pfad: `archive/`

Originalquellen werden dauerhaft aufbewahrt und inhaltlich nicht nachträglich bereinigt. Dazu gehören Forschungstagebücher, Exporte, Screenshots, Videos, externe Quellen und Rohnotizen.

Regeln:

- Originalquellen werden niemals stillschweigend überschrieben.
- Fehler und spätere Korrekturen bleiben nachvollziehbar.
- Jede Quelle erhält eine stabile Kennung.
- Medien werden über Dateinamen, Pfad oder URL referenziert.

### 2. Beobachtungen

Pfad: `data/observations/`

Eine Beobachtung ist eine einzelne, quellengestützte Aussage. Sie beschreibt genau einen feststellbaren Sachverhalt, zum Beispiel einen Fundort, eine Uhrzeit, eine Farbe, einen Verkaufspreis oder einen Questfortschritt.

Beobachtungen enthalten mindestens:

- eindeutige Kennung,
- Typ,
- Aussage oder strukturierte Werte,
- Quellenverweis,
- Forschungsstatus,
- Zeitpunkt der Erfassung.

### 3. Entitäten

Pfad: `data/entities/`

Entitäten führen mehrere Beobachtungen zu einem konsolidierten Datensatz zusammen. Beispiele sind Seelentropfen, Vampster, Insekten, NPCs, Quests, Rezepte oder Gegenstände.

Entitäten dürfen widersprüchliche Beobachtungen enthalten, müssen diese aber kenntlich machen. Eine Entität ist keine Originalquelle.

### 4. Wiki-Seiten

Pfad: `docs/`

Wiki-Seiten sind die lesbare Darstellung der bestätigten oder ausreichend gekennzeichneten Daten. Sie dürfen redaktionell ergänzt werden, dürfen aber keine unbelegten Tatsachen als sicher darstellen.

### 5. Forschungsaufgaben

Pfad: `research/`

Offene Fragen, Hypothesen und geplante Tests werden getrennt von bestätigten Daten verwaltet.

Empfohlene Unterstruktur:

```text
research/
├── offene-fragen/
├── hypothesen/
└── experimente/
```

### 6. Generierte Ausgaben

Pfad: `generated/`

Automatisch erzeugte Berichte, Statistiken, Änderungslisten und Hilfsdateien werden hier abgelegt. Sie sind reproduzierbar und nicht die maßgebliche Datenquelle.

## Datenhoheit

Die maßgebliche Reihenfolge lautet:

1. Originalquelle belegt, was tatsächlich dokumentiert wurde.
2. Beobachtung beschreibt eine einzelne Auswertung der Quelle.
3. Entität konsolidiert mehrere Beobachtungen.
4. Wiki-Seite präsentiert den aktuellen Forschungsstand.

Bei Widersprüchen gilt nicht automatisch die jüngste Aussage. Entscheidend sind Quellenlage, Status und nachvollziehbare Korrekturen.

## Sicherheitsprinzipien

- Automatisierung darf Originalquellen nicht verändern.
- Automatisierung darf bestätigte Daten nicht ohne Prüfung überschreiben.
- Neue automatische Auswertungen werden zunächst über Pull Requests vorgeschlagen.
- Unvollständige Daten werden gespeichert und als unvollständig markiert.
- Korrekturen ersetzen nicht die Historie, sondern ergänzen sie.

## Zielstruktur

```text
archive/
    forschungstagebuecher/
research/
    offene-fragen/
    hypothesen/
    experimente/
data/
    observations/
    entities/
docs/
generated/
scripts/
.github/workflows/
```

## Nachvollziehbarkeit

Jede Wiki-Aussage soll langfristig folgende Kette ermöglichen:

```text
Wiki-Seite
→ Entität
→ Beobachtung
→ Forschungstagebuch
→ Screenshot, Video oder Notiz
```
