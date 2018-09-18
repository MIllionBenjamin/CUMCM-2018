genesequence = ['0']
genesequence2 = [-1]

for p in range(1, 254 +1):
    s = bin(p)
    s2 = s[2:]
    s3 = ''
    while (len(s3) + len(s2) < 8):
        s3 += '0'
    s3 += s2
    genesequence.append(s3)

for q in range(1, 254 + 1):
    for r in range(0, 8):
        genesequence2.append(int(genesequence[q][r]))
    print(genesequence2)
    genesequence2 = [-1]
