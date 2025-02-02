l1 = list(map(int,input("Enter numbers in list 1 :").split()))
l2 = list(map(int,input("Enter numbers in list 2 :").split()))

print("List 1 : ",l1)
print("List 2 : ",l2)

new_list = [num for num in l1 if num in l2]

print("Common numbers : ",new_list)