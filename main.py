n = int(input("Enter a number: "))
p = 1;
while(n):
    r = n % 10
    p = p * r
    n = n // 10
print(p)