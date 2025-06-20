from pathlib import Path
from typing import List


class Playlist:
    def __init__(self):
        self.tracks : List[Path] = []
        
    def add(self, file:Path):
        if file.exists() and file.is_file():
            if file not in self.tracks:
                self.tracks.append(file)
                print(f"Added: {file.name}")
            else:
                print(f"File already in playlist: {file.name}")
        else:
            print(f"File Not Found: {file.name}")
            
    def remove(self, file: Path):
        try:
            self.tracks.remove(file)
            print(f"Removed: {file.name}")
        except ValueError:
            print(f"{file.name} not in Playlist! ")
    
    def list(self):
        if not self.tracks:
            print("Playlist is Empty!")
            return
        for i, track in enumerate(self.tracks, 1):
            print(f"{i:02d}. {track.name}")
        
    
    def save(self, output_path:Path, relative=False):
        with output_path.open("w", encoding="utf-8") as f:
            for track in self.tracks:
                line = track.name if relative else str(track.resolve())
                f.write(f"{line}\n")
        print(f"Playlist saved in {output_path}!")
        
    def clear(self):
        self.tracks = []