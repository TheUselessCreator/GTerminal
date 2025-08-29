import os
from colorama import init, Fore
from manager.mod_manager import handle_command
from src.config import DOWNLOADS_FOLDER

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = f"""{Fore.CYAN}
  /$$$$$$  /$$$$$$$$                                /$$                     /$$
 /$$__  $$|__  $$__/                               |__/                    | $$
| $$  \__/   | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$ | $$
| $$ /$$$$   | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$| $$__  $$ |____  $$| $$
| $$|_  $$   | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$| $$  \ $$  /$$$$$$$| $$
| $$  \ $$   | $$| $$_____/| $$      | $$ | $$ | $$| $$| $$  | $$ /$$__  $$| $$
|  $$$$$$/   | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$| $$  | $$|  $$$$$$$| $$
 \______/    |__/ \_______/|__/      |__/ |__/ |__/|__/|__/  |__/ \_______/|__/
                                                                               
                  GTerminal V1.0.0 Made by TheUseless --help
"""
    print(banner)

def main_loop():
    while True:
        try:
            command_input = input(Fore.GREEN + "\n> ").strip()
            if command_input.lower() in ["exit", "quit"]:
                print(Fore.RED + "Exiting GTerminal...")
                break
            
            if command_input == "":
                continue

            parts = command_input.split()
            command = parts[0]
            args = parts[1:] if len(parts) > 1 else None

            output = handle_command(command, args)

            # If mod not found, show available .dll files in Downloads
            if "Mod file not found in Downloads" in output:
                dll_files = [f for f in os.listdir(DOWNLOADS_FOLDER) if f.endswith(".dll")]
                if dll_files:
                    output += f"\nAvailable mods in Downloads:\n- " + "\n- ".join(dll_files)
                else:
                    output += "\nNo .dll files found in Downloads folder."
            
            print(Fore.CYAN + output)

        except KeyboardInterrupt:
            print(Fore.RED + "\nExiting GTerminal...")
            break
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    print_banner()
    main_loop()
