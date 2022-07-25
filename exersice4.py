# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


pathO = 'originFile.txt'
pathD = 'decreaseFile.txt'
with open(pathO, 'r') as fileO:
    originData = fileO.readline()
print(originData)

def rle(originData):
    stringOfdecrease = ''
    i = 0
    while i <= len(originData) - 1:
        count = 1
        word = originData[i]
        while i < len(originData) - 1:
            if originData[i + 1] == originData[i]:
                count+=1
                i+=1
            else:
                break
        stringOfdecrease = stringOfdecrease + str(count) + word
        i+=1
    print(stringOfdecrease)
    return stringOfdecrease

with open(pathD, 'w') as fileD:
    fileD.write(rle(originData))

#-----------------------------------------------------------------

with open(pathD, 'r') as fileD:
    decreaseData = fileD.readline()
print(decreaseData)

def unpacking(originData):
    stringUP = ''
    i = 0
    j = 1
    while i <= len(originData) - 1:
        helpString = ''
        count = int(originData[i])
        while count != 0:
            helpString+=originData[j]
            count-=1
        stringUP = stringUP + helpString
        i+=2
        j+=2
    print(stringUP)
    return stringUP

with open(pathO, 'w') as fileO:
    fileO.write(unpacking(decreaseData))


