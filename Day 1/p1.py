
def checkWordsBackward(line, i, dict):
    sub1 = line[i-2:i+1] if i-2 >= 0 else ""
    sub2 = line[i-3:i+1] if i-3 >= 0 else ""
    sub3 = line[i-4:i+1] if i-4 >= 0 else ""
    if (sub1 in dict.keys()):
        return dict[sub1]
    elif (sub2 in dict.keys()):
        return dict[sub2]
    elif (sub3 in dict.keys()):
        return dict[sub3]
    return None

def checkWordsForward(line, i, dict):
    sub1 = line[i:i+3] if i + 3 <= len(line) else ""
    sub2 = line[i:i+4] if i + 4 <= len(line) else ""
    sub3 = line[i:i+5] if i + 5 <= len(line) else ""
    if (sub1 in dict.keys()):
        return dict[sub1]
    elif (sub2 in dict.keys()):
        return dict[sub2]
    elif (sub3 in dict.keys()):
        return dict[sub3]
    return None

# parse input
def parseLine(line, dict):
    i = 0
    ans = 0
    while (i < len(line)):
        val = ord(line[i])
        if (val >= ord('0') and val <= ord('9')):
            ans += (val - ord('0')) * 10
            break
        val = checkWordsForward(line, i, dict)
        if (val != None):
            ans += val * 10
            break
        i += 1
    i = len(line)-1
    while (i >= 0):
        val = ord(line[i])
        if (val >= ord('0') and val <= ord('9')):
            ans += (val - ord('0'))
            break
        val = checkWordsBackward(line, i, dict)
        if (val != None):
            ans += val
            break
        i -= 1
    return ans

if __name__ == "__main__":
    dict = {"one":1, "two":2, "three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    f = open("p1.txt", "r")
    ans = 0
    for line in f:
        ans += parseLine(line, dict)
    print(ans)
