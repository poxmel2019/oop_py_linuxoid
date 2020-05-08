"""Packages and modules"""
from for_oop8 import data_collect
def f():

    
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

    special_tuple = data_collect()
    

    #r1.addWD(1,1)
    #r1.addWD(1,1)
    #r1.addWD(1,2)
    r1 = Room(special_tuple[0],special_tuple[1],special_tuple[2])
    r1.surface_square()
    r1.measure_rool_wallpaper(special_tuple[3],special_tuple[4])
    print("You are going to wallpapering next square: "+str(r1.square))
    print("You need %s quantity rolls of wall paper" % str(r1.rulon))


    
    

