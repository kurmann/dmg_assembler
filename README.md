# DMG Assembler

`dmg-assembler` ist ein Python-Skript zur automatischen Erstellung von DMG-Dateien (Disk Images) aus Dateien und Verzeichnissen auf macOS. Es ermöglicht Nutzern, Final Cut Pro-Bundles, einzelne Dateien oder ganze Verzeichnisse effizient zu archivieren, indem es diese in DMG-Dateien umwandelt. Dieses Tool ist besonders nützlich für Entwickler, Content-Creators und jeden, der regelmäßig Dateien und Verzeichnisse für die Archivierung oder Verteilung verpacken muss.

## Features

- Automatische Erstellung von DMG-Dateien aus jedem Verzeichnis oder jeder Datei.
- Behandlung von Final Cut Pro-Bundles als Einzeldateien.
- Einfacher Einsatz durch Integration mit macOS Automator.
- Unterstützung für benutzerdefinierte DMG-Eigenschaften wie Volume-Name.

## Voraussetzungen

- macOS
- Python 3.x

## Installation

Klonen Sie das Repository oder laden Sie den Code herunter:

```bash
git clone https://github.com/IhrBenutzername/dmg-assembler.git
```

Navigieren Sie in das Verzeichnis des heruntergeladenen Repositories:

```bash
cd dmg-assembler
```

Machen Sie das Skript ausführbar:

```bash
chmod +x dmg_assembler.py
```

## Verwendung

Um `dmg-assembler` zu nutzen, führen Sie das Skript mit dem Pfad zum Zielverzeichnis als Argument aus:

```bash
./dmg_assembler.py /Pfad/zum/Verzeichnis
```

Das Skript durchläuft das angegebene Verzeichnis und erstellt für jede darin gefundene Datei oder jedes Verzeichnis eine separate DMG-Datei.

## Beitrag

Beiträge sind herzlich willkommen! Bitte erstellen Sie einen Pull Request, um Verbesserungen vorzuschlagen, oder melden Sie Probleme im Issues-Bereich.

## Lizenz

`dmg-assembler` ist unter der MIT-Lizenz veröffentlicht. Weitere Informationen finden Sie in der [LIZENZ](LIZENZ)-Datei.

## Änderungsverlauf

### Unveröffentlicht

- keine

### Version 0.3 - 2024-04-07

#### Hinzugefügt

- Möglichkeit als Eingabeparameter festzulegen, ob ein Image beschreibbar ist oder nicht.
- Möglichkeit das Zielverzeichnis anzugeben (Standard ist das Eingabeverzeichnis)

#### Geändert

- Verwendet Apple Filesystem als DMG-Dateisystem
- Verschiebt erfogreich verarbeitete Dateien ins Unterverzeichnis "Archived to DMG"

### Version 0.2 - 2024-04-07

#### Geändert

- Verbesserte Statusmeldungen

#### Behoben

- Versteckte Dateien im Wurzelverzeichnis werden nicht als einzelnes DMG archivier

### Version 0.1 - 2024-04-07

#### Hinzugefügt

- Erste Vesion