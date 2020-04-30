def f0():
    class A:
        def __init__(self, v1, v2):
            self.field1 = v1
            self.field2 = v2
        def __str__(self):
            return str(self.field1) + " " + str(self.field2)
        
    a = A(3,4)
    print(a)
    
def f1():

    class T1:
        n = 10
        def total(self, N):
            self.total = int(self.n) + int(N)

    class T2:
        def total(self, s):
            self.total = len(str(s))

    t1 = T1()
    t2 = T2()
    t1.total(45)
    t2.total(45)
    
    print(t1.total)
    print(t2.total)

def f2():

    class Rectangle:
        def __init__(self, width, height, sign):
            self.w = int(width)
            self.h = int(height)
            self.s = str(sign)
        def __str__(self):
            rect = []
            for i in range(self.h):
                rect.append(self.s * self.w)
            rect = '\n'.join(rect)
            return rect

    b = Rectangle(10,3,'*')
    print(b)

def f():

    class Person:
        def __init__(self,a):
            self.a = int(a)
            #self.b = int(b)
        
        def __add__(self,b):
           return float(self.a+b)

    per1 = Person(10)
    per2 = Person(20)
    c = per1.a+per2.a
    
    print(c)
        
            
