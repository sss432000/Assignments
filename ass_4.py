
class Shape():
    def info(self):
        print("Different Shapes")
class Rectangle(Shape):
    def info(self):
        print("Adjacent sides are equal")
class Square(Shape):
    def info(self):
        print("All sides are equal")
class Triangle(Shape):
    def info(self):
        print("Base and Height")
class Circle(Shape):
    def info(self):
        print("Circle having constant radius")
class Hexagon(Shape):
    def info(self):
        print("Hexagon having six sides")
 
class cat():
    def __init__(self, c = "black", F = "black"):
        self.__legs = 4
        self.__eyecolor = c
        self.__furrcolor = F
    def setLegs(self, n):
        self.__legs = n
    def getLegs(self):
        return self.__legs
    def speak(self):
        print("meow")
    def getEyecolor(self):
        return self.__eyecolor
    def getFurrcolor(self):
        return self.__furrcolor
    def setFurrcolor(self, f):
        self.__furrcolor = f

class lion(cat):
    def speak(self):
        print("roar")

class tiger(lion, cat):
    pass

class monkey():
    def __init__(self, c = "brown"):
        self.__legs = 2
        self.__eyecolor = c
        self.__Furrcolor = "brown"
    def setLegs(self, n):
        self.__legs = n
    def getLegs(self):
        return self.__legs
    def speak(self):
        print("grunt")
    def getEyecolor(self):
        return self.__eyecolor
    def getFurrcolor(self):
        return self.__Furrcolor
    def setFurrcolor(self, F):
        self.__Furrcolor = F

class humans(monkey):
    def speak(self):
        print("talk")
    def getFurrcolor():
        return self.__Furrcolor

class horse():
    def __init__(self, c = "brown", f = "brown"):
        self.__legs = 4
        self.__eyecolor = c
        self.__Furrcolor = f
    def setLegs(self, n):
        self.__legs = n
    def getLegs(self):
        return self.__legs
    def speak(self):
        print("neigh")
    def getEyecolor(self):
        return self.__eyecolor
    def getFurrcolor(self):
        return self.__Furrcolor
    def setFurrcolor(self, f):
        self.__Furrcolor = f

class donkey(horse):
    def speak(self):
        print("bray")

class zebra(horse):
    def speak(self):
        print("bray")

class quagga(zebra, horse):
    def speak(self):
        print("kwa-ha-ha")

if __name__ == '__main__':
      
    c = cat()
    c.speak()
    l = lion()
    l.speak()
    print("legs of lion before : ",l.getLegs())
    l.setLegs(2)
    print("legs of lion after set : ", l.getLegs())
    t = tiger()
    t.speak()
    print("legs of tiger : ",t.getLegs())
    i = Shape()
    i.info()
    r = Rectangle()
    r.info()
    s = Square()
    s.info()
    tri = Triangle()
    tri.info()
    cir = Circle()
    cir.info()
    h = Hexagon()
    h.info()
    
    
