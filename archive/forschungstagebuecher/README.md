# Forschungstagebücher

Dieser Ordner enthält die dauerhaft archivierten Forschungsnotizen aus den Spieltagebuch-Chats.

## Grundsatz

Die Dateien in diesem Ordner sind **Originalquellen**. Sie werden nicht stillschweigend korrigiert oder überschrieben. Spätere Auswertungen verweisen auf die jeweilige Datei und das zugehörige GitHub-Issue.

## Automatischer Import

1. In GitHub ein neues Issue mit der Vorlage **Forschungstag archivieren** erstellen.
2. Titel im Format `[Forschungstagebuch] Tag 19` verwenden.
3. Die von ChatGPT erzeugte Forschungsnotiz vollständig in das Issue einfügen.
4. Der Workflow legt daraus eine Datei unter `archive/forschungstagebuecher/` an.
5. Die Änderung wird als Pull Request geöffnet und erst nach Prüfung in `main` übernommen.

## Dateinamen

- `tag-017-issue-123.md`
- `tag-018-issue-124.md`

Die Issue-Nummer verhindert Namenskonflikte und erhält die Herkunft.

## Spätere Ausbaustufe

Aus den archivierten Quellen sollen getrennt erzeugt werden:

- Einzelbeobachtungen unter `data/observations/`
- konsolidierte Datensätze unter `data/entities/`
- daraus generierte Wiki-Seiten unter `docs/`

Automatisch erzeugte Daten dürfen bestätigte Angaben nicht ungeprüft überschreiben. Widersprüche und unvollständige Beobachtungen bleiben sichtbar.