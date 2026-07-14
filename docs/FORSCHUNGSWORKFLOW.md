# Forschungsworkflow

## Ziel

Der Forschungsworkflow beschreibt, wie ein Spieltag vom Chat bis zur veröffentlichten Wiki-Aussage verarbeitet wird.

## Standardablauf

```text
Forschung im Chat
→ Tag abschließen
→ vollständige Forschungsakte erzeugen
→ GitHub-Issue anlegen
→ Archivdatei erzeugen
→ Beobachtungen extrahieren
→ Entitäten aktualisieren
→ Wiki generieren
→ Änderungen prüfen und mergen
```

## 1. Forschung im Chat

Während des Spielens werden Beobachtungen fortlaufend erfasst. Dazu gehören auch:

- unvollständige Funde,
- spontane Vermutungen,
- Korrekturen,
- Screenshots,
- Videos,
- Questfortschritte,
- Kompendium-Nummern,
- Uhrzeiten,
- Orte,
- Preise und Werte.

Nichts wird verworfen, nur weil ein Datensatz noch nicht vollständig ist.

## 2. Forschungstag abschließen

Der Abschlussbefehl lautet:

```text
Tag X archivieren
```

Daraufhin wird eine vollständige Forschungsakte erstellt. Sie enthält nicht nur eine Zusammenfassung, sondern alle verfügbaren Informationen des Tages in chronologischer und strukturierter Form.

## 3. GitHub-Issue als Eingang

Für jeden abgeschlossenen Tag wird ein Issue mit folgendem Titel angelegt:

```text
[Forschungstagebuch] Tag X
```

Das Issue ist der technische Eingang des Importprozesses. Es enthält die vollständige Forschungsakte und wird mit dem Import-Workflow verarbeitet.

## 4. Archivierung

Der GitHub-Workflow erzeugt aus dem Issue eine Datei unter:

```text
archive/forschungstagebuecher/JJJJ/tag-XXX-issue-NNN.md
```

Die Archivdatei enthält:

- Metadaten,
- vollständige chronologische Notizen,
- strukturierte Beobachtungsblöcke,
- Korrekturen,
- offene Fragen,
- Medienreferenzen,
- Verweis auf das Ursprungs-Issue.

Archivdateien werden nicht automatisch nachträglich verändert. Ergänzungen erfolgen über neue Quellen, Kommentare oder Korrekturbeobachtungen.

## 5. Beobachtungen extrahieren

Aus dem Archiv werden einzelne Beobachtungen erzeugt. Jede Beobachtung muss auf eine konkrete Stelle der Quelle verweisen.

Automatische Extraktion darf:

- neue Beobachtungen vorschlagen,
- unvollständige Beobachtungen anlegen,
- mögliche Duplikate markieren,
- Widersprüche erkennen.

Automatische Extraktion darf nicht:

- bestätigte Beobachtungen still überschreiben,
- Unsicherheiten entfernen,
- Quellenangaben weglassen,
- Vermutungen als bestätigte Fakten einstufen.

## 6. Entitäten konsolidieren

Beobachtungen werden passenden Entitäten zugeordnet. Dabei gelten folgende Regeln:

- identische Aussagen können zusammengeführt werden,
- widersprüchliche Aussagen bleiben sichtbar,
- Korrekturen erhalten einen Verweis auf die korrigierte Aussage,
- der Forschungsstatus wird nicht ohne nachvollziehbaren Grund erhöht.

## 7. Wiki erzeugen

Wiki-Seiten werden aus den Entitäten erzeugt oder redaktionell ergänzt. Nur ausreichend belegte Daten werden als Tatsachen dargestellt. Unsichere Informationen erhalten einen sichtbaren Forschungsstatus.

## 8. Pull Requests und Prüfung

Automatisch erzeugte Änderungen werden zunächst als Pull Request vorgeschlagen. Vor dem Merge wird geprüft:

- Ist die Originalquelle vollständig archiviert?
- Sind alle Beobachtungen mit Quellen verknüpft?
- Wurden Unsicherheiten korrekt übernommen?
- Gibt es unbemerkte Überschreibungen?
- Sind Korrekturen nachvollziehbar?
- Bleibt das Wiki baubar?

## Fehler- und Korrekturworkflow

Eine spätere Korrektur löscht die frühere Aussage nicht aus der Forschungshistorie.

Beispiel:

```text
Tag 17: Gesamtzahl zunächst als 51 notiert
Tag 17: später auf 53 korrigiert
```

Im Archiv bleiben beide Schritte erhalten. In den Beobachtungen wird die frühere Angabe als korrigiert markiert und mit der neuen Beobachtung verknüpft.

## Offene Forschung

Offene Fragen aus Forschungstagen werden zusätzlich unter `research/` erfasst. Beispiele:

- unbekannte Kompendium-Nummer,
- fehlende Spawnzeit,
- unbestätigter Fundort,
- Preis ohne Qualitätsstufe,
- nicht zugeordneter Screenshot.

## Medien

Medien werden nicht nur als allgemeiner Hinweis erwähnt. Jede relevante Datei erhält soweit möglich:

- Dateiname,
- Medientyp,
- Reihenfolge,
- zugehörige Beobachtung,
- Beschreibung des sichtbaren Inhalts.

## Qualitätsziel

Der Workflow ist erfolgreich, wenn eine Person später jede Wiki-Aussage bis zur ursprünglichen Notiz oder zum ursprünglichen Medium zurückverfolgen kann.
