def isValidIpAddressNumber(string: str) -> bool:
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt))


def generateValidIpAddressSequence(string: str) -> list:
    ipAddressesFound = []
    for i in range(1, min(len(string), 4)):
        currentIpAddressParts = ['', '', '', '']
        currentIpAddressParts[0] = string[:i]
        if not isValidIpAddressNumber(currentIpAddressParts[0]):
            continue
        for j in range(i+1, i+min(len(string)-i, 4)):
            currentIpAddressParts[1] = string[i:j]
            if not isValidIpAddressNumber(currentIpAddressParts[1]):
                continue
            for k in range(j+1, j+min(len(string)-j, 4)):
                currentIpAddressParts[2] = string[j:k]
                currentIpAddressParts[3] = string[k:]
                if isValidIpAddressNumber(currentIpAddressParts[2]) and isValidIpAddressNumber(currentIpAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIpAddressParts))
    return ipAddressesFound




def validIPAddresses(string):
    return generateValidIpAddressSequence(string)

print(validIPAddresses("1921680"))