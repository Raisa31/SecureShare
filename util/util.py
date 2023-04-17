def stringToInteger(messageString):
    integerValue = ''.join(map(str,[ord(char) for char in messageString.lower()]))
    return int(integerValue)
    
def integerToString(messageInteger):
    st = 0
    messageIntegerStr = str(messageInteger)
    stringArray = []
    while st < len(messageIntegerStr):
        num = messageIntegerStr[st] + messageIntegerStr[st+1]
        if int(num) >=97 and int(num) <= 122:
            st += 2
        else:
            num += messageIntegerStr[st + 2]
            st += 3
        stringArray.append(chr(int(num)))
    return ''.join(stringArray)
