from ecc import * 

prime = 223
a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)
x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)
x2 = FieldElement(num=17, prime=prime)
y2 = FieldElement(num=56, prime=prime)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
for _ in range(100):
    p2 += p2
    print(p2)
