###call range
x = range(20)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))
### With 2 arguments
x = range(3, 10)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))

#### Three arguments
x = range(3, 10, 2)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))

####Ranges
for x in range(10):
  print(x) 

####Using list
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

####Slicing
r = range(10)
print(r[2])
print(r[:3])

#### Membership
r = range(0, 10, 2)
print(list(r))
print(6 in r)
print(7 in r)

####Length
r = range(0, 10, 2)
print(list(r))
print(len(r))
