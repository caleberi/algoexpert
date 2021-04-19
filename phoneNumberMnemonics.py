def phoneNumberMnemonics(phoneNumber):
    if phoneNumber=="1" or phoneNumber=="0":
        return [phoneNumber]
    currentMnemonics = ["0"]*len(phoneNumber)
    phoneNumberDialPadLayout = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    mnemonicsFound=[]

    phoneNumberMnemonicsHelper(0,phoneNumber,phoneNumberDialPadLayout,currentMnemonics,mnemonicsFound)
    return mnemonicsFound

def phoneNumberMnemonicsHelper(idx,phoneNumber,dialPadLayout,currentMnemonics,mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonics=''.join(currentMnemonics)
        mnemonicsFound.append(mnemonics)
    else:
        digit=phoneNumber[idx] # 1,9,0,5
        letters=dialPadLayout[digit] 
        for letter in letters:
            currentMnemonics[idx]=letter
            phoneNumberMnemonicsHelper(idx+1,phoneNumber, dialPadLayout,currentMnemonics,mnemonicsFound) #[]
            print(f"phoneNumberMnemonicsHelper({idx+1},{phoneNumber},dialPadLayout,{currentMnemonics},{mnemonicsFound})")



print(phoneNumberMnemonics('1905'))


