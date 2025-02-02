master = list(map(int, input("Enter list of numbers :").split()))
print("Master List : ", master)
number = int(input("Enter the number :"))

new_list = [num for num in master if num<number]
print("New List :",new_list)