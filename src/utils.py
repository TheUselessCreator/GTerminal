import os
import shutil
import random
from .config import STEAM_PATH, DOWNLOADS_FOLDER, BEPINEX_PLUGIN_PATH

def gorilla_tag_installed():
    """Check if Gorilla Tag is installed in the Steam path."""
    return os.path.exists(STEAM_PATH)

def add_mod(file_name):
    """Move a mod DLL from Downloads to Gorilla Tag BepInEx plugins folder."""
    src_path = os.path.join(DOWNLOADS_FOLDER, file_name)
    if not os.path.exists(src_path):
        return False, "Mod file not found in Downloads."

    if not os.path.exists(BEPINEX_PLUGIN_PATH):
        try:
            os.makedirs(BEPINEX_PLUGIN_PATH)
        except Exception as e:
            return False, f"Failed to create plugins folder: {e}"

    dest_path = os.path.join(BEPINEX_PLUGIN_PATH, file_name)
    try:
        shutil.move(src_path, dest_path)
        return True, f"Mod '{file_name}' added successfully to plugins folder!"
    except Exception as e:
        return False, f"Failed to move mod: {e}"

def remove_mod(file_name):
    """Remove a mod from the plugins folder."""
    mod_path = os.path.join(BEPINEX_PLUGIN_PATH, file_name)
    if not os.path.exists(mod_path):
        return False, f"Mod '{file_name}' not found in plugins folder."
    try:
        os.remove(mod_path)
        return True, f"Mod '{file_name}' removed successfully."
    except Exception as e:
        return False, f"Failed to remove mod: {e}"

def panic_mods():
    """Remove all mods from the plugins folder."""
    if not os.path.exists(BEPINEX_PLUGIN_PATH):
        return False, "Plugins folder not found."
    try:
        for f in os.listdir(BEPINEX_PLUGIN_PATH):
            file_path = os.path.join(BEPINEX_PLUGIN_PATH, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return True, "All mods removed from plugins folder!"
    except Exception as e:
        return False, f"Failed to remove mods: {e}"

def backup_mods():
    """Backup all mods to a folder in Downloads."""
    if not os.path.exists(BEPINEX_PLUGIN_PATH):
        return False, "Plugins folder not found."

    mods = [f for f in os.listdir(BEPINEX_PLUGIN_PATH) if f.endswith(".dll")]
    if not mods:
        return False, "No mods to backup."

    # Generate random 3-letter string
    rand_str = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    backup_folder = os.path.join(DOWNLOADS_FOLDER, f"Backup_Gtag{rand_str}")

    os.makedirs(backup_folder, exist_ok=True)

    try:
        for mod in mods:
            shutil.copy2(os.path.join(BEPINEX_PLUGIN_PATH, mod), backup_folder)
        return True, f"Backup created at {backup_folder}"
    except Exception as e:
        return False, f"Failed to backup mods: {e}"

def install_gtag():
    """
    Simulate updating Gorilla Tag so mods work.
    In reality, this would involve Steam commands or user confirmation.
    """
    if not gorilla_tag_installed():
        return False, "Gorilla Tag not found. Cannot install/update mods."
    return True, "Gorilla Tag 'updated' successfully. Mods should now work!"
