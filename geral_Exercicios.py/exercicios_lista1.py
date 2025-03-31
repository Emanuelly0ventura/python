a = 11
b = 3

print(f"a: {a+b*a}")
print(f"b: {b*a+b}")
print(f"c: {a//b}")
print(f"d: {b%a}")
print(f"e: {a%b}")
print(f"f: {b//a}")
print(f"g: {b-a/b}")
print(f"h: {10+a%b}")
print(f"i: {10-b//a}")


x = True
y = False

print(f"a: {x and y}")
print(f"b: {x or y}")
print(f"c: {x and y or x}")
print(f"d: {x or y or x}")
print(f"e: {not(x or not y)}")
print(f"f: {not(not x and not y)}")

#lista 1

a = 5
b = 9
x = not True
y = False and True
m = "casa"
n = "mesa"

print(x and y == x or y)
print(a * b<= b - a)
print(not(a == b or not b != a))
print(not(m != n and b > a))
print(b + a <= a * b and y)
print(x and not y or a // b != a % b)

