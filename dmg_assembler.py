#!/usr/bin/env python3
import os
import sys
import shutil
from dmg_creator import create_dmg

# Standardwerte setzen
directory_to_watch = sys.argv[1]
image_format = "UDRW"
destination_directory = directory_to_watch

# Überprüfe die Anzahl der Argumente, um den Modus und das Zielverzeichnis zu bestimmen
if len(sys.argv) > 2:
    if sys.argv[2].lower() == "readonly":
        image_format = "UDRO"
    else:
        destination_directory = sys.argv[2]
        if len(sys.argv) > 3 and sys.argv[3].lower() == "readonly":
            image_format = "UDRO"

archived_directory = os.path.join(directory_to_watch, "Archived to DMG")

# Stelle sicher, dass das Archiv-Verzeichnis und das Zielverzeichnis existieren
if not os.path.exists(archived_directory):
    os.makedirs(archived_directory)
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Überprüfe jedes Element im Verzeichnis
for item in os.listdir(directory_to_watch):
    full_path = os.path.join(directory_to_watch, item)
    
    # Ignoriere, wenn es eine versteckte oder DMG-Datei ist oder das Archiv-Verzeichnis selbst
    if item.startswith('.') or item.endswith('.dmg') or item == "Archived to DMG":
        continue
    
    # Erstelle DMG und verschiebe bei Erfolg
    if os.path.isfile(full_path) or os.path.isdir(full_path):
        if create_dmg(full_path, destination_directory, image_format):
            shutil.move(full_path, os.path.join(archived_directory, os.path.basename(full_path)))
