class Test: 
    """printing the objects"""

    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "Test a:%s b:%s" % (self.a, self.b) 
  
# Driver Code         
t = Test(1234, 5678) 
print(t) 
print(type(t.__repr__))