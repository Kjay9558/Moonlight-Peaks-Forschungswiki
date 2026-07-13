# Styleguide des Moonlight Peaks Forschungswikis

Dieser Styleguide legt die verbindlichen Regeln für Aufbau, Sprache, Gestaltung und Quellenarbeit im Moonlight Peaks Forschungswiki fest.

Ziel ist ein konsistentes, gut lesbares und langfristig wartbares deutschsprachiges Wiki.

---

## 1. Sprache

Das Forschungswiki wird vollständig auf Deutsch geschrieben.

Offizielle englische Spielbegriffe bleiben erhalten, wenn sie im Spiel selbst auf Englisch angezeigt werden oder für die eindeutige Zuordnung wichtig sind.

Beim ersten Auftreten wird der englische Begriff zusammen mit der deutschen Bezeichnung genannt.

Beispiel:

> Das **Bug Net (Fangnetz)** wird zum Fangen von Insekten verwendet.

Danach kann innerhalb derselben Seite bevorzugt die deutsche Bezeichnung verwendet werden.

### Schreibweise

- Fließtexte werden auf Deutsch geschrieben.
- Offizielle Namen von Gegenständen, Orten, Charakteren und Fähigkeiten werden nicht frei übersetzt.
- Eigene deutsche Erklärungen werden ergänzend verwendet.
- Spieltitel werden kursiv geschrieben: *Moonlight Peaks*.
- Unsichere Übersetzungen werden vermieden.
- Begriffe werden im gesamten Wiki einheitlich verwendet.

---

## 2. Ordner- und Dateinamen

Ordner- und Dateinamen werden grundsätzlich auf Englisch geschrieben.

Sie bestehen ausschließlich aus:

- Kleinbuchstaben
- Zahlen
- Bindestrichen

Leerzeichen, Unterstriche und Großbuchstaben werden nicht verwendet.

### Richtig

```text
bug-net.md
bug-catching.md
black-tulip.md
gift-preferences.md
moonlight-flowers.md
```

### Falsch

```text
BugNet.md
Bug Net.md
bug_net.md
Schwarze-Tulpe.md
```

### Ordnerstruktur

Thematisch zusammengehörige Dateien werden in gemeinsamen Ordnern abgelegt.

Beispiel:

```text
docs/
└── gameplay/
    └── insects/
        ├── index.md
        ├── bug-net.md
        ├── bug-catching.md
        └── insect-spawns.md
```

Jeder größere Themenbereich erhält eine `index.md`.

---

## 3. Frontmatter

Jede Inhaltsseite beginnt mit einem YAML-Frontmatter.

Mindestens enthalten sein müssen:

```yaml
---
title: Seitentitel
description: Kurze Beschreibung des Seiteninhalts.
---
```

### Beispiel

```yaml
---
title: Fangnetz
description: Informationen zur Freischaltung, Herstellung und Verwendung des Fangnetzes in Moonlight Peaks.
---
```

Der Titel wird auf Deutsch geschrieben.

Die Beschreibung soll:

- kurz sein,
- den Inhalt der Seite eindeutig wiedergeben,
- keine unnötigen Füllwörter enthalten,
- nach Möglichkeit den offiziellen englischen Begriff erwähnen, wenn er wichtig ist.

---

## 4. Überschriften

Jede Seite besitzt genau eine Hauptüberschrift der Ebene 1.

```md
# Fangnetz
```

Weitere Abschnitte verwenden Ebene 2.

```md
## Freischaltung
## Herstellung
## Verwendung
```

Unterabschnitte verwenden Ebene 3.

```md
### Benötigte Materialien
### Bekannte Einschränkungen
```

Überschriftenebenen dürfen nicht übersprungen werden.

### Falsch

```md
# Fangnetz
### Herstellung
```

### Richtig

```md
# Fangnetz
## Herstellung
### Benötigte Materialien
```

---

## 5. Standardaufbau einer Seite

Nicht jeder Abschnitt ist für jeden Seitentyp erforderlich. Die Reihenfolge soll jedoch nach Möglichkeit beibehalten werden.

```text
Frontmatter
Hauptüberschrift
Infobox
Einleitung
Übersicht
Freischaltung oder Erwerb
Herstellung oder Beschaffung
Verwendung
Mechaniken
Tipps
Forschungsnotizen
Forschungsstatus
Siehe auch
Quellen
```

### Empfohlene Grundstruktur

```md
---
title: Seitentitel
description: Kurze Beschreibung.
---

# Seitentitel

Infobox

Kurze Einleitung zum Thema.

## Übersicht

## Freischaltung

## Herstellung

## Verwendung

## Tipps

## Forschungsnotizen

## Forschungsstatus

## Siehe auch

## Quellen
```

Leere Abschnitte werden nicht angelegt, nur um die Standardstruktur vollständig erscheinen zu lassen.

---

## 6. Infoboxen

Jede geeignete Seite erhält am Anfang eine Infobox.

Die Infobox steht direkt unter der Hauptüberschrift und vor dem Einleitungstext.

Infoboxen sollen:

- wichtige Daten schnell erfassbar darstellen,
- auf Smartphones gut lesbar bleiben,
- einheitliche Feldnamen verwenden,
- keine langen Fließtexte enthalten,
- unbekannte Werte klar kennzeichnen.

Unbekannte Werte werden mit `Unbekannt` oder `❓ Unbekannt` angegeben.

### Allgemeines Tabellenformat

```md
| Eigenschaft | Wert |
|---|---|
| Englischer Name | Bug Net |
| Kategorie | Werkzeug |
| Forschungsstatus | 🧪 In Untersuchung |
```

---

## 7. Infobox: Werkzeug

Werkzeugseiten verwenden nach Möglichkeit folgende Felder:

```md
| Eigenschaft | Wert |
|---|---|
| Deutscher Name | Fangnetz |
| Englischer Name | Bug Net |
| Kategorie | Werkzeug |
| Freischaltung | Unbekannt |
| Herstellung | Herstellbar |
| Verbesserbar | Unbekannt |
| Verwendungszweck | Insekten fangen |
| Forschungsstatus | 🧪 In Untersuchung |
```

Nicht benötigte Felder dürfen weggelassen werden.

---

## 8. Infobox: Charakter

Charakterseiten verwenden nach Möglichkeit folgende Felder:

```md
| Eigenschaft | Wert |
|---|---|
| Name | Alina |
| Familie | Khazan |
| Geburtstag | Frühling 10 |
| Wohnort | Unbekannt |
| Romanze möglich | Ja |
| Forschungsstatus | ✅ Bestätigt |
```

Weitere mögliche Felder:

- Spezies
- Beruf
- Verwandtschaft
- Laden
- Öffnungszeiten
- Erstes Auftreten

---

## 9. Infobox: Gegenstand

Gegenstandsseiten verwenden nach Möglichkeit folgende Felder:

```md
| Eigenschaft | Wert |
|---|---|
| Name | Gegenstandsname |
| Englischer Name | Offizieller Name |
| Kategorie | Ressource |
| Verkaufspreis | Unbekannt |
| Stapelgröße | Unbekannt |
| Fundort | Unbekannt |
| Forschungsstatus | 🧪 In Untersuchung |
```

---

## 10. Infobox: Pflanze

Pflanzenseiten verwenden nach Möglichkeit folgende Felder:

```md
| Eigenschaft | Wert |
|---|---|
| Name | Schwarze Tulpe |
| Englischer Name | Black Tulip |
| Jahreszeit | Frühling |
| Saatgut | Unbekannt |
| Wachstumstage | Unbekannt |
| Nachwachsende Ernte | Nein |
| Verkaufspreis | Unbekannt |
| Verarbeitung | Unbekannt |
| Forschungsstatus | 🧪 In Untersuchung |
```

---

## 11. Infobox: Insekt

Insektenseiten verwenden nach Möglichkeit folgende Felder:

```md
| Eigenschaft | Wert |
|---|---|
| Name | Insektenname |
| Englischer Name | Offizieller Name |
| Jahreszeit | Unbekannt |
| Tageszeit | Unbekannt |
| Wetter | Unbekannt |
| Fundort | Unbekannt |
| Verkaufspreis | Unbekannt |
| Forschungsstatus | 🧪 In Untersuchung |
```

---

## 12. Infobox: Fisch

Fischseiten verwenden nach Möglichkeit folgende Felder:

```md
| Eigenschaft | Wert |
|---|---|
| Name | Fischname |
| Englischer Name | Offizieller Name |
| Jahreszeit | Unbekannt |
| Tageszeit | Unbekannt |
| Wetter | Unbekannt |
| Gewässer | Unbekannt |
| Fundort | Unbekannt |
| Verkaufspreis | Unbekannt |
| Forschungsstatus | 🧪 In Untersuchung |
```

---

## 13. Forschungsstatus

Der Forschungsstatus zeigt, wie zuverlässig eine Information ist.

Folgende Status werden verwendet:

| Symbol | Status | Bedeutung |
|---|---|---|
| ✅ | Bestätigt | Durch eigene Tests oder mehrere zuverlässige Quellen bestätigt |
| 🧪 | In Untersuchung | Hinweise sind vorhanden, aber noch nicht vollständig bestätigt |
| 🔄 | Wird überprüft | Die Information wird aktuell erneut getestet |
| ❓ | Unbekannt | Es liegen noch keine ausreichenden Daten vor |
| ⚠️ | Veraltet | Die Information stammt aus einer älteren Spielversion und könnte nicht mehr gelten |

### Bestätigt

Der Status `✅ Bestätigt` wird verwendet, wenn mindestens eine der folgenden Bedingungen erfüllt ist:

- Die Information wurde im eigenen Spiel reproduzierbar getestet.
- Die Information wurde durch mehrere unabhängige Quellen bestätigt.
- Die Information stammt direkt aus dem Spiel.
- Die Information wurde durch verlässliches Datamining belegt.

### In Untersuchung

Der Status `🧪 In Untersuchung` wird verwendet, wenn:

- nur eine einzelne Beobachtung vorliegt,
- Community-Berichte widersprüchlich sind,
- genaue Bedingungen noch fehlen,
- eine Aussage plausibel, aber nicht reproduzierbar getestet ist.

### Wird überprüft

Der Status `🔄 Wird überprüft` wird verwendet, wenn:

- ein vorhandener Eintrag gezielt erneut getestet wird,
- ein Update die Mechanik verändert haben könnte,
- widersprüchliche neue Daten vorliegen.

### Unbekannt

Der Status `❓ Unbekannt` wird verwendet, wenn:

- keine ausreichenden Informationen vorliegen,
- ein Wert noch nicht ermittelt wurde,
- eine Mechanik bislang nicht dokumentiert ist.

### Veraltet

Der Status `⚠️ Veraltet` wird verwendet, wenn:

- die Information aus einer älteren Spielversion stammt,
- ein Update die Mechanik verändert hat,
- der ursprüngliche Zustand nur noch historisch relevant ist.

Veraltete Informationen dürfen erhalten bleiben, wenn sie für die Versionsgeschichte oder Forschung relevant sind. Sie müssen jedoch eindeutig als veraltet gekennzeichnet werden.

---

## 14. Forschungsstatus auf Seiten

Jede Seite erhält am Ende einen Abschnitt zum Forschungsstatus, sofern noch offene oder unterschiedlich sichere Informationen vorhanden sind.

Beispiel:

```md
## Forschungsstatus

| Thema | Status |
|---|:---:|
| Existenz des Werkzeugs | ✅ Bestätigt |
| Freischaltung | 🧪 In Untersuchung |
| Herstellungsrezept | ❓ Unbekannt |
| Verbesserungen | ❓ Unbekannt |
```

Sind alle Informationen einer kurzen Seite vollständig bestätigt, kann ein einzelner Hinweis ausreichen:

```md
## Forschungsstatus

Die auf dieser Seite aufgeführten Informationen sind aktuell vollständig bestätigt.
```

---

## 15. Hinweisboxen

Für besondere Hinweise werden MkDocs-Admonitions verwendet.

### Bestätigte Information

```md
!!! success "Bestätigt"

    Diese Information wurde im eigenen Spiel überprüft.
```

### Forschungsbedarf

```md
!!! warning "Forschungsstatus"

    Die genauen Voraussetzungen werden derzeit noch untersucht.
```

### Beobachtung

```md
!!! info "Beobachtung"

    Das Insekt erschien während eines regnerischen Abends.
```

### Veraltete Information

```md
!!! danger "Veraltete Information"

    Diese Angabe stammt aus einer älteren Spielversion.
```

Hinweisboxen werden sparsam verwendet. Normale Informationen gehören in den Fließtext oder in Tabellen.

---

## 16. Forschungsnotizen

Unbestätigte Beobachtungen werden nicht als gesicherte Fakten formuliert.

Sie werden unter `Forschungsnotizen` dokumentiert.

Beispiel:

```md
## Forschungsnotizen

!!! info "Beobachtung"

    Das Fangnetz scheint nach dem Schwingen eine kurze Abklingzeit zu besitzen.

!!! warning "Noch unbestätigt"

    Es ist derzeit unbekannt, ob sich die Abklingzeit durch Verbesserungen verändert.
```

Forschungsnotizen sollen möglichst enthalten:

- Datum der Beobachtung
- Spielversion
- Jahreszeit
- Tageszeit
- Wetter
- Fundort
- verwendete Plattform
- besondere Bedingungen

Beispiel:

```md
### Beobachtung vom 13. Juli 2026

- Plattform: PC
- Spielversion: Unbekannt
- Jahreszeit: Frühling
- Tageszeit: Abend
- Wetter: Regen
- Beobachtung: Das Insekt erschien in der Nähe des Sees.
```

---

## 17. Eigene Forschung

Eigene Tests werden nachvollziehbar dokumentiert.

Eine Forschungsangabe sollte möglichst beantworten:

- Was wurde getestet?
- Unter welchen Bedingungen?
- Wie oft wurde es beobachtet?
- War das Ergebnis reproduzierbar?
- Welche Spielversion wurde verwendet?

Beispiel:

```md
### Eigener Test

- Datum: 13. Juli 2026
- Plattform: PC
- Spielversion: Unbekannt
- Test: Annäherung an ein Insekt im Gehen und Rennen
- Ergebnis: Beim Rennen floh das Insekt früher.
- Wiederholungen: 3
- Status: 🧪 In Untersuchung
```

Ein einzelner Test gilt nicht automatisch als endgültige Bestätigung.

---

## 18. Tabellen

Tabellen werden für strukturierte Daten verwendet.

### Format

```md
| Eigenschaft | Wert |
|---|---|
| Kategorie | Werkzeug |
| Verkaufspreis | Unbekannt |
```

Zahlen können rechtsbündig formatiert werden:

```md
| Material | Menge |
|---|---:|
| Holz | 10 |
| Stoff | 2 |
```

Tabellen sollen auf Smartphones lesbar bleiben.

Sehr breite Tabellen werden vermieden. Falls nötig, werden Informationen auf mehrere Tabellen oder Abschnitte verteilt.

---

## 19. Listen

Listen werden verwendet, wenn die Reihenfolge nicht zwingend wichtig ist.

```md
- Frühling
- Sommer
- Herbst
```

Nummerierte Listen werden für Abläufe verwendet.

```md
1. Fangnetz ausrüsten.
2. Insekt langsam annähern.
3. Fangnetz im richtigen Moment verwenden.
```

Listen mit nur einem einzelnen Punkt werden vermieden.

---

## 20. Interne Links

Interne Links werden als relative Markdown-Links geschrieben.

### Richtig

```md
[Insekten](index.md)
[Fangmechanik](bug-catching.md)
[Alina](../../characters/alina.md)
```

### Falsch

```md
[[Insekten]]
[[Bug Catching]]
```

Links dürfen erst gesetzt werden, wenn der Zielpfad bekannt ist.

Noch nicht vorhandene Seiten können im Abschnitt `Siehe auch` als geplanter Inhalt genannt werden, sollten aber nicht als kaputter Link angelegt werden.

Beispiel:

```md
## Siehe auch

- [Insekten](index.md)
- Fangmechanik *(geplant)*
- Liste aller Insekten *(geplant)*
```

---

## 21. Abschnitt „Siehe auch“

Der Abschnitt `Siehe auch` steht grundsätzlich vor den Quellen.

Er enthält nur direkt verwandte Themen.

Beispiel:

```md
## Siehe auch

- [Insekten](index.md)
- [Fangmechanik](bug-catching.md)
- [Jahreszeiten](../../world/seasons.md)
```

Eine Seite sollte nicht auf sich selbst verlinken.

---

## 22. Quellen

Jede Seite mit konkreten Spieldaten erhält einen Abschnitt `Quellen`.

Die Quellen werden nach Art getrennt.

### Standardstruktur

```md
## Quellen

### Eigene Forschung

- Eigener Test, PC, 13. Juli 2026.

### Offizielle Quellen

- Offizielle Spielbeschreibung.
- Patchnotes der jeweiligen Spielversion.

### Community-Quellen

- Community-Wiki.
- Reddit-Beitrag.
- Discord-Beobachtung.

### Datamining

- Aus Spieldateien ermittelte Daten.
```

Nicht vorhandene Unterabschnitte werden weggelassen.

---

## 23. Quellenqualität

Quellen werden nach Möglichkeit in folgender Reihenfolge gewichtet:

1. Direkt im Spiel sichtbare Daten
2. Reproduzierbare eigene Tests
3. Offizielle Aussagen und Patchnotes
4. Verlässliches Datamining
5. Mehrere übereinstimmende Community-Quellen
6. Einzelne Community-Beobachtungen
7. Vermutungen

Eine einzelne Community-Aussage wird nicht als bestätigte Tatsache übernommen.

Widersprüchliche Quellen werden transparent dokumentiert.

Beispiel:

```md
!!! warning "Widersprüchliche Angaben"

    Zwei Community-Quellen nennen unterschiedliche Jahreszeiten. Eine eigene Überprüfung steht noch aus.
```

---

## 24. Bilder

Bilder werden in einem thematisch passenden Unterordner gespeichert.

Empfohlene Struktur:

```text
docs/
└── assets/
    └── images/
        ├── tools/
        ├── characters/
        ├── crops/
        ├── insects/
        ├── fish/
        └── locations/
```

Dateinamen folgen denselben Regeln wie Markdown-Dateien.

Beispiel:

```text
bug-net.png
alina-portrait.png
black-tulip.png
```

### Alt-Texte

Jedes Bild erhält einen beschreibenden Alt-Text.

```md
![Das Fangnetz im Inventar](../../assets/images/tools/bug-net.png)
```

Nicht verwenden:

```md
![](image.png)
```

Bilder sollen:

- nicht unnötig groß sein,
- auf mobilen Geräten funktionieren,
- keine fremden Wasserzeichen enthalten,
- nur verwendet werden, wenn die Nutzungsrechte geklärt sind.

---

## 25. Mobile Darstellung

Das Wiki wird grundsätzlich auch für Smartphones gestaltet.

Deshalb gelten folgende Regeln:

- Tabellen möglichst schmal halten.
- Keine langen untrennbaren Textzeilen verwenden.
- Große Bilder responsiv einbinden.
- Infoboxen nicht ausschließlich für Desktop gestalten.
- Inhalte in kurze, klar gegliederte Abschnitte aufteilen.
- Keine wichtigen Informationen nur über Hover-Effekte darstellen.
- Karten und Grids müssen auch einspaltig funktionieren.

---

## 26. Schreibstil

Der Schreibstil ist:

- sachlich,
- verständlich,
- freundlich,
- präzise,
- möglichst spoilerarm,
- frei von unnötiger Wertung.

### Vermeiden

- „Ich glaube“
- „Vielleicht“
- „Bestimmt“
- „Offensichtlich“
- „Wie jeder weiß“
- unbelegte Superlative
- unnötige Umgangssprache

### Stattdessen

```md
Die genaue Bedingung ist derzeit unbekannt.
```

oder:

```md
Bisherige Beobachtungen deuten darauf hin, dass das Insekt nur am Abend erscheint.
```

---

## 27. Spoiler

Storyrelevante Informationen werden zurückhaltend formuliert.

Deutliche Spoiler werden mit einer Warnung gekennzeichnet.

```md
??? warning "Story-Spoiler"

    Dieser Inhalt verrät ein späteres Ereignis.
```

Informationen, die für Freischaltungen notwendig sind, sollen so spoilerarm wie möglich beschrieben werden.

---

## 28. Versionierung

Spielmechaniken können sich durch Updates verändern.

Wenn bekannt, wird die getestete Spielversion angegeben.

Beispiel:

```md
!!! info "Spielversion"

    Zuletzt überprüft in Version 0.0.0 auf dem PC.
```

Ändert sich eine Mechanik, wird die alte Information nicht kommentarlos überschrieben.

Stattdessen wird dokumentiert:

- welche Information vorher galt,
- ab welcher Version sie geändert wurde,
- wie der aktuelle Stand lautet.

---

## 29. Umgang mit unbekannten Daten

Unbekannte Daten werden nicht geschätzt.

### Richtig

```md
| Verkaufspreis | Unbekannt |
```

### Falsch

```md
| Verkaufspreis | Vermutlich etwa 100 |
```

Schätzungen dürfen nur in Forschungsnotizen stehen und müssen klar als Schätzung bezeichnet werden.

---

## 30. Seitenindex

Jeder größere Ordner besitzt eine `index.md`.

Eine Indexseite enthält:

- eine kurze Einführung,
- Links zu den Unterseiten,
- gegebenenfalls eine Übersichtskarte,
- offene Forschungsbereiche.

Beispiel:

```md
---
title: Insekten
description: Übersicht über Insekten und das Käferfangen in Moonlight Peaks.
---

# Insekten

Insekten können mit dem Fangnetz gefangen werden.

## Themen

- [Fangnetz](bug-net.md)
- Fangmechanik *(geplant)*
- Insektenarten *(geplant)*
- Spawnbedingungen *(geplant)*
```

---

## 31. Seitentypen

Für folgende Themen werden eigene Seiten bevorzugt:

- Charaktere
- Werkzeuge
- Pflanzen
- Fische
- Insekten
- Gegenstände
- Gebäude
- Orte
- Quests
- Rezepte
- Spielmechaniken
- Festivals
- Fähigkeiten
- Geschäfte

Eine Seite soll möglichst ein klar abgegrenztes Hauptthema behandeln.

---

## 32. Duplikate vermeiden

Informationen werden nur an einer zentralen Stelle vollständig gepflegt.

Andere Seiten verlinken auf diese Hauptseite.

Beispiel:

Die vollständigen Geschenkvorlieben eines Charakters stehen auf dessen Charakterseite.

Eine allgemeine Geschenkseite darf eine Kurzfassung enthalten, sollte aber auf die Charakterseite verweisen.

Dadurch werden widersprüchliche Daten vermieden.

---

## 33. Navigation

Neue Seiten werden erst dann in die Navigation aufgenommen, wenn:

- die Datei existiert,
- ein sinnvoller Grundinhalt vorhanden ist,
- der Titel feststeht,
- der Pfad korrekt ist.

Bezeichnungen in der Navigation werden auf Deutsch geschrieben.

Beispiel:

```yaml
nav:
  - Gameplay:
      - Übersicht: gameplay/index.md
      - Insekten:
          - Übersicht: gameplay/insects/index.md
          - Fangnetz: gameplay/insects/bug-net.md
```

---

## 34. Qualitätsprüfung vor einem Commit

Vor dem Commit sollte geprüft werden:

- Ist die Seite vollständig auf Deutsch?
- Sind offizielle englische Begriffe korrekt geschrieben?
- Ist das Frontmatter vorhanden?
- Gibt es genau eine Hauptüberschrift?
- Stimmen alle relativen Links?
- Sind unbekannte Werte klar markiert?
- Ist der Forschungsstatus nachvollziehbar?
- Sind Quellen angegeben?
- Funktioniert die Darstellung auf dem Smartphone?
- Enthält die Seite unbelegte Aussagen?
- Wurden unnötige Duplikate vermieden?

---

## 35. Commit-Namen

Commit-Namen folgen diesem Schema:

```text
aktion thema
```

Verwendete Aktionen:

| Aktion | Verwendung |
|---|---|
| `add` | Neue Dateien oder Inhalte hinzufügen |
| `change` | Bestehende Inhalte verändern oder erweitern |
| `fix` | Fehler beheben |
| `update` | Daten oder Medien aktualisieren |
| `refactor` | Struktur verändern, ohne den Inhalt wesentlich zu ändern |
| `remove` | Dateien oder Inhalte entfernen |

### Beispiele

```text
add styleguide
add bug net page
add insect navigation
change research status
fix broken links
update character data
refactor gameplay structure
remove duplicate gift data
```

Commit-Namen werden:

- kleingeschrieben,
- kurz gehalten,
- ohne Punkt beendet,
- möglichst eindeutig formuliert.

---

## 36. Weiterentwicklung des Styleguides

Dieser Styleguide darf erweitert werden, wenn neue Seitentypen oder wiederkehrende Anforderungen entstehen.

Änderungen sollen:

- bestehende Inhalte berücksichtigen,
- möglichst rückwärtskompatibel sein,
- klar dokumentiert werden,
- anschließend auf neue Seiten konsequent angewendet werden.

Bei widersprüchlichen Regeln gilt die zuletzt beschlossene und dokumentierte Regel.