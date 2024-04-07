#!/usr/bin/env python3
import os
import sys
import shutil
from dmg_creator import create_dmg  # Importieren der Funktion

directory_to_watch = sys.argv[1]
image_format = "UDRW" if len(sys.argv) < 3 or sys.argv[2].lower() != "readonly" else "UDRO"
archived_directory = os.path.join(directory_to_watch, "Archived to DMG")

# Stelle sicher, dass das Archiv-Verzeichnis existiert
if not os.path.exists(archived_directory):
    os.makedirs(archived_directory)

# Überprüfe jedes Element im Verzeichnis
for item in os.listdir(directory_to_watch):
    full_path = os.path.join(directory_to_watch, item)
    
    # Ignoriere, wenn es eine versteckte oder DMG-Datei ist oder das Archiv-Verzeichnis selbst
    if item.startswith('.') or item.endswith('.dmg') or item == "Archived to DMG":
        continue
    
    # Erstelle DMG und verschiebe bei Erfolg
    if os.path.isfile(full_path) or os.path.isdir(full_path):
        if create_dmg(full_path, directory_to_watch, image_format):
            shutil.move(full_path, os.path.join(archived_directory, os.path.basename(full_path)))
