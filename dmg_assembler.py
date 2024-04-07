#!/usr/bin/env python3
import os
import sys
import subprocess

# Das Verzeichnis aus den übergebenen Argumenten holen
directory_to_watch = sys.argv[1]

# Funktion zum Erstellen des DMG
def create_dmg(source):
    volume_name = os.path.basename(source)
    dmg_name = os.path.splitext(volume_name)[0] + '.dmg'
    dmg_path = os.path.join(directory_to_watch, dmg_name)

    # Stellen Sie sicher, dass wir keine DMGs erzeugen
    if source.endswith('.dmg'):
        return

    command = f'hdiutil create -volname "{volume_name}" -srcfolder "{source}" -ov -format UDRW "{dmg_path}"'
    subprocess.run(command, shell=True)

# Überprüfe jedes Element im Verzeichnis
for item in os.listdir(directory_to_watch):
    full_path = os.path.join(directory_to_watch, item)
    
    # Ignoriere, wenn es eine DMG-Datei ist
    if full_path.endswith('.dmg'):
        continue
    
    # Erstelle DMG für Dateien und Verzeichnisse
    if os.path.isfile(full_path) or os.path.isdir(full_path):
        create_dmg(full_path)