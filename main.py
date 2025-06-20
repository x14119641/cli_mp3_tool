from pathlib import Path
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory, InMemoryHistory
from file_completer import CustomFileCompleter
from utils import resolve_paths
import shlex
import file_browser
import playlist

current_dir = Path.cwd()
playlist = playlist.Playlist()

#  C:\Users\danie\Documents\Soulseek Downloads\complete\spartano\(1992) En Directo A Todo Gas
def show_help():
    print("""
Available commands: (Well we are updating, this just an example)
  ls                     List files and folders
  cd <folder>            Change directory
  add <file or pattern>  Add files to playlist
  remove <file>          Remove file from playlist
  list                   Show playlist files
  save <name.m3u>        Save playlist
  export <folder>        Copy files to folder in order
  clear                  Clear playlist
  load <file.m3u>        Load existing playlist
  info                   Show playlist info
  pwd                    Show current directory
  help or ?              Show this help
  exit                   Exit the app
""")


def repl():
    global current_dir
    # history = FileHistory(".cli_history")
    history = InMemoryHistory()

    while True:
        try:
            completer = CustomFileCompleter(str(current_dir))
            cmd_line = prompt(f"[{current_dir} > ", completer=completer, history=history, complete_while_typing=True)
            
            if not cmd_line:
                continue
            # Handle help
            if cmd_line == "?" or cmd_line == "help":
                show_help()
                continue
            # Handle wildcard ? to show content in directory
            if "?" in cmd_line:
                print("Files and folders in current cirectory:")
                file_browser.list_files(current_dir)
            
            cmd_parts = shlex.split(cmd_line, posix=False)
            cmd, *args = cmd_parts
            
            if cmd == "ls":
                file_browser.list_files(current_dir=current_dir)
            elif cmd == "cd":
                if args:
                    path_input = " ".join(args).strip('"')
                    current_dir = file_browser.change_dir(current_dir, path_input)
                    completer = CustomFileCompleter(str(current_dir)) # Refresh currentdir in compiler
                else:
                    print("To use cd please: use <folder>")
            elif cmd == "pwd":
                print(current_dir)
            elif cmd == "exit":
                break
            elif cmd == "add":
                for arg in args:
                    for track_path in resolve_paths(current_dir, arg):
                        playlist.add(track_path)
            elif cmd == "remove":
                for arg in args:
                    for track_path in resolve_paths(current_dir, arg):
                        playlist.remove(track_path)
            elif cmd == "list":
                playlist.list()
            elif cmd == "save":
                if args: 
                    output = current_dir /args[0]
                    if not output.suffix:
                        output = output.with_suffix('.m3u')
                    playlist.save(output_path=output)
                else:
                    print("Something went wrong, try to use save <playlist_name>")
            else:
                print("Unknown command")    
        except Exception as e:
            print('Exception: ', str(e))
        except KeyboardInterrupt:
            print('\nExiting')
            break
        
        
if __name__ == "__main__":
    repl()