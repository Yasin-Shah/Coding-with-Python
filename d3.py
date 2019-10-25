p= {'name':"Nikku", 'age':21, 'address':'indore',
'marks':{'maths':78,'phy':67,'chem':45}}

print(p)
print(p.keys())

print(p.values())

print(p.get('name'))
print(p.pop('name'))
print(p)

print(p.popitem())
print(p)

del p['age']
print(p)

#del p
p.clear()
print(p)
