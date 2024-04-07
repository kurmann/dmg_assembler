#!/usr/bin/env python3
import os
import sys
import subprocess

# Überprüft, ob eine Eingangsvariable gesetzt ist; Default ist "UDRW"
image_format = "UDRW" if len(sys.argv) < 3 or sys.argv[2].lower() != "readonly" else "UDRO"
directory_to_watch = sys.argv[1]

# Funktion zum Erstellen des DMG mit APFS
def create_dmg(source):
    volume_name = os.path.basename(source)
    dmg_name = os.path.splitext(volume_name)[0] + '.dmg'
    dmg_path = os.path.join(directory_to_watch, dmg_name)

    # Ignoriere versteckte Dateien und DMG-Dateien
    if source.startswith('.') or source.endswith('.dmg'):
        print("Ignoriere Datei:", source)
        return

    print(f"Erstelle {image_format} DMG für: {source}")
    
    command = f'hdiutil create -volname "{volume_name}" -srcfolder "{source}" -ov -fs APFS -format {image_format} "{dmg_path}"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f"{image_format} DMG erfolgreich erstellt: {dmg_name}")
    else:
        print(f"Fehler beim Erstellen von {image_format} DMG für {source}: {stderr.decode()}")

# Überprüfe jedes Element im Verzeichnis
for item in os.listdir(directory_to_watch):
    full_path = os.path.join(directory_to_watch, item)
    
    # Ignoriere, wenn es eine versteckte oder DMG-Datei ist
    if item.startswith('.') or item.endswith('.dmg'):
        continue
    
    # Erstelle DMG für Dateien und Verzeichnisse
    if os.path.isfile(full_path) or os.path.isdir(full_path):
        create_dmg(full_path)
