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
        n = exponent
        while n < 0:
            # if exponent was negative we have a^exponent = (a^(prime-(exponent+1)))%prime
            n += self.prime - 1
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other):
        # a /f b = (a.(b^p-2))%p
        if self.prime != other.prime:
            raise ValueError(f'{self} and {other} is not in some field')
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return self.__class__(num, self.prime)



    
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

        