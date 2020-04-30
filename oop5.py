def f0():
    class B:
        count = 0
        def __init__(self):
            B.count += 1
        def __del__(self):
            B.count -= 1

    a = B()
    b = B()
    print(B.count)
    del(a)
    B.count -= 1
    print(B.count)

def f1():

    class B:
        __count = 0
        def __init__(self):
            B.__count += 1
        def __del__(self):
            B.__count -= 1
    a = B()

    #print(B.__count)
    print(B._B__count)

def f2():

    class B:
        __count = 0
        def __init__(self):
            B.__count += 1
        def __del__(self):
            B.__count -= 1
        def qtyObject():
            return B.__count

    a = B()
    b = B()
    print(B.qtyObject())

def f3():
    class DoLi:
        def __init__(self,l):
            self.double = DoLi.__makeDouble(l)
        def __makeDouble(old):
            new = []
            for i in old:
                new.append(i)
                new.append(i)
            return new
    nums = DoLi([1, 3, 4, 6, 12])
    print(nums.__makeDouble)
    print(DoLi.__makeDouble([1,2]))

def f4():
    class A:
        def __init__(self,v):
            self.field1 = v
    a = A(10)
    a.field2 = 20
    print(a.field1)
    print(a.field2)

def f5():
    class A:
        def __init__(self,v):
            self.field1 = v
        def __setattr__(self,attr,value):
            if attr == 'field1':
                self.__dict__[attr] = value
            else:
                raise AttributeError
    a = A(15)
    print(a.field1)

    a.field2 = 30

def f6():
    class Book:
        title = None
        author = None

        def __init__(self,title,author):
            self.title = title
            self.author = author

    b1 = Book('Three deaths of Ben Baxter','Robert Shekli')
    print(b1.title,b1.author)
def f7():
    class Book:
        __title = None
        __author = None

        def getTitle():
            return Book.__title
        def setTitle(self,title):
            Book.__title = title
        
        
    b1 = Book()
    b1.title = '23'
    #print(b1.title)
    #b1.setTitle('12')
    print(Book.getTitle())
def f8():
    class Book:
        title = None
        __author = None
        def getAuthor():
            return Book.__author
        def setAuthor(self,author):
            Book.__author = author
        
    n = Book()
    print(n.title)
    n.title = 'The cold heart'
    print(n.title)
    #n._Book__author = 'Gauf'
    n.setAuthor('Gauf')
    print(Book.getAuthor())
    #print(n.__author)
    #print(n._Book__author)
    
    
    #print(b1.author)
    
    
