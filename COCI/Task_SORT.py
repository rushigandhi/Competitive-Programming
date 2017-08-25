inputList = [int(e) for e in input().split()]
N = inputList[0]
C = inputList[1]
numList = list()
freqList = list()
message = [int(e) for e in input().split()]
for i in range(N):
    if message[i] in numList:
        iVal = numList.index(message[i])
        freqList[iVal] += 1
    else:
        numList.append(message[i])
        freqList.append(1)


print(numList, freqList)

'''
9 77
11 33 11 77 54 11 25 25 33'''