from pathlib import Path
import file_browser
import playlist

current_dir = Path.cwd()


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
    
    while True:
        try:
            cmd_line = input(f"[{current_dir} > ").strip()
            
            if not cmd_line:
                continue
            # Handle help
            if cmd_line == "?" or cmd_line == help:
                show_help()
                continue
            # Handle wildcard ? to show content in directory
            if "?" in cmd_line:
                print("Files and folders in current cirectory:")
                file_browser.list_files(current_dir)
            
            cmd, *args = cmd_line.split()
            
            if cmd == "ls":
                file_browser.list_files(current_dir=current_dir)
            elif cmd == "cd":
                current_dir = file_browser.change_dir(current_dir, args[0])
            elif cmd == "pwd":
                print(current_dir)
            elif cmd == "exit":
                break
            else:
                print("Unknown command")    
        except Exception as e:
            print('Exception: ', str(e))
        except KeyboardInterrupt:
            print('\nExiting')
            break
        
        
if __name__ == "__main__":
    repl()