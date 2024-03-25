# Import the FieldElement class
from field_element import FieldElement

# Define prime and elements
p = 13
a = FieldElement(7, p)
b = FieldElement(12, p)
c = FieldElement(6, p)

print(a+b==c)
print(f'a + b = {a+b}')
print(f'c - b = {c-b}')


print(a*b==c)
print(f'a . c = {a*c}')
print(f'b . a = {b * a}')

t = FieldElement(7, 31)

print(t**(-3))

p = 19

a = FieldElement(2, p)

b = FieldElement(7, p)

c = FieldElement(5, p)

print(a/b)
print(b/c)

