s = "python"
for i in s:
    print((i),end=' ')

print("\n")
g = 5
#str(input)
n = 1
for i in range(1,g+1):
    n = n * i
    
print(n)

n = str(input("enter the string"))
m = ' '
st = " "
count = 0
for i in n:
    st = i + st
    count = count + 1
    
print(st)
print(count)



sum = 0
li = [2,3,4,5,7,9,19]
for i in li:
    sum = sum + i
    
print(sum)
k = max(li)
print(k)
print(li[len(li)]-	)
