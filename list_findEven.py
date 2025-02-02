master = list(map(int, input("Enter list of numbers :").split()))

new_list = [num for num in master if num%2==0]

print(sorted(new_list))