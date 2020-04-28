def f():
    class Person:
        def __init__(self,name,surname,qua=1):
            self.name = name
            self.surname = surname
            self.qua = qua
        def info(self):
            print("Name: {0}\nSurname: \
{1}\nQualification: {2}".format(self.name, self.surname, self.qua))
        def __del__(self):
            print("Goodbye Mister {0} {1}".format(self.name, self.surname))

    emp1 = Person('Tom','Long')
    emp2 = Person('Bob','Hoskins',2)
    emp3 = Person('Jack','Craine',3)

    emp1.info()
    emp2.info()
    emp3.info()

    del(emp1)
    input()
        
