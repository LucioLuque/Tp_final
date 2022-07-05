import unittest
from modulation import *
import numpy as np

from read_files import ReadInstrument

class Test_Case(unittest.TestCase):
    def test_modulation_CONSTANT(self):
        t=np.array([0,0.25,0.5,0.75,1,1.25,1.5,1.75,2])
        tx=[0.5]
        e=np.ones(9)
        self.assertTrue((CONSTANT(t,tx)==e).all())

    def test_modulation_LINEAR(self):
        t= np.array([0,0.25,0.5,0.75,1,1.25,1.5,1.75,2])
        tx=[0.5]
        e=np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
        self.assertTrue((LINEAR(t,tx)==e).all())
    
    def test_modulation_INVLINEAR(self):
        t= np.array([0,0.25,0.5,0.75,1,1.25,1.5,1.75,2])
        tx=[1.25]
        e=np.array([1,0.8,0.6,0.4,0.2,0,0,0,0])
        self.assertTrue((INVLINEAR(t,tx)==e).all)
    
    def test_modulation_SIN(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([1.0, 0.9955757321914929, 1.0088398712487532, 0.9867618370794549, 1.0176105293265967])
        self.assertTrue((SIN(t,tx)==e).all())
    
    def test_modulation_EXP(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([0.006737946999085469, 0.0820849986238988, 1.0, 12.182493960703471, 148.41315910257657])
        self.assertTrue((EXP(t,tx)==e).all())
        
    def test_modulation_INVEXP(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([1.0, 0.0820849986238988, 0.006737946999085469, 0.0005530843701478338, 4.5399929762484875e-05])
        self.assertTrue((INVEXP(t,tx)==e).all())
    
    def test_modulation_QUARTCOS(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([1.0, 0.7071067811865476, 6.123233995736766e-17, -0.7071067811865475, -1.0])
        self.assertTrue((QUARTCOS(t,tx)==e).all())

    def test_modulation_QUARTSIN(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([0.0, 0.7071067811865476, 1.0, 0.7071067811865476, 1.2246467991473532e-16])
        self.assertTrue((QUARTSIN(t,tx)==e).all())

    def test_modulation_HALFCOS(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([1.0, 0.5, 0.0, 0.4999999999999999, 1.0])
        self.assertTrue((HALFCOS(t,tx)==e).all())

    def test_modulation_HALFSIN(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([0.0, 0.5, 1.0, 0.5000000000000001, 0.0])
        self.assertTrue((HALFSIN(t,tx)==e).all())

    def test_modulation_LOG(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([0.0, 0.7403626894942439, 1.0, 1.1613680022349748, 1.2787536009528289])
        self.assertTrue((LOG(t,tx)==e).all())

    def test_modulation_INVLOG(self):
        t=np.array([0,0.25,0.5,0.75,1])
        tx=[0.5]
        e=np.array([1.0, 0.7403626894942439, 0, 0, 0])
        self.assertTrue((INVLOG(t,tx)==e).all())

    def test_modulation_TRI(self):
        t=np.array([0,0.01,0.02,0.03,0.04,0.05])
        tx=[0.05,0.03,1.3]
        e=np.array([0.0, 0.4333333333333334, 0.8666666666666668, 1, 1, 1])
        self.assertTrue((TRI(t,tx)==e).all())

    def test_modulation_PULSES(self):
        t=np.array([0,0.01,0.02,0.03,0.04,0.05])
        tx=[0.05,0.03,0.1]
        e=np.array([0.7000000000000002, 1, 1, 1, 1, 0.7000000000000002])
        self.assertTrue((PULSES(t,tx)==e).all())
    
    def test_read_instrument(self):
        f="piano.txt"
        e={1:1,2:0.72727272,3:0.31818181,4:0.090909}
        l=[["LINEAR",0.02],["SIN"],["INVEXP",0.06]]
        self.assertEqual(ReadInstrument(f).read(),(e,l))
    
if __name__== '__main__':
    unittest.main()