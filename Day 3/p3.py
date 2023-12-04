from collections import defaultdict

class Symbols():
    def __init__(self):
        self.symbolPos = set()
        self.gearsNums = defaultdict(lambda: [])

    def addSymbols(self, line, lineNum):
        line = line.rstrip()
        for i in range(len(line)):
            char = line[i]
            if char != '.' and (ord(char) < ord('0') or ord(char) > ord('9')):
                self.symbolPos.add((lineNum, i))

    def addPotentialGears(self, line, lineNum):
        line = line.rstrip()
        for i in range(len(line)):
            char = line[i]
            # only add gear symbols
            if char == '*':
                self.gearsNums[(lineNum, i)] = []
    
    def checkAdjacentSymbols(self, x,y):
        xVals = [x-1,x,x+1]
        yVals = [y-1,y,y+1]
        for xVal in xVals:
            for yVal in yVals:
                if ((xVal, yVal) in self.symbolPos):
                    return True
        return False
    
    def checkAdjacentGears(self, x,y):
        xVals = [x-1,x,x+1]
        yVals = [y-1,y,y+1]
        gearPos = set()
        for xVal in xVals:
            for yVal in yVals:
                if ((xVal, yVal) in self.gearsNums.keys()):
                    gearPos.add((xVal, yVal)) 
        return gearPos

    # part 1
    def parseLine(self, line, lineNum):
        curNum = None
        include = False
        ans = 0
        for i in range(len(line)):
            char = line[i]
            # if numeric
            if (ord(char) >= ord('0') and ord(char) <= ord('9')):
                curNum = curNum * 10 + int(char) if curNum else int(char)
                x = lineNum
                y = i
                if (self.checkAdjacentSymbols(x,y)):
                    include = True
            else:
                if (curNum != None):
                    if (include):
                        ans += curNum
                    curNum = None
                include = False
        if (curNum != None):
            if (include):
                ans += curNum
        return ans
    
    # part 2
    def parseGears(self, line, lineNum):
        curNum = None
        gears = set()
        for i in range(len(line)):
            char = line[i]
            # if numeric
            if (ord(char) >= ord('0') and ord(char) <= ord('9')):
                curNum = curNum * 10 + int(char) if curNum else int(char)
                x = lineNum
                y = i
                gears.update(self.checkAdjacentGears(x,y))
            else:
                if (curNum != None):
                    for gear in gears:
                        self.gearsNums[gear].append(curNum)
                    curNum = None
                    gears = set()
        if (curNum != None):
            for gear in gears:
                self.gearsNum[gear].append(curNum)

if __name__ == "__main__":
    f = open("p3.txt", "r")
    lineNum = 0
    symbols = Symbols()
    prevLine = ""
    ans = 0
    #lines = []
    for line in f:
        #lines.append(line.rstrip())
        #symbols.addSymbols(line, lineNum)
        #ans += symbols.parseLine(prevLine, lineNum-1)
        symbols.addPotentialGears(line, lineNum)
        symbols.parseGears(prevLine, lineNum-1)
        prevLine = line
        lineNum += 1
    # include last line
    #ans += symbols.parseLine(prevLine, lineNum-1)
    symbols.parseGears(prevLine, lineNum-1)
    for k,v in symbols.gearsNums.items():
        if (len(v) == 2):
            ans += v[0] * v[1]
    print(ans)
