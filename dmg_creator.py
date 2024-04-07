# dmg_creator.py
import subprocess
import os

def create_dmg(source, destination, image_format="UDRW", filesystem="APFS"):
    volume_name = os.path.basename(source)
    dmg_name = os.path.splitext(volume_name)[0] + '.dmg'
    dmg_path = os.path.join(destination, dmg_name)

    # Ignoriere versteckte Dateien und DMG-Dateien
    if source.startswith('.') or source.endswith('.dmg'):
        print("Ignoriere Datei:", source)
        return False

    print(f"Erstelle {image_format} DMG für: {source}")

    command = f'hdiutil create -volname "{volume_name}" -srcfolder "{source}" -ov -fs {filesystem} -format {image_format} "{dmg_path}"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f"{image_format} DMG erfolgreich erstellt: {dmg_name}")
        return True
    else:
        print(f"Fehler beim Erstellen von {image_format} DMG für {source}: {stderr.decode()}")
        return False
