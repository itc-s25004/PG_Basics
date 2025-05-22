a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionFrom:
    print("b cannot be zero.")
