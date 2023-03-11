def triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return "можно"
    else:
        return "нельзя"
a = int(input())
b = int(input())
c = int(input())
print (triangle(a, b, c))