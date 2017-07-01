with open('dataset_3363_2.txt') as inf:
    s = inf.readline()

out = ''
numStartIndex = 0
numEndIndex = 0
curCharindex = 0
for i in range(len(s) - 1):
    if s[i+1].isdigit():
        if numStartIndex == 0:
            numStartIndex = i+1
        #print('numStartIndex: ' + str(numStartIndex))
        
    if i == len(s) - 2:
        numEndIndex = len(s)
        #print('numEndIndex: ' + str(numEndIndex))
        out += s[curCharindex] * int(s[numStartIndex:numEndIndex])
    elif s[i+1].isdigit() == False:
        numEndIndex = i+1
        #print('numEndIndex: ' + str(numEndIndex))
        out += s[curCharindex] * int(s[numStartIndex:numEndIndex])
        curCharindex = i+1
        #print('curCharindex: ' + str(curCharindex))
        numStartIndex = 0
print(out)