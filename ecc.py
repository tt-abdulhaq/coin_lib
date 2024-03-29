from unittest import TestCase

class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            # the num have to be on {0,1,2,...prime-1}
            raise ValueError(f'Not {num} in Field({num}, {prime-1})')
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f'FieldElement({self.num})_{self.prime}'
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self, other) -> bool:
        return not (self == other)
    
    def __add__(self, other):
        # a +f b = (a+b) % prime
        if self.prime != other.prime:
            raise ValueError(f'{self} and {other} is not in some field')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)
    
    def __neg__(self):
        # -f a = (-a) % prime
        return self.__class__((-self.num) % self.prime, self.prime)
    
    def __sub__(self, other):
        # a -f b = (a-b) % prime
        if self.prime != other.prime:
            raise ValueError(f'{self} and {other} is not in some field')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)
    
    def __mul__(self, other):
        # a .f b = (a.b) % prime
        if self.prime != other.prime:
            raise ValueError(f'{self} and {other} is not in some field')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)
    
    def __pow__(self, exponent):
        # a^exponent = (a^exponent) % prime
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other):
        # a /f b = (a.(b^p-2))%p
        if self.prime != other.prime:
            raise ValueError(f'{self} and {other} is not in some field')
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return self.__class__(num, self.prime)

class Point:

    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        if self.x is None and self.y is None:
            return   
        if self.y**2 != self.x**3 + self.a * x + self.b:
            raise ValueError(f"Value in not Point({self.x, self.y}) Curve")
        
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b
    
    def __ne__(self, other) -> bool:
        return  not (self == other)
    
    def __repr__(self) -> str:
        return f"Point({self.x, self.y})"
    
    def __add__(self, other):

        if self.a != other.a or self.b != other.b:
            raise ValueError("Value in not on some Curve")

        if self.x is None:
            return other
        if other.x is None:
            return self

        if self == other:
            if self.x == other.x and self.y != other.y:
                return self.__class__(None, None, self.a, self.b)
            else:
                print("here")
                s = ((FieldElement(3, self.x.prime) * self.x**2) + self.a) / (FieldElement(2, self.x.prime) * self.y)
                x = s**2 - (FieldElement(2, self.x.prime)*self.x)
                y = s * (self.x - x) - self.y
                return self.__class__(x, y, self.a, self.b)
            
            
        else:
            if self.y == FieldElement(0, self.x.prime) * self.x:
                return self.__class__(None, None, self.a, self.b)
            else:
                print("Here")
                s = (other.y - self.y) / (other.x - self.x)
                x = s ** 2 - self.x - other.x
                y =  s * (self.x - x) - self.y
                return self.__class__(x, y, self.a, self.b)
            
        
        



    
class ECCTest(TestCase):

    def field_element_test(self):
        prime = 13
        a = FieldElement(num=7, prime=prime)
        b = FieldElement(num=6, prime=prime)
        print(a==a)
        print(a!=b)
        with self.assertRaises(ValueError):
            print(FieldElement(num=14, prime=prime))
        a_add_b = FieldElement(0,prime=prime)
        print((a+b) == a_add_b)
        a_sub_b = FieldElement(1, prime=prime)
        print((a-b) == a_sub_b)
        neg_a = -a
        print(neg_a == b)
        a_mul_b = FieldElement(3,prime=prime)
        print((a*b) == a_mul_b)
        a_pow_3 = FieldElement(5, prime=prime)
        print((a**3) == a_pow_3)
        a_div_b = FieldElement(12, prime=prime)
        print((a/b) == a_div_b)

        