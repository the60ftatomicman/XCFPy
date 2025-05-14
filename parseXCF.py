## https://developer.gimp.org/core/standards/xcf/#xcf-file
## https://github.com/FHPythonUtils/GimpFormats
## THE ISSUE YOU ARE HAVING... you need to modify your props list based soley on the things that it shows
# ---------- Imports
# ----- Internal Libs
from os import path
from src.xcf import xcf
from src.picross.picross import picross

# ---------- Main
if __name__ == '__main__':
    dirRoot     = path.dirname(path.realpath(__file__))
    xcfFilePath = dirRoot+"/demo.xcf"
    xcfData = None
    with open(xcfFilePath, "rb", buffering=0) as f:
        xcfData = xcf(f)
    # Now to do some stuff for Picross
    # TODO -- we only handle puzzles less than 64 pixels atm.
    # TODO -- id like to get the library to be more generalized but curretly
    # TODO -- I am letting perfect be the enemy of working

    #print(xcfData.get_pixels("Puzzle"))
    #print("----")
    #print(xcfData.get_pixels("Color"))
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