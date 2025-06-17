from pathlib import Path
import shutil

AUDIO_EXTENSIONS = {".mp3", ".flac", ".wav", ".ogg", ".aac", ".m4a", ".m3u"}
def get_home_music_path():
    return Path.home() / "Music"

def list_files(current_dir:Path):
    if not current_dir.exists():
        print("Path does not exists!")
        return
    
    # Order folders and files
    entries = sorted(
        (e for e in current_dir.iterdir() if e.is_dir() or e.suffix.lower() in AUDIO_EXTENSIONS), 
        key=lambda e: (not e.is_dir(), e.name.lower()))
    
    display_names = [
        f"{'📁' if e.is_dir() else '🎵'} {e.name}" for e in entries
    ]

    # Get terminal width
    terminal_width = shutil.get_terminal_size((80,20)).columns
    max_len = max(len(name) for name in display_names) if display_names else 0
    col_width = max_len + 4
    cols = max(1, terminal_width // col_width)
    # PRint in rows
    for i in range(0, len(display_names), cols):
        row = display_names[i:i+cols]
        print("".join(name.ljust(col_width) for name in row))
    
def change_dir(current_dir:Path, new_path=str) -> Path:
    target = (current_dir / new_path).resolve()
    
    if target.is_dir():
        return target
    else:
        print("Not a directory")
        return current_dir