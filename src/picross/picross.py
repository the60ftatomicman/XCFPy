import json
import math
from copy import deepcopy
class picross:

    def __init__(self,name, puzzlePixelData, winPixelData,dimensions):
        self.json = {
            "name"   : name,
            "size"   : dimensions[0],
            "divider": 2,
            "hints"  : {
                "vertical"  : [[]]*dimensions[0],
                "horizontal": [[]]*dimensions[0]
            },
            "view" :{
                "baseSize" : 50,
                "final":""
            }
        }
        #https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
        self.puzzleData = [puzzlePixelData[i:i + dimensions[0]] for i in range(0, len(puzzlePixelData), dimensions[0])]
        self.parsePuzzleData()

        self.winData = []
        if winPixelData != []:
            self.winData = [winPixelData[i:i + dimensions[0]] for i in range(0, len(winPixelData), dimensions[0])]

    # See _getBoardState from the JS editor
    def parsePuzzleData(self):
        fullSize = self.json["size"]

        for i in range(fullSize):
            self.json["hints"]["vertical"][i]   = []
            self.json["hints"]["horizontal"][i] = []

            totalCol=0
            totalRow=0
            
            for j in range(fullSize):
                cellCol = self.puzzleData[j][i] # going across
                cellRow = self.puzzleData[i][j] # going down

                if j < fullSize-1:
                    #----- Columns
                    if cellCol[3] == 255:
                        totalCol +=1
                    elif totalCol > 0:
                        self.json["hints"]["vertical"][i].append(totalCol)
                        totalCol = 0
                    #----- Rows
                    if cellRow[3] == 255:
                        totalRow +=1
                    elif totalRow > 0:
                        self.json["hints"]["horizontal"][i].append(totalRow)
                        totalRow = 0
                else:
                    #----- Columns
                    if cellCol[3] == 255:
                        totalCol +=1
                        
                    if (totalCol > 0):
                        self.json["hints"]["vertical"][i].append(totalCol)
                    elif len(self.json["hints"]["vertical"][i]) == 0:
                        self.json["hints"]["vertical"][i] = [0]
                    totalCol = 0
                    #----- Rows
                    if cellRow[3] == 255:
                        totalRow +=1
                        
                    if (totalRow > 0):
                        self.json["hints"]["horizontal"][i].append(totalRow)
                    elif len(self.json["hints"]["horizontal"][i]) == 0:
                        self.json["hints"]["horizontal"][i] = [0]
                    totalRow = 0


    def get_blob(self):
        return json.dumps(self.json)
       