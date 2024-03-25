


class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime-1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return "FieldElement_{}({})".format(self.prime, self.num)
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self, other) -> bool:
        return not (self.__eq__(other=other))
    
    
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot add two number is different filed")
        num = (self.num + other.num) % self.prime
        return self.__class__(num=num, prime=self.prime)
    
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot dub two number is different filed")
        num = (self.num - other.num) % self.prime
        return self.__class__(num=num, prime=self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot dub multiply number is different filed")
        num = (self.num * other.num) % self.prime
        return self.__class__(num=num, prime=self.prime)
    
    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n,  self.prime)
        return self.__class__(num=num, prime=self.prime)
    
    def __floordiv__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot dub divide number is different filed")
        
        # use Fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        # we return an element of the same class      
        num = self.num * pow(other.num, self.prime - 2 , self.prime)
        return self.__class__(num = num, prime = self.prime)
        

    
