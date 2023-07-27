# Plutonia Text Generator
A small script to generate vanilla DEHACKED files for text replacements for Final Doom: The Plutonia Experiment

While stuff like this exists for DOOM2.wad, nothing does for PLUTONIA.wad, and counting string lengths manually is a pain so I made this script to do it for me :P

Note: This DOES NOT have support for editing states, sound effects or things. It's for text strings only. You'll want to use something like DECOHACK or WhackED4 for that.

## Running the script
- You will need Python 3.9.0 installed to run this.

1. Download the python file, and two json files and put them in an empty folder.

2. Inside "input.json", edit all the fields in the "data" column to your desired text string. Currently the script supports edits to all level names and intermission screens, you can add new rows to the json file at the bottom if you would like to edit more strings, though you'll need to update "plstrings.json" at the same time with the existing plutonia string.

3. Open a terminal window, and run the command `python pldeh.py`

4. A DEHACKED.txt file will be generated which you can copy into your wad with any WAD editor, such as SLADE.
