class Demo:
   __name=None
   __age= None
   __AVG_AGE=None
   def __init__(self,name,age,avg=60):
      #print("This is default const")
      self.__name= name
      self.__age= age
      Demo.__AVG_AGE=avg
   def show(self):
      print("Name is "+self.__name+" Age is "+str(self.__age)+" Avg age: "+str(Demo.__AVG_AGE))
      
      
d= Demo("Rahul",34)
d1=Demo("Rohit",35)
d2= Demo("Rohan",36,65)
d.show()
d1.show()
d2.show()
