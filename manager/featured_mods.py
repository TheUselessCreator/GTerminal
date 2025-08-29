FEATURED_MODS = [
    {"name": "ExtraJump", "github": "https://github.com/user/ExtraJump"},
    {"name": "SpeedBoost", "github": "https://github.com/user/SpeedBoost"},
    {"name": "WallHack", "github": "https://github.com/user/WallHack"},
]

def list_featured_mods():
    return "\n".join([f"{mod['name']}: {mod['github']}" for mod in FEATURED_MODS])
