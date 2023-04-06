a,b = 0,1
sum = 0


n = input("Enter number: ")
print (f"{a} {b}", end=' ')
if (n.isdigit()):
    n = int(n)
    count = 2
    while (count < n):
        sum = a+b
        print(sum, end=' ')
        a,b = b, sum
        count += 1
else:
    print("Invalid Input")