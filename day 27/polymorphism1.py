

# """
# Polymorphism : meaning=> having many forms. 
# In programming, polymorphism means same function name (but different signatures) 
# being uses for different types.
# """


class India(): 
    def capital(self): 
        print("Cappital - New delhi") 
  
    def language(self): 
        print("language - hindi.") 
  
    def type(self): 
        print("India is a Asian nation.") 
  
class Uk(): 
    def capital(self): 
        print("capital - london.") 
  
    def language(self): 
        print("language - English") 
  
    def type(self): 
        print("uk is a europian nation ") 
  
india_obj = India() 
uk_obj  = Uk()
for country in (india_obj, uk_obj):
    country.capital()
    country.language()
    country.type()
