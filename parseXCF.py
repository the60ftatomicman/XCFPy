## https://developer.gimp.org/core/standards/xcf/#xcf-file
## https://github.com/FHPythonUtils/GimpFormats
## THE ISSUE YOU ARE HAVING... you need to modify your props list based soley on the things that it shows
# ---------- Imports
# ----- Internal Libs
import datetime
from os import path
from src.xcf import xcf
from src.picross.picross import picross

# ---------- Main
if __name__ == '__main__':
    dirRoot     = path.dirname(path.realpath(__file__))
    xcfFilePath = dirRoot+"/xcfs/quicktest.xcf"
    xcfData = None
    with open(xcfFilePath, "rb", buffering=0) as f:
        xcfData = xcf(f)
    # Now to do some stuff for Picross
    puzzlePixels = xcfData.get_pixels("Puzzle")
    if puzzlePixels == []:
        print("ERROR - We do not have a layer named puzzle or it could not be parsed.")
    
    puzzleDimensions = xcfData.get_dimensions("Puzzle")
    if puzzleDimensions == [-1,-1]:
        print("ERROR - We do not have a layer named puzzle or it could not be parsed.")
    
    winPixels    = xcfData.get_pixels("Color")
    if winPixels == []:
        print("WARNING - Layer [Color] not provided Therefore we will not generate a win picture.")

    puzzle = picross("test",puzzlePixels,winPixels,puzzleDimensions)
    print("---- OUTPUT ----")
    print(puzzle.get_blob())
    print("---- OUTPUT ----")

    #Write a client file so I can send it to mel
    dirRoot     = path.dirname(path.realpath(__file__))
    clientFilePath = dirRoot+"/client_apps/client.html"
    date_stamp = datetime.datetime.now().strftime("%m_%d_%Y")
    outputFilePath = dirRoot+"/output/"+date_stamp+".html"
    replaceString = "REPLACE ME"
    clientData = None
    try:
        with open(clientFilePath, "r") as f:
            clientData = f.read()
            clientData = clientData.replace(replaceString, puzzle.get_blob())
        with open(outputFilePath, "w") as f:
            f.write(clientData)
    except FileNotFoundError:
        print("Error: File not found at: %s" % (clientFilePath))
    except Exception as e:
        print("An error occurred while reading client file: %s"%(e))