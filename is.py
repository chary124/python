a = [1,0,2,0]
 #in#dex = 0;
nzero = 0;
for i in range(0,len(a)):
    if(a[i]!=0):
        temp = a[i]
        a[i] = a[nzero]
        a[nzero] = temp;
        nzero += 1
        
for i in range(0,len(a)):
    print(a[i])
       


st = "  chary"
st = st.spilt()
print(st)