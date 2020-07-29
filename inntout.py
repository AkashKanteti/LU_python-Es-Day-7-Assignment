#Question-3
lis=[(1,2,3),[1,2],['a','hit','less']]
lis2=[]
for i in lis:
    try:
        for j in i:
            lis2.append(j)
    except:
        lis2.append(i)
print(lis2)
