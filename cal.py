a = [4,2,521,12,1,3]
#a.sort()
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        
        if(a[j]<a[i]):
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            
print(a)

arr = [3,4,4,55]
for i in range(0,len(arr)):
    print(arr[i])
        