
def parseLine(line):
    card = line.split(":")[1]
    nums = card.split("|")
    winners = nums[0].strip().split(" ")
    numbers = nums[1].strip().split(" ")
    ans = 0
    for n in numbers:
        if (n != '' and n in winners):
            ans = 2*ans if ans >= 1 else 1
    
    return ans

def parseLine2(line):
    card = line.split(":")[1]
    nums = card.split("|")
    winners = nums[0].strip().split(" ")
    numbers = nums[1].strip().split(" ")
    count = 0
    for n in numbers:
        if (n != '' and n in winners):
            count += 1
    return count

if __name__ == "__main__":
    f = open("p4.txt", "r")
    ans = 0
    NUM_LINES = 204 # hard-coded by input
    countList = [1 for _ in range(NUM_LINES)]
    i = 0
    for line in f:
        res = parseLine2(line.rstrip())
        cardCount = countList[i]
        for j in range(1,res+1):
            countList[i+j] += cardCount
        ans += cardCount
        i += 1
    print(ans)