import sys, json

def main():
    print("Generator for Strings for Final Doom")
    print("Proceeding will overwrite any file named 'DEHACKED.txt' currently in this folder")
    
    selection = input('''    
    To edit a TNT file, press (T)
    To edit a Plutonia file, press (P)
    To exit the program, press (Q)
    >''').upper()

    
    if selection == "Q":
        sys.exit(0)
    elif selection == "P":
        gen_final_doom('plstrings.json')
    elif selection == "T":
        gen_final_doom('tntstrings.json')
    else:
        print("Invalid Input")


    sys.exit(0)

def gen_final_doom(wad_json):
    strings = {}
    with open(wad_json, 'r', encoding='utf-8') as file_obj:
        strings = json.load(file_obj)
    
    inputStrs = {}
    with open('input.json', 'r', encoding='utf-8') as file_obj:
        inputStrs = json.load(file_obj)

    dehFile = open('DEHACKED.txt', 'w')

    dehFile.write("Patch File for DeHackEd v3.0\n\n# Note: Use the pound sign ('#') to start comment lines.\n\nDoom version = 19\nPatch format = 6\n\n")

    for i in range(0, len(inputStrs)):
        newname = inputStrs[i]["data"]
        if (len(newname) > len(strings[i]["data"])):
            print(f"String: {newname} is longer than replaced string, this may cause errors in vanilla.")
        dehFile.write("Text "+str(len(strings[i]["data"]))+" "+str(len(newname))+"\n"+strings[i]["data"]+newname+"\n\n")
        
    print("DONE!")
    dehFile.close()


if __name__ == "__main__":
    main()