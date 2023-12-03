
# returns 0 if not possible
# returns game id if possible
def parseLine(line, dict):
    line = line.rstrip()
    game = line.split(": ")
    id = int(game[0].split(" ")[1])
    handfuls = game[1].split("; ")
    for handful in handfuls:
        counts = handful.split(", ")
        for count in counts:
            vals = count.split(" ")
            num = int(vals[0])
            color = vals[1]
            #print(vals)
            if (dict[color] < num):
                return 0 # not possible
    return id

# get power of game
def parseLinePower(line):
    dict = {"red": 0, "green": 0, "blue": 0}
    line = line.rstrip()
    game = line.split(": ")
    #id = int(game[0].split(" ")[1])
    handfuls = game[1].split("; ")
    for handful in handfuls:
        counts = handful.split(", ")
        for count in counts:
            vals = count.split(" ")
            num = int(vals[0])
            color = vals[1]
            if (dict[color] < num):
                dict[color] = num
    return dict["red"] * dict["green"] * dict["blue"]

if __name__ == "__main__":
    dict = {"red": 12, "green": 13, "blue": 14}
    f = open("p2.txt", "r")
    ans = 0
    for line in f:
        # part 1
        # ans += parseLine(line, dict)
        # part 2
        ans += parseLinePower(line)
    print(ans)