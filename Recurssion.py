def suma(*args):
    string = ""
    for arg in args:
        string += arg
    return string

print(suma(input()))

'''side1 = int(input("side 1: "))
side2 = int(input("side 2: "))
side3 = int(input("side 3: "))
side4 = int(input("side 4: "))
if (side1 == side3 and side2 == side4) or (side1 == side4 and side2 == side3) or (side1 == side2 and side3 == side4):
    print("possible")
else:
    print("not possible")'''




'''num = int(input())
digit1 = num % 10
digit2 = num // 10
if digit1 + digit2 < 10:
    print(num)
else:
    print("invalid")'''



'''
ch = input().lower()
vowels = list("aeiou")
if ch in vowels:
    print("vowel")
else:
    print("not a vowel")'''





'''def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))
    
n = int(input("n: "))
for x in range (1,n+1):
    print(fib(x), end=" ")'''
    
