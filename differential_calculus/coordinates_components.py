import datetime
from pandas import DataFrame, Series
import sympy
import numpy as np
import pickle
import struct
import itertools
import json

class Particle(object):
    
    def __init__(self, apogee):
        self.apogee=apogee
        self.start_alt=0.0
        self.start=False
        self.state=0
    
    def output(self):
        return self.alt_gen()
    
    def alt_gen(self):
        self.start_count()
        while self.start:
            if self.start_alt <= self.apogee:
                self.start_alt += 0.0001
                self.duration = str(datetime.datetime.now())
                s=json.dumps({f"time: {self.duration}":f"distance: {self.start_alt}"})
                print(s)
        
                

        
    def activation(self, data_):
        return data_
    
    def start_count(self):
        self.start=True
        
class Ship(Particle):
    pass
        
if __name__ == '__main__':
    rk=Particle(5)
    rk.alt_gen()
    print("Process complete!!")