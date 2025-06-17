from pathlib import Path


AUDIO_EXTENSIONS = {".mp3", ".flac", ".wav", ".ogg", ".aac", ".m4a", ".m3u"}
def get_home_music_path():
    return Path.home() / "Music"

def list_files(current_dir:Path):
    if not current_dir.exists():
        print("Path does not exists!")
        return
    
        # Order folders and files
    entries = sorted(current_dir.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
    for entry in entries:
        if entry.is_dir() or entry.suffix.lower() in AUDIO_EXTENSIONS:
            icon = "U+1F5C0" if entry.is_dir() else "U+1F3B5"
            print(f"{icon} {entry.name}")

def change_dir(current_dir:Path, new_path=str) -> Path:
    target = (current_dir / new_path).resolve()
    
    if target.is_dir():
        return target
    else:
        print("Not a directory")
        return current_dir