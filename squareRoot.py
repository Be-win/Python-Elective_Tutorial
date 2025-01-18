def square_root(n):
    x = n
    while True :
        root = 0.5 * (x+n/x)
        if abs(root - x) < 0.0001:
            break
        x = root
    return f'{root:.4f}'

num = int(input("Enter a number: "))
if num <= 0:
    print("Invalid input")
    exit(0)
print(square_root(num))



