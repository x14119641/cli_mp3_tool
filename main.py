from pathlib import Path
import file_browser
import playlist

current_dir = Path.cwd()

def repl():
    global current_dir
    
    while True:
        try:
            cmd_line = input(f"[{current_dir} > ").strip()
            if not cmd_line:
                continue
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