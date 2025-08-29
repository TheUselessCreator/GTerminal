from src.utils import gorilla_tag_installed, add_mod, remove_mod, panic_mods, backup_mods, install_gtag
from manager.featured_mods import list_featured_mods
from src.config import DISCORD_LINK, GITHUB_LINK

def handle_command(command, args=None):
    if command == "--help":
        return """
Gorilla Tag Mod Manager Commands:

--help       Show this help message
--discord    Open Discord server
--github     Open GitHub repo
--add        Add a mod from Downloads to plugins folder (--add modname.dll)
--remove     Remove a mod from plugins folder (--remove modname.dll)
--mods       Show featured mods
--install    Update Gorilla Tag to enable mods
--panic      Remove all mods from plugins folder
--backup     Backup all mods to Downloads
"""
    elif command == "--discord":
        return f"Join Discord: {DISCORD_LINK}"
    elif command == "--github":
        return f"GitHub: {GITHUB_LINK}"
    elif command == "--add":
        if not gorilla_tag_installed():
            return "Gorilla Tag not found. Please make sure it's installed via Steam."
        if not args:
            return "Please provide a mod file name."
        success, message = add_mod(args[0])
        return message
    elif command == "--remove":
        if not gorilla_tag_installed():
            return "Gorilla Tag not found."
        if not args:
            return "Please provide a mod file name to remove."
        success, message = remove_mod(args[0])
        return message
    elif command == "--mods":
        return list_featured_mods()
    elif command == "--install":
        success, message = install_gtag()
        return message
    elif command == "--panic":
        success, message = panic_mods()
        return message
    elif command == "--backup":
        success, message = backup_mods()
        return message
    else:
        return f"Unknown command: {command}. Use --help for commands."
