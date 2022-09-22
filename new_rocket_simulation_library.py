import datetime
import numpy as np
import json

class Coord(object):
    def __init__(self, x=0, y=0, z=0):
        self.x=x
        self.y=y
        self.z=z
    
    def move(self, *args):
        self.change_x=args[0]-self.x
        if len(args)==2:
            self.change_y=args[1]-self.y
        if len(args)>2:
            self.change_y=args[1]-self.y
            self.change_z=args[2]-self.z
        return self
        
class Particle:
    def __init__(self, *args, dim=1, acc=0, vel=0, save=False):
        self.dim=dim
        self.point_=Coord().move(*args[:self.dim])#has 3 properties x, y, and z
        self.position=np.array([self.point_.change_x], dtype=np.float64)
        if self.dim==2:
            self.position=np.array([self.point_.change_x, self.point_.change_y], dtype=np.float64)
        elif self.dim==3:
            self.position=np.array([self.point_.change_x, self.point_.change_y, self.point_.change_z], dtype=np.float64)
        self.acc=acc
        self.vel=vel
        self.save=save
        self.start_time=datetime.datetime.now()#start time initialization
        
    def generate_alt(self):
        
        x_=np.array([Coord().move(0, 0, 0).change_x], dtype=np.float64)
        x_coord=np.around(x_, decimals=4)#making the precision of x to be of 4 decimal places.
        ini_=x_coord
        
        if self.dim == 2:
            y_=np.array([Coord().move(0, 0, 0).change_y], dtype=np.float64)
            y_coord=np.around(y_, decimals=4)#making the precision of y to be 4 decimal places
            ini_=np.array([x_coord[0], y_coord[0]], dtype=np.float64)
            
        elif self.dim == 3:
            y_=np.array([Coord().move(0, 0, 0).change_y], dtype=np.float64)
            y_coord=np.around(y_, decimals=4)#making the precision of y to be 4 decimal places
            
            
            z_=np.array([Coord().move(0, 0, 0).change_z], dtype=np.float64)
            z_coord=np.around(z_, decimals=4)
            ini_=np.array([x_coord[0], y_coord[0], z_coord[0]], dtype=np.float64)
            
        fin_=self.position
        print("Upward trajectory")
        while np.all(ini_<= fin_):
            self.time_=datetime.datetime.now()#fetch time in real time
            ini_ += 0.0001
            #coordinates=tuple(ini_)
            s1=json.dumps({f"{self.time_}":f"{ini_}"})
            if self.save == True:
                #channel the output to database
                pass
            #redirect the output to the graphing engine
            print(s1)
            
        print("Downward trajectory")  
        while np.all(ini_>=0):
            self.time_=datetime.datetime.now()
            ini_ -= 0.0001
            #coordinates=tuple(ini_)
            s2=json.dumps({f"{self.time_}":f"{ini_}"})
            if self.save == True:
                #channel the output to the database
                pass
            #redirect the output to the graphing engine
            print(s2)
            
            
        print(f"The duration of flight is: {self.duration()}")
    
    def duration(self):
        return self.time_ - self.start_time
    
    def acceleration(self):
        pass
    
    def speed(self):
        pass


if __name__=="__main__" :
    part=Particle(3, 3, 3, dim=3, acc=0, vel=0)
    part.generate_alt()
    
    #syst=Coord(3, 3, 3)
    #syst.move(5, 8, 10)
    #print(syst.change_x, syst.change_y, syst.change_z)
