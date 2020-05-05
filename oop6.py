"""Composition"""
def f0():
    global r1
    class Win_Door:
        global self,square
        def __init__(self,x,y):
            self.square = x * y
    class Room:
        global self,square
        def __init__(self,x,y,z):
            self.square = 2 * z * (x + y)
            self.wd = []
        def addWD(self,w,h):
            self.wd.append(Win_Door(w,h))
        def workSurface(self):
            new_square = self.square
            for i in self.wd:
                new_square -= i.square
            return new_square

    r1 = Room(6, 3, 2.7)
    print(r1.square)
    r1.addWD(1,1)
    r1.addWD(1,1)
    r1.addWD(1,2)
    print(r1.workSurface())
def f():
    global r1
    class Win_Door:
        global self,square
        def __init__(self,x,y):
            self.square = x * y
    class Room:
        global self,square
        def __init__(self,x,y,z):
            self.width = x
            self.length = y
            self.height = z
            self.wd = []
             
        def addWD(self,w,h):
            self.wd.append(Win_Door(w,h))
        def surface_square(self):
            self.square = 2 * (self.width + self.length) * self.height
            return self.square
            #return (2 * (self.width + self.length) * self.height)
        def workSurface(self):
            new_square = 2 * (self.width + self.length) * self.height
            for i in self.wd:
                new_square -= i.square
            return new_square
        def measure_rool_wallpaper(self,x,y):
            self.paper_width = x
            self.paper_height = y
            self.rulon = self.square / (self.paper_width * self.paper_height)
            
    print("Hello. You are going to wallpapering. We need some data")
    width = int(input('Width: '))
    length = int(input('Length: '))
    height = int(input('Height: '))
    paper_width = int(input('Paper width: '))
    paper_length = int(input('Paper length: '))
    r1 = Room(width,length,height)
    r1.surface_square()
    
    #r1.addWD(1,1)
    #r1.addWD(1,1)
    #r1.addWD(1,2)
    r1.measure_rool_wallpaper(paper_width,paper_length)
    print("You are going to wallpapering next square: "+str(r1.square))
    print("You need %s quantity rolls of wall paper" % str(r1.rulon))
