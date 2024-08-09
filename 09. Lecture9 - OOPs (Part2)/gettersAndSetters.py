class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # function to get value of _age 
     def getAge(self): 
         print("getter method called") 
         return self._age 
       
     # function to set value of _age 
     def setAge(self, a): 
         print("setter method called") 
         self._age = a 
  
     # function to delete _age attribute 
     def delAge(self): 
         del self._age 
     
     age = property(getAge, setAge, delAge)  
  
mark = Geeks() 
  
mark.age = 10
  
print(mark.age)