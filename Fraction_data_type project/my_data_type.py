class Fraction:
    def __init__(self,n,d):
        self.n=n
        self.d=d

    def __str__(self):
            return self.simplify(self.n, self.d)

    def simplify(self,n,d):
        a=min(n,d)
        for i in range(a,1,-1):
            if(n%i==0) and (d%i==0):
                n=int(n/i)
                d=int(d/i)
                return "{}/{}".format(n,d)



    def __add__(self,other):
        temp_n=self.n*other.d+other.n*self.d
        temp_d=self.d*other.d
        return self.simplify(temp_n,temp_d)
        #return "{}/{}".format(temp_n,temp_d)

    def __sub__(self,other):
        temp_n=self.n*other.d-other.n*self.d
        temp_d=self.d*other.d
        return self.simplify(temp_n,temp_d)
        #return "{}/{}".format(temp_n,temp_d)

    def __mul__(self, other):
        temp_n = self.n * other.n
        temp_d = self.d * other.d
        return self.simplify(temp_n,temp_d)
        #return "{}/{}".format(temp_n, temp_d)

    def __truediv__(self, other):
        temp_n=self.n*other.d
        temp_d=self.d*other.n
        return self.simplify(temp_n,temp_d)
        #return "{}/{}".format(temp_n,temp_d)


class Logarithm:

    def __init__(self,):

a=Fraction(4,5)
b=Fraction(2,2)
print(a+b)
