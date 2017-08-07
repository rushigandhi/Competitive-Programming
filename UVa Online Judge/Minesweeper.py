inputLine = input()
inputLine.split()
length = int(inputLine[0])
wid = int(inputLine[2])
grid = [[0 for j in range (length + 2)] for i in range (wid + 2)]
mineList = []
for x in range(length):
        tempList = list(input())
        for i in range(wid):
            if tempList[i] == '*':
                coordinates = str(i) + str(x)
                mineList.append(coordinates)
        grid[x+1] = [""]+tempList+[""]

print(grid)
for y in range(1, length + 1):
    for x in range(1, wid + 1):
        counter = 0
        if grid[y][x] == '.':
            for i in range(-1,2):
                for j in range(-1,2):
                    neighX = x + i
                    neighY = y + j
                    if grid[neighY][neighX] == "*":
                        counter+=1
            grid[y][x] = str(counter)

            '''
            for i in range(len(mineList)):
                mineCoord = int(mineList[i])
                mineX = (mineCoord//10)%10
                mineY = mineCoord%10
                deltaX = abs(mineX - x)
                deltaY = abs(mineY - y)
                # print("mine", mineList[i])
                # print("point", str(x) + str(y))
                if deltaX == 1 and deltaY == 1 or deltaX == 1 and deltaY == 0 or deltaX == 0 and deltaY == 1:
                    counter += 1
                # print("counter", counter)
            grid[y][x] = str(counter)
            # print("counter", counter)'''

for y in range(1, length + 1):
        line = ''.join(str(e) for e in grid[y][1:] )
        print(line)

'''grid = list(filter(None, grid))
print(grid)
print(mineList)'''