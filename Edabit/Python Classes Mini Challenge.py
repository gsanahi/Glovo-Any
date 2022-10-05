import Test

# 
# CODE
# 

class Programmer:    #(Programmer)
    def __init__(self,salary,work_hours):  # (int,int) --> Programmer
        self.salary = salary
        self.work_hours = work_hours
        
    def __del__(self):
        return "oof, " + str( self.salary) + ", " + str(self.work_hours)

    
    def compare(self, other): # (Programer) --> Programer
        if  self.salary > other.salary :
            return other
        elif self.salary == other.salary :
            if self.work_hours < other.work_hours : 
                return other
        else:
            return self



# 
# FINISH CODE
# I want you to create a class called programmer. It should have a salary value, work_hours value, and a __del__(self) function. __del__(self) should 
# return "oof, " + str(salary) + ", " + str(work_hours) when the object is destroyed. salary and work_hours will be in the constructor. 
# Variables in a class are defined with self.name = value.

#Also, define a function that will compare two programmers (their salary and work_hours) and return the programmer with the lower salary. 
# If their salary is equal, then compare their work_hours, which will always be different.

#This is not really a challenge, just an introduction to Python classes.

# 
# TESTS
# 
jack = Programmer(10000, 8)
john = Programmer(50000, 5)
Test.assert_equals(jack.salary, 10000, "did you make the salary variable inside __init__?")
Test.assert_equals(jack.work_hours, 8, "did you define work_hours in __init__?")
bad = jack.compare(john)
Test.assert_equals(bad, jack, "your compare function seems wrong")
dead = bad.__del__()
Test.assert_equals(dead, "oof, 10000, 8", "your __del__ is just wrong")
# 
# FINISH TESTS
# 