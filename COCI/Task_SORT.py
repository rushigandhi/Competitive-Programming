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
print(numList,freqList)
for i in range(len(freqList)):
    for x in range(len(freqList) - 1):
        if freqList[x + 1] < freqList[x]:
            tempFreq = freqList[x + 1]
            tempNum = numList[x + 1]
            freqList[x + 1] = freqList[x]
            numList[x + 1] = numList[x]
            freqList[x] = tempFreq
            numList[x] = tempNum
        if message.index(numList[x + 1]) < message.index(numList[x]) and freqList[x + 1] == freqList[x]:
            tempFreq = freqList[x + 1]
            tempNum = numList[x + 1]
            freqList[x + 1] = freqList[x]
            numList[x + 1] = numList[x]
            freqList[x] = tempFreq
            numList[x] = tempNum
        print(numList, freqList)

revNum = list(reversed(numList))
revFreq = list(reversed(freqList))

for i in range(len(revNum)):
    for x in range(revFreq[i]):
        print(revNum[i])



'''
9 77
11 33 11 77 54 11 25 25 33

or freqList[x + 1] == freqList[x]'''