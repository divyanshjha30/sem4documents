num1 = 0
lst1 = []
print("Enter elements one by one for list 1(-999 to exit): ",end="")
while (num1!=-999):
    if(num1 == -999):
        break
    num1 = int(input())
    lst1.append(num1)
print(lst1)
lst2 = []
lst3 = []
print("Enter elements one by one for list 2(-999 to exit): ",end="")
num1 = 0
while (num1!=-999):
    if(num1 == -999):
        break
    num1 = int(input())
    lst2.append(num1)
print(lst2)
lst3.append(lst1)
lst3.append(lst2)
print("lst3: ",lst3)
print(len(lst3))