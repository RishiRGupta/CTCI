# #1.1
x=input()
temp={}
if len(x) == 1:
    print("Unique")
for i in range(len(x)):
    if x[i] not in temp:
        temp[x[i]]=1
    else:
        temp[x[i]]+=1
print(temp)
if any(value >=2 for value in temp.values()):
    print("Not Unique")
else:
    print("Unique")
#1.1 Without using any additional Memory, But will increase the time complexity to O(n^2)
