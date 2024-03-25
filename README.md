# Finite Field Operations in Python

This repository contains a Python implementation of finite field arithmetic operations using the `FieldElement` class. The `FieldElement` class allows performing arithmetic operations within a finite field.

## Finite Field Definition

Mathematically, a finite field is defined as a finite set of numbers satisfying the following properties:

- **Closure**: If a and b are in the set, a + b, a × b, a - b, and a / b are in the set.
- **Additive Identity**: 0 exists, and a + 0 = a.
- **Multiplicative Identity**: 1 exists, and a × 1 = a.
- **Additive Inverse**: For every a in the set, -a is also in the set, such that a + (-a) = 0.
- **Multiplicative Inverse**: For every a in the set (except 0), a^-1 is also in the set, such that a × a^-1 = 1.

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
- **Exponentiation**: a^x = (a^x) % p

### Division

Division in finite fields is defined using the multiplicative inverse:

- **Division**: a / b = a × b^-1 = a × b^(p-2)

## Example Usage

You can use the `FieldElement` class to perform arithmetic operations within a finite field. Here's how you can use it:

```python
# Import the FieldElement class
from field_element import FieldElement

# Define prime and elements
p = 31
a = FieldElement(2, p)
b = FieldElement(3, p)
c = FieldElement(24, p)

# Perform arithmetic operations
result1 = a * b / c
result2 = FieldElement(17, p) ** -3
result3 = c ** -4 * 11

# Print the results
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
