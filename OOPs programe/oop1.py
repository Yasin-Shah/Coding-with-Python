class Demo:
   
   def __init__(self,name,age):
      #print("This is default const")
      self.__name= name
      self.__age= age
      
   def show(self):
      print("Name is "+self.__name+" Age is "+str(self.__age))
      
      
d= Demo("Rahul",34)
d1=Demo("Rohit",35)
d2= Demo("Rohan",36)
d.show()
d1.show()
d2.show()
