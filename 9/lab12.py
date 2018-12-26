
import math

class Vector(object): 
    ''' ''' 
    
    def __init__(self, x=0, y=0):
        ''' '''
        self.x = float(x) 
        self.y = float(y) 
        
    def __str__(self): 
        ''' '''
        return '({:.2f},{:.2f})'.format(self.x,self.y)
        
    def __repr__(self): 
        ''' ''' 
        return self.__str__()
        
    def __add__(self, vector) :
        ''' ''' 
        return Vector(self.x + vector.x, self.y + vector.y) 
    
    def __sub__(self, vector) :
        ''' ''' 
        return Vector(self.x - vector.x, self.y - vector.y) 
    
    def __mul__(self, value): 
        ''' ''' 
        if type(value) in (float, int): 
            return Vector(self.x*value, self.y*value) 
        elif type(value) == Vector: 
            return (self.x*value.x, self.y*value.y)

    def __rmul__(self): 
        ''' ''' 
        return self.__mul__() 
    
    def __eq__(self, value): 
        ''' ''' 
        if self.x == value.x and self.y == value.y:
            return True
        
        else:
            return False
        
    def magnitude(self): 
        ''' ''' 
        return math.sqrt(self.x**2 + self.y**2) 
    
    def unit(self): 
        ''' ''' 
        try: 
            self.x = (self.x) / self.magnitude()
            self.y = (self.y) / self.magnitude()
        except ValueError:
            print ("Cannot convert zero vector to a unit vector.") 
            
def main(): 
    ''' ''' 
    
    v1 = Vector(5,6) 
    v2 = Vector(5,6) 
    
    v3 = v1 + v2 
    v4 = v1 - v2 
    v5 = v1 * v2 
    v6 = v1*3
    print("V6:", v6)
    print(v3)
    print(v4) 
    print(v5)
    print(v1 == v2) 
    print(v1.magnitude()) 
    v1.unit()
    print(v1)
    print(v1.magnitude())

    
if __name__ == "__main__": 
    main()