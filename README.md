# cli_mp3_tool
Create `.m3u` playlists using a Linux-like terminal interface.

## Idea
The goal is to easily build music playslist without relying on the Windows media player, using intuitive terminal-style commands. 
The aim of this tool is to especifically prepare files for hardware players like the **Fii0 X1** or **USB drives for car stereos**.

## Pattern Matching and Navigation
This tool supports file matching to help you quickly build playsits:
- Use wildcars like `*.mp3`, `string*`, `track1.mp3` to add or remove multiple files.
- Example:
    - `add track_*` -> Adds all files starging with `track_`.
    - `remove *.wag`-> Removes all files finishing with `.wag`.

### Basic Commands
 Command |  Description |
|-----|------|
| `ls`   | List files and folders in the current directory |  
| `cd <dir>` | Change current directory  |   
| `add <file or *.mp3>` | Add file(s) to the playlist |
| `add .` | Adds all supported audio files from the current directory |
| `remove <file or *.mp3>` | Remove file(s) from the playlist |
| `search <string>` | Search for filenames in the current cirectory containing the given string |
| `pwd` | Show current working directory |
| `TAB` key | Auto-complete paths like a real shell (`cd >tab>`) |
| `list` | Show all files in the playlist |
| `save <name.m3u>` | Save the playlist to `. m3u` file |   
| `exit` | Exit the app |


## Additional Features (planned or in progress)
I want to be able to run this playsit in my car, so I beleive the cassetes dont run m3u files. 
But I will use my hifi mp3 reproductor (Fiio X1) thorough the jack 3.5 connection.  
 Command |  Description |
|-----|------|
| `export <target_folder>` | Copies all files in the current playlist to a target folder in order. Adds numbering (`01_`,`02_`, etc) to perserve playback order. Ideal for copying to a USB or SD card. |  
| `clear` | Clears the current playlist in memory.  |   
| `load <name.m3u>` | Loads an existing .m3u playlist for editing or exporting. |
| `help` or `?` | List all available commands and their descriptions. |
| `info` | Shows the number of files, total size, total duration or other metadata if possible |   

## Notes
- Playlists are saved using **relative paths** to support portable devices like the Fii0 X1.
- Exported files are copied in playlist order, with optional renaming dor consistent playback.
- You can copy the exported folder directly to a USB stick or SD card for use in a car stereo or MP3 player.


