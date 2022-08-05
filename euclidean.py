a=[[0 for l in range(6)] for m in range(6)]
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]=max(abs(j-0),abs(i-2))
        #print(a[i][j])
print(a)
