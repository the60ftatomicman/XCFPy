## https://developer.gimp.org/core/standards/xcf/#xcf-file
## https://github.com/FHPythonUtils/GimpFormats
## THE ISSUE YOU ARE HAVING... you need to modify your props list based soley on the things that it shows
# ---------- Imports
# ----- Internal Libs
from os import path
from src.xcf import xcf

# ---------- Main
if __name__ == '__main__':
    dirRoot     = path.dirname(path.realpath(__file__))
    xcfFilePath = dirRoot+"/demo.xcf"
    with open(xcfFilePath, "rb", buffering=0) as f:
        xcfData = xcf(f)