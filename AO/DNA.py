f = open("demofile.txt", "r")

numPairs = int(f.readline())


for i in numPairs:
    strand1 = str(f.readline()).upper()
    strand2 = str(f.readline()).upper()
    tempStrand = ''
    maxStrand = ['']

    for j in strand1.length:
        for k in strand2.length:
            if(strand1[j] == strand2[k]):
                tempStrand += strand2[k]
            else:
                break

        maxStrand[maxStrand.length - 1] += strand1[j]
