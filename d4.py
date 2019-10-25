d1= {1:45,'A':56,"Hello":'abc',True:67}
print(d1)

d1= {1:45,'A':56,"Hello":'abc','True':67}
print(d1)
d1[56]=89
print(d1)
d1[56]="Rohan"
print(d1)

# Update Method

d1={}
print(d1)
d1.update(a=89,b=45,c='qwe')
print(d1)
d1.update(a=100,b=67.90,c='abc')
print(d1)
