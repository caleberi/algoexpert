def nthNaturalNumber(N):
    answer = 0
    i=0
    while N!=0:
        answer+= (10**i)*(N%9)
        N=N//9
        i+=1
    return answer

print(nthNaturalNumber(19))
    