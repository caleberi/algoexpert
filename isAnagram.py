def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        s_history ={}
        for ch in s:
            if ch in s_history:
                s_history[ch]+=1
            else:
                s_history[ch]=1
            
        t_history ={}
        for ch in t:
            if ch in t_history:
                t_history[ch]+=1
            else:
                t_history[ch]=1
        
        for item in s_history:
            if item in t_history and s_history[item]==t_history[item]:
                continue
            else:
                return False
        
        return True

def isAnagram(original, anagram, firstPtr=0, secondPtr=0):
    if len(original) != len(anagram):
        return False
    if firstPtr == len(original):
        return True
    if secondPtr == len(anagram) :
        return False  
    if original[firstPtr] == anagram[secondPtr]:
        return isAnagram(original, anagram, firstPtr+1, 0)
    else:
        return isAnagram(original, anagram, firstPtr, secondPtr+1)