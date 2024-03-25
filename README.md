# Finite Field Operations in Python

This repository contains a Python implementation of finite field arithmetic operations using the `FieldElement` class. The `FieldElement` class allows performing arithmetic operations within a finite field.

## Finite Field Definition

Mathematically, a finite field is defined as a finite set of numbers satisfying the following properties:

- **Closure**: If a and b are in the set, a + b, a × b, a - b, and a / b are in the set.
- **Additive Identity**: 0 exists, and a + 0 = a.
- **Multiplicative Identity**: 1 exists, and a × 1 = a.
- **Additive Inverse**: For every a in the set, -a is also in the set, such that a + (-a) = 0.
- **Multiplicative Inverse**: For every a in the set (except 0), a<sup>-1</sup> is also in the set, such that a × a<sup>-1</sup> = 1.

## Defining Finite Sets

If the size (order) of the set is p, the elements of the set are typically denoted as 0, 1, 2, ..., p-1. In math notation, the finite field set looks like this:

Fp = {0, 1, 2, ..., p-1}

## Finite Field Arithmetic Operations

### Addition and Subtraction

- **Addition**: a + b = (a + b) % p
- **Subtraction**: a - b = (a - b) % p
- **Additive Inverse**: -a = (-a) % p

### Multiplication and Exponentiation

- **Multiplication**: a × b = (a × b) % p
- **Exponentiation**: a<sup>x</sup> = (a<sup>x</sup>) % p

### Division

Division in finite fields is defined using the multiplicative inverse:

- **Division**: a / b = a × b<sup>-1</sup> = a × b<sup>(p-2)</sup>

## Example Usage

You can use the `FieldElement` class to perform arithmetic operations within a finite field. Here's how you can use it:

```python
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


