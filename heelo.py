a = [2,3,4,5,6,7,8]
start = 0
length = len(a)
end = length-1
key = 4
while(start<=end):
    mid = int(start + (start-end)/2)#mid =  
    if a[mid]==key:
        print(mid)
        break
#         #break
    elif key>a[mid]:
              start = mid+1
    else:
              end = mid-1