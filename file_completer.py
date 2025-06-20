from prompt_toolkit.completion import Completer, Completion
from pathlib import Path


AUDIO_EXTENSIONS = {".mp3", ".flac", ".wav", ".ogg", ".aac", ".m4a", ".m3u"}



class CustomFileCompleter(Completer):
    def __init__(self, current_dir):
        self.current_dir = Path(current_dir)
        
        
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.strip()
        
        parts = text.split()
        if not parts:
            for entry in sorted(self.current_dir.iterdir()):
                if entry.is_dir() or entry.suffix.lower() in AUDIO_EXTENSIONS:
                    yield Completion(entry.name, start_position=0)
            return
        if len(parts) == 1 and not text.endswith(" "):
            return 
        
        
        last_word = parts[-1]
        base_dir = (self.current_dir / Path(last_word).parent).resolve()
        prefix = Path(last_word).name
        
        if not base_dir:
            return
        
        try:
            for child in base_dir.iterdir():
                if child.name.startswith(prefix):
                    suffix = "/" if child.is_dir() else ""
                    quoted = f'"{child.name}{suffix}"' if ' ' in child.name else f"{child.name}{suffix}"
                    yield Completion(quoted, start_position=-len(prefix))
        except FileNotFoundError:
            pass