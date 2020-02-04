def contador(param):
    words = param.split()
    wordsCount = {}
    
    for x in words:
        if x in wordsCount:
            wordsCount[x] =  wordsCount[x] + 1
        else:
            wordsCount[x] = 1
    print(wordsCount)

    
print(contador(str(input("Digite algo:"))));