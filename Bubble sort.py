a=[2,7,4,6,9,1,0]
for j in range(0,len(a)):
    for i in range(0,len(a)-1):
        if(a[i]>a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
print(a)


        
