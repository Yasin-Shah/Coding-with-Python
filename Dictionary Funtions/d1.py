# Nested Dictonary
Student= [{'name':"Nikku", 'age':21, 'address':'indore',
'marks':{'maths':78,'phy':67,'chem':45}},
{'name':"Cikku", 'age':18, 'address':'bhopal',
'marks':{'maths':90,'phy':77,'chem':95}}]


for d in Student:
 for k1,v1 in d.items():
  if type(v1)==type({}):
   for k2,v2 in v1.items():
    print(k2,"---",v2)
  else:
   print(k1,"--",v1)


