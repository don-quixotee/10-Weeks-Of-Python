# """
# while implementing inheritace with polymophism when we have child class which inherits method 
# from parent class , when the the inherited mothod from  the parent class doesnt fit well in the 
# child class and we need to modify the method , this is called polymorphism.
# when we modify the  method of a parent class in the child class (method with same name )
# """
class India:
    def intro(self):
        print("there are many big cities  in india ")
    def city(self):
        print("most of the big cities are  metro cities in india")

class States(India):
    def city(self):
        print("every state have some big city in india")

class Ut(India):
    def city(self):
        print("there are some big cities in ut as well")

ind = India()
st = States()
ut = Ut()
ind.intro()
ind.city()

print()

st.intro()
st.city()

print()

ut.intro()
ut.city()

