class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("calling method on base class")
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
        num_left_calls = 0
        def call_me(self):
            BaseClass.call_me(self)
            print("calling method on left class")
            self.num_left_calls += 1
class RightSubClass(BaseClass):
        num_right_calls = 0
        def call_me(self):
            BaseClass.call_me(self)
            print("Calling mrthod from right class")
            self.num_right_calls +=1

class SubClass(LeftSubClass, RightSubClass):
        num_sub_calls = 0
        def call_me(self):
            LeftSubClass.call_me(self)
            RightSubClass.call_me(self)
            print("calling method on Subclass")
            self.num_sub_calls +=1
s = SubClass()
s.call_me()
print(s.num_sub_calls, s.num_right_calls, s.num_left_calls, s.num_base_calls)
""" here the base class call me funtion has been called twice 'which shouldnt happen' .
such practice can create ambiguity in the program"""
