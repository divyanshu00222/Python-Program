#Largest of three

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)
